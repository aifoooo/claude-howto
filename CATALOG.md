<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 功能目录

> Claude Code 所有功能的快速参考指南：命令、代理、技能、插件和钩子。

**导航**: [命令](#斜杠命令) | [权限模式](#权限模式) | [子代理](#子代理) | [技能](#技能) | [插件](#插件) | [MCP 服务器](#mcp-服务器) | [钩子](#钩子) | [记忆](#记忆文件) | [新功能](#新功能-2026年3月)

---

## 摘要

| 功能 | 内置 | 示例 | 总计 | 参考 |
|---------|----------|----------|-------|-----------|
| **斜杠命令** | 55+ | 8 | 63+ | [01-slash-commands/](01-slash-commands/) |
| **子代理** | 6 | 10 | 16 | [04-subagents/](04-subagents/) |
| **技能** | 5 个捆绑 | 4 | 9 | [03-skills/](03-skills/) |
| **插件** | - | 3 | 3 | [07-plugins/](07-plugins/) |
| **MCP 服务器** | 1 | 8 | 9 | [05-mcp/](05-mcp/) |
| **钩子** | 25 个事件 | 7 | 7 | [06-hooks/](06-hooks/) |
| **记忆** | 7 种类型 | 3 | 3 | [02-memory/](02-memory/) |
| **总计** | **99** | **43** | **117** | |

---

## 斜杠命令

命令是用户调用的快捷方式，执行特定操作。

### 内置命令

| 命令 | 描述 | 使用时机 |
|---------|-------------|-------------|
| `/help` | 显示帮助信息 | 入门、学习命令 |
| `/btw` | 侧问，不增加上下文 | 快速附带问题 |
| `/chrome` | 配置 Chrome 集成 | 浏览器自动化 |
| `/clear` | 清除对话历史 | 重新开始、减少上下文 |
| `/diff` | 交互式 diff 查看器 | 审查更改 |
| `/config` | 查看/编辑配置 | 自定义行为 |
| `/status` | 显示会话状态 | 检查当前状态 |
| `/agents` | 列出可用代理 | 查看委托选项 |
| `/skills` | 列出可用技能 | 查看自动调用能力 |
| `/hooks` | 列出配置的钩子 | 调试自动化 |
| `/insights` | 分析会话模式 | 会话优化 |
| `/install-slack-app` | 安装 Claude Slack 应用 | Slack 集成 |
| `/keybindings` | 自定义键盘快捷键 | 键位自定义 |
| `/mcp` | 列出 MCP 服务器 | 检查外部集成 |
| `/memory` | 查看已加载的记忆文件 | 调试上下文加载 |
| `/mobile` | 生成移动端二维码 | 移动访问 |
| `/passes` | 查看使用次数 | 订阅信息 |
| `/plugin` | 管理插件 | 安装/删除扩展 |
| `/plan` | 进入规划模式 | 复杂实现 |
| `/rewind` | 回退到检查点 | 撤销更改、探索替代方案 |
| `/checkpoint` | 管理检查点 | 保存/恢复状态 |
| `/cost` | 显示 token 使用成本 | 监控支出 |
| `/context` | 显示上下文窗口使用情况 | 管理对话长度 |
| `/export` | 导出对话 | 保存以供参考 |
| `/extra-usage` | 配置额外使用限制 | 速率限制管理 |
| `/feedback` | 提交反馈或错误报告 | 报告问题 |
| `/login` | 通过 Anthropic 认证 | 访问功能 |
| `/logout` | 登出 | 切换账户 |
| `/sandbox` | 切换沙盒模式 | 安全命令执行 |
| `/vim` | 切换 vim 模式 | Vim 风格编辑 |
| `/doctor` | 运行诊断 | 排查问题 |
| `/reload-plugins` | 重新加载已安装的插件 | 插件管理 |
| `/release-notes` | 显示发布说明 | 查看新功能 |
| `/remote-control` | 启用远程控制 | 远程访问 |
| `/permissions` | 管理权限 | 控制访问 |
| `/session` | 管理会话 | 多会话工作流 |
| `/rename` | 重命名当前会话 | 整理会话 |
| `/resume` | 恢复上一个会话 | 继续工作 |
| `/todo` | 查看/管理待办列表 | 跟踪任务 |
| `/tasks` | 查看后台任务 | 监控异步操作 |
| `/copy` | 复制上一个响应到剪贴板 | 快速分享输出 |
| `/teleport` | 将会话转移到另一台机器 | 远程继续工作 |
| `/desktop` | 打开 Claude 桌面应用 | 切换到桌面界面 |
| `/theme` | 更改颜色主题 | 自定义外观 |
| `/usage` | 显示 API 使用统计 | 监控配额和成本 |
| `/fork` | 分叉当前对话 | 探索替代方案 |
| `/stats` | 显示会话统计 | 审查会话指标 |
| `/statusline` | 配置状态栏 | 自定义状态显示 |
| `/stickers` | 查看会话贴纸 | 趣味奖励 |
| `/fast` | 切换快速输出模式 | 加快响应 |
| `/terminal-setup` | 配置终端集成 | 设置终端功能 |
| `/upgrade` | 检查更新 | 版本管理 |

### 自定义命令（示例）

| 命令 | 描述 | 使用时机 | 范围 | 安装 |
|---------|-------------|-------------|-------|--------------|
| `/optimize` | 分析代码优化 | 性能改进 | 项目 | `cp 01-slash-commands/optimize.md .claude/commands/` |
| `/pr` | 准备 Pull Request | 提交 PR 前 | 项目 | `cp 01-slash-commands/pr.md .claude/commands/` |
| `/generate-api-docs` | 生成 API 文档 | 文档 API | 项目 | `cp 01-slash-commands/generate-api-docs.md .claude/commands/` |
| `/commit` | 创建带上下文的 git 提交 | 提交更改 | 用户 | `cp 01-slash-commands/commit.md .claude/commands/` |
| `/push-all` | 暂存、提交并推送 | 快速部署 | 用户 | `cp 01-slash-commands/push-all.md .claude/commands/` |
| `/doc-refactor` | 重构文档结构 | 改进文档 | 项目 | `cp 01-slash-commands/doc-refactor.md .claude/commands/` |
| `/setup-ci-cd` | 设置 CI/CD 流水线 | 新项目 | 项目 | `cp 01-slash-commands/setup-ci-cd.md .claude/commands/` |
| `/unit-test-expand` | 扩展测试覆盖率 | 改进测试 | 项目 | `cp 01-slash-commands/unit-test-expand.md .claude/commands/` |

> **范围**: `用户` = 个人工作流（`~/.claude/commands/`）, `项目` = 团队共享（`.claude/commands/`）

**参考**: [01-slash-commands/](01-slash-commands/) | [官方文档](https://code.claude.com/docs/en/interactive-mode)

**快速安装（所有自定义命令）**:
```bash
cp 01-slash-commands/*.md .claude/commands/
```

---

## 权限模式

Claude Code 支持 6 种权限模式，控制工具调用的授权方式。

| 模式 | 描述 | 使用时机 |
|------|-------------|-------------|
| `default` | 每个工具调用都提示 | 标准交互使用 |
| `acceptEdits` | 自动接受文件编辑，其他提示 | 信任的编辑工作流 |
| `plan` | 仅读取工具，无写入 | 规划和探索 |
| `auto` | 自动接受所有工具，无提示 | 完全自主操作（研究预览版） |
| `bypassPermissions` | 跳过所有权限检查 | CI/CD、无头环境 |
| `dontAsk` | 跳过需要权限的工具 | 非交互式脚本 |

> **注意**: `auto` 模式是研究预览功能（2026年3月）。仅在可信的沙盒环境中使用 `bypassPermissions`。

**参考**: [官方文档](https://code.claude.com/docs/en/permissions)

---

## 子代理

用于特定任务的、具有隔离上下文的专用 AI 助手。

### 内置子代理

| 代理 | 描述 | 工具 | 模型 | 使用时机 |
|-------|-------------|-------|-------|-------------|
| **general-purpose** | 多步骤任务、研究 | 所有工具 | 继承模型 | 复杂研究、多文件任务 |
| **Plan** | 实现规划 | 读取、Glob、Grep、Bash | 继承模型 | 架构设计、规划 |
| **Explore** | 代码库探索 | 读取、Glob、Grep | Haiku 4.5 | 快速搜索、理解代码 |
| **Bash** | 命令执行 | Bash | 继承模型 | Git 操作、终端任务 |
| **statusline-setup** | 状态栏配置 | Bash、读取、写入 | Sonnet 4.6 | 配置状态栏显示 |
| **Claude Code Guide** | 帮助和文档 | 读取、Glob、Grep | Haiku 4.5 | 获取帮助、学习功能 |

### 子代理配置字段

| 字段 | 类型 | 描述 |
|-------|------|-------------|
| `name` | string | 代理标识符 |
| `description` | string | 代理的功能 |
| `model` | string | 模型覆盖（如 `haiku-4.5`） |
| `tools` | array | 允许的工具列表 |
| `effort` | string | 推理努力级别（`low`、`medium`、`high`） |
| `initialPrompt` | string | 代理启动时注入的系统提示 |
| `disallowedTools` | array | 明确拒绝该代理使用的工具 |

### 自定义子代理（示例）

| 代理 | 描述 | 使用时机 | 范围 | 安装 |
|-------|-------------|-------------|-------|--------------|
| `code-reviewer` | 全面的代码质量审查 | 代码审查会话 | 项目 | `cp 04-subagents/code-reviewer.md .claude/agents/` |
| `code-architect` | 功能架构设计 | 新功能规划 | 项目 | `cp 04-subagents/code-architect.md .claude/agents/` |
| `code-explorer` | 深度代码库分析 | 理解现有功能 | 项目 | `cp 04-subagents/code-explorer.md .claude/agents/` |
| `clean-code-reviewer` | 整洁代码原则审查 | 可维护性审查 | 项目 | `cp 04-subagents/clean-code-reviewer.md .claude/agents/` |
| `test-engineer` | 测试策略和覆盖率 | 测试规划 | 项目 | `cp 04-subagents/test-engineer.md .claude/agents/` |
| `documentation-writer` | 技术文档 | API 文档、指南 | 项目 | `cp 04-subagents/documentation-writer.md .claude/agents/` |
| `secure-reviewer` | 安全重点审查 | 安全审计 | 项目 | `cp 04-subagents/secure-reviewer.md .claude/agents/` |
| `implementation-agent` | 完整功能实现 | 功能开发 | 项目 | `cp 04-subagents/implementation-agent.md .claude/agents/` |
| `debugger` | 根本原因分析 | Bug 调查 | 用户 | `cp 04-subagents/debugger.md .claude/agents/` |
| `data-scientist` | SQL 查询、数据分析 | 数据任务 | 用户 | `cp 04-subagents/data-scientist.md .claude/agents/` |

> **范围**: `用户` = 个人（`~/.claude/agents/`）, `项目` = 团队共享（`.claude/agents/`）

**参考**: [04-subagents/](04-subagents/) | [官方文档](https://code.claude.com/docs/en/sub-agents)

**快速安装（所有自定义代理）**:
```bash
cp 04-subagents/*.md .claude/agents/
```

---

## 技能

具有指令、脚本和模板的自动调用能力。

### 示例技能

| 技能 | 描述 | 自动调用时机 | 范围 | 安装 |
|-------|-------------|-------------------|-------|--------------|
| `code-review` | 全面的代码审查 | "审查这段代码"、"检查质量" | 项目 | `cp -r 03-skills/code-review .claude/skills/` |
| `brand-voice` | 品牌一致性检查器 | 编写营销文案 | 项目 | `cp -r 03-skills/brand-voice .claude/skills/` |
| `doc-generator` | API 文档生成器 | "生成文档"、"API 文档" | 项目 | `cp -r 03-skills/doc-generator .claude/skills/` |
| `refactor` | 系统化代码重构（Martin Fowler） | "重构这个"、"清理代码" | 用户 | `cp -r 03-skills/refactor ~/.claude/skills/` |

> **范围**: `用户` = 个人（`~/.claude/skills/`）, `项目` = 团队共享（`.claude/skills/`）

### 技能结构

```
~/.claude/skills/skill-name/
├── SKILL.md          # 技能定义和指令
├── scripts/          # 辅助脚本
└── templates/        # 输出模板
```

### 技能 Frontmatter 字段

技能在 `SKILL.md` 中支持 YAML frontmatter 配置：

| 字段 | 类型 | 描述 |
|-------|------|-------------|
| `name` | string | 技能显示名称 |
| `description` | string | 技能的功能 |
| `autoInvoke` | array | 自动调用触发短语 |
| `effort` | string | 推理努力级别（`low`、`medium`、`high`） |
| `shell` | string | 脚本使用的 shell（`bash`、`zsh`、`sh`） |

**参考**: [03-skills/](03-skills/) | [官方文档](https://code.claude.com/docs/en/skills)

**快速安装（所有技能）**:
```bash
cp -r 03-skills/* ~/.claude/skills/
```

### 捆绑技能

| 技能 | 描述 | 自动调用时机 |
|-------|-------------|-------------------|
| `/simplify` | 代码质量审查 | 编写代码后 |
| `/batch` | 对多个文件运行提示 | 批量操作 |
| `/debug` | 调试失败的测试/错误 | 调试会话 |
| `/loop` | 定期运行提示 | 重复任务 |
| `/claude-api` | 使用 Claude API 构建应用 | API 开发 |

---

## 插件

将命令、代理、MCP 服务器和钩子打包的集合。

### 示例插件

| 插件 | 描述 | 组件 | 使用时机 | 范围 | 安装 |
|--------|-------------|------------|-------------|-------|--------------|
| `pr-review` | PR 审查工作流 | 3 个命令、3 个代理、GitHub MCP | 代码审查 | 项目 | `/plugin install pr-review` |
| `devops-automation` | 部署和监控 | 4 个命令、3 个代理、K8s MCP | DevOps 任务 | 项目 | `/plugin install devops-automation` |
| `documentation` | 文档生成套件 | 4 个命令、3 个代理、模板 | 文档 | 项目 | `/plugin install documentation` |

> **范围**: `项目` = 团队共享, `用户` = 个人工作流

### 插件结构

```
.claude-plugin/
├── plugin.json       # 清单文件
├── commands/         # 斜杠命令
├── agents/           # 子代理
├── skills/           # 技能
├── mcp/              # MCP 配置
├── hooks/            # 钩子脚本
└── scripts/          # 工具脚本
```

**参考**: [07-plugins/](07-plugins/) | [官方文档](https://code.claude.com/docs/en/plugins)

**插件管理命令**:
```bash
/plugin list              # 列出已安装的插件
/plugin install <name>    # 安装插件
/plugin remove <name>     # 移除插件
/plugin update <name>     # 更新插件
```

---

## MCP 服务器

用于外部工具和 API 访问的 Model Context Protocol 服务器。

### 常用 MCP 服务器

| 服务器 | 描述 | 使用时机 | 范围 | 安装 |
|--------|-------------|-------------|-------|--------------|
| **GitHub** | PR 管理、issues、代码 | GitHub 工作流 | 项目 | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| **Database** | SQL 查询、数据访问 | 数据库操作 | 项目 | `claude mcp add db -- npx -y @modelcontextprotocol/server-postgres` |
| **Filesystem** | 高级文件操作 | 复杂文件任务 | 用户 | `claude mcp add fs -- npx -y @modelcontextprotocol/server-filesystem` |
| **Slack** | 团队沟通 | 通知、更新 | 项目 | 在设置中配置 |
| **Google Docs** | 文档访问 | 文档编辑、审查 | 项目 | 在设置中配置 |
| **Asana** | 项目管理 | 任务跟踪 | 项目 | 在设置中配置 |
| **Stripe** | 支付数据 | 财务分析 | 项目 | 在设置中配置 |
| **Memory** | 持久化记忆 | 跨会话记忆 | 用户 | 在设置中配置 |
| **Context7** | 库文档 | 最新文档查找 | 内置 | 内置 |

> **范围**: `项目` = 团队（`.mcp.json`）, `用户` = 个人（`~/.claude.json`）, `内置` = 预装

### MCP 配置示例

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**参考**: [05-mcp/](05-mcp/) | [MCP 协议文档](https://modelcontextprotocol.io)

**快速安装（GitHub MCP）**:
```bash
export GITHUB_TOKEN="your_token" && claude mcp add github -- npx -y @modelcontextprotocol/server-github
```

---

## 钩子

事件驱动的自动化，在 Claude Code 事件上执行 shell 命令。

### 钩子事件

| 事件 | 描述 | 触发时机 | 使用场景 |
|-------|-------------|----------------|-----------|
| `SessionStart` | 会话开始/恢复 | 会话初始化 | 设置任务 |
| `InstructionsLoaded` | 指令已加载 | CLAUDE.md 或规则文件加载 | 自定义指令处理 |
| `UserPromptSubmit` | 处理提示前 | 用户发送消息 | 输入验证 |
| `PreToolUse` | 工具执行前 | 任何工具运行前 | 验证、日志 |
| `PermissionRequest` | 显示权限对话框 | 敏感操作前 | 自定义批准流程 |
| `PostToolUse` | 工具成功后 | 任何工具完成后 | 格式化、通知 |
| `PostToolUseFailure` | 工具执行失败 | 工具错误后 | 错误处理、日志 |
| `Notification` | 发送通知 | Claude 发送通知 | 外部警报 |
| `SubagentStart` | 启动子代理 | 子代理任务开始 | 初始化子代理上下文 |
| `SubagentStop` | 子代理结束 | 子代理任务完成 | 链式操作 |
| `Stop` | Claude 完成响应 | 响应完成 | 清理、报告 |
| `StopFailure` | API 错误结束回合 | 发生 API 错误 | 错误恢复、日志 |
| `TeammateIdle` | 队友代理空闲 | 代理团队协调 | 分配工作 |
| `TaskCompleted` | 任务标记完成 | 任务完成 | 任务后处理 |
| `TaskCreated` | 通过 TaskCreate 创建任务 | 创建新任务 | 任务跟踪、日志 |
| `ConfigChange` | 配置已更新 | 设置被修改 | 响应配置更改 |
| `CwdChanged` | 工作目录更改 | 目录更改 | 目录特定设置 |
| `FileChanged` | 监视的文件更改 | 文件被修改 | 文件监视、重建 |
| `PreCompact` | 压缩操作前 | 上下文压缩 | 状态保存 |
| `PostCompact` | 压缩完成后 | 压缩完成 | 压缩后操作 |
| `WorktreeCreate` | 正在创建 worktree | Git worktree 创建 | 设置 worktree 环境 |
| `WorktreeRemove` | 正在移除 worktree | Git worktree 移除 | 清理 worktree 资源 |
| `Elicitation` | MCP 服务器请求输入 | MCP 征求 | 输入验证 |
| `ElicitationResult` | 用户响应征求 | 用户响应 | 响应处理 |
| `SessionEnd` | 会话终止 | 会话终止 | 清理、保存状态 |

### 示例钩子

| 钩子 | 描述 | 事件 | 范围 | 安装 |
|------|-------------|-------|-------|--------------|
| `validate-bash.py` | 命令验证 | PreToolUse:Bash | 项目 | `cp 06-hooks/validate-bash.py .claude/hooks/` |
| `security-scan.py` | 安全扫描 | PostToolUse:Write | 项目 | `cp 06-hooks/security-scan.py .claude/hooks/` |
| `format-code.sh` | 自动格式化 | PostToolUse:Write | 用户 | `cp 06-hooks/format-code.sh ~/.claude/hooks/` |
| `validate-prompt.py` | 提示验证 | UserPromptSubmit | 项目 | `cp 06-hooks/validate-prompt.py .claude/hooks/` |
| `context-tracker.py` | Token 使用跟踪 | Stop | 用户 | `cp 06-hooks/context-tracker.py ~/.claude/hooks/` |
| `pre-commit.sh` | 预提交验证 | PreToolUse:Bash | 项目 | `cp 06-hooks/pre-commit.sh .claude/hooks/` |
| `log-bash.sh` | 命令日志 | PostToolUse:Bash | 用户 | `cp 06-hooks/log-bash.sh ~/.claude/hooks/` |

> **范围**: `项目` = 团队（`.claude/settings.json`）, `用户` = 个人（`~/.claude/settings.json`）

### 钩子配置

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "command": "~/.claude/hooks/validate-bash.py"
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write",
        "command": "~/.claude/hooks/format-code.sh"
      }
    ]
  }
}
```

**参考**: [06-hooks/](06-hooks/) | [官方文档](https://code.claude.com/docs/en/hooks)

**快速安装（所有钩子）**:
```bash
mkdir -p ~/.claude/hooks && cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh
```

---

## 记忆文件

跨会话自动加载的持久化上下文。

### 记忆类型

| 类型 | 位置 | 范围 | 使用时机 |
|------|----------|-------|-------------|
| **托管策略** | 组织托管的策略 | 组织 | 强制执行组织范围的标准 |
| **项目** | `./CLAUDE.md` | 项目（团队） | 团队标准、项目上下文 |
| **项目规则** | `.claude/rules/` | 项目（团队） | 模块化项目规则 |
| **用户** | `~/.claude/CLAUDE.md` | 用户（个人） | 个人偏好 |
| **用户规则** | `~/.claude/rules/` | 用户（个人） | 模块化个人规则 |
| **本地** | `./CLAUDE.local.md` | 本地（git 忽略） | 机器特定覆盖（截至 2026 年 3 月未在官方文档中；可能是遗留） |
| **自动记忆** | 自动 | 会话 | 自动捕获的洞察和修正 |

> **范围**: `组织` = 管理员管理, `项目` = 通过 git 与团队共享, `用户` = 个人偏好, `本地` = 不提交, `会话` = 自动管理

**参考**: [02-memory/](02-memory/) | [官方文档](https://code.claude.com/docs/en/memory)

**快速安装**:
```bash
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

---

## 新功能（2026 年 3 月）

| 功能 | 描述 | 如何使用 |
|---------|-------------|------------|
| **远程控制** | 通过 API 远程控制 Claude Code 会话 | 使用远程控制 API 以编程方式发送提示并接收响应 |
| **Web 会话** | 在基于浏览器的环境中运行 Claude Code | 通过 `claude web` 或 Anthropic Console 访问 |
| **桌面应用** | Claude Code 原生桌面应用 | 使用 `/desktop` 或从 Anthropic 网站下载 |
| **代理团队** | 协调多个代理处理相关任务 | 配置协作和共享上下文的队友代理 |
| **任务列表** | 后台任务管理和监控 | 使用 `/tasks` 查看和管理后台操作 |
| **提示建议** | 上下文感知的命令建议 | 基于当前上下文自动出现建议 |
| **Git Worktrees** | 用于并行开发的隔离 git worktree | 使用 worktree 命令进行安全的并行分支工作 |
| **沙盒化** | 用于安全的隔离执行环境 | 使用 `/sandbox` 切换；在受限环境中运行命令 |
| **MCP OAuth** | MCP 服务器的 OAuth 认证 | 在 MCP 服务器设置中配置 OAuth 凭据以实现安全访问 |
| **MCP 工具搜索** | 动态搜索和发现 MCP 工具 | 使用工具搜索查找跨连接服务器可用的 MCP 工具 |
| **计划任务** | 使用 `/loop` 和 cron 工具设置重复任务 | 使用 `/loop 5m /command` 或 CronCreate 工具 |
| **Chrome 集成** | 使用无头 Chromium 的浏览器自动化 | 使用 `--chrome` 标志或 `/chrome` 命令 |
| **键盘自定义** | 自定义键位，包括和弦支持 | 使用 `/keybindings` 或编辑 `~/.claude/keybindings.json` |
| **自动模式** | 无需权限提示的完全自主操作（研究预览版） | 使用 `--mode auto` 或 `/permissions auto`；2026 年 3 月 |
| **渠道** | 多渠道通信（Telegram、Slack 等）（研究预览版） | 配置渠道插件；2026 年 3 月 |
| **语音听写** | 语音输入提示 | 使用麦克风图标或语音键位 |
| **代理钩子类型** | 生成子代理而非运行 shell 命令的钩子 | 在钩子配置中设置 `"type": "agent"` |
| **提示钩子类型** | 向对话注入提示文本的钩子 | 在钩子配置中设置 `"type": "prompt"` |
| **MCP 征求** | MCP 服务器可在工具执行期间请求用户输入 | 通过 `Elicitation` 和 `ElicitationResult` 钩子事件处理 |
| **WebSocket MCP 传输** | MCP 服务器连接的基于 WebSocket 的传输 | 在 MCP 服务器配置中使用 `"transport": "websocket"` |
| **插件 LSP 支持** | 通过插件集成语言服务器协议 | 在 `plugin.json` 中配置 LSP 服务器以实现编辑器功能 |
| **托管 Drop-ins** | 组织托管的 drop-in 配置（v2.1.83） | 管理员通过托管策略配置；自动应用到所有用户 |

---

## 快速参考矩阵

### 功能选择指南

| 需求 | 推荐功能 | 为什么 |
|------|---------------------|-----|
| 快速快捷方式 | 斜杠命令 | 手动、即时 |
| 持久上下文 | 记忆 | 自动加载 |
| 复杂自动化 | 技能 | 自动调用 |
| 专用任务 | 子代理 | 隔离上下文 |
| 外部数据 | MCP 服务器 | 实时访问 |
| 事件自动化 | 钩子 | 事件触发 |
| 完整解决方案 | 插件 | 一站式捆绑 |

### 安装优先级

| 优先级 | 功能 | 命令 |
|----------|---------|---------|
| 1. 必备 | 记忆 | `cp 02-memory/project-CLAUDE.md ./CLAUDE.md` |
| 2. 日常使用 | 斜杠命令 | `cp 01-slash-commands/*.md .claude/commands/` |
| 3. 质量 | 子代理 | `cp 04-subagents/*.md .claude/agents/` |
| 4. 自动化 | 钩子 | `cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh` |
| 5. 外部 | MCP | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| 6. 高级 | 技能 | `cp -r 03-skills/* ~/.claude/skills/` |
| 7. 完整 | 插件 | `/plugin install pr-review` |

---

## 一命令完整安装

安装此仓库中的所有示例：

```bash
# 创建目录
mkdir -p .claude/{commands,agents,skills} ~/.claude/{hooks,skills}

# 安装所有功能
cp 01-slash-commands/*.md .claude/commands/ && \
cp 02-memory/project-CLAUDE.md ./CLAUDE.md && \
cp -r 03-skills/* ~/.claude/skills/ && \
cp 04-subagents/*.md .claude/agents/ && \
cp 06-hooks/*.sh ~/.claude/hooks/ && \
chmod +x ~/.claude/hooks/*.sh
```

---

## 其他资源

- [Claude Code 官方文档](https://code.claude.com/docs/en/overview)
- [MCP 协议规范](https://modelcontextprotocol.io)
- [学习路线图](LEARNING-ROADMAP.md)
- [主 README](README.md)

---

**最后更新**: 2026 年 3 月
