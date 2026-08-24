# Integrated supporting reference: zotero-csl-skill/validate/schema-checklist.md

> Embedded source: `embedded-source/zotero-csl-skill/validate/schema-checklist.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# CSL 1.0.2 必需项速查表

## 文档结构树

```
style (root)
  ├── @class              ✓ 必需    "in-text" | "note"
  ├── @version            ✓ 必需    "1.0"
  ├── @default-locale     ○ 可选（推荐）  语言代码如 "en-US", "zh-CN"
  ├── @xmlns              ✓ 必需    "http://purl.org/net/xbiblio/csl"
  │
  ├── info                ✓ 必需
  │   ├── title           ✓ 必需    文本
  │   ├── id              ✓ 必需    URI
  │   ├── updated         ✓ 必需    ISO 8601 datetime
  │   ├── author          ○ 可选
  │   │   ├── name        ○ 可选
  │   │   ├── email       ○ 可选
  │   │   └── uri         ○ 可选
  │   ├── contributor     ○ 可选（多个）
  │   ├── category        ○ 可选（推荐）
  │   │   ├── @citation-format  ○ 可选  枚举值见下
  │   │   └── @field            ○ 可选  枚举值见下
  │   ├── link            ○ 可选（多个）
  │   │   ├── @href       ✓ 必需（如有 link）
  │   │   └── @rel        ✓ 必需（如有 link）  "self" | "independent-parent" | "template" | "documentation"
  │   ├── rights          ○ 可选
  │   │   └── @license    ○ 可选    URI
  │   ├── summary         ○ 可选
  │   └── issn / eissn / issnl  ○ 可选
  │
  ├── locale              ○ 可选（多个）
  │   ├── @xml:lang       ○ 可选    语言代码
  │   ├── terms           ○ 可选
  │   │   └── term        ○ 可选（多个）
  │   │       ├── @name   ✓ 必需（如有 term）
  │   │       ├── @form   ○ 可选    "long" | "short" | "verb" | "verb-short" | "symbol"
  │   │       └── @gender ○ 可选    "masculine" | "feminine"
  │   ├── date            ○ 可选
  │   └── style-options   ○ 可选
  │
  ├── macro               ○ 可选（多个）
  │   ├── @name           ✓ 必需（如有 macro）  唯一标识符
  │   └── (渲染元素)       ✓ 必需    至少一个子元素
  │
  ├── citation            ✓ 必需
  │   ├── @et-al-min                    ○ 可选  正整数
  │   ├── @et-al-use-first              ○ 可选  正整数
  │   ├── @et-al-subsequent-min         ○ 可选  正整数
  │   ├── @et-al-subsequent-use-first   ○ 可选  正整数
  │   ├── @disambiguate-add-names       ○ 可选  "true" | "false"
  │   ├── @disambiguate-add-givenname   ○ 可选  "true" | "false"
  │   ├── @disambiguate-add-year-suffix ○ 可选  "true" | "false"
  │   ├── @givenname-disambiguation-rule ○ 可选  "all-names" | "all-names-with-initials" | "primary-name" | "primary-name-with-initials" | "by-cite"
  │   ├── @collapse                     ○ 可选  "citation-number" | "year" | "year-suffix" | "year-suffix-ranged"
  │   ├── sort            ○ 可选
  │   │   └── key         ✓ 必需（如有 sort）  至少一个
  │   └── layout          ✓ 必需    至少一个
  │       ├── @locale     ○ 可选    语言代码
  │       ├── @prefix     ○ 可选
  │       ├── @suffix     ○ 可选
  │       ├── @delimiter  ○ 可选
  │       └── (渲染元素)
  │
  └── bibliography        ○ 可选
      ├── @et-al-min                ○ 可选  正整数
      ├── @et-al-use-first          ○ 可选  正整数
      ├── @subsequent-author-substitute ○ 可选
      ├── @second-field-align       ○ 可选  "flush" | "margin"
      ├── @hanging-indent           ○ 可选  "true" | "false"
      ├── @line-spacing             ○ 可选  正整数
      ├── @entry-spacing            ○ 可选  非负整数
      ├── sort            ○ 可选
      │   └── key         ✓ 必需（如有 sort）  至少一个
      └── layout          ✓ 必需（如有 bibliography）  至少一个
          └── (渲染元素)
