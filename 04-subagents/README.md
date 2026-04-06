<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Subagents - 完整参考指南

Subagents 是 Claude Code 可以将任务委托给的专业 AI 助手。每个 subagent 都有特定目的，使用与主对话分离的独立上下文窗口，并可以配置特定工具和自定义系统提示。

## 目录

1. [概述](#概述)
2. [核心优势](#核心优势)
3. [文件位置](#文件位置)
4. [配置](#配置)
5. [内置 Subagents](#内置-subagents)
6. [管理 Subagents](#管理-subagents)
7. [使用 Subagents](#使用-subagents)
8. [可恢复代理](#可恢复代理)
9. [链式 Subagents](#链式-subagents)
10. [Subagents 的持久内存](#subagents-的持久内存)
11. [后台 Subagents](#后台-subagents)
12. [Worktree 隔离](#worktree-隔离)
13. [限制可生成的 Subagents](#限制可生成的-subagents)
14. [`claude agents` CLI 命令](#claude-agents-cli-命令)
15. [代理团队（实验性）](#代理团队实验性)
16. [插件 Subagent 安全](#插件-subagent-安全)
17. [架构](#架构)
18. [上下文管理](#上下文管理)
19. [何时使用 Subagents](#何时使用-subagents)
20. [最佳实践](#最佳实践)
21. [此文件夹中的示例 Subagents](#此文件夹中的示例-subagents)
22. [安装说明](#安装说明)
23. [相关概念](#相关概念)

---

## 概述

Subagents 通过以下方式实现 Claude Code 中的委托任务执行：

- 创建具有独立上下文窗口的**隔离 AI 助手**
- 为专业领域提供**自定义系统提示**
- 强制**工具访问控制**以限制能力
- 防止复杂任务造成**上下文污染**
- 实现多个专业任务的**并行执行**

每个 subagent 独立运作，收到干净的状态，只接收其任务所需的特定上下文，然后将结果返回给主代理进行综合。

**快速开始**：使用 `/agents` 命令交互式创建、查看、编辑和管理你的 subagents。

---

## 核心优势

| 优势 | 描述 |
|---------|-------------|
| **上下文保持** | 在独立上下文中运作，防止主对话污染 |
| **专业 expertise** | 针对特定领域微调，成功率更高 |
| **可复用性** | 跨不同项目使用，与团队共享 |
| **灵活权限** | 不同 subagent 类型有不同的工具访问级别 |
| **可扩展性** | 多个代理同时处理不同方面 |

---

## 文件位置

Subagent 文件可以存储在多个位置，具有不同的作用域：

| 优先级 | 类型 | 位置 | 作用域 |
|----------|------|----------|-------|
| 1（最高） | **CLI 定义的** | 通过 `--agents` 标志（JSON） | 仅会话 |
| 2 | **项目 subagents** | `.claude/agents/` | 当前项目 |
| 3 | **用户 subagents** | `~/.claude/agents/` | 所有项目 |
| 4（最低） | **插件代理** | 插件 `agents/` 目录 | 通过插件 |

当存在重复名称时，较高优先级的源优先。

---

## 配置

### 文件格式

Subagent 在 YAML 前置元数据之后定义，后跟 markdown 中的系统提示：

```yaml
---
name: your-sub-agent-name
description: 描述何时应调用此 subagent
tools: tool1, tool2, tool3  # 可选 - 如省略则继承所有工具
disallowedTools: tool4  # 可选 - 明确禁止的工具
model: sonnet  # 可选 - sonnet、opus、haiku 或 inherit
permissionMode: default  # 可选 - 权限模式
maxTurns: 20  # 可选 - 限制代理轮次
skills: skill1, skill2  # 可选 - 预加载到上下文的 skills
mcpServers: server1  # 可选 - 可用的 MCP 服务器
memory: user  # 可选 - 持久内存作用域（user、project、local）
background: false  # 可选 - 作为后台任务运行
effort: high  # 可选 - 推理 effort（low、medium、high、max）
isolation: worktree  # 可选 - git worktree 隔离
initialPrompt: "Start by analyzing the codebase"  # 可选 - 作为主代理运行时的自动提交第一轮
hooks:  # 可选 - 组件作用域的钩子
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/security-check.sh"
---

你的 subagent 的系统提示在这里。这可以是多个段落，
应该清楚定义 subagent 的角色、能力，
以及解决问题的方法。
```

### 配置字段

| 字段 | 必需 | 描述 |
|-------|----------|-------------|
| `name` | 是 | 唯一标识符（小写字母和连字符） |
| `description` | 是 | 目的的自然语言描述。包含"use PROACTIVELY"以鼓励自动调用 |
| `tools` | 否 | 特定工具的逗号分隔列表。省略以继承所有工具。支持 `Agent(agent_name)` 语法以限制可生成的 subagents |
| `disallowedTools` | 否 | subagent 不得使用的工具的逗号分隔列表 |
| `model` | 否 | 使用的模型：`sonnet`、`opus`、`haiku`、完整模型 ID 或 `inherit`。默认为配置的 subagent 模型 |
| `permissionMode` | 否 | `default`、`acceptEdits`、`dontAsk`、`bypassPermissions`、`plan` |
| `maxTurns` | 否 | subagent 可以进行的最大代理轮次 |
| `skills` | 否 | 要预加载的 skills 逗号分隔列表。在启动时将完整 skill 内容注入 subagent 上下文 |
| `mcpServers` | 否 | 使 subagent 可用的 MCP 服务器 |
| `hooks` | 否 | 组件作用域的钩子（PreToolUse、PostToolUse、Stop） |
| `memory` | 否 | 持久内存目录作用域：`user`、`project` 或 `local` |
| `background` | 否 | 设置为 `true` 始终将此 subagent 作为后台任务运行 |
| `effort` | 否 | 推理 effort 级别：`low`、`medium`、`high` 或 `max` |
| `isolation` | 否 | 设置为 `worktree` 以使 subagent 有自己的 git worktree |
| `initialPrompt` | 否 | 当 subagent 作为主代理运行时的自动提交第一轮 |

### 工具配置选项

**选项 1：继承所有工具（省略字段）**
```yaml
---
name: full-access-agent
description: 具有所有可用工具的代理
---
```

**选项 2：指定单个工具**
```yaml
---
name: limited-agent
description: 仅具有特定工具的代理
tools: Read, Grep, Glob, Bash
---
```

**选项 3：条件工具访问**
```yaml
---
name: conditional-agent
description: 具有过滤工具访问的代理
tools: Read, Bash(npm:*), Bash(test:*)
---
```

### 基于 CLI 的配置

使用 `--agents` 标志和 JSON 格式为单个会话定义 subagents：

```bash
claude --agents '{
  "code-reviewer": {
    "description": "Expert code reviewer. Use proactively after code changes.",
    "prompt": "You are a senior code reviewer. Focus on code quality, security, and best practices.",
    "tools": ["Read", "Grep", "Glob", "Bash"],
    "model": "sonnet"
  }
}'
```

**`--agents` 标志的 JSON 格式：**

```json
{
  "agent-name": {
    "description": "Required: when to invoke this agent",
    "prompt": "Required: system prompt for the agent",
    "tools": ["Optional", "array", "of", "tools"],
    "model": "optional: sonnet|opus|haiku"
  }
}
```

**代理定义优先级：**

代理定义按此优先级顺序加载（先匹配优先）：
1. **CLI 定义的** - `--agents` 标志（仅会话，JSON）
2. **项目级** - `.claude/agents/`（当前项目）
3. **用户级** - `~/.claude/agents/`（所有项目）
4. **插件级** - 插件 `agents/` 目录

这允许 CLI 定义在单个会话中覆盖所有其他来源。

---

## 内置 Subagents

Claude Code 包含多个始终可用的内置 subagents：

| 代理 | 模型 | 目的 |
|-------|-------|---------|
| **general-purpose** | 继承 | 复杂的、多步骤任务 |
| **Plan** | 继承 | 为计划模式进行研究 |
| **Explore** | Haiku | 只读代码库探索（快速/中等/非常彻底） |
| **Bash** | 继承 | 在独立上下文中的终端命令 |
| **statusline-setup** | Sonnet | 配置状态行显示 |
| **Claude Code Guide** | Haiku | 回答 Claude Code 功能问题 |

### General-Purpose Subagent

| 属性 | 值 |
|----------|-------|
| **模型** | 继承自父级 |
| **工具** | 所有工具 |
| **目的** | 复杂研究任务、多步骤操作、代码修改 |

**何时使用**：需要探索和修改以及复杂推理的任务。

### Plan Subagent

| 属性 | 值 |
|----------|-------|
| **模型** | 继承自父级 |
| **工具** | Read、Glob、Grep、Bash |
| **目的** | 在计划模式中自动使用以研究代码库 |

**何时使用**：当 Claude 需要在呈现计划之前理解代码库时。

### Explore Subagent

| 属性 | 值 |
|----------|-------|
| **模型** | Haiku（快速、低延迟） |
| **模式** | 严格只读 |
| **工具** | Glob、Grep、Read、Bash（仅只读命令） |
| **目的** | 快速代码库搜索和分析 |

**何时使用**：在不进行更改时搜索/理解代码。

**彻底性级别** - 指定探索深度：
- **"quick"** - 最小探索的快速搜索，适合查找特定模式
- **"medium"** - 中等探索，平衡速度和彻底性，默认方法
- **"very thorough"** - 跨多个位置和命名约定的全面分析，可能需要更长时间

### Bash Subagent

| 属性 | 值 |
|----------|-------|
| **模型** | 继承自父级 |
| **工具** | Bash |
| **目的** | 在独立上下文窗口中执行终端命令 |

**何时使用**：运行可以从隔离上下文中受益的 shell 命令时。

### Statusline Setup Subagent

| 属性 | 值 |
|----------|-------|
| **模型** | Sonnet |
| **工具** | Read、Write、Bash |
| **目的** | 配置 Claude Code 状态行显示 |

**何时使用**：在设置或自定义状态行时。

### Claude Code Guide Subagent

| 属性 | 值 |
|----------|-------|
| **模型** | Haiku（快速、低延迟） |
| **工具** | 只读 |
| **目的** | 回答有关 Claude Code 功能和使用的问题 |

**何时使用**：当用户询问 Claude Code 如何工作或如何使用特定功能时。

---

## 管理 Subagents

### 使用 `/agents` 命令（推荐）

```bash
/agents
```

这提供一个交互式菜单来：
- 查看所有可用 subagents（内置、用户和项目）
- 通过引导设置创建新的 subagents
- 编辑现有自定义 subagents 和工具访问
- 删除自定义 subagents
- 查看存在重复时哪些 subagents 处于活动状态

### 直接文件管理

```bash
# 创建一个项目 subagent
mkdir -p .claude/agents
cat > .claude/agents/test-runner.md << 'EOF'
---
name: test-runner
description: Use proactively to run tests and fix failures
---

You are a test automation expert. When you see code changes, proactively
run the appropriate tests. If tests fail, analyze the failures and fix
them while preserving the original test intent.
EOF

# 创建一个用户 subagent（在所有项目中可用）
mkdir -p ~/.claude/agents
```

---

## 使用 Subagents

### 自动委托

Claude 根据以下内容主动委托任务：
- 你请求中的任务描述
- subagent 配置中的 `description` 字段
- 当前上下文和可用工具

要鼓励主动使用，在你的 `description` 字段中包含"use PROACTIVELY"或"MUST BE USED"：

```yaml
---
name: code-reviewer
description: Expert code review specialist. Use PROACTIVELY after writing or modifying code.
---
```

### 显式调用

你可以显式请求特定的 subagent：

```
> Use the test-runner subagent to fix failing tests
> Have the code-reviewer subagent look at my recent changes
> Ask the debugger subagent to investigate this error
```

### @-Mention 调用

使用 `@` 前缀来保证调用特定 subagent（绕过自动委托启发式）：

```
> @"code-reviewer (agent)" review the auth module
```

### 全会话代理

使用特定代理作为主代理运行整个会话：

```bash
# 通过 CLI 标志
claude --agent code-reviewer

# 通过 settings.json
{
  "agent": "code-reviewer"
}
```

### 列出可用代理

使用 `claude agents` 命令列出来自所有来源的所有已配置代理：

```bash
claude agents
```

---

## 可恢复代理

Subagents 可以通过保留完整上下文继续之前的对话：

```bash
# 初始调用
> Use the code-analyzer agent to start reviewing the authentication module
# 返回 agentId: "abc123"

# 稍后恢复代理
> Resume agent abc123 and now analyze the authorization logic as well
```

**用例**：
- 跨多个会话的长期研究
- 不丢失上下文的迭代改进
- 保持上下文的多步骤工作流

---

## 链式 Subagents

顺序执行多个 subagents：

```bash
> First use the code-analyzer subagent to find performance issues,
  then use the optimizer subagent to fix them
```

这支持复杂工作流，其中一个 subagent 的输出作为另一个的输入。

---

## Subagents 的持久内存

`memory` 字段为 subagents 提供在对话之间保留的持久目录。这允许 subagents 随着时间积累知识，存储笔记、发现和跨会话保留的上下文。

### 内存作用域

| 作用域 | 目录 | 用例 |
|-------|-----------|----------|
| `user` | `~/.claude/agent-memory/<name>/` | 跨所有项目的个人笔记和偏好 |
| `project` | `.claude/agent-memory/<name>/` | 与团队共享的项目特定知识 |
| `local` | `.claude/agent-memory-local/<name>/` | 不提交到版本控制的本地项目知识 |

### 工作原理

- 内存目录中 `MEMORY.md` 的前 200 行自动加载到 subagent 的系统提示中
- `Read`、`Write` 和 `Edit` 工具自动启用，供 subagent 管理其内存文件
- subagent 可以根据需要在其内存目录中创建额外文件

### 示例配置

```yaml
---
name: researcher
memory: user
---

You are a research assistant. Use your memory directory to store findings,
track progress across sessions, and build up knowledge over time.

Check your MEMORY.md file at the start of each session to recall previous context.
```

---

## 后台 Subagents

Subagents 可以在后台运行，释放主对话以进行其他任务。

### 配置

设置 `background: true` 在前置元数据中以始终将 subagent 作为后台任务运行：

```yaml
---
name: long-runner
background: true
description: Performs long-running analysis tasks in the background
---
```

### 键盘快捷键

| 快捷键 | 操作 |
|----------|--------|
| `Ctrl+B` | 将当前运行的 subagent 任务放到后台 |
| `Ctrl+F` | 终止所有后台代理（按两次确认） |

### 禁用后台任务

设置环境变量以完全禁用后台任务支持：

```bash
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1
```

---

## Worktree 隔离

`isolation: worktree` 设置为 subagent 提供自己的 git worktree，允许它独立进行更改而不影响主工作树。

### 配置

```yaml
---
name: feature-builder
isolation: worktree
description: Implements features in an isolated git worktree
tools: Read, Write, Edit, Bash, Grep, Glob
---
```

### 工作原理

- subagent 在独立分支上自己的 git worktree 中运作
- 如果 subagent 未进行任何更改，worktree 会自动清理
- 如果存在更改，worktree 路径和分支名称会返回给主代理以供审查或合并

---

## 限制可生成的 Subagents

你可以通过在 `tools` 字段中使用 `Agent(agent_type)` 语法来控制给定 subagent 允许生成哪些 subagents。这提供了一种允许特定 subagents 进行委托的方法。

> **注意**：在 v2.1.63 中，`Task` 工具被重命名为 `Agent`。现有的 `Task(...)` 引用仍然作为别名工作。

### 示例

```yaml
---
name: coordinator
description: Coordinates work between specialized agents
tools: Agent(worker, researcher), Read, Bash
---

You are a coordinator agent. You can delegate work to the "worker" and
"researcher" subagents only. Use Read and Bash for your own exploration.
```

在此示例中，`coordinator` subagent 只能生成 `worker` 和 `researcher` subagents。它不能生成其他 subagent，即使它们在其他地方定义。

---

## `claude agents` CLI 命令

`claude agents` 命令列出按来源分组的所有已配置代理（内置、用户级、项目级）：

```bash
claude agents
```

此命令：
- 显示来自所有来源的所有可用代理
- 按其来源位置对代理进行分组
- 当较高优先级级别的代理遮蔽较低级别的代理时指示**覆盖**（例如，与用户级代理同名的项目级代理）

---

## 代理团队（实验性）

代理团队协调多个 Claude Code 实例共同处理复杂任务。与 subagents（被委托子任务并返回结果的子任务）不同，队友独立运作，拥有自己的上下文并通过共享邮箱系统直接通信。

> **注意**：代理团队是实验性的，需要 Claude Code v2.1.32+。使用前请启用。

### Subagents vs 代理团队

| 方面 | Subagents | 代理团队 |
|--------|-----------|-------------|
| **委托模型** | 父级委托子任务，等待结果 | 团队负责人分配工作，队友独立执行 |
| **上下文** | 每个子任务的新鲜上下文，结果被提炼回来 | 每个队友维护自己的持久上下文 |
| **协调** | 由父级管理的顺序或并行 | 具有自动依赖管理的共享任务列表 |
| **通信** | 仅返回值 | 通过邮箱的代理间消息 |
| **会话恢复** | 支持 | 不支持进程内队友 |
| **最适合** | 集中的、定义明确的子任务 | 需要并行工作的大型多文件项目 |

### 启用代理团队

设置环境变量或将其添加到你的 `settings.json`：

```bash
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

或在 `settings.json` 中：

```json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

### 启动团队

启用后，在提示中要求 Claude 与队友合作：

```
User: Build the authentication module. Use a team — one teammate for the API endpoints,
      one for the database schema, and one for the test suite.
```

Claude 将创建团队、分配任务并自动协调工作。

### 显示模式

控制队友活动的显示方式：

| 模式 | 标志 | 描述 |
|------|------|----------|
| **自动** | `--teammate-mode auto` | 自动为你的终端选择最佳显示模式 |
| **进程内** | `--teammate-mode in-process` | 在当前终端中内联显示队友输出（默认） |
| **分窗格** | `--teammate-mode tmux` | 在单独的 tmux 或 iTerm2 窗格中打开每个队友 |

```bash
claude --teammate-mode tmux
```

你也可以在 `settings.json` 中设置显示模式：

```json
{
  "teammateMode": "tmux"
}
```

> **注意**：分窗格模式需要 tmux 或 iTerm2。在 VS Code 终端、Windows Terminal 或 Ghostty 中不可用。

### 导航

在分窗格模式下使用 `Shift+Down` 在队友之间导航。

### 团队配置

团队配置存储在 `~/.claude/teams/{team-name}/config.json`。

### 架构

**关键组件**：

- **团队负责人**：创建团队、分配任务和协调的主 Claude Code 会话
- **共享任务列表**：具有自动依赖跟踪的同步任务列表
- **邮箱**：队友用于通信状态和协调的代理间消息系统
- **队友**：独立的 Claude Code 实例，每个都有自己的上下文窗口

### 任务分配和消息传递

团队负责人将工作分解为任务并分配给队友。共享任务列表处理：

- **自动依赖管理** — 任务等待其依赖完成
- **状态跟踪** — 队友在工作时有更新任务状态
- **代理间消息** — 队友通过邮箱发送消息进行协调（例如，"数据库 schema 已就绪，你可以开始编写查询"）

### 计划批准工作流

对于复杂任务，团队负责人在队友开始工作之前创建执行计划。用户审查并批准计划，确保团队的方法在有任何代码更改之前与期望一致。

### 团队钩子事件

代理团队引入两个额外的 [钩子事件](../06-hooks/)：

| 事件 | 触发时机 | 用例 |
|-------|-----------|----------|
| `TeammateIdle` | 队友完成当前任务且没有待处理工作时 | 触发通知、分配后续任务 |
| `TaskCompleted` | 共享任务列表中的任务被标记为完成 | 运行验证、更新仪表板、链式依赖工作 |

### 最佳实践

- **团队规模**：保持 3-5 个队友以获得最佳协调
- **任务大小**：将工作分解为每个 5-15 分钟的任务——足够小以并行化，足够大以有意义
- **避免文件冲突**：为不同队友分配不同的文件或目录以防止合并冲突
- **从简单开始**：对于你的第一个团队使用进程内模式；一旦熟悉了就切换到分窗格
- **清晰的任务描述**：提供具体的、可操作的任务描述，以便队友可以独立工作

### 限制

- **实验性**：功能行为可能在未来版本中更改
- **无会话恢复**：进程内队友在会话结束后无法恢复
- **每个会话一个团队**：无法在单个会话中创建嵌套团队或多个团队
- **固定领导**：团队负责人角色无法转移给队友
- **分窗格限制**：需要 tmux/iTerm2；VS Code 终端、Windows Terminal 或 Ghostty 不可用
- **无跨会话团队**：队友仅在当前会话内存在

> **警告**：代理团队是实验性的。首先使用非关键工作进行测试，并监控队友协调以发现意外行为。

---

## 插件 Subagent 安全

插件提供的 subagents 具有受限的前置元数据功能以保证安全。以下字段在插件 subagent 定义中**不允许**：

- `hooks` - 不能定义生命周期钩子
- `mcpServers` - 不能配置 MCP 服务器
- `permissionMode` - 不能覆盖权限设置

这可以防止插件通过 subagent 钩子升级权限或执行任意命令。

---

## 架构

### 高层架构

### 子代理生命周期

---

## 上下文管理

### 关键点

- 每个 subagent 获得一个**新的上下文窗口**，没有主对话历史
- 只有**相关上下文**被传递给 subagent 的特定任务
- 结果被**提炼**回主代理
- 这可以防止长项目上的**上下文 token 耗尽**

### 性能考虑

- **上下文效率** - 代理保留主上下文，实现更长的会话
- **延迟** - Subagents 以干净状态启动，收集初始上下文时可能增加延迟

### 关键行为

- **无嵌套生成** - Subagents 不能生成其他 subagents
- **后台权限** - 后台 subagents 自动拒绝任何未预先批准的权限
- **后台化** - 按 `Ctrl+B` 将当前运行的任务放到后台
- **转录** - Subagent 转录存储在 `~/.claude/projects/{project}/{sessionId}/subagents/agent-{agentId}.jsonl`
- **自动压缩** - Subagent 上下文在约 95% 容量时自动压缩（使用 `CLAUDE_AUTOPCACT_PCT_OVERRIDE` 环境变量覆盖）

---

## 何时使用 Subagents

| 场景 | 使用 Subagent | 为什么 |
|----------|--------------|-----|
| 具有多个步骤的复杂功能 | 是 | 分离关注点，防止上下文污染 |
| 快速代码审查 | 否 | 不必要的开销 |
| 并行任务执行 | 是 | 每个 subagent 有自己的上下文 |
| 需要专业 expertise | 是 | 自定义系统提示 |
| 长期分析 | 是 | 防止主上下文耗尽 |
| 单个任务 | 否 | 不必要地增加延迟 |

---

## 最佳实践

### 设计原则

**应该做：**
- 从 Claude 生成的代理开始 - 用 Claude 生成初始 subagent，然后迭代定制
- 设计聚焦的 subagents - 单一、清晰的职责而非一个做所有事
- 编写详细提示 - 包含特定指令、示例和约束
- 限制工具访问 - 仅授予 subagent 目的所需的必要工具
- 版本控制 - 将项目 subagents 检入版本控制以便团队协作

**不应该做：**
- 创建具有相同角色的重叠 subagents
- 给 subagents 不必要的工具访问
- 对简单的单步任务使用 subagents
- 在一个 subagent 的提示中混合关注点
- 忘记传递必要的上下文

### 系统提示最佳实践

1. **对角色具体化**
   ```
   You are an expert code reviewer specializing in [specific areas]
   ```

2. **明确优先事项**
   ```
   Review priorities (in order):
   1. Security Issues
   2. Performance Problems
   3. Code Quality
   ```

3. **指定输出格式**
   ```
   For each issue provide: Severity, Category, Location, Description, Fix, Impact
   ```

4. **包含操作步骤**
   ```
   When invoked:
   1. Run git diff to see recent changes
   2. Focus on modified files
   3. Begin review immediately
   ```

### 工具访问策略

1. **从限制性开始**：从仅基本工具开始
2. **仅在需要时扩展**：根据需求添加工具
3. **尽可能只读**：对分析代理使用 Read/Grep
4. **沙箱执行**：将 Bash 命令限制为特定模式

---

## 此文件夹中的示例 Subagents

此文件夹包含可立即使用的示例 subagents：

### 1. Code Reviewer (`code-reviewer.md`)

**目的**：全面的代码质量和可维护性分析

**工具**：Read、Grep、Glob、Bash

**专业领域**：
- 安全漏洞检测
- 性能优化识别
- 代码可维护性评估
- 测试覆盖率分析

**何时使用**：你需要专注于质量和安全性的自动化代码审查时

---

### 2. Test Engineer (`test-engineer.md`)

**目的**：测试策略、覆盖率分析和自动化测试

**工具**：Read、Write、Bash、Grep

**专业领域**：
- 单元测试创建
- 集成测试设计
- 边界情况识别
- 覆盖率分析（>80% 目标）

**何时使用**：你需要全面的测试套件创建或覆盖率分析时

---

### 3. Documentation Writer (`documentation-writer.md`)

**目的**：技术文档、API 文档和用户指南

**工具**：Read、Write、Grep

**专业领域**：
- API 端点文档
- 用户指南创建
- 架构文档
- 代码注释改进

**何时使用**：你需要创建或更新项目文档时

---

### 4. Secure Reviewer (`secure-reviewer.md`)

**目的**：以最少权限进行以安全为重点的代码审查

**工具**：Read、Grep

**专业领域**：
- 安全漏洞检测
- 认证/授权问题
- 数据暴露风险
- 注入攻击识别

**何时使用**：你需要安全审计而无需修改能力时

---

### 5. Implementation Agent (`implementation-agent.md`)

**目的**：功能开发的全栈实现专家

**工具**：Read、Write、Edit、Bash、Grep、Glob

**专业领域**：
- 功能实现
- 代码生成
- 构建和测试执行
- 代码库修改

**何时使用**：你需要 subagent 端到端实现功能时

---

### 6. Debugger (`debugger.md`)

**目的**：错误、测试失败和意外行为的调试专家

**工具**：Read、Edit、Bash、Grep、Glob

**专业领域**：
- 根本原因分析
- 错误调查
- 测试失败解决方案
- 最小修复实现

**何时使用**：你遇到 bug、错误或意外行为时

---

### 7. Data Scientist (`data-scientist.md`)

**目的**：SQL 查询和数据分析的数据分析专家

**工具**：Bash、Read、Write

**专业领域**：
- SQL 查询优化
- BigQuery 操作
- 数据分析和可视化
- 统计见解

**何时使用**：你需要数据分析、SQL 查询或 BigQuery 操作时

---

## 安装说明

### 方法 1：使用 /agents 命令（推荐）

```bash
/agents
```

然后：
1. 选择"Create New Agent"
2. 选择项目级或用户级
3. 详细描述你的 subagent
4. 选择要授予访问权限的工具（或留空以继承全部）
5. 保存并使用

### 方法 2：复制到项目

将代理文件复制到项目的 `.claude/agents/` 目录：

```bash
# 导航到你的项目
cd /path/to/your/project

# 如果 agents 目录不存在则创建
mkdir -p .claude/agents

# 从此文件夹复制所有代理文件
cp /path/to/04-subagents/*.md .claude/agents/

# 删除 README（.claude/agents 中不需要）
rm .claude/agents/README.md
```

### 方法 3：复制到用户目录

对于在你所有项目中都可用的代理：

```bash
# 创建用户代理目录
mkdir -p ~/.claude/agents

# 复制代理
cp /path/to/04-subagents/code-reviewer.md ~/.claude/agents/
cp /path/to/04-subagents/debugger.md ~/.claude/agents/
# ... 根据需要复制其他
```

### 验证

安装后，验证代理已被识别：

```bash
/agents
```

你应该看到你安装的代理与内置代理一起列出。

---

## 文件结构

```
project/
├── .claude/
│   └── agents/
│       ├── code-reviewer.md
│       ├── test-engineer.md
│       ├── documentation-writer.md
│       ├── secure-reviewer.md
│       ├── implementation-agent.md
│       ├── debugger.md
│       └── data-scientist.md
└── ...
```

---

## 相关概念

### 相关功能

- **[斜杠命令](../01-slash-commands/)** - 用户发起的快速快捷方式
- **[内存](../02-memory/)** - 跨会话持久上下文
- **[Skills](../03-skills/)** - 可复用的自主能力
- **[MCP 协议](../05-mcp/)** - 实时外部数据访问
- **[Hooks](../06-hooks/)** - 事件驱动的 shell 命令自动化
- **[插件](../07-plugins/)** - 捆绑的扩展包

### 与其他功能的对比

| 功能 | 用户调用 | 自动调用 | 持久 | 外部访问 | 隔离上下文 |
|---------|--------------|--------------|-----------|------------------|------------------|
| **斜杠命令** | 是 | 否 | 否 | 否 | 否 |
| **Subagents** | 是 | 是 | 否 | 否 | 是 |
| **内存** | 自动 | 自动 | 是 | 否 | 否 |
| **MCP** | 自动 | 是 | 否 | 是 | 否 |
| **Skills** | 是 | 是 | 否 | 否 | 否 |

---

## 额外资源

- [官方 Subagents 文档](https://code.claude.com/docs/en/sub-agents)
- [CLI 参考](https://code.claude.com/docs/en/cli-reference) - `--agents` 标志和其他 CLI 选项
- [插件指南](../07-plugins/) - 用于捆绑代理和其他功能
- [Skills 指南](../03-skills/) - 用于自动调用的能力
- [内存指南](../02-memory/) - 用于持久上下文
- [Hooks 指南](../06-hooks/) - 用于事件驱动的自动化

---

*最后更新：2026 年 3 月*

*本指南涵盖 Claude Code 的完整 subagent 配置、委托模式和最佳实践。*
