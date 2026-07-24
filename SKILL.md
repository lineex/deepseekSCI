---
name: deepseekSCI
description: "DeepSeek++ 大一统 (All-In-One) 科研 Master Super-Skill。全盘熔炼【思考与自愈层 (五步链+4级自愈/强制100%摘要提取与PICO结构化解析/全浏览器操控驱动多库检索与PDF下载)】、【临床大数据库挖掘 (NHANES/MIMIC/UKB)】、【临床文献合成与 Meta 分析 (PRISMA/ROB2/R建模)】、【生物医学与分子组学 (Biomni: AlphaFold/ChEMBL/ClinVar/Reactome)】与【全自主科研创新 (HKUDS: 创新度/消融实验/Scientist-Bench盲审)】五大支柱。严格遵守【亲自执行、零模拟数据、100%真实性】红线，直接产出发表级 SCI 论文。"
---

# deepseekSCI: 大一统 (All-In-One) 科研 Master Super-Skill Protocol

本 Skill 为 DeepSeek++ / Antigravity 提供大一统 (All-In-One) 的五支柱融合科研 Agent Master Protocol，无缝整合 **OpenScience** (`synthetic-sciences/openscience`)、斯坦福 **Biomni** (`snap-stanford/biomni`) 以及港大 **AI-Researcher** (`HKUDS/AI-Researcher`, NeurIPS 2025) 三大开源 AI 科研顶级架构。

---

## 📄 强制 100% 摘要全量提取与结构化深度分析 Protocol (Mandatory Abstract & Full-Text Deep Extraction Protocol)

> [!IMPORTANT]
> **彻底解决“只检索标题而不提取摘要”问题的核心强制规范：**

1. **摘要 100% 全量提取第一指令 (100% Mandatory Abstract Extraction Directive)**：
   - 🚫 **严禁**仅列出标题 (Title)、PMID 或 DOI 就宣布检索完成！
   - ✅ **强制要求**：无论是通过 API 还是全浏览器操控 (`browser_*`)，**必须 100% 提取抓取每篇文献的完整摘要 (Abstract)**、发表年份、期刊名称、作者及其机构。

2. **摘要与全文 PICO 结构化解析流水线 (Structured Abstract & PICO Parsing Pipeline)**：
   - 提取摘要后，必须亲自运行 Python 脚本对所有摘要进行文本分析与结构化提取，生成包含以下核心字段的 PICO 数据库：
     - **P (Population / Sample Size)**：样本量 $N$ 与人口学/疾病特征。
     - **I (Intervention / Exposure)**：干预措施、药物剂量或暴露因素。
     - **C (Control / Comparator)**：对照组或安慰剂配置。
     - **O (Outcomes & Effect Sizes)**：核心结局指标、OR/HR/RR 及其 95% CI 与 $p$ 值。
     - **Design**：研究设计（RCT、前瞻性队列、回顾性队列、病例对照、Meta分析）。

3. **摘要缺失自动自愈补全矩阵 (Abstract Coverage Healing Matrix)**：
   - 数据处理 Python 脚本必须校验摘要完整度。若发现某些文献摘要缺失，自动触发 **Tier 1 摘要自愈补全**：
     - **补全途径 A (PubMed E-Fetch)**：通过 NCBI E-Fetch API 依据 PMID 自动补全 XML 中的 Abstract 节点。
     - **补全途径 B (OpenAlex Inverted Index)**：通过 OpenAlex API 自动还原倒排索引摘要 (abstract_inverted_index)。
     - **补全途径 C (浏览器 DOM 抓取)**：使用 `browser_*` 导航至文献 DOI 页面，提取 `.abstract` / `#abstract` 节点内容。

---

## 🌐 全浏览器操控驱动多库全量检索与全文下载 Protocol (Full Browser Automation Driven Multi-DB Engine)

> [!IMPORTANT]
> **全浏览器操控 (`browser_*` / Chrome DevTools MCP) 作为多数据库检索的第一优先核心策略：**

