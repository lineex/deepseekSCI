# Integrated supporting reference: zotero-csl-skill/components/citation.md

> Embedded source: `embedded-source/zotero-csl-skill/components/citation.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# citation -- citation 元素

## 参数

| 参数 | 类型 | 可选值 | 默认 | 说明 |
|------|------|--------|------|------|
| format | string | `numeric` / `author-date` / `note` | — | 引用格式类型，对应 `<style>` 的 `class` 属性和 `<category citation-format>` |
| collapse | string | `citation-number` / `year` / `year-suffix` | — | 引用合并策略。`citation-number` 用于 numeric 格式合并连续编号；`year` 用于 author-date 格式合并同作者同年 |
| prefix | string | `"["` / `"("` / 自定义 | — | 引用整体前缀 |
| suffix | string | `"]"` / `")"` / `"."` / `"。"` | — | 引用整体后缀 |
| delimiter | string | `", "` / `"; "` / `"；"` | `", "` | 同一 citation 中多条引用之间的分隔符 |
| disambiguate | string | `add-year-suffix` / `add-names` / `add-givenname` | — | 歧义消解策略（author-date 格式用） |
| sort | string | `citation-number` / `author+year` | — | citation 内部排序方式 |
| note-position | string | `first` / `ibid` / `subsequent` | — | note 格式中的位置判断条件 |

## 模板

### numeric: [1], [1, 3], [1-3]

```xml
<!-- style 根元素需设置 class="in-text" -->
<citation collapse="citation-number">
  <sort>
    <key variable="citation-number"/>
  </sort>
  <layout prefix="[" suffix="]" delimiter=", ">
    <text variable="citation-number"/>
  </layout>
</citation>
```

效果：`[1]`、`[1, 3]`、`[1-3]`（连续编号自动合并为范围）。

### author-date: (Author, 2024)

```xml
<!-- style 根元素需设置 class="in-text" -->
<citation et-al-min="3" et-al-use-first="1" disambiguate-add-year-suffix="true" disambiguate-add-names="true" disambiguate-add-givenname="true" collapse="year">
  <sort>
    <key macro="author"/>
    <key macro="date" sort="ascending"/>
  </sort>
  <layout prefix="(" suffix=")" delimiter="; ">
    <group delimiter=", ">
      <text macro="author-short"/>
      <text macro="date"/>
      <text macro="locator"/>
    </group>
  </layout>
</citation>
```

效果：`(Smith, 2024)`、`(Smith, 2024a, 2024b)`（同作者同年用后缀区分）、`(Smith, 2024; Jones, 2023)`。

### note - 首次引用（完整引用）

参考 `太平洋学报.csl` 中的实际 note 格式：

```xml
<!-- style 根元素需设置 class="note" -->
<citation>
  <!-- 中文条目 layout -->
  <layout delimiter="；" suffix="。" locale="zh">
    <text macro="entry-layout-zh"/>
  </layout>
  <!-- 英文条目 layout（默认） -->
  <layout delimiter="; " suffix=".">
    <text macro="entry-layout-en"/>
  </layout>
</citation>
```

首次引用时输出完整的书目信息（作者、标题、出版信息、页码等），由 `entry-layout-zh` 和 `entry-layout-en` 宏控制。

### note - ibid（同上）

在支持 ibid 的 note 样式中，紧接相同来源的重复引用可简化为"同上"：

```xml
<citation>
  <layout delimiter="；" suffix="。" locale="zh">
    <choose>
      <if position="ibid-with-locator">
        <group delimiter="，">
          <text term="ibid"/>
          <text macro="locator-zh"/>
        </group>
      </if>
      <else-if position="ibid">
        <text term="ibid"/>
      </else-if>
      <else>
        <text macro="entry-layout-zh"/>
      </else>
    </choose>
  </layout>
  <layout delimiter="; " suffix=".">
    <choose>
      <if position="ibid-with-locator">
        <group delimiter=", ">
          <text term="ibid"/>
          <text macro="locator-en"/>
        </group>
      </if>
      <else-if position="ibid">
        <text term="ibid"/>
      </else-if>
      <else>
        <text macro="entry-layout-en"/>
      </else>
    </choose>
  </layout>
