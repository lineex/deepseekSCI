# Integrated supporting reference: mimicr-agent/references/study-template-and-modules.md

> Embedded source: `embedded-source/mimicr-agent/references/study-template-and-modules.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# MIMIC 研究模板与模块映射

## 固定研究模板

把任何用户输入都先映射成这个结构：

```text
[MIMIC研究模板 - 待确认]

1. 研究题目：
2. 研究目的：
3. 数据源与版本：MIMIC-IV / hosp / icu / ed / 其他
4. 研究设计：横断面 / 队列 / 生存分析 / 预测建模
5. 目标人群与队列入口：
6. 纳入标准：
7. 排除标准：
8. 暴露变量：
9. 结局变量：
10. 协变量：
11. 关键诊断/药物/操作定义：
12. 关键提取时间窗：
13. 是否需要 ICU 第1天或第n天汇总：是/否
14. 是否需要连续时序数据：是/否
15. 是否需要缺失值处理：是/否
16. 是否需要生存分析：是/否
17. 是否需要亚组/交互分析：是/否
18. 是否需要限制性立方样条：是/否
19. 统计方法：
- 描述性分析
- 线性 / Logistic / Cox
- RCS
- 分层分析
- 敏感性分析
20. 待确认问题：
- 逐条列出
```

如果用户原始方案更细，就保留更细的内容，但仍然映射到这个固定结构。

## 代码生成前必须完成的查找

1. 找函数
   - `mimicr_params.R search <term>`
2. 找 help/topic/alias
   - `mimicr_params.R topics <term>`
3. 看函数参数规范
   - `mimicr_params.R show --fn <function>`
4. 看核心参考
   - `mimicr-core-functions.md`
   - `mimicr-functions.tsv`
   - `mimicr-arguments.tsv`

## 模块触发规则

### 路径、启动、数据库准备

当用户需要初始化环境、配置数据库根目录或检查工作路径时，优先看：

- `config_path`
- `get_path`
- `mimic_start`

### 原始表抽取

当研究需要 admissions/patients/icustays/diagnoses/procedures/pharmacy/labs 等基础表时，优先看：

- `db_*`

常见入口：

- `db_patients`
- `db_admissions`
- `db_icustays`
- `db_diagnoses_d.hadm`
- `db_procedures_d.hadm`
- `db_lab_D.subj.t`
- `db_input.events_D.icu.t`
- `db_output.events_d.icu.t`
- `db_prescriptions_D.hadm.t`

### ICU 时序

当方案要求住院期间逐时点、逐事件或时间窗提取，优先看：

- `dt_*`

常见入口：

- `dt_icustays.detail`
- `dt_icustays.hourly`
- `dt_VitalSign_icu.t`
- `dt_ventilation_icu.t`
- `dt_urine.output_icu.t`
- `dt_crrt_icu.t`

### ICU 第1天或第n天汇总

当方案要求 `day 1` 或 `前24小时` 汇总指标时，优先看：

- `d1_*`
- `day1_icu`
- `dayn_icu`

常见入口：

- `d1_lab_icu`
- `d1_VitalSign_icu`
- `d1_GCS_icu`
- `d1_sofa_icu`
- `d1_saps2_icu`
- `d1_aps3_icu`

### 诊断与疾病定义

当方案需要 CKD/AKI/ARDS/感染/卒中/糖尿病 等定义时，优先看：

- `diag_*`

### 派生指数和评分

当方案需要 Charlson/eGFR/SOFA/MELD/GCS 等指数或评分时，优先看：

- `dex_*`

### 药物暴露

当方案需要抗生素、升压药、ACEI/ARB、利尿剂等用药定义时，优先看：

- `drug_*`
- `d1_*pre_hadm*`
- `d1_*input_icu*`

### 结局

当方案需要 ICU 死亡、住院死亡、n日死亡等结局时，优先看：

- `death_*`

### 建模与图形

当方案进入结果分析阶段，优先看：

- `crude.Model.n`
- `reg_table`
- `RCS`
- `km_plot`
- `forestplot`
- `Qnplot`
- `Rnplot`

### 缺失值

当方案需要插补或缺失值概览时，优先看：

- `missValue`
- `mice2`
- `missForest2`
- `missvalue_knn`

## 代码生成顺序

确认后，优先按这个顺序生成模块：

1. `00_setup.R`
2. `01_cohort.R`
3. `02_exposure.R`
4. `03_outcome.R`
5. `04_covariates.R`
6. `05_model.R`
7. `06_visualize.R`
8. `reports/analysis_report.qmd`

结尾固定提醒：

```text
请确认是否按此模板生成代码，或直接指出需要修改的字段。只有在我确认后，你才能进入代码生成阶段。
```

