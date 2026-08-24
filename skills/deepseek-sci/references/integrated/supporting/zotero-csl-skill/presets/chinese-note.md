# Integrated supporting reference: zotero-csl-skill/presets/chinese-note.md

> Embedded source: `embedded-source/zotero-csl-skill/presets/chinese-note.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

---
name: 中文社科脚注样式
description: 中文社科脚注格式（太平洋学报/中国社会科学），class=note，双语，中文用书名号+顿号+一字线，英文用斜体+逗号，ibid=同上，bibliography带[1]编号
components: [name, citation, bibliography, title, date, container, publisher, access, locators, locale-zh, locale-en]
---

## name

```yaml
# 英文作者（名在前 Given Surname，全名）
name-as-sort-order:             # 不设置，名在前
sort-separator: ", "
initialize-with: ". "           # 缩写首字母（initialize="false" 在 style 根元素上阻止缩写）
initialize: false               # 设在 <style> 根元素，实际不缩写
delimiter: ", "
and: text                       # "and" 连接
et-al-min:                      # 不设置，显示全部作者
et-al-use-first:                # 不设置

# 中文作者
# delimiter: "、"（顿号分隔）
# 不设 initialize-with，显示全名
# 不设 and（中文不使用连接词）
# book 类型: 作者名后附"著"标签（<label form="short"/>）
# 非 book 类型: 仅 substitute 的 editor/compiler 附标签

是否双语: 是
```

## citation

```yaml
format: note
collapse:                       # 不设置
prefix:                         # 不设置
suffix:                         # 不设置
delimiter: "; "                 # 英文多条引用分隔
# 中文 delimiter: "；"（全角分号）
# 英文 suffix: "."
# 中文 suffix: "。"
note-position: first / ibid     # 首次完整引用 + ibid 简写
  # first: 完整引用（entry-layout-zh / entry-layout-en）
  # ibid: 中文"同上"，英文 "Ibid."
  # ibid-with-locator: "同上，第X页" / "Ibid., p. X"
  # subsequent: 不使用（太平洋学报不区分 subsequent，每次完整引用）
sort:                           # 不设置（按引用顺序）
```

## bibliography

```yaml
hanging-indent: false
second-field-align: flush       # [1] 编号后文字左对齐
entry-spacing: 0                # 紧凑排列
line-spacing: 1
sort: citation-number           # 按引用编号排序（note 格式 bibliography 默认）
numbering: true                 # [1] 编号
suffix: "."                     # 英文条目结尾
# 中文条目 suffix: "。" （通过双语 layout 分别设置）
```

## title

```yaml
# 英文
article-journal: quotes         # "Article Title"（引号）
book: italic                    # *Book Title*（斜体）
chapter: quotes                 # "Chapter Title"
thesis: quotes                  # "Thesis Title", Ph.D. Dissertation
webpage: italic                 # *Webpage Title*

# 中文
# article-journal: 引号 ""（quotes="true"，使用 locale 中文引号）
# book: 书名号《》（prefix/suffix 手动添加）
# chapter: 书名号《》
# thesis: 书名号《》
# webpage: 引号 ""

是否双语: 是
```

## date

```yaml
# 英文：根据类型决定精度
# 期刊: 仅年份 year
# 报纸/网页: 完整日期 text
# 其他: 仅年份 year
default-parts: year
form: text
括号: 无

# 中文：2024年 / 2024年版
# book/chapter: 年份 + "版"（<text term="edition" form="short"/>）
# 报纸/网页: 完整日期
# 其他: 仅年份
# 无日期: "出版时间不详"
中文年份: 有
```

## container

```yaml
# 英文期刊: 斜体 + Vol./No. 标签
journal: italic
# 英文章节/会议: "in" 连接
book-in: "in"
conference: "in"

# 中文期刊: 书名号《》 + 2024年第X期
# 中文章节/会议: 冒号连接编者与书名
# journal: 书名号
# book-in: "："（编者主编：《书名》）
# conference: "："

是否双语: 是
```

## publisher

```yaml
# 英文: 仅出版社名（不含出版地）
format: "Publisher"

# 中文: 仅出版社名
# thesis 特殊: 学校名 + 论文类型（博士论文/硕士论文）

是否双语: 是
```

## access

```yaml
doi: false
url: webpage-only               # 仅 post/webpage 等类型显示 URL
accessed-date: false
```

## locators

```yaml
# 英文
volume-format: "Vol. X"         # <label variable="volume" form="short"/>
issue-format: "No. X"           # <label variable="issue" form="short"/>
page-format: "pp. X"            # <label variable="page" form="short"/>，自动 p./pp.
separator: ", "

# 中文
# volume-format: "第X卷"
# issue-format: "第X期"
# page-format: "第X页"（报纸为"第X版"）
# page-range-delimiter: "—"（一字线 em dash）
```

## locale-zh

```yaml
et-al: "等"
and: "和"
edition: "版"
ibid: "同上"
in: "载"
no-date: "出版时间不详"
open-quote: "\u201C"            # "
close-quote: "\u201D"           # "
open-inner-quote: "\u2018"      # '
close-inner-quote: "\u2019"     # '
page-range-delimiter: "\u2014"  # em dash —（一字线）
author: "著"
editor: "主编"
compiler: "整理"
thesis: "博士论文"
anonymous: "佚名"
```

## locale-en

```yaml
page-range-delimiter: "-"       # hyphen
punctuation-in-quote: false     # 英式标点（中文社科期刊常用）
translator-form-short: "trans."
```

