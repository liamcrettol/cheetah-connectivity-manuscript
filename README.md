# Cheetah connectivity manuscript

The manuscript, predeclared analysis protocol, and bibliography for a study
of temporal structural connectivity, unprotected pinch points, and monitoring
priorities for free-ranging cheetahs in southern Africa. This is the
canonical home for the paper and connects to Overleaf via GitHub sync.

The analysis itself, ArcGIS project, decision log, and processing scripts,
lives in a separate repo:
[cheetah-connectivity](https://github.com/liamcrettol/cheetah-connectivity).
That repo carries a full ArcGIS geodatabase and Git LFS binaries that
Overleaf's GitHub integration can't handle, which is why the two are split.

## Layout

    tex/          manuscript (main.tex + sections/)
    protocol/     predeclared analysis protocol, landcover_crosswalk.csv,
                  temporal_alignment.csv
    refs/         bibliography (methods_canon.bib verified; cheetah_lit.bib)
    .github/      CI: builds both PDFs on every push

## Building

    make            # both PDFs
    make watch      # continuous rebuild while writing
    make clean

Requires TeX Live with biblatex-apa and biber, or open in a Codespace, the
devcontainer supplies both. Overleaf compiles independently of this.

## Protocol lock

The protocol is fixed before any connectivity result is generated. When it is
signed, tag it:

    git tag -a protocol-v1.0 -m "protocol locked"
    git push origin protocol-v1.0

Amendments after that point go in the protocol's amendment log AND get their
own commit, so the sequence of changes is externally checkable.

Note: an earlier protocol-v1.0 tag from before this repo split exists on
cheetah-connectivity, dated 18 August 2026. It remains the authoritative
record of that lock date. Any future re-lock or amendment tag belongs here
instead, since this is now where protocol.tex lives.
