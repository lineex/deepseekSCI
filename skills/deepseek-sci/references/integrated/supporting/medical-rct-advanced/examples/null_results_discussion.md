# Integrated supporting reference: medical-rct-advanced/examples/null_results_discussion.md

> Embedded source: `embedded-source/medical-rct-advanced/examples/null_results_discussion.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# Null Results Discussion Framework
## 5-Step Template for NEJM-Level Reporting

Based on systematic analysis of TTM2, INCEPTION, BOX, TAME trials

---

## Step 1: Direct, Unambiguous Opening

### ✅ DO: Clear Negative Statement

**Template**:
> "In this randomized trial, [intervention] **did not lead to better [outcome]** than [control] in [population]."

**Examples from Published Trials**:

**TTM2**:
> "We found no significant difference in the percentage of patients with a favorable outcome between targeted hypothermia and targeted normothermia."

**TAME**:
> "Targeted mild hypercapnia did not lead to better neurologic outcomes at 6 months than targeted normocapnia."

**BOX**:
> "We found no significant difference between liberal and restrictive oxygenation targets in the composite outcome of death or survival with a poor neurologic outcome."

### ❌ DON'T: Soften or Hedge

**Avoid**:
- "Although the difference did not reach statistical significance..."
- "There was a trend toward benefit..."
- "The results suggest a possible effect..."
- "We observed a numerical advantage..."

**Why**: These phrases imply the trial "almost" showed benefit, undermining the null finding's validity

---

## Step 2: Compare to Contemporary Trials (Evidence Network)

### ✅ DO: Cite 2-3 Recent Trials

**Template**:
> "Our findings are [consistent | inconsistent] with [Trial A] and[Trial B]. In [Trial A, context], [brief result]. However, our trial differed in [key aspect]."

**Table Format** (preferred for major discrepancies):

| Trial | Design | Population | N | Result | Key Difference |
|-------|--------|-----------|---|--------|----------------|
| **Your Trial** | [Multicenter RCT] | [Population] | [N] | [Null] | - |
| Trial A | [Design] | [Population] | [N] | [Positive/Null] | [Difference] |
| Trial B | [Design] | [Population] | [N] | [Positive/Null] | [Difference] |

**INCEPTION Example**:

```markdown
### Comparison to Previous ECPR Trials

Our findings contrast with the ARREST trial but align with the Prague OHCA study:

| Trial | Setting | N | Control Group Survival | ECPR Effect |
|-------|---------|---|----------------------|-------------|
| **INCEPTION** | 10 centers, Canada | 134 | 31% ROSC rate | No benefit (RR 1.4, P=0.52) |
| ARREST | Single center, US | 30 | 7% survival | Large benefit (RR 2.9) |
| Prague | Single center, Czech | 256 | Similar to INCEPTION | No benefit |

