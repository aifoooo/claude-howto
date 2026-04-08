<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 示例 - 快速参考卡

## 快速安装命令

### 斜杠命令
```bash
# 安装全部
cp 01-slash-commands/*.md .claude/commands/

# 安装特定命令
cp 01-slash-commands/optimize.md .claude/commands/
```

### 内存
```bash
# 项目内存
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 个人内存
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

### 技能
```bash
# 个人技能
cp -r 03-skills/code-review ~/.claude/skills/

# 项目技能
cp -r 03-skills/code-review .claude/skills/
```

### 子代理
```bash
# 安装全部
cp 04-subagents/*.md .claude/agents/

# 安装特定代理
cp 04-subagents/code-reviewer.md .claude/agents/
```

### MCP
```bash
# 设置凭据
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# 安装配置（项目范围）
cp 05-mcp/github-mcp.json .mcp.json

# 或用户范围：添加到 ~/.claude.json
```

### 钩子
```bash
# 安装钩子
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 在设置中配置（~/.claude/settings.json）
```

### 插件
```bash
# 从示例安装（如已发布）
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

### 检查点
```bash
# 检查点在每个用户提示时自动创建
# 要回滚，按两次 Esc 或使用：
/rewind

# 然后选择：恢复代码和对话、恢复对话、
# 恢复代码、从此处总结、或算了
```

### 高级功能
```bash
# 在设置中配置（.claude/settings.json）
# 参见 09-advanced-features/config-examples.json

# 规划模式
/plan Task description

# 权限模式（使用 --permission-mode 标志）
# default        - 对危险操作请求批准
# acceptEdits    - 自动接受文件编辑，其他则询问
# plan           - 只读分析，无修改
# dontAsk        - 接受除危险操作外的所有操作
# auto           - 后台分类器自动决定权限
# bypassPermissions - 接受所有操作（需要 --dangerously-skip-permissions）

# 会话管理
/resume                # 恢复之前的对话
/rename "name"         # 命名当前会话
/fork                  # 分叉当前会话
claude -c              # 继续最近的对话
claude -r "session"    # 按名称/ID 恢复会话
```

---

## 功能速查表

| 功能 | 安装路径 | 使用方法 |
|---------|-------------|-------|
| **斜杠命令（55+）** | `.claude/commands/*.md` | `/command-name` |
| **内存** | `./CLAUDE.md` | 自动加载 |
| **技能** | `.claude/skills/*/SKILL.md` | 自动调用 |
| **子代理** | `.claude/agents/*.md` | 自动委托 |
| **MCP** | `.mcp.json`（项目）或 `~/.claude.json`（用户） | `/mcp__server__action` |
| **钩子（25 个事件）** | `~/.claude/hooks/*.sh` | 事件触发（4 种类型）|
| **插件** | 通过 `/plugin install` | 捆绑全部 |
| **检查点** | 内置 | `Esc+Esc` 或 `/rewind` |
| **规划模式** | 内置 | `/plan <task>` |
| **权限模式（6 种）** | 内置 | `--allowedTools`、`--permission-mode` |
| **会话** | 内置 | `/session <command>` |
| **后台任务** | 内置 | 后台运行 |
| **远程控制** | 内置 | WebSocket API |
| **Web 会话** | 内置 | `claude web` |
| **Git Worktrees** | 内置 | `/worktree` |
| **Auto Memory** | 内置 | 自动保存到 CLAUDE.md |
| **任务列表** | 内置 | `/task list` |
| **捆绑技能（5 个）** | 内置 | `/simplify`、`/loop`、`/claude-api`、`/voice`、`/browse` |

---

## 常见使用场景

### 代码审查
```bash
# 方法 1：斜杠命令
cp 01-slash-commands/optimize.md .claude/commands/
# 使用：/optimize

# 方法 2：子代理
cp 04-subagents/code-reviewer.md .claude/agents/
# 使用：自动委托

# 方法 3：技能
cp -r 03-skills/code-review ~/.claude/skills/
# 使用：自动调用

# 方法 4：插件（最佳）
/plugin install pr-review
# 使用：/review-pr
```

### 文档
```bash
# 斜杠命令
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# 子代理
cp 04-subagents/documentation-writer.md .claude/agents/

# 技能
cp -r 03-skills/doc-generator ~/.claude/skills/

# 插件（完整解决方案）
/plugin install documentation
```

### DevOps
```bash
# 完整插件
/plugin install devops-automation

# 命令：/deploy、/rollback、/status、/incident
```

### 团队标准
```bash
# 项目内存
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 编辑以适配您的团队
vim CLAUDE.md
```

### 自动化和钩子
```bash
# 安装钩子（25 个事件，4 种类型：command、http、prompt、agent）
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 示例：
# - 预提交测试：pre-commit.sh
# - 自动格式化代码：format-code.sh
# - 安全扫描：security-scan.sh

# 用于完全自主工作流程的 Auto Mode
claude --enable-auto-mode -p "Refactor and test the auth module"
# 或使用 Shift+Tab 交互循环模式
```

### 安全重构
```bash
# 检查点在每个用户提示前自动创建
# 尝试重构
# 如果成功：继续
# 如果失败：按 Esc+Esc 或使用 /rewind 返回
```

### 复杂实现
```bash
# 使用规划模式
/plan Implement user authentication system

# Claude 创建详细计划
# 审查并批准
# Claude 系统化实现
```

### CI/CD 集成
```bash
# 以无头模式运行（非交互）
claude -p "Run all tests and generate report"

# 使用权限模式进行 CI
claude -p "Run tests" --permission-mode dontAsk

# 使用 Auto Mode 进行完全自主的 CI 任务
claude --enable-auto-mode -p "Run tests and fix failures"

# 使用钩子进行自动化
# 参见 09-advanced-features/README.md
```

### 学习和实验
```bash
# 使用规划模式进行安全分析
claude --permission-mode plan

# 安全实验 - 检查点自动创建
# 如果需要回滚：按 Esc+Esc 或使用 /rewind
```

### Agent Teams
```bash
# 启用 agent teams
export CLAUDE_AGENT_TEAMS=1

# 或在 settings.json 中
{ "agentTeams": { "enabled": true } }

# 开始时使用："使用团队方法实现功能 X"
```

### 计划任务
```bash
# 每 5 分钟运行一个命令
/loop 5m /check-status

# 一次性提醒
/loop 30m "提醒我检查部署"
```

---

## 文件位置参考

```
您的项目/
├── .claude/
│   ├── commands/              # 斜杠命令放在这里
│   ├── agents/                # 子代理放在这里
│   ├── skills/                # 项目技能放在这里
│   └── settings.json          # 项目设置（钩子等）
├── .mcp.json                  # MCP 配置（项目范围）
├── CLAUDE.md                  # 项目内存
└── src/
    └── api/
        └── CLAUDE.md          # 目录特定内存

用户主目录/
├── .claude/
│   ├── commands/              # 个人命令
│   ├── agents/                # 个人代理
│   ├── skills/                # 个人技能
│   ├── hooks/                 # 钩子脚本
│   ├── settings.json          # 用户设置
│   ├── managed-settings.d/    # 托管设置（企业/组织）
│   └── CLAUDE.md              # 个人内存
└── .claude.json               # 个人 MCP 配置（用户范围）
```

---

## 查找示例

### 按类别
- **斜杠命令**：`01-slash-commands/`
- **内存**：`02-memory/`
- **技能**：`03-skills/`
- **子代理**：`04-subagents/`
- **MCP**：`05-mcp/`
- **钩子**：`06-hooks/`
- **插件**：`07-plugins/`
- **检查点**：`08-checkpoints/`
- **高级功能**：`09-advanced-features/`
- **CLI**：`10-cli/`

### 按使用场景
- **性能**：`01-slash-commands/optimize.md`
- **安全**：`04-subagents/secure-reviewer.md`
- **测试**：`04-subagents/test-engineer.md`
- **文档**：`03-skills/doc-generator/`
- **DevOps**：`07-plugins/devops-automation/`

### 按复杂度
- **简单**：斜杠命令
- **中等**：子代理、内存
- **高级**：技能、钩子
- **完整**：插件

---

## 学习路径

### 第一天
```bash
# 阅读概述
cat README.md

# 安装一个命令
cp 01-slash-commands/optimize.md .claude/commands/

# 尝试它
/optimize
```

### 第 2-3 天
```bash
# 设置内存
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
vim CLAUDE.md

# 安装子代理
cp 04-subagents/code-reviewer.md .claude/agents/
```

### 第 4-5 天
```bash
# 设置 MCP
export GITHUB_TOKEN="your_token"
cp 05-mcp/github-mcp.json .mcp.json

# 尝试 MCP 命令
/mcp__github__list_prs
```

### 第二周
```bash
# 安装技能
cp -r 03-skills/code-review ~/.claude/skills/

# 让它自动调用
# 只需说："审查这段代码的问题"
```

### 第三周起
```bash
# 安装完整插件
/plugin install pr-review

# 使用捆绑功能
/review-pr
/check-security
/check-tests
```

---

## 新功能（2026 年 3 月）

| 功能 | 描述 | 使用方法 |
|---------|-------------|-------|
| **Auto Mode** | 带后台分类器的完全自主操作 | `--enable-auto-mode` 标志，`Shift+Tab` 循环模式 |
| **Channels** | Discord 和 Telegram 集成 | `--channels` 标志，Discord/Telegram 机器人 |
| **Voice Dictation** | 向 Claude 说话输入命令和上下文 | `/voice` 命令 |
| **钩子（25 个事件）** | 扩展钩子系统，4 种类型 | command、http、prompt、agent 钩子类型 |
| **MCP Elicitation** | MCP 服务器可在运行时请求用户输入 | 服务器需要澄清时自动提示 |
| **WebSocket MCP** | 用于 MCP 连接的 WebSocket 传输 | 在 `.mcp.json` 中配置 `ws://` URL |
| **Plugin LSP** | 插件的 Language Server Protocol 支持 | `userConfig`、`${CLAUDE_PLUGIN_DATA}` 变量 |
| **远程控制** | 通过 WebSocket API 控制 Claude Code | 用于外部集成的 `claude --remote` |
| **Web 会话** | 基于浏览器的 Claude Code 界面 | `claude web` 启动 |
| **桌面应用** | 原生桌面应用程序 | 从 claude.ai/download 下载 |
| **任务列表** | 管理后台任务 | `/task list`、`/task status <id>` |
| **Auto Memory** | 从对话自动保存内存 | Claude 自动将关键上下文保存到 CLAUDE.md |
| **Git Worktrees** | 用于并行开发的隔离工作空间 | `/worktree` 创建隔离工作空间 |
| **模型选择** | 在 Sonnet 4.6 和 Opus 4.6 之间切换 | `/model` 或 `--model` 标志 |
| **Agent Teams** | 在任务上协调多个代理 | 使用 `CLAUDE_AGENT_TEAMS=1` 环境变量启用 |
| **计划任务** | 使用 `/loop` 的定期任务 | `/loop 5m /command` 或 CronCreate 工具 |
| **Chrome 集成** | 浏览器自动化 | `--chrome` 标志或 `/chrome` 命令 |
| **键盘自定义** | 自定义键绑定 | `/keybindings` 命令 |

---

## 技巧和窍门

### 自定义
- 从示例原样开始
- 修改以适应您的需求
- 与团队共享前测试
- 对配置进行版本控制

### 最佳实践
- 使用内存存储团队标准
- 使用插件实现完整工作流程
- 使用子代理处理复杂任务
- 使用斜杠命令处理快速任务

### 故障排除
```bash
# 检查文件位置
ls -la .claude/commands/
ls -la .claude/agents/

# 验证 YAML 语法
head -20 .claude/agents/code-reviewer.md

# 测试 MCP 连接
echo $GITHUB_TOKEN
```

---

## 功能矩阵

| 需求 | 使用这个 | 示例 |
|------|----------|------|
| 快速快捷方式 | 斜杠命令（55+） | `01-slash-commands/optimize.md` |
| 团队标准 | 内存 | `02-memory/project-CLAUDE.md` |
| 自动工作流程 | 技能 | `03-skills/code-review/` |
| 专业任务 | 子代理 | `04-subagents/code-reviewer.md` |
| 外部数据 | MCP（+ Elicitation、WebSocket）| `05-mcp/github-mcp.json` |
| 事件自动化 | 钩子（25 个事件，4 种类型）| `06-hooks/pre-commit.sh` |
| 完整解决方案 | 插件（+ LSP 支持）| `07-plugins/pr-review/` |
| 安全实验 | 检查点 | `08-checkpoints/checkpoint-examples.md` |
| 完全自主 | Auto Mode | `--enable-auto-mode` 或 `Shift+Tab` |
| 聊天集成 | Channels | `--channels`（Discord、Telegram）|
| CI/CD 流水线 | CLI | `10-cli/README.md` |

---

## 快速链接

- **主指南**：`README.md`
- **完整索引**：`INDEX.md`
- **摘要**：`EXAMPLES_SUMMARY.md`
- **原始指南**：`claude_concepts_guide.md`

---

## 常见问题

**问：我应该使用哪个？**
答：从斜杠命令开始，根据需要添加功能。

**问：我可以混合使用功能吗？**
答：可以！它们可以协同工作。内存 + 命令 + MCP = 强大。

**问：我如何与团队共享？**
答：将 `.claude/` 目录提交到 git。

**问：密钥怎么办？**
答：使用环境变量，永远不要硬编码。

**问：我可以修改示例吗？**
答：当然可以！它们是可供自定义的模板。

---

## 检查清单

入门检查清单：

- [ ] 阅读 `README.md`
- [ ] 安装 1 个斜杠命令
- [ ] 尝试该命令
- [ ] 创建项目 `CLAUDE.md`
- [ ] 安装 1 个子代理
- [ ] 设置 1 个 MCP 集成
- [ ] 安装 1 个技能
- [ ] 尝试一个完整插件
- [ ] 根据您的需求自定义
- [ ] 与团队分享

---

**快速入门**：`cat README.md`

**完整索引**：`cat INDEX.md`

**本卡**：保留以便快速参考！
