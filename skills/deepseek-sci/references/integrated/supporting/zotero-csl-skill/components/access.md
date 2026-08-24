# Integrated supporting reference: zotero-csl-skill/components/access.md

> Embedded source: `embedded-source/zotero-csl-skill/components/access.md`
> This file is part of the single `deepseek-sci` skill. Apply the parent Python-only and provenance rules.

# access -- DOI/URL

## 参数

| 参数 | 类型 | 可选值 | 默认 | 说明 |
|------|------|--------|------|------|
| doi | string | `true` / `false` / `prefix` | `false` | 是否显示 DOI。`prefix` 表示加 `https://doi.org/` 前缀输出完整链接 |
| url | string | `always` / `never` / `webpage-only` | `webpage-only` | URL 显示策略 |
| accessed-date | boolean | `true` / `false` | `false` | 是否显示访问日期 |

## 模板

### DOI 优先（有 DOI 显示 DOI，否则显示 URL）

```xml
<macro name="access">
  <choose>
    <if variable="DOI">
      <!-- doi="prefix" 时加前缀 -->
      <text variable="DOI" prefix="https://doi.org/"/>
    </if>
    <else-if variable="URL">
      <text variable="URL"/>
    </else-if>
  </choose>
  <!-- accessed-date="true" 时追加访问日期 -->
  <group prefix="（" suffix="）">
    <date variable="accessed" form="text"/>
  </group>
</macro>
```

### 仅 URL

```xml
<macro name="access">
  <text variable="URL"/>
  <!-- 可选：附加访问日期 -->
  <group prefix=" [" suffix="]">
    <date variable="accessed" form="text"/>
  </group>
</macro>
```

### 仅 webpage 类型显示 URL

这是《太平洋学报》等中文社科期刊的常见做法。参考 `太平洋学报.csl` 中的实现：

```xml
<!-- 英文 -->
<macro name="access-en">
  <choose>
    <if type="post post-weblog software webpage" match="any">
      <text variable="URL"/>
    </if>
  </choose>
</macro>

<!-- 中文 -->
<macro name="access-zh">
  <choose>
    <if type="post post-weblog software webpage" match="any">
      <text variable="URL"/>
    </if>
  </choose>
</macro>
```

### 不显示任何链接

```xml
<macro name="access">
  <!-- 空 macro，不输出任何内容 -->
</macro>
```

## 注意事项

- CSL 中 DOI 变量名为全大写 `DOI`，URL 变量名为全大写 `URL`。
- `doi="prefix"` 需要手动拼接前缀 `https://doi.org/`，因为 Zotero 存储的 DOI 字段通常只是标识符（如 `10.1234/xxx`），不含协议前缀。
- `accessed-date` 对应 CSL 的 `accessed` 日期变量，通常在网页类型中使用，格式如 `2024-01-15`。
- 中文样式中访问日期常用中文括号包裹，英文样式常用方括号。
- `webpage-only` 模式通过 `<if type="post post-weblog software webpage">` 限定类型，是中文学术期刊最常见的策略。
- 如果同时需要 DOI 和 accessed-date，应将访问日期放在 DOI 之后，用适当分隔符连接。

