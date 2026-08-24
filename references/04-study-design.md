# Study Design

## 1. Lock the common protocol

Every design must state:

- scientific question and hypothesis;
- target population and setting;
- eligibility and sampling frame;
- time zero/index date;
- exposure/intervention and assignment procedure;
- comparator strategy;
- primary and secondary outcomes with windows;
- follow-up and censoring;
- target estimand/effect measure;
- confounders, effect modifiers and mediators;
- missing-data strategy;
- precision/power rationale;
- primary, sensitivity and subgroup analyses;
- ethics, registration, data governance and reporting guideline.

Use PICOTS for interventions, PECO for exposures, PCC for scoping reviews and a prediction-specific target population/outcome/horizon definition for models.

## 2. Observational association or causal inference

Distinguish descriptive, prognostic, associational and causal aims before selecting a model.

For causal questions:

1. draw a DAG based on subject knowledge;
2. define the causal contrast and time zero;
3. separate baseline confounders from mediators and post-exposure variables;
4. assess exchangeability, positivity, consistency and interference;
5. choose matching, standardization, g-computation, weighting or outcome regression based on the estimand and data;
6. inspect covariate balance and weight distribution, not model fit alone;
7. predefine negative controls, quantitative bias analysis or E-values when useful;
8. state residual confounding and measurement error.

Do not adjust automatically for every measured variable. Avoid conditioning on colliders or variables affected by exposure.

## 3. Target trial emulation

Map each component explicitly:

| Component | Required specification |
|---|---|
| Eligibility | criteria evaluated before/at time zero |
| Strategies | implementable treatment/exposure rules |
| Assignment | observational analogue of random allocation |
| Time zero | aligned eligibility, assignment and follow-up |
| Follow-up | start, end and competing events |
| Outcome | definition and ascertainment window |
| Causal contrast | per-protocol or intention-to-treat analogue |
| Analysis | cloning/censoring/weighting, landmarking or other method |

Diagnose immortal time, prevalent-user bias, grace periods, treatment crossover, informative censoring and positivity. If treatment may start during a grace period, emulate assignment consistently; a simple exposed-versus-unexposed comparison can be biased. State comparator strategies precisely, such as early versus deferred/no early treatment, rather than early versus never treated when later treatment is allowed.

Never select a subgroup using information measured after time zero unless the estimand explicitly conditions on a post-baseline event and the design handles that conditioning.

## 4. Randomized trials

Use SPIRIT for protocol and CONSORT for reporting. Define allocation, concealment, blinding, intervention fidelity, co-interventions, adherence, harms, stopping, data monitoring and estimand.

Select advanced features only when justified:

- factorial designs require interaction and power assumptions;
- co-enrollment requires compatibility and interaction monitoring;
- adaptive sample-size revision requires prespecified blinded/unblinded governance;
- cluster or multicenter designs require intracluster correlation and center effects;
- ordinal/sliding-dichotomy analyses require a clinically defensible scale and prespecification;
- common outcomes may favor risk ratios or risk differences over odds ratios.

Plan how null results will be interpreted through precision, adherence, separation between groups, endpoint sensitivity, generalizability and remaining evidence, not by searching for a positive subgroup.

## 5. Prediction and prognostic models

Use TRIPOD and assess risk of bias with PROBAST. Define intended user, use point, outcome horizon and decision consequence.

- Split by patient and time/site where appropriate; prevent leakage from future measurements or repeated encounters.
- Keep all preprocessing, imputation, variable selection and tuning inside resampling.
- Match effective sample size to outcome prevalence and candidate parameters; avoid simplistic events-per-variable rules as the only rationale.
- Report discrimination, calibration-in-the-large, calibration slope, calibration plots, overall accuracy and clinical utility.
- Use optimism correction/internal validation; seek temporal or external validation.
- Compare with a credible clinical baseline and assess net benefit only over meaningful thresholds.
- Do not call a model clinically useful from AUC alone.

## 6. Diagnostic accuracy

Use STARD. Define intended use, index test, reference standard, threshold timing, blinding, indeterminate results and participant flow.

Avoid case-control spectrum designs when estimating clinical accuracy. Report sensitivity, specificity, predictive values at the observed prevalence, likelihood ratios and uncertainty. Account for verification bias, imperfect reference standards and multiple thresholds.

## 7. Prospective cohorts and registries

Build the CRF from the estimand backward. Include only fields needed for eligibility, exposure/intervention, confounding, outcomes, safety, missingness interpretation and prespecified subgroups.

For time-sensitive acute-care research, capture:

```text
event/arrival -> first measurement -> recognition -> decision -> order -> execution -> definitive care
```

Record measurement state such as pre/post transfusion, fluid, ventilation, sedation, procedure or rescue treatment. Define one index sample when treatment alters phenotype classification. Pilot abstraction rules and inter-rater reliability before scale-up.

## 8. Power and precision

Base justification on the primary estimand and model. Report assumptions and their source. Use simulations for complex longitudinal, clustered, survival, causal or prediction designs. Explore a plausible range rather than a single optimistic effect.

For feasibility pilots, focus on recruitment, completeness and precision rather than testing effectiveness. When event support is weak, simplify the estimand/model or broaden the cohort instead of relying on unstable penalization as a substitute for design.

## 9. Protocol registration

Register prospectively when applicable: trial registry for interventional studies, PROSPERO/OSF or another suitable registry for evidence syntheses, and a time-stamped protocol for observational analyses. Record amendments with date, rationale and whether outcomes were inspected.