```

---

## 属性枚举值速查表

### style 元素

| 属性 | 允许值 |
|------|--------|
| `class` | `in-text`, `note` |
| `version` | `1.0` |
| `default-locale` | IETF 语言标签：`en-US`, `en-GB`, `zh-CN`, `zh-TW`, `de-DE`, `fr-FR`, `ja-JP`, `ko-KR` 等 |
| `demote-non-dropping-particle` | `never`, `sort-only`, `display-and-sort` |
| `initialize-with-hyphen` | `true`, `false` |
| `page-range-format` | `expanded`, `chicago`, `minimal`, `minimal-two` |
| `name-delimiter` | 任意字符串 |
| `names-delimiter` | 任意字符串 |

### category 元素

| 属性 | 允许值 |
|------|--------|
| `citation-format` | `author-date`, `author`, `numeric`, `label`, `note` |
| `field` | `anthropology`, `astronomy`, `biology`, `botany`, `chemistry`, `communications`, `engineering`, `generic-base`, `geography`, `geology`, `history`, `humanities`, `law`, `linguistics`, `literature`, `math`, `medicine`, `philosophy`, `physics`, `political_science`, `psychology`, `science`, `social_science`, `sociology`, `theology`, `zoology` |

### link 元素

| 属性 | 允许值 |
|------|--------|
| `rel` | `self`, `independent-parent`, `template`, `documentation` |

### name 元素

| 属性 | 允许值 |
|------|--------|
| `and` | `text`, `symbol` |
| `delimiter-precedes-et-al` | `contextual`, `always`, `never`, `after-inverted-name` |
| `delimiter-precedes-last` | `contextual`, `always`, `never`, `after-inverted-name` |
| `et-al-min` | 正整数 |
| `et-al-use-first` | 正整数（必须 < et-al-min） |
| `et-al-use-last` | `true`, `false` |
| `form` | `long`, `short`, `count` |
| `initialize` | `true`, `false` |
| `initialize-with` | 任意字符串（常用 `. `, `.`） |
| `name-as-sort-order` | `first`, `all` |
| `sort-separator` | 任意字符串（默认 `, `） |

### names 元素

| 属性 | 允许值 |
|------|--------|
| `variable` | `author`, `editor`, `translator`, `container-author`, `collection-editor`, `editorial-director`, `illustrator`, `original-author`, `recipient`, `reviewed-author`, `composer`, `director`, `interviewer` |
| `delimiter` | 任意字符串 |

### label 元素

| 属性 | 允许值 |
|------|--------|
| `form` | `long`, `short`, `verb`, `verb-short`, `symbol` |
| `plural` | `always`, `never`, `contextual` |

### text 元素

| 属性 | 允许值 |
|------|--------|
| `variable` | 所有 CSL 变量（见下方变量表） |
| `macro` | 已定义的 macro 名称 |
| `term` | CSL 术语名称 |
| `value` | 任意字面文本 |
| `form` | `long`, `short` |
| `font-style` | `normal`, `italic`, `oblique` |
| `font-weight` | `normal`, `bold`, `light` |
| `font-variant` | `normal`, `small-caps` |
| `text-decoration` | `none`, `underline` |
| `text-case` | `lowercase`, `uppercase`, `capitalize-first`, `capitalize-all`, `sentence`, `title` |
| `vertical-align` | `baseline`, `sup`, `sub` |
| `display` | `block`, `left-margin`, `right-inline`, `indent` |

### number 元素

| 属性 | 允许值 |
|------|--------|
| `variable` | `edition`, `volume`, `issue`, `number`, `number-of-pages`, `number-of-volumes`, `citation-number`, `chapter-number`, `collection-number` |
| `form` | `numeric`, `ordinal`, `long-ordinal`, `roman` |

### date 元素

| 属性 | 允许值 |
|------|--------|
| `variable` | `issued`, `accessed`, `event-date`, `original-date`, `submitted` |
| `form` | `numeric`, `text` |
| `date-parts` | `year`, `year-month`, `year-month-day` |

### date-part 元素

| 属性 | 允许值 |
|------|--------|
| `name` | `year`, `month`, `day` |
| `form`（year） | `long`, `short` |
| `form`（month） | `long`, `short`, `numeric`, `numeric-leading-zeros` |
| `form`（day） | `numeric`, `numeric-leading-zeros`, `ordinal` |
| `range-delimiter` | 任意字符串（默认 `–`） |

### choose / if / else-if 元素

| 属性 | 允许值 |
|------|--------|
| `type` | `article`, `article-journal`, `article-magazine`, `article-newspaper`, `bill`, `book`, `broadcast`, `chapter`, `dataset`, `entry`, `entry-dictionary`, `entry-encyclopedia`, `figure`, `graphic`, `interview`, `legal_case`, `legislation`, `manuscript`, `map`, `motion_picture`, `musical_score`, `pamphlet`, `paper-conference`, `patent`, `personal_communication`, `post`, `post-weblog`, `regulation`, `report`, `review`, `review-book`, `song`, `speech`, `standard`, `thesis`, `treaty`, `webpage` |
| `variable` | 任意 CSL 变量名 |
| `is-numeric` | 任意 CSL 变量名 |
| `is-uncertain-date` | 日期变量名 |
| `locator` | `act`, `appendix`, `article-locator`, `book`, `canon`, `chapter`, `column`, `elocation`, `equation`, `figure`, `folio`, `issue`, `line`, `note`, `opus`, `page`, `paragraph`, `part`, `rule`, `scene`, `section`, `sub-verbo`, `supplement`, `table`, `timestamp`, `title-number`, `verse`, `volume` |
| `position` | `first`, `subsequent`, `ibid`, `ibid-with-locator`, `near-note` |
| `match` | `all`, `any`, `none` |

### sort / key 元素

| 属性 | 允许值 |
|------|--------|
| `variable` | 任意 CSL 变量名 |
| `macro` | 已定义的 macro 名称 |
| `sort` | `ascending`, `descending` |

### group 元素

| 属性 | 允许值 |
|------|--------|
| `delimiter` | 任意字符串 |
| `prefix` | 任意字符串 |
| `suffix` | 任意字符串 |
| `display` | `block`, `left-margin`, `right-inline`, `indent` |

### term 元素（locale 内）

| 属性 | 允许值 |
|------|--------|
| `name` | 术语名称（如 `and`, `et-al`, `editor`, `translator`, `page`, `issue`, `volume`, `edition`, `retrieved`, `from`, `in`, `forthcoming`, `no date`, `accessed`, `available at`, `ibid`, `presented at` 等） |
| `form` | `long`, `short`, `verb`, `verb-short`, `symbol` |
| `gender` | `masculine`, `feminine` |
| `gender-form` | `masculine`, `feminine` |

---

## 常用 CSL 变量速查

### 标准变量（文本类）

`abstract`, `annote`, `archive`, `archive_collection`, `archive_location`, `archive-place`, `authority`, `call-number`, `citation-key`, `citation-label`, `collection-title`, `container-title`, `container-title-short`, `dimensions`, `DOI`, `event-title`, `genre`, `ISBN`, `ISSN`, `jurisdiction`, `keyword`, `language`, `license`, `medium`, `note`, `original-publisher`, `original-publisher-place`, `original-title`, `part-title`, `PMCID`, `PMID`, `publisher`, `publisher-place`, `references`, `reviewed-genre`, `reviewed-title`, `scale`, `source`, `status`, `title`, `title-short`, `URL`, `year-suffix`

### 数字变量

`chapter-number`, `citation-number`, `collection-number`, `edition`, `first-reference-note-number`, `issue`, `locator`, `number`, `number-of-pages`, `number-of-volumes`, `page`, `page-first`, `part-number`, `printing-number`, `section`, `supplement-number`, `version`, `volume`

### 日期变量

`accessed`, `available-date`, `event-date`, `issued`, `original-date`, `submitted`

### 名称变量

`author`, `chair`, `collection-editor`, `compiler`, `composer`, `container-author`, `contributor`, `curator`, `director`, `editor`, `editor-translator`, `editorial-director`, `executive-producer`, `guest`, `host`, `illustrator`, `interviewer`, `narrator`, `organizer`, `original-author`, `performer`, `producer`, `recipient`, `reviewed-author`, `script-writer`, `series-creator`, `translator`

