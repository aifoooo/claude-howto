<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

<p align="center">
  <a href="https://github.com/trending">
    <img src="https://img.shields.io/badge/GitHub-🔥%20%231%20Trending-purple?style=for-the-badge&logo=github"/>
  </a>
</p>

[![GitHub Stars](https://img.shields.io/github/stars/luongnv89/claude-howto?style=flat&color=gold)](https://github.com/luongnv89/claude-howto/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/luongnv89/claude-howto?style=flat)](https://github.com/luongnv89/claude-howto/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-2.2.0-brightgreen)](CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude_Code-2.1+-purple)](https://code.claude.com)

# 一周末精通 Claude Code

从只会输入 `claude` 到玩转 agents、hooks、skills 和 MCP server —— 配以可视化教程、可直接复制粘贴的模板，以及循序渐进的学习路径。

**[15 分钟入门](#15-分钟入门)** | **[找到你的起点](#不确定从哪里开始)** | **[浏览功能目录](CATALOG.md)**

---

## 目录

- [痛点](#痛点)
- [claude-howto 如何解决](#claude-howto-如何解决)
- [运作原理](#运作原理)
- [不确定从哪里开始？](#不确定从哪里开始)
- [15 分钟入门](#15-分钟入门)
- [学完能做哪些东西？](#学完能做哪些东西)
- [常见问题](#常见问题)
- [贡献指南](#贡献指南)
- [许可证](#许可证)

---

## 痛点

你安装了 Claude Code，跑了几条 prompt。然后呢？

- **官方文档只描述功能，却不教你如何组合。** 你知道斜杠命令存在，却不知道怎么把它和 hooks、memory、subagents 串联成真正省时的工作流。
- **没有清晰的学习路径。** 应该先学 MCP 还是先学 hooks？Skills 和 subagents 谁先谁后？结果你囫囵吞枣地看了一遍，什么都没掌握。
- **示例太基础。** 一个"hello world"级别的斜杠命令示例，无法帮你构建真正能在生产环境使用的代码审查流水线 —— 还要配合 memory、委托给专业 subagents、自动运行安全扫描。

你把 Claude Code 90% 的能力闲置着，而你甚至不知道自己不知道什么。

---

## claude-howto 如何解决

这不是另一份功能手册。是一份**结构化、可视化、案例驱动**的指南，教你用真实场景的模板把每个 Claude Code 功能真正用起来——模板可以直接复制到你的项目里。

| | 官方文档 | 本指南 |
|--|---------------|------------|
| **形式** | 参考文档 | 带 Mermaid 图的可视化教程 |
| **深度** | 功能描述 | 内部运作原理讲解 |
| **示例** | 基础代码片段 | 可直接用于生产的模板 |
| **结构** | 按功能组织 | 循序渐进的学习路径 |
| **上手** | 自主探索 | 带时间估算的引导式路线图 |
| **自测** | 无 | 交互测验，发现知识盲区并生成个性化路径 |

### 你将获得：

- **10 个教程模块**，覆盖 Claude Code 所有功能 —— 从斜杠命令到自定义 agent teams
- **可直接复制粘贴的配置** —— 斜杠命令、CLAUDE.md 模板、hook 脚本、MCP 配置、subagent 定义，以及完整的插件包
- **Mermaid 图表**，展示每个功能内部如何运作，让你理解"为什么"，而不只是"怎么做"
- **引导式学习路径**，用 11-13 小时从入门到精通
- **内置自测** —— 在 Claude Code 里直接运行 `/self-assessment` 或 `/lesson-quiz hooks`，找到自己的薄弱环节

**[开始学习路线 ->](LEARNING-ROADMAP.md)**

---

## 运作原理

### 1. 找到你的水平

做一下[自测](LEARNING-ROADMAP.md#-find-your-level)，或者在 Claude Code 里运行 `/self-assessment`。根据你已有的基础获得个性化路线图。

### 2. 按引导路径学习

按顺序学完 10 个模块 —— 每个模块都建立在前一个的基础上。学习过程中直接把模板复制到你的项目里。

### 3. 把功能组合成工作流

真正的力量在于组合。学会把斜杠命令 + memory + subagents + hooks 连接成自动化流水线，处理代码审查、部署、文档生成等任务。

### 4. 检验你的理解

每个模块学完后运行 `/lesson-quiz [topic]`。测验会精确定位你的遗漏点，让你快速补全。

**[15 分钟入门](#15-分钟入门)**

---

## 已有 5,900+ 开发者使用

- **5,900+ GitHub stars**，来自每天使用 Claude Code 的开发者
- **690+ forks** —— 团队在为本工作流定制
- **活跃维护** —— 每次 Claude Code 发布都会同步更新（最新：v2.2.0，2026 年 3 月）
- **社区驱动** —— 来自真实生产配置的贡献

[![Star History Chart](https://api.star-history.com/svg?repos=luongnv89/claude-howto&type=Date)](https://star-history.com/#luongnv89/claude-howto&Date)

---

## 不确定从哪里开始？

做一下自测，或者根据自己的水平选择：

| 级别 | 你能…… | 从这里开始 | 时间 |
|-------|-----------|------------|------|
| **入门** | 启动 Claude Code 并对话 | [斜杠命令](01-slash-commands/) | ~2.5 小时 |
| **中级** | 使用 CLAUDE.md 和自定义命令 | [Skills](03-skills/) | ~3.5 小时 |
| **高级** | 配置 MCP servers 和 hooks | [高级功能](09-advanced-features/) | ~5 小时 |

**完整 10 模块学习路径：**

| 顺序 | 模块 | 级别 | 时间 |
|-------|--------|-------|------|
| 1 | [斜杠命令](01-slash-commands/) | 入门 | 30 分钟 |
| 2 | [Memory](02-memory/) | 入门+ | 45 分钟 |
| 3 | [检查点](08-checkpoints/) | 中级 | 45 分钟 |
| 4 | [CLI 基础](10-cli/) | 入门+ | 30 分钟 |
| 5 | [Skills](03-skills/) | 中级 | 1 小时 |
| 6 | [Hooks](06-hooks/) | 中级 | 1 小时 |
| 7 | [MCP](05-mcp/) | 中级+ | 1 小时 |
| 8 | [Subagents](04-subagents/) | 中级+ | 1.5 小时 |
| 9 | [高级功能](09-advanced-features/) | 高级 | 2-3 小时 |
| 10 | [插件](07-plugins/) | 高级 | 2 小时 |

**[完整学习路线图 ->](LEARNING-ROADMAP.md)**

---

## 15 分钟入门

```bash
# 1. 克隆本指南
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto

# 2. 复制你的第一个斜杠命令
mkdir -p /path/to/your-project/.claude/commands
cp 01-slash-commands/optimize.md /path/to/your-project/.claude/commands/

# 3. 试试看 — 在 Claude Code 里输入：
# /optimize

# 4. 想学更多？设置项目 memory：
cp 02-memory/project-CLAUDE.md /path/to/your-project/CLAUDE.md

# 5. 安装一个 skill：
cp -r 03-skills/code-review ~/.claude/skills/
```

想要完整配置？这里是**1 小时必要设置**：

```bash
# 斜杠命令（15 分钟）
cp 01-slash-commands/*.md .claude/commands/

# 项目 memory（15 分钟）
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 安装一个 skill（15 分钟）
cp -r 03-skills/code-review ~/.claude/skills/

# 周末目标：加上 hooks、subagents、MCP 和插件
# 按照学习路径一步步来
```

**[查看完整安装参考](#15-分钟入门)**

---

## 学完能做哪些东西？

| 使用场景 | 需要组合的功能 |
|----------|------------------------|
| **自动化代码审查** | 斜杠命令 + Subagents + Memory + MCP |
| **团队新成员入职** | Memory + 斜杠命令 + 插件 |
| **CI/CD 自动化** | CLI 参考 + Hooks + 后台任务 |
| **文档生成** | Skills + Subagents + 插件 |
| **安全审计** | Subagents + Skills + Hooks（只读模式） |
| **DevOps 流水线** | 插件 + MCP + Hooks + 后台任务 |
| **大型重构** | 检查点 + 规划模式 + Hooks |

---

## 常见问题

**这个收费吗？**
免费。MIT 许可证，永久免费。个人项目、工作用、团队用都可以，只需保留许可证声明即可。

**有人维护吗？**
有。本指南与每次 Claude Code 发布保持同步。当前版本：v2.2.0（2026 年 3 月），兼容 Claude Code 2.1+。

**和官方文档有什么区别？**
官方文档是功能参考。本指南是带图表和生产级模板的教程，同时有循序渐进的学习路径。两者互补 —— 从这里入门，需要细节时再查官方文档。

**学完所有内容需要多长时间？**
完整路径 11-13 小时。但 15 分钟就能获得实际收益 —— 复制一个斜杠命令模板然后用起来就够了。

**能配合 Claude Sonnet / Haiku / Opus 使用吗？**
可以。所有模板均适用于 Claude Sonnet 4.6、Claude Opus 4.6 和 Claude Haiku 4.5。

**能贡献内容吗？**
当然。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。欢迎新的示例、bug 修复、文档改进和社区模板。

**能离线阅读吗？**
可以。运行 `uv run scripts/build_epub.py` 生成包含所有内容和渲染后图表的 EPUB 电子书。

---

## 今天就开始精通 Claude Code

你已经安装了 Claude Code。你和 10 倍生产力之间，只差知道怎么用它。本指南给你结构化的路径、可视化的解释和可直接复制粘贴的模板，帮你抵达目标。

MIT 许可证。永久免费。克隆它、fork 它，让它变成你自己的。

**[开始学习路线 ->](LEARNING-ROADMAP.md)** | **[浏览功能目录](CATALOG.md)** | **[15 分钟入门](#15-分钟入门)**

---

<details>
<summary>快速导航 —— 所有功能</summary>

| 功能 | 描述 | 目录 |
|---------|-------------|--------|
| **功能目录** | 完整参考及安装命令 | [CATALOG.md](CATALOG.md) |
| **斜杠命令** | 用户触发的快捷命令 | [01-slash-commands/](01-slash-commands/) |
| **Memory** | 持久化上下文 | [02-memory/](02-memory/) |
| **Skills** | 可复用能力 | [03-skills/](03-skills/) |
| **Subagents** | 专业 AI 助手 | [04-subagents/](04-subagents/) |
| **MCP Protocol** | 外部工具访问 | [05-mcp/](05-mcp/) |
| **Hooks** | 事件驱动自动化 | [06-hooks/](06-hooks/) |
| **插件** | 打包的功能集 | [07-plugins/](07-plugins/) |
| **检查点** | 会话快照与回溯 | [08-checkpoints/](08-checkpoints/) |
| **高级功能** | 规划、思考、后台任务 | [09-advanced-features/](09-advanced-features/) |
| **CLI 参考** | 命令、参数和选项 | [10-cli/](10-cli/) |
| **博客文章** | 真实使用案例 | [Blog Posts](https://medium.com/@luongnv89) |

</details>

<details>
<summary>功能对比</summary>

| 功能 | 调用方式 | 持久性 | 最适合 |
|---------|-----------|------------|----------|
| **斜杠命令** | 手动（`/cmd`） | 仅当前会话 | 快速快捷命令 |
| **Memory** | 自动加载 | 跨会话 | 长期学习 |
| **Skills** | 自动调用 | 文件系统 | 自动化工作流 |
| **Subagents** | 自动委托 | 隔离上下文 | 任务分发 |
| **MCP Protocol** | 自动查询 | 实时 | 实时数据访问 |
| **Hooks** | 事件触发 | 已配置 | 自动化与验证 |
| **插件** | 一个命令 | 所有功能 | 完整解决方案 |
| **检查点** | 手动/自动 | 基于会话 | 安全实验 |
| **规划模式** | 手动/自动 | 规划阶段 | 复杂实现 |
| **后台任务** | 手动 | 任务持续时间 | 长时间运行操作 |
| **CLI 参考** | 终端命令 | 当前会话/脚本 | 自动化与脚本 |

</details>

<details>
<summary>安装快速参考</summary>

```bash
# 斜杠命令
cp 01-slash-commands/*.md .claude/commands/

# Memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Skills
cp -r 03-skills/code-review ~/.claude/skills/

# Subagents
cp 04-subagents/*.md .claude/agents/

# MCP
export GITHUB_TOKEN="token"
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# Hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 插件
/plugin install pr-review

# 检查点（自动启用，在设置中配置）
# 见 08-checkpoints/README.md

# 高级功能（在设置中配置）
# 见 09-advanced-features/config-examples.json

# CLI 参考（无需安装）
# 见 10-cli/README.md 使用示例
```

</details>

<details>
<summary>01. 斜杠命令</summary>

**位置**：[01-slash-commands/](01-slash-commands/)

**是什么**：存为 Markdown 文件的用户触发快捷命令

**示例**：
- `optimize.md` - 代码优化分析
- `pr.md` - Pull Request 准备
- `generate-api-docs.md` - API 文档生成器

**安装**：
```bash
cp 01-slash-commands/*.md /path/to/project/.claude/commands/
```

**用法**：
```
/optimize
/pr
/generate-api-docs
```

**了解更多**：[Discovering Claude Code Slash Commands](https://medium.com/@luongnv89/discovering-claude-code-slash-commands-cdc17f0dfb29)

</details>

<details>
<summary>02. Memory</summary>

**位置**：[02-memory/](02-memory/)

**是什么**：跨会话持久化的上下文

**示例**：
- `project-CLAUDE.md` - 全团队项目标准
- `directory-api-CLAUDE.md` - 目录特定规则
- `personal-CLAUDE.md` - 个人偏好

**安装**：
```bash
# 项目 memory
cp 02-memory/project-CLAUDE.md /path/to/project/CLAUDE.md

# 目录 memory
cp 02-memory/directory-api-CLAUDE.md /path/to/project/src/api/CLAUDE.md

# 个人 memory
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

**用法**：Claude 自动加载

</details>

<details>
<summary>03. Skills</summary>

**位置**：[03-skills/](03-skills/)

**是什么**：可复用、自动调用的能力，包含指令和脚本

**示例**：
- `code-review/` - 带脚本的全面代码审查
- `brand-voice/` - 品牌调性一致性检查
- `doc-generator/` - API 文档生成器

**安装**：
```bash
# 个人 skills
cp -r 03-skills/code-review ~/.claude/skills/

# 项目 skills
cp -r 03-skills/code-review /path/to/project/.claude/skills/
```

**用法**：相关内容自动触发

</details>

<details>
<summary>04. Subagents</summary>

**位置**：[04-subagents/](04-subagents/)

**是什么**：带有隔离上下文和自定义提示的专业 AI 助手

**示例**：
- `code-reviewer.md` - 全面的代码质量分析
- `test-engineer.md` - 测试策略和覆盖率
- `documentation-writer.md` - 技术文档
- `secure-reviewer.md` - 安全审查（只读）
- `implementation-agent.md` - 完整功能实现

**安装**：
```bash
cp 04-subagents/*.md /path/to/project/.claude/agents/
```

**用法**：由主 agent 自动委托

</details>

<details>
<summary>05. MCP Protocol</summary>

**位置**：[05-mcp/](05-mcp/)

**是什么**：Model Context Protocol，用于访问外部工具和 API

**示例**：
- `github-mcp.json` - GitHub 集成
- `database-mcp.json` - 数据库查询
- `filesystem-mcp.json` - 文件操作
- `multi-mcp.json` - 多 MCP server

**安装**：
```bash
# 设置环境变量
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# 通过 CLI 添加 MCP server
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# 或手动添加到项目 .mcp.json（见 05-mcp/ 示例）
```

**用法**：配置好之后 MCP 工具自动对 Claude 可用

</details>

<details>
<summary>06. Hooks</summary>

**位置**：[06-hooks/](06-hooks/)

**是什么**：事件驱动的 shell 命令，在响应 Claude Code 事件时自动执行

**示例**：
- `format-code.sh` - 写入前自动格式化代码
- `pre-commit.sh` - 提交前运行测试
- `security-scan.sh` - 扫描安全问题
- `log-bash.sh` - 记录所有 bash 命令
- `validate-prompt.sh` - 验证用户提示词
- `notify-team.sh` - 事件发生时发送通知

**安装**：
```bash
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

在 `~/.claude/settings.json` 中配置 hooks：
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/format-code.sh"]
    }],
    "PostToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/security-scan.sh"]
    }]
  }
}
```

**用法**：hooks 在事件发生时自动执行

**Hook 类型**（4 种类型，25 个事件）：
- **工具 Hooks**：`PreToolUse`、`PostToolUse`、`PostToolUseFailure`、`PermissionRequest`
- **会话 Hooks**：`SessionStart`、`SessionEnd`、`Stop`、`StopFailure`、`SubagentStart`、`SubagentStop`
- **任务 Hooks**：`UserPromptSubmit`、`TaskCompleted`、`TaskCreated`、`TeammateIdle`
- **生命周期 Hooks**：`ConfigChange`、`CwdChanged`、`FileChanged`、`PreCompact`、`PostCompact`、`WorktreeCreate`、`WorktreeRemove`、`Notification`、`InstructionsLoaded`、`Elicitation`、`ElicitationResult`

</details>

<details>
<summary>07. 插件</summary>

**位置**：[07-plugins/](07-plugins/)

**是什么**：命令、agents、MCP 和 hooks 的打包集合

**示例**：
- `pr-review/` - 完整的 PR 审查工作流
- `devops-automation/` - 部署和监控
- `documentation/` - 文档生成

**安装**：
```bash
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

**用法**：使用打包好的斜杠命令和功能

</details>

<details>
<summary>08. 检查点和回溯</summary>

**位置**：[08-checkpoints/](08-checkpoints/)

**是什么**：保存对话状态并回溯到之前的点，以探索不同方法

**核心概念**：
- **检查点（Checkpoint）**：对话状态的快照
- **回溯（Rewind）**：返回之前的检查点
- **分支点（Branch Point）**：从同一检查点探索多个方案

**用法**：
```
# 检查点随每个用户 prompt 自动创建
# 要回溯，按 Esc 两次或使用：
/rewind

# 然后选择五个选项之一：
# 1. 恢复代码和对话
# 2. 仅恢复对话
# 3. 仅恢复代码
# 4. 从这里总结
# 5. 算了
```

**使用场景**：
- 尝试不同的实现方案
- 从错误中恢复
- 安全实验
- 对比不同解决方案
- A/B 测试不同设计

</details>

<details>
<summary>09. 高级功能</summary>

**位置**：[09-advanced-features/](09-advanced-features/)

**是什么**：面向复杂工作流和自动化的高级能力

**包含内容**：
- **规划模式（Planning Mode）** — 编程前创建详细实现计划
- **扩展思考（Extended Thinking）** — 复杂问题深度推理（用 `Alt+T` / `Option+T` 切换）
- **后台任务（Background Tasks）** — 不阻塞地运行长时间操作
- **权限模式（Permission Modes）** — `default`、`acceptEdits`、`plan`、`dontAsk`、`bypassPermissions`
- **无头模式（Headless Mode）** — 在 CI/CD 中运行 Claude Code：`claude -p "Run tests and generate report"`
- **会话管理** — `/resume`、`/rename`、`/fork`、`claude -c`、`claude -r`
- **配置** — 在 `~/.claude/settings.json` 中自定义行为

详见 [config-examples.json](09-advanced-features/config-examples.json) 中的完整配置。

</details>

<details>
<summary>10. CLI 参考</summary>

**位置**：[10-cli/](10-cli/)

**是什么**：Claude Code 完整命令行接口参考

**快速示例**：
```bash
# 交互模式
claude "explain this project"

# 打印模式（非交互）
claude -p "review this code"

# 处理文件内容
cat error.log | claude -p "explain this error"

# JSON 输出供脚本使用
claude -p --output-format json "list functions"

# 恢复会话
claude -r "feature-auth" "continue implementation"
```

**使用场景**：CI/CD 流水线集成、脚本自动化、批处理、多会话工作流、自定义 agent 配置

</details>

<details>
<summary>示例工作流</summary>

### 完整代码审查工作流

```markdown
# 使用：斜杠命令 + Subagents + Memory + MCP

用户：/review-pr

Claude：
1. 加载项目 memory（编码规范）
2. 通过 GitHub MCP 获取 PR
3. 委托给 code-reviewer subagent
4. 委托给 test-engineer subagent
5. 综合 findings
6. 提供全面审查
```

### 自动化文档

```markdown
# 使用：Skills + Subagents + Memory

用户："生成 auth 模块的 API 文档"

Claude：
1. 加载项目 memory（文档规范）
2. 检测到文档生成请求
3. 自动调用 doc-generator skill
4. 委托给 api-documenter subagent
5. 创建带示例的完整文档
```

### DevOps 部署

```markdown
# 使用：插件 + MCP + Hooks

用户：/deploy production

Claude：
1. 运行 pre-deploy hook（验证环境）
2. 委托给 deployment-specialist subagent
3. 通过 Kubernetes MCP 执行部署
4. 监控进度
5. 运行 post-deploy hook（健康检查）
6. 报告状态
```

</details>

<details>
<summary>目录结构</summary>

```
├── 01-slash-commands/
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   └── README.md
├── 02-memory/
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   └── README.md
├── 03-skills/
│   ├── code-review/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   └── templates/
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   └── templates/
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   └── README.md
├── 04-subagents/
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   └── README.md
├── 05-mcp/
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
├── 06-hooks/
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   └── README.md
├── 07-plugins/
│   ├── pr-review/
│   ├── devops-automation/
│   ├── documentation/
│   └── README.md
├── 08-checkpoints/
│   ├── checkpoint-examples.md
│   └── README.md
├── 09-advanced-features/
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
├── 10-cli/
│   └── README.md
└── README.md (this file)
```

</details>

<details>
<summary>最佳实践</summary>

### 应该做
- 从简单的斜杠命令开始
- 逐步添加功能
- 用 memory 记录团队规范
- 先在本地测试配置
- 记录自定义实现
- 对项目配置进行版本控制
- 与团队共享插件

### 不应该做
- 不要创建冗余功能
- 不要硬编码凭据
- 不要跳过文档
- 不要把简单任务复杂化
- 不要忽略安全最佳实践
- 不要提交敏感数据

</details>

<details>
<summary>故障排查</summary>

### 功能未加载
1. 检查文件位置和命名
2. 验证 YAML frontmatter 语法
3. 检查文件权限
4. 查看 Claude Code 版本兼容性

### MCP 连接失败
1. 验证环境变量
2. 检查 MCP server 安装
3. 测试凭据
4. 查看网络连接

### Subagent 未委托
1. 检查工具权限
2. 验证 agent 描述清晰度
3. 查看任务复杂度
4. 独立测试 agent

</details>

<details>
<summary>测试</summary>

本项目包含全面的自动化测试：

- **单元测试**：使用 pytest 的 Python 测试（Python 3.10、3.11、3.12）
- **代码质量**：使用 Ruff 的 linting 和格式化
- **安全**：使用 Bandit 的漏洞扫描
- **类型检查**：使用 mypy 的静态类型分析
- **构建验证**：EPUB 生成测试
- **覆盖率追踪**：Codecov 集成

```bash
# 安装开发依赖
uv pip install -r requirements-dev.txt

# 运行所有单元测试
pytest scripts/tests/ -v

# 带覆盖率报告运行测试
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# 运行代码质量检查
ruff check scripts/
ruff format --check scripts/

# 运行安全扫描
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/

# 运行类型检查
mypy scripts/ --ignore-missing-imports
```

测试在每次推送到 `main`/`develop` 以及每个 PR 到 `main` 时自动运行。详见 [TESTING.md](.github/TESTING.md)。

</details>

<details>
<summary>EPUB 生成</summary>

想离线阅读本指南？生成 EPUB 电子书：

```bash
uv run scripts/build_epub.py
```

这会创建 `claude-howto-guide.epub`，包含所有内容和渲染后的 Mermaid 图表。

详见 [scripts/README.md](scripts/README.md)。

</details>

<details>
<summary>贡献</summary>

发现问题或想贡献示例？我们非常欢迎！

**请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详细指南：**
- 贡献类型（示例、文档、功能、bug、反馈）
- 如何搭建开发环境
- 目录结构及如何添加内容
- 写作指南和最佳实践
- 提交和 PR 流程

**我们的社区准则：**
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - 我们如何对待彼此
- [SECURITY.md](SECURITY.md) - 安全政策和漏洞报告

### 报告安全问题

如果你发现安全漏洞，请负责任地报告：

1. **使用 GitHub 私密漏洞报告**：https://github.com/luongnv89/claude-howto/security/advisories
2. **或阅读** [.github/SECURITY_REPORTING.md](.github/SECURITY_REPORTING.md) 了解详细说明
3. **不要** 为安全漏洞开公开 issue

快速开始：
1. Fork 并克隆仓库
2. 创建描述性分支（`add/功能名`、`fix/bug`、`docs/改进`）
3. 按指南进行修改
4. 提交带清晰描述的 pull request

**需要帮助？** 开一个 issue 或 discussion，我们会引导你完成流程。

</details>

<details>
<summary>更多资源</summary>

- [Claude Code 文档](https://code.claude.com/docs/en/overview)
- [MCP 协议规范](https://modelcontextprotocol.io)
- [Skills 仓库](https://github.com/luongnv89/skills) - 可直接使用的 skills 集合
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [Boris Cherny 的 Claude Code 工作流](https://x.com/bcherny/status/2007179832300581177) - Claude Code 创建者分享的系统化工作流：并行 agents、共享 CLAUDE.md、Plan 模式、斜杠命令、subagents，以及用于自主长时间会话的验证 hooks。

</details>

---

## 贡献指南

我们欢迎贡献！详见 [Contributing Guide](CONTRIBUTING.md)。

## 贡献者

感谢所有为这个项目做出贡献的人！

| 贡献者 | PRs |
|-------------|-----|
| [wjhrdy](https://github.com/wjhrdy) | [#1 - add a tool to create an epub](https://github.com/luongnv89/claude-howto/pull/1) |
| [VikalpP](https://github.com/VikalpP) | [#7 - fix(docs): Use tilde fences for nested code blocks in concepts guide](https://github.com/luongnv89/claude-howto/pull/7) |

---

## 许可证

MIT 许可证 - 见 [LICENSE](LICENSE)。可自由使用、修改和分发。唯一要求是保留许可证声明。

---

**最后更新**：2026 年 3 月
**Claude Code 版本**：2.1+
**兼容模型**：Claude Sonnet 4.6、Claude Opus 4.6、Claude Haiku 4.5
