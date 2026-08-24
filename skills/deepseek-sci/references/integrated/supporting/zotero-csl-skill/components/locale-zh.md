# Integrated supporting reference: zotero-csl-skill/components/locale-zh.md

> Embedded source: `embedded-source/zotero-csl-skill/components/locale-zh.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# locale-zh -- 中文本地化 + 双语模式

## 参数

| 参数 | 类型 | 可选值 | 默认 | 说明 |
|------|------|--------|------|------|
| et-al | string | `等` / 自定义 | `等` | 多作者省略词 |
| and | string | `和` / 自定义 | `和` | 连接最后两位作者的词 |
| edition | string | `版` / 自定义 | `版` | 版本术语 |
| ibid | string | `同上` / 自定义 | `同上` | 同一来源重复引用 |
| in | string | `载` / 自定义 | `载` | 收录于 |
| no-date | string | `出版时间不详` / 自定义 | `出版时间不详` | 无日期时的替代文字 |
| open-quote | string | `"` / 自定义 | `"` | 左双引号 |
| close-quote | string | `"` / 自定义 | `"` | 右双引号 |
| open-inner-quote | string | `'` / 自定义 | `'` | 左单引号 |
| close-inner-quote | string | `'` / 自定义 | `'` | 右单引号 |
| page-range-delimiter | string | `—`（em dash） / 自定义 | `—` | 中文页码连接号 |
| author | string | `著` / 自定义 | `著` | 作者角色标签（form="short"） |
| editor | string | `主编` / 自定义 | `主编` | 编辑角色标签（form="short"） |
| compiler | string | `整理` / 自定义 | `整理` | 整理者角色标签（form="short"） |
| thesis | string | `博士论文` / 自定义 | `博士论文` | 学位论文术语 |
| anonymous | string | `佚名` / 自定义 | `佚名` | 匿名作者替代文字 |

## 模板

### 完整中文 locale 术语覆盖

参考 `太平洋学报.csl` 中的实际定义：

```xml
<locale xml:lang="zh">
  <terms>
    <term name="anonymous">佚名</term>
    <term name="edition" form="short">版</term>
    <term name="ibid">同上</term>
    <term name="in">载</term>
    <term name="no date">出版时间不详</term>
    <term name="open-quote">"</term>
    <term name="close-quote">"</term>
    <term name="open-inner-quote">'</term>
    <term name="close-inner-quote">'</term>
    <!-- 中文页码的连接号使用一字线（em dash） -->
    <term name="page-range-delimiter">&#8212;</term>
    <term name="author" form="short">著</term>
    <term name="editor" form="short">主编</term>
    <term name="compiler" form="short">整理</term>
    <term name="thesis">博士论文</term>
  </terms>
</locale>
```

### citation 双语 layout（zh + default）

在 `<citation>` 中通过 `locale` 属性区分中英文条目的渲染方式。Zotero 根据条目的 `language` 字段判断是否匹配 `zh` locale：

```xml
<citation>
  <!-- 中文条目使用此 layout -->
  <layout delimiter="；" suffix="。" locale="zh">
    <text macro="entry-layout-zh"/>
  </layout>
  <!-- 非中文条目（默认）使用此 layout -->
  <layout delimiter="; " suffix=".">
    <text macro="entry-layout-en"/>
  </layout>
</citation>
```

### bibliography 双语 layout（zh + default）

```xml
<bibliography entry-spacing="0" second-field-align="flush">
  <!-- 中文条目 -->
  <layout locale="zh">
    <text variable="citation-number" prefix="[" suffix="]"/>
    <text macro="entry-layout-zh" suffix="。"/>
  </layout>
  <!-- 非中文条目（默认） -->
  <layout>
    <text variable="citation-number" prefix="[" suffix="]"/>
    <text macro="entry-layout-en" suffix="."/>
  </layout>
</bibliography>
```

## 注意事项

- **双语 layout 机制**：CSL 1.0 支持在 `<layout>` 上指定 `locale` 属性。Zotero 会检查条目的 `language` 字段，若以 `zh` 开头（如 `zh`、`zh-CN`、`zh-TW`），则匹配带有 `locale="zh"` 的 layout；否则使用不带 `locale` 的默认 layout。
- **`language` 字段的填写**：用户需要在 Zotero 条目的「语言」字段中填入 `zh` 或 `zh-CN`，否则中文条目将按英文 layout 渲染。
- **引号覆盖**：中文引号 `""` 和 `''` 通过覆盖 `open-quote`/`close-quote`/`open-inner-quote`/`close-inner-quote` 四个术语实现。在 XML 中使用 `quotes="true"` 属性时会自动使用这些引号。
- **page-range-delimiter**：`&#8212;` 是 Unicode em dash（一字线 —），用于中文页码范围（如"第 23—45 页"）。必须同时在 `<style>` 根元素上设置 `page-range-format="expanded"` 才能正确展开页码。
- **author/editor/compiler 的 `form="short"`**：这些术语在 `<label form="short"/>` 时输出，用于在作者名后追加角色标签（如"张三著""李四主编"）。
- **`et-al` 和 `and`**：如果使用 CSL 内置的 `<name>` 元素的 `et-al-min`/`et-al-use-first` 属性来截断作者列表，`et-al` 术语会被自动使用。中文 locale 下默认应为"等"。`and` 术语在 `<name and="text">` 时用于连接最末两位作者。
- **`ibid` 术语**：仅在 note 样式（`class="note"`）中且使用 `position="ibid"` 条件判断时生效。

