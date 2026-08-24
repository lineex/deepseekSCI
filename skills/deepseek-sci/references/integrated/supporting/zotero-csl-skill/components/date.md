# Integrated supporting reference: zotero-csl-skill/components/date.md

> Embedded source: `embedded-source/zotero-csl-skill/components/date.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# 日期格式

## 参数

| 参数 | 类型 | 可选值 | 默认 | 说明 |
|------|------|--------|------|------|
| default-parts | 属性 | `year` / `year-month` / `year-month-day` | `year-month-day` | 默认显示的日期部分 |
| form | 属性 | `text` / `numeric` | `text` | 日期格式。`text` = "January 1, 2024"，`numeric` = "1/1/2024" |
| 括号 | 格式 | 有/无 | 无 | 年份是否加括号，如 `(2024)` |
| 中文年份 | 格式 | 有/无 | 无 | 是否使用 "2024年" 格式 |

## 模板

### 仅年份

典型输出：`2024`

```xml
<macro name="date">
  <date variable="issued" form="text" date-parts="year"/>
</macro>
```

### 完整日期

典型输出（text 格式）：`January 15, 2024`
典型输出（numeric 格式）：`1/15/2024`

```xml
<!-- text 格式 -->
<macro name="date">
  <date variable="issued" form="text"/>
</macro>

<!-- numeric 格式 -->
<macro name="date">
  <date variable="issued" form="numeric"/>
</macro>
```

### 带括号年份 (2024)

典型输出：`(2024)`

用于 APA 等在作者后紧跟括号年份的风格。

```xml
<macro name="date">
  <date variable="issued" prefix="(" suffix=")">
    <date-part name="year"/>
  </date>
</macro>
```

### 中文年份（2024年 / 2024年第X期）

典型输出：`2024年` / `2024年第3期`

```xml
<!-- 中文日期宏：按文献类型区分详细程度 -->
<macro name="date-zh">
  <choose>
    <if variable="issued">
      <choose>
        <!-- 报纸、网页等需要完整日期 -->
        <if type="article-newspaper collection manuscript personal_communication post post-weblog software webpage" match="any">
          <date variable="issued" form="text"/>
        </if>
        <!-- 书籍、章节附加"版"字 -->
        <else-if type="book chapter classic" match="any">
          <date variable="issued" form="text" date-parts="year"/>
          <text term="edition" form="short"/>
        </else-if>
        <!-- 其他类型仅显示年份 -->
        <else>
          <date variable="issued" form="text" date-parts="year"/>
        </else>
      </choose>
    </if>
    <!-- 无日期时的回退 -->
    <else-if type="classic post post-weblog software webpage" match="none">
      <text term="no date"/>
    </else-if>
  </choose>
</macro>
```

> **说明**：中文 locale 下 `form="text"` 和 `date-parts="year"` 会输出如 "2024年" 的格式（取决于 locale 的日期格式定义）。`<text term="edition" form="short"/>` 在 zh locale 下输出"版"。

需要配合的 locale 定义：

```xml
<locale xml:lang="zh">
  <terms>
    <term name="edition" form="short">版</term>
    <term name="no date">出版时间不详</term>
  </terms>
</locale>
```

### 双语完整方案（date-en + date-zh）

```xml
<macro name="date-en">
  <choose>
    <!-- 档案、手稿等需要完整日期 -->
    <if type="collection manuscript personal_communication" match="any">
      <date variable="issued" form="text"/>
    </if>
    <!-- 期刊仅年份 -->
    <else-if type="article-journal article-magazine" match="any">
      <date variable="issued" form="text" date-parts="year"/>
    </else-if>
    <!-- 报纸需要完整日期 -->
    <else-if type="article-newspaper">
      <date variable="issued" form="text"/>
    </else-if>
    <!-- 网页需要完整日期 -->
    <else-if type="post post-weblog webpage" match="any">
      <date variable="issued" form="text"/>
    </else-if>
    <!-- 其他仅年份 -->
    <else>
      <date variable="issued" form="text" date-parts="year"/>
    </else>
  </choose>
</macro>

<macro name="date-zh">
  <choose>
    <if variable="issued">
      <choose>
        <if type="article-newspaper collection manuscript personal_communication post post-weblog software webpage" match="any">
          <date variable="issued" form="text"/>
        </if>
        <else-if type="book chapter classic" match="any">
          <date variable="issued" form="text" date-parts="year"/>
          <text term="edition" form="short"/>
        </else-if>
        <else>
          <date variable="issued" form="text" date-parts="year"/>
        </else>
      </choose>
    </if>
    <else-if type="classic post post-weblog software webpage" match="none">
      <text term="no date"/>
    </else-if>
  </choose>
</macro>
```

## 注意事项

1. **`form` vs `date-part` 子元素**：使用 `form="text"` 或 `form="numeric"` 会调用 locale 的预定义日期格式，这是最简单的方式。若需自定义格式，可改用 `<date-part>` 子元素逐一指定。
2. **`date-parts` 属性**：只能与 `form` 一起使用，用于截断日期精度。`date-parts="year"` 只显示年，`date-parts="year-month"` 显示年月。
3. **中文"版"字**：对于书籍再版，中文习惯在年份后加"版"（如"2020年版"），通过 `<text term="edition" form="short"/>` 实现。
4. **无日期处理**：当 `issued` 变量为空时，英文输出 "n.d."（CSL 默认），中文可通过 locale 定义 `<term name="no date">出版时间不详</term>` 自定义。
5. **`original-date`**：用于古籍的原始年代（年号等），通过单独的宏处理：
   ```xml
   <macro name="original-date-zh">
     <date variable="original-date">
       <date-part name="year"/>
     </date>
   </macro>
   ```
6. **括号年份**：使用 `prefix="("` `suffix=")"` 直接在 `<date>` 元素上添加，而非包裹在 `<group>` 中，以确保无日期时括号也不会输出。

