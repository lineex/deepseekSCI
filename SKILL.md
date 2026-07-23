---
name: deepseekSCI
description: "DeepSeek++ 医学与科学研究 Plan-Execution 双模式 Graph 蓝图架构 Agent Skill。严格遵守【绝对禁止将代码/任务抛给用户执行 (Mandatory Self-Execution)】红线。将科研主线拆解为 Graph 节点与分支 Loop 独立执行，结果校验后回填主干。具备【全自动连续循环推进（免手动口令）】与【深入思考自我纠错自愈】能力。融合浏览器自动化与全套文献库及大数据库，严格遵守【零模拟数据、零步骤跳过、100%真实性】红线，直接产出发表级 SCI 论文。"
---

# deepseekSCI: 医学与科学研究 Plan-Execution Graph 蓝图架构 Protocol

本 Skill 为 DeepSeek++ / Antigravity 提供专业的医学与科学研究 Agent 工作流。采用 **Graph 蓝图架构 (Graph-Directed Blueprint Architecture)**，将主干任务解耦为多分支 Loop 独立运行与自愈，校验后精确汇聚回主干，极大提升科研产出效率与可靠性。

---

## 🚨 核心原则：科研真实性、亲自执行与零模拟数据禁令 (Mandatory Integrity & Execution)

> [!IMPORTANT]
> **本 Protocol 适用最高标准的学术诚信规范，任何违反以下红线的行为均视为严重违规：**

1. **🚫 绝对禁止将代码抛给用户手动运行 (Mandatory Self-Execution Directive)**
   - **绝对禁止**在回复中输出 *“已为用户提供 Python 脚本/请用户自行运行脚本/需用户获得数据集后继续”* 等推卸执行责任的语句！
   - 任何生成的 Python 文献/数据提取脚本、R 语言统计代码、API 抓取程序，**必须由 Agent 亲自调用 `python_exec` 或 `Execute Shell Command` 本地工具直接运行**。
   - Agent 必须亲自捕获运行输出的数据与日志，直接回填入 Graph 主干任务，无人值守推进至下一步。若受限于单轮工具调用步数限制，用户只需输入“继续”，Agent 必须立刻调用工具亲自运行脚本，绝不甩包袱给用户。

2. **🚫 零模拟/虚假数据禁令 (Zero Mock Data Policy)**
   - **绝对禁止**伪造、拼接、或使用 `set.seed()`/`rnorm()` 等代码生成任何形式的模拟数据、Mock 对象或虚假数值。
   - 所有分析结果（如 HR/OR/RR、95% CI、$p$ 值、$I^2$ 异质性等）**必须 100% 源自真实的本地 R / Python 脚本对真实 NHANES、MIMIC 数据库或文献真机抽取的运行输出**。
   - 缺失值必须通过标准的多重插补 (Multiple Imputation) 或完备病例分析处理，严禁人工编造填补。

3. **🔄 自动连续推进机制 (Non-Stop Continuous Execution)**
   - 当每一步骤或阶段达到任务要求后，**必须自动发起并连续执行下一个步骤**，直达整个研究任务（如发表级 SCI 论文初稿）完全交付。
   - 保持无人值守的自动化流式推进。

4. **🛠️ 深度思考与自愈纠错机制 (Deep-Thinking Error Recovery & Self-Healing)**
   - 执行过程中若遇到任何代码报错（R/Python Traceback）、网络/数据库请求异常、或统计检验诊断不通过（如多重共线性 VIF 过高、模型不收敛、$I^2$ 异质性异常）：
   - **绝对禁止中断任务或简单将原始报错抛给用户**。
   - 必须自动触发**深入思考 (Deep-Thinking Root Cause Analysis)**，诊断根因，自动重构代码、调整控制变量或切换检索/分析策略。
   - 自动重新运行并校验修复效果，成功后**继续无缝接续先前未完成的任务**，形成“报错 $\rightarrow$ 深入思考 $\rightarrow$ 修复代码/策略 $\rightarrow$ 自动重试 $\rightarrow$ 校验成功 $\rightarrow$ 继续推进”的自愈闭环。

