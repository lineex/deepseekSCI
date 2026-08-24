# Integrated supporting reference: zotero-csl-skill/components/bibliography.md

> Embedded source: `embedded-source/zotero-csl-skill/components/bibliography.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# bibliography -- bibliography 元素

## 参数

| 参数 | 类型 | 可选值 | 默认 | 说明 |
|------|------|--------|------|------|
| hanging-indent | boolean | `true` / `false` | `false` | 悬挂缩进（首行顶格，后续行缩进） |
| second-field-align | string | `flush` / `margin` / 不设置 | — | 第二字段对齐方式。`flush` 使编号后的文字左对齐，`margin` 将编号放在页边距中 |
| entry-spacing | integer | `0` / `1` / `2` | `1` | 条目间距（以行为单位，0 表示无额外间距） |
| line-spacing | integer | `1` / `2` | `1` | 行间距倍数 |
| sort | string | `citation-number` / `author+year` | — | 参考文献排序方式 |
| subsequent-author-substitute | string | `"———"` / `"---"` / 自定义 | — | 连续相同作者时的替代符号 |
| suffix | string | `"."` / `"。"` | `"."` | 每条参考文献的结尾符号 |
| numbering | boolean | `true` / `false` | `false` | 是否在条目前显示编号（如 `[1]`） |

## 模板

### numeric 带编号 [1]，flush 对齐

参考 `太平洋学报.csl` 中的实际定义：

```xml
<bibliography entry-spacing="0" second-field-align="flush">
  <!-- 中文条目 -->
  <layout locale="zh">
    <text variable="citation-number" prefix="[" suffix="]"/>
    <text macro="entry-layout-zh" suffix="。"/>
  </layout>
  <!-- 英文条目（默认） -->
  <layout>
    <text variable="citation-number" prefix="[" suffix="]"/>
    <text macro="entry-layout-en" suffix="."/>
  </layout>
</bibliography>
```

效果：

```
[1]  张三：《论文标题》，《期刊名》，2024年第1期。
[2]  Smith, "Article Title," Journal Name, 2024.
```

`second-field-align="flush"` 使 `[1]` 之后的正文文字对齐到同一列，编号不占用正文空间。

### author-date 悬挂缩进

```xml
<bibliography hanging-indent="true" entry-spacing="1" line-spacing="1">
  <sort>
    <key macro="author"/>
    <key macro="date" sort="ascending"/>
  </sort>
  <layout suffix=".">
    <group delimiter=". ">
      <text macro="author"/>
      <text macro="date" prefix="(" suffix=")"/>
      <text macro="title"/>
      <text macro="container"/>
    </group>
  </layout>
</bibliography>
```

效果：

```
Smith, John. (2024). "Article Title." Journal Name, Vol. 10, No. 2.
    Continued text wraps with hanging indent.
```

`hanging-indent="true"` 使首行顶格、续行缩进，便于快速定位作者姓氏。

### note 样式参考文献列表

note 样式也可以附带 bibliography，通常按作者排序，不带编号：

```xml
<bibliography hanging-indent="true" entry-spacing="0" line-spacing="1">
  <sort>
    <key macro="author"/>
    <key macro="date" sort="ascending"/>
  </sort>
  <layout locale="zh">
    <text macro="entry-layout-zh" suffix="。"/>
  </layout>
  <layout>
    <text macro="entry-layout-en" suffix="."/>
  </layout>
</bibliography>
```

效果：

```
张三：《论文标题》，《期刊名》，2024年第1期。
Smith, "Article Title," Journal Name, 2024.
```

无编号，按作者字母/拼音排序，悬挂缩进。

### 中文样式（"。"结尾）

中文参考文献以句号"。"结尾，英文以 period "." 结尾。通过双语 layout 分别指定 suffix：

```xml
<bibliography entry-spacing="0" second-field-align="flush">
  <layout locale="zh">
    <text variable="citation-number" prefix="[" suffix="]"/>
    <text macro="entry-layout-zh" suffix="。"/>
  </layout>
  <layout>
    <text variable="citation-number" prefix="[" suffix="]"/>
    <text macro="entry-layout-en" suffix="."/>
  </layout>
</bibliography>
```

### subsequent-author-substitute（连续相同作者替代）

当参考文献列表中多条连续条目的作者相同时，用长划线替代重复的作者名：

```xml
<bibliography hanging-indent="true" subsequent-author-substitute="———">
  <sort>
    <key macro="author"/>
    <key macro="date" sort="ascending"/>
  </sort>
  <layout suffix=".">
    <group delimiter=". ">
      <text macro="author"/>
      <text macro="date" prefix="(" suffix=")"/>
      <text macro="title"/>
    </group>
  </layout>
</bibliography>
```

效果：

```
Smith, John. (2023). First Article.
———. (2024). Second Article.
———. (2025). Third Article.
```

## 注意事项

- **`second-field-align`**：此属性专为带编号的参考文献设计。`flush` 将编号视为独立列，正文从编号后对齐；`margin` 将编号放入页边距区域。如果不需要编号，通常使用 `hanging-indent` 代替。
- **`entry-spacing`**：单位为标准行高。`0` 表示条目间无额外空白（紧凑排列），`1` 表示条目间空一行。中文学术期刊通常使用 `0`。
- **`subsequent-author-substitute`**：仅在 bibliography 有 `<sort>` 且按作者排序时有效。替代符号在中文样式中常用三字线"———"，英文样式中常用三个 em dash "———" 或六个短横线 "------"。
- **`sort` 的位置**：`<sort>` 必须是 `<bibliography>` 的第一个子元素（在 `<layout>` 之前）。numeric 格式不需要显式排序（默认按 `citation-number` 排），但 author-date 和 note 格式通常需要按作者+年份排序。
- **双语 layout 的 suffix**：中文条目 `suffix="。"` 和英文条目 `suffix="."` 是分别设置在各自的 `<layout>` 元素上的，这样可以确保不同语言的条目使用对应的标点符号。
- **`太平洋学报.csl` 的 bibliography 特征**：使用 `entry-spacing="0"`（紧凑）、`second-field-align="flush"`（编号对齐），带 `[n]` 编号，中英文条目分别以 `。` 和 `.` 结尾。没有显式 `<sort>`，因为 note 格式的 bibliography 默认按 `citation-number` 排序。