1. **浏览器操控第一原则 (Primary Browser Automation Directive)**：
   - 100% 完全支持并优先采用 **DeepSeek++ 全浏览器自动化操控 (`browser_*` / `browser_subagent`)** 实现所有数据库（PubMed, Embase, WoS, Cochrane Library, Scopus, Google Scholar, Europe PMC, ScienceDirect, IEEE Xplore）的搜索、交互筛选与全文 PDF 下载。
   - 真实浏览器操作可天然避开 API 频控、完美渲染 SPA 动态 JavaScript 页面（彻底解决 Cochrane / Europe PMC 空 Shell 问题），并直接继承用户在浏览器中已登录的机构 WebVPN / EZproxy / 校园网全文下载权限！

2. **目标数据库全浏览器操控路线图 (Full Browser Operation Roadmap)**：
   - 🌐 **PubMed** (`https://pubmed.ncbi.nlm.org`)：通过 `browser_*` 打开 PubMed 搜索页，自动输入 MeSH 组合表达式，点击检索，自动解析页面 DOM 或导出 CSV/NBIB 获取完整 PMID, DOI, Abstract, Title, Authors。
   - 🌐 **Cochrane Library** (`https://www.cochranelibrary.com`)：通过 `browser_*` 打开搜索页，自动等待 DOM 节点 `#searchResults` 渲染完成（解决 0 条目问题），分别提取 Reviews, Protocols 与 CENTRAL 条目及 CD 号/DOI/完整摘要。
   - 🌐 **Europe PMC** (`https://europepmc.org`)：通过 `browser_*` 打开页面，自动等待 JS 节点完成渲染，提取 PMCID、完整摘要、Open Access PDF 下载按钮与全文 XML。
   - 🌐 **Web of Science** (`https://www.webofscience.com`)：通过 `browser_*` 导航至 WoS，继承机构 EZproxy/WebVPN 认证，输入 `TS=(...)` 表达式，逐页提取 WoS Accession ID、Times Cited、DOI 与摘要。
   - 🌐 **Embase** (`https://www.embase.com`)：结合 `embase-session` / `embase-web-search` 与 `browser_*` 自动操控导航并提交 Emtree 表达式，抓取完整文献卡片与摘要。
   - 🌐 **Scopus** (`https://www.scopus.com`)：通过 `browser_*` 打开 Scopus 检索页，提取 TITLE-ABS-KEY 结果、EID/DOI 与摘要。
   - 🌐 **Google Scholar** (`https://scholar.google.com`)：通过 `browser_*` 模拟真实人类操作（带 3-5 秒 Jitter 停顿），输入关键词检索，提取引用次数、Snippet/Abstract 与 PDF 直链。

3. **数据抓取落盘与 Python 自动去重**：
   - 所有由浏览器提取到的分库文献数据统一导出保存为 `data/raw_pubmed.json`, `data/raw_cochrane.json`, `data/raw_embase.json`, `data/raw_wos.json`, `data/raw_europepmc.json` 等。
   - 亲自运行 Python 去重脚本（标准 DOI 匹配 + Title 相似度 $>95\%$ 模糊去重），输出精准的分库检索量与去重后总量的 PRISMA 2020 流程表。

4. **机构权限继承与全文 PDF 自动下载**：
   - 操控浏览器直接点击文献页面中的 `PDF Download`、`PMC Open Access` 或 `Publisher Link` 按钮，自动将 PDF 论文下载保存至本地 `downloads/` 目录，无需手动干预。

---

## 🏛️ 五大核心支柱矩阵 (Five Master Pillars Architecture)

```
                            ┌────────────────────────┐
                            │   大一统科研假说/课题  │
                            │ All-In-One Master Input│
                            └───────────┬────────────┘
                                        │
    ┌───────────────────┬───────────────┼───────────────┬───────────────────┐
    ▼                   ▼               ▼               ▼                   ▼
┌───────────────┐ ┌───────────┐ ┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│ 支柱 1：      │ │ 支柱 2：  │ │ 支柱 3：      │ │ 支柱 4：      │ │ 支柱 5：      │
│ 思考与自愈层  │ │ 临床大数据│ │ 临床文献 Meta │ │ 生物医学组学  │ │ 全自主科研创新│
│ 五步链+4级自愈│ │ NHANES/MIMIC│ │ PRISMA/ROB2/R │ │ Biomni/AlphaFold│ │ HKUDS/消融盲审│
└───────┬───────┘ └─────┬─────┘ └───────┬───────┘ └───────┬───────┘ └───────┬───────┘
        │               │               │               │               │
        └───────────────┴───────────────┼───────────────┴───────────────┘
                                        ▼
                            ┌────────────────────────┐
                            │ 本地 R / Python 稳健分析│
                            │ 矢量图表与 SCI 论文交付│
                            └───────────┬────────────┘
```

