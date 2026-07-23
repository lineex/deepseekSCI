# DeepSeekSCI: DeepSeek++ & AI Agent 医学科研 Plan-Execution 闭环工作流 Skill

`deepseekSCI` 是专为 **DeepSeek++** 及 AI Agent 环境打造的顶级医学与科学研究 Agent Skill。

它打破了传统 AI 简单生成文本的限制，建立起 **Plan 模式 (科研设计)** 与 **Execution 模式 (本地代码运行与数据挖掘)** 的自动化双向闭环迭代圈，涵盖从科研思路、文献 Meta 分析 (Path A) 到 NHANES / MIMIC 临床大数据库挖掘、R 语言统计建模、矢量图表绘制、文献真伪校验 (Path B) 的完整发表流水线。

---

## 🌟 核心特性

- 🔄 **Plan-Execution 自动化闭环**：结合 PICO/PECO 规范化与 DAG (有向无环图) 因果关系构建，根据本地统计分析或文献合成结果，自动回传至 Plan 模式调整参数与假设，实现方案的闭环优化。
- 📚 **Path A：文献综述与 Systematic Review / Meta 分析**：
  - 多源文献检索 (PubMed, Web of Science, Embase, OpenAlex, EuropePMC)
  - 自动偏倚风险评估 (ROB2, ROBINS-I)
  - R 语言 Meta 分析计算 ($I^2$, Tau^2, Egger 检验, 剪补法)
  - PMID/DOI 严格真伪校验 (杜绝 AI 假文献)
  - 森林图 (Forest plot)、漏斗图 (Funnel plot)、PRISMA 流程图绘制
  - 模块化学术润色与 SCI 审稿人视角的 Peer Reviewer 评估，**直接产出发表级论文**。
- 📊 **Path B：医学大数据库挖掘与观察性研究**：
  - NHANES (`nhanesr-research-agent`) 与 MIMIC-IV (`mimicr-agent`) 数据库挖掘
  - 驱动本地 R 语言/RScript 运行加权 Logistic 回归、Cox 比例风险模型、限制性立方样条 (RCS) 非线性探索及敏感性分析 (E-value)
  - 出版级 Table 1 基线表、森林图、样条曲线矢量图绘制
  - 全文本论文自动撰写、语言润色与文献校验，**直接产出可发表的数据分析 SCI 论文**。

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
或直接提出科研诉求，DeepSeek++ 会自动调用本 Protocol 执行课题设计、数据分析与论文撰写！

---

## 📄 License
MIT License
