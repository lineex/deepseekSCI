---
name: deepseekSCI
description: "DeepSeek++ 医学与科学研究 Plan-Execution 双模式闭环 Agent Skill。涵盖 PICO 课题构思、文献检索/综合/Meta分析 (Path A) 以及 NHANES/MIMIC 大数据库挖掘、本地 R 语言稳健统计分析、出版级矢量图表创作、文献真伪校验全流程 (Path B)，最终直接产出发表级 SCI 论文。"
---

# deepseekSCI: 医学与科学研究 Plan-Execution 闭环 Protocol

本 Skill 为 DeepSeek++ / Antigravity 提供专业的医学与科学研究 Agent 工作流，涵盖 Plan 模式与 Execution 模式的双向闭环迭代，旨在加速从科研思路到可直接发表 SCI 论文的全流水线。

---

## 🎯 核心闭环架构：Plan 模式与 Execution 模式迭代循环

```
                      ┌─────────────────────────┐
                      │    Plan 模式 (设计)     │
                      │ 需求构建 / 问题规范 / DAG│
                      └────────────┬────────────┘
                                   │
                         制定方案与指令派发
                                   │
                                   ▼
                      ┌─────────────────────────┐
                      │   Execution 模式 (执行) │
                      │ 本地 R/Python / 数据库挖掘│
                      └────────────┬────────────┘
                                   │
                         数据反馈与结果评估
                                   │
                                   └────────────► 方案优化与轮次迭代
```

### 1. Plan 模式（需求构建与方案设计）
- **规范科研问题**：使用 PICO (Population, Intervention/Exposure, Comparator, Outcome) 或 PECO 框架将用户思路标准化为严格的科研假设。
- **因果关系与 DAG 构建**：在数据分析或文献抽取前，显式绘制有向无环图 (DAG)，明确暴露因素、结局变量、混杂因子 (Confounders)、中介因子 (Mediators) 和碰撞因子 (Colliders)。
- **分析/检索 Plan 制定**：明确所使用的数据库 (NHANES/MIMIC/PubMed等)、R 语言统计模型策略（加权Logistic/Cox/RCS/PSM）及敏感性分析路径。

### 2. Execution 模式（工具驱动与数据分析执行）
- **工具调用与执行**：驱动本地 Native Host (`shell`, `python_exec`, `Rscript`) 进行代码运行、文献检索与数据提取。
- **结果捕获与质量控制**：实时捕获代码输出结果、统计诊断指标（模型收敛性、$I^2$ 异质性、共线性 VIF 值等）。

### 3. 闭环迭代机制
- 若 Execution 模式中遇到收敛失败、混杂偏倚或异质性过高，**必须返回 Plan 模式**更新调整控制变量或统计模型，重新生成改进后的方案，实现“设计-执行-反馈-再优化”的自动化科研加速。

---

## 🔬 流水线 1：文献综述与 Systematic Review / Meta 分析 (Path A)

适用于无原始数据、基于已有文献进行二次合成的科研课题，目标为产出直接达到发表标准的 Meta 分析或 Systematic Review。

### 阶段与步骤：
1. **科研思路与文献检索 (Idea & Literature Search)**
   - 调用文献检索工具 (`pubmed-database`, `literature-search-openalex`, `literature-search-europepmc`, `ch-search`, `wos_lit_mining`) 构建精准 Mesh 词与主题词组合。
2. **文献综合与偏倚风险评价 (Literature Synthesis & Risk of Bias)**
   - 提取纳入文献的核心数据（样本量、研究设计、HR/OR/RR 及其 95% CI）。
   - 调用 `review-feasibility-to-meta` 与 `ai-peer-reviewer` 进行 ROB2 (RCT) 或 ROBINS-I (观察性研究) 工具测评。
3. **Meta 分析与数据计算 (Meta-Analysis Statistics)**
   - 使用 R 语言 (`meta` / `metafor` 包) 进行固定效应与随机效应模型计算，输出异质性指数 ($I^2, \tau^2$)、Eggr/Begg 发表偏倚检验及剪补法 (Trim-and-Fill) 分析。
