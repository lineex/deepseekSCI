# Integrated supporting reference: zotero-csl-skill/presets/gbt7714-numeric.md

> Embedded source: `embedded-source/zotero-csl-skill/presets/gbt7714-numeric.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

---
name: GB/T 7714-2015 数字引用
description: 国标数字编号格式，双语支持，[1]编号，//连接章节，中文顿号+书名号，英文无斜体，4人以上省略
components: [name, citation, bibliography, title, date, container, publisher, access, locators, locale-zh, locale-en]
---

## name

```yaml
# 英文作者
name-as-sort-order: all
sort-separator: ", "
initialize-with: " "
delimiter: ", "
and:                          # 不设置，无连接词
et-al-min: 4
et-al-use-first: 3
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
format: numeric
collapse: citation-number
prefix: "["
suffix: "]"
delimiter: ", "
sort: citation-number
```

## bibliography

```yaml
hanging-indent: false
second-field-align: flush
entry-spacing: 0
line-spacing: 1
sort: citation-number
numbering: true                # [1] 编号
suffix: "."                    # 英文条目结尾
# 中文条目 suffix: "。" （通过双语 layout 分别设置）
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
括号: 无

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
separator: ": "                # 卷期与页码之间

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