5. **🌐 浏览器操控驱动全量检索 (Browser Control Driven Search & Extraction)**
   - **严格联动 DeepSeek++ 浏览器控制能力 (`browser_*` 工具)**：根据文献 Skill 提供的检索语法与操作方向，自动挂载与操控浏览器标签页（PubMed, IEEE Xplore, Embase, Web of Science, Cochrane, Scopus, ScienceDirect, Google Scholar）。
   - **自动导航、翻页与提取**：在网页输入框自动填充精准 Boolean 检索式，逐页导航，从 DOM / 文本快照中提取**每一篇文献的标题、作者、DOI 及完整摘要 (Abstract)**，严禁任何手动或代码层面的中途截断。

6. **📚 全量文献检索与摘要获取禁令 (Full-Coverage Literature & Abstract Retrieval)**
   - **绝对禁止“仅获取前 10 篇 / 前 20 篇”等偷工减料行为**。
   - 文献检索阶段必须构建精准的检索式，对于检索命中的每一篇相关文献，**必须 100% 获取其摘要 (Abstract) 进行完整初筛**。

7. **📄 纳入文献 100% 全文阅读与深度提取 (Mandatory Full-Text Analysis)**
   - 对于经过摘要初筛符合纳入标准的文献，**必须 100% 获取全文 (Full Text)**（调用 `pm-fulltext`, `gs-fulltext`, `scopus-fulltext` 或通过浏览器控制导航至 PMC/Sci-Hub/出版社页面下载）。
   - **绝对禁止仅凭摘要信息推断结论或填报 Meta 数据**。必须深入全文 Methods、Results 及附表提取样本量、调整后 HR/OR/RR 及其 95% CI。

8. **🪜 零步骤跳过原则 (Complete Step-by-Step Execution)**
   - **绝对禁止**为了追求速度而跳过研究流程中的任何一步。
   - 必须完整按顺序执行：**假说建立 $\rightarrow$ 因果 DAG 构造 $\rightarrow$ 浏览器操控全量检索与逐篇摘要提取 $\rightarrow$ 纳入文献全文获取与深度分析 $\rightarrow$ ROB2/ROBINS-I 偏倚评价 $\rightarrow$ R 语言 Meta 建模 $\rightarrow$ 真实性校验 $\rightarrow$ 论文撰写**。
   - **宁慢勿错，每一步骤必须输出完整诊断日志**。

9. **🔍 100% 真实性与防 AI 幻觉校验 (100% Fact & Citation Verification)**
   - 论文引用的每一篇参考文献必须经由 `pm-paper-detail` / `reference-intelligence-mining` 校验真实 PMID / DOI / Accession ID，**严禁任何 AI 幻觉生成的虚假文献**。
   - 论文 Results 部分引用的每一个统计数字必须与本地 R / Python 控制台的日志输出或原文数据 **0 误差对应**。

---

## 🗺️ Graph 蓝图架构与分支 Loop 汇聚机制 (Graph Blueprint Paradigm)

```
                              ┌────────────────────────┐
                              │  主干蓝图 (Main Trunk) │
                              │ PICO 课题与总目标规划  │
                              └───────────┬────────────┘
                                          │
            ┌─────────────────────────────┼─────────────────────────────┐
            ▼                             ▼                             ▼
  ┌───────────────────┐         ┌───────────────────┐         ┌───────────────────┐
  │  分支 Loop A      │         │  分支 Loop B      │         │  分支 Loop C      │
  │ 多源文献全量抓取  │         │ R 语言模型建模    │         │ 敏感性与 RCS 拟合 │
  └─────────┬─────────┘         └─────────┬─────────┘         └─────────┬─────────┘
            │ 思考/自愈/校验              │ 思考/自愈/校验              │ 思考/自愈/校验
            ▼                             ▼                             ▼
  ┌───────────────────┐         ┌───────────────────┐         ┌───────────────────┐
  │ 校验结果回填主干  │         │ 校验结果回填主干  │         │ 校验结果回填主干  │
  └─────────┬─────────┘         └─────────┬─────────┘         └─────────┬─────────┘
            └─────────────────────────────┼─────────────────────────────┘
                                          ▼
                              ┌────────────────────────┐
                              │ 汇聚主干：SCI 论文交付 │
                              └────────────────────────┘
```

