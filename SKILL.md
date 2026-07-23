---
name: deepseekSCI
description: "DeepSeek++ 医学与科学研究 Plan-Execution 双模式闭环 Agent Skill。具备【全自动连续循环推进（无须手动输入继续）】与【深入思考自我纠错自愈（报错自动排查修复）】能力。融合浏览器自动化与全套文献库及大数据库，严格遵守【零模拟数据、零步骤跳过、100%真实性】红线，直接产出发表级 SCI 论文。"
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

2. **🔄 自动连续推进机制 (Non-Stop Continuous Execution)**
   - 当每一步骤或阶段达到任务要求后，**必须自动发起并连续执行下一个步骤**，直达整个研究任务（如发表级 SCI 论文初稿）完全交付。
   - **严禁在步骤间停顿要求用户手动输入“继续”或回车**，保持无人值守的自动化流式推进。

3. **🛠️ 深度思考与自愈纠错机制 (Deep-Thinking Error Recovery & Self-Healing)**
   - 执行过程中若遇到任何代码报错（R/Python Traceback）、网络/数据库请求异常、或统计检验诊断不通过（如多重共线性 VIF 过高、模型不收敛、$I^2$ 异质性异常）：
   - **绝对禁止中断任务或简单将原始报错抛给用户**。
   - 必须自动触发**深入思考 (Deep-Thinking Root Cause Analysis)**，诊断根因，自动重构代码、调整控制变量或切换检索/分析策略。
   - 自动重新运行并校验修复效果，成功后**继续无缝接续先前未完成的任务**，形成“报错 $\rightarrow$ 深入思考 $\rightarrow$ 修复代码/策略 $\rightarrow$ 自动重试 $\rightarrow$ 校验成功 $\rightarrow$ 继续推进”的自愈闭环。

4. **🌐 浏览器操控驱动全量检索 (Browser Control Driven Search & Extraction)**
   - **严格联动 DeepSeek++ 浏览器控制能力 (`browser_*` 工具)**：根据文献 Skill 提供的检索语法与操作方向，自动挂载与操控浏览器标签页（PubMed, IEEE Xplore, Embase, Web of Science, Cochrane, Scopus, ScienceDirect, Google Scholar）。
   - **自动导航、翻页与提取**：在网页输入框自动填充精准 Boolean 检索式，逐页导航，从 DOM / 文本快照中提取**每一篇文献的标题、作者、DOI 及完整摘要 (Abstract)**，严禁任何手动或代码层面的中途截断。

5. **📚 全量文献检索与摘要获取禁令 (Full-Coverage Literature & Abstract Retrieval)**
   - **绝对禁止“仅获取前 10 篇 / 前 20 篇”等偷工减料行为**。
   - 文献检索阶段必须构建精准的检索式，对于检索命中的每一篇相关文献，**必须 100% 获取其摘要 (Abstract) 进行完整初筛**。
   - 明确认可：全量检索与逐篇摘要抓取虽然消耗较多时间与流量，但必须严格执行，不容打折。

6. **📄 纳入文献 100% 全文阅读与深度提取 (Mandatory Full-Text Analysis)**
   - 对于经过摘要初筛符合纳入标准的文献，**必须 100% 获取全文 (Full Text)**（调用 `pm-fulltext`, `gs-fulltext`, `scopus-fulltext` 或通过浏览器控制导航至 PMC/Sci-Hub/出版社页面下载）。
   - **绝对禁止仅凭摘要信息推断结论或填报 Meta 数据**。必须深入全文 Methods、Results 及附表提取样本量、调整后 HR/OR/RR 及其 95% CI。

7. **🪜 零步骤跳过原则 (Complete Step-by-Step Execution)**
   - **绝对禁止**为了追求速度而跳过研究流程中的任何一步。
   - 必须完整按顺序执行：**假说建立 $\rightarrow$ 因果 DAG 构造 $\rightarrow$ 浏览器操控全量检索与逐篇摘要提取 $\rightarrow$ 纳入文献全文获取与深度分析 $\rightarrow$ ROB2/ROBINS-I 偏倚评价 $\rightarrow$ R 语言 Meta 建模 $\rightarrow$ 真实性校验 $\rightarrow$ 论文撰写**。
   - **宁慢勿错，每一步骤必须输出完整诊断日志**。

8. **🔍 100% 真实性与防 AI 幻觉校验 (100% Fact & Citation Verification)**
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
                ┌──────────────────┴──────────────────┐
                │             自动评估与自愈           │
                │ 成功 ──► 自动下一步 (无需手动口令)   │
                │ 出错 ──► 深入思考根因 ──► 代码/策略修复│
                └──────────────────┬──────────────────┘
                                   │
                                   └────────────► 方案优化与轮次迭代
