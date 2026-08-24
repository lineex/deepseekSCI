# Integrated supporting reference: research-workflow-adapter/references/critical_care_nma_pattern.md

> Embedded source: `embedded-source/research-workflow-adapter/references/critical_care_nma_pattern.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# Critical Care NMA Pattern

Source article:

- Zhou Z, Liu C, Yang Y, Wang F, Zhang L, et al. Anticoagulation options for continuous renal replacement therapy in critically ill patients: a systematic review and network meta-analysis of randomized controlled trials. Critical Care. 2023;27:222. DOI: 10.1186/s13054-023-04519-1.

Use this pattern for:

- ICU intervention comparisons.
- CRRT or critical-care treatment comparisons.
- RCT-only network meta-analysis.
- Evidence synthesis where direct and indirect comparisons are both useful.

Core reusable workflow:

1. Define a PICO question.
2. Register the protocol when feasible.
3. Follow PRISMA or PRISMA-NMA.
4. Search PubMed, Embase, Web of Science, and Cochrane sources.
5. Add reference-list and prior-meta-analysis citation chasing.
6. Screen studies with two independent reviewers when possible.
7. Extract study, population, intervention, comparator, outcome, and technical variables.
8. Assess risk of bias with a design-appropriate tool.
9. Run pairwise meta-analysis before NMA.
10. Use RR or OR for dichotomous outcomes.
11. Use MD or SMD for continuous outcomes.
12. Assess heterogeneity with I2.
13. Assess transitivity through clinical and methodological comparability.
14. Assess local and global inconsistency.
15. Assess publication bias only when study counts are adequate.
16. Generate PRISMA flow, network geometry, forest plots, league tables, and rank plots.
17. Use SUCRA or similar rankings cautiously.
18. Run sensitivity and subgroup analyses for plausible effect modifiers.

Interpretation guardrails:

- Do not treat the top-ranked intervention as clinically preferred without considering effect size, confidence interval, risk of bias, and evidence sparsity.
- Flag single-study network nodes as low-certainty or hypothesis-generating.
- Report when publication bias cannot be assessed.
- Report whether homogeneity, transitivity, and consistency were evaluated.
- Separate statistical ranking from clinical recommendation.

Standard outputs:

- `evidence/protocol/protocol_registration.md`
- `evidence/search/search_strategy.md`
- `evidence/screening/prisma_flow.csv`
- `evidence/extraction/extraction_table.xlsx`
- `evidence/risk_of_bias/risk_of_bias.csv`
- `evidence/nma/network_nodes.csv`
- `evidence/nma/network_edges.csv`
- `outputs/nma/pairwise_meta.csv`
- `outputs/nma/heterogeneity.csv`
- `outputs/nma/inconsistency.csv`
- `outputs/nma/nma_league_table.csv`
- `outputs/nma/sucra_rank.csv`
- `outputs/figures/prisma_flow.png`
- `outputs/figures/network_geometry.png`
- `outputs/figures/forest_plot.png`
- `outputs/figures/rank_plot.png`

