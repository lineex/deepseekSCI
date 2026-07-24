# DeepSeekSCI: 大一统 (All-In-One) AI 科研 Master Super-Skill

`deepseekSCI` 是专为 **DeepSeek++** 及 AI Agent 环境打造的大一统五支柱融合 Master Agent Skill。

它全盘熔炼了 **OpenScience** (`synthetic-sciences/openscience`)、斯坦福 **Biomni** (`snap-stanford/biomni`) 以及港大 **AI-Researcher** (`HKUDS/AI-Researcher`, NeurIPS 2025) 三大开源顶级 AI 科研架构，建立起从临床大数据库挖掘、文献 Meta 分析、生物分子组学、算法消融实验到发表级 SCI 论文初稿的完整 Plan-Execution 双向闭环。

---

## 🏛️ 融合后的 5 大核心支柱

- 🧠 **支柱 1：思考与自愈层 (Cognitive Thinking & Self-Healing)**：
  - **思考五步链**：课题拆解 $\rightarrow$ 50+ DB路由 $\rightarrow$ 边界预判 $\rightarrow$ 代码运行 $\rightarrow$ 日志校验。
  - **4 级故障分级自愈矩阵**：自动解决语法/缺包报错、模型不收敛/多重共线性、网络限流/API 异常及 Meta 分析高异质性 ($I^2 > 75\%$)。
- 📊 **支柱 2：临床大数据库挖掘 (Clinical Big Data Mining)**：
  - NHANES / MIMIC-IV / UK Biobank / TriNetX 队列挖掘。
  - 出版级 Table 1 基线表、加权 Logistic/Cox 回归 (Model 1/2/3)、限制性立方样条 (RCS) 非线性拟合、PSM/IPW 因果匹配与 E-value 敏感性分析。
- 📚 **支柱 3：临床医学文献综述与 Meta 分析 (Lit Synthesis & Meta)**：
  - 自动遍历 PubMed, Embase, WoS, Cochrane, Scopus, Google Scholar。
  - 基于 DOI 与 Title 相似度的自动多库去重与 PRISMA 2020 流程图统计。
  - ROB2 / ROBINS-I 偏倚评估、R 语言 `meta` / `metafor` 随机效应建模、Egger 检验与剪补法。
- 🧬 **支柱 4：生物医学与分子组学 (Biomedical Omics & Targets - Stanford Biomni)**：
  - 单细胞 RNA-seq 降维聚类、CRISPR 筛选、Ensembl VEP 变异效应与 gnomAD 人群频率。
  - AlphaFold / PDB 3D 结构解析及 pLDDT 置信度、Foldseek 比对、InterPro 结构域。
  - ChEMBL / PubChem 分子匹配、$IC_{50}, K_i$ 活性与 ADMET 药理预测。
  - ClinVar 致病性分级、openFDA FAERS 不良事件、Reactome 通路与 STRING PPI 网络。
- 🎓 **支柱 5：全自主科研创新与同行评审 (HKUDS AI-Researcher - NeurIPS 2025)**：
  - 研究空白诊断与课题**创新度得分 (Novelty Score)** 计算。
  - 算法重构与本地 Python **消融实验 (Ablation Study)** 及 Baseline 评测。
  - **Scientist-Bench 科学同行评审**（模拟 NeurIPS / Nature / NEJM 审稿人盲审与 0 幻觉校验）。

---

## 🚨 三大红线保障

1. **绝对禁止推卸代码给用户**：Agent 必须亲自调用本地工具直接运行 Python/R 脚本。
2. **零模拟/虚假数据禁令**：所有 OR/HR/RR、$p$ 值、$I^2$ 等数值 100% 源于真实数据库与真机计算。
3. **严禁单库提前终止**：必须完成目标数据库矩阵遍历与自动去重。

---

## 🛠️ 在 DeepSeek++ 中安装与使用

### 1. 导入方式
在 DeepSeek++ 侧边栏的 **“技能 (Skills)”** 页面：
1. 点击 **【导入 GitHub】** 按钮。
2. 粘贴仓库地址：`https://github.com/lineex/deepseekSCI`
3. 点击 **【预览】** -> **【导入所选】**。

### 2. 唤醒与使用
在 [chat.deepseek.com](https://chat.deepseek.com) 对话框中输入：
```text
/deepseekSCI
```
或直接提出科研诉求，DeepSeek++ 会自动调用本 Protocol 执行课题设计、多库文献检索、数据/组学挖掘、消融实验与论文撰写！

---

## 📄 License
MIT License
