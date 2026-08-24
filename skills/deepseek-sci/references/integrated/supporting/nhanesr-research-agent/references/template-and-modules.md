# Integrated supporting reference: nhanesr-research-agent/references/template-and-modules.md

> Embedded source: `embedded-source/nhanesr-research-agent/references/template-and-modules.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# NHANES template and module mapping

## Fixed template fields

Use this field map when normalizing user input:

- `研究题目`: brief title, can be inferred from exposure + outcome if needed
- `研究目的`: one or two sentences
- `研究设计`: choose from cross-sectional, cohort, mortality follow-up
- `研究周期`: keep as user-specified cycle span
- `研究对象`: target population
- `纳入标准` / `排除标准`: explicit screening rules
- `暴露变量`
- `结局变量`
- `协变量`
- `是否需要饮食数据`
- `是否需要补充剂数据`
- `是否需要死亡结局`
- `是否需要亚组分析`
- `是否需要加权分析`
- `是否需要年龄标化`
- `统计方法`
- `待确认问题`

## Module triggers

### Dietary data

When `是否需要饮食数据 = 是`, prefer:

- `db_drtot()`
- `db_driff()`
- `db_fped()`
- `dex_HEI()`
- `dex_DII()`
- `dex_DASH.Mellen()`
- `dex_OBS()`
- `dex_PRAL.NEAP()`

Be explicit about:

- `day`
- `both2days`
- `dietary`
- `version`
- summary function and join logic

### Supplement data

When `是否需要补充剂数据 = 是`, inspect local `nhanesR` references first and then attach supplement extraction logic as a dedicated module. Keep supplement exposure definitions explicit and mark uncertain supplement windows or ingredient grouping rules as `待确认`.

### Mortality outcome

When `是否需要死亡结局 = 是`, prefer:

- `db_mort()`

Then define:

- time variable
- event indicator
- censoring rule
- Cox or KM modules if requested

### Subgroup analysis

When `是否需要亚组分析 = 是`, keep subgroup variables explicit and prefer:

- subgroup-specific models
- `stratum_model()` where appropriate
- interaction tests when scientifically justified

### Weighted analysis

When `是否需要加权分析 = 是`, always:

1. choose one weight family
2. create or verify the merged-cycle weight
3. build `svy_design()`
4. keep weighted analysis separate from unweighted diagnostics when needed

### Age standardization

When `是否需要年龄标化 = 是`, ask for or infer the target age groups and standard population approach only if low-risk. If the method materially affects the conclusion, list it under `待确认问题`.

### Statistical method mapping

- `描述性分析`: weighted or unweighted summaries, baseline table
- `加权线性回归`: `svyglm(..., family = gaussian())`
- `logistic`: `svyglm(..., family = quasibinomial())`
- `Cox`: survey-compatible survival workflow if available, otherwise explicit follow-up model with explanation
- `限制性立方样条`: `RCS()` or explicit spline workflow
- `分层分析`: subgroup models plus interaction where needed
- `敏感性分析`: alternate coding, alternate exclusions, alternate weight/sample restriction, or complete-case vs other analytic sample logic

