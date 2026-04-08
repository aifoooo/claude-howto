# Claude How To - 品牌资产

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="logos/claude-howto-logo.svg">
</picture>

Claude How To 项目标志、图标和 favicons 的完整集合。所有资产使用 V3.0 设计：带代码括号（`>`）符号的指南针，代表代码中的引导式导航 — 使用黑/白/灰调色板，配以亮绿色（#22C55E）强调色。

## 目录结构

```
resources/
├── logos/
│   ├── claude-howto-logo.svg       # 主 logo - 浅色模式 (520×120px)
│   └── claude-howto-logo-dark.svg  # 主 logo - 深色模式 (520×120px)
├── icons/
│   ├── claude-howto-icon.svg       # 应用图标 - 浅色模式 (256×256px)
│   └── claude-howto-icon-dark.svg  # 应用图标 - 深色模式 (256×256px)
└── favicons/
    ├── favicon-16.svg              # Favicon - 16×16px
    ├── favicon-32.svg              # Favicon - 32×32px (主要)
    ├── favicon-64.svg              # Favicon - 64×64px
    ├── favicon-128.svg             # Favicon - 128×128px
    └── favicon-256.svg             # Favicon - 256×256px
```

`assets/logo/` 中的额外资产：
```
assets/logo/
├── logo-full.svg       # 标志 + 文字（水平）
├── logo-mark.svg       # 仅指南针符号 (120×120px)
├── logo-wordmark.svg   # 仅文字
├── logo-icon.svg       # 应用图标 (512×512, 圆角)
├── favicon.svg         # 16×16 优化版
├── logo-white.svg      # 深色背景用白色版本
└── logo-black.svg      # 黑色单色版本
```

## 资产概览

### 设计理念（V3.0）

**带代码括号的指南针** — 引导与代码的结合：
- **指南针环** = 导航、找到方向
- **北针（绿色）** = 学习路径上的方向、进度
- **南针（黑色）** = 根基、坚实基础
- **`>` 括号** = 终端提示符、代码、CLI 上下文
- **刻度线** = 精确、结构化学习

### Logos

**文件**：
- `logos/claude-howto-logo.svg`（浅色模式）
- `logos/claude-howto-logo-dark.svg`（深色模式）

**规格**：
- **尺寸**：520×120 px
- **用途**：主要 header/branding logo，带文字
- **使用场景**：
  - 网站 header
  - README 徽章
  - 营销材料
  - 印刷材料
- **格式**：SVG（完全可缩放）
- **模式**：浅色（白色背景）和深色（#0A0A0A 背景）

### Icons

**文件**：
- `icons/claude-howto-icon.svg`（浅色模式）
- `icons/claude-howto-icon-dark.svg`（深色模式）

**规格**：
- **尺寸**：256×256 px
- **用途**：应用图标、头像、缩略图
- **使用场景**：
  - 应用图标
  - 头像
  - 社交媒体缩略图
  - 文档标题
- **格式**：SVG（完全可缩放）
- **模式**：浅色（白色背景）和深色（#0A0A0A 背景）

**设计元素**：
- 带基点和间点刻度线的指南针环
- 绿色北针（方向/引导）
- 黑色南针（根基）
- 中心 `>` 代码括号（终端/CLI）
- 绿色中心点强调

### Favicons

针对网页使用优化的多尺寸版本：

| 文件 | 尺寸 | DPI | 用途 |
|------|------|-----|-------|
| `favicon-16.svg` | 16×16 px | 1x | 浏览器标签（较老浏览器） |
| `favicon-32.svg` | 32×32 px | 1x | 标准浏览器 favicon |
| `favicon-64.svg` | 64×64 px | 1x-2x | 高 DPI 显示屏 |
| `favicon-128.svg` | 128×128 px | 2x | Apple touch 图标、书签 |
| `favicon-256.svg` | 256×256 px | 4x | 现代浏览器、PWA 图标 |

**优化说明**：
- 16px：最简几何 — 仅环、指针、V 形
- 32px：添加基点刻度线
- 64px+：完整细节，含间点刻度
- 所有保持与主图标视觉一致
- SVG 格式确保任意尺寸清晰显示

