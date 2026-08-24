# Integrated supporting reference: review-feasibility-to-meta/references/rase-case-audit.md

> Embedded source: `embedded-source/review-feasibility-to-meta/references/rase-case-audit.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# RAsE benchmark case

## Registered protocol

PROSPERO `CRD42022349074`, version 1.0, registered 3 September 2022.

Question:

> Does resuscitation of patients with shock-induced endotheliopathy lead to worsening endothelial dysfunction?

Planned:

- PubMed/MEDLINE and Embase, 2011-2021, English;
- RCTs, observational studies, case series and case reports;
- no comparator required;
- endothelial outcomes grouped as microvascular imaging, glycocalyx biomarkers and endothelial mediators;
- odds ratios as the stated effect measure;
- random effects if `I2 > 50%`, fixed effects if `I2 < 50%`;
- subgroup analysis by shock type;
- risk of bias described only as review of each article's statistical analysis plan.

At registration, formal searching was marked complete and screening had started; extraction, risk-of-bias assessment and synthesis had not started.

## Final publication

- search updated through July 2023;
- 195 records, 68 full texts, 32 qualitative studies and 10 quantitative studies;
- continuous marker and microcirculatory effects pooled with random-effects models;
- Cochrane and Newcastle-Ottawa tools used;
- studies from different shock types and different clinical contrasts were combined.

## Protocol-to-publication deviations

1. continuous mean/standardized effects replaced the registered odds-ratio plan;
2. random effects were used even for MFI with `I2 = 0%`, contrary to the registered threshold rule;
3. planned shock-type subgrouping did not prevent cross-shock pooling;
4. risk-of-bias tools were strengthened after registration;
5. search dates were extended, appropriately, but the update should be logged as an amendment;
6. comparator-free eligibility created heterogeneous contrasts for meta-analysis.

## Statistical consistency error

The syndecan-1 meta-analysis reported `0.27 (95% CI -0.07 to 0.60), p = 0.12, I2 = 75.85%`. The abstract and figure caption nevertheless described the result as statistically significant. This illustrates why the final audit must compare forest plots, confidence intervals, p values and prose mechanically and manually.

## Transferable lesson

Transfer the pipeline:

`registered question -> systematic search -> evidence domains -> conceptual output`

Do not transfer:

`same biomarker -> assumed common estimand -> pooled effect -> causal framework`

## Verified PubMed-only replication controls

The 2026-07-14 test replication added the following reusable controls:

- historical initial-window count: 68 versus 69 reported, logged as database drift;
- separate initial and update batches with one electronic/print date overlap;
- primary-query, sensitivity-query and citation-chain recovery reported separately;
- 32/32 benchmark reports recovered and 39 reports linked to 35 cohort families after the update;
- benchmark supplement extraction distinguished from primary full-text verification;
- 17 displayed effects reconstructed across four modules, revealing 11 distinct report labels despite the publication stating 10;
- model-based `I2` reproduced the STATA display more closely than Q-based `I2`;
- all four pooled effects matched to rounding, while corrected estimand assessment rejected all four marker-defined pools for causal inference;
- the source syndecan-1 significance error was preserved in a benchmark failure report, then corrected in the replication manuscript.

