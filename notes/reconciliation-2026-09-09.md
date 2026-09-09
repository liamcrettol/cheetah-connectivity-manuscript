# Reconciliation: protocol vs analysis vs manuscript

Working note, 9 September 2026. Audit of `cheetah-connectivity` (analysis) against
`protocol/protocol.tex` (locked 18 Aug, tag `protocol-v1.0`) and `tex/sections/`.
Not manuscript prose. Every number below is traceable to a file named in the row.

---

## 1. What was actually run

### Cores

Source is the Weise et al. 2017 Dryad **density** raster
`cheetahsouthernafricadensity.tif`, not the distribution/evidence raster.

| Parameter | Value | Source |
|---|---|---|
| Density threshold | stored value >= 51, i.e. 0.51 cheetahs per 100 km2 | `finalize_primary_cheetah_cores.py` |
| Contiguity | eight-neighbour | same |
| Minimum patch | 500 km2 | same |
| Cores retained | **23** | `primary_cheetah_cores.csv` |
| Core area range | 506 to 99,673 km2 | same |

Core IDs are non-contiguous region-group codes: 1, 9, 13, 17, 18, 24, 26, 27, 28,
30, 31, 32, 33, 36, 38, 40, 41, 42, 43, 45, 49, 50, 53.

Only **one** core definition was carried forward.

### Link network

Union of an undirected 3-nearest-neighbour graph on core centroids and the
minimum spanning tree (`create_core_neighbor_network.py`, `K_NEIGHBORS=3`).

| Link type | Count |
|---|---|
| KNN only | 23 |
| KNN + MST | 22 |
| MST bridge only | 0 |
| **Total selected links** | **45** |

All 253 undirected pairs among 23 cores were solved in Circuitscape; the 45 are
the selected subset used for least-cost path work and priority screening.

### Final resistance model

`resistance_final_balanced_fence_documented_YEAR = resistance_temporal_veg_balanced_YEAR x fence_multiplier_main_kruger_documented_1km`

| Component | Weight |
|---|---|
| Anthropogenic pressure (built, roads, livestock index, flare-masked VIIRS lights; lights sub-weight 0.10) | 0.60 |
| Vegetation structure | 0.20 |
| Terrain (mean slope rescaled 1 to 10) | 0.20 |

Vegetation transform: `1 + 9 * mean(VCF bare, 100 - min(100, tree + nontree)) / 100`

Fence multiplier is finite, range 1.0 to 25.0, cell-wise maximum of KAZA and
documented Kruger cells. Final resistance range approx 1.009 to 106-110 by year.
Source: `final_balanced_fence_resistance_register_20260908_080959.csv`,
`temporal_vegetation_sensitivity_register.csv`.

Sensitivity scenarios actually built: veg_low (0.7/0.1/0.2), veg_balanced
(0.6/0.2/0.2), veg_high (0.4/0.4/0.2), plus three anthropogenic weighting models
(primary, equal, infrastructure-emphasis) and the fence variants.

### Circuitscape

Completed 2026-09-08 13:00:23. Pairwise, 23 focal regions, 253 pairs per year,
4 years = 1,012 solves. CG+AMG, double precision, 8-neighbour. Grid 2310 x 2200
at 1 km. Zero failures, all `pair_253_logged: true`.
Source: `final_pairwise_current_flow_qc_20260909_071026.json`.

Note: the QC records `wkid: 0`, so the CRS is not stamped in the Circuitscape
output rasters. Worth confirming before claiming ESRI:102022 end to end.

### Temporal change, two different metrics

**Circuitscape effective resistance, 2012 to 2024**
(`final_effective_resistance_change_2012_2024_20260909_073544.csv`)

| Set | n | Median | Median abs | Range | Inc / Dec |
|---|---|---|---|---|---|
| All pairs | 253 | -1.224% | 2.822% (p90 6.089%) | | 92 / 161 |
| Selected links | 45 | -1.557% | 5.183% | -8.243 to +13.119 | 18 / 27 |
| Primary-priority links | 32 | -2.618% | | | 12 / 20 |

**Least-cost path cost, 2012 to 2024, 45 selected links**
(`temporal_vegetation_scenario_agreement.csv`)