---

## 🧠 支柱 1：思考与自愈层 Protocol (Cognitive Thinking & Self-Healing)

### 1. 思考五步链 Protocol (5-Step Cognitive Thinking Chain)
在执行任何复杂科研指令前，Agent 必须完成以下认知推理：
- **Step 1: 课题拆解与因果假说构建 (Intent & Hypothesis)**：拆解研究目标，明确 PICO / 因果 DAG 与控制变量。
- **Step 2: 50+ 科学数据库与工具拓扑路由 (Topology Routing)**：在 50+ 数据库与工具中挑选最精准 API / Skill / 浏览器组合，拒绝盲目试错。
- **Step 3: 边界条件与异常预判 (Edge Case Pre-check)**：预判缺失值、字段类型转换、API 限流及包依赖，提前嵌入防护代码。
- **Step 4: 动态代码合成与真机运行 (Dynamic Code Synthesis & Exec)**：生成 Python/R 代码在本地运行，抓取控制台日志。
- **Step 5: 实证控制台日志校验与自愈 (Log Verification & Healing)**：检查运行日志与计算结果，报错自动触发自愈。

### 2. 4 级故障分级自愈矩阵 (4-Tier Error Recovery Matrix)
- **Tier 1 (代码语法、依赖包缺失与 JSON/数据格式解析报错/摘要缺失)**：自动抓取 Traceback，调用 `pip` / `install.packages()` 补全包；遇到 `JSONDecodeError`/`KeyError`/`摘要缺失` 自动切换为容错解析与摘要补全，修正代码后自动重试，**严禁因解析报错或摘要缺失放弃代码运行**。
- **Tier 2 (模型不收敛与多重共线性)**：自动检测 VIF 指标（剔除 $VIF > 10$ 变量）、调整求解器或采用 PCA 降维。
- **Tier 3 (网络 HTTP 异常/API 限流/429/JS依赖)**：自动启动指数退避 (Exponential Backoff) 重试，或全面切换至 `browser_*` 浏览器操控完成 DOM 解析、摘要抓取与全文下载。
- **Tier 4 (Meta 分析统计异质性 $I^2 > 75\%$ )**：自动触发亚组分析与敏感性分析排除异质性，并运行剪补法 (Trim-and-Fill)。

---

## 📊 支柱 2：临床大数据库挖掘 (Clinical Big Data Mining)

针对 **NHANES**、**MIMIC-IV**、**UK Biobank**、**TriNetX** 提供出版级医学统计：
1. **队列构建与因果 DAG**：明确暴露（Exposure）、结局（Outcome）与协变量（Confounders），绘制因果 DAG。
2. **数据清洗与加权**：调用 `nhanesr-research-agent` 或 `mimicr-agent` 完成抽样加权与多重插补 (Multiple Imputation)。
3. **本地 R 语言稳健统计**：
   - **Table 1 基线表**：连续变量均值 $\pm$ 标准差 / 中位数 [IQR]，分类变量频数与百分比。
   - **多因素 Cox/Logistic 回归**：Model 1 (未调整)、Model 2 (初步调整) 与 Model 3 (全调整) 的 OR/HR (95% CI) 与 VIF 诊断。
   - **限制性立方样条 (RCS)**：拟合非线性关联，计算 $p$ for overall / non-linearity 及转折点。
   - **PSM / IPW 匹配**：平衡组间协变量，检查卡尺 $SMD < 0.1$。
   - **亚组与敏感性分析**：交互作用 $p$ for interaction 及 E-value 混杂敏感性计算。
4. **矢量图表导出**：出版级 Table 1、森林图、RCS 关联样条图、K-M 生存曲线。

---

## 📚 支柱 3：临床医学文献综述与 Systematic Review / Meta 分析

