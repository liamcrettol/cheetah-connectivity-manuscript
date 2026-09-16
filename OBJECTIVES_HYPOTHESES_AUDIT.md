# Objectives and hypotheses audit

This is an internal writing aid, not manuscript prose. It compares the locked protocol
with the analyses that were actually completed.

## Objectives

| Original item | What happened | Status for the paper |
|---|---|---|
| O1: measure modeled connectivity change among fixed cores from 2012 to 2024 | Completed for 23 fixed cores across four snapshots. Overall effective-resistance change was small. | Completed |
| O2: identify robust pinch points and describe their protected-area status | Narrowed to 45 selected links, 32 main links, 13 uncertain links, and protected-area coverage of high-current areas. The full core-definition and resolution grid was not run, and exact biological pinch points were not demonstrated. | Partly completed after a disclosed change |
| O3: create and stress-test a ranked monitoring map | The planned 10-km cell index and three weighting tests were not built. A link-level main/uncertain classification was produced instead. | Not completed; replaced by a simpler output |

## Hypotheses

| Hypothesis | Evidence from the completed analysis | Audit conclusion |
|---|---|---|
| H1: losses would be limited to a minority of links and concentrated on high-betweenness links | Of the 45 selected links, 18 became harder and 27 became easier. A descriptive rank check between cost change and baseline betweenness was approximately zero ($\rho = 0.014$). | Mixed. The minority condition matched; the betweenness condition did not. Do not call H1 supported. |
| H2: high-current land would be disproportionately outside protected areas and the result would hold across thresholds | In 2024, protected coverage was below the 31.26% background at the 80th and 90th percentiles, but above it at the 95th and 99th percentiles. The permutation result depended on spatial block size. | Not supported under the full locked rule. Report a threshold-dependent descriptive pattern, not a dependable significance result. |
| H3: only a limited subset of links would remain important across assumptions | The completed screens retained 32 of 45 links as main priorities and 13 as uncertain. The full planned core-definition and resolution grid was not completed. | Partly evaluated and not supported as written. Most selected links were retained, not a limited subset. |
| H4: the top monitoring cells would combine network importance, stale or sparse evidence, and rapid change | The cell-level monitoring index and its three weighting tests were not built. | Not tested. The 13 uncertain links can guide future surveys, but they are not an H4 result. |

## Evidence used for this audit

- `final_effective_resistance_change_2012_2024_20260909_073544.csv`
- `conservation_link_importance_betweenness.csv`
- `table_pa_coverage.tex` and its archived source tables
- `full_weight_sensitivity_summary.csv`
- `conservation_link_evidence_integrated.csv`
- `h1_betweenness_change_audit.json`
- the locked `protocol/protocol.tex` at commit
  `d7de8675a074dfbffc0c7c856bb5645e1e13867d`

The H1 rank value is a descriptive Spearman correlation obtained by joining the 45
selected-link rows on their core-pair IDs. The calculation is archived in
`analysis/scripts/audit_h1_betweenness_change.py` in the connectivity repository.
