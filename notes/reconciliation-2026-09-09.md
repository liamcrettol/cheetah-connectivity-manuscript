# Reconciliation: protocol vs analysis vs manuscript

Working note, 9 September 2026. Audit of `cheetah-connectivity` (analysis) against
`protocol/protocol.tex` (locked 18 Aug, tag `protocol-v1.0`) and `tex/sections/`.
Not manuscript prose. Every number below is traceable to a file named in the row.

Revised 9 September after the Astra evidence audit, which ran read-only
diagnostics on the rasters themselves and found a problem upstream of most of
what is recorded here. Corrections are marked inline.

---

## 0. Corrections from the Astra audit

**The high-current maps select input cores, not corridors.** Every cell in the
top 10%, 5% and 1% of positive final current is inside an input core, in all four
years. Independently corroborated here by area arithmetic: the 23 cores total
246,654 km2, which is 9.85% of the 2,503,870-cell valid domain, while the
top-decile selection is 233,812 cells, or 9.34% of the domain. The top decile
fits inside the core footprint with room to spare.

Mechanism: each focal region participates in 22 of 253 pairwise experiments, and
22/253 = 0.08696, against a reported 90th-percentile positive current of 0.08702.
Core cells sit on a plateau created by focal-node current injection.

This invalidates two things reported in sections 1 and 2 below as if they were
landscape findings:

1. **The protected-area result.** The 35.47 / 27.62 / 33.90 percent figures
   describe protected-area coverage of core cells, not of connecting landscape.
   Recomputed on the outside-core domain (see
   `resistances/` in the analysis repo), against a matched background of
   **31.26%**:

   | Percentile of current | 2012 | 2024 |
   |---|---:|---:|
   | 80th (minimum) | 24.23% | 23.27% |
   | 90th | 26.31% | 25.54% |
   | 95th | 35.57% | 33.45% |
   | 99th | 44.17% | 44.63% |

   Coverage is lowest at the **80th percentile**, not the top, crosses background
   at about the **93rd**, and the gap **widened** over the study period, from
   -7.03 to -7.99 points at the 80th. Direction is stable under 0/1/5/10 km core
   buffers.

   **So H2 is supported for the broad connecting landscape and reverses only in
   the most concentrated tail.** The earlier reading in this note, that H2 was
   refuted, was wrong. It was reading core geography.

   Note the background: 31.26% is coverage across the outside-core
   *positive-current* domain, which is the population the selection is drawn
   from. The Astra audit used 30.13%, which includes 165,765 zero-current cells
   that could never be selected, so it understates the gap slightly.

   Do not quote a p-value. Under a block null the top-decile gap gives p = 0.006
   at 25 km blocks and p = 0.096 at 50 km. Significance here is mostly a function
   of the assumed autocorrelation scale, which the original uniform null hid by
   returning 0.001 everywhere.

2. **The temporal stationarity of current.** The near-identical 90th percentile
   and high-current cell counts across 2012 to 2024 are stationarity of the fixed
   core geometry, not evidence that the corridor network held steady. Outside
   cores, the 2012/2024 top-decile Jaccard overlap is 91.19%, which is the
   defensible version of that statement and is still conditional on fixed cores.

The Circuitscape solves are fine. This is an output-domain and interpretation
problem, not a failed model run. Note also that
`set_focal_node_currents_to_zero` is documented as not implemented in
Circuitscape 5 (installed version 5.17.1), so this is not fixable by a config
flag; it needs post-hoc masking of the core domain with the changed domain
reported.

**Two further Astra findings not caught here.** The vegetation transform reduces
to `V = 1 + 0.09 x bare` whenever the three VCF fractions sum to 100, so swapping
tree for non-tree cover at fixed bare cover changes nothing; it is a bare-cover
proxy, not a vegetation-structure model. And the 2030 scenario vegetation
fractions are clipped independently, so their sums are not preserved: maxima of
151.5% and 194% against a historical range of 98 to 102%. The 2030 inputs are
physically inconsistent, which matters more than the incomplete run recorded
below.

**One disagreement worth recording.** Section 7 below lists "compute dPC" as an
option. Astra argues against adding PC/dPC because it would import dispersal
assumptions this evidence cannot calibrate. That is the better call. The
protocol's own lock note concedes the 100 km value comes from hub spacing rather
than a dispersal study, and no cheetah natal-dispersal telemetry exists for this
system. Amend and drop rather than compute.

**Synthesis point across both audits.** CHIRPS precipitation was never acquired
(section 3 below). Combined with the vegetation function collapsing to bare
cover, and with the vegetation term dominating the 2030 mean resistance change,
this means a substantial share of the project's temporal signal is bare-cover
fraction in a semi-arid system with no rainfall covariate. Bare cover there is
strongly rainfall-driven. Some of what is currently described as landscape change
may be interannual rainfall variability.

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

