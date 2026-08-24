# Integrated supporting reference: medical-research-submission/references/journal-targeting.md

> Embedded source: `embedded-source/medical-research-submission/references/journal-targeting.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# Journal Targeting（选刊与 Author Guidelines）

目标：投稿前锁定目标期刊，并逐项核对 Author Guidelines，杜绝"格式不符直接退稿"。

## 1. 选刊五步法

1. **范围匹配**：期刊 Aim & Scope 是否覆盖本研究主题（用 `scopus-source-browse` 查期刊资料页）。
2. **文章类型匹配**：期刊是否接收本研究类型（Original Research / Review / Meta / Case Series / Letter）。
3. **档次匹配**：JCR 分区 / IF / CiteScore 与稿件预期匹配；用 `scopus-source-browse` 或 web_search 查最新指标（勿凭记忆）。
4. **实际门槛**：接受率、审稿周期（可从期刊官网 / 论文投稿经验帖获取）。
5. **合规与成本**：OA/APC 或版面费、单位或基金报销政策、是否被目标数据库收录（PubMed/MEDLINE 优先）。

选完第一目标后，**同时准备降档链**（Plan B、Plan C），投稿被拒可快速顺延，避免重做格式。

## 2. Author Guidelines 核对清单（投稿前逐项打勾）

| # | 项目 | 核对内容 |
|---|---|---|
| 1 | 文章类型与篇幅 | 字数上限（正文/摘要）、页码、结构要求 |
| 2 | 摘要 | 结构化/非结构化、字数上限、关键词数量 |
| 3 | 标题 | 字符数限制、是否允许缩写 |
| 4 | 正文结构 | IMRAD 或期刊特定顺序（如 CONSORT 流程段落） |
| 5 | 参考文献 | 数量上限、格式（Vancouver/AMA/作者-年份）、是否需 DOI |
| 6 | 图表 | 数量上限、文件格式（TIFF/EPS/PDF/PPT）、分辨率（≥300 dpi）、尺寸、字体 |
| 7 | 表格 | 可编辑格式（Word/Excel）、三线表或其他要求 |
| 8 | 补充材料 | 命名规范、是否随正文审阅 |
| 9 | 伦理声明 | IRB/伦理批件号、知情同意、动物伦理 |
| 10 | 注册声明 | 临床试验注册号（ClinicalTrials.gov / ChiCTR）、PROSPERO（系统评价） |
| 11 | 利益冲突 | ICMJE COI 表、期刊自有 COI 表单 |
| 12 | 作者贡献 | CRediT 或期刊格式的作者贡献声明 |
| 13 | 基金声明 | 资助编号完整、基金格式 |
| 14 | 数据可用性 | 数据共享声明、代码可用性声明 |
| 15 | Cover Letter | 篇幅、是否要求包含建议审稿人/排除审稿人 |
| 16 | 文件清单 | 上传系统要求的文件列表（Editorial Manager/ScholarOne 等） |
| 17 | 行号/页眉 | 是否要求连续行号、页眉含稿件号 |
| 18 | 双盲/单盲 | 是否需要匿名稿件（去作者信息） |

核对结果写入 `formatted/journal_compliance.md`，逐项标注"符合/不符合+修改位置"。

## 3. 常见目标期刊速查（以最新 Author Guidelines 为准，下表仅为经验值）

### 顶级综述类（NEJM/Lancet/JAMA/BMJ/Nature Medicine）
| 期刊 | 类型 | 字数 | 摘要 | 参考文献 | 图表 |
|---|---|---|---|---|---|
| NEJM | Review Article | ~4000 | 非结构化 ≤150 词 | ≤80 | ≤6，约稿制 |
| NEJM | Clinical Practice | ~2500 | 非结构化 ≤150 词 | ≤40 | ≤4 |
| Lancet | Seminar / Review | ~5000 | 非结构化 ≤300 词 | ≤100 | ≤6 |
| JAMA | Review | ~4000 | 结构化 ≤350 词 | ≤100 | ≤5，需 Key Points |
| BMJ | Clinical Review | ~3000 | 结构化 ≤300 词 | ≤60 | ≤5，需 WYNK Box |
| Nature Medicine | Review | ~6000 | 非结构化 ≤150 词 | 无硬限 | ≤10，转化导向 |

### 重症医学（ICU 方向常用）
| 期刊 | 类型 | 字数 | 摘要 | 参考文献 | 图表 | 特殊要素 |
|---|---|---|---|---|---|---|
| Critical Care Medicine | Original/Review | ~5000 | 结构化 ≤250 词 | ≤100 | ≤8 | Take-home Points |
| Intensive Care Medicine | Review / SR | ≤4000 | 结构化 ≤250 词 | ≤75 | ≤8 | Take-home Msg + Tweet |
| Critical Care | Original/Review | 4000–5000 | 结构化 | ≤100 | ≤8 | 接收数据库研究（MIMIC） |
| Chest | Original/Review | ~3500 | 结构化 ≤250 词 | ≤100 | ≤6 | 临床导向 |
| Annals of Intensive Care | Original/Review | ~4000 | 结构化 | ≤80 | ≤8 | OA 期刊 |
| Shock / J Crit Care / AJRCCM | Original | 3000–4500 | 结构化 | 40–80 | 4–8 | 按各刊要求 |

### 创伤/外科（创伤方向常用）
| 期刊 | 类型 | 字数 | 摘要 | 参考文献 | 图表 |
|---|---|---|---|---|---|
| J Trauma Acute Care Surg | Original | ~3500 | 结构化 ≤250 词 | ≤50 | ≤8 |
| Injury | Original/Review | ~3000 | 结构化 ≤250 词 | ≤50 | ≤6 |
| World J Surg | Original | ~3000 | 结构化 ≤250 词 | ≤40 | ≤6 |
| Eur J Trauma Emerg Surg | Original/Review | ~3000 | 结构化 | ≤40 | ≤6 |
| J Surg Res | Original | ~3000 | 结构化 | ≤40 | ≤6 |

> 速查表只用于初筛。**定稿前必须打开期刊官网作者须知核对最新版**（格式与限额会变）。

## 4. 与其它技能联动

- `scopus-source-browse`：查期刊 CiteScore、分区、收稿范围、出版者。
- `pm-advanced-search`：查该刊近期文章类型与风格（投稿前读 2–3 篇近期论文对齐写法）。
- `zotero-csl-skill` / `csl`：按期刊要求生成 CSL 引用样式。
- `bilingual-academic-writer`：如目标期刊为中文核心（中华系列等），切换中文文体与格式。

