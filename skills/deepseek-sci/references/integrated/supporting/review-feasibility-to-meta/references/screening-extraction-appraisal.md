# Integrated supporting reference: review-feasibility-to-meta/references/screening-extraction-appraisal.md

> Embedded source: `embedded-source/review-feasibility-to-meta/references/screening-extraction-appraisal.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# Search, screening, extraction and appraisal

## Search quality

- Translate concepts into controlled vocabulary and free text for each database.
- Preserve exact queries, translations, interfaces, limits, dates and counts.
- Peer-review the strategy using PRESS when feasible.
- Include trial registries, citation chaining and author contact when relevant.
- Preserve raw exports unchanged and generate normalized derivatives separately.
- Document deduplication identifiers, fuzzy-title rules and manual decisions.

## Screening

Use stable identifiers at three levels:

```text
record_id: database/export record
report_id: publication or report
study_id/cohort_family: underlying participants or experiment
```

Before full screening:

1. pilot 25-100 records across expected boundary cases;
2. refine explanatory notes without changing substantive eligibility post hoc;
3. freeze controlled exclusion reasons;
4. retain an adjudication log.

Full-text exclusion reasons should be mutually exclusive and use one primary reason, for example:

```text
wrong population
wrong intervention/exposure
wrong comparator
wrong outcome/measurement
wrong design
wrong event time
not primary research
duplicate/companion report without unique data
full text unavailable
insufficient extractable data
```

Treat unavailable full text separately from confirmed ineligibility in the PRISMA flow.

## Extraction

The extraction form must reproduce the analysis. Include:

- study and report identifiers;
- cohort family and overlap notes;
- design, country, setting and dates;
- eligibility and sample size by arm/time point;
- intervention/exposure and comparator detail;
- outcome definition, scale and event time;
- raw event counts, means, SDs, change scores or adjusted estimates;
- adjustment set and estimand;
- assay/instrument and thresholds where relevant;
- missingness, attrition and author contact;
- transformations, imputations and derived values;
- funding and conflicts.

Never extract a narrative conclusion in place of the numeric inputs required for an effect estimate.

## Risk-of-bias routing

| Study question | Preferred tool |
|---|---|
| randomized intervention effect | RoB 2 |
| nonrandomized intervention effect | ROBINS-I |
| exposure effect | ROBINS-E or justified domain tool |
| diagnostic accuracy | QUADAS-2/QUADAS-C |
| prediction model | PROBAST/PROBAST+AI as applicable |
| systematic review | ROBIS or AMSTAR 2 according to purpose |
| animal intervention | SYRCLE |

Assess risk of bias for the result used in synthesis, not only the paper as a whole. State how judgments affect synthesis and certainty.

## Dependence control

- Link companion reports before synthesis.
- Select one estimate per cohort/outcome/time point according to a prespecified hierarchy or use a dependence-aware model.
- Avoid double-counting shared control groups.
- Record nested biorepository and trial-substudy relationships.


