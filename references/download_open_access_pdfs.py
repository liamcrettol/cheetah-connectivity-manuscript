"""Build the manuscript reference index and download lawful open-access PDFs.

The script reads every BibTeX entry in refs/, checks OpenAlex for an open copy,
and downloads only URLs that return a real PDF. Restricted publisher PDFs are
not bypassed or redistributed.
"""

from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote
from urllib.request import Request, urlopen
import csv
import json
import re
import time


REPO = Path(__file__).resolve().parents[1]
BIB_DIR = REPO / "refs"
OUT_DIR = REPO / "references"
PDF_DIR = OUT_DIR / "pdfs"
INDEX_CSV = OUT_DIR / "reference_index.csv"
INDEX_MD = OUT_DIR / "README.md"
PDF_DIR.mkdir(parents=True, exist_ok=True)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) cheetah-connectivity-reference-index/1.0"

# Stable, lawful open copies for important project references.
KNOWN_OPEN_PDFS = {
    "moqanaki2017iran": "https://www.fs.usda.gov/rm/pubs_journals/2016/rmrs_2016_moqanaki_e001.pdf",
    "weise2017distribution": "https://europepmc.org/articles/PMC5729830?pdf=render",
    "dimbleby2024rewilding": "https://www.frontiersin.org/journals/conservation-science/articles/10.3389/fcosc.2024.1351366/pdf",
    "melzheimer2020hubs": "https://europepmc.org/articles/PMC7776775?pdf=render",
}


def bib_entries(text):
    starts = list(re.finditer(r"(?m)^@(\w+)\{([^,]+),", text))
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        block = text[match.start() : end]
        fields = {}
        for field in ["title", "author", "year", "journal", "school", "doi", "url"]:
            found = re.search(rf"(?ims)^\s*{field}\s*=\s*\{{(.*?)\}}\s*,?\s*$", block)
            fields[field] = " ".join(found.group(1).split()) if found else ""
        yield {
            "key": match.group(2).strip(),
            "type": match.group(1).lower(),
            **fields,
        }


def safe_name(value):
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("_")
    return cleaned[:120]


def get_json(url):
    request = Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urlopen(request, timeout=30) as response:
        return json.load(response)


def openalex_record(doi):
    if not doi:
        return None
    url = "https://api.openalex.org/works/https://doi.org/" + quote(doi, safe="")
    try:
        return get_json(url)
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError):
        return None


def candidate_pdf(record):
    if not record:
        return "", "", ""
    locations = []
    if record.get("best_oa_location"):
        locations.append(record["best_oa_location"])
    if record.get("primary_location"):
        locations.append(record["primary_location"])
    locations.extend(record.get("locations") or [])
    seen = set()
    for location in locations:
        if not location:
            continue
        pdf_url = location.get("pdf_url") or ""
        if not pdf_url or pdf_url in seen:
            continue
        seen.add(pdf_url)
        if location.get("is_oa") is False:
            continue
        license_name = location.get("license") or ""
        landing = location.get("landing_page_url") or ""
        return pdf_url, license_name, landing
    return "", "", ""


def download_pdf(url, target):
    url = quote(url, safe=":/?&=%#")
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/pdf,application/octet-stream;q=0.9,*/*;q=0.1",
        },
    )
    try:
        with urlopen(request, timeout=60) as response:
            data = response.read()
    except (HTTPError, URLError, TimeoutError) as exc:
        return False, f"download failed: {type(exc).__name__}"
    if not data.startswith(b"%PDF"):
        return False, "link did not return a PDF"
    target.write_bytes(data)
    return True, "downloaded open-access PDF"


entries = []
for bib_file in sorted(BIB_DIR.glob("*.bib")):
    for entry in bib_entries(bib_file.read_text(encoding="utf-8-sig")):
        entry["bib_file"] = bib_file.name
        entries.append(entry)

rows = []
for number, entry in enumerate(entries, start=1):
    doi = entry["doi"].strip()
    doi_url = f"https://doi.org/{doi}" if doi else ""
    record = openalex_record(doi)
    pdf_url, license_name, landing = candidate_pdf(record)
    if entry["key"] in KNOWN_OPEN_PDFS:
        pdf_url = KNOWN_OPEN_PDFS[entry["key"]]
        landing = doi_url or landing
        license_name = license_name or "public repository/open publisher copy"
    local_file = ""
    status = "no open PDF located"
    note = "Use the DOI or source link to check library access."
    if pdf_url:
        filename = safe_name(f"{entry['key']}_{entry['year']}") + ".pdf"
        target = PDF_DIR / filename
        if target.exists() and target.read_bytes()[:4] == b"%PDF":
            ok, message = True, "already downloaded"
        else:
            ok, message = download_pdf(pdf_url, target)
        if ok:
            local_file = str(target.relative_to(REPO)).replace("\\", "/")
            status = "downloaded open-access PDF"
            note = message
        else:
            status = "open PDF link found but download failed"
            note = message
    source_url = landing or entry["url"] or doi_url
    rows.append(
        {
            "key": entry["key"],
            "year": entry["year"],
            "title": entry["title"],
            "source": entry["journal"] or entry["school"],
            "doi": doi,
            "doi_url": doi_url,
            "source_url": source_url,
            "pdf_url": pdf_url,
            "local_file": local_file,
            "status": status,
            "license_or_oa_note": license_name,
            "note": note,
            "bib_file": entry["bib_file"],
        }
    )
    print(f"[{number:02d}/{len(entries):02d}] {entry['key']}: {status}")
    time.sleep(0.1)

with INDEX_CSV.open("w", encoding="utf-8-sig", newline="") as stream:
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)

downloaded = [row for row in rows if row["local_file"]]
not_downloaded = [row for row in rows if not row["local_file"]]
lines = [
    "# Reference library",
    "",
    f"This folder indexes all {len(rows)} BibTeX references in `refs/`.",
    f"Open-access PDFs downloaded: {len(downloaded)}.",
    f"Entries without a downloaded PDF: {len(not_downloaded)}.",
    "",
    "Only open publisher or public-repository copies are stored here. A missing PDF",
    "does not mean the reference is unavailable. Follow its DOI or source link and use",
    "library access if needed. `reference_index.csv` contains the full link and status",
    "record.",
    "",
    "## Downloaded PDFs",
    "",
]
for row in downloaded:
    readme_path = row["local_file"].removeprefix("references/")
    lines.append(f"- `{row['key']}`: [{row['title']}]({readme_path})")
lines.extend(["", "## No PDF stored", ""])
for row in not_downloaded:
    link = row["source_url"] or row["doi_url"]
    if link:
        lines.append(f"- `{row['key']}`: [{row['title']}]({link}) - {row['status']}")
    else:
        lines.append(f"- `{row['key']}`: {row['title']} - {row['status']}")
lines.extend(
    [
        "",
        "## Refreshing the library",
        "",
        "Run `python references/download_open_access_pdfs.py` from the repository root.",
        "The script checks every BibTeX entry again and keeps existing valid PDFs.",
        "",
    ]
)
INDEX_MD.write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote {INDEX_CSV}")
print(f"Wrote {INDEX_MD}")
