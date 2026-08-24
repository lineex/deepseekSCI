# Data Analysis

## 1. Data intake

Before modeling:

1. inventory files, tables, keys, row counts, date coverage and codebook versions;
2. keep raw data read-only and hash local extracts;
3. identify unit, timezone, duplication and impossible-value risks;
4. create `protocol/variable_dictionary.csv` from the bundled template;
5. build a cohort flow with exclusion counts;
6. profile missingness and measurement frequency by relevant groups;
7. create one analysis-ready dataset from scripted transformations.

Do not infer clinical meaning from column names alone. Verify source table, code system, specimen, unit, timing and aggregation.

## 2. Analytical sequence

Run in this order:

1. locked cohort and variable construction;
2. data-quality report;
3. descriptive characteristics and unweighted/weighted sample flow;
4. primary model;
5. diagnostics and assumption checks;
6. prespecified sensitivity analyses;
7. prespecified subgroup/effect-modification analyses;
8. exploratory analyses, clearly separated;
9. publication tables/figures generated directly from model objects;
10. run manifest and traceability map.

Use effect estimates, confidence/credible intervals and clinically interpretable scales. P values are supporting information, not the result.

## 3. Missing data and informative measurement

- Distinguish structural absence, not measured, below detection, not applicable and lost follow-up.
- Describe missingness by exposure, outcome, severity, site and time.
- Use complete-case analysis only with a defensible missingness argument and sensitivity checks.
- Multiple imputation models should include analysis variables, outcome information where appropriate, nonlinear terms/interactions and auxiliary predictors; pool with correct rules.
- For longitudinal clinical data, test whether being measured predicts severity/treatment/outcome. Complete trajectories can form a selected, sicker cohort.

Do not replace missing clinical values with normal values unless the data-generating process explicitly supports it.

## 4. Model selection and diagnostics

Choose the model from outcome structure and estimand:

- binary: risk difference/ratio or logistic models as appropriate;
- count/rate: Poisson, negative binomial or zero-inflated/hurdle models with justified offsets;
- continuous/bounded: linear, ordinal, beta, two-part or other distribution-aware models;
- time-to-event: Kaplan-Meier for description, Cox/AFT/flexible parametric models, competing-risk methods when relevant;
- repeated measures: mixed models, GEE, joint models or trajectory methods with explicit assumptions;
- clustered/multicenter: cluster-robust or hierarchical effects aligned with sampling and estimand.

Check functional form, influential observations, residual patterns, calibration, proportional hazards, overdispersion, sparse cells, separation and convergence as relevant. VIF can diagnose linear dependence but is not an automatic variable-deletion rule; resolve collinearity using design knowledge, reparameterization or a documented estimand choice.

## 5. Nonlinearity, interactions and multiplicity

Prespecify clinically plausible nonlinear terms and knots. Report overall and nonlinear evidence plus an interpretable curve with data density. Do not select a threshold solely from the most favorable observed split.

Treat subgroup claims as interaction questions. Report stratum estimates and the interaction estimate with uncertainty. Distinguish confirmatory from exploratory multiplicity and apply an appropriate control strategy when multiple primary hypotheses exist.

## 6. Causal methods

For propensity or treatment models:

- use baseline variables selected from the DAG;
- inspect overlap/positivity before estimating effects;
- report weight formula, stabilization and truncation;
- assess balance with SMD and plots, not significance tests;
- report effective sample size and extreme weights;
- use outcome models compatible with the estimand and weights;
- consider doubly robust or g-methods when justified;
- test alternate definitions and unmeasured-confounding assumptions.

Do not interpret good balance as proof of no confounding.

## 7. MIMIC and other EHR databases

- Fix database version and code repository commit.
- Resolve ICU/hospital encounter hierarchy and repeated admissions.
- Align all windows to a clinically meaningful time zero.
- Separate charted time, specimen time, result time, order time and administration time.
- Handle unit conversions and duplicated chart events explicitly.
- Distinguish treatment before versus after the index measurement.
- Document code lists and validate phenotypes against source logic or samples.
- Report informative testing, left truncation, immortal time and discharge/death competing processes.

For large tables, select only needed columns, filter early, persist intermediate cohorts and avoid repeatedly scanning raw data.

## 8. NHANES and complex surveys

- Join cycles using stable participant identifiers and component documentation.
- Select the weight for the smallest analytic subsample and combine cycles correctly.
- Include strata and PSU variables; use survey-aware estimation for means, regression and variance.
- Distinguish fasting/laboratory subsamples and changing assay methods across cycles.
- Apply detection-limit and pregnancy/age restrictions as prespecified.
- Report unweighted N with weighted population estimates.

Ordinary regression on weighted rows without the survey design is not an NHANES analysis.

## 9. Prediction and machine learning

Build a leakage audit before training. Use nested resampling for tuning, compare against a parsimonious baseline, quantify optimism and report calibration. Store the preprocessing recipe and final feature definitions. Evaluate fairness/transportability across relevant demographic, temporal and site strata without turning every stratum into an unsupported claim.

## 10. Output contract

Create machine-readable and publication-ready outputs:

```text
analysis/outputs/cohort_flow.csv
analysis/outputs/missingness.csv
analysis/outputs/table1.csv
analysis/outputs/primary_effects.csv
analysis/outputs/model_diagnostics.csv
analysis/outputs/sensitivity_effects.csv
analysis/outputs/subgroup_effects.csv
analysis/outputs/figure_data/*.csv
analysis/outputs/session_info.txt
analysis/run_manifest.json
```

Every displayed table/figure must be reproducible from its machine-readable source. Save model objects when licensing and size permit.