1. **全浏览器操控精准多库联合检索与摘要抓取**：使用 `browser_*` 顺序检索 PubMed, Embase, Web of Science, Cochrane Library, Scopus, Europe PMC, OpenAlex, Google Scholar，100% 抓取摘要。
2. **自动去重与 PRISMA 2020**：运行 Python 自动去重脚本（处理 DOI 与 Title 匹配），输出分库检索量与去重后总量的 PRISMA 流程图数据表。
3. **100% 全文/摘要提取与偏倚评价**：基于抓取的完整摘要及全文提取样本量、干预措施、结局指标及调整后 HR/OR/RR (95% CI)，完成 ROB2 / ROBINS-I 测评。
4. **R 语言 Meta 建模**：计算 $I^2, \tau^2$，使用 `meta` / `metafor` 随机效应模型，自动运行亚组分析、Egger 检验与剪补法。

---

## 🧬 支柱 4：生物医学与分子组学 (Biomedical Omics & Targets - Stanford Biomni)

1. **单细胞与基因组学**：CRISPR 筛选 sgRNA 设计、scRNA-seq 降维聚类 (UMAP/t-SNE)、Ensembl VEP 变异影响预测与 gnomAD 人群频率。
2. **结构生物学与蛋白靶点**：AlphaFold/PDB 3D 结构解析及 pLDDT 评分 (`alphafold-database-fetch-and-analyze`, `pdb-database`)、Foldseek 比对、InterPro 结构域。
3. **药物化学与 ADMET 药理学**：ChEMBL/PubChem 分子匹配、$IC_{50}, K_i$ 活性与 ADMET 预测。
4. **临床基因组与调控网络**：ClinVar 致病性评级、openFDA 不良反应、Reactome 通路富集与 STRING 蛋白质互作 (PPI) 网络。

---

## 🎓 支柱 5：全自主科研创新与同行评审 (HKUDS AI-Researcher - NeurIPS 2025)

1. **假说提炼与研究空白诊断**：自动分析文献局限，计算课题**创新度得分 (Novelty Score)**，构建可证伪假说。
2. **方法创新与算法重构**：重构数学描述与算法流程，确定优化目标。
3. **本地消融实验与 Benchmark 评测**：编写 Python 代码在本地运行 Baseline 对比、**消融实验 (Ablation Study)** 与参数敏感性分析。
4. **Scientist-Bench 科学同行评审**：模拟 NeurIPS / Nature / NEJM 审稿人对论文执行双盲审查，确保数据 0 幻觉。

---

## 🚨 核心执行红线 (Mandatory Red Lines)

1. **🚫 绝对禁止将代码抛给用户手动运行**：Agent 必须亲自调用本地工具直接运行 Python/R 脚本。
2. **🚫 零模拟/虚假数据禁令**：所有 OR/HR/RR、$p$ 值、$I^2$ 等数值 100% 源于真实数据库与真机计算。
3. **🔄 自动连续推进机制**：无人值守连续推进流。
4. **🚫 严禁单库检索后提前终止**：必须完成目标数据库矩阵遍历与自动去重。

---

## 🛠️ 已集成 50+ 科学数据库与专业工具矩阵

- **文献数据库**：PubMed, Embase, Web of Science, Cochrane Library, Scopus, Google Scholar, Europe PMC, OpenAlex, ClinicalTrials.gov, IEEE Xplore, ScienceDirect, arXiv, bioRxiv.
- **临床大数据库**：`nhanesr-research-agent`, `mimicr-agent`, `openfda-database`, `clinical-trials-database`.
- **分子/结构/基因库**：`uniprot-database`, `pdb-database`, `alphafold-database-fetch-and-analyze`, `foldseek-structural-search`, `chembl-database`, `pubchem-database`, `ensembl-database`, `dbsnp-database`, `clinvar-database`, `gnomad-database`, `gtex-database`, `human-protein-atlas-database`, `encode-ccres-database`, `jaspar-database`, `quickgo-database`, `reactome-database`, `string-database`, `interpro-database`.
- **统计与创新引擎**：`medical-stat-project-agent`, `stat-project-agent`, `medical_research_architect`, `method-innovation-engine`, `data-to-discovery-agent`.
- **撰写与审稿**：`bilingual-academic-writer`, `bachert-academic-polish`, `manuscript-writing-polish-format`, `ai-peer-reviewer`, `humanizer`.
