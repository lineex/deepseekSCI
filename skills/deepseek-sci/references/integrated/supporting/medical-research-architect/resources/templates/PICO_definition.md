# Integrated supporting reference: medical_research_architect/resources/templates/PICO_definition.md

> Embedded source: `embedded-source/medical_research_architect/resources/templates/PICO_definition.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# PICO Definition Document

> **Standard**: This document follows the Evidence-Based Medicine (EBM) PICO framework.

## Project Header
| Property | Value |
| :--- | :--- |
| **Research Topic** | `[Insert Raw Topic Here]` |
| **Version** | 1.0 |
| **Date** | `[DATE]` |

---

## P - Population (Patient/Problem)

### Target Population
-   **Description**: `[Who is being studied? e.g., Adults aged 18-65 with Type 2 Diabetes]`

### Inclusion Criteria
1.  `[Criterion 1]`
2.  `[Criterion 2]`

### Exclusion Criteria
1.  `[Criterion 1, e.g., Pregnancy]`
2.  `[Criterion 2, e.g., Severe Comorbidities]`

---

## I - Intervention (Exposure)

### Primary Intervention
-   **Name**: `[e.g., Metformin 500mg BID]`
-   **Type**: `[Drug / Procedure / Exposure / Behavioral]`
-   **Dosage/Frequency**: `[If applicable]`
-   **Duration**: `[e.g., 12 weeks]`

---

## C - Comparison (Control)

### Comparator
-   **Name**: `[e.g., Placebo / Standard of Care / No Treatment]`
-   **Type**: `[Placebo / Active Comparator / Usual Care]`

### Auditor Validation
> [!IMPORTANT]
> **Is this a valid clinical comparator?**
> -   `[ ]` **Yes**: Comparator represents a clinically relevant alternative (Placebo, Gold Standard, or Usual Care).
> -   `[ ]` **No (Strawman)**: Comparator is weak or undefined. **Action Required: Revise.**

-   **Justification**: `[Explain why this comparator is appropriate.]`

---

## O - Outcome

### Primary Outcome
| Property | Value |
| :--- | :--- |
| **Name** | `[e.g., HbA1c Level]` |
| **Metric/Unit** | `[e.g., Percentage (%), Mean Change]` |
| **Measurement Timepoint** | `[e.g., Baseline vs. 12 Weeks]` |
| **Clinical Significance Threshold** | `[e.g., Δ ≥ 0.5%]` |

### Secondary Outcomes
1.  `[e.g., Fasting Blood Glucose (mg/dL)]`
2.  `[e.g., Body Weight (kg)]`
3.  `[e.g., Adverse Event Rate]`

---

## Study Design

| Property | Value |
| :--- | :--- |
| **Study Type** | `[e.g., Randomized Controlled Trial (RCT) / Prospective Cohort / Case-Control]` |
| **Blinding** | `[e.g., Double-Blind / Single-Blind / Open-Label]` |
| **Setting** | `[e.g., Multi-center, Hospital-based]` |
| **Anticipated Sample Size** | `[e.g., N = 200]` |

---

## Hypothesis

### Null Hypothesis (H₀)
> `[e.g., There is no significant difference in HbA1c levels between the Intervention and Control groups at 12 weeks.]`

### Alternative Hypothesis (H₁)
> `[e.g., The Intervention group will show a statistically significant reduction in HbA1c levels compared to the Control group at 12 weeks.]`

---

## Approval Status

-   `[ ]` **PICO_FINALIZED**: All elements are complete and validated. Ready for Gap Analysis.

