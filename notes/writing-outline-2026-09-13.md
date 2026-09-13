# Manuscript writing outline

This is a writing checklist, not manuscript prose. Delete each TODO as it is
completed. The main paper covers 2012--2024 only. Do not include the exploratory
2030 scenarios.

## Central answer to keep consistent throughout

TODO: Express this in Liam's own words in the Abstract, Results, Discussion and
Conclusion:

- Modelled connectivity did not decline broadly between 2012 and 2024.
- Effective resistance changed little overall and decreased slightly on balance.
- Deterioration was localized to a minority of links.
- Thirty-two links passed the final robustness screen; thirteen are uncertainty
  priorities rather than failed or unimportant links.
- Moderately high-current connecting landscape was less protected than the
  outside-core background, while the most concentrated current was more protected.

Claim boundary: these are modelled structural connections and candidate priority
areas. They are not observed cheetah movements, verified crossings or demonstrated
gene flow.

## Abstract: one paragraph, approximately 200--250 words

TODO: Write one or two sentences for each item:

1. Context: range contraction and the importance of connectivity outside protected
   areas.
2. Question: how potential structural connectivity among fixed cheetah cores changed
   from 2012 to 2024, and which links were robust to tested assumptions.
3. Methods: 23 fixed cores, 1-km resistance surfaces, four time points, least-cost
   paths, pairwise current flow and link-level robustness screens.
4. Headline result: all 253 pairs had a median effective-resistance change of -1.224%;
   161 decreased and 92 increased.
5. Priority result: 32 of 45 selected links were primary and 13 were retained as
   uncertainty priorities.
6. Protection result: outside-core protected-area coverage was 31.26% in the
   background, 23.27% above the 80th current percentile, and 44.63% above the 99th.
7. Boundary and implication: results identify model-based priorities for targeted
   field assessment, not confirmed movement corridors.

Do not mention 2030, a monitoring index, observed connectivity loss or validated
pinch points.

## Introduction: four paragraphs, no subsections needed

### Paragraph 1: conservation problem

TODO:

- Establish cheetah range contraction and the large proportion of range outside
  formal protected areas.
- Explain why connections among remaining areas matter.
- Cite the regional range assessment and protected/unprotected-land literature.

### Paragraph 2: knowledge gap

TODO:

- Distinguish habitat suitability from connectivity.
- Summarize the closest southern African connectivity studies.
- Explain that cheetah-specific regional temporal connectivity change remains poorly
  described.
- Avoid claiming that no previous study exists unless the literature search supports
  that absolute statement.

### Paragraph 3: analytical approach

TODO:

- Briefly contrast least-cost paths with circuit theory.
- Explain why resistance assumptions require sensitivity checks.
- State that fixed historical cores isolate landscape-side change; they do not show
  changes in cheetah distribution.

### Paragraph 4: objectives and expectations

TODO:

- Objective 1: measure 2012--2024 change among fixed cores.
- Objective 2: identify influential links that remain usable across tested resistance,
  fence and vegetation assumptions.
- Objective 3: describe protected-area coverage of outside-core current.
- Keep H1--H3 only if hypotheses are required by the capstone format. If retained,
  align them with these three objectives and evaluate them honestly in Results.
- End with the structural-connectivity claim boundary.

## Methods: five subsections

### 1. Study design, extent and cores

TODO:

- Describe the southern African extent, projection and 1-km grid.
- Cite the 2010--2016 source dataset used to derive cores.
- State the threshold: density >=0.51 cheetahs per 100 km2, contiguous eight-neighbor
  patches, minimum area 500 km2.
- Report 23 fixed cores and explain why they were held constant across 2012, 2016,
  2020 and 2024.
- Explain that 45 selected links were the union of the k=3 nearest-neighbor graph and
  the minimum spanning tree.

### 2. Resistance surfaces

TODO:

- Provide a source/year/resolution/static-or-dynamic table for every covariate.
- Dynamic inputs: built-up fraction, nighttime lights and vegetation continuous
  fields.
- Static inputs: roads, livestock, terrain/slope and fences. Protected areas are an
  overlay, not a resistance input.
