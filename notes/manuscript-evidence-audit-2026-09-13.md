# Manuscript-to-analysis audit

Audit date: 13 September 2026

This audit compares the current manuscript repo against the analysis handoff,
the committed report/QC records in `cheetah-connectivity`, and the actual
outputs described in `notes/reconciliation-2026-09-09.md`. It is an audit only:
the manuscript files were not rewritten.

## Bottom line

The paper is writeable, but the Introduction needs to be narrowed before prose
is finalized. The strongest defensible paper is:

> A temporally comparative, scenario-based assessment of structural
> connectivity among fixed cheetah core areas in southern Africa, identifying
> broad priority linkages and separating connection-cost stability from route-
> location uncertainty.

The paper should not currently promise:

- a completed three-scenario 2030 forecast;
- a ranked list of monitoring cells;
- a general finding that connectivity declined;
- independent validation of the model;
- a resolution-robust conclusion across 1, 2, and 5 km;
- a single definitive corridor line.

## Introduction audit

### Opening paragraph

Current wording says the study provides a predictive look at future land
permeability under three scenarios and concludes that cheetahs are at risk of
further range contraction and isolation due to anthropogenic development.

**Status: revise substantially.** The 2030 work is incomplete: the high-
development scenario has only 6 of 45 links available, and the future VCF
fractions are physically inconsistent in the high-development inputs. The final
temporal results do not show broad connectivity loss: effective resistance fell
slightly on balance and directions were mixed.

**Safe replacement idea:** introduce the study as a retrospective 2012--2024
comparison with fixed historical cores, then state that resistance scenarios
were used to evaluate uncertainty. Remove the 2030 forecast from the opening
unless it is completed and independently QC-checked.

Also replace “the core range is not expected to change” with “the core areas
were held fixed as a modeling assumption.” The data do not support a forecast
about future range location.

### Gap paragraph

Current wording says the objective is to identify pinch points among areas of
suitable habitat on unprotected lands and that the study assesses connectivity
among usable habitat.

**Status: revise.** The model uses fixed density-derived core polygons and
structural resistance. It does not establish habitat suitability, functional
use, or observed movement. “Pinch point” should mean a location of concentrated
modeled current or a link-level bottleneck, not a confirmed movement bottleneck.

The novelty statement should be narrowed to: “Few studies have quantified
temporal change in modeled structural connectivity among southern African
cheetah core areas.” Do not imply that cheetah connectivity modeling itself is
new. Moqanaki and Cushman modeled Asiatic-cheetah connectivity in Iran using
500 m resistance layers, resistant kernels, and factorial least-cost paths.[^1]

### Methodological-frame paragraph

The description of least-cost and circuit-theoretic connectivity is broadly
accurate. The description of the two sensitivity axes also matches the
implemented vegetation and anthropogenic weighting work.

**Status: keep with two corrections.**

1. Say “model scenarios” rather than implying that the implemented scenarios
   are identical to protocol IDs RES-01 to RES-06. The reconciliation note says
   those IDs were never instantiated as such.
2. Define “robust” using the actual implemented gates. The 80% rule was route
   overlap within 5 km, not the predeclared cell-level k/n agreement rule.

The sentence “a link is only described as robust here if it survives them” is
usable after the gates are stated precisely.

### Objectives and hypotheses

#### Objective 1

“Measure changes in modeled structural connectivity among fixed-range cores
across four time points” is supported. Keep it.

#### Objective 2

“Determine pinch points that remain influential across the entire sensitivity
grid and describe their protected-area status” is only partly supported.

What exists is a link-level robust/uncertain screen, current concentration
summaries outside cores, and protected-area coverage by current percentile. A
cell-level pinch-point agreement grid was not produced.

**Recommended wording:** “identify core-to-core linkages that remain important
across tested resistance assumptions and characterize the protection context of
the connecting landscape.”

#### Objective 3

“Produce and stress-test a ranked list of monitoring priorities” is not
supported as written. The planned cell-level MCDA and W1-W3 monitoring index
were not built.

**Recommended wording:** “produce a link-level screening of robust priorities
and uncertainty-driven survey priorities.”

#### H1

The revised H1 is valid and falsifiable. The actual result is non-support:
change was mixed and not concentrated on the highest-betweenness links.

Keep H1, but write the Results and Discussion around the null outcome rather
than around “connectivity loss.”

#### H2

The current H2 predicts high-value connectivity is disproportionately outside
protected areas. That is too broad. Outside the cores, protection is lowest in
the moderately high-current connecting landscape, but the highest-current tail
becomes more protected and crosses background near the 93rd percentile.