| Scenario | Median | Median abs | Range | Inc / Dec |
|---|---|---|---|---|
| veg_low | -1.207% | 3.568% | -7.791 to +9.246 | 16 / 29 |
| veg_balanced | -3.448% | 6.272% | -13.786 to +18.629 | 17 / 28 |
| veg_high | -5.136% | 9.281% | -23.194 to +35.419 | 15 / 30 |

Direction consistent across all three vegetation weights: **43 of 45**.

These two metrics disagree in magnitude for the same links (e.g. link 1-9:
Circuitscape +10.97%, veg_balanced LCP +18.63%). The paper has to name one as
primary and label the other.

### Current surfaces are effectively stationary

(`manuscript_results_package/table_current_temporal_evidence_20260909_084224.csv`)

| Year | 90th pct positive current | Cells above | Common support |
|---|---|---|---|
| 2012 | 0.08702686 | 233,813 | 2,503,870 |
| 2016 | 0.08702077 | 233,815 | 2,503,870 |
| 2020 | 0.08702215 | 233,815 | 2,503,870 |
| 2024 | 0.08702298 | 233,812 | 2,503,870 |

Three cells of variation across twelve years.

### Robustness as implemented

Link-level, three gates, all must pass:

1. **weight_robust** — both alternative weightings produce a route with >= 80% of
   its length within 5 km of the primary route
   (`summarize_full_weight_sensitivity.py`). 90 comparisons (45 links x 2
   alternatives): 79 ROBUST, 11 WEIGHT_SENSITIVE, so **34 of 45** links pass.
2. **fence_robust** — link not destabilised by the fence scenarios. Five links
   affected: 1-13, 1-17, 9-13, 13-17, 27-30.
3. **vegetation_direction_robust** — same sign of 2012-2024 change under veg
   low/balanced/high. Two links fail: 28-38, 40-45 (both already excluded).

Final: **32 primary-priority, 13 uncertainty**. The 34-vs-32 gap that the review
note flags is exactly the two weight-robust links that the fence screen removes.

### Betweenness

Unweighted (hop-count) Brandes edge betweenness on the 45-edge graph, normalised
by 253 undirected pairs after a 21/23 correction to the original 231 denominator.
Edge weights (effective distances) are **not** used.

Top five: 38-40 (0.409), 24-38 (0.316), 17-24 (0.300), 30-40 (0.238), 27-41 (0.103).

### Protected areas

WDPA August 2026, terrestrial and coastal polygons, status not Proposed,
dissolved. 2,301 polygons in extent. 748,864 of 2,503,870 valid model cells
protected = **29.91%**. Null is 999 hypergeometric draws, seed 20260909. 2024 only.

| Band | Protected | Null mean | Difference | p |
|---|---|---|---|---|
| 95th-99th pct | 35.47% | 29.90% | +5.57 pp | 0.001 (upper) |
| >= 99th pct | 27.62% | 29.91% | -2.29 pp | 0.001 (lower) |
| >= 95th pct | 33.90% | 29.91% | +4.00 pp | 0.001 (upper) |

p = 0.001 is the floor of (0+1)/(999+1), not an exact value.

**H2 is refuted for the high-current band.** High-value modelled connectivity is
more protected than chance, not less. Only the narrow >= 99th tail runs the other
way, and it does so by 2.3 points.

### Occurrence consistency screen

Early 2010-2012: 5,395 records, 47 sources, 413 thinned 10 km cells.
Late 2013-2016: 7,062 records, 61 sources, 450 cells. Jaccard 0.239.

| Test | Result |
|---|---|
| 2016 resistance, late vs early | medians 2.279 vs 2.126, Cliff's d = 0.115, p = 0.0035 (Bonf. 0.0105) |
| Inside fixed cores | 67.8% vs 45.8%, OR 0.401, p = 8e-11 |
| Within 10 km of robust priority path | 0/413 vs 3/450, p = 0.25 |

The archive that produced these records also produced the cores, so this is not
independent. No post-2016 records exist, so 2020 and 2024 have no check at all.

### 2030 scenarios

low_growth 45/45, continuation 45/45, **high_development 6/45**. The three-scenario
comparison is incomplete and cannot be reported as one.

---

## 2. Divergences from the locked protocol

