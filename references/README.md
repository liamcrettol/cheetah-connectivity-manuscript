# Reference library

This folder indexes all 29 BibTeX references in `refs/`.
Open-access PDFs downloaded: 13.
Entries without a downloaded PDF: 16.

Only open publisher or public-repository copies are stored here. A missing PDF
does not mean the reference is unavailable. Follow its DOI or source link and use
library access if needed. `reference_index.csv` contains the full link and status
record.

## Downloaded PDFs

- `verschueren2024guild`: [A Diminished Large Carnivore Guild with Contrasting Species-Habitat Associations Persists Outside National Parks in Namibia's Central-Eastern Landscape](pdfs/verschueren2024guild_2024.pdf)
- `sousa2026kaza`: [Multispecies Transboundary Landscape Connectivity in the {KAZA} {TFCA}](pdfs/sousa2026kaza_2026.pdf)
- `hofmann2023wilddog`: [A Three-Step Approach for Assessing Landscape Connectivity via Simulated Dispersal: African Wild Dog Case Study](pdfs/hofmann2023wilddog_2023.pdf)
- `lines2019kafuezambezi`: [Status of Terrestrial Mammals at the Kafue--Zambezi Interface: Implications for Transboundary Connectivity](pdfs/lines2019kafuezambezi_2019.pdf)
- `mutoro2025kenya`: [Impact of Anthropogenic Landscape Alteration on the Distribution of Potential Cheetah (\emph{Acinonyx jubatus}) Habitats in Southern Kenya: Revealing Cheetah Behavioural Change](pdfs/mutoro2025kenya_2025.pdf)
- `dimbleby2024rewilding`: [Rewilding Landscapes with Apex Predators: Cheetah (\emph{Acinonyx jubatus}) Movements Reveal the Importance of Environmental and Individual Contexts](pdfs/dimbleby2024rewilding_2024.pdf)
- `musenge2026liuwa`: [Four Decades of Spatio-Temporal Habitat Dynamics in a Human-Wildlife Co-Existence Landscape in the Liuwa Ecosystem of Zambia](pdfs/musenge2026liuwa_2026.pdf)
- `moqanaki2016iran`: [All Roads Lead to Iran: Predicting Landscape Connectivity of the Last Stronghold for the Critically Endangered Asiatic Cheetah](pdfs/moqanaki2016iran_2017.pdf)
- `weise2017distribution`: [The Distribution and Numbers of Cheetah (Acinonyx jubatus) in Southern Africa](pdfs/weise2017distribution_2017.pdf)
- `anantharaman2020circuitscape`: [Circuitscape in {J}ulia: High Performance Connectivity Modelling to Support Conservation Decisions](pdfs/anantharaman2020circuitscape_2020.pdf)
- `landau2021omniscape`: [Omniscape.jl: Software to Compute Omnidirectional Landscape Connectivity](pdfs/landau2021omniscape_2021.pdf)
- `melzheimer2020hubs`: [Communication Hubs of an Asocial Cat Are the Source of a Human--Carnivore Conflict and Key to Its Solution](pdfs/melzheimer2020hubs_2020.pdf)
- `meijer2018grip`: [Global Patterns of Current and Future Road Infrastructure](pdfs/meijer2018grip_2018.pdf)

## No PDF stored

- `mulenga2025kafue`: Factors Influencing Cheetah (\emph{Acinonyx jubatus}) Distribution in Kafue National Park, Zambia - no open PDF located
- `buk2018metapopulation`: [Conservation of Severely Fragmented Populations: Lessons from the Transformation of Uncoordinated Reintroductions of Cheetahs (\emph{Acinonyx jubatus}) into a Managed Metapopulation with Self-Sustained Growth](https://doi.org/10.1007/s10531-018-1606-y) - no open PDF located
- `mcrae2008circuit`: [Using Circuit Theory to Model Connectivity in Ecology, Evolution, and Conservation](https://doi.org/10.1890/07-1861.1) - no open PDF located
- `adriaensen2003leastcost`: [The Application of `Least-Cost' Modelling as a Functional Landscape Model](https://doi.org/10.1016/S0169-2046(02)00242-6) - no open PDF located
- `beier2008forks`: [Forks in the Road: Choices in Procedures for Designing Wildland Linkages](https://doi.org/10.1111/j.1523-1739.2008.00942.x) - no open PDF located
- `zeller2012resistance`: [Estimating Landscape Resistance to Movement: A Review](https://doi.org/10.1007/s10980-012-9737-0) - no open PDF located
- `zeller2018equal`: [Are All Data Types and Connectivity Models Created Equal? Validating Common Connectivity Approaches with Dispersal Data](https://doi.org/10.1111/ddi.12742) - open PDF link found but download failed
- `keeley2021metrics`: [Connectivity Metrics for Conservation Planning and Monitoring](https://doi.org/10.1016/j.biocon.2021.109008) - open PDF link found but download failed
- `saura2007pc`: [A New Habitat Availability Index to Integrate Connectivity in Landscape Conservation Planning: Comparison with Existing Indices and Application to a Case Study](https://doi.org/10.1016/j.landurbplan.2007.03.005) - no open PDF located
- `saura2009conefor`: [Conefor Sensinode 2.2: A Software Package for Quantifying the Importance of Habitat Patches for Landscape Connectivity](https://doi.org/10.1016/j.envsoft.2008.05.005) - no open PDF located
- `roberts2017cv`: [Cross-Validation Strategies for Data with Temporal, Spatial, Hierarchical, or Phylogenetic Structure](https://doi.org/10.1111/ecog.02881) - no open PDF located
- `naidoo2024kaza`: [Landscape Connectivity for African Elephants in the World's Largest Transfrontier Conservation Area: A Collaborative, Multi-Scalar Assessment](https://hal.science/hal-04916622) - open PDF link found but download failed
- `brennan2020multispecies`: [Characterizing Multispecies Connectivity across a Transfrontier Conservation Landscape](https://doi.org/10.1111/1365-2664.13716) - open PDF link found but download failed
- `osipova2018fencing`: [Fencing Solves Human-Wildlife Conflict Locally but Shifts Problems Elsewhere: A Case Study Using Functional Connectivity Modelling of the African Elephant](https://doi.org/10.1111/1365-2664.13246) - no open PDF located
- `marker2008spatial`: [Spatial Ecology of Cheetahs on North-Central Namibian Farmlands](https://doi.org/10.1111/j.1469-7998.2007.00375.x) - open PDF link found but download failed
- `kennedy2019ghm`: [Managing the Middle: A Shift in Conservation Priorities Based on the Global Human Modification Gradient](https://doi.org/10.1111/gcb.14549) - no open PDF located

## Refreshing the library

Run `python references/download_open_access_pdfs.py` from the repository root.
The script checks every BibTeX entry again and keeps existing valid PDFs.
