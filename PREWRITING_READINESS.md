# Prewriting readiness scaffold

## Ready

- [x] Main map figures selected and inserted.
- [x] Figures 5 and 6 removed from the manuscript as requested.
- [x] Main result-table stubs populated from saved CSV outputs.
- [x] Protected-area table replaced with outside-core coverage values and no unstable permutation p-value.
- [x] Data-source acronyms and KNN/MST labels defined in their corresponding tables.
- [x] ArcGIS Pro, Python, Julia, and Circuitscape versions verified.
- [x] GitHub Actions manuscript build passing before this readiness commit.
- [x] Weise et al. range citation connected to the Methods.
- [x] WDPA release month and DOI recorded.
- [x] Table-source CSVs archived under `tex/tables/source_data/`.
- [x] Results consolidated into four substantive subsections.
- [x] Objectives and hypotheses traced against the locked protocol and completed analyses.

## TODO — decisions to make before writing sentences

- [ ] TODO: Explain that Git marks the protocol as version 1.0 even though the saved document still says “0.1 draft.”
- [ ] TODO: Count and name the scenarios that were actually completed; do not use the old five-scenario wording. The list is now in the `\nscen` macro in `main.tex`: a main surface plus 8 alternatives in three groups.
- [ ] TODO: Decide whether the conditional 2030 scenarios belong in Results or the Supplement. Do not call them forecasts. Suggestion: Supplement, because they were not in the protocol. Note their rows were renamed on 5 Oct 2026 (see the table's TODO for why).
- [x] Independent plausibility check completed 5 Oct 2026 against the Limpopo tracking data (protocol steps 23.1–23.5). New table `table_limpopo_plausibility.tex`. Writing guides are in Methods, Results, and Discussion.
- [x] Stricter tracking follow-ups done 5 Oct 2026: step check with the animal as the unit (main result: 0.56, 95% interval 0.51–0.61, 7 of 9 animals), layer breakdown (roads carry most of it, vegetation alone leans slightly the wrong way), all nine surfaces (0.55–0.56), road crossings (26% of real moves against 35% of alternatives). The current lean did not hold up in the step check. Fences cannot be tested: none are mapped near the tracks. New table `table_limpopo_steps.tex`.
- [ ] TODO: Add one standard step-selection reference to the bib (Methods step 6) and one road-avoidance source for the Discussion.
- [ ] TODO: Call the same-archive occurrence comparison the weaker, non-independent check, presented after the tracking check.
- [ ] TODO: Decide whether to request the Namibia camera-trap data (Verschueren et al. 2024) or state that it was not obtained.

## Added 5 October 2026: fixes found in review

These came out of a full read of the paper against the protocol and the analysis outputs. Each one has a TODO in the section where it lives.

- [ ] TODO: Introduction hypotheses do not match the H1–H4 that Results judge. The protected-area one predicts the opposite of H2, the link-stability one is circular, and H4 is missing. Locked wording is in the intro TODO.
- [ ] TODO: Methods says each core joined its single nearest neighbor; it was three nearest neighbors plus a minimum spanning tree.
- [ ] TODO: Methods describes slope wrong. The code is a straight ramp from 10 to 30 degrees, flat is easiest, and there is no 15 percent sweet spot.
- [ ] TODO: Say the weights, slope ramp, and fence multiplier were your choices informed by literature, not fitted. Limitations sentence 3 was corrected to match.
- [ ] TODO: Appendix A1 needs four more change items: a main surface was chosen, when the weights were set, PC/dPC dropped, one core definition instead of three.
- [ ] TODO: Give the real reason PC/dPC was dropped. "No telemetry" was already handled by protocol decision 4.
- [ ] TODO: Explain the 0.51 cheetahs per 100 km² core cutoff and whether a minimum core size was used.
- [ ] TODO: Abstract checklist at the top of `00_abstract.tex` (fixed cores missing, two banned phrases, "predictive," mixed denominators).
- [ ] TODO: Covariates table should say which layers went into resistance, and add land cover and protected areas.
- [ ] TODO: Rainfall (CHIRPS) was never checked. Say so in the alignment table or in Limitations.
- [ ] TODO: Explain that the planned cell-level monitoring score was replaced by a table of 32 main-priority and 13 uncertain links.
- [ ] TODO: Revise the objectives paragraph so it reports the narrowed Objective 2 and the uncompleted original Objective 3.
- [ ] TODO: Report H1 as mixed, H2 as unsupported under its full rule, H3 as partly evaluated and not supported as written, and H4 as not tested.
- [ ] TODO: Decide whether to show the full 32-link table in the Supplement while keeping the top ten in the main text.
- [ ] TODO: Confirm department name, advisor acknowledgement, and archive/DOI destination.

## TODO — drafting order

1. [ ] TODO: Methods — write only from the factual blocks already embedded in `02_methods.tex`.
2. [ ] TODO: Results — use `tex/tables/source_data/`; keep interpretation out of this section.
3. [ ] TODO: Limitations — write one paragraph of no more than four sentences from the existing prompt.
4. [ ] TODO: Discussion — interpret effective-resistance stability separately from route-location instability.
5. [ ] TODO: Introduction — complete citation integration and revise the final objectives paragraph.
6. [ ] TODO: Conclusion — three or four bounded sentences.
7. [ ] TODO: Abstract — write last and keep the fixed historical cores in sentence two.

## TODO — simple wording rules

- [ ] TODO: Use “modeled structural connectivity,” “modeled current,” and “modeled priority links.”
- [ ] TODO: Do not use “observed movement,” “validated corridor,” “functional connectivity,” or “pinch point” as a biological finding.
- [ ] TODO: Use effective resistance as the main measure of change. Explain it as the total modeled difficulty of connection between two cores.
- [ ] TODO: Explain that static layers affect where resistance is located but cannot create change between years.
- [ ] TODO: Describe future results as “what could happen under these assumptions,” not as predictions of what will happen.