Each needs either a rerun or an amendment-log entry in protocol section 19.

| # | Protocol says | Analysis did | Severity |
|---|---|---|---|
| 1 | Cores C1/C2/C3 from evidence-category raster, min areas 2000/1000/500 km2 | One definition, density raster, >= 0.51/100 km2, min 500 km2 | High: changes the data product and drops a whole sensitivity axis |
| 2 | 144 runs: 6 scenarios x 3 core defs x 4 snapshots at 1 km, plus 2 km and 5 km for first and last snapshot | One core definition, 1 km only, no resolution sensitivity | High: the resolution claim in Methods section on scale is unsupported |
| 3 | Robust = cell in top decile of current in >= 80% of runs | Link-level route overlap >= 80% within 5 km, plus fence and vegetation gates | High: same "80%", entirely different construct. No agreement raster exists |
| 4 | RES-01 to RES-06 from the workbook register, RES-04 illustrative, RES-06 composite gHM | Never instantiated. Actual set is 3 anthropogenic weightings + 3 vegetation weightings + fence variants | Medium: needs a mapping table or a plain statement |
| 5 | PC and dPC in Conefor, dispersal 100 km with 50/200/400 sensitivity, betweenness on effective-distance-weighted graph | No PC, no dPC, no Conefor, dispersal parameter unused, betweenness unweighted | High: O2 and part of H1 rest on this |
| 6 | PA denominator = modelled network (top quartile of current); null = 999 configuration permutations preserving patch geometry; thresholds top 5/10/20% | Denominator = full valid grid; null = uniform hypergeometric; bands 95-99/>=99/>=95 pct; 2024 only | High: this is the H2 test |
| 7 | Plausibility check on Limpopo tracking (9 individuals) and Namibia camera-trap, both external to core definition | Occurrence-consistency screen on the same archive that built the cores | High: the predeclared independent check was not done |
| 8 | Six-component MCDA at 10 km cells, weight sets W1-W3, Spearman and Jaccard stability | Not built | High: O3 and H4 have no result |
| 9 | Study locked 18 Aug | 2030 forecasting scenarios added after, one incomplete | Medium: scope expansion post-lock |

---

## 3. Data-quality items that belong in Limitations

- **VIIRS product version changes mid-series.** V21 through 2020, V22 for 2024
  (`temporal_alignment.csv`). The protocol required pinning one collection
  version. Lights carry the smallest sub-weight (0.10), which limits the damage,
  but it is a genuine temporal-comparability break.
- **GHSL offsets sit at the tolerance limit.** 2010 for the 2012 snapshot is -2
  years, exactly the maximum tolerated offset. 2025 for 2024 is +1.
