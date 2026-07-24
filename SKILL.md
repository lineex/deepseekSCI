---
name: deepseekSCI
description: "DeepSeek++ 大一统 (All-In-One) 科研 Master Super-Skill。全盘熔炼【思考与自愈层 (五步链+4级自愈/包含JSON格式报错+Cochrane 0条目+Europe PMC REST API+GS 429退避协议)】、【临床大数据库挖掘 (NHANES/MIMIC/UKB)】、【临床文献合成与 Meta 分析 (PRISMA/ROB2/R建模)】、【生物医学与分子组学 (Biomni: AlphaFold/ChEMBL/ClinVar/Reactome)】与【全自主科研创新 (HKUDS: 创新度/消融实验/Scientist-Bench盲审)】五大支柱。严格遵守【亲自执行、零模拟数据、100%真实性】红线，直接产出发表级 SCI 论文。"
---

# deepseekSCI: 大一统 (All-In-One) 科研 Master Super-Skill Protocol

本 Skill 为 DeepSeek++ / Antigravity 提供大一统 (All-In-One) 的五支柱融合科研 Agent Master Protocol，无缝整合 **OpenScience** (`synthetic-sciences/openscience`)、斯坦福 **Biomni** (`snap-stanford/biomni`) 以及港大 **AI-Researcher** (`HKUDS/AI-Researcher`, NeurIPS 2025) 三大开源 AI 科研顶级架构。

---

## 🌐 数据库动态渲染、API 限流与 429 报错自愈 Protocol (Multi-DB Fetching & Rendering Protocol)

> [!IMPORTANT]
> **针对 Cochrane Library 0 条目、Google Scholar 429 限流及 Europe PMC JS 依赖问题的强制解决方案：**

1. **Europe PMC (动态 JS 页面无损获取规则)**：
   - 🚫 **严禁**使用静态 `web_fetch` 抓取 Europe PMC 网页 HTML（仅能获取 Shell 框架）。
   - ✅ **强制策略**：直接调用 Europe PMC 官方免费 REST API（`https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=...&format=json&pageSize=100`）或调用 `literature-search-europepmc` 技能，100% 提取结构化 JSON 数据、PMCID 及全文 XML。

2. **Cochrane Library (动态 SPA 页面渲染抓取规则)**：
   - 🚫 **严禁**使用静态 HTML 抓取（仅获取页面框架，条目数为0）。
   - ✅ **强制策略**：使用 `ch-search` / `ch-advanced-search` 专用技能，或挂载 `browser_*` 浏览器自动化，等待 DOM 节点渲染完成后，从页面中完整提取 Reviews, Protocols 及 CENTRAL 条目。

3. **Google Scholar (HTTP 429 限流与 Tier 3 退避策略)**：
   - 当遇到 HTTP 429 限流时，自动触发 Tier 3 自愈协议：
   - **策略 A**：启动 `gs-search` 带有随机延迟（Jitter）与指数退避 (Exponential Backoff) 的抓取。
   - **策略 B**：平滑无缝切换至 **OpenAlex API** (`https://api.openalex.org/works?search=...`) 与 **Europe PMC REST API**，作为替代的全量文献与引文图谱数据源，保证检索流程零中断。

4. **多库数据统一落盘与 Python 自动去重**：
   - 抓取到的所有结构化 API 数据统一保存为本地 JSON / CSV 文件。
   - 亲自运行 Python 去重脚本（标准 DOI 匹配 + Title 相似度 $>95\%$ 模糊去重），输出精准的分库检索量与去重后总量的 PRISMA 2020 流程表。

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
- **Step 2: 50+ 科学数据库与工具拓扑路由 (Topology Routing)**：在 50+ 数据库与工具中挑选最精准 API / Skill 组合，拒绝盲目试错。
- **Step 3: 边界条件与异常预判 (Edge Case Pre-check)**：预判缺失值、字段类型转换、API 限流及包依赖，提前嵌入防护代码。
- **Step 4: 动态代码合成与真机运行 (Dynamic Code Synthesis & Exec)**：生成 Python/R 代码在本地运行，抓取控制台日志。
- **Step 5: 实证控制台日志校验与自愈 (Log Verification & Healing)**：检查运行日志与计算结果，报错自动触发自愈。

### 2. 4 级故障分级自愈矩阵 (4-Tier Error Recovery Matrix)
- **Tier 1 (代码语法、依赖包缺失与 JSON/数据格式解析报错)**：自动抓取 Traceback，调用 `pip` / `install.packages()` 补全包；遇到 `JSONDecodeError`/`KeyError` 自动切换为容错解析（如正则提取、`ast.literal_eval` 兼容、编码修复），修正代码后自动重试，**严禁因解析报错放弃代码运行**。
- **Tier 2 (模型不收敛与多重共线性)**：自动检测 VIF 指标（剔除 $VIF > 10$ 变量）、调整求解器或采用 PCA 降维。
- **Tier 3 (网络 HTTP 异常/API 限流/429/JS依赖)**：自动启动指数退避 (Exponential Backoff)、切换 REST API 接口（如 Europe PMC REST / OpenAlex API）或挂载 `browser_*` 浏览器渲染。
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

1. **精准多库联合检索**：顺序检索 PubMed, Embase, Web of Science, Cochrane Library, Scopus, Europe PMC (REST API), OpenAlex, Google Scholar。
2. **自动去重与 PRISMA 2020**：按 DOI 匹配与 Title 相似度（$>95\%$）自动去重，输出 PRISMA 流程图数据表。
3. **100% 全文提取与偏倚评价**：深入全文提取样本量、干预措施、结局指标及调整后 HR/OR/RR (95% CI)，完成 ROB2 / ROBINS-I 测评。
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