The higher control group success rate in INCEPTION (31% ROSC) likely reflects...
```

### ❌ DON'T: Ignore Conflicting Evidence

**Avoid**:
- Citing only trials that agree with your result
- Dismissing positive trials without explanation
- Claiming your trial supersedes all prior evidence

---

## Step 3: Explain Discrepancies with EXACTLY 3 Rational Explanations

### The Framework

When your result contradicts a prior positive trial, provide **exactly 3** explanations spanning:

1. **Population/Context Differences**
2. **Intervention/Control Differences**
3. **Outcome Measurement/Timing Differences**

### ✅ Example: INCEPTION vs ARREST

**Population Difference**:
> "ARREST enrolled highly selected patients in a single, high-volume ECPR center with standardized protocols. INCEPTION's multicenter design included varied center experience and patient populations."

**Control Group Difference**:
> "The control group in ARREST had a 7% survival rate, compared to 31% who achieved ROSC in INCEPTION, suggesting more effective conventional CPR in our trial."

**Timing/Logistics Difference**:
> "Time from arrest to ECMO cannulation was longer in INCEPTION (median 74 min) than in ARREST (median 42 min), potentially reducing ECPR's efficacy window."

### ✅ Example: BOX vs ICU-ROX Subgroup

**Population**:
> "ICU-ROX enrolled general ICU patients with varying acuity; BOX exclusively enrolled comatose cardiac arrest survivors with hypoxic-ischemic brain injury."

**Intervention**:
> "ICU-ROX targeted oxygen broadly (SpO₂ 90-97%); BOX used precise PaO₂ targets (9-10 kPa vs 13-14 kPa) with protocolized FiO₂ adjustments."

**Outcome**:
> "ICU-ROX's subgroup analysis included only 166 patients with ischemic encephalopathy and was not powered for definitive conclusions."

### ❌ DON'T:

- Provide <3 or >3 explanations (3 is the magic number for credibility)
- Be vague ("populations were different")
- Be defensive ("our trial was better designed")

---

## Step 4: Subgroup Analysis - Show but Don't Over-Interpret

### ✅ DO: Present Forest Plot, State Consistency

**Template**:
> "The results appeared to be consistent across prespecified subgroups (Figure 3), and there was no interaction with [other intervention if factorial]."

**Figure Requirements**:
- Forest plot showing RR/HR for each subgroup
- Interaction P-values listed
- NO highlighting of "trends"

**Text**:
- State "consistent across subgroups"
- Report interaction P-values
- If P_interaction <0.05, acknowledge but don't overstate

**TAME Example**:
> "The results appeared to be consistent across prespecified subgroups defined by sex, age, time to ROSC, initial cardiac rhythm, and shock status (Figure 2)."

### ❌ DON'T: Cherry-Pick "Promising" Subgroups

**Avoid**:
> "Although the overall trial was negative, we observed a trend toward benefit in elderly patients (P_interaction=0.18)..."

**Why**: This undermines the primary finding and invites false hope

**Exception**: Only discuss subgroup if:
- P_interaction <0.01 AND
- Biologically plausible AND
- Consistent with other outcomes AND
- Explicitly stated as "hypothesis-generating only"

---

## Step 5: Definitive Conclusion (NOT "More Research Needed")

### ✅ DO: State Definitive Conclusion

**Template**:
> "[Intervention] did not improve [outcome] compared with [control] in [population]."

**Stronger Version** (if sample size was adequate):
> "These findings do not support the use of [intervention] for [indication] in [population]."

**Examples**:

**TTM2**:
> "Targeting a core temperature of 33°C did not lead to a lower incidence of death by 6 months than targeting normothermia."

**BOX**:
> "Targeting a restrictive or liberal oxygenation strategy... resulted in a similar incidence of death or severe disability or coma."

**TAME**:
> "Targeted mild hypercapnia did not lead to better neurologic outcomes at 6 months than targeted normocapnia."

### ❌ DON'T: Hedge with "Future Research"

**Avoid**:
> "Larger trials may be needed to detect smaller but clinically meaningful effects."

**Why**: 
- Implies your trial was inadequate
- Suggests there's still hope (when evidence says no)
- Wastes future research resources

**Exception**: Only say "future research" if:
- You found a safety signal needing investigation OR
- Novel subgroup hypothesis emerged (clearly labeled exploratory) OR
- Mechanistic question remains despite null clinical effect

### Special Case: When Sample Size Was Truly Inadequate

**If**:
- Trial stopped early for futility OR
- Wide confidence intervals OR
- Power <70% for planned effect size

**Then**:
> "The trial was underpowered to detect small effects. The 95% CI ([[lower]] to [upper]) cannot exclude a modest [benefit/harm]."

**But don't say**: "A larger trial is needed"

**Instead**: Quantify the uncertainty and move on

---

## Complete Example: Null Results Discussion

### Trial: Hypothetical Drug X for Sepsis

**Opening** (Step 1):
> "In this multicenter trial, Drug X did not reduce 28-day mortality compared with placebo in patients with septic shock."

**Context** (Step 2):
> "Our findings contrast with the single-center DRUG-X PILOT trial (N=120), which reported a 15% absolute mortality reduction. However, two contemporaneous trials in critical care populations also found no benefit: the SEPSIS-DRUG trial (N=800, RR 0.95, 95% CI 0.82-1.10) and the ICU-RESCUE trial (subgroup analysis, N=450)."

**Explanations** (Step 3):
> "Several factors may explain the discrepancy with DRUG-X PILOT. First, our trial enrolled patients with higher baseline APACHE II scores (mean 28 vs 22), reflecting more severe illness. Second, our control group received more aggressive early fluid resuscitation and antibiotics, consistent with evolving sepsis guidelines implemented between 2020-2024. Third, DRUG-X PILOT administered the drug within 6 hours of shock onset, whereas 35% of our patients received it at 6-12 hours due to pragmatic enrollment procedures."

**Subgroups** (Step 4):
> "Results were consistent across prespecified subgroups defined by baseline lactate, time to treatment, and source of infection (Figure S4). Although point estimates suggested possible heterogeneity by renal function (P_interaction=0.08), this was not statistically significant and should be considered hypothesis-generating."

**Conclusion** (Step 5):
> "Drug X did not reduce mortality in patients with septic shock. These findings do not support routine use of Drug X in this population."

---

## Quick Checklist

Before submitting null results Discussion:

- [ ] Opening sentence clearly states "did not" language
- [ ] Cited 2-3 contemporary trials in similar domain
- [ ] If conflicting with prior positive trial, provided exactly 3 explanations
- [ ] Forest plot included for subgroups
- [ ] Stated "consistent across subgroups"
- [ ] Did NOT selectively highlight "trend" subgroups
- [ ] Conclusion is definitive (not "more research needed")
- [ ] Overall tone is confident, not defensive

---

## Common Pitfalls

### Pitfall 1: The "Almost Significant" Trap
❌ "The P-value of 0.07 approached statistical significance"
✅ "No significant difference was observed (P=0.07)"

### Pitfall 2: The "Underpowered" Excuse
❌ "Our trial may have been underpowered for this effect size"
✅ State the CI limits and accept the null (unless truly stopped early)

### Pitfall 3: The "Biomarker Showed Promise" Distraction
❌ "Although the clinical outcome was null, we observed promising biomarker trends"
✅ Report biomarkers but don't emphasize in Discussion if primary was null

### Pitfall 4: The "Subgroup Savior"
❌ "The overall result was negative, but elderly women showed a trend..."
✅ Show forest plot, state consistency, move on

### Pitfall 5: The "Call for Bigger Trial"
❌ "A larger trial with greater power may detect smaller effects"
✅ "Our trial does not support [intervention] for [indication]"

---

**End of Null Results Framework**

**Key Principle**: Null results deserve confident, definitive reporting - not defensive hedging.

