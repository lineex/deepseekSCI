# Integrated supporting reference: zotero-csl-skill/components/locators.md

> Embedded source: `embedded-source/zotero-csl-skill/components/locators.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# 卷/期/页

## 参数

| 参数 | 类型 | 可选值 | 默认 | 说明 |
|------|------|--------|------|------|
| volume-format | 格式 | 纯数字 / `"Vol. X"` / `"第X卷"` | 视风格而定 | 卷号的显示格式 |
| issue-format | 格式 | `(X)` / `"No. X"` / `"第X期"` | 视风格而定 | 期号的显示格式 |
| page-format | 格式 | 纯数字 / `"pp. X"` / `"第X页"` | 视风格而定 | 页码的显示格式 |
| page-range-delimiter | 字符 | `"-"` / `"–"` / `"—"` | 视 locale 而定 | 页码范围的连接符 |
| separator | 字符串 | 任意 | 视风格而定 | 卷期之间、期页之间的分隔符 |

## 模板

### 紧凑格式: 15(3): 245-260

典型输出：`15(3): 245-260`

```xml
<!-- 卷期部分（通常嵌入容器宏中） -->
<group>
  <number variable="volume"/>
  <number variable="issue" prefix="(" suffix=")"/>
</group>

<!-- 页码部分（通常作为独立宏） -->
<macro name="page">
  <number variable="page"/>
</macro>
```

完整组合示例（在容器宏内）：

```xml
<macro name="container-periodical">
  <group delimiter=", ">
    <text variable="container-title" font-style="italic"/>
    <group>
      <number variable="volume"/>
      <number variable="issue" prefix="(" suffix=")"/>
    </group>
  </group>
</macro>

<!-- 页码在 entry-layout 中单独引用 -->
<macro name="page">
  <number variable="page"/>
</macro>
```

### 英文标签: Vol. 15, No. 3, pp. 245-260

典型输出：`Vol. 15, No. 3, pp. 245-260`

```xml
<!-- 卷 -->
<macro name="volume-en">
  <choose>
    <if is-numeric="volume">
      <label variable="volume" form="short" suffix=" "/>
      <number variable="volume"/>
    </if>
    <else>
      <text variable="volume"/>
    </else>
  </choose>
</macro>

<!-- 期刊容器中包含卷期 -->
<macro name="container-periodical-en">
  <group delimiter=", ">
    <text variable="container-title" text-case="title" font-style="italic"/>
    <group>
      <label variable="volume" form="short" text-case="capitalize-first"/>
      <number variable="volume"/>
    </group>
    <group>
      <label variable="issue" form="short" text-case="capitalize-first"/>
      <number variable="issue"/>
    </group>
  </group>
</macro>

<!-- 页码 -->
<macro name="page-en">
  <choose>
    <if is-numeric="page">
      <label variable="page" form="short"/>
      <number variable="page"/>
    </if>
    <else>
      <text variable="page"/>
    </else>
  </choose>
</macro>
```

> **说明**：`<label variable="volume" form="short"/>` 输出 "Vol."，`<label variable="issue" form="short"/>` 输出 "No."，`<label variable="page" form="short"/>` 输出 "p." 或 "pp."（自动根据单页/多页切换）。

页码范围连接号通过 locale 控制：

```xml
<locale xml:lang="en">
  <terms>
    <term name="page-range-delimiter">-</term>
  </terms>
</locale>
```

### 中文格式: 第15卷第3期，第245-260页

典型输出：`第15卷第3期，第245—260页`

```xml
<!-- 卷 -->
<macro name="volume-zh">
  <choose>
    <if is-numeric="volume">
      <text value="第"/>
      <number variable="volume"/>
      <label variable="volume" form="short"/>
    </if>
    <else>
      <text variable="volume"/>
    </else>
  </choose>
</macro>