4. **文献真实性校验 (Fact & Citation Verification)**
   - 调用 `reference-intelligence-mining` 与 `citing-papers-intelligence` 校验每一个引用文献的 PMID/DOI，严格防止 AI 假文献幻觉。
5. **图表创作与顶刊润色 (Publication-ready Figures & Polish)**
   - 生成高清矢量图：PRISMA 流程图、森林图 (Forest Plot)、漏斗图 (Funnel Plot)。
   - 调用 `bachert-academic-polish` / `bilingual-academic-writer` / `manuscript-writing-polish-format` 完成整篇论文的模块化撰写与学术润色，形成可直接投递的论文初稿。

---

## 📊 流水线 2：医学大数据库挖掘与观察性研究 (Path B)

适用于利用 **NHANES**、**MIMIC-IV** 等公开临床数据库进行横断面 (Cross-Sectional) 或纵向队列 (Longitudinal Cohort) 研究，目标为产出包含完整数据分析与验证的高水平 SCI 论文。

### 阶段与步骤：
1. **课题构思与因果分析 (Study Design & DAG)**
   - 确定暴露变量、结局变量及协变量。显式构建倾向性评分匹配 (PSM) 或逆概率加权 (IPW) 策略。
2. **数据库挖掘与抽取 (Database Mining)**
   - **NHANES 数据库**：调用 `nhanesr-research-agent`、`nhanesr-auto-params` 与 `nhanesr-function-reference` 进行多周期数据合并、复杂抽样权重设定 (`WTMEC2YR` / `WTINT2YR`) 与变量清洗。
   - **MIMIC 数据库**：调用 `mimicr-agent` 进行 ICU/住院患者 Cohort 构建、时间窗口定义及异常值插补。
3. **驱动本地 R 语言完成稳健统计分析 (Local R Data Analysis)**
   - 调用 `Execute Shell Command` / `Execute Python Code` / 本地 RScript 引擎，运行以下严谨统计分析代码：
     - **基线分析**：复杂抽样/加权 Table 1 生成。
     - **回归模型**：多因素 Logistic 回归、Cox 比例风险模型、多重线性回归。
     - **非线性探索**：限制性立方样条 (Restricted Cubic Splines, RCS) 寻找剂量-效应关联与转折点 (Inflection Points)。
     - **亚组与交互作用分析**：Subgroup Analysis & Interaction Tests。
     - **敏感性分析**：E-value 计算、未测混杂因子敏感性分析。
4. **高质量图表绘制 (Publication-ready Visualizations)**
   - 自动生成出版级图表：基线表 (Table 1)、多因素分析森林图、RCS 剂量-效应关联图、K-M 生存曲线。
5. **文章撰写、真实性验证与审稿打磨 (Drafting, Verification & Polish)**
   - 根据数据分析结果自动撰写 Introduction, Methods, Results, Discussion。
   - 调用 `ai-peer-reviewer` 进行 SCI 审稿人视角的严格模拟评估（检查统计是否完备、讨论是否深入）。
   - 完成文献 PMID 严格真实性校验与学术语言润色，产出可以直接发表的完整 SCI 论文初稿。

---

## 🛠️ 已集成技能库 (Loaded Skill Mapping)

环境已无缝导入以下专业科研技能：
- **科研架构与选题**：`medical_research_architect`, `nsfc-topic-ideation`, `patent-topic-recommendation`
- **数据库挖掘 (NHANES/MIMIC)**：`nhanesr-research-agent`, `nhanesr-auto-params`, `nhanesr-function-reference`, `mimicr-agent`
- **统计与分析引擎**：`medical-stat-project-agent`, `stat-project-agent`
- **文献综述与 Meta 分析**：`medical-review-writing`, `review-feasibility-to-meta`, `critical-care-review-master`, `narrative-review-replication`
- **论文撰写、润色与审稿**：`bilingual-academic-writer`, `bachert-academic-polish`, `manuscript-writing-polish-format`, `ai-peer-reviewer`
- **图表创作与文献校验**：`nanadraw-biomedical-mcp`, `citing-papers-intelligence`, `reference-intelligence-mining`, `wos_lit_mining`
