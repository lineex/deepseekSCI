# Integrated supporting reference: zotero-csl-skill/validate/rules.md

> Embedded source: `embedded-source/zotero-csl-skill/validate/rules.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# CSL 逻辑一致性规则清单

供 AI 在 CSL 生成后做逻辑审核使用。每条规则标注严重级别：

- **error** — 必须修复，否则 CSL 无法正常工作或违反规范
- **warning** — 建议修复，不影响基本功能但可能导致非预期行为

---

## R1: 结构完整性

| # | 检查项 | 级别 |
|---|--------|------|
| R1.1 | `<style>` 必须有 `class` 属性 | error |
| R1.2 | `<style>` 必须有 `version` 属性 | error |
| R1.3 | `<style>` 必须有 `default-locale` 属性 | warning |
| R1.4 | `<info>` 必须存在且包含 `<title>` 子元素 | error |
| R1.5 | `<info>` 必须包含 `<id>` 子元素 | error |
| R1.6 | `<info>` 必须包含 `<updated>` 子元素 | error |
| R1.7 | `<id>` 的值必须是唯一 URI | error |
| R1.8 | `<citation>` 必须存在 | error |
| R1.9 | `<citation>` 必须包含至少一个 `<layout>` | error |
| R1.10 | `<bibliography>` 如存在，必须包含至少一个 `<layout>` | error |

---

## R2: macro 引用完整性

| # | 检查项 | 级别 |
|---|--------|------|
| R2.1 | 每个 `<text macro="X"/>` 必须有对应的 `<macro name="X">` 定义 | error |
| R2.2 | 每个 `<key macro="X"/>` 必须有对应的 `<macro name="X">` 定义 | error |
| R2.3 | 已定义但未被任何地方引用的 macro 应报告 | warning |
| R2.4 | macro 不能循环引用（A 引用 B，B 引用 A） | error |

---

## R3: class 与 format 一致

| # | 检查项 | 级别 |
|---|--------|------|
| R3.1 | `class="in-text"` 时，`<category citation-format>` 应为 `numeric` 或 `author-date` | error |
| R3.2 | `class="note"` 时，`<category citation-format>` 应为 `note` | error |
| R3.3 | numeric 样式的 bibliography 中应引用 `citation-number` | warning |
| R3.4 | note 样式的 citation 中建议有 `position` 条件判断（处理 ibid 等） | warning |

---

## R4: 参数合法性

| # | 检查项 | 级别 |
|---|--------|------|
| R4.1 | `et-al-min` 必须 > `et-al-use-first`（在所有出现的位置检查：`<style>`, `<citation>`, `<bibliography>`, `<names>`, `<key>`） | error |
| R4.2 | `et-al-use-first` 必须 >= 1 | error |
| R4.3 | `name-as-sort-order` 值只能是 `"first"` 或 `"all"` | error |
| R4.4 | `and` 值只能是 `"text"` 或 `"symbol"` | error |
| R4.5 | `delimiter-precedes-last` 值只能是 `"always"` / `"never"` / `"contextual"` / `"after-inverted-name"` | error |
| R4.6 | `page-range-format` 值只能是 `"expanded"` / `"chicago"` / `"minimal"` / `"minimal-two"` | error |
| R4.7 | `form` 属性值需符合对应元素的允许值（见 schema-checklist.md） | error |
| R4.8 | `class` 值只能是 `"in-text"` 或 `"note"` | error |

---

## R5: 双语一致性

| # | 检查项 | 级别 |
|---|--------|------|
| R5.1 | 多个 `<layout>` 时，带 `locale` 属性的必须排在前面，不带的排在最后（作为 fallback） | error |
| R5.2 | 带 `locale="zh"` 的 layout 引用的宏应对应中文格式逻辑 | warning |
| R5.3 | 默认 layout（无 locale 属性）引用的宏应对应英文格式逻辑 | warning |
| R5.4 | 如有中文 layout，应有 `<locale xml:lang="zh">` 提供术语覆盖 | error |

---

## R6: 无残留

| # | 检查项 | 级别 |
|---|--------|------|
| R6.1 | 不能有 `[xxx]` 形式的占位符文本（正则：`\[[a-zA-Z_]+\]`） | error |
| R6.2 | 不能有内容为空的 macro（`<macro>` 无任何子元素） | error |
| R6.3 | 不能有注释掉的模板代码块（`<!-- ... -->` 中包含 CSL 元素标签） | warning |
| R6.4 | `<info>/<title>` 不能是通用占位名，如 "Custom Style"、"Untitled"、"My Style" | warning |

---

## R7: 最佳实践（警告级）

| # | 检查项 | 级别 |
|---|--------|------|
| R7.1 | `<substitute>` 元素应放在 `<names>` 内部 | warning |
| R7.2 | author 的 `<names>` 建议提供 `<substitute>`（回退到 editor 或 title） | warning |
| R7.3 | note 样式建议处理 ibid 情况（`position="ibid"`） | warning |
| R7.4 | `<bibliography>` 建议包含 `<sort>` 子元素 | warning |

