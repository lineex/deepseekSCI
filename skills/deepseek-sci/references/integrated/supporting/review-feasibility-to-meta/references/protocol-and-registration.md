# Integrated supporting reference: review-feasibility-to-meta/references/protocol-and-registration.md

> Embedded source: `embedded-source/review-feasibility-to-meta/references/protocol-and-registration.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# Protocol and registration

## Protocol lock order

1. Review type and rationale.
2. Structured question and primary estimand.
3. Eligibility criteria.
4. Outcome hierarchy and event-time windows.
5. Information sources and search strategy.
6. Selection process.
7. Data items and extraction process.
8. Risk-of-bias methods.
9. Effect measures.
10. Synthesis groups and model.
11. Heterogeneity, subgroup and sensitivity methods.
12. Reporting-bias and certainty methods.
13. Amendments, data management, code and dissemination.

## PROSPERO crosswalk

| Protocol object | PROSPERO field |
|---|---|
| title and review type | Review title and basic details |
| primary question/estimand | Review objectives |
| rationale and overlap | Condition/domain, context, similar reviews |
| population | Population |
| intervention/exposure | Intervention(s) or exposure(s) |
| comparator | Comparator(s) or control(s) |
| outcomes and time points | Main and additional outcomes |
| study designs | Study design |
| databases, dates, language and grey literature | Searches |
| selection process | Data collection process |
| extraction and author contact | Data extraction |
| risk-of-bias tools and reviewer process | Risk of bias assessment |
| effect measures and model | Planned data synthesis |
| subgroup/sensitivity analyses | Analysis of subgroups or subsets |
| publication bias and certainty | Reporting bias and certainty |
| dates and stage | Review timeline and review stage |
| protocol repository | Availability of full protocol |
| funding and conflicts | Affiliation, funding and conflict fields |

## Registration timing

- Pilot searches, overlap checks and screening calibration may occur before registration.
- Register while the review is genuinely prospective, ideally before formal title/abstract screening and always before outcome-aware extraction and synthesis.
- Record the stage truthfully.
- Save the submitted record, registration identifier, publication date and each later version.

## Protocol snapshot

Freeze:

- `protocol.md`;
- `analysis_plan.md`;
- `search_strategy_draft.md`;
- extraction schema;
- risk-of-bias plan;
- synthesis-decision rules.

Create a SHA-256 checksum and a dated archive. Amendments must state what changed, why, when, whether results were known and the expected impact.

## Minimum analysis-plan details

- primary and secondary outcomes;
- preferred and fallback effect measures;
- direction harmonization;
- multi-arm and repeated-measure handling;
- cluster and crossover handling;
- missing standard deviations and imputation hierarchy;
- zero-event methods;
- model and tau-squared estimator;
- confidence-interval method;
- prediction interval rule;
- subgroup and meta-regression eligibility;
- sensitivity analyses;
- reporting-bias assessment threshold;
- certainty framework;
- software and package versions.


