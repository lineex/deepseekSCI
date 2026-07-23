---
name: deepseekSCI
description: "DeepSeek++ 医学与科学研究 Plan-Execution 双模式闭环 Agent Skill。融合【浏览器控制自动化 (Browser Control)】与全套文献数据库 Skill（PubMed, Embase, Web of Science, Cochrane, Scopus, ScienceDirect, IEEE Xplore, Google Scholar等）。严格遵守【零模拟数据、零步骤跳过、全量摘要提取与全文阅读、100%真实性】红线，实现自动操控浏览器进行精准检索与信息提取，涵盖 Meta 分析 (Path A) 与 NHANES/MIMIC 大数据库挖掘及 R 语言分析 (Path B)，直接产出发表级 SCI 论文。"
---

# deepseekSCI: 医学与科学研究 Plan-Execution 闭环 Protocol

本 Skill 为 DeepSeek++ / Antigravity 提供专业的医学与科学研究 Agent 工作流，涵盖 Plan 模式与 Execution 模式的双向闭环迭代。

---

## 🚨 核心原则：科研真实性与全量文献检索/全文分析禁令 (Mandatory Research Integrity)

> [!IMPORTANT]
> **本 Protocol 适用最高标准的学术诚信规范，任何违反以下红线的行为均视为严重违规：**

1. **🚫 零模拟/虚假数据禁令 (Zero Mock Data Policy)**
   - **绝对禁止**伪造、拼接、或使用 `set.seed()`/`rnorm()` 等代码生成任何形式的模拟数据、Mock 对象或虚假数值。
   - 所有分析结果（如 HR/OR/RR、95% CI、$p$ 值、$I^2$ 异质性等）**必须 100% 源自真实的本地 R / Python 脚本对真实 NHANES、MIMIC 数据库或文献真机抽取的运行输出**。
   - 缺失值必须通过标准的多重插补 (Multiple Imputation) 或完备病例分析处理，严禁人工编造填补。

2. **🌐 浏览器操控驱动全量检索 (Browser Control Driven Search & Extraction)**
   - **严格联动 DeepSeek++ 浏览器控制能力 (`browser_*` 工具)**：根据文献 Skill 提供的检索语法与操作方向，自动挂载与操控浏览器标签页（PubMed, IEEE Xplore, Embase, Web of Science, Cochrane, Scopus, ScienceDirect, Google Scholar）。
   - **自动导航、翻页与提取**：在网页输入框自动填充精准 Boolean 检索式，逐页导航，从 DOM / 文本快照中提取**每一篇文献的标题、作者、DOI 及完整摘要 (Abstract)**，严禁任何手动或代码层面的中途截断。

3. **📚 全量文献检索与摘要获取禁令 (Full-Coverage Literature & Abstract Retrieval)**
   - **绝对禁止“仅获取前 10 篇 / 前 20 篇”等偷工减料行为**。
   - 文献检索阶段必须构建精准的检索式，对于检索命中的每一篇相关文献，**必须 100% 获取其摘要 (Abstract) 进行完整初筛**。
   - 明确认可：全量检索与逐篇摘要抓取虽然消耗较多时间与流量，但必须严格执行，不容打折。

4. **📄 纳入文献 100% 全文阅读与深度提取 (Mandatory Full-Text Analysis)**
   - 对于经过摘要初筛符合纳入标准的文献，**必须 100% 获取全文 (Full Text)**（调用 `pm-fulltext`, `gs-fulltext`, `scopus-fulltext` 或通过浏览器控制导航至 PMC/Sci-Hub/出版社页面下载）。
   - **绝对禁止仅凭摘要信息推断结论或填报 Meta 数据**。必须深入全文 Methods、Results 及附表提取样本量、调整后 HR/OR/RR 及其 95% CI。

5. **🪜 零步骤跳过原则 (Complete Step-by-Step Execution)**
   - **绝对禁止**为了追求速度而跳过研究流程中的任何一步。
   - 必须完整按顺序执行：**假说建立 $\rightarrow$ 因果 DAG 构造 $\rightarrow$ 浏览器操控全量检索与逐篇摘要提取 $\rightarrow$ 纳入文献全文获取与深度分析 $\rightarrow$ ROB2/ROBINS-I 偏倚评价 $\rightarrow$ R 语言 Meta 建模 $\rightarrow$ 真实性校验 $\rightarrow$ 论文撰写**。
   - **宁慢勿错，每一步骤必须输出完整诊断日志**。

6. **🔍 100% 真实性与防 AI 幻觉校验 (100% Fact & Citation Verification)**
   - 论文引用的每一篇参考文献必须经由 `pm-paper-detail` / `reference-intelligence-mining` 校验真实 PMID / DOI / Accession ID，**严禁任何 AI 幻觉生成的虚假文献**。
   - 论文 Results 部分引用的每一个统计数字必须与本地 R / Python 控制台的日志输出或原文数据 **0 误差对应**。

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
                      │ 浏览器控制自动化检索与提取 │
                      └────────────┬────────────┘
                                   │
                         数据反馈与结果评估
                                   │
                                   └────────────► 方案优化与轮次迭代
