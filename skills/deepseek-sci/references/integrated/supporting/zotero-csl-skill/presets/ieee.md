# Integrated supporting reference: zotero-csl-skill/presets/ieee.md

> Embedded source: `embedded-source/zotero-csl-skill/presets/ieee.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

---
name: IEEE
description: IEEE数字编号格式，[1]编号，名在前I. M. Surname，7人+et al.显示1人，article引号book斜体，Vol./No./pp.标签，flush对齐
components: [name, citation, bibliography, title, date, container, publisher, access, locators, locale-en]
---

## name

```yaml
# 名在前，缩写首字母: I. M. Surname
name-as-sort-order:             # 不设置，名在前 Given Surname
sort-separator: ", "
initialize-with: ". "           # 缩写名，用句点+空格连接
initialize: true
delimiter: ", "
and: text                       # "and" 连接最后两位
et-al-min: 7
et-al-use-first: 1             # 7人以上只显示第1人 + et al.
delimiter-precedes-last: contextual
delimiter-precedes-et-al: contextual

是否双语: 否
```

## citation

```yaml
format: numeric
collapse: citation-number       # [1]-[3] 连续编号合并
prefix: "["
suffix: "]"
delimiter: ", "
sort: citation-number
```

## bibliography

```yaml
hanging-indent: false
second-field-align: flush       # [1] 编号后文字左对齐
entry-spacing: 0
line-spacing: 1
sort: citation-number           # 按引用顺序（编号排序）
numbering: true                 # [1] 编号
suffix: "."
```

## title

```yaml
# article: 引号，book: 斜体
article-journal: quotes         # "Article Title"
book: italic                    # *Book Title*
chapter: quotes                 # "Chapter Title"
thesis: quotes                  # "Thesis Title"
webpage: italic                 # *Webpage Title*

是否双语: 否
```

## date

```yaml
default-parts: year-month       # 期刊可显示月份缩写
form: text
括号: 无

中文年份: 无
```

## container

```yaml
# 期刊名: 斜体
journal: italic

# 章节/会议: "in" 连接
book-in: "in"
conference: "in"

是否双语: 否
```

## publisher

```yaml
# Place: Publisher
format: "Place: Publisher"

是否双语: 否
```

## access

```yaml
doi: prefix                     # 显示完整 DOI 链接 https://doi.org/...
url: webpage-only               # 无 DOI 时网页类型显示 URL
accessed-date: true             # 显示访问日期（网页类型）
```

## locators

```yaml
# 英文标签格式: Vol. X, No. Y, pp. Z
volume-format: "Vol. X"         # <label variable="volume" form="short"/>
issue-format: "No. X"           # <label variable="issue" form="short"/>
page-format: "pp. X"            # <label variable="page" form="short"/>，自动单页p./多页pp.
separator: ", "                 # 卷、期、页码之间逗号分隔
```

## locale-en

```yaml
page-range-delimiter: "\u2013"  # en dash –
punctuation-in-quote: false     # 标点在引号外
translator-form-short: "trans."
```