## HTML 集成

### 基础 Favicon 设置

```html
<!-- 浏览器 favicon -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">

<!-- Apple touch 图标（移动设备主屏幕） -->
<link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">

<!-- PWA 和现代浏览器 -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">
```

### 完整设置

```html
<head>
  <!-- 主要 favicon -->
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg" sizes="32x32">
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">

  <!-- Apple touch 图标 -->
  <link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">

  <!-- PWA 图标 -->
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">

  <!-- Android -->
  <link rel="shortcut icon" href="/resources/favicons/favicon-256.svg">

  <!-- PWA manifest 引用（如果使用 manifest.json） -->
  <meta name="theme-color" content="#000000">
</head>
```

## 调色板

### 主要颜色
- **黑色**：`#000000`（主要文字、笔触、南针）
- **白色**：`#FFFFFF`（浅色背景）
- **灰色**：`#6B7280`（次要文字、次要刻度线）

### 强调色
- **亮绿色**：`#22C55E`（北针、中心点、强调线 — 仅用于高亮，永不作为背景）

### 深色模式
- **背景**：`#0A0A0A`（近黑色）

### CSS 变量
```css
--color-primary: #000000;
--color-secondary: #6B7280;
--color-accent: #22C55E;
--color-bg-light: #FFFFFF;
--color-bg-dark: #0A0A0A;
```

### Tailwind 配置
```js
colors: {
  brand: {
    primary: '#000000',
    secondary: '#6B7280',
    accent: '#22C55E',
  }
}
```

### 使用指南
- 使用黑色作为主要文字和结构元素
- 使用灰色作为次要/辅助元素
- 绿色**仅**用于高亮 — 指针、点、强调线
- 永不将绿色用作背景色
- 保持 WCAG AA 对比度（最低 4.5:1）

## 设计指南

### Logo 使用
- 用于白色或深色（#0A0A0A）背景
- 按比例缩放
- logo 周围保持留白（最小：logo 高度 / 2）
- 根据背景使用提供的浅色/深色变体

### 图标使用
- 使用标准尺寸：16、32、64、128、256px
- 保持指南针比例
- 按比例缩放

### Favicon 使用
- 根据场景使用适当尺寸
- 16-32px：浏览器标签、书签
- 64px：网站图标
- 128px+：Apple/Android 主屏幕

## SVG 优化

所有 SVG 文件都是扁平设计，无渐变或滤镜：
- 清晰的基于笔触的几何
- 无嵌入光栅
- 优化的路径
- 响应式 viewBox

网页优化：
```bash
# 压缩 SVG 同时保持质量
svgo --config='{
  "js2svg": {
    "indent": 2
  },
  "plugins": [
    "convertStyleToAttrs",
    "removeRasterImages"
  ]
}' input.svg -o output.svg
```

## PNG 转换

为老旧浏览器支持将 SVG 转换为 PNG：

```bash
# 使用 ImageMagick
convert -density 300 -background none favicon-256.svg favicon-256.png

# 使用 Inkscape
inkscape -D -z --file=favicon-256.svg --export-png=favicon-256.png
```

## 无障碍

- 高对比度色彩比率（WCAG AA 合规 — 最低 4.5:1）
- 任意尺寸可识别的清晰几何形状
- 可缩放矢量格式
- 图标中无文字（文字在 wordmark 中单独添加）
- 无红绿色彩依赖

## 归属

这些资产是 Claude How To 项目的一部分。

**许可证**：MIT（请参阅项目 LICENSE 文件）

## 版本历史

- **v3.0**（2026年2月）：黑/白/灰 + 绿色强调调色板的指南针括号设计
- **v2.0**（2026年1月）：翡翠色调色板的 Claude 风格12射线星爆设计
- **v1.0**（2026年1月）：原始六边形递进图标设计

---

**最后更新**：2026年2月
**当前版本**：3.0（指南针括号）
**所有资产**：生产就绪 SVG，完全可缩放，WCAG AA 无障碍