```

### 1. Plan 模式（需求构建与方案设计）
- **规范科研问题**：使用 PICO (Population, Intervention/Exposure, Comparator, Outcome) 或 PECO 框架将用户思路标准化为严格的科研假设。
- **因果关系与 DAG 构建**：在数据分析或文献抽取前，显式绘制有向无环图 (DAG)，明确暴露因素、结局变量、混杂因子 (Confounders)、中介因子 (Mediators) 和碰撞因子 (Colliders)。
- **分析/检索 Plan 制定**：明确所使用的医学与工程数据库 (NHANES/MIMIC/PubMed/Embase/WOS/IEEE等)、浏览器自动化操控路径、R 语言统计模型策略（加权Logistic/Cox/RCS/PSM）及敏感性分析路径。

### 2. Execution 模式（工具驱动、浏览器自动化与数据分析执行）
- **工具调用与执行**：驱动本地 Native Host (`shell`, `python_exec`, `Rscript`) 进行代码运行；联动浏览器控制 (`browser_*`) 自动导航至各数据库网页执行输入、翻页与摘要/全文数据抽取。
- **结果捕获与质量控制**：实时捕获代码输出结果、统计诊断指标（模型收敛性、$I^2$ 异质性、共线性 VIF 值等）。

### 3. 闭环迭代机制
- 若 Execution 模式中遇到收敛失败、混杂偏倚或异质性过高，**必须返回 Plan 模式**更新调整控制变量或统计模型，重新生成改进后的方案，实现“设计-执行-反馈-再优化”的自动化科研加速。

---

## 🔬 流水线 1：文献综述与 Systematic Review / Meta 分析 (Path A)

适用于无原始数据、基于已有文献进行二次合成的科研课题，结合用户已有的专业医学与工程文献数据库 Skill 矩阵及浏览器自动化控制进行检索与提取，目标为产出直接达到发表标准的 Meta 分析或 Systematic Review。

### 阶段与步骤（不跳过任何一步）：
1. **浏览器操控驱动全量文献/摘要检索 (Browser Control Driven Search & Full Harvesting)**
   - 根据研究需求，自动控制浏览器加载目标数据库页面，填充检索式并抓取数据：
     - **PubMed**: 联动 `pubmed-database` / `pm-search` 与 `browser_*` 操控 `pubmed.ncbi.nlm.nih.gov` 逐页提取。
     - **IEEE Xplore**: 联动 `ieee-xplore-database` 与 `browser_*` 操控 `ieeexplore.ieee.org` 提取工程与 AI 摘要。
     - **Cochrane Library**: 联动 `ch-search` 与 `browser_*` 操控 `cochranelibrary.com` 抓取 Trials 与 Reviews。
     - **Web of Science**: 联动 `wos_lit_mining` 与 `browser_*` 操控 Web of Science 平台检索。
     - **Embase**: 联动 `embase-web-search` 与 `browser_*` 操控 Embase 会话。
     - **Scopus**: 联动 `scopus-search` 与 `browser_*` 操控 Scopus 搜索结果页。
     - **ScienceDirect**: 联动 `sd-search` 与 `browser_*` 操控 Elsevier 平台。
     - **Google Scholar**: 联动 `gs-search` 与 `browser_*` 操控 Scholar 检索。
     - **OpenAlex / EuropePMC**: 联动 `literature-search-openalex`, `literature-search-europepmc`。
   - **逐篇提取摘要**：对检索到的所有相关结果（严禁仅取前10篇）获取 Abstract 并逐篇进行纳入/排除标准审查。

2. **纳入文献 100% 全文获取与深度提取 (Full-Text Retrieval & Extraction)**
   - 对符合纳入标准的文献，调用全文工具（`pm-fulltext`, `gs-fulltext`, `scopus-fulltext` 或通过浏览器控制导航至 PMC/Sci-Hub/出版社页面下载）获取 **100% 全文 (Full-Text)**。
   - 从全文正文与附表中提取关键研究数据（样本量、暴露定义、调整后 HR/OR/RR 及其 95% CI）。
   - 调用 `review-feasibility-to-meta` 与 `ai-peer-reviewer` 进行 ROB2 (RCT) 或 ROBINS-I (观察性研究) 偏倚风险测评。

3. **Meta 分析与数据计算 (Meta-Analysis Statistics)**
   - 使用 R 语言 (`meta` / `metafor` 包) 进行固定效应与随机效应模型计算，输出异质性指数 ($I^2, \tau^2$)、Egger/Begg 发表偏倚检验及剪补法 (Trim-and-Fill) 分析。

4. **文献真实性校验 (Fact & Citation Verification)**
   - 调用 `reference-intelligence-mining` 与 `citing-papers-intelligence` 校验每一个引用文献的 PMID/DOI，严格防止 AI 假文献幻觉。

5. **图表创作与顶刊润色 (Publication-ready Figures & Polish)**
   - 生成高清矢量图：PRISMA 流程图、森林图 (Forest Plot)、漏斗图 (Funnel Plot)。
   - 调用 `bachert-academic-polish` / `bilingual-academic-writer` / `manuscript-writing-polish-format` 完成整篇论文的模块化撰写与学术润色，形成可直接投递的论文初稿。

---

## 📊 流水线 2：医学大数据库挖掘与观察性研究 (Path B)

适用于利用 **NHANES**、**MIMIC-IV** 等公开临床数据库及生物医学专项数据库进行横断面 (Cross-Sectional) 或纵向队列 (Longitudinal Cohort) 研究，目标为产出包含完整数据分析与验证的高水平 SCI 论文。

### 阶段与步骤（不跳过任何一步）：
1. **课题构思与因果分析 (Study Design & DAG)**
   - 确定暴露变量、结局变量及协变量。显式构建倾向性评分匹配 (PSM) 或逆概率加权 (IPW) 策略。
2. **数据库真实挖掘与抽取 (Real Database Mining & Genomic Integration)**
   - **NHANES 数据库**：调用 `nhanesr-research-agent`、`nhanesr-auto-params` 与 `nhanesr-function-reference` 进行多周期真实数据合并、复杂抽样权重设定 (`WTMEC2YR` / `WTINT2YR`) 与变量清洗。
   - **MIMIC 数据库**：调用 `mimicr-agent` 进行 ICU/住院患者真实 Cohort 构建、时间窗口定义及异常值插补。
   - **生物医学专项库支持**：联动 `clinvar-database`, `dbsnp-database`, `openfda-database`, `pubchem-database`, `chembl-database`, `opentargets-database`, `uniprot-database`, `gtex-database`, `human-protein-atlas-database` 进行机制解释与分子靶点交叉验证。
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
   - 根据真实数据分析结果自动撰写 Introduction, Methods, Results, Discussion。
   - 调用 `ai-peer-reviewer` 进行 SCI 审稿人视角的严格模拟评估。
   - 完成文献 PMID 严格真实性校验与学术语言润色，产出可以直接发表的完整 SCI 论文初稿。

---

## 🛠️ 已集成专业技能与浏览器控制矩阵 (Full Database & Browser Automation Mapping)

环境与本 Skill 已全面无缝整合以下文献库、浏览器控制与科研工具：
- **浏览器控制引擎**：DeepSeek++ `browser_*` (Debugger / Accessibility Tree DOM 自动化控制)
- **文献库矩阵**：
  - `pubmed-database` / `pm-search` / `pm-advanced-search` / `pm-paper-detail` / `pm-fulltext` / `pm-export` (PubMed 全套)
  - `ieee-xplore-database` / `ieee-search` / `ieee-paper-detail` / `ieee-export` (IEEE Xplore 全套)
  - `embase-web-search` / `embase-session` / `embase-check-login` (Embase 全套)
  - `wos_lit_mining` / `wos-search` / `wos-paper-detail` / `wos-export` (Web of Science 全套)
  - `ch-search` / `ch-advanced-search` / `ch-paper-detail` / `ch-export` (Cochrane Library 全套)
  - `scopus-search` / `scopus-advanced-search` / `scopus-document-detail` / `scopus-export` / `scopus-fulltext` (Scopus 全套)
  - `sd-search` / `sd-advanced-search` / `sd-paper-detail` / `sd-export` (ScienceDirect 全套)
  - `gs-search` / `gs-advanced-search` / `gs-cited-by` / `gs-fulltext` / `gs-export` (Google Scholar 全套)
  - `literature-search-openalex` / `literature-search-europepmc` / `clinical-trials-database`
- **临床大数据库挖掘 (NHANES/MIMIC)**：`nhanesr-research-agent`, `nhanesr-auto-params`, `nhanesr-function-reference`, `mimicr-agent`
- **统计与分析引擎**：`medical-stat-project-agent`, `stat-project-agent`, `medical_research_architect`
- **文献综述与 Meta 分析**：`medical-review-writing`, `review-feasibility-to-meta`, `critical-care-review-master`, `narrative-review-replication`
- **论文撰写、润色与审稿**：`bilingual-academic-writer`, `bachert-academic-polish`, `manuscript-writing-polish-format`, `ai-peer-reviewer`
- **图表创作与文献校验**：`nanadraw-biomedical-mcp`, `citing-papers-intelligence`, `reference-intelligence-mining`
