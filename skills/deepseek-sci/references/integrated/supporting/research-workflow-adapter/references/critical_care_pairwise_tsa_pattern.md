# Integrated supporting reference: research-workflow-adapter/references/critical_care_pairwise_tsa_pattern.md

> Embedded source: `embedded-source/research-workflow-adapter/references/critical_care_pairwise_tsa_pattern.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# Critical Care Pairwise TSA Pattern

Source article:

- Liu C, Mao Z, Kang H, Hu J, Zhou F. Regional citrate versus heparin anticoagulation for continuous renal replacement therapy in critically ill patients: a meta-analysis with trial sequential analysis of randomized controlled trials. Critical Care. 2016;20:144. DOI: 10.1186/s13054-016-1299-0.

Use this pattern for:

- Two-arm intervention comparisons.
- RCT-only conventional meta-analysis.
- Critical-care treatment comparisons.
- Questions where evidence sufficiency is as important as pooled effect direction.
- Projects requiring trial sequential analysis and GRADE.

Core reusable workflow:

1. Define a PICO question.
2. Follow PRISMA.
3. Search multiple databases from inception to a prespecified end date.
4. Include PubMed, Embase, Web of Science, Cochrane sources, and region-specific databases when relevant.
5. Avoid language restriction when feasible.
6. Search references of reviews and included studies.
7. Include RCTs when causal intervention evidence is required.
8. Use two independent reviewers for selection and extraction when possible.
9. Resolve disagreements by consensus or a third reviewer.
10. Extract study design, sample size, population, intervention, comparator, outcome, and adverse event data.
11. Predefine primary and secondary outcomes.
12. Assess risk of bias using Cochrane domains.
13. Contact authors for missing data when feasible.
14. Assess certainty of evidence using GRADE.
15. Pool dichotomous outcomes with RR or OR and 95% CI.
16. Pool continuous outcomes with MD or SMD and 95% CI.
17. Quantify heterogeneity with I2.
18. Use fixed-effect models when heterogeneity is acceptable.
19. Use random-effects models when heterogeneity is substantial.
20. Run prespecified subgroup and sensitivity analyses.
21. Assess publication bias when study counts are adequate.
22. Run TSA for primary outcomes and key safety outcomes when sparse data or repeated testing may inflate random error.

TSA essentials:

- Define alpha, beta, anticipated effect size, control event rate, and diversity adjustment.
- Estimate required information size.
- Plot the cumulative Z-curve.
- Compare the Z-curve with conventional significance boundaries.
- Compare the Z-curve with trial sequential monitoring boundaries.
- Assess whether futility boundaries are crossed.

Interpretation guardrails:

- Conventional statistical significance is not sufficient if the TSA boundary is not crossed.
- Non-significant pooled results may still be informative if the futility boundary is crossed.
- If the required information size is not reached, state that evidence remains underpowered.
- Do not overstate certainty when risk of bias, imprecision, or inconsistency is present.
- Align the final conclusion with GRADE certainty and TSA sufficiency.

Standard outputs:

- `evidence/protocol/protocol_registration.md`
- `evidence/search/search_strategy.md`
- `evidence/screening/prisma_flow.csv`
- `evidence/extraction/extraction_table.xlsx`
- `evidence/risk_of_bias/risk_of_bias.csv`
- `evidence/grade/grade_summary.csv`
- `evidence/tsa/tsa_parameters.csv`
- `outputs/tables/pairwise_meta.csv`
- `outputs/tables/subgroup_meta.csv`
- `outputs/tables/sensitivity_meta.csv`
- `outputs/tables/publication_bias.csv`
- `outputs/tsa/tsa_summary.csv`
- `outputs/figures/prisma_flow.png`
- `outputs/figures/forest_plot.png`
- `outputs/figures/funnel_plot.png`
- `outputs/figures/tsa_plot.png`