- State the final weights: anthropogenic 0.60, vegetation 0.20, terrain 0.20.
- Within anthropogenic resistance: built 0.30, roads 0.30, livestock 0.30, lights
  0.10.
- Describe the slope transformation: <=10 degrees low resistance, 10--30 degrees
  increasing linearly, >=30 degrees capped, then scaled 1--10.
- Describe vegetation-low, balanced and high weights as sensitivity assumptions.
- Explain the documented finite fence multiplier and its 1--25 range.
- Describe vegetation as a bare-cover proxy, not a complete vegetation-structure
  model.

### 3. Connectivity and network metrics

TODO:

- Explain least-cost path calculation for the 45 selected links.
- Explain pairwise Circuitscape: 23 focal regions, 253 pairs per year, four years,
  1,012 completed solves, eight-neighbor connectivity, double precision and CG+AMG.
- State that current summaries exclude core cells because focal regions accumulate
  high current by construction.
- Define effective resistance as the primary temporal measure and least-cost path cost
  as secondary.
- Explain unweighted edge betweenness and its normalization by 253 core pairs.
- State that PC/dPC and dispersal-kernel metrics were not calculated.

### 4. Temporal and protected-area comparisons

TODO:

- Define absolute and percentage change from 2012 to 2024.
- State that cores, grid and modelling procedure were held constant.
- Explain outside-core current percentile ranks.
- Describe the August 2026 protected-area layer: polygons only, terrestrial/coastal,
  proposed areas excluded and features dissolved.
- Explain comparison of PA coverage across current percentiles with the 31.26%
  eligible outside-core background.
- Do not report the unstable permutation p-value.

### 5. Robustness, uncertainty and reproducibility

TODO:

- Define all three link-level gates separately:
  1. Weight test: both alternatives retain at least 80% of the route within 5 km;
     34 of 45 pass.
  2. Fence test: five affected links are removed by the final screen.
  3. Vegetation test: the sign of 2012--2024 change must agree across low, balanced
     and high vegetation weights.
- Report the final result: 32 primary links and 13 uncertainty links.
- Explain the separate 1-km temporal route-overlap diagnostic; do not merge it with
  the 5-km weight test.
- Record software versions. Known: Circuitscape.jl 5.17.1. Still fill in ArcGIS Pro,
  Python and Julia versions.
- State repository/archive locations and redistribution restrictions.

## Results: four subsections

Keep interpretation out of this section. Report numbers, directions and locations.

### 1. Overall connectivity change

TODO: Report:

- All 253 pairs: median effective-resistance change -1.224%; 161 decreased and 92
  increased; median absolute change 2.822%; 90th percentile absolute change 6.089%.
- Forty-five selected links: median change -1.557%.
- Thirty-two primary links: median change -2.618%; 20 decreased and 12 increased.
- Largest increase: link 33--38, approximately +13.1%.
- Outside-core current was spatially similar among years: top-decile agreement
  approximately 0.91--0.93.
- Describe the result as mixed and close to stable overall, not regional connectivity
  loss.

Figure TODO: Map 2012--2024 percentage change in current outside cores, with a bounded
color scale so extremes do not wash out the map.

### 2. Priority links and model sensitivity

TODO: Report:

- 32 primary links and 13 uncertainty links.
- 34 of 45 pass the weight test; the full three-gate screen leaves 32.
- H3 is only partly supported because 32 of 45 is a majority, not a small subset.
- Highest final corrected betweenness links: 38--40 (0.409), 24--38 (0.316), 17--24
  (0.300), 30--40 (0.238), and 27--41 (0.103).
- Vegetation direction agrees for 43 of 45 links; 28--38 and 40--45 do not.
- Cost direction is comparatively stable, but route location is not: 49 of 180
  route-years fall below 80% overlap within 1 km, involving 21 of the 32 primary
  links. Link 17--24 has zero overlap in 2020.
- Graph construction matters: k=2/3/4/5 produces 31/45/61/77 edges, and only k=3
  makes 17--24 a bridge.

Figure TODO: Map the real 32 primary path geometries and 13 uncertainty path
geometries with different symbols. Do not use straight centroid links.

Table TODO: List the 32 primary links with betweenness, change, and each robustness
flag. Keep the fields separate; do not create a composite score.

### 3. Protected-area coverage

