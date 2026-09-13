# Simple writing outline

Use this as a checklist. It is not text to copy into the paper. Delete each TODO
after you finish it. This paper covers 2012 to 2024. Leave out the unfinished 2030
work.

## Main answer

Keep this answer the same throughout the paper:

- The model does not show a large loss of connectivity across the whole region.
- Connections changed only a little and became slightly easier overall.
- Some individual links became harder.
- Of the 45 links studied closely, 32 passed all checks. The other 13 need more
  research.
- Land with moderately high current was less protected than the rest of the land
  outside the cores. The very highest-current land was more protected.

The model shows where movement may be easier or harder. It does not prove that
cheetahs use a route. Call the lines "modelled links" or "possible corridors," not
confirmed corridors or crossings.

## Abstract

Write this last as one short paragraph.

TODO:

1. Explain why connections between cheetah areas matter.
2. State your question: how did modelled connections change from 2012 to 2024?
3. Briefly describe the work: 23 fixed cores, 1-km cells, four years, least-cost
   paths and current-flow modelling.
4. Give the main result. Across all 253 pairs, the middle change was -1.224%. A
   negative value means the connection became easier in the model. Of the 253 pairs,
   161 became easier and 92 became harder.
5. State that 32 of 45 selected links passed the checks and 13 were uncertain.
6. Give the protection result: 31.26% of available land outside the cores was
   protected, compared with 23.27% above the 80th current percentile and 44.63%
   above the 99th percentile.
7. Say the results can guide field surveys and planning but do not prove where
   cheetahs move.

Do not mention 2030, a monitoring score, confirmed pinch points or broad
connectivity loss.

## Introduction

Use four paragraphs. You do not need subsections.

### Paragraph 1: Why this matters

TODO:

- Explain that cheetah range has become smaller.
- Explain that much of the remaining range is outside protected areas.
- Explain why connections between important areas matter.
- Add sources for these facts.

### Paragraph 2: What past research is missing

TODO:

- Explain that habitat suitability and connectivity answer different questions.
- Briefly describe similar studies, including the Asiatic cheetah paper.
- Explain what your study adds: change through time for southern African cheetahs.
- Do not say nobody has done this unless your literature search proves it.

### Paragraph 3: Your approach

TODO:

- Explain that a least-cost path shows the single lowest-cost route between two
  cores.
- Explain that current flow shows several places where movement may occur.
- Explain that results depend on the resistance values, so you tested other weights.
- Explain that using the same cores every year measures landscape change, not changes
  in cheetah range.

### Paragraph 4: Your questions

TODO:

- How did modelled connectivity change from 2012 to 2024?
- Which links stayed important when model settings changed?
- How much connecting land was protected?
- Keep H1 to H3 only if your program requires hypotheses.
- End by saying the model does not prove animal movement.

## Methods

Use five subsections.

### 1. Study area and cores

TODO:

- Describe the study area, map projection and 1-km cells.
- Cite the 2010 to 2016 cheetah data used to make the cores.
- Explain the core rules: at least 0.51 cheetahs per 100 km2, touching cells joined,
  and a minimum size of 500 km2.
- State that there were 23 cores and that the same cores were used in all four years.
- Explain that the 45 links included each core's three nearest neighbors plus the
  links needed to keep the network connected.

### 2. Resistance maps

TODO:

- Make a table of every input, source, year, original cell size and whether it
  changed through time.
- Inputs that changed: built-up land, nighttime lights and vegetation.
- Inputs kept the same: roads, livestock, slope and fences.
- Protected areas were compared with results. They were not part of resistance.
- Give the main weights: human pressures 60%, vegetation 20% and slope 20%.
- Within human pressures, built-up land, roads and livestock were each 30%; lights
  were 10%.
- Explain the slope scores: low through 10 degrees, increasing from 10 to 30 degrees,
  and highest above 30 degrees.
- Explain that you tested lower and higher vegetation weights.
- Explain how fences increased resistance.
- Call the vegetation layer a measure of bare cover, not full vegetation structure.

### 3. Connectivity modelling

TODO:

- Explain how least-cost paths were made for the 45 selected links.
- Explain that current flow was calculated for all 253 possible core pairs in each
  of four years. All 1,012 runs finished successfully.
- State the Circuitscape version and main settings.
- Explain that core cells were removed from current summaries because the model
  automatically gives them very high current.
- Explain effective resistance: lower means an easier modelled connection; higher
  means a harder connection.
- Explain the link importance score: a high score means many shortest trips through
  the core network use that link.
- State that PC and dPC were not calculated.

### 4. Comparing years and protected areas

TODO:

- Explain how change from 2012 to 2024 was calculated.
- State that the cores, cell size and modelling steps stayed the same.
- Explain current percentile: how high a cell's current was compared with other
  cells outside the cores.
- Describe the August 2026 protected-area data and say proposed areas were excluded.
- State that 31.26% of land available for this comparison was protected.
- Do not give the p-value because it changed too much when the test settings changed.

### 5. Checks and uncertainty

TODO:

- Explain the three checks:
  1. Weight check: both other weight choices had to keep at least 80% of the path
     within 5 km of the main path. Thirty-four of 45 passed.
  2. Fence check: five links changed enough to be removed from the main group.
  3. Vegetation check: the direction of change had to stay the same with low, medium
     and high vegetation weights.
- State that 32 links passed all checks. The other 13 remained uncertain links.
- Explain that the separate 1-km overlap test measured route movement between years.
  Do not combine it with the 5-km weight check.
- Add software versions. Circuitscape.jl was 5.17.1. You still need ArcGIS Pro,
  Python and Julia versions.