**Recommended revision:** “Protection is lower than background across much of
the moderately high-current connecting landscape, but the relationship changes
in the extreme high-current tail.”

#### H3

The “limited subset” prediction is not a good description of the result because
32 of 45 links passed the implemented primary screen. Call this partially
supported: most selected links were cost-robust under tested scenarios, while a
smaller uncertainty set remained spatially or fence sensitive.

#### H4

There is no result for the planned highest-priority monitoring cells. Either
rewrite H4 around link-level robust/uncertain screening or explicitly report it
as not tested. Do not retain language implying stable monitoring cells.

## Methods audit

### Scale and cores

Supported:

- 1 km working grain;
- Africa Albers equal-area projection;
- 23 fixed cores;
- four temporal snapshots;
- fixed historical core baseline.

Needs correction:

- The 45 links were not produced by one nearest-neighbor link per core. They
  came from the union of a 3-nearest-neighbor graph and a minimum spanning tree.
- The planned 2 km and 5 km resolution checks were not run. Move any claim that
  conclusions are resolution-robust into Limitations.

### Covariates

The methods should distinguish temporal signal from spatial signal:

- Dynamic: GHSL built-up, VIIRS radiance, MODIS VCF.
- Static: roads, livestock, fences, terrain, hydrography, protected areas, and
  fixed cores.

The current manuscript says static covariates “provide context” in a way that
could imply they were excluded from resistance. They were included in the
resistance surface, but they contribute no temporal change. Rewrite that
sentence.

### Resistance model

The final model specification is:

```text
R_final,t = (0.60 anthropogenic_t + 0.20 vegetation_t + 0.20 terrain) × fence_t
```

Within anthropogenic pressure:

```text
0.30 built-up + 0.30 roads + 0.30 livestock + 0.10 night lights
```

The terrain transform is based on mean slope, with resistance 1 below 10
degrees, a linear increase from 10 to 30 degrees, and a cap at 30 degrees.
Maximum slope was retained for sensitivity/context, not used in the primary
surface.

The manuscript must state that the implemented scenario set diverged from the
predeclared RES-01 to RES-06 labels. The reconciliation note says the actual
work included three vegetation-weight scenarios, three anthropogenic-weight
models, and fence variants.

### Connectivity modeling

The committed QC receipt supports the following claims:

- Circuitscape.jl pairwise mode;
- 253 undirected core pairs per year;
- 4 years and 1,012 total solves;
- 8-neighbor raster connectivity;
- CG+AMG solver and double precision;
- zero logged failures.

The manuscript should explain that the 45 selected links are the priority-
screening subset, while all 253 pairs were solved for the current-flow stage.

Current values are reported outside the core domain because focal cores carry
the highest current by construction. Say that masking removes the forced core
concentration from the reported summaries but does not change the underlying
pairwise solve.

### Network structure

The manuscript should state that betweenness was unweighted hop-count
betweenness on the k=3 graph. The ranking depends on graph construction: k=2,
3, 4, and 5 yield 31, 45, 61, and 77 edges, respectively. A single k=3 rank
should therefore be described as conditional, with rank ranges or a graph-
sensitivity caveat.

PC and dPC were not computed. Do not promise them in the Introduction or
Methods. The reconciliation note recommends dropping them because they require
an unsupported dispersal-distance assumption.

### Independent plausibility assessment

The existing occurrence consistency screen is not independent because the same
2010--2016 archive contributed to the core definition. No post-2016 occurrence
check exists. Either run the predeclared external Limpopo/Namibia check or
rename this section “Occurrence consistency screen” and state the circularity.

Never call this validation.

## Results audit

The current Results file is an outline, not a safe final Results section. Its
numbers are mostly present in the TODO text, but several captions and figure
labels are wrong.

Supported numbers available in the committed evidence package:

- All 253 pairs: median effective-resistance change about -1.224%; 92 increased
  and 161 decreased.
- Selected 45 links: median change about -1.557%.
- Primary 32 links: median change about -2.618%; 12 increased and 20 decreased.
- 32 of 45 links passed the final primary screen; 13 remained uncertainty links.
- 49 of 180 route-years fell below the 1 km directional-overlap review trigger.
- The outside-core protected-area curve bottoms near 23% around the 80th
  current percentile and crosses the 31.26% background near the 93rd percentile.

Results that should not be written as currently framed:

- “Connectivity declined” as a general result. Use “changed little on balance,
  with mixed directions.”
- A ranked list of monitoring cells. It does not exist.
- Per-country connectivity change. The available country table describes
  covariate change, not connectivity change.
- An ensemble agreement map. No cell-level agreement raster was produced.
- Protected-area p-values from the old null. The reconciliation note says the
  result changes with block size and the old comparison included fixed cores.

## Figures and tables that need correction

### Figure 1

The current caption calls it ensemble agreement, but the file is a 2024 high-
current concentration map. Rename the figure or replace the file.

### Figure 2

The current figure is effectively near-uniform because it shows the fixed-core
footprint. It should be remade from outside-core current change or described as
such. Do not use it as evidence of a changing corridor network until the domain
is corrected.

### Figure 3

The current figure draws straight centroid-to-centroid selection links, not
least-cost routes. It must be replaced with the actual route geometries before
calling it a corridor or priority-link figure.

### Figure 4

The strongest version is a protected-area coverage-versus-current-percentile
curve, not the current map. Report the outside-core domain and the background
coverage line.

### Tables

- Use the newer manuscript-results-package priority table, not the superseded
  top-20 table.
- There are 32 primary links, not 20.
- Do not include a country-attribution column unless it is built.
- Do not include an agreement-score column unless a cell-level agreement metric
  is produced.
- Replace the planned composite monitoring-index table with a link-level
  decision table, or remove it.

## Discussion and conclusion audit

The Discussion headings currently overstate the evidence. In particular,
“Where permeability has declined” should become something like “Where modeled
permeability changed and what co-occurred,” because the temporal result is mixed
and slightly lower resistance on balance.

The protection discussion should distinguish the moderately high-current
connecting landscape from the extreme high-current tail. Do not write that
connectivity as a whole is unprotected.

The monitoring discussion should be about 32 robust links and 13 uncertainty or
survey-priority links. Pair 17–24 is a strong example because it is the only
bridge in the k=3 graph and has very unstable route location. Do not call this
an index.

The Limitations section is correctly aimed at the major risks, but each TODO
must be turned into prose. The highest-priority limitations are fixed cores,
structural rather than functional interpretation, expert-assigned resistance,
missing rainfall, one core definition/one resolution, route-location
uncertainty, current masking outside cores, and the VIIRS/GHSL comparability
issues.

## Recommended writing order

1. Revise the Introduction to remove 2030 forecasting, cell-level monitoring,
   and broad connectivity-loss claims.
2. Finish Methods with the actual resistance formula, k=3 graph construction,
   pairwise Circuitscape design, and the real robustness gates.
3. Replace Results figure captions and stale figure labels before writing prose.
4. Draft Results from the committed results package, choosing effective
   resistance as the primary temporal metric and least-cost cost as secondary.
5. Write Limitations before Discussion so the claim boundary stays visible.
6. Write Discussion and Conclusion from the supported findings only.
7. Leave the 500 m terrain pilot in a sensitivity/supplementary section.

## Source files checked

- [Manuscript Introduction](../cheetah-connectivity-manuscript/tex/sections/01_introduction.tex)
- [Manuscript Methods](../cheetah-connectivity-manuscript/tex/sections/02_methods.tex)
- [Manuscript Results](../cheetah-connectivity-manuscript/tex/sections/03_results.tex)
- [Manuscript Limitations](../cheetah-connectivity-manuscript/tex/sections/05_limitations.tex)
- [Reconciliation and analysis audit](../cheetah-connectivity-manuscript/notes/reconciliation-2026-09-09.md)
- [Current-flow QC receipt](https://github.com/liamcrettol/cheetah-connectivity/blob/main/analysis/reports/final_pairwise_current_flow_qc_20260909_071026.json)

## External methodological comparison

Moqanaki and Cushman used a 500 m common raster grain, 90 m DEM-derived slope,
an inverted Gaussian terrain response, resistant-kernel analysis, and factorial
least-cost paths. Their paper is a methodological precedent, not a template
that requires your study to reproduce every component. Your regional 1 km
model can remain a macro structural-connectivity analysis if its grain and claim
boundary are stated clearly.[^1]

[^1]: Moqanaki, E. M., and S. A. Cushman. “All roads lead to Iran: Predicting landscape connectivity of the last stronghold for the critically endangered Asiatic cheetah.” *Animal Conservation* (2016). [USDA-hosted PDF](https://www.fs.usda.gov/rm/pubs_journals/2016/rmrs_2016_moqanaki_e001.pdf).
