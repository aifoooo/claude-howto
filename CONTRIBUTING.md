<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# 为 Claude How To 做贡献

感谢您对贡献此项目感兴趣！本指南将帮助您了解如何有效地做出贡献。

## 关于本项目

Claude How To 是一份视觉化、示例驱动的 Claude Code 指南。我们提供：
- **Mermaid 图表** 解释功能工作原理
- **可直接使用的生产就绪模板**
- **带上下文和最佳实践的真实案例**
- **从入门到高级的渐进式学习路径**

## 贡献类型

### 1. 新示例或模板
为现有功能添加示例（斜杠命令、技能、钩子等）：
- 可直接复制粘贴的代码
- 清晰的工作原理说明
- 使用场景和优势
- 故障排除提示

### 2. 文档改进
- 澄清混淆的章节
- 修复拼写和语法错误
- 添加缺失的信息
- 改进代码示例

### 3. 功能指南
为新的 Claude Code 功能创建指南：
- 逐步教程
- 架构图
- 常见模式和反模式
- 真实工作流程

### 4. Bug 报告
报告您遇到的问题：
- 描述您期望的结果
- 描述实际发生的情况
- 包含复现步骤
- 添加相关的 Claude Code 版本和操作系统

### 5. 反馈和建议
帮助改进指南：
- 建议更好的解释
- 指出覆盖范围的空白
- 推荐新的章节或重组

## 入门指南

### 1. Fork 和 Clone
```bash
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto
```

### 2. 创建分支
使用描述性的分支名称：
```bash
git checkout -b add/feature-name
git checkout -b fix/issue-description
git checkout -b docs/improvement-area
```

### 3. 设置您的环境

预提交钩子在每次提交前本地运行与 CI 相同的检查。所有四项检查必须通过，PR 才会被接受。

**必需依赖：**

```bash
# Python 工具（uv 是此项目的包管理器）
pip install uv
uv venv
source .venv/bin/activate
uv pip install -r scripts/requirements-dev.txt

# Markdown linter（Node.js）
npm install -g markdownlint-cli

# Mermaid 图表验证器（Node.js）
npm install -g @mermaid-js/mermaid-cli

# 安装 pre-commit 并激活钩子
uv pip install pre-commit
pre-commit install
```

**验证您的设置：**

```bash
pre-commit run --all-files
```

每次提交时运行的钩子：

| 钩子 | 检查内容 |
|------|----------|
| `markdown-lint` | Markdown 格式和结构 |
| `cross-references` | 相对链接、锚点、代码围栏 |
| `mermaid-syntax` | 所有 ` ```mermaid ` 块正确解析 |
| `link-check` | 外部 URL 可访问 |
| `build-epub` | EPUB 生成无错误（仅在 `.md` 更改时） |

## 目录结构

```
├── 01-slash-commands/      # 用户调用的快捷方式
├── 02-memory/              # 持久化上下文示例
├── 03-skills/              # 可复用能力
├── 04-subagents/           # 专业 AI 助手
├── 05-mcp/                 # Model Context Protocol 示例
├── 06-hooks/               # 事件驱动自动化
├── 07-plugins/             # 捆绑功能
├── 08-checkpoints/         # 会话快照
├── 09-advanced-features/   # 规划、思考、后台任务
├── 10-cli/                 # CLI 参考
├── scripts/                # 构建和实用脚本
└── README.md               # 主指南
```

## 如何贡献示例

### 添加斜杠命令
1. 在 `01-slash-commands/` 中创建 `.md` 文件
2. 包含：
   - 清晰的功能描述
   - 使用场景
   - 安装说明
   - 使用示例
   - 自定义提示
3. 更新 `01-slash-commands/README.md`

### 添加技能
1. 在 `03-skills/` 中创建目录
2. 包含：
   - `SKILL.md` - 主文档
   - `scripts/` - 辅助脚本（如需要）
   - `templates/` - 提示模板
   - README 中的使用示例
3. 更新 `03-skills/README.md`

### 添加子代理
1. 在 `04-subagents/` 中创建 `.md` 文件
2. 包含：
   - Agent 目的和能力
   - 系统提示结构
   - 示例使用场景
   - 集成示例
3. 更新 `04-subagents/README.md`

### 添加 MCP 配置
1. 在 `05-mcp/` 中创建 `.json` 文件
2. 包含：
   - 配置说明
   - 所需环境变量
   - 设置说明
   - 使用示例
3. 更新 `05-mcp/README.md`

### 添加钩子
1. 在 `06-hooks/` 中创建 `.sh` 文件
2. 包含：
   - Shebang 和描述
   - 清晰注释解释逻辑
   - 错误处理
   - 安全考虑
3. 更新 `06-hooks/README.md`

## 写作指南

### Markdown 样式
- 使用清晰的标题（H2 为章节，H3 为子章节）
- 保持段落简短且聚焦
- 使用项目符号列表
- 包含带语言规范的代码块
- 在章节之间添加空行

### 代码示例
- 使示例可直接复制使用
- 为非显而易见的逻辑添加注释
- 同时包含简单版本和高级版本
- 展示真实使用场景
- 突出潜在问题

### 文档
- 解释"为什么"而不仅仅是"是什么"
- 包含前置条件
- 添加故障排除章节
- 链接到相关主题
- 保持入门友好

### JSON/YAML
- 使用适当的缩进（一致使用 2 或 4 个空格）
- 添加解释配置的注释
- 包含验证示例

### 图表
- 尽可能使用 Mermaid
- 保持图表简单易读
- 在图表下方添加描述
- 链接到相关章节

## 提交指南

遵循约定式提交格式：
```
type(scope): description

