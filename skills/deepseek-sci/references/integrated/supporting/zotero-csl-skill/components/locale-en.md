# Integrated supporting reference: zotero-csl-skill/components/locale-en.md

> Embedded source: `embedded-source/zotero-csl-skill/components/locale-en.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# locale-en -- 英文本地化

## 参数

| 参数 | 类型 | 可选值 | 默认 | 说明 |
|------|------|--------|------|------|
| page-range-delimiter | string | `"-"` / `"–"` (en dash) | `"–"` | 英文页码连接号 |
| punctuation-in-quote | boolean | `true` / `false` | `false` | 标点是否放在引号内（美式 `true`，英式 `false`） |
| translator-form-short | string | `"trans."` / 自定义 | `"trans."` | 译者标签的缩写形式 |

## 模板

### 英文 locale（使用 hyphen 作页码连接号）

参考 `太平洋学报.csl` 中的实际定义：

```xml
<locale xml:lang="en">
  <style-options punctuation-in-quote="false"/>
  <terms>
    <!-- 英文页码的连接号使用 hyphen -->
    <term name="page-range-delimiter">-</term>
    <term name="translator" form="short">trans.</term>
  </terms>
</locale>
```

### 英文 locale（使用 en dash 作页码连接号）

部分英文期刊（如 APA、Chicago）要求使用 en dash：

```xml
<locale xml:lang="en">
  <style-options punctuation-in-quote="true"/>
  <terms>
    <term name="page-range-delimiter">&#8211;</term>
    <term name="translator" form="short">trans.</term>
  </terms>
</locale>
```

### 英文 locale（美式标点规则）

美式英语将逗号和句号放在引号内：

```xml
<locale xml:lang="en">
  <style-options punctuation-in-quote="true"/>
  <terms>
    <term name="page-range-delimiter">&#8211;</term>
    <term name="translator" form="short">trans.</term>
  </terms>
</locale>
```

### 英文 locale（英式标点规则）

英式英语将标点放在引号外（中文学术期刊常用此设置）：

```xml
<locale xml:lang="en">
  <style-options punctuation-in-quote="false"/>
  <terms>
    <term name="page-range-delimiter">-</term>
    <term name="translator" form="short">trans.</term>
  </terms>
</locale>
```

## 注意事项

- **`punctuation-in-quote`**：此选项控制句号和逗号是否移入引号内。设为 `true` 时，`"Title",` 变为 `"Title,"` ——这是美式英语的标点规则。中文社科期刊引用英文文献时通常设为 `false`。
- **`page-range-delimiter`**：CSL 规范默认使用 en dash (`–`, `&#8211;`)。如果期刊要求使用 hyphen (`-`)，需要在 locale 中显式覆盖。注意此设置需要配合 `<style>` 根元素的 `page-range-format` 属性才能生效。
- **`translator` 缩写**：`form="short"` 的 `translator` 术语用于 `<label form="short"/>` 输出。英文中通常缩写为 `trans.`，显示为 `trans. John Smith` 或 `John Smith, trans.`（取决于 `<names>` 中 `<label>` 的位置）。
- **`xml:lang="en"` 的匹配范围**：此 locale 会匹配所有以 `en` 开头的语言（`en-US`、`en-GB` 等），除非有更具体的 locale 块（如 `xml:lang="en-GB"`）覆盖。
- **与 `default-locale` 的关系**：`<style>` 根元素的 `default-locale` 属性决定了没有 `language` 字段的条目使用哪个 locale。如果设为 `default-locale="en-US"`，则无语言标记的条目默认按英文处理。