---

## 🔬 流水线 1：文献综述与 Systematic Review / Meta 分析 (Path A)

适用于无原始数据、基于已有文献进行二次合成的科研课题，目标为产出直接达到发表标准的 Meta 分析或 Systematic Review。

### 阶段与步骤（亲自执行、无需口令确认）：
1. **精准构建检索式与全量文献/摘要检索 (Precision Search & Full Abstract Harvesting)**
   - 构建精准检索式，启动各文献库抓取分支 Loop，通过浏览器操控与 API 逐篇提取摘要。
2. **纳入文献 100% 全文获取与深度提取 (Full-Text Retrieval & Extraction)**
   - 启动全文获取分支 Loop，100% 深入正文与附表提取 HR/OR/RR 及其 95% CI，进行 ROB2 / ROBINS-I 偏倚测评。Agent 亲自调用 `python_exec` 或 `shell` 执行导出与下载，绝不上交用户。
3. **Meta 分析与数据计算 (Meta-Analysis Statistics)**
   - 启动 R 语言合并分支 Loop，计算 $I^2, \tau^2$、Egger 检验及剪补法。若代码报错自动触发深入思考自愈修复。
4. **文献真实性校验 (Fact & Citation Verification)**
   - 启动校验分支 Loop，核对每一篇引用文献的 PMID/DOI。
5. **图表创作与顶刊润色 (Publication-ready Figures & Polish)**
   - 汇聚各分支结果回填主干，生成 PRISMA 流程图、森林图、漏斗图，完成论文模块化撰写。

---

## 📊 流水线 2：医学大数据库挖掘与观察性研究 (Path B)

适用于利用 **NHANES**、**MIMIC-IV** 等公开临床数据库及生物医学专项数据库进行横断面 (Cross-Sectional) 或纵向队列 (Longitudinal Cohort) 研究，目标为产出包含完整数据分析与验证的高水平 SCI 论文。

### 阶段与步骤（亲自执行、无需口令确认）：
1. **课题构思与因果分析 (Study Design & DAG)**
   - 确定暴露、结局与协变量，构建因果 DAG 与 PSM / IPW 策略。
2. **数据库挖掘与分子/基因靶点关联 (Database Mining & Genomic Integration)**
   - 启动数据挖掘分支 Loop (`nhanesr-research-agent`, `mimicr-agent`) 进行 Cohort 构建与变量清洗。
3. **驱动本地 R 语言完成稳健统计分析 (Local R Data Analysis)**
   - 并行启动分析分支 Loop：生成 Table 1 基线表、多因素 Logistic/Cox 回归、RCS 限制性立方样条拟合、亚组分析及 E-value 敏感性分析。Agent 亲自运行 R 脚本，报错自动深入思考重构。
4. **高质量图表绘制与主干汇聚 (Publication-ready Visualizations)**
   - 各分析分支结果回填主干，自动生成出版级 Table 1、森林图、RCS 关联图、K-M 生存曲线。
5. **文章撰写、真实性验证与审稿打磨 (Drafting, Verification & Polish)**
   - 结合真机运算数据撰写全文，完成 PMID 真实性校验与学术润色，交付 SCI 论文初稿。

---

## 🛠️ 已集成专业技能与浏览器控制矩阵 (Full Database & Browser Automation Mapping)

环境与本 Skill 已全面无缝整合以下文献库、浏览器控制与科研工具：
- **亲力亲为执行引擎**：Mandatory Self-Execution & Anti-Offload Automation Engine
- **Graph 蓝图调度引擎**：Graph Blueprint & Branch Execution Sub-Loop Engine
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