TODO: Report the outside-core values:

- Eligible background: 31.26% protected.
- Above 80th current percentile: 23.27%.
- Above 90th: 25.54%.
- Above 95th: 33.45%.
- Above 99th: 44.63%.
- Coverage crosses the background near the 93rd percentile.
- At the 80th percentile, the gap widens from -7.03 percentage points in 2012 to
  -7.99 in 2024.
- Direction is stable after excluding 0, 1, 5 and 10 km around cores.

Figure TODO: Use a coverage-versus-current-percentile curve. This communicates the
result better than a single protected-area map.

### 4. Evidence limitations relevant to the results

TODO: Keep this brief or move it to the supplement:

- The occurrence consistency screen is not independent because the same 2010--2016
  archive helped define the cores.
- There are no comparable occurrence records for 2020 or 2024.
- Therefore, do not call the model empirically validated.

## Discussion: four subsections

### 1. Main interpretation

TODO:

- Explain why small average change can coexist with important localized increases.
- Discuss link 33--38 as the clearest increase without claiming a causal driver.
- Relate stable current patterns and unstable exact path locations.

### 2. Protection and management implications

TODO:

- Explain the non-linear PA result: moderately high-flow connecting areas are least
  protected, while the most concentrated tail overlaps PAs more strongly.
- Discuss cooperation with private, communal and other non-PA land managers.
- Avoid saying simply that "connectivity is unprotected."

### 3. Robust links and survey priorities

TODO:

- Explain that primary links are supported by the tested assumptions.
- Treat the 13 uncertainty links as places where field data could change management
  conclusions.
- Use 17--24 as the main example: structurally influential but spatially unstable.
- Suggest targeted telemetry, camera surveys or ground verification without claiming
  that the study designed or ranked a field-monitoring program.

### 4. Comparison with other connectivity research

TODO:

- Compare the framework with the Asiatic cheetah, elephant and multispecies studies.
- Explain which methods transfer and why species-specific resistance values do not.
- State that the 1-km regional model is for strategic screening, not fine-scale route
  placement.

## Limitations: combine into four paragraphs

### Paragraph 1: biological interpretation

TODO: Combine fixed historical cores, structural-versus-functional connectivity,
sampling bias and lack of independent movement validation.

### Paragraph 2: resistance and temporal inputs

TODO: Combine expert-assigned resistance, static roads/livestock/fences, rainfall not
modelled, vegetation acting mainly as a bare-cover proxy, and the VIIRS version change.

### Paragraph 3: spatial and network sensitivity

TODO: Combine one core definition, one 1-km resolution, graph k sensitivity, route
location instability, outside-core current masking and uneven mapping completeness.

### Paragraph 4: scope

TODO: State that climate forecasts, conflict, occupancy, functional connectivity,
future scenarios, PC/dPC, fine-scale corridor delineation and the planned MCDA are
outside the completed analysis.

## Conclusion: one short paragraph

TODO: Write four sentences:

1. Overall 2012--2024 connectivity changed little and slightly improved on balance.
2. Localized deterioration and structurally influential links still create management
   priorities.
3. The PA pattern makes the broader connecting landscape, not only the highest-current
   cells, important for cross-boundary conservation.
4. The 32 primary and 13 uncertainty links provide a transparent basis for management
   screening and targeted field assessment, not confirmed corridors.

## Final figure and table set

Keep the main paper compact:

1. Figure: study area, 23 fixed cores and four descriptive nuclei.
2. Figure: outside-core current change, 2012--2024.
3. Figure: 32 primary and 13 uncertainty path geometries.
4. Figure: protected-area coverage across current percentiles.
5. Table: covariates, sources, years, resolution and temporal treatment.
6. Table: 32 primary links and their separate evidence fields.
7. Supplement: complete 45-link results, sensitivity diagnostics and workflow details.

## Final prohibited-claim check

Before considering a section complete, search for and fix any statement implying:

- broad regional connectivity decline;
- observed or validated cheetah movement;
- confirmed pinch points or crossings;
- a completed 2030 forecast;
- a completed monitoring index or MCDA;
- tested alternative core definitions or spatial resolutions;
- causal attribution of connectivity change to one pressure;
- country-level connectivity results that were not calculated.
