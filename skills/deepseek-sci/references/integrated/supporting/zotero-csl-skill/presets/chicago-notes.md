# Integrated supporting reference: zotero-csl-skill/presets/chicago-notes.md

> Embedded source: `embedded-source/zotero-csl-skill/presets/chicago-notes.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

---
name: Chicago Notes & Bibliography 17th
description: Chicago Manual of Style 第17版脚注+参考文献格式，首次完整引用/ibid/subsequent简写，bibliography悬挂缩进按作者排序，book斜体article引号，脚注名在前/参考文献姓在前
components: [name, citation, bibliography, title, date, container, publisher, access, locators, locale-en]
---

## name

```yaml
# 脚注中的作者（名在前 Given Surname）
name-as-sort-order:             # 不设置，默认名在前
sort-separator: ", "
initialize-with:                # 不设置，显示全名
initialize: true
delimiter: ", "
and: text                       # "and" 连接最后两位
et-al-min: 4
et-al-use-first: 1
delimiter-precedes-last: contextual

# 参考文献中的作者（姓在前 Surname, Given）
# bibliography 中覆盖:
#   name-as-sort-order: first   # 仅第一作者倒序
#   sort-separator: ", "
#   and: text
#   delimiter: ", "

是否双语: 否
```

## citation

```yaml
format: note
collapse:                       # 不设置
prefix:                         # 不设置（脚注格式无行内前缀）
suffix:                         # 不设置
delimiter: "; "
note-position: first / ibid / subsequent
  # first: 完整引用（作者全名+标题+出版信息+页码）
  # ibid: "Ibid." 或 "Ibid., 页码"
  # ibid-with-locator: "Ibid., 页码"
  # subsequent: 简写（Surname, Title-short, 页码）
sort:                           # 不设置（按引用顺序）
```

## bibliography

```yaml
hanging-indent: true
second-field-align:             # 不设置（无编号，用悬挂缩进）
entry-spacing: 0
line-spacing: 1
sort: author+year               # 按作者姓氏+年份排序
subsequent-author-substitute: "———"   # 连续相同作者用三字线替代
suffix: "."
numbering: false
```

## title

```yaml
# book/report 等独立出版物: 斜体
article-journal: quotes         # 期刊文章用引号
book: italic                    # 书籍用斜体
chapter: quotes                 # 章节用引号
thesis: quotes                  # 学位论文用引号
webpage: italic                 # 网页用斜体

是否双语: 否
```

## date

```yaml
default-parts: year
form: text
括号: 无
# 脚注中日期作为出版信息的一部分，用括号包裹
# 参考文献中日期紧跟作者后，也可加括号

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
doi: false
url: webpage-only
accessed-date: false
```

## locators

```yaml
# 卷期: 紧凑格式
volume-format: 纯数字
issue-format: ", no. X"          # 小写 no.
page-format: 纯数字
separator: ": "                  # 卷期与页码之间
```

## locale-en

```yaml
page-range-delimiter: "\u2013"   # en dash –
punctuation-in-quote: true       # 美式标点（逗号句号在引号内）
translator-form-short: "trans."
```

