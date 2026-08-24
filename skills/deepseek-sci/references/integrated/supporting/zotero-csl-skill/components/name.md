# Integrated supporting reference: zotero-csl-skill/components/name.md

> Embedded source: `embedded-source/zotero-csl-skill/components/name.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# 作者/姓名格式

## 参数

| 参数 | 类型 | 可选值 | 默认 | 说明 |
|------|------|--------|------|------|
| name-as-sort-order | 属性 | `all` / `first` / 不设置 | 不设置 | 姓名是否倒序（Surname, Given）。`all` 全部倒序，`first` 仅第一作者倒序 |
| sort-separator | 字符串 | 任意 | `", "` | 倒序时姓与名之间的分隔符 |
| initialize-with | 字符串 | 如 `". "` 或 `" "` | 不设置 | 名的缩写连接符。设置后自动启用缩写，如 `". "` 得到 `J. K.` |
| initialize | 布尔 | `true` / `false` | `true` | 是否缩写名。设为 `false` 可阻止 `initialize-with` 的缩写行为 |
| delimiter | 字符串 | 任意 | `", "` | 作者之间的分隔符 |
| and | 关键字 | `text` / `symbol` / 不设置 | 不设置 | 最后两位作者间连接词。`text` = "and"，`symbol` = "&" |
| et-al-min | 数字 | 任意正整数 | 不设置 | 作者数达到此值时触发 et al. 省略 |
| et-al-use-first | 数字 | 任意正整数 | 不设置 | 省略时保留前几位作者 |
| delimiter-precedes-last | 关键字 | `always` / `never` / `contextual` | `contextual` | 最后一位作者前是否加分隔符。`contextual` = 3人以上才加 |
| delimiter-precedes-et-al | 关键字 | `always` / `never` / `contextual` | `contextual` | et al. 前是否加分隔符 |
| 是否双语 | 设计决策 | 是/否 | — | 中文用顿号 `、` 作 delimiter，不使用 and 连接词 |

## 模板

### 标准英文（Surname Initial, 逗号分隔）

典型输出：`Smith J. K., Johnson L. M., Wang H.`

```xml
<macro name="author">
  <names variable="author">
    <name name-as-sort-order="all" sort-separator=", " initialize-with=". " delimiter=", "/>
    <substitute>
      <names variable="editor"/>
    </substitute>
  </names>
</macro>
```

### APA 风格（Surname, I., & 连接）

典型输出：`Smith, J. K., Johnson, L. M., & Wang, H.`

```xml
<macro name="author">
  <names variable="author">
    <name name-as-sort-order="all" sort-separator=", " initialize-with=". "
          delimiter=", " and="symbol" delimiter-precedes-last="always"/>
    <substitute>
      <names variable="editor"/>
    </substitute>
  </names>
</macro>
```

带 et al. 省略（7 人以上只显示前 6 人）：

```xml
<macro name="author">
  <names variable="author">
    <name name-as-sort-order="all" sort-separator=", " initialize-with=". "
          delimiter=", " and="symbol" delimiter-precedes-last="always"
          et-al-min="7" et-al-use-first="6"/>
    <substitute>
      <names variable="editor"/>
    </substitute>
  </names>
</macro>
```

### 中文风格（姓名全称，顿号分隔，加"著/主编"标签）

典型输出（book 类型）：`王明远、李华著` / `张三、李四主编`

```xml
<macro name="author-zh">
  <choose>
    <if type="book classic" match="any">
      <names variable="author">
        <name delimiter="、"/>
        <label form="short"/>
        <substitute>
          <names variable="editor"/>
          <names variable="compiler"/>
        </substitute>
      </names>
    </if>
    <else>
      <names variable="author">
        <name delimiter="、"/>
        <substitute>
          <names variable="editor">
            <name delimiter="、"/>
            <label form="short"/>
          </names>
          <names variable="compiler">
            <name delimiter="、"/>
            <label form="short"/>
          </names>
        </substitute>
      </names>
    </else>
  </choose>
</macro>
```

> **说明**：中文 `<name>` 不设置 `initialize-with`，确保显示全名。`<label form="short"/>` 在 `zh` locale 下输出"著""主编""整理"等标签（需配合 locale 定义）。Book 类型直接在作者后附标签，非 book 类型仅在 substitute 的 editor/compiler 后附标签。

需要配合的 locale 定义：

```xml
<locale xml:lang="zh">
  <terms>
    <term name="author" form="short">著</term>
    <term name="editor" form="short">主编</term>
    <term name="compiler" form="short">整理</term>
  </terms>
</locale>
```

### 双语（author-en + author-zh 两个宏）

同时定义两个宏，在 `<citation>` / `<bibliography>` 的 `<layout locale="zh">` 和默认 `<layout>` 中分别调用。

```xml
<macro name="author-en">
  <names variable="author">
    <name and="text"/>
    <label form="short" prefix=", "/>
    <substitute>
      <names variable="editor"/>
      <names variable="compiler"/>
    </substitute>
  </names>
</macro>

<macro name="author-zh">
  <choose>
    <if type="book classic" match="any">
      <names variable="author">
        <name delimiter="、"/>
        <label form="short"/>
        <substitute>
          <names variable="editor"/>
          <names variable="compiler"/>
        </substitute>
      </names>
    </if>
    <else>
      <names variable="author">
        <name delimiter="、"/>
        <substitute>
          <names variable="editor">
            <name delimiter="、"/>
            <label form="short"/>
          </names>
          <names variable="compiler">
            <name delimiter="、"/>
            <label form="short"/>
          </names>
        </substitute>
      </names>
    </else>
  </choose>
</macro>
```

## 注意事项

1. **`initialize` 与 `initialize-with` 的关系**：`initialize-with` 同时控制是否缩写和缩写字符。若要显示全名但仍需 `initialize-with` 定义的句点格式，需在 `<style>` 根元素上设 `initialize="false"`。
2. **中文姓名不应缩写**：中文宏中不设 `initialize-with`，CSL 会自动显示全名。
3. **`<label>` 位置**：`<label>` 必须作为 `<names>` 的直接子元素，紧跟 `<name>` 之后。它输出的是 `<names>` 对应 variable 的角色标签（如 author/editor）。
4. **`<substitute>` 的回退逻辑**：当 `author` 为空时依次尝试 `editor` -> `compiler`。substitute 内的 `<names>` 可以有自己的 `<name>` 和 `<label>` 子元素来覆盖格式。
5. **英文默认 delimiter**：`<name>` 的默认 delimiter 是 `", "`，默认 and 是不设置（即不加连接词），所以 `<name and="text"/>` 会输出 "A, B, and C"。
6. **`delimiter-precedes-last`**：APA 要求始终在 & 前加逗号（Oxford comma），所以设为 `always`。