[optional body]
```

类型：
- `feat`: 新功能或示例
- `fix`: Bug 修复或更正
- `docs`: 文档更改
- `refactor`: 代码重构
- `style`: 格式更改
- `test`: 测试添加或更改
- `chore`: 构建、依赖等

示例：
```
feat(slash-commands): Add API documentation generator
docs(memory): Improve personal preferences example
fix(README): Correct table of contents link
docs(skills): Add comprehensive code review skill
```

## 提交前

### 检查清单
- [ ] 代码遵循项目样式和约定
- [ ] 新示例包含清晰文档
- [ ] README 文件已更新（本地和根目录）
- [ ] 无敏感信息（API 密钥、凭据）
- [ ] 示例已测试且可用
- [ ] 链接已验证且正确
- [ ] 文件权限正确（脚本可执行）
- [ ] 提交消息清晰且描述性强

### 本地测试
```bash
# 运行所有 pre-commit 检查（与 CI 相同）
pre-commit run --all-files

# 查看您的更改
git diff
```

## Pull Request 流程

1. **创建带有清晰描述的 PR**：
   - 这添加/修复了什么？
   - 为什么需要它？
   - 相关问题（如果有）

2. **包含相关详细信息**：
   - 新功能？包含使用场景
   - 文档？解释改进
   - 示例？展示前后对比

3. **链接到问题**：
   - 使用 `Closes #123` 自动关闭相关问题

4. **耐心等待审查**：
   - 维护者可能会提出改进建议
   - 根据反馈迭代
   - 最终决定权归维护者

## 代码审查流程

审查者将检查：
- **准确性**：它是否按描述工作？
- **质量**：它是否生产就绪？
- **一致性**：它是否遵循项目模式？
- **文档**：它是否清晰完整？
- **安全**：是否有漏洞？

## 报告问题

### Bug 报告
包含：
- Claude Code 版本
- 操作系统
- 复现步骤
- 期望行为
- 实际行为
- 如适用，附上截图

### 功能请求
包含：
- 使用场景或要解决的问题
- 建议的解决方案
- 您考虑过的替代方案
- 其他上下文

### 文档问题
包含：
- 令人困惑或缺失的内容
- 建议的改进
- 示例或参考

## 项目政策

### 敏感信息
- 永远不要提交 API 密钥、令牌或凭据
- 在示例中使用占位符值
- 包含 `.env.example` 用于配置文件
- 记录所需的环境变量

### 代码质量
- 保持示例专注和可读
- 避免过度工程化的解决方案
- 为非显而易见的逻辑添加注释
- 提交前彻底测试

### 知识产权
- 原始内容归作者所有
- 项目使用教育许可证
- 尊重现有版权
- 在需要时提供归属

## 获取帮助

- **问题**：在 GitHub Issues 中打开讨论
- **一般帮助**：查看现有文档
- **开发帮助**：查看类似示例
- **代码审查**：在 PR 中标记维护者

## 认可

贡献者将在以下位置获得认可：
- README.md 贡献者部分
- GitHub 贡献者页面
- 提交历史

## 安全

贡献示例和文档时，请遵循安全编码实践：

- **永远不要硬编码密钥或 API 密钥** - 使用环境变量
- **警告安全影响** - 突出潜在风险
- **使用安全默认值** - 默认启用安全功能
- **验证输入** - 展示适当的输入验证和清理
- **包含安全说明** - 记录安全注意事项

如需报告安全问题，请参阅 [SECURITY.md](SECURITY.md) 了解我们的漏洞报告流程。

## 行为准则

我们致力于提供一个欢迎和包容的社区。请阅读 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) 了解我们的完整社区标准。

简而言之：
- 尊重和包容
- 优雅地欢迎反馈
- 帮助他人学习和成长
- 避免骚扰或歧视
- 向维护者报告问题

所有贡献者都应该维护此准则并相互以善意和尊重相待。

## 许可证

通过向本项目贡献，您同意您的贡献将在 MIT 许可证下获得许可。有关详细信息，请参阅 [LICENSE](LICENSE) 文件。

## 问题？

- 查看 [README](README.md)
- 查看 [LEARNING-ROADMAP.md](LEARNING-ROADMAP.md)
- 查看现有示例
- 打开问题进行讨论

感谢您的贡献！
