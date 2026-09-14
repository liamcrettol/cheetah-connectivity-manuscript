# Cheetah connectivity paper-writing packet

## Recommended study framing

**Working claim:** This study evaluates temporally comparative, scenario-based
structural connectivity among fixed cheetah core areas. The modeled linkages
are decision-support outputs, not observed movement routes.

**Primary spatial scale:** 1 km regional raster grain.

**Optional local diagnostic:** 500 m terrain-aware pilot for link 31–32. It is
not part of the primary regional model.

## Research questions

1. How does modeled structural connectivity among the fixed core areas vary
   across the four landscape snapshots?
2. Which core-to-core linkages are consistently prioritized across scenarios?
3. How sensitive are priority linkages to resistance assumptions, especially
   terrain and vegetation?
4. Where do priority linkages intersect roads, fences, or other management
   features?

## Study design and data

- Historical core baseline: 23 fixed core polygons.
- Primary selected network: 45 neighboring core pairs.
- Temporal snapshots: 2012, 2016, 2020, and 2024.
- Anthropogenic pressure components: built-up pressure, roads, livestock,
  and flare-masked night lights.
- Vegetation structure: VCF tree, non-tree, and bare-cover fractions.
- Terrain: SRTM-derived slope summarized to the 1 km model grid.
- Fences: finite/crossable fence multiplier scenario, where the documented
  final surface is available.
- Water and NoData treatment must be reported from the final model register;
  do not describe NoData or VCF-zero cells as permanent water barriers unless
  the final QC explicitly supports that statement.

## Primary resistance equation

For year `t`, the unfenced balanced resistance is:

```text
R_unfenced,t = 0.60 A_t + 0.20 V_t + 0.20 T
```

Anthropogenic pressure is:

```text
A_t = 0.30 built_t + 0.30 roads + 0.30 livestock + 0.10 lights_t
```

Vegetation resistance is based on the sparse/bare-cover proxy derived from
VCF tree, non-tree, and bare fractions. Terrain resistance is transformed to
the 1–10 range from mean slope. The documented final scenario is:

```text
R_final,t = R_unfenced,t × fence_multiplier_t
```

Use the exact final resistance register for the manuscript’s final formula
and layer names. The local reconstruction used for diagnostic testing is not
a substitute for that register.

## Connectivity analysis

Describe the primary result as broad-scale connectivity among fixed cores.
The repository documentation indicates a selected 45-pair least-cost network
and a planned/recorded pairwise current-flow analysis across 253 undirected
core pairs per year. Before reporting current-flow results, verify that the
completed output set is present and QC-passed.

Report:

- all source/destination definitions;
- raster grain, projection, neighborhood rule, and cost normalization;
- how pairwise results were aggregated into priority links;
- how temporal consistency and scenario robustness were assessed.

## Terrain sensitivity evidence already available

For core pair 31–32:

- Saved path length: 64.73 km.
- 30 m native-terrain diagnostic: 63.78 km; 100% within 5 km of saved path.
- 1 km-grid p90-slope sensitivity: 66.38 km; 100% within 1 km of saved path;
  cost increased 14.6% relative to the reconstructed mean-slope baseline.
- 500 m local pilot: 66.51 km; 92.9% within 1 km and 100% within 5 km of the
  saved path.

Interpretation: terrain changes the exact line and cost, especially around
steep or dissected terrain, but the broader 31–32 corridor remains stable.
Present these as sensitivity evidence, not as a replacement regional model.

## Approved candidate nuclei for optional local work

- Northwest: cores 1, 9, 13, 17, 18, 24
- Central: cores 28, 30, 33, 36, 38, 40, 42, 43, 45, 41
- Southern: cores 49, 50, 53
- Eastern: cores 26, 27, 31, 32

These groupings are approved analysis strata for future management-scale
zoom-ins. They are not required for the macro paper.

## Sensitivity and uncertainty language

Use “sensitivity analysis” for alternate resistance parameterizations and
“spatial uncertainty” for route displacement. Do not treat a route-overlap
threshold as a biological cutoff. The repository handoff reports that route
geometry can be less stable than optimized cost, so discuss alternative routes
as uncertainty rather than automatically rejecting a priority link.

## Figures to prepare

1. Study area, 23 cores, and regional macro network.
2. Resistance-model workflow and component weights.
3. Four temporal resistance or connectivity summaries.
4. Priority-link map with roads, fences, and major management barriers.
5. Terrain sensitivity example for link 31–32: saved path, p90 1 km path,
   and optional 500 m diagnostic path.
6. Optional four-nucleus map for the management-scale discussion.

## Tables to prepare

1. Data sources, years, native resolutions, transformations, and model roles.
2. Resistance components, weights, and parameter ranges.
3. Core-pair priority-link register across years/scenarios.
4. Sensitivity summary: cost change, route overlap, and temporal stability.
5. Road/fence crossing or pinch-point inventory.

## Claims that are ready versus not ready

### Ready to draft

- The study is a scenario-based structural-connectivity analysis.
- The macro model uses a 1 km grain and fixed core areas.
- Terrain is included as a 20% resistance component.
- The 31–32 terrain sensitivity changes local route geometry but preserves the
  broader corridor.
- The optional local models are management refinements, not prerequisites for
  the regional analysis.

### Do not finalize yet

- Exact current-flow rankings or cumulative current results until the final
  output files and QC are recovered.
- Claims that modeled paths are observed or realized animal movement routes.
- Claims that fences are empirically calibrated barriers.
- Claims that all local variables have 500 m or 30 m detail; most non-terrain
  inputs remain at their source/model grain.

## Suggested manuscript structure

1. Introduction
2. Study area
3. Data and resistance-surface construction
4. Connectivity and priority-link analysis
5. Sensitivity and uncertainty analysis
6. Results
7. Discussion
8. Management implications
9. Limitations and conclusions

The main text should emphasize the regional 1 km result. Put the 31–32
terrain comparison and any future four-nucleus local models in a sensitivity
or supplementary section.
