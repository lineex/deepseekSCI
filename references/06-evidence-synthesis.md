# Evidence Synthesis

## 1. Route before searching

Choose the product that matches the question:

- systematic review/meta-analysis for a focused estimable question;
- scoping review for concepts, evidence types and gaps;
- rapid review when methods are deliberately streamlined and limitations declared;
- narrative/state-of-the-art review for conceptual integration;
- umbrella review for existing syntheses;
- replication/update when a benchmark review supplies a reproducible protocol.

Run a feasibility pilot before promising meta-analysis. Estimate eligible-study count, independence of cohorts, effect extractability, outcome compatibility and likely heterogeneity.

## 2. Protocol and registration

Specify PICOS, eligible designs, reports versus studies, outcomes/time points, effect hierarchy, search sources, screening, extraction, risk of bias, synthesis model, heterogeneity, subgroup/meta-regression, missing data, certainty and amendments. Register prospectively when possible.

Use PRISMA 2020 and relevant extensions. A narrative synthesis still needs explicit search and selection methods when presented as systematic.

## 3. Study identity and extraction

Create a study-family identifier to link protocols, conference abstracts, primary reports, follow-ups and subgroup papers from the same cohort. Extract arm-level and effect-level data without double counting.

Prefer adjusted or unadjusted effects according to the prespecified estimand. Do not mix OR, RR and HR as if interchangeable. Align direction, units and time horizons before pooling. Document conversions and digitization.

## 4. Risk of bias and certainty

Use the design-appropriate tool:

- ROB 2 for randomized trials;
- ROBINS-I for nonrandomized intervention studies;
- QUADAS-2 for diagnostic accuracy;
- PROBAST for prediction;
- suitable JBI/CASP tools for other designs when justified.

Risk-of-bias judgments require signaling-question support, not only a color plot. Use GRADE per outcome, considering risk of bias, inconsistency, indirectness, imprecision and publication bias, with transparent reasons for rating changes.

## 5. Pairwise meta-analysis

- Use a model consistent with expected effect variation; do not choose fixed versus random solely from an I-squared threshold.
- Report effect estimate, interval, tau-squared, prediction interval when meaningful and I-squared with context.
- Use Hartung-Knapp or other small-sample methods where appropriate and preplanned.
- Explore heterogeneity through clinically prespecified moderators and influence analyses.
- Use funnel plots/asymmetry tests only with an adequate number of sufficiently comparable studies.
- Treat trim-and-fill as a sensitivity device with strong assumptions, never as automatic repair.

If pooling is not defensible, retain a structured synthesis without manufacturing a summary effect.

## 6. Special synthesis routes

### Diagnostic accuracy

Use hierarchical/bivariate models for sensitivity and specificity when data allow. Preserve thresholds and avoid separate univariate pooling that loses their dependence.

### Network meta-analysis

Build a treatment network only when transitivity is clinically plausible. Report network geometry, direct/indirect evidence, heterogeneity, local/global inconsistency and certainty. Rankings such as SUCRA are secondary to effect estimates and certainty; do not present rank as proof of superiority.

### Trial sequential analysis

Use TSA only for a prespecified sparse or repeatedly updated pairwise question. Report alpha, beta, anticipated effect, heterogeneity/diversity adjustment, information size and monitoring/futility boundaries. Interpret conventional significance and information sufficiency separately.

### Individual participant or dose-response analysis

Lock harmonization rules, repeated-participant handling and nonlinear model choices before synthesis. Preserve within-study comparisons.

## 7. Narrative and state-of-the-art reviews

Build an architecture before prose:

1. clinical/scientific paradox;
2. operational definition and adjacent entities;
3. phenotype/time/setting map;
4. burden and key outcomes;
5. organizing mechanistic principle;
6. mechanism modules tied to observable evidence;
7. measurement validity;
8. management or translational implications;
9. counterevidence and controversies;
10. research agenda with testable questions.

Use figures as cognitive tools: phenotype map, mechanism system, measurement interpretation, management/trial algorithm and evidence-gap map. Give each figure one primary job and state uncertainty in the caption.

## 8. Review replication and updates

When replicating a published review:

1. identify its actual review type and protocol;
2. reconstruct searches, dates, eligibility, study families, extracted effects and analysis settings;
3. compare counts and results at each module;
4. classify discrepancies as search drift, eligibility interpretation, data extraction, effect conversion, model choice or software;
5. produce a replication scorecard before extending the search date.

Do not optimize the method until the original result is sufficiently reproduced or the irrecoverable difference is documented.

## 9. Required outputs

```text
protocol/review_protocol.md
search/search_strategy.md
search/search_log.csv
evidence/deduplicated_records.csv
evidence/screening/title_abstract.csv
evidence/screening/full_text.csv
evidence/extraction/evidence_matrix.csv
evidence/risk_of_bias.csv
analysis/outputs/effect_sizes.csv
analysis/outputs/meta_results.csv
analysis/outputs/heterogeneity.csv
analysis/outputs/sensitivity.csv
analysis/outputs/certainty.csv
manuscript/figures/prisma_flow.*
```

Generate the PRISMA flow from recorded counts and explain any arithmetic mismatch.
