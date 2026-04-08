# 更新日志

## v2.2.0 — 2026-03-26

### 文档

- 将所有教程和参考文档与 Claude Code v2.1.84 (f78c094) 同步 @luongnv89
  - 更新斜杠命令至 55+ 内置 + 5 个捆绑技能，标记 3 个已弃用
  - 扩展钩子事件从 18 个至 25 个，新增 `agent` 钩子类型（现共 4 种类型）
  - 新增 Auto Mode、Channels、Voice Dictation 至高级功能
  - 新增 `effort`、`shell` 技能 frontmatter 字段；`initialPrompt`、`disallowedTools` agent 字段
  - 新增 WebSocket MCP 传输、elicitation、2KB 工具容量限制
  - 新增插件 LSP 支持、`userConfig`、`${CLAUDE_PLUGIN_DATA}`
  - 更新所有参考文档（CATALOG、QUICK_REFERENCE、LEARNING-ROADMAP、INDEX）
- 将 README 重写为落地页结构指南 (32a0776) @luongnv89

### Bug 修复

- 添加缺失的 cSpell 词汇和 CI 合规性 README 章节 (93f9d51) @luongnv89
- 添加 `Sandboxing` 至 cSpell 词典 (b80ce6f) @luongnv89

**完整更新日志**: https://github.com/luongnv89/claude-howto/compare/v2.1.1...v2.2.0

---

## v2.1.1 — 2026-03-13

### Bug 修复

- 移除导致 CI 链接检查失败的已失效 marketplace 链接 (3fdf0d6) @luongnv89
- 添加 `sandboxed` 和 `pycache` 至 cSpell 词典 (dc64618) @luongnv89

**完整更新日志**: https://github.com/luongnv89/claude-howto/compare/v2.1.0...v2.1.1

---

## v2.1.0 — 2026-03-13

### 功能

- 添加自适应学习路径，包含自我评估和课程测验技能 (1ef46cd) @luongnv89
  - `/self-assessment` — 跨 10 个功能区域的交互式熟练度测验，提供个性化学习路径
  - `/lesson-quiz [lesson]` — 每个课程的知识点检查，包含 8-10 道针对性问题

### Bug 修复

- 更新已失效的 URL、弃用说明和过时引用 (8fe4520) @luongnv89
- 修复资源和自我评估技能中的失效链接 (7a05863) @luongnv89
- 在概念指南中使用波浪号围栏处理嵌套代码块 (5f82719) @VikalpP
- 添加缺失词汇至 cSpell 词典 (8df7572) @luongnv89

### 文档

- 阶段 5 QA — 修复文档间的一致性、URL 和术语 (00bbe4c) @luongnv89
- 完成阶段 3-4 — 新功能覆盖和参考文档更新 (132de29) @luongnv89
- 在 MCP 上下文膨胀章节添加 MCPorter 运行时 (ef52705) @luongnv89
- 在 6 个指南中添加缺失的命令、功能和设置 (4bc8f15) @luongnv89
- 添加基于现有仓库约定的样式指南 (84141d0) @luongnv89
- 在指南比较表中添加自我评估行 (8fe0c96) @luongnv89
- 添加 VikalpP 至贡献者列表，感谢 PR #7 (d5b4350) @luongnv89
- 在 README 和路线图中添加自我评估和课程测验技能参考 (d5a6106) @luongnv89

### 新贡献者

- @VikalpP 首次贡献于 #7

**完整更新日志**: https://github.com/luongnv89/claude-howto/compare/v2.0.0...v2.1.0

---

## v2.0.0 — 2026-02-01

### 功能

- 将所有文档与 Claude Code 2026年2月功能同步 (487c96d)
  - 更新跨所有 10 个教程目录和 7 个参考文档的 26 个文件
  - 新增 **Auto Memory** 文档 — 每个项目的持久化学习记录
  - 新增 **Remote Control**、**Web Sessions** 和 **Desktop App** 文档
  - 新增 **Agent Teams**（实验性多代理协作）文档
  - 新增 **MCP OAuth 2.0**、**Tool Search** 和 **Claude.ai Connectors** 文档
  - 新增 **Persistent Memory** 和 **Worktree Isolation** 文档（适用于 subagents）
  - 新增 **Background Subagents**、**Task List**、**Prompt Suggestions** 文档
  - 新增 **Sandboxing** 和 **Managed Settings**（企业版）文档
  - 新增 **HTTP Hooks** 和 7 个新钩子事件文档
  - 新增 **Plugin Settings**、**LSP Servers** 和 Marketplace 更新文档
  - 新增 **Summarize from Checkpoint** 回滚选项文档
  - 记录 17 个新斜杠命令（`/fork`、`/desktop`、`/teleport`、`/tasks`、`/fast` 等）
  - 记录新 CLI 标志（`--worktree`、`--from-pr`、`--remote`、`--teleport`、`--teammate-mode` 等）
  - 记录用于自动记忆、努力级别、代理团队等的新环境变量

### 设计

- 重新设计 logo 为指南针括号标志，配以简约配色 (20779db)

### Bug 修复 / 更正

- 更新模型名称：Sonnet 4.5 → **Sonnet 4.6**，Opus 4.5 → **Opus 4.6**
- 修复权限模式名称：将虚构的 "Unrestricted/Confirm/Read-only" 替换为实际的 `default`/`acceptEdits`/`plan`/`dontAsk`/`bypassPermissions`
- 修复钩子事件：移除虚构的 `PreCommit`/`PostCommit`/`PrePush`，添加实际事件（`SubagentStart`、`WorktreeCreate`、`ConfigChange` 等）
- 修复 CLI 语法：将 `claude-code --headless` 替换为 `claude -p`（打印模式）
- 修复检查点命令：将虚构的 `/checkpoint save/list/rewind/diff` 替换为实际的 `Esc+Esc` / `/rewind` 界面
- 修复会话管理：将虚构的 `/session list/new/switch/save` 替换为实际的 `/resume`/`/rename`/`/fork`
- 修复插件清单格式：`plugin.yaml` → `.claude-plugin/plugin.json`
- 修复 MCP 配置路径：`~/.claude/mcp.json` → `.mcp.json`（项目）/ `~/.claude.json`（用户）
- 修复文档 URL：`docs.claude.com` → `docs.anthropic.com`；移除虚构的 `plugins.claude.com`
- 移除跨多个文件的虚构配置字段
- 将所有"最后更新"日期更新至 2026年2月

**完整更新日志**: https://github.com/luongnv89/claude-howto/compare/20779db...v2.0.0