- **CHIRPS precipitation was never acquired** (`temporal_alignment.csv`: "deferred
  diagnostic, not yet acquired"). Vegetation carries 0.20 of the final resistance
  weight and most of the temporal signal, and there is no rainfall covariate, so
  VCF change cannot be separated from interannual rainfall variability.
- **The vegetation proxy averages two near-inverse measures.** VCF tree vs bare
  Spearman = -0.877, nontree vs bare = -0.836
  (`predictor_spearman_correlation.csv`). `mean(bare, 100 - tree - nontree)` is
  close to one measure counted twice, not two independent signals.
- **Livestock cattle and goats correlate at 0.774**, flagged REVIEW in
  `predictor_redundancy_review.csv`.
- **All-zero VCF triplets**: 174,975 cells, 96.7% in persistent water-class
  context, mostly Makgadikgadi. Retained at a finite midpoint score of 5.5/10
  rather than treated as barrier or NoData. Documented decision, needs stating.
- **Route geometry is less stable than route cost**: 49 of 180 route-years fell
  below the 80% directional-overlap review trigger.
- **Zimbabwe lights show a max of 652.7** in both 2020-2024 and 2012-2024
  (`country_absolute_change_summary.csv`), well above every other country. Worth
  confirming the flare mask caught everything.
- **No core-to-country attribution exists.** The country summary covers eight
  countries because of the 100 km buffer (NAM, ZAF, ZMB, AGO, BWA, ZWE, MOZ, SWZ)
  and reports covariate change, not connectivity change. Results asks for
  per-country connectivity reporting; that table does not exist yet.

---

## 4. Manuscript content that is now wrong

- `02_methods.tex`, connectivity outline block: "Circuitscape current-flow stage
  not yet run". It ran on 8 September and passed QC.
- `02_methods.tex`, temporal outline block: median robust-link change approx
  -0.002%, largest increase 0.349%, no link >= 1%. That is the anthropogenic-only
  model. The final model gives numbers two to three orders of magnitude larger.
  If this survives into prose it is actively misleading.
- `02_methods.tex`, range cores: "calculated the Euclidean distance to the nearest
  neighbor. This yielded 45 straight-line links". 23 cores with one nearest
  neighbour each cannot give 45. It is k=3 nearest neighbours unioned with the MST.
- `02_methods.tex`, robustness: orphaned fragment "I considered a res".
- `02_methods.tex`: "23 cores and 45 links" appears in both the study-area and
  range-cores subsections.
- `03_results.tex`: `\label{fig:agreement}` points at
  `Figure_1_high_current_concentration_2024.png` with the caption "Ensemble
  agreement across the sensitivity grid". No agreement figure exists and no
  agreement raster was produced.
- `main.tex`: `\nscen` is "five". The implemented scenario count depends on how
  you count and is not five under any obvious reading.
- `00_abstract.tex` and `01_introduction.tex`: the framing assumes a
  protected-area gap. The result is the opposite for the high-current band.
- Range-envelope citation is still `\TODO{find citation}`. It is Weise et al.
  2017, and it is in neither `.bib` file.

---

## 5. Figures

Four exist: high-current concentration 2024, temporal current evidence, robust
priority links, protected-area context.

Problems common to all four: no legend, no scale bar, no north arrow, no CRS
note, and the frame crops the analysis extent so the 100 km buffer and the buffer
countries are not visible. Core symbology differs between figures (black, blue,
pale pink), so they do not read as a set despite
`apply_unified_paper_palette.py` existing.

Specific:

- **Figure 3** draws straight centroid-to-centroid lines, not least-cost paths.
  The generating script says so explicitly: "Straight lines select pairs only;
  they are not corridors." For a connectivity paper this is the single most
  misreadable figure in the set.
- **Figure 2** is near-uniform, which is honest given the current surfaces barely
  move, but it does not communicate anything and it is not panelled by year.

---

## 6. Conflicting result tables

`paper_table_top20_connectivity_priorities.csv` and
`manuscript_results_package/table_primary_priority_links_20260909_084224.csv`
both rank the priority links, and they disagree.

| | top20 table | results package |
|---|---|---|
| Betweenness, link 38-40 | 0.44805 | 0.40909 (corrected by 21/23) |
| Change metric | LCP cost, veg_balanced | Circuitscape effective resistance |
| Link 38-40 change | +2.625% | +4.783% |
| Link 24-38 change | +4.120% | +7.439% |

Ranks agree; values do not. The results package is newer and its README says to
use it as the source of numerical values. The top20 table should be treated as
superseded or deleted so it cannot be cited by accident.

---

## 7. Decisions needed

Ordered by how much downstream writing they unblock.

1. **Which temporal metric is primary**, Circuitscape effective resistance or
   LCP path cost. Sets every number in Results section 1.
2. **H2**: report the refutation as the finding, or rerun the PA test to the
   predeclared spec (network denominator, configuration null) and see whether the
   sign changes. Protocol section on decision rules already says what to do if H2
   is not significant.
3. **H4 / monitoring**: build the MCDA, or amend O3 to a link-level robust vs
   uncertain split and say so.
4. **Network metrics**: compute dPC, or drop to betweenness-only and amend.
   If dropping, note the betweenness is unweighted and decide whether to
   recompute it with effective-distance weights.
5. **Plausibility assessment**: run the Limpopo route, or rename what exists and
   state that the predeclared independent check was not performed.
6. **Resolution sensitivity**: run 2 km and 5 km, or amend and move the claim in
   the scale subsection into Limitations.
7. **2030 scenarios**: finish high_development, or cut the forecasting scope
   entirely and remove it from the Introduction.
8. **Scenario naming**: map the implemented set onto RES IDs or declare the
   divergence, and fix `\nscen`.
