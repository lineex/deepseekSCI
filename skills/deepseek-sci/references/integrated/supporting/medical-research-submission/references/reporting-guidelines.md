# Integrated supporting reference: medical-research-submission/references/reporting-guidelines.md

> Embedded source: `embedded-source/medical-research-submission/references/reporting-guidelines.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# Reporting Guidelines（报告规范与清单）

投稿"直接可用"的前提：按研究类型执行对应报告规范，清单随稿附上并逐条标注位置。总入口：EQUATOR Network（equator-network.org）。

## 1. 研究类型 → 指南映射

| 研究类型 | 指南 | 版本 | 条目 | 关键要求 |
|---|---|---|---|---|
| 随机对照试验 | CONSORT | 2010 | 25 + 流程图 | 随机化方法、分配隐藏、盲法、流失图 |
| 队列研究 | STROBE | 2007 | 22 | 暴露/结局定义、随访完整性、偏倚处理 |
| 病例对照研究 | STROBE | 2007 | 22 | 匹配策略、暴露测量、选择偏倚 |
| 横断面研究 | STROBE | 2007 | 22 | 抽样、应答率、患病率 |
| 系统评价/Meta分析 | PRISMA | 2020 | 27 + 流程图 | 检索式全文、筛选流程、偏倚风险、GRADE |
| 预后模型 | TRIPOD | 2015 | 22 | 模型构建/验证分离、校准与判别、缺失数据处理 |
| 诊断准确性 | STARD | 2015 | 30 | 金标准、盲法判读、2×2 表 |
| 常规数据库研究（MIMIC/NHANES/医保/EMR） | RECORD | 2015 | STROBE+13 | 数据来源描述、纳入排除的编码规则、链接方法 |
| 动物实验 | ARRIVE | 2020 | 21 | 随机化、盲法、样本量计算 |
| 卫生经济学 | CHEERS | 2022 | 28 | 视角、成本、贴现、敏感性分析 |

## 2. 数据库研究特别提醒（MIMIC/NHANES 适用）

- **必须**用 RECORD（STROBE 扩展），不是裸 STROBE：补充了数据来源版本、变量提取的代码/规则、重复与缺失处理、数据可用性声明。
- MIMIC：写明版本（如 MIMIC-IV v2.2）、使用许可（PhysioNet credential）、提取 SQL/脚本公开链接、符合 HIPAA 的说明、伦理豁免理由。
- NHANES：写明调查周期（如 2011–2018）、合并周期的权重处理（见 `nhanesr-auto-params`）、复杂抽样设计（strata/PSU/weight）。

## 3. 使用流程

1. 稿件定稿后，选定对应指南（可叠加：如数据库队列 = RECORD）。
2. 逐条核对，在清单上标注**页码/行号/表格图号**（`checklist_*.docx|pdf`）。
3. 每条必须给出位置或明确"不适用（NA+理由）"，禁止空表声称遵循。
4. 清单作为补充文件随投稿包上传，并在 cover letter 中声明。

## 4. PRISMA 2020 核心条目（Meta 分析必查）

- 标题标明系统评价；结构化摘要含背景/方法/结果/讨论。
- 检索式全文可复现（数据库、日期、全部检索词、过滤器）。
- 流程图：识别 → 筛选 → 纳入（含排除原因计数）。
- 偏倚风险：RCT 用 RoB 2，观察性用 ROBINS-I。
- 合成：效应量类型、随机/固定效应模型与理由、异质性（I²）、亚组/敏感性分析。
- 发表偏倚：漏斗图 + Egger 检验（≥10 篇时）。
- 证据确定性：GRADE 分级并附理由。

## 5. CONSORT 2010 核心条目（RCT 必查）

- 流程图（登记→随机→干预→随访→分析）与各阶段流失人数。
- 随机序列生成方法、分配隐藏机制、实施者、盲法对象与破盲。
- 样本量计算（效应量依据、α、power）。
- 主要/次要结局定义与测量时点；结局修改需披露。
- 意向性分析（ITT）为主，补充符合方案分析。
- 不良事件报告；试验注册号（ClinicalTrials.gov/ChiCTR）。

## 6. TRIPOD 核心条目（预后模型必查）

- 明确区分模型**开发**与**外部验证**（或内部验证方法：bootstrap/CV）。
- 报告样本量、事件数/参数比（EPV）。
- 缺失数据处理方法；连续变量是否假设线性。
- 判别（C 统计量/AUC）与校准（校准图/Hosmer-Lemeshow）都要报。
- 模型公式/评分表完整呈现（可临床应用）。

## 7. 与其它技能联动

- 系统评价复刻：`review-replica-agent`（对照金标准逐阶段比对）。
- 可行性评估：`review-feasibility-to-meta`。
- 引用核验：`_shared/citation-verification-protocol.md`。