<!-- 期 -->
<macro name="issue-zh">
  <choose>
    <if is-numeric="issue">
      <text value="第"/>
      <number variable="issue"/>
      <label variable="issue" form="short"/>
    </if>
    <else>
      <text variable="issue"/>
    </else>
  </choose>
</macro>

<!-- 页码 -->
<macro name="page-zh">
  <choose>
    <if is-numeric="page">
      <text value="第"/>
      <number variable="page"/>
      <choose>
        <if type="article-newspaper">
          <text value="版"/>
        </if>
        <else>
          <label variable="page" form="short"/>
        </else>
      </choose>
    </if>
    <else>
      <text variable="page"/>
    </else>
  </choose>
</macro>
```

> **说明**：中文的 `<label variable="volume" form="short"/>` 需在 locale 中定义为"卷"，`<label variable="issue" form="short"/>` 为"期"，`<label variable="page" form="short"/>` 为"页"。报纸的页码用"版"而非"页"。

中文页码范围使用一字线（em dash）：

```xml
<locale xml:lang="zh">
  <terms>
    <term name="page-range-delimiter">&#8212;</term>
  </terms>
</locale>
```

### Locator（引用定位）

除了 page（参考文献的页码范围），CSL 还支持 locator（引注中的具体位置）。两者格式类似但用途不同：

```xml
<!-- 英文 locator -->
<macro name="locator-en">
  <choose>
    <if is-numeric="locator">
      <label variable="locator" form="short"/>
      <number variable="locator"/>
    </if>
    <else>
      <text variable="locator"/>
    </else>
  </choose>
</macro>

<!-- 中文 locator -->
<macro name="locator-zh">
  <choose>
    <if is-numeric="locator">
      <text value="第"/>
      <number variable="locator"/>
      <choose>
        <if type="article-newspaper" locator="page" match="all">
          <text value="版"/>
        </if>
        <else>
          <label variable="locator" form="short"/>
        </else>
      </choose>
    </if>
    <else>
      <text variable="locator"/>
    </else>
  </choose>
</macro>

<!-- 优先显示 locator，无 locator 时显示 page -->
<macro name="locator-or-page-en">
  <choose>
    <if variable="locator">
      <text macro="locator-en"/>
    </if>
    <else>
      <text macro="page-en"/>
    </else>
  </choose>
</macro>

<macro name="locator-or-page-zh">
  <choose>
    <if variable="locator">
      <text macro="locator-zh"/>
    </if>
    <else-if type="article-journal article-magazine" match="none">
      <text macro="page-zh"/>
    </else-if>
  </choose>
</macro>
```

> **说明**：`locator-or-page` 宏的逻辑是：有 locator 时优先显示 locator（用户在引注中指定的具体页码），否则显示 page（参考文献的完整页码范围）。中文期刊文章不显示 page（页码信息已包含在期刊容器中）。

## 注意事项

1. **`<number>` vs `<text variable>`**：对于卷、期、页码，优先使用 `<number>` 元素，它支持 `is-numeric` 条件判断和自动格式化。`<text variable="..."/>` 适用于非数字内容的回退。
2. **`is-numeric` 判断**：使用 `<choose><if is-numeric="volume">` 来区分纯数字和非数字卷号。非数字时直接输出原文（如 "Special Issue"）。
3. **`page-range-format`**：在 `<style>` 根元素上设置，控制页码范围的压缩方式。`expanded` = 完整显示（245-260），`chicago` = Chicago 风格压缩（245-60）。
4. **`page-range-delimiter`**：通过 locale term 控制，英文通常用连字符 `-` 或 en dash `–`，中文用一字线（em dash `—`）。
5. **卷期与容器的关系**：卷期信息通常嵌入容器宏中，而非作为独立宏。英文格式中卷期紧跟期刊名，中文格式中卷期跟在日期之后。
6. **报纸的"版"**：中文报纸的 page 不是"页"而是"版"（如"第3版"），需在 page 宏中特殊处理。

