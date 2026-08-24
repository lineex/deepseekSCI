# Integrated supporting reference: medical-research-submission/references/paper-types.md

> Embedded source: `embedded-source/medical-research-submission/references/paper-types.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# Paper Types（文章类型模板与写作规范）

目标：任何文章类型都有明确的字数、结构、统计表述规范，写出来即接近期刊定稿水平。

## 1. 文章类型速查

| 类型 | 正文字数（经验值） | 摘要 | 结构 | 图表 | 特殊要求 |
|---|---|---|---|---|---|
| Original Research | 3000–4500 | 结构化 250–300 词 | IMRAD | ≤6–8 | 伦理+注册+数据可用性 |
| Brief Report / Short Communication | 2000–2500 | 结构化 ≤250 词 | IMRAD 精简 | ≤3–4 | 创新点突出 |
| Systematic Review + Meta | 4000–6000 | 结构化（PICOS） | PRISMA 结构 | ≤8 | PROSPERO+PRISMA 清单+GRADE |
| Narrative Review | 3000–6000 | 非结构化 ≤300 词 | 期刊模板（见 `medical-review-writing`） | ≤6–10 | 检索策略段 |
| Case Series | 1500–2500 | 结构化 ≤250 词 | Intro/Methods/Results/Discussion | ≤4 | 伦理+知情同意 |
| Study Protocol | 2500–4000 | 结构化 | 背景/方法/统计/伦理 | ≤4 | 注册号；SPIRIT 清单 |
| Letter / Comment | 500–1000 | 无 | 简短 | ≤1–2 | 引用 ≤10 |

> 所有上限以目标期刊 Author Guidelines 为准（见 `journal-targeting.md`）。

## 2. IMRAD 分节要点

**Title**：信息量充足（PICO 含关键要素），≤20 词经验值，避免缩写与"novel"式空话。

**Abstract（结构化）**：Background（研究问题+意义）→ Methods（设计/人群/暴露/结局/统计）→ Results（**核心数字齐全**：例数、效应量、95%CI、P）→ Conclusions（与结果一致，不超范围）。摘要内不出现未定义缩写与引用。

**Introduction**：漏斗式三段——背景与负担 → 现有证据缺口（明确"不知道什么"）→ 本研究目的（一句话假设）。末段不写结果。

**Methods**：
- 设计：研究类型、时间窗、地点、伦理批件号、注册号。
- 人群：纳入/排除标准（数据库研究：写明版本与代码规则，见 `reporting-guidelines.md` RECORD）。
- 暴露/干预与结局：操作化定义、测量时点、结局判定标准。
- 协变量：选择依据（DAG/文献），分类与连续变量处理。
- 统计：软件与版本、缺失数据处理、模型（类型+调整变量）、亚组/敏感性分析、显著性水平；可复现（脚本路径）。

**Results**：结果先行，按"基线 → 主分析 → 亚组 → 敏感性"顺序；每段指向表图；数字与 `analysis/outputs/` 完全一致；不解释、不评价。

**Discussion**：首段重述主要发现（1–2 句）→ 与既往研究比较（为什么不同/一致）→ 机制解释（适度）→ 局限（设计、样本、偏倚、泛化性，逐条诚实）→ 临床/研究意义 → 结论（克制，不超数据）。

## 3. 统计报告规范

- P 值：报告到 3 位小数（P=0.034）；P<0.001 时写 "P<0.001"，**禁止写 P=0.000**。
- 效应量：OR/HR/RR 均带 95% CI；连续结局报均差/回归系数+CI。
- 描述统计：正态用 mean±SD，偏态用 median(IQR)，注明检验方法（t/Mann-Whitney/χ²/Fisher/ANOVA/Kruskal-Wallis）。
- 模型：注明软件包与版本、调整变量清单、比例风险假设（Cox）、线性假设、多重比较校正方法。
- 缺失数据：报告缺失比例与处理方式（完整病例/多重插补/加权），禁止静默删除。
- 生存分析：报告随访中位数、删失、事件数；KM 曲线标注风险人数表。
- 预测模型：判别+校准都要报（见 TRIPOD）。
- 表格内 P 值用统一格式；表注声明检验方法与校正。

## 4. 数字溯源规则（防"数字对不上"）

1. 稿件中每个统计数字从 `analysis/outputs/table_*.csv` 复制，不手敲。
2. 正文、摘要、图、表、supplementary 同一数字必须一致（用 `sync-docs` 审计）。
3. 分析重跑后，**所有**涉及数字的段落（摘要/结果/讨论/图注表注）同步更新（遵循 `manuscript-writing-polish-format` 同步规则）。
4. 稿内保留可追溯标记：表格编号+行/列（如 `Table 2, Model 3`）。

## 5. 高频拒稿原因自查

- 选题无新意或已被做透（S0 未过门）。
- Methods 不可复现（缺版本、缺代码、缺定义）。
- 统计错误：多重比较不校正、P 值误用、模型过拟合（EPV 不足）。
- 结论超出数据（因果语言用于观察性研究）。
- 报告规范缺失（无 checklist、无注册号）。
- 语言与格式不达标（超字数、图表超限、引用格式错、无行号）。
- 图表质量差（分辨率不足、图例不完整、表不可编辑）。
- Cover letter 无说服力或与期刊范围不匹配。

## 6. 与其它技能联动

- 写作：`manuscript-writing-polish-format`、`medical-review-writing`（综述模板）。
- 润色：`humanizer` 等（见 SKILL.md S5）。
- 统计：`medical-stat-project-agent`（研究全流程）、`mimicr-agent`、`nhanesr-auto-params`。
- 文档同步审计：`sync-docs`。

