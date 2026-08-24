# Integrated supporting reference: medical-rct-advanced/resources/sap_template.md

> Embedded source: `embedded-source/medical-rct-advanced/resources/sap_template.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# Statistical Analysis Plan (SAP) Template
## For Advanced RCT Designs

---

## 1. Study Overview

**Trial Name**: [Full trial name]  
**Acronym**: [ACRONYM]  
**Design**: [Simple RCT | 2×2 Factorial | Adaptive | Other]  
**ClinicalTrials.gov**: NCT[number]

**Primary Question**: [One sentence research question]

---

## 2. Sample Size and Power

### 2.1 Sample Size Calculation

**Primary Endpoint Expected Rates**:
- Control group: [XX]%
- Intervention group: [YY]%
- **Absolute difference**: [ZZ] percentage points

**Statistical Parameters**:
- Power: [80% | 90%]%
- Alpha (two-sided): 0.05
- **Required sample size**: [N] per group

**Adherence Buffer**:
- Expected protocol deviations: [X]%
- Expected loss to follow-up: [Y]%
- **Inflated sample size**: [N_final]

### 2.2 Factorial Design Adjustment (if applicable)

| Design | Sample Size |
|--------|-------------|
| Two separate trials | [N1] + [N2] = [Total] |
| **Factorial 2×2** | **[N_factorial]** |
| **Savings** | **[Difference]** |

**Interaction Assumption**: No strong interaction expected between [Intervention A] and [Intervention B]

---

## 3. Primary Analysis

### 3.1 Statistical Model

**Outcome Distribution**: [Binary | Ordinal | Continuous | Time-to-event]

**Link Function Decision**:
```
Expected outcome prevalence: [XX]%

IF prevalence <10%: Use logit-link → report OR
IF prevalence 10-20%: Either acceptable → report [OR | RR]
IF prevalence >20%: MUST use log-link → report RR
```

**Selected**: [Logit | Log | Identity] link

**Model Specification**:
```R
library(lme4)

model <- glmer(
  outcome ~ intervention + 
            [covariate1] + [covariate2] +  # Fixed effects
            (1 | center),                    # Random intercept
  family = binomial(link = "[logit|log]"),
  data = trial_data
)
```

### 3.2 Adjustments and Stratification

**Stratification Variables** (used in randomization):
- [ ] Trial center
- [ ] [Other stratification variable]
- [ ] Co-enrollment in [Trial Name] *(if applicable)*

**Additional Covariates** (adjusted in analysis):
- [ ] Age (continuous)
- [ ] Sex
- [ ] [Disease-specific baseline characteristic]

---

## 4. Secondary Analyses

### 4.1 Secondary Endpoints

| Endpoint | Type | Analysis Method |
|----------|------|-----------------|
| [Endpoint 1] | [Binary/Ordinal/Continuous] | [GLM/GLMM/Cox] |
| [Endpoint 2] | Time-to-event | Cox proportional hazards |
| [Endpoint 3] | ... | ... |

**Multiplicity Adjustment**: [None | Bonferroni | Holm | Other]

**Rationale**: [Explain why adjustment is/isn't applied]

---

## 5. Subgroup Analyses

### 5.1 Pre-specified Subgroups

**PRIMARY** (for primary outcome):
- [ ] Age (≤65 vs >65 years)
- [ ] Sex (Male vs Female)
- [ ] Disease severity ([define categories])
- [ ] [Other clinically relevant subgroup]

**Statistical Method**: Interaction testing

**Model**:
```R
model_interaction <- glmer(
  outcome ~ intervention * subgroup_variable + (1|center),
  family = binomial(link = "[link]")
)
```

**Interpretation Threshold**: 
- P_interaction <0.10 suggests heterogeneity
- If P_interaction <0.05, report separate estimates

**Forest Plot**: Will be generated for all pre-specified subgroups

### 5.2 Exploratory Subgroups (NOT for definitive conclusions)

- [List any exploratory subgroups]
- Clearly labeled as "exploratory" in manuscript

---

## 6. Sensitivity Analyses

### 6.1 Missing Data

**Primary Approach**: Multiple imputation (m=20 imputations)

**Imputation Model Includes**:
- Outcome variable
- All predictors in primary model
- Auxiliary variables: [list]

**Sensitivity Analysis**:
- Complete case analysis
- Best-worst case scenario
- Worst-best case scenario

### 6.2 Per-Protocol Analysis

**Definition of Per-Protocol Population**:
- Received ≥[XX]% of allocated intervention
- No major protocol violations
- Outcome data available

**Rationale**: Assess efficacy under ideal adherence

### 6.3 Alternative Model Specifications

If using log-link:
- **Sensitivity**: Repeat with logit-link (report OR in supplement)

If composite endpoint:
- **Sensitivity**: Analyze components separately

---

## 7. Interim Analyses (if applicable)

### 7.1 DSMB Charter

**Timing**: After [N1] and [N2] patients complete follow-up

**Stopping Rules**:
- **Efficacy**: [Define stopping boundary, e.g., O'Brien-Fleming]
- **Futility**: [Define futility boundary]
- **Safety**: [Pre-specified adverse event thresholds]

**Alpha Spending**: [Method, e.g., Lan-DeMets]

**Adaptive Adjustments Allowed**:
- [ ] Sample size re-estimation
- [ ] Event rate re-estimation
- [ ] Inclusion/exclusion criteria modification

### 7.2 Blinding During Interim

- Statistician unblinded for DSMB
- Investigators remain blinded
- DSMB recommendations coded (continue/stop/modify)

---

## 8. Co-Enrollment Handling (if applicable)

**Co-enrolled Trial**: [Trial Name]

**Proportion Expected**: [XX]%

**Statistical Handling**:

1. **Stratification**: Co-enrollment status included in randomization strata

2. **Analysis Adjustment**:
```R
model <- glmer(
  outcome ~ intervention + 
            co_enrolled_trial_X +  # Fixed covariate
            (1|center)
)
```

3. **Interaction Testing**:
```R
model_interaction <- glmer(
  outcome ~ intervention * co_enrolled_trial_X + (1|center)
)

