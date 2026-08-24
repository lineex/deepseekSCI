# Discovery and Feasibility

## 1. Start from the scientific problem

Translate the user's input into:

- clinical/scientific burden;
- decision or mechanism that remains uncertain;
- population and setting;
- potentially modifiable exposure, intervention or process;
- outcome meaningful to patients or practice;
- available data or feasible collection route.

Do not start with a fashionable method or available variable. A method is useful only if it resolves a real inferential or clinical problem.

## 2. Build a current landscape

Run a dated, reproducible horizon scan before claiming novelty:

1. find recent systematic reviews, guidelines and pivotal primary studies;
2. identify ongoing or recently completed trials and protocols;
3. trace references backward and citations forward for anchor studies;
4. map population, exposure/intervention, comparator, outcome, time, setting, design and estimand;
5. record contradictory and null evidence, not only supportive papers.

Separate “no direct study identified in searched sources as of DATE” from “never studied.”

## 3. Generate candidates with explicit gap mechanisms

Use one or more productive gap types:

- **clinical contradiction**: observed practice or outcome conflicts with prevailing expectation;
- **mechanistic bridge**: plausible pathway has not been connected to patient-level outcomes;
- **timing/trajectory**: static measurement misses evolution, treatment timing or landmark state;
- **measurement state**: assay/phenotype changes with treatment, sedation, support or sampling context;
- **heterogeneity**: average effect may conceal prespecified effect modifiers;
- **transportability**: evidence does not generalize across population, center or resource setting;
- **implementation delay**: recognition, decision and execution intervals may be modifiable;
- **comparative strategy**: real-world comparator differs from “ever versus never” exposure;
- **negative evidence**: a plausible intervention repeatedly fails, suggesting a revised construct or estimand;
- **method validity**: leakage, informative testing, competing events, non-positivity or misclassification distort conclusions.

For every candidate, write a falsifiable one-sentence hypothesis and the smallest credible study that could test it.

## 4. Score, then challenge

Score 0-4 with written evidence for each dimension:

| Dimension | Question |
|---|---|
| Importance | Would resolving this change knowledge, decisions or patient-relevant outcomes? |
| Novelty | Is the estimand or mechanism genuinely different from current evidence? |
| Actionability | Is there a modifiable decision, process or intervention? |
| Identifiability | Can the target contrast be estimated without fatal design bias? |
| Data fit | Are variables, timing, units and follow-up available? |
| Event support | Is sample/event burden adequate for the primary model? |
| Feasibility | Can the work finish with available resources and access? |
| Transportability | Is the result likely to matter beyond one idiosyncratic sample? |

Do not use the total score mechanically. A fatal flaw in identifiability, event support or measurement invalidates a high total.

## 5. Denominator-first feasibility

Before making a rare phenotype primary, count sequentially:

```text
source population
-> eligible population
-> exposure/intervention groups
-> valid time-zero records
-> complete primary-outcome records
-> primary events by group
-> complete candidate covariates
```

Report missingness and measurement frequency by exposure, severity and outcome. Repeated testing is often informative. If a strict phenotype produces weak event support, use a broader primary cohort and retain the phenotype as a prespecified subgroup or enrichment strategy.

For prospective work, define the minimum shared CRF and one index sampling time before treatment when timing affects classification.

## 6. Novelty verification matrix

Create `discovery/novelty_matrix.csv` with:

```text
candidate_id,direct_review_found,direct_primary_found,ongoing_trial_found,
population_difference,exposure_difference,comparator_difference,outcome_difference,
time_or_setting_difference,estimand_difference,remaining_gap,search_date,confidence
```

Novelty is claim-specific. A topic can be familiar while a timing, comparator or estimand remains new.

## 7. Minimum viable validation

Choose the smallest test that could overturn enthusiasm:

- database query for denominator/event counts;
- codebook audit for variable and timing availability;
- 20-50 record chart pilot for abstraction reliability;
- search pilot for eligible study count and extractable effects;
- negative-control or falsification endpoint;
- simulation based on plausible parameters for power/precision;
- external sample or temporal split for transportability.

Record a go/pivot/stop decision with evidence. Do not rescue a weak question by adding many secondary outcomes.

## 8. Candidate output

Rank no more than five candidates and recommend one. Each row should include:

```text
rank | question | hypothesis | gap mechanism | target estimand | data source |
expected denominator/events | main bias | minimum validation | decision
```

Then create a concise topic brief containing rationale, primary question, clinical/scientific value, design, minimum dataset, main risk and immediate next action.
