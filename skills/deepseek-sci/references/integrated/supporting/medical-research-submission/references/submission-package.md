# Integrated supporting reference: medical-research-submission/references/submission-package.md

> Embedded source: `embedded-source/medical-research-submission/references/submission-package.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# Submission Package（投稿包规范）

目标：投稿包文件齐全、命名规范、规格达标，上传系统即可完成提交。S7 投稿门按本文件执行，并运行 `scripts/check_submission_package.py` 校验。

## 1. 投稿包文件清单

| 文件 | 规范 | 必须 |
|---|---|---|
| `manuscript.docx`（或 .tex→PDF） | 含行号；正文+图表位置标记；按期刊模板排版 | ✅ |
| `cover_letter.docx` | ≤1 页；结构见 §2 | ✅ |
| `title_page.docx` | 标题、全部作者+单位+ORCID、通讯作者、字数统计、图表数、基金号 | ✅（多数期刊） |
| `abstract`/`keywords` | 常并入 manuscript 或单独上传 | 视期刊 |
| `highlights.docx` | 3–5 条，每条 ≤85 字符 | 视期刊（Elsevier 系） |
| `figures/fig1.tif`… | 位图 ≥300 dpi（TIFF/PNG/JPEG），线图矢量（EPS/PDF），RGB，单图 ≤10 MB，命名 figN | ✅ |
| `tables/table1.docx`… | Word/Excel 可编辑，非图片；表注含缩写与统计说明 | ✅ |
| `supplementary/` | 命名 eTable1/eFigure1/Appendix；正文需引用 | 视期刊 |
| `checklist_<guideline>.pdf` | 报告规范清单逐条标注页码/行号 | ✅（按研究类型） |
| `icmje_coi.pdf` | 每位作者签署的 ICMJE 利益冲突表 | ✅ |
| `ethics_approval.pdf` | IRB 批件/伦理豁免文件（如有） | 如有 |
| `trial_registration.pdf` | 注册证明（临床试验/PROSPERO） | 如有 |
| `references.bib`/`.ris` | 与正文引用一一对应 | ✅ |
| `submission_gate_report.md` | 校验脚本输出 + 人工核对记录 | ✅ |

## 2. Cover Letter 模板

```text
[日期]

Dear Editor-in-Chief,

We are pleased to submit our manuscript entitled "[标题]" for consideration
for publication in [期刊名] as an [文章类型].

[3–5 句核心内容：研究问题 → 方法 → 主要发现（含关键数字） → 临床/科学意义]

This manuscript is original, has not been published previously, and is not
under consideration elsewhere. All authors have approved the submission and
declare no conflict of interest (or: declare conflicts as follows...).

We suggest the following reviewers: [3–4 位，附机构与邮箱].
(如需要) We request that the following be excluded: ...

Corresponding author: [姓名, 单位, 邮箱, 电话]

Sincerely,
[姓名] on behalf of all authors
```

规则：≤1 页；前景匹配期刊范围；核心发现量化；不夸大；无格式错误。

## 3. 图表文件规范

- **位图**：TIFF 优先（LZW 压缩），≥300 dpi；PNG ≥300 dpi；JPEG 仅用于照片类。
- **线图/示意图**：矢量 EPS 或 PDF（可无限缩放）。
- 色彩：RGB（多数在线期刊）；灰度图用灰度模式；字体 Arial/Helvetica ≥ 8 pt。
- 尺寸：单栏 8.5 cm / 双栏 17.5 cm 经验值（按期刊要求）。
- 每张图图例独立成段：标题句 + 方法句 + 结果句 + 缩写说明。
- 投稿系统要求的分辨率检查：上传前用 `scripts/check_submission_package.py` 预检。

## 4. 表格规范

- Word 可编辑表格（不用截图/图片嵌入）。
- 三线表（顶线、栏目线、底线）为多数期刊默认；表题在表上方，表注在表下方。
- 表注必含：缩写全称、统计方法、P 值定义、单位。
- 每表在正文首次出现处引用，编号顺序与正文一致。

## 5. 伦理与注册

- 人研究：IRB 批件号 + 知情同意声明（或豁免理由）写入 Methods。
- 动物：ARRIVE + 伦理批件。
- 临床试验：注册号（ClinicalTrials.gov/ChiCTR）写入摘要与 Methods。
- 系统评价：PROSPERO 注册号（如有）。
- 数据库研究（MIMIC/NHANES）：数据使用许可声明 + 伦理豁免理由。

## 6. 修回协议（收到 Major/Minor Revision 后）

1. 新建 `revision_N/` 目录，备份原始投稿包。
2. **Response letter**（point-by-point）：
   - 每条审稿意见：引用原文（Reviewer #N, Comment ...）→ 作者回复 → 修改位置（页码/行号/图表）。
   - 接受的意见明确"已修改"；不接受的给出理由（附证据）。
3. 修订稿两种版本：`revised_manuscript_tracked.docx`（修订模式/高亮）与 `revised_manuscript_clean.docx`。
4. 所有修改同步更新摘要、数字、图题表注、补充材料编号（遵循 `manuscript-writing-polish-format` 的同步规则）。
5. 时限内提交（常见 14–60 天），超时前可申请延期。

## 7. 投稿系统操作要点

- Editorial Manager / ScholarOne / 期刊自有系统通用流程：注册 ORCID → 选文章类型 → 逐项上传文件 → 填元数据（作者/单位/基金/建议审稿人） → 生成 PDF 预览 → **人工检查 PDF 预览**（排版、图缺失、作者信息泄漏） → 提交。
- 双盲期刊：正文与补充材料中删除作者/机构信息、致谢、基金号（自查清单核对）。
- 提交后记录稿件号（如 EM-xxxx-1234），用于后续查询。

## 8. 与其它技能联动

- 文件格式转换：`_shared/pandoc-multiformat.md`（md→docx/tex/pdf）。
- 引用核验：`_shared/citation-verification-protocol.md`。
- 文档同步审计：`sync-docs`（讲稿/稿件/数据三者一致）。
- 投稿包校验：`scripts/check_submission_package.py`（本插件）。

