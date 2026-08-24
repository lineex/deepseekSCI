# Integrated supporting reference: review-feasibility-to-meta/references/synthesis-and-reporting.md

> Embedded source: `embedded-source/review-feasibility-to-meta/references/synthesis-and-reporting.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# Synthesis and reporting

## Synthesis readiness

For every proposed synthesis answer:

1. Do studies estimate the same clinical question?
2. Are populations and settings transportable enough?
3. Are interventions/exposures and comparators equivalent?
4. Are outcomes defined on compatible scales?
5. Are event times aligned?
6. Are estimates adjusted for materially different covariates?
7. Are cohorts independent?
8. Is the direction of benefit/harm harmonized?

If a key answer is no, split the synthesis or use structured narrative synthesis.

## Effect measures

- Binary: risk ratio, odds ratio or risk difference according to the estimand and event frequency.
- Continuous, same scale: mean difference.
- Continuous, different valid scales: standardized mean difference with interpretive caution.
- Time-to-event: log hazard ratio with time-origin and proportional-hazards assumptions considered.
- Diagnostic accuracy: paired sensitivity/specificity models, not separate univariate pooling when avoidable.
- Pre-post data: distinguish change-score and final-value contrasts; account for within-person correlation.

Do not combine adjusted and unadjusted estimates without a prespecified rationale.

## Model principles

- Choose fixed/common-effect or random-effects from the target inference and expected clinical variation, not from an `I2` cutoff.
- For random effects, prespecify the tau-squared estimator, commonly REML, and interval method.
- Consider Hartung-Knapp adjustments and prediction intervals when appropriate, especially with few heterogeneous studies.
- Report tau-squared and explain heterogeneity clinically; `I2` alone is insufficient.
- With very few studies, emphasize individual estimates and uncertainty.

## Small-study and reporting bias

- Funnel plots and asymmetry tests are usually uninformative with fewer than about ten studies and may mislead when heterogeneity is substantial.
- Compare protocols, registrations and publications for selective outcome reporting.
- Search trial registries and unpublished sources when relevant.

## Subgroups and meta-regression

- Prespecify a small number of biologically or clinically justified hypotheses.
- Use interaction tests rather than comparing significance within subgroups.
- Treat meta-regression as exploratory with sparse studies; avoid one covariate per tiny evidence set.
- Distinguish study-level effect modification from individual-level interaction.

## No-meta synthesis

When pooling is not justified:

1. group studies by a prespecified clinical hierarchy;
2. report study-level effect direction and precision;
3. avoid vote counting by statistical significance;
4. explain heterogeneity and risk of bias;
5. follow SWiM where applicable.

## Reporting order

1. protocol and deviations;
2. PRISMA flow;
3. study/cohort characteristics;
4. risk of bias;
5. individual study results;
6. pooled or structured synthesis;
7. heterogeneity and sensitivity;
8. reporting bias and certainty;
9. limitations of evidence and review process;
10. conclusion bounded by certainty.

Use PRISMA 2020 and the extension appropriate to abstracts, searches, scoping, diagnostic accuracy, network meta-analysis or individual participant data.