</citation>
```

中文输出"同上"（由 `<term name="ibid">同上</term>` 定义），英文输出 "Ibid."。

### note - subsequent（简写引用）

后续引用使用简写形式（通常只保留作者+标题缩写+页码）：

```xml
<citation>
  <layout delimiter="；" suffix="。" locale="zh">
    <choose>
      <if position="ibid-with-locator">
        <group delimiter="，">
          <text term="ibid"/>
          <text macro="locator-zh"/>
        </group>
      </if>
      <else-if position="ibid">
        <text term="ibid"/>
      </else-if>
      <else-if position="subsequent">
        <group delimiter="，">
          <text macro="author-zh"/>
          <text macro="title-short-zh"/>
          <text macro="locator-zh"/>
        </group>
      </else-if>
      <else>
        <text macro="entry-layout-zh"/>
      </else>
    </choose>
  </layout>
  <layout delimiter="; " suffix=".">
    <choose>
      <if position="ibid-with-locator">
        <group delimiter=", ">
          <text term="ibid"/>
          <text macro="locator-en"/>
        </group>
      </if>
      <else-if position="ibid">
        <text term="ibid"/>
      </else-if>
      <else-if position="subsequent">
        <group delimiter=", ">
          <text macro="author-short-en"/>
          <text macro="title-short-en"/>
          <text macro="locator-en"/>
        </group>
      </else-if>
      <else>
        <text macro="entry-layout-en"/>
      </else>
    </choose>
  </layout>
</citation>
```

## 注意事项

- **`class` 属性**：CSL 的 `<style>` 根元素必须指定 `class="in-text"` 或 `class="note"`。numeric 和 author-date 使用 `class="in-text"`，note 使用 `class="note"`。此属性决定 citation 是行内插入还是脚注/尾注。
- **`collapse`**：`citation-number` 合并策略仅在 numeric 格式下有效，可将 `[1, 2, 3]` 合并为 `[1-3]`。`year` 和 `year-suffix` 在 author-date 格式下有效，可将 `(Smith, 2024a; Smith, 2024b)` 合并为 `(Smith, 2024a, b)`。
- **`disambiguate` 系列属性**：在 `<citation>` 元素上设置，仅对 author-date 格式有意义。`disambiguate-add-year-suffix="true"` 会给同作者同年的条目添加 a/b/c 后缀。`disambiguate-add-names="true"` 会展开更多作者名以消除歧义。`disambiguate-add-givenname="true"` 会添加作者名来区分同姓作者。
- **`position` 条件**：note 样式中 `<if position="...">` 可判断引用位置。支持的值包括 `first`（首次引用）、`ibid`（紧接重复引用）、`ibid-with-locator`（紧接重复引用但有不同页码）、`subsequent`（非首次非紧接的重复引用）。判断顺序应为 `ibid-with-locator` > `ibid` > `subsequent` > `first`（else 分支）。
- **双语 layout**：如 `太平洋学报.csl` 所示，通过在 `<layout>` 上指定 `locale="zh"` 区分中英文条目。中文条目使用中文标点（分隔符 `；`，后缀 `。`），英文条目使用英文标点（分隔符 `; `，后缀 `.`）。
- **`sort` 元素**：在 `<citation>` 内部的 `<sort>` 控制同一 citation 中多条引用的排列顺序。numeric 格式通常按 `citation-number` 排序，author-date 通常按作者+年份排序。note 格式一般不排序（按引用顺序）。
- **`太平洋学报.csl` 不使用 position 判断**：该样式在 citation 中直接输出完整引用，没有 ibid 或 subsequent 简写。这是因为其《规定》要求每次脚注都给出完整信息。

