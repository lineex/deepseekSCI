# Integrated supporting reference: zotero-csl-skill/presets/gbt7714-author-date.md

> Embedded source: `embedded-source/zotero-csl-skill/presets/gbt7714-author-date.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

---
name: GB/T 7714-2015 著者-年份
description: 国标著者-年份格式，双语支持，(Author, Year)引用，悬挂缩进，无编号，按作者+年排序
components: [name, citation, bibliography, title, date, container, publisher, access, locators, locale-zh, locale-en]
---

## name

```yaml
# 英文作者
name-as-sort-order: all
sort-separator: ", "
initialize-with: " "
delimiter: ", "
and: text                      # "and" 连接最后两位
et-al-min: 4
et-al-use-first: 3
delimiter-precedes-last: never
delimiter-precedes-et-al: never

# 中文作者
# delimiter: "、"
# 不设 initialize-with，显示全名
# 不设 and
# et-al-min: 4
# et-al-use-first: 3

是否双语: 是
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
second-field-align:             # 不设置，无编号对齐
entry-spacing: 1
line-spacing: 1
sort: author+year               # 按作者姓氏 + 年份排序
numbering: false                # 无编号
suffix: "."                     # 英文条目结尾
# 中文条目 suffix: "。"
```

## title

```yaml
# 英文：所有类型均为纯文本，无斜体无引号
article-journal: plain
book: plain
chapter: plain
thesis: plain
webpage: plain

# 中文：书名号 + 引号
# article-journal: 引号 ""（quotes="true"）
# book: 书名号《》
# chapter: 书名号《》
# thesis: 书名号《》
# webpage: 引号 ""

是否双语: 是
```

## date

```yaml
# 英文：仅年份，纯文本
default-parts: year
form: text
括号: 无                        # bibliography 中无括号，作者后紧跟年份

# 中文：2024年 格式
中文年份: 有
```

## container

```yaml
# 英文期刊：纯文本，无斜体
journal: plain

# 中文期刊：书名号《》
# journal: 书名号

# 章节/会议：// 连接（GB/T 7714 特有）
book-in: "//"
conference: "//"

是否双语: 是
```

## publisher

```yaml
# 英文：Place: Publisher
format: "Place: Publisher"

# 中文：出版地：出版社（全角冒号）
是否双语: 是
```

## access

```yaml
doi: false
url: webpage-only
accessed-date: false
```

## locators

```yaml
# 英文
volume-format: 纯数字
issue-format: (X)              # 紧凑格式 15(3)
page-format: 纯数字
separator: ": "

# 中文
# volume-format: "第X卷"
# issue-format: "第X期"
# page-format: "第X页"（报纸为"第X版"）
```

## locale-zh

```yaml
et-al: "等"
and: "和"
edition: "版"
ibid: "同上"
in: "载"
no-date: "出版时间不详"
open-quote: "\u201C"
close-quote: "\u201D"
open-inner-quote: "\u2018"
close-inner-quote: "\u2019"
page-range-delimiter: "\u2014"   # em dash —
author: "著"
editor: "主编"
compiler: "整理"
thesis: "博士论文"
anonymous: "佚名"
```

## locale-en

```yaml
page-range-delimiter: "-"
punctuation-in-quote: false
translator-form-short: "trans."
```

