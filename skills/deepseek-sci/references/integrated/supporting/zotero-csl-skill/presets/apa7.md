# Integrated supporting reference: zotero-csl-skill/presets/apa7.md

> Embedded source: `embedded-source/zotero-csl-skill/presets/apa7.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

---
name: APA 7th Edition
description: APA第7版英文样式，author-date引用，Surname, I. M.格式，&连接，21人+省略显示前19，斜体书名/刊名，DOI前缀，悬挂缩进
components: [name, citation, bibliography, title, date, container, publisher, access, locators, locale-en]
---

## name

```yaml
name-as-sort-order: all
sort-separator: ", "
initialize-with: ". "           # 缩写名带句点+空格: I. M.
delimiter: ", "
and: symbol                     # & 连接最后两位
et-al-min: 21
et-al-use-first: 19
delimiter-precedes-last: always  # Oxford comma: A, B, & C
delimiter-precedes-et-al: always

是否双语: 否                     # 纯英文
```

## citation

```yaml
format: author-date
collapse: year
prefix: "("
suffix: ")"
delimiter: "; "
disambiguate: add-year-suffix   # 同作者同年加 a/b 后缀
sort: author+year
# citation 内 et-al: min=3, use-first=1（行内引用更激进省略）
```

## bibliography

```yaml
hanging-indent: true
second-field-align:             # 不设置
entry-spacing: 1
line-spacing: 2                 # APA 要求双倍行距
sort: author+year               # 按作者姓氏 + 年份排序
numbering: false                # 无编号
suffix: "."
```

## title

```yaml
article-journal: plain          # 期刊文章标题：纯文本（sentence case）
book: italic                    # 书名：斜体
chapter: plain                  # 章节标题：纯文本
thesis: italic                  # 学位论文：斜体
webpage: italic                 # 网页标题：斜体

是否双语: 否
```

## date

```yaml
default-parts: year
form: text
括号: 有                         # 作者后紧跟 (2024)
```

## container

```yaml
journal: italic                 # 期刊名：斜体
book-in: "in"                   # 章节用 "In Editor (Ed.), Book Title"
conference: "in"

是否双语: 否
```

## publisher

```yaml
# APA 7 仅出版社，不含出版地
format: 仅 Publisher
```

## access

```yaml
doi: prefix                     # 输出完整链接 https://doi.org/10.xxxx
url: webpage-only               # 仅网页类型显示 URL
accessed-date: false            # APA 7 通常不要求访问日期
```

## locators

```yaml
volume-format: 纯数字            # 斜体卷号（继承容器斜体后紧跟）
issue-format: (X)               # 非斜体括号期号
page-format: 纯数字              # 纯数字页码，无 pp. 前缀
page-range-delimiter: "–"       # en dash
separator: ", "
```

## locale-en

```yaml
page-range-delimiter: "\u2013"   # en dash –
punctuation-in-quote: true       # 美式标点：句号逗号在引号内
translator-form-short: "trans."
```