# Report interaction P-value for primary outcome
```

4. **Sensitivity Analysis**: Repeat primary analysis excluding co-enrolled patients

---

## 9. Special Methods

### 9.1 Sliding Dichotomy (if using ordinal outcome)

**Applicable**: [GOS-E | mRS | Other ordinal scale]

**Prognostic Model**: [Name of validated model, e.g., IMPACT, CRASH]

**Algorithm**:

| Baseline Prognostic Score | "Favorable Outcome" Definition |
|---------------------------|--------------------------------|
| [Score range 1] (Best prognosis) | [Outcome] ≥ [Threshold 1] |
| [Score range 2] (Moderate) | [Outcome] ≥ [Threshold 2] |
| [Score range 3] (Poor) | [Outcome] ≥ [Threshold 3] |

**Pre-specification**: Algorithm finalized before any outcome data collected

**Blinded Implementation**: Prognostic scores calculated before unblinding

**Statistical Model**:
```R
# Create binary outcome using sliding dichotomy
trial_data$favorable <- with(trial_data, {
  ifelse(prognosis_score > threshold1, outcome >= cutoff1,
  ifelse(prognosis_score > threshold2, outcome >= cutoff2,
         outcome >= cutoff3))
})

model <- glmer(favorable ~ intervention + (1|center),
               family = binomial(link = "log"))
```

**Reference**: See `resources/sliding_dichotomy_algorithm.R`

---

## 10. Reporting Plan

### 10.1 Primary Manuscript

**Results Section Order**:
1. **Enrollment and baseline** (CONSORT diagram, Table 1)
2. **Intervention delivery** (adherence, separation in intervention parameter)
   - Figure 1: Time-series of intervention parameter
   - Median/mean values in each group
   - Protocol deviations reported
3. **Primary outcome** (effect estimate with 95% CI, P-value)
4. **Secondary outcomes** (all pre-specified outcomes, Table 2)
5. **Subgroup analyses** (forest plot)
6. **Adverse events** (Table 3)

### 10.2 Statistical Reporting Standards

**Effect Estimates**:
- Report point estimate + 95% CI + P-value
- For binary outcomes: [RR | OR] depending on link function
- For continuous: Mean difference or ratio
- For time-to-event: Hazard ratio

**P-values**:
- Report exact P-values (not "P<0.05")
- State two-sided vs one-sided
- For primary outcome, alpha adjusted for interim analyses

**Model Diagnostics**:
- State assumption checks performed
- Report ICC for mixed models
- For Cox: verify proportional hazards assumption

---

## 11. Software and Reproducibility

**Statistical Software**: 
- R version [X.X.X]
- Key packages: lme4, survival, mice (for imputation)

**Code Archiving**: 
- All analysis code deposited at [repository]
- Synthetic dataset for reproducibility

**Blinding**:
- Analyst blinded via recoding (Group A/Group B)
- Unblinding code held by [role]
- Unblinding date: [Date or trigger event]

---

## 12. Deviations from SAP

**Process for Handling**:
- All deviations documented in amendment log
- Rationale and timing recorded
- Major deviations reported in manuscript Methods

**Pre-specified Analyses Hierarchy**:
1. Primary outcome primary analysis
2. Primary outcome sensitivity analyses
3. Secondary outcomes
4. Subgroup analyses (interaction tests)
5. Exploratory analyses

**SAP Version Control**:
- Version 1.0: [Date] - Initial SAP
- Version 1.1: [Date] - [Brief description of changes]

---

## 13. Signatures and Approval

**SAP Finalized By**: [Date]  
**Protocol Version**: [Version number]  
**Amendment History**: [If applicable]

**Approvals**:
- [ ] Principal Investigator
- [ ] Lead Statistician
- [ ] Steering Committee Chair
- [ ] Ethics Committee (if required)

**Lock Date**: Analysis code frozen on [Date], before database lock

---

**End of SAP Template**