- Add the repository and final data archive information.

## Results

Use three subsections. Report what happened here. Explain why it matters later in
the Discussion.

### 1. Change from 2012 to 2024

TODO:

- All 253 pairs: middle change -1.224%; 161 became easier and 92 became harder.
- The middle size of change was 2.822%. Ninety percent changed by no more than 6.089%.
- The 45 selected links: middle change -1.557%.
- The 32 main links: middle change -2.618%; 20 easier and 12 harder.
- Link 33 to 38 had the largest increase, about +13.1%.
- The highest 10% of current was similar among years, with agreement of 0.91 to 0.93.
- Do not call this broad connectivity loss. Overall change was small and mixed.

Figure TODO: Map current change outside the cores from 2012 to 2024.

### 2. Main and uncertain links

TODO:

- Report 32 main links and 13 uncertain links.
- Say 34 passed the weight check and 32 passed all checks.
- If you keep H3, say it was partly supported because 32 of 45 is most of the network,
  not a small group.
- Highest link importance scores: 38 to 40 (0.409), 24 to 38 (0.316), 17 to 24
  (0.300), 30 to 40 (0.238), and 27 to 41 (0.103).
- Forty-three of 45 links kept the same direction under all vegetation weights. Links
  28 to 38 and 40 to 45 did not.
- Exact routes were less stable. Forty-nine of 180 paths had less than 80% overlap
  within 1 km. This affected 21 of the 32 main links. Link 17 to 24 had no overlap
  in 2020.
- Say the importance ranking changed when the number of neighbors changed. The ranks
  are useful but not exact.

Figure TODO: Map the real 32 main paths and 13 uncertain paths in different colors.
Do not use straight lines between core centers as corridors.

Table TODO: List the 32 main links, change, importance and each check separately. Do
not make one combined score.

### 3. Protected-area coverage

TODO:

- All available land outside cores: 31.26% protected.
- Above the 80th current percentile: 23.27% protected.
- Above the 90th: 25.54%.
- Above the 95th: 33.45%.
- Above the 99th: 44.63%.
- Protection passed the 31.26% background near the 93rd percentile.
- At the 80th percentile, the protection gap grew from 7.03 percentage points in
  2012 to 7.99 points in 2024.
- The same basic pattern remained after removing land within 0, 1, 5 and 10 km of
  the cores.

Figure TODO: Make a line graph of protected-area coverage at each current percentile.

## Discussion

Use four subsections.

### 1. What the change means

TODO:

- Explain that a small overall change can hide larger changes on individual links.
- Discuss link 33 to 38 as the clearest increase.
- Do not say one input caused the change. This analysis did not test cause and effect.
- Explain that cost can stay similar even when the exact route moves.

### 2. Protected areas and management

TODO:

- Explain that moderately high-current land was less protected.
- Explain that the very highest-current land was more protected.
- Discuss work with private, communal and other land managers outside protected areas.
- Do not simply say connectivity is unprotected.

### 3. Where fieldwork is needed

TODO:

- Explain that the 32 main links passed the checks you completed.
- Explain that the 13 uncertain links are useful places for more research.
- Use link 17 to 24 as an example. It is important to the network, but its route moved.
- Suggest telemetry, cameras or field checks. Do not claim you made a full monitoring
  plan or ranked survey sites.

### 4. Comparison with other studies

TODO:

- Compare your approach with the Asiatic cheetah and southern African studies.
- Explain which methods are similar.
- Explain that resistance values from another species or place cannot simply be copied.
- State that a 1-km regional model finds broad areas for attention. It cannot choose
  an exact place for a fence opening or other action.

## Limitations

Use four paragraphs instead of many small sections.

### Paragraph 1: What the model shows

TODO: Explain that the cores came from older data and stayed fixed. The model shows
possible connections, not real movement. Missing records do not prove absence. You
did not have independent movement data to test the model.

### Paragraph 2: Resistance-map limits

TODO: Explain that resistance scores came from past research and expert reasoning.
Roads, livestock and fences did not change through time. Rainfall was not included.
Vegetation mostly measured bare cover. The nighttime-lights version changed in 2024.

### Paragraph 3: Map and network limits

TODO: Explain that you tested one core map and one 1-km cell size. Exact routes changed
more than their costs. Link importance changed when the number of neighbors changed.
Data quality also differed among countries.

### Paragraph 4: Work not completed

TODO: State that you did not complete future forecasts, other core maps, other cell
sizes, PC/dPC, a monitoring score or a fine-scale corridor study.

## Conclusion

Write one short paragraph.

TODO:

1. Connectivity changed little overall and became slightly easier on average.
2. Some links became harder and still deserve attention.
3. Work outside protected areas is important for connecting cores.
4. The 32 main links and 13 uncertain links can guide planning and field research,
   but they are not confirmed cheetah routes.

## Figures and tables

1. Study-area map with 23 cores and four broad groups.
2. Current-change map outside the cores, 2012 to 2024.
3. Map of 32 main paths and 13 uncertain paths.
4. Graph of protected-area coverage across current percentiles.
5. Table of model inputs and data sources.
6. Table of the 32 main links and each check.
7. Put full 45-link results and extra checks in the supplement.

## Final check

Remove any sentence saying:

- connectivity declined across the whole region;
- the lines show real cheetah movement;
- the model found confirmed pinch points or crossings;
- the 2030 forecast was completed;
- a monitoring score was completed;
- other core maps or cell sizes were tested;
- one pressure caused a change;
- connectivity was calculated separately for each country.