```

### 1. Plan 模式（需求构建与方案设计）
- **规范科研问题**：使用 PICO (Population, Intervention/Exposure, Comparator, Outcome) 或 PECO 框架将用户思路标准化为严格的科研假设。
- **因果关系与 DAG 构建**：在数据分析或文献抽取前，显式绘制有向无环图 (DAG)，明确暴露因素、结局变量、混杂因子 (Confounders)、中介因子 (Mediators) 和碰撞因子 (Colliders)。
- **分析/检索 Plan 制定**：明确所使用的医学与工程数据库 (NHANES/MIMIC/PubMed/Embase/WOS/IEEE等)、浏览器自动化操控路径、R 语言统计模型策略（加权Logistic/Cox/RCS/PSM）及敏感性分析路径。

### 2. Execution 模式（工具驱动、浏览器自动化与自愈执行）
- **工具调用与执行**：驱动本地 Native Host (`shell`, `python_exec`, `Rscript`) 进行代码运行；联动浏览器控制 (`browser_*`) 自动导航至各数据库网页执行输入、翻页与摘要/全文数据抽取。
- **自愈式结果捕获与质量控制**：
  - 正常情况：阶段指标通过后**无缝自动启动下一阶段**，不请求人工回复确认。
  - 异常情况：捕获代码 Traceback / 模型收敛失败，**深入思考寻找替代建模或修复代码**，重新运行通过后再继续。

### 3. 闭环迭代机制
- 若 Execution 模式中遇到收敛失败、混杂偏倚或异质性过高，**必须返回 Plan 模式**更新调整控制变量或统计模型，重新生成改进后的方案，实现“设计-执行-反馈-再优化”的自动化科研加速。

---

## 🔬 流水线 1：文献综述与 Systematic Review / Meta 分析 (Path A)

适用于无原始数据、基于已有文献进行二次合成的科研课题，目标为产出直接达到发表标准的 Meta 分析或 Systematic Review。

### 阶段与步骤（自动连续执行、无需口令确认）：
1. **浏览器操控驱动全量文献/摘要检索 (Browser Control Driven Search & Full Harvesting)**
   - 自动控制浏览器加载目标数据库页面，填充检索式并抓取数据：PubMed, IEEE Xplore, Cochrane, Web of Science, Embase, Scopus, ScienceDirect, Google Scholar, OpenAlex, EuropePMC。
   - **逐篇提取摘要**：对检索到的所有相关结果获取 Abstract 并逐篇进行审查。
2. **纳入文献 100% 全文获取与深度提取 (Full-Text Retrieval & Extraction)**
   - 获取 100% 全文 (Full-Text) 并深入正文与附表提取 HR/OR/RR 及其 95% CI。调用 `review-feasibility-to-meta` 与 `ai-peer-reviewer` 进行 ROB2 / ROBINS-I 偏倚风险测评。
3. **Meta 分析与数据计算 (Meta-Analysis Statistics)**
   - 使用 R 语言 (`meta` / `metafor` 包) 进行模型计算，输出异质性指数 ($I^2, \tau^2$)、Egger/Begg 发表偏倚检验及剪补法。若代码报错自动触发深入思考修改 R 脚本。
4. **文献真实性校验 (Fact & Citation Verification)**
   - 校验每一篇引用文献的 PMID/DOI。
5. **图表创作与顶刊润色 (Publication-ready Figures & Polish)**
   - 生成 PRISMA 流程图、森林图、漏斗图，完成整篇论文模块化撰写与学术润色，交付论文初稿。

---

## 📊 流水线 2：医学大数据库挖掘与观察性研究 (Path B)

适用于利用 **NHANES**、**MIMIC-IV** 等公开临床数据库及生物医学专项数据库进行横断面 (Cross-Sectional) 或纵向队列 (Longitudinal Cohort) 研究，目标为产出包含完整数据分析与验证的高水平 SCI 论文。

### 阶段与步骤（自动连续执行、无需口令确认）：
1. **课题构思与因果分析 (Study Design & DAG)**
   - 确定暴露、结局与协变量。构建 PSM / IPW 策略。
2. **数据库真实挖掘与抽取 (Real Database Mining & Genomic Integration)**
   - **NHANES / MIMIC 真实挖掘**：调用 `nhanesr-research-agent` 与 `mimicr-agent` 进行数据清洗与 Cohort 构建。联动专项数据库做机制解释。
3. **驱动本地 R 语言完成稳健统计分析 (Local R Data Analysis)**
   - 运行 Table 1 基线表、多因素 Logistic/Cox 回归、RCS 限制性立方样条非线性拟合、亚组分析及 E-value 敏感性分析。若运行报错自动深入思考重构 R 脚本并重试。
4. **高质量图表绘制 (Publication-ready Visualizations)**
   - 自动生成出版级图表：基线表 (Table 1)、森林图、RCS 剂量-效应关联图、K-M 生存曲线。
5. **文章撰写、真实性验证与审稿打磨 (Drafting, Verification & Polish)**
   - 根据真实数据结果自动撰写 Introduction, Methods, Results, Discussion。
   - 完成 PMID 真实性校验与学术润色，交付可发表的 SCI 论文初稿。

---

## 🛠️ 已集成专业技能与浏览器控制矩阵 (Full Database & Browser Automation Mapping)

环境与本 Skill 已全面无缝整合以下文献库、浏览器控制与科研工具：
- **自动化流控与自愈引擎**：Deep-Thinking Auto-Recovery & Continuous Pipeline Runner
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
