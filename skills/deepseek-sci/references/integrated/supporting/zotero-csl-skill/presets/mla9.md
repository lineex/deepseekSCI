# Integrated supporting reference: zotero-csl-skill/presets/mla9.md

> Embedded source: `embedded-source/zotero-csl-skill/presets/mla9.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

---
name: MLA 9th Edition
description: MLA第9版英文样式，author-page引用，Surname, First Middle格式，and连接，3人+省略显示前1，斜体容器名，minimal-two页码压缩
components: [name, citation, bibliography, title, date, container, publisher, access, locators, locale-en]
---

## name

```yaml
name-as-sort-order: first              # 仅第一作者倒排: Surname, First M.
sort-separator: ", "
initialize-with: ". "                  # 缩写中间名: M.
delimiter: ", "
and: text                              # "and" 连接最后两位
et-al-min: 3
et-al-use-first: 1
delimiter-precedes-last: never         # A and B（无 Oxford comma）
delimiter-precedes-et-al: never

是否双语: 否
```

## citation

```yaml
format: author                         # author-page（无年份）
prefix: "("
suffix: ")"
delimiter: "; "
disambiguate: add-names                # 同姓加名字区分
sort: none                             # 不排序，按出现顺序
suppress-author: false
# locator（页码）无前缀标签，直接跟在作者后
```

## bibliography

```yaml
hanging-indent: true
second-field-align:                    # 不设置
entry-spacing: 0
line-spacing: 2                        # MLA 要求双倍行距
sort: author+title                     # 按作者 + 标题排序
numbering: false
suffix: "."
subsequent-author-substitute: "---"    # 连续同作者用三短线替代
```

## title

```yaml
article-journal: quotes               # 期刊文章标题：引号
book: italic                           # 书名：斜体
chapter: quotes                        # 章节标题：引号
thesis: italic                         # 学位论文：斜体
webpage: quotes                        # 网页标题：引号
container: italic                      # 容器名（期刊/论文集）：斜体

是否双语: 否
```

## date

```yaml
default-parts: year-month-day          # MLA 完整日期（日 月缩写 年）
form: text
括号: 无
# 英文 locale 日期格式: "15 Jan. 2024"
```

## container

```yaml
journal: italic                        # 期刊名：斜体
book-in: none                          # 无 "In" 前缀，直接用容器名
conference: italic

是否双语: 否
```

## publisher

```yaml
format: 仅 Publisher                    # MLA 9 仅出版社，不含出版地
```

## access

```yaml
doi: prefix                            # https://doi.org/10.xxxx
url: always                            # 所有类型有 URL 就显示
accessed-date: false                   # MLA 通常不要求访问日期
```

## locators

```yaml
volume-format: 纯数字                   # vol. 15 → 用 label
issue-format: "No. X"                  # no. 3 → 用 label
page-format: "pp. X"                   # pp. 245-60 → 用 label
page-range-delimiter: "–"             # en dash
page-range-format: minimal-two         # 245-60 压缩格式
separator: ", "
```

## locale-en

```yaml
page-range-delimiter: "\u2013"         # en dash –
punctuation-in-quote: true             # 美式标点
```