### Current surfaces are effectively stationary (SUPERSEDED, see section 0)

The table below measures the fixed core footprint, not the corridor network.
Retained for provenance.


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

### Protected areas (SUPERSEDED, see section 0)

The bands below are core cells. Use Astra's outside-core recomputation instead:
top decile 25.54% protected vs 30.13% background, top percentile 44.63%.
Retained for provenance.

WDPA August 2026, terrestrial and coastal polygons, status not Proposed,
dissolved. 2,301 polygons in extent. 748,864 of 2,503,870 valid model cells
protected = **29.91%**. Null is 999 hypergeometric draws, seed 20260909. 2024 only.

| Band | Protected | Null mean | Difference | p |
|---|---|---|---|---|
| 95th-99th pct | 35.47% | 29.90% | +5.57 pp | 0.001 (upper) |
| >= 99th pct | 27.62% | 29.91% | -2.29 pp | 0.001 (lower) |
| >= 95th pct | 33.90% | 29.91% | +4.00 pp | 0.001 (upper) |

p = 0.001 is the floor of (0+1)/(999+1), not an exact value.

Do not read H2 from this table. It describes core cells. See section 0.

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

## 7. Graph and route sensitivity (from the Astra audit)

**The priority ranking depends on the neighbour rule.** Rebuilding the graph at
k = 2, 3, 4, 5 on the existing core centroids gives 31, 45, 61 and 77 edges. The
k=3 graph used here has exactly one bridge, 17-24. The k=4 and k=5 graphs have no
bridge at all and their leading betweenness edges differ substantially. So
"robust priority links" is conditional on k=3, and that condition is currently
unstated. Testing this needs no new solves.

**Restricting the graph to the 32 eligible links isolates core 1.** The shortlist
is not a complete network-maintenance plan.

**Route location is much less stable than route cost.** 49 of 180 route-years
fell below 80% bidirectional overlap at 1 km in the VCF comparison, covering 29
pairs in at least one year, including 21 of the 32 supposedly eligible pairs.
Pair 17-24 recorded a 2020 overlap of zero. The single graph bridge is also the
most geographically unstable link in the set.

Note the two overlap rules are not the same test: the weight screen used 80%
within 5 km, the VCF comparison used 80% bidirectional at 1 km. Do not report
them as one robustness criterion.

This separation is a genuine result rather than a defect. Confidence that two
regions are cheaply connected is not confidence in where the line runs, and a
spatially uncertain link is a good survey target.

---

## 8. Decisions needed

Reordered after the Astra audit. The first item now gates almost everything else.

1. **Recompute every current-derived result outside the core domain.** The PA
   comparison, the temporal persistence claim, and the high-current figures all
   currently describe core geography. Post-hoc masking with the changed domain
   stated, since the Circuitscape 5 focal-current option is not implemented.
   No solver run required.
2. **Which temporal metric is primary**, Circuitscape effective resistance or LCP
   path cost. Sets every number in Results section 1.
3. **State the graph condition, and report rank ranges across k** rather than one
   ranking from k=3. Cheap, and it changes what "robust" can mean.
4. **Split robustness into separate reported fields**: connection-cost stability,
   route-location stability, fence uncertainty, data coverage. Stop collapsing
   them into one eligibility flag.
5. **2030 scenarios**: fix the cover-closure problem (fractions summing to 194%)
   and finish high_development, or cut the forecasting scope and remove it from
   the Introduction. Renaming does not repair the inputs.
6. **H4 / monitoring**: amend O3 to the link-level decision table rather than
   building the MCDA. A weighted composite adds false precision here.
7. **Network metrics**: drop PC/dPC and amend, per section 0. Decide separately
   whether to recompute betweenness with effective-distance weights.
8. **Plausibility assessment**: run the Limpopo route, or rename what exists and
   state that the predeclared independent check was not performed.
9. **Resolution sensitivity**: run 2 km and 5 km, or amend and move the claim in
   the scale subsection into Limitations.
10. **Scenario naming**: map the implemented set onto RES IDs or declare the
    divergence, and fix `\nscen`.

---

## 9. Citations to add

Neither `.bib` file currently has these, and three of them are load-bearing.

- **Weise et al. 2017**, PeerJ 5:e4096. The range and density source. Currently
  `\TODO{find citation}` in Methods.
- **Moqanaki & Cushman 2017**, Animal Conservation. Prior cheetah connectivity
  modelling (Asiatic cheetah, Iran). Rules out any "first connectivity study"
  novelty claim in the Introduction.
- **Mills, Broomhall & du Toit 2004**, Wildlife Biology 10:177-186. Cheetah
  habitat use is context-dependent, not open-grassland-only. Relevant to the
  unsourced terrain-affinity claim in the resistance subsection.
- **McRae et al. 2012**, PLOS ONE 7:e52604. Barrier detection and restoration
  benefit, if the intervention framing is kept.
