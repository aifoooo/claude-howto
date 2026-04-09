<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# EPUB 构建器脚本

从 Claude How-To markdown 文件构建 EPUB 电子书。

## 功能

- 按文件夹结构组织章节（01-slash-commands、02-memory 等）
- 通过 Kroki.io API 将 Mermaid 图表渲染为 PNG 图片
- 异步并发获取 - 并行渲染所有图表
- 从项目 logo 生成封面图片
- 将内部 markdown 链接转换为 EPUB 章节引用
- 严格错误模式 - 如果任何图表无法渲染则失败

## 要求

- Python 3.10+
- [uv](https://github.com/astral-sh/uv)
- 用于 Mermaid 图表渲染的网络连接

## 快速开始

```bash
# 最简单的方式 - uv 处理一切
uv run scripts/build_epub.py
```

## 开发设置

```bash
# 创建虚拟环境
uv venv

# 激活并安装依赖
source .venv/bin/activate
uv pip install -r requirements-dev.txt

# 运行测试
pytest scripts/tests/ -v

# 运行脚本
python scripts/build_epub.py
```

## 命令行选项

```
用法：build_epub.py [-h] [--root ROOT] [--output OUTPUT] [--verbose]
                     [--timeout TIMEOUT] [--max-concurrent MAX_CONCURRENT]

选项：
  -h, --help            显示此帮助信息并退出
  --root, -r ROOT       根目录（默认：仓库根目录）
  --output, -o OUTPUT   输出路径（默认：claude-howto-guide.epub）
  --verbose, -v         启用详细日志
  --timeout TIMEOUT     API 超时时间（秒）（默认：30）
  --max-concurrent N    最大并发请求数（默认：10）
```

## 示例

```bash
# 带详细输出构建
uv run scripts/build_epub.py --verbose

# 自定义输出位置
uv run scripts/build_epub.py --output ~/Desktop/claude-guide.epub

# 限制并发请求数（如果被限流）
uv run scripts/build_epub.py --max-concurrent 5
```

## 输出

在仓库根目录创建 `claude-howto-guide.epub`。

EPUB 包含：
- 带项目 logo 的封面图片
- 带嵌套章节的目录
- 所有 markdown 内容转换为 EPUB 兼容的 HTML
- 渲染为 PNG 图片的 Mermaid 图表

## 运行测试

```bash
# 使用虚拟环境
source .venv/bin/activate
pytest scripts/tests/ -v

# 或直接使用 uv
uv run --with pytest --with pytest-asyncio \
    --with ebooklib --with markdown --with beautifulsoup4 \
    --with httpx --with pillow --with tenacity \
    pytest scripts/tests/ -v
```

## 依赖

通过 PEP 723 内联脚本元数据管理：

| 包 | 用途 |
|---------|---------|
| `ebooklib` | EPUB 生成 |
| `markdown` | Markdown 转 HTML |
| `beautifulsoup4` | HTML 解析 |
| `httpx` | 异步 HTTP 客户端 |
| `pillow` | 封面图片生成 |
| `tenacity` | 重试逻辑 |

## 故障排查

**构建失败并显示网络错误**：检查网络连接和 Kroki.io 状态。尝试 `--timeout 60`。

**限流**：使用 `--max-concurrent 3` 减少并发请求。

**缺少 logo**：如果未找到 `claude-howto-logo.png`，脚本会生成纯文本封面。
