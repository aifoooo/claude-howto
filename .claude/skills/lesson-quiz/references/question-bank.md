# 课程测验 - 题库

每课10道题。每道题包含：类别、题目、选项（3-4个）、正确答案、解析和复习部分。

---

## 第01课：斜杠命令

### Q1
- **Category**: 概念
- **Question**: Claude Code 中有哪四种类型的斜杠命令？
- **Options**: A) Built-in, skills, plugin commands, MCP prompts | B) Built-in, custom, hook commands, API prompts | C) System, user, plugin, terminal commands | D) Core, extension, macro, script commands
- **Correct**: A
- **Explanation**: Claude Code 有内置命令（如 /help、/compact）、技能（SKILL.md 文件）、插件命令（带命名空间的 plugin-name:command）以及 MCP 提示（/mcp__server__prompt）。
- **Review**: 斜杠命令类型部分

### Q2
- **Category**: 实践
- **Question**: 如何将用户提供的所有参数传递给技能？
- **Options**: A) Use `${args}` | B) Use `$ARGUMENTS` | C) Use `$@` | D) Use `$INPUT`
- **Correct**: B
- **Explanation**: `$ARGUMENTS` 捕获命令名称后的所有文本。对于位置参数，使用 `$0`、`$1` 等。
- **Review**: 参数处理部分

### Q3
- **Category**: 概念
- **Question**: 当同名的技能（.claude/skills/name/SKILL.md）和旧命令（.claude/commands/name.md）同时存在时，哪个优先？
- **Options**: A) The legacy command | B) The skill | C) Whichever was created first | D) Claude asks the user to choose
- **Correct**: B
- **Explanation**: 技能优先于同名的旧命令。技能系统取代了旧的命令系统。
- **Review**: 技能优先级部分

### Q4
- **Category**: 实践
- **Question**: 如何将实时 shell 输出注入到技能的提示词中？
- **Options**: A) Use `$(command)` syntax | B) Use `!`command`` (backtick with !) syntax | C) Use `@shell:command` syntax | D) Use `{command}` syntax
- **Correct**: B
- **Explanation**: `!`command`` 语法运行 shell 命令并将其输出注入到技能提示词中，供 Claude 使用。
- **Review**: 动态上下文注入部分

### Q5
- **Category**: 概念
- **Question**: 技能 frontmatter 中的 `disable-model-invocation: true` 有什么作用？
- **Options**: A) Prevents the skill from running entirely | B) Allows only the user to invoke it (Claude cannot auto-invoke) | C) Hides it from the /help menu | D) Disables the skill's AI processing
- **Correct**: B
- **Explanation**: `disable-model-invocation: true` 表示只有用户可以通过 `/command-name` 触发命令。Claude 永远不会自动调用它，这对于有副作用（如部署）的技能很有用。
- **Review**: 调用控制部分

### Q6
- **Category**: 实践
- **Question**: 你想创建一个只能由 Claude 自动调用的技能（对用户的 / 菜单隐藏）。需要设置哪个 frontmatter 字段？
- **Options**: A) `disable-model-invocation: true` | B) `user-invocable: false` | C) `hidden: true` | D) `auto-only: true`
- **Correct**: B
- **Explanation**: `user-invocable: false` 从用户的斜杠菜单中隐藏技能，但允许 Claude 根据上下文自动调用。
- **Review**: 调用控制矩阵

### Q7
- **Category**: 实践
- **Question**: 名为 "deploy" 的自定义技能的正确目录结构是什么？
- **Options**: A) `.claude/commands/deploy.md` | B) `.claude/skills/deploy/SKILL.md` | C) `.claude/skills/deploy.md` | D) `.claude/deploy/SKILL.md`
- **Correct**: B
- **Explanation**: 技能位于 `.claude/skills/` 下的目录中，内部包含 `SKILL.md` 文件。目录名与命令名相同。
- **Review**: 技能类型和位置部分

### Q8
- **Category**: 概念
- **Question**: 插件命令如何避免与用户命令冲突？
- **Options**: A) They use a `plugin-name:command-name` namespace | B) They have a special .plugin extension | C) They are prefixed with `p/` | D) They override user commands automatically
- **Correct**: A
- **Explanation**: 插件命令使用如 `pr-review:check-security` 这样的命名空间来避免与独立用户命令冲突。
- **Review**: 插件命令部分

### Q9
- **Category**: 实践
- **Question**: 你想限制技能可以使用哪些工具。需要添加哪个 frontmatter 字段？
- **Options**: A) `tools: [Read, Grep]` | B) `allowed-tools: [Read, Grep]` | C) `permissions: [Read, Grep]` | D) `restrict-tools: [Read, Grep]`
- **Correct**: B
- **Explanation**: SKILL.md frontmatter 中的 `allowed-tools` 字段限定了命令可以调用的工具范围。
- **Review**: Frontmatter 字段参考

### Q10
- **Category**: 概念
- **Question**: 技能中的 `@file` 语法用于什么？
- **Options**: A) Importing another skill | B) Referencing a file to include its content in the prompt | C) Creating a symlink | D) Setting file permissions
- **Correct**: B
- **Explanation**: 技能中的 `@path/to/file` 语法将引用文件的内容包含到提示词中，允许技能引入模板或上下文文件。
- **Review**: 文件引用部分

---

## 第02课：记忆

### Q1
- **Category**: 概念
- **Question**: Claude Code 的记忆层次结构有多少层，哪一层优先级最高？
- **Options**: A) 5 levels, User Memory is highest | B) 7 levels, Managed Policy is highest | C) 3 levels, Project Memory is highest | D) 7 levels, Auto Memory is highest
- **Correct**: B
- **Explanation**: 层次结构有7层：Managed Policy > Project Memory > Project Rules > User Memory > User Rules > Local Project Memory > Auto Memory。Managed Policy（由管理员设置）优先级最高。
- **Review**: 记忆层次结构部分

### Q2
- **Category**: 实践
- **Question**: 在对话期间如何快速向记忆添加新规则？
- **Options**: A) Type `/memory add "rule text"` | B) Prefix your message with `#` (e.g., `# always use TypeScript`) | C) Type `/rule "rule text"` | D) Use `@add-memory "rule text"`
- **Correct**: B
- **Explanation**: `#` 前缀模式允许在对话期间快速添加单条规则。Claude 会询问将其保存到哪个记忆级别。
- **Review**: 快速记忆更新部分

### Q3
- **Category**: 概念
- **Question**: CLAUDE.md 中 `@path/to/file` 导入的最大深度是多少？
- **Options**: A) 3 levels deep | B) 5 levels deep | C) 10 levels deep | D) Unlimited
- **Correct**: B
- **Explanation**: `@import` 语法支持递归导入，最大深度为5层，以防止无限循环。
- **Review**: 导入语法部分

### Q4
- **Category**: 实践
- **Question**: 如何将规则文件限定为仅适用于 `src/api/` 中的文件？
- **Options**: A) Put the rule in `src/api/CLAUDE.md` | B) Add `paths: src/api/**` YAML frontmatter to a `.claude/rules/*.md` file | C) Name the file `.claude/rules/api.md` | D) Use `@scope: src/api` in the rule file
- **Correct**: B
- **Explanation**: `.claude/rules/` 中的文件支持 `paths:` frontmatter 字段，使用 glob 模式将规则限定到特定目录。
- **Review**: 路径特定规则部分

### Q5
- **Category**: 概念
- **Question**: Auto Memory 的 MEMORY.md 在会话开始时加载多少行？
- **Options**: A) All lines | B) First 100 lines | C) First 200 lines | D) First 500 lines
- **Correct**: C
- **Explanation**: MEMORY.md 的前200行在会话开始时自动加载到上下文中。从 MEMORY.md 引用的主题文件按需加载。
- **Review**: Auto Memory 部分

### Q6
- **Category**: 实践
- **Question**: 你想要不提交到 git 的个人项目偏好设置。应该使用哪个文件？
- **Options**: A) `~/.claude/CLAUDE.md` | B) `CLAUDE.local.md` | C) `.claude/rules/personal.md` | D) `.claude/memory/personal.md`
- **Correct**: B
- **Explanation**: 项目根目录中的 `CLAUDE.local.md` 用于个人项目特定偏好。它应该被 git 忽略。
- **Review**: 记忆位置对比

### Q7
- **Category**: 概念
- **Question**: `/init` 命令有什么作用？
- **Options**: A) Initializes a new Claude Code project from scratch | B) Generates a template CLAUDE.md based on your project structure | C) Resets all memory to defaults | D) Creates a new session
- **Correct**: B
- **Explanation**: `/init` 分析你的项目并生成模板 CLAUDE.md，其中包含建议的规则和标准。它是一次性引导工具。
- **Review**: /init 命令部分

### Q8
- **Category**: 实践
- **Question**: 如何完全禁用 Auto Memory？
- **Options**: A) Delete the ~/.claude/projects directory | B) Set `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` | C) Add `auto-memory: false` to CLAUDE.md | D) Use `/memory disable auto`
- **Correct**: B
- **Explanation**: 设置 `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1` 禁用自动记忆。设置为 `0` 则强制启用。未设置 = 默认启用。
- **Review**: Auto Memory 配置部分

### Q9
- **Category**: 概念
- **Question**: 低优先级的记忆层能否覆盖更高优先级层的规则？
- **Options**: A) Yes, the most recent rule always wins | B) No, higher tiers always take precedence | C) Yes, if the lower tier uses the `!important` flag | D) It depends on the rule type
- **Correct**: B
- **Explanation**: 记忆优先级从 Managed Policy 向下流动。较低层（如 Auto Memory）无法覆盖较高层（如 Project Memory）。
- **Review**: 记忆层次结构部分

### Q10
- **Category**: 实践
- **Question**: 你在两个代码库之间工作，希望 Claude 从两者都加载 CLAUDE.md。使用什么标志？
- **Options**: A) `--multi-repo` | B) `--add-dir /path/to/other` | C) `--include /path/to/other` | D) `--merge-context /path/to/other`
- **Correct**: B
- **Explanation**: `--add-dir` 标志从额外目录加载 CLAUDE.md，允许多代码库上下文。
- **Review**: 附加目录部分

---

## 第03课：技能

### Q1
- **Category**: 概念
- **Question**: 技能系统中的渐进式披露有三个级别，分别是什么？
- **Options**: A) Metadata, instructions, resources | B) Name, body, attachments | C) Header, content, scripts | D) Summary, details, data
- **Correct**: A
- **Explanation**: 第1级：元数据（约100个token，始终加载），第2级：SKILL.md 正文（<5k token，在触发时加载），第3级：捆绑资源（脚本/引用/资产，按需加载）。
- **Review**: 渐进式披露架构部分

### Q2
- **Category**: 实践
- **Question**: 技能被 Claude 自动调用的最重要因素是什么？
- **Options**: A) The skill's file name | B) The `description` field in frontmatter with when-to-use keywords | C) The skill's directory location | D) The `auto-invoke: true` frontmatter field
- **Correct**: B
- **Explanation**: Claude 仅根据技能的 `description` 字段决定是否自动调用。它必须包含特定的触发短语和场景。
- **Review**: 自动调用部分

### Q3
- **Category**: 概念
- **Question**: SKILL.md 文件的最大推荐长度是多少？
- **Options**: A) 100 lines | B) 250 lines | C) 500 lines | D) 1000 lines
- **Correct**: C
- **Explanation**: SKILL.md 应保持在500行以下。更大的参考材料应放在 `references/` 子目录文件中。
- **Review**: 内容指南部分

### Q4
- **Category**: 实践
- **Question**: 如何让技能在具有独立上下文的隔离子代理中运行？
- **Options**: A) Set `isolation: true` in frontmatter | B) Set `context: fork` with an `agent` field in frontmatter | C) Set `subagent: true` in frontmatter | D) Put the skill in `.claude/agents/`
- **Correct**: B
- **Explanation**: `context: fork` 在独立上下文中运行技能，`agent` 字段指定使用的代理类型（如 `Explore`、`Plan`、自定义代理）。
- **Review**: 在子代理中运行技能部分

### Q5
- **Category**: 概念
- **Question**: 分配给技能元数据（第1级）的上下文预算大约是多少？
- **Options**: A) 0.5% of context window | B) 2% of context window | C) 5% of context window | D) 10% of context window
- **Correct**: B
- **Explanation**: 技能元数据约占上下文窗口的2%（回退：16,000个字符）。这可以通过 `SLASH_COMMAND_TOOL_CHAR_BUDGET` 配置。
- **Review**: 上下文预算部分

### Q6
- **Category**: 实践
- **Question**: 技能需要引用一个大型 API 规范。应该放在哪里？
- **Options**: A) Inline in SKILL.md | B) In a `references/api-spec.md` file inside the skill directory | C) In the project's CLAUDE.md | D) In a separate `.claude/rules/` file
- **Correct**: B
- **Explanation**: 大型参考材料应放在 `references/` 子目录中。Claude 按需加载第3级资源，保持 SKILL.md 精简。
- **Review**: 支持文件结构部分

### Q7
- **Category**: 概念
- **Question**: 技能中的引用内容和任务内容有什么区别？
- **Options**: A) Reference is read-only, Task is read-write | B) Reference adds knowledge to context, Task provides step-by-step instructions | C) Reference is for documentation, Task is for code | D) There is no difference
- **Correct**: B
- **Explanation**: 引用内容向 Claude 的上下文添加领域知识（如品牌指南）。任务内容为工作流程提供可操作的逐步说明。
- **Review**: 技能内容类型部分

### Q8
- **Category**: 实践
- **Question**: 技能 frontmatter 的 `name` 字段允许哪些字符？
- **Options**: A) Any characters | B) Lowercase letters, numbers, and hyphens only (max 64 chars) | C) Letters and underscores | D) Alphanumeric only
- **Correct**: B
- **Explanation**: 名称必须为 kebab-case（小写、连字符），最多64个字符，不能包含 "anthropic" 或 "claude"。
- **Review**: SKILL.md 格式部分

### Q9
- **Category**: 概念
- **Question**: Claude 搜索技能的顺序是什么？
- **Options**: A) User > Project > Enterprise | B) Enterprise > Personal > Project (plugin uses namespace) | C) Project > User > Enterprise | D) Alphabetical order
- **Correct**: B
- **Explanation**: 优先级顺序是：Enterprise > Personal > Project。插件技能使用命名空间（plugin-name:skill），因此不会冲突。
- **Review**: 技能类型和位置部分

### Q10
- **Category**: 实践
- **Question**: 如何防止 Claude 自动调用技能，同时仍允许用户手动使用？
- **Options**: A) Set `user-invocable: false` | B) Set `disable-model-invocation: true` | C) Remove the description field | D) Set `auto-invoke: false`
- **Correct**: B
- **Explanation**: `disable-model-invocation: true` 防止 Claude 自动调用，但将技能保留在用户的 `/` 菜单中供手动使用。
- **Review**: 调用控制部分

---

## 第04课：子代理

### Q1
- **Category**: 概念
- **Question**: 与内联对话相比，子代理的主要优势是什么？
- **Options**: A) They are faster | B) They operate in a separate, clean context window preventing context pollution | C) They can use more tools | D) They have better error handling
- **Correct**: B
- **Explanation**: 子代理获得全新的上下文窗口，只接收主代理传递的内容。这防止主对话被任务特定的细节污染。
- **Review**: 概述部分

### Q2
- **Category**: 实践
- **Question**: 代理定义的优先级顺序是什么？
- **Options**: A) Project > User > CLI | B) CLI > User > Project | C) User > Project > CLI | D) They all have equal priority
- **Correct**: B
- **Explanation**: CLI 定义的代理（`--agents` 标志）覆盖用户级（`~/.claude/agents/`），后者覆盖项目级（`.claude/agents/`）。
- **Review**: 文件位置部分

### Q3
- **Category**: 概念
- **Question**: 哪个内置子代理使用 Haiku 模型并针对只读代码库探索进行了优化？
- **Options**: A) general-purpose | B) Plan | C) Explore | D) Bash
- **Correct**: C
- **Explanation**: Explore 子代理使用 Haiku 进行快速、只读的代码库探索。它支持三种详尽程度：快速、中等、非常详尽。
- **Review**: 内置子代理部分

### Q4
- **Category**: 实践
- **Question**: 如何限制协调器代理可以生成哪些子代理？
- **Options**: A) Use `allowed-agents:` field | B) Use `Task(agent_name)` syntax in the `tools` field | C) Set `spawn-limit: 2` | D) Use `restrict-agents: [name1, name2]`
- **Correct**: B
- **Explanation**: 在 tools 字段中添加 `Task(worker, researcher)` 创建一个允许列表 —— 代理只能生成名为 "worker" 或 "researcher" 的子代理。
- **Review**: 限制可生成子代理部分

### Q5
- **Category**: 概念
- **Question**: `isolation: worktree` 对子代理有什么作用？
- **Options**: A) Runs the agent in a Docker container | B) Gives the agent its own git worktree so changes don't affect the main tree | C) Prevents the agent from reading any files | D) Runs the agent in a sandbox
- **Correct**: B
- **Explanation**: Worktree 隔离创建一个独立的 git worktree。如果代理没有做出更改，它会自动清理。如果做出了更改，则返回 worktree 路径和分支。
- **Review**: Worktree 隔离部分

### Q6
- **Category**: 实践
- **Question**: 如何让子代理在后台运行？
- **Options**: A) Set `background: true` in the agent config | B) Use `async: true` in the agent config | C) Press Ctrl+D after starting it | D) Use `--background` CLI flag
- **Correct**: A
- **Explanation**: 代理配置中的 `background: true` 使子代理始终作为后台任务运行。用户也可以使用 Ctrl+B 将前台任务发送到后台。
- **Review**: 后台子代理部分

### Q7
- **Category**: 概念
- **Question**: `memory` 字段的 scope 为 `project` 对子代理有什么作用？
- **Options**: A) Gives read access to the project CLAUDE.md | B) Creates a persistent memory directory scoped to the current project | C) Shares the main agent's conversation history | D) Loads the project's git history
- **Correct**: B
- **Explanation**: `memory` 字段为子代理创建持久目录。scope 为 `project` 意味着记忆绑定到当前项目。代理的 MEMORY.md 前200行自动加载。
- **Review**: 持久记忆部分

### Q8
- **Category**: 实践
- **Question**: 如何在子代理的描述中包含短语以鼓励 Claude 自动向其委派任务？
- **Options**: A) Add "priority: high" | B) Include "use PROACTIVELY" or "MUST BE USED" in the description | C) Set `auto-delegate: true` | D) Add "trigger: always"
- **Correct**: B
- **Explanation**: 在描述中包含 "use PROACTIVELY" 或 "MUST BE USED" 等短语会强烈鼓励 Claude 自动委派匹配的任务。
- **Review**: 自动委派部分

### Q9
- **Category**: 概念
- **Question**: 子代理的有效 `permissionMode` 值有哪些？
- **Options**: A) read, write, admin | B) default, acceptEdits, bypassPermissions, plan, dontAsk, auto | C) safe, normal, dangerous | D) restricted, standard, elevated
- **Correct**: B
- **Explanation**: 子代理支持六种权限模式：default（提示所有操作）、acceptEdits（自动接受文件编辑）、bypassPermissions（跳过所有检查）、plan（只读分析）、dontAsk（自动拒绝，除非预先批准）、auto（后台分类器决定）。
- **Review**: 配置字段部分

### Q10
- **Category**: 实践
- **Question**: 如何恢复从先前运行返回了 agentId 的子代理？
- **Options**: A) Use `/resume agent-id` | B) Pass the `resume` parameter with the agentId when calling Task tool | C) Use `claude -r agent-id` | D) Subagents cannot be resumed
- **Correct**: B
- **Explanation**: 子代理可以通过在调用 Task 工具时传递 `resume` 参数和之前的 agentId 来恢复，继续保留完整上下文。
- **Review**: 可恢复代理部分

---

## 第05课：MCP

### Q1
- **Category**: 概念
- **Question**: 三种 MCP 传输协议是什么，哪种是推荐的？
- **Options**: A) HTTP (recommended), Stdio, SSE (deprecated) | B) WebSocket (recommended), REST, gRPC | C) TCP, UDP, HTTP | D) Stdio (recommended), HTTP, SSE
- **Correct**: A
- **Explanation**: HTTP 推荐用于远程服务器。Stdio 用于本地进程（目前最常见）。SSE 已弃用但仍受支持。
- **Review**: 传输协议部分

### Q2
- **Category**: 实践
- **Question**: 如何通过 CLI 添加 GitHub MCP 服务器？
- **Options**: A) `claude mcp install github` | B) `claude mcp add --transport http github https://api.github.com/mcp` | C) `claude plugin add github-mcp` | D) `claude connect github`
- **Correct**: B
- **Explanation**: 使用带 `--transport` 标志的 `claude mcp add`，后跟名称和服务器 URL。对于 stdio：`claude mcp add github -- npx -y @modelcontextprotocol/server-github`。
- **Review**: MCP 配置管理部分

### Q3
- **Category**: 概念
- **Question**: 当 MCP 工具描述超过上下文窗口的10%时会发生什么？
- **Options**: A) They are truncated | B) Tool Search auto-enables to dynamically select relevant tools | C) Claude shows an error | D) Extra tools are disabled
- **Correct**: B
- **Explanation**: 当工具超过上下文的10%时，MCP 工具搜索会自动启用。它需要 Sonnet 4 或 Opus 4 最低版本（不支持 Haiku）。
- **Review**: MCP 工具搜索部分

### Q4
- **Category**: 实践
- **Question**: 如何在 MCP 配置中使用环境变量回退？
- **Options**: A) `${VAR || "default"}` | B) `${VAR:-default}` | C) `${VAR:default}` | D) `${VAR ? "default"}`
- **Correct**: B
- **Explanation**: `${VAR:-default}` 在环境变量未设置时提供回退值。没有回退的 `${VAR}` 在未设置时会报错。
- **Review**: 环境变量扩展部分

### Q5
- **Category**: 概念
- **Question**: MCP 和 Memory 在数据访问方面有什么区别？
- **Options**: A) MCP is faster, Memory is slower | B) MCP is for live/changing external data, Memory is for persistent/static preferences | C) MCP is for code, Memory is for text | D) They are interchangeable
- **Correct**: B
- **Explanation**: MCP 连接到实时、变化的外部数据源（API、数据库）。Memory 存储持久的、静态的项目上下文和偏好。
- **Review**: MCP vs Memory 部分

### Q6
- **Category**: 实践
- **Question**: 当团队成员首次遇到项目范围的 `.mcp.json` 时会发生什么？
- **Options**: A) It loads automatically | B) They get an approval prompt to trust the project's MCP servers | C) It's ignored unless they opt in via settings | D) Claude asks the admin to approve
- **Correct**: B
- **Explanation**: 项目范围的 `.mcp.json` 会在每个团队成员首次使用时触发安全批准提示。这是刻意的 —— 它可以防止不受信任的 MCP 服务器。
- **Review**: MCP 范围部分

### Q7
- **Category**: 概念
- **Question**: `claude mcp serve` 有什么作用？
- **Options**: A) Starts an MCP server dashboard | B) Makes Claude Code itself act as an MCP server for other applications | C) Serves MCP documentation | D) Tests MCP server connections
- **Correct**: B
- **Explanation**: `claude mcp serve` 将 Claude Code 本身变成 MCP 服务器，实现多代理编排，其中一个 Claude 实例可以被另一个控制。
- **Review**: Claude 作为 MCP 服务器部分

### Q8
- **Category**: 实践
- **Question**: MCP 工具的默认最大输出大小是多少？
- **Options**: A) 5,000 tokens | B) 10,000 tokens | C) 25,000 tokens | D) 50,000 tokens
- **Correct**: C
- **Explanation**: 默认最大值是25,000个token（`MAX_MCP_OUTPUT_TOKENS`）。在10k token时会出现警告。磁盘持久化上限为50,000个字符。
- **Review**: MCP 输出限制部分

### Q9
- **Category**: 概念
- **Question**: 当 `allowedMcpServers` 和 `deniedMcpServers` 都匹配托管配置中的服务器时，哪个优先？
- **Options**: A) Allowed wins | B) Denied wins | C) The last one configured wins | D) Both are applied independently
- **Correct**: B
- **Explanation**: 在托管 MCP 配置中，拒绝规则始终优先于允许规则。
- **Review**: 托管 MCP 配置部分

### Q10
- **Category**: 实践
- **Question**: 如何在对话中引用 MCP 资源？
- **Options**: A) Use `/mcp resource-name` | B) Use `@server-name:protocol://resource/path` mention syntax | C) Use `mcp.get("resource")` | D) Resources are auto-loaded
- **Correct**: B
- **Explanation**: MCP 资源通过对话中的 `@server-name:protocol://resource/path` 提及语法访问。
- **Review**: MCP 资源部分

---

## 第06课：钩子

### Q1
- **Category**: 概念
- **Question**: Claude Code 中有哪四种类型的钩子？
- **Options**: A) Pre, Post, Error, and Filter hooks | B) Command, HTTP, Prompt, and Agent hooks | C) Before, After, Around, and Through hooks | D) Input, Output, Filter, and Transform hooks
- **Correct**: B
- **Explanation**: Command 钩子运行 shell 脚本，HTTP 钩子调用 webhook 端点，Prompt 钩子使用单轮 LLM 评估，Agent 钩子使用基于子代理的验证。
- **Review**: 钩子类型部分

### Q2
- **Category**: 实践
- **Question**: 钩子脚本以代码2退出。会发生什么？
- **Options**: A) Non-blocking warning shown | B) Blocking error — stderr is shown as an error to Claude, tool use is prevented | C) Hook is retried | D) Session ends
- **Correct**: B
- **Explanation**: 退出代码0 = 成功/继续，退出代码2 = 阻塞错误（stderr 作为错误显示给 Claude），工具使用被阻止，任何其他非零 = 非阻塞（stderr 仅在详细模式显示）。
- **Review**: 退出代码部分

### Q3
- **Category**: 概念
- **Question**: PreToolUse 钩子通过 stdin 接收哪些 JSON 字段？
- **Options**: A) `tool_name` and `tool_output` | B) `session_id`, `tool_name`, `tool_input`, `hook_event_name`, `cwd`, and more | C) Only `tool_name` | D) The full conversation history
- **Correct**: B
- **Explanation**: 钩子通过 stdin 接收一个 JSON 对象，包含：session_id、transcript_path、hook_event_name、tool_name、tool_input、tool_use_id、cwd 和 permission_mode。
- **Review**: JSON 输入结构部分

### Q4
- **Category**: 实践
- **Question**: PreToolUse 钩子如何在执行前修改工具的输入参数？
- **Options**: A) Return modified JSON on stderr | B) Return JSON with `updatedInput` field on stdout (exit code 0) | C) Write to a temp file | D) Hooks cannot modify inputs
- **Correct**: B
- **Explanation**: PreToolUse 钩子可以在 stdout 上输出带 `"updatedInput": {...}` 的 JSON（退出代码0），以在 Claude 使用参数之前修改它们。
- **Review**: PreToolUse 输出部分

### Q5
- **Category**: 概念
- **Question**: 哪个钩子事件支持 `CLAUDE_ENV_FILE` 以将环境变量持久化到会话中？
- **Options**: A) PreToolUse | B) UserPromptSubmit | C) SessionStart | D) All events
- **Correct**: C
- **Explanation**: 只有 SessionStart 钩子可以使用 `CLAUDE_ENV_FILE` 将环境变量持久化到会话中。
- **Review**: SessionStart 部分

### Q6
- **Category**: 实践
- **Question**: 你想要一个只在技能首次加载时运行一次、而不是每次工具调用都运行的钩子。需要添加什么字段？
- **Options**: A) `run-once: true` | B) `once: true` in the component hook definition | C) `single: true` | D) `max-runs: 1`
- **Correct**: B
- **Explanation**: 组件范围的钩子（在 SKILL.md 或代理 frontmatter 中定义）支持 `once: true`，仅在首次激活时运行。
- **Review**: 组件范围钩子部分

### Q7
- **Category**: 概念
- **Question**: Stop 钩子定义在子代理的 frontmatter 中。它会自动转换为什么？
- **Options**: A) A PostToolUse hook | B) A SubagentStop hook | C) A SessionEnd hook | D) It stays as a Stop hook
- **Correct**: B
- **Explanation**: 当 Stop 钩子放在子代理的 frontmatter 中时，它会自动转换为 SubagentStop，以便在该特定子代理完成时运行。
- **Review**: 组件范围钩子部分

### Q8
- **Category**: 实践
- **Question**: 如何匹配来自特定服务器的所有 MCP 工具？
- **Options**: A) `matcher: "mcp_github"` | B) `matcher: "mcp__github__.*"` (regex pattern) | C) `matcher: "mcp:github:*"` | D) `matcher: "github-mcp"`
- **Correct**: B
- **Explanation**: 匹配器使用正则表达式模式。MCP 工具遵循 `mcp__server__tool` 命名约定，因此 `mcp__github__.*` 匹配所有 GitHub MCP 工具。
- **Review**: 匹配器模式部分

### Q9
- **Category**: 概念
- **Question**: Claude Code 总共支持多少个钩子事件？
- **Options**: A) 10 | B) 16 | C) 25 | D) 30
- **Correct**: C
- **Explanation**: Claude Code 支持25个钩子事件：PreToolUse、PostToolUse、PostToolUseFailure、UserPromptSubmit、Stop、StopFailure、SubagentStop、SubagentStart、PermissionRequest、Notification、PreCompact、PostCompact、SessionStart、SessionEnd、WorktreeCreate、WorktreeRemove、ConfigChange、CwdChanged、FileChanged、TeammateIdle、TaskCompleted、TaskCreated、Elicitation、ElicitationResult、InstructionsLoaded。
- **Review**: 钩子事件表

### Q10
- **Category**: 实践
- **Question**: 你想调试为什么钩子没有触发。最佳方法是什么？
- **Options**: A) Add print statements to the hook script | B) Use `--debug` flag and `Ctrl+O` for verbose mode | C) Check the system log | D) Hooks don't have debugging tools
- **Correct**: B
- **Explanation**: `--debug` 标志和 `Ctrl+O` 详细模式显示钩子执行详情，包括哪些钩子触发了、它们的输入和输出。
- **Review**: 调试部分

---

## 第07课：插件

### Q1
- **Category**: 概念
- **Question**: 插件的核心清单文件是什么，它在哪里？
- **Options**: A) `plugin.yaml` in the root directory | B) `.claude-plugin/plugin.json` | C) `package.json` with a "claude" key | D) `.claude/plugin.md`
- **Correct**: B
- **Explanation**: 插件清单位于 `.claude-plugin/plugin.json`，包含必填字段：name、description、version、author。
- **Review**: 插件定义结构部分

### Q2
- **Category**: 实践
- **Question**: 发布前如何在本地测试插件？
- **Options**: A) Use `/plugin test ./my-plugin` | B) Use `claude --plugin-dir ./my-plugin` | C) Use `claude plugin validate ./my-plugin` | D) Copy it to ~/.claude/plugins/
- **Correct**: B
- **Explanation**: `--plugin-dir` 标志从本地目录加载插件进行测试。它可以重复加载多个插件。
- **Review**: 测试部分

### Q3
- **Category**: 概念
- **Question**: 在插件钩子和 MCP 配置中引用插件安装目录的环境变量是什么？
- **Options**: A) `$PLUGIN_HOME` | B) `${CLAUDE_PLUGIN_ROOT}` | C) `$PLUGIN_DIR` | D) `${CLAUDE_PLUGIN_PATH}`
- **Correct**: B
- **Explanation**: `${CLAUDE_PLUGIN_ROOT}` 解析为插件的安装目录，在钩子和 MCP 配置中启用可移植的路径引用。
- **Review**: 插件目录结构部分

### Q4
- **Category**: 实践
- **Question**: 插件在 "pr-review" 插件中有一个名为 "check-security" 的命令。用户如何调用它？
- **Options**: A) `/check-security` | B) `/pr-review:check-security` | C) `/plugin pr-review check-security` | D) `/pr-review/check-security`
- **Correct**: B
- **Explanation**: 插件命令使用 `plugin-name:command-name` 命名空间来避免与用户命令和其他插件冲突。
- **Review**: 插件命令部分

### Q5
- **Category**: 概念
- **Question**: 插件可以捆绑哪些组件？
- **Options**: A) Only commands and settings | B) Commands, agents, skills, hooks, MCP servers, LSP config, settings, templates, scripts | C) Only commands, hooks, and MCP servers | D) Only skills and agents
- **Correct**: B
- **Explanation**: 插件可以捆绑：commands/、agents/、skills/、hooks/hooks.json、.mcp.json、.lsp.json、settings.json、templates/、scripts/、docs/、tests/。
- **Review**: 插件目录结构部分

### Q6
- **Category**: 实践
- **Question**: 如何从 GitHub 安装插件？
- **Options**: A) `claude plugin add github:username/repo` | B) `/plugin install github:username/repo` | C) `npm install @claude/username-repo` | D) `git clone` then `claude plugin register`
- **Correct**: B
- **Explanation**: 使用 `/plugin install github:username/repo` 直接从 GitHub 仓库安装。
- **Review**: 安装方法部分

### Q7
- **Category**: 概念
- **Question**: 插件中 `settings.json` 的 `agent` 键有什么作用？
- **Options**: A) Specifies authentication credentials | B) Sets the main thread agent for the plugin | C) Lists available subagents | D) Configures agent permissions
- **Correct**: B
- **Explanation**: 插件 settings.json 中的 `agent` 键指定当插件处于活动状态时用作主线程代理的代理定义。
- **Review**: 插件设置部分

### Q8
- **Category**: 实践
- **Question**: 如何管理插件生命周期（启用/禁用/更新）？
- **Options**: A) Edit a config file manually | B) Use `/plugin enable`, `/plugin disable`, `/plugin update plugin-name` | C) Use `claude plugin-manager` | D) Reinstall the plugin
- **Correct**: B
- **Explanation**: Claude Code 提供斜杠命令进行完整的生命周期管理：enable、disable、update、uninstall。
- **Review**: 安装方法部分

### Q9
- **Category**: 概念
- **Question**: 插件相对于独立技能/钩子/MCP 的主要优势是什么？
- **Options**: A) Plugins are faster | B) Single-command install, versioned, marketplace distribution, bundles everything together | C) Plugins have more permissions | D) Plugins work offline
- **Correct**: B
- **Explanation**: 插件将多个组件打包成一个可安装单元，具有版本控制、市场分发和自动更新功能 —— 而非手动设置独立组件。
- **Review**: 独立 vs 插件对比部分

### Q10
- **Category**: 实践
- **Question**: 插件钩子配置位于插件目录内的哪个位置？
- **Options**: A) `.claude-plugin/hooks.json` | B) `hooks/hooks.json` | C) `plugin.json` hooks section | D) `.claude/settings.json`
- **Correct**: B
- **Explanation**: 插件钩子在插件目录结构中的 `hooks/hooks.json` 中配置。
- **Review**: 插件钩子部分

---

## 第08课：检查点

### Q1
- **Category**: 概念
- **Question**: 检查点捕获哪四样东西？
- **Options**: A) Git commits, branches, tags, stashes | B) Messages, file modifications, tool usage history, session context | C) Code, tests, logs, configs | D) Inputs, outputs, errors, timing
- **Correct**: B
- **Explanation**: 检查点捕获对话消息、Claude 工具做出的文件修改、工具使用历史和会话上下文。
- **Review**: 概述部分

### Q2
- **Category**: 实践
- **Question**: 如何访问检查点浏览器？
- **Options**: A) Use `/checkpoints` command | B) Press `Esc + Esc` (double-escape) or use `/rewind` | C) Use `/history` command | D) Press `Ctrl+Z`
- **Correct**: B
- **Explanation**: 双转义（Esc+Esc）或 `/rewind` 命令打开检查点浏览器以选择恢复点。
- **Review**: 访问检查点部分

### Q3
- **Category**: 概念
- **Question**: 有多少个回退选项，它们是什么？
- **Options**: A) 3: Undo, Redo, Reset | B) 5: Restore code+conversation, Restore conversation, Restore code, Summarize from here, Never mind | C) 2: Full restore, Partial restore | D) 4: Code, Messages, Both, Cancel
- **Correct**: B
- **Explanation**: 5个选项是：恢复代码和对话（完全回滚）、仅恢复对话、仅恢复代码、从这里总结（压缩）、算了（取消）。
- **Review**: 回退选项部分

### Q4
- **Category**: 实践
- **Question**: 你在 Claude Code 中通过 Bash 使用了 `rm -rf temp/`，然后想回退。检查点会恢复这些文件吗？
- **Options**: A) Yes, checkpoints capture everything | B) No, Bash filesystem operations (rm, mv, cp) are not tracked by checkpoints | C) Only if you used the Edit tool instead | D) Only if autoCheckpoint was enabled
- **Correct**: B
- **Explanation**: 检查点仅跟踪 Claude 工具做出的文件更改（Write、Edit）。Bash 命令如 rm、mv、cp 在检查点跟踪之外操作。
- **Review**: 限制部分

### Q5
- **Category**: 概念
- **Question**: 检查点保留多长时间？
- **Options**: A) Until session ends | B) 7 days | C) 30 days | D) Indefinitely
- **Correct**: C
- **Explanation**: 检查点在会话之间保留最多30天，之后自动清理。
- **Review**: 检查点持久化部分

### Q6
- **Category**: 实践
- **Question**: 回退时的"从这里总结"有什么作用？
- **Options**: A) Deletes the conversation from that point | B) Compresses the conversation into an AI-generated summary while preserving the original in the transcript | C) Creates a bullet-point list of changes | D) Exports the conversation to a file
- **Correct**: B
- **Explanation**: Summarize 将对话压缩成更短的 AI 生成摘要。原始完整文本保存在记录文件中。
- **Review**: 总结选项部分

### Q7
- **Category**: 概念
- **Question**: 检查点何时自动创建？
- **Options**: A) Every 5 minutes | B) On every user prompt | C) Only when you manually save | D) After every tool use
- **Correct**: B
- **Explanation**: 自动检查点在每个用户提示时创建，捕获 Claude 处理请求之前的状态。
- **Review**: 自动检查点部分

### Q8
- **Category**: 实践
- **Question**: 如何禁用自动检查点创建？
- **Options**: A) Use `--no-checkpoints` flag | B) Set `autoCheckpoint: false` in settings | C) Delete the checkpoints directory | D) Checkpoints cannot be disabled
- **Correct**: B
- **Explanation**: 在配置中设置 `autoCheckpoint: false` 以禁用自动检查点创建（默认值为 true）。
- **Review**: 配置部分

### Q9
- **Category**: 概念
- **Question**: 检查点是 git 提交的替代品吗？
- **Options**: A) Yes, they're more powerful | B) No, they are complementary — checkpoints are session-scoped and expire, git is permanent and shareable | C) Yes, for small projects | D) Only in solo development
- **Correct**: B
- **Explanation**: 检查点是临时的（保留30天）、会话范围的、无法共享的。Git 提交是永久的、可审计的、可共享的。两者配合使用。
- **Review**: 与 git 集成部分

### Q10
- **Category**: 实践
- **Question**: 你想比较两种不同的方法。推荐的检查点工作流程是什么？
- **Options**: A) Create two separate sessions | B) Checkpoint before approach A, try it, rewind to checkpoint, try approach B, compare results | C) Use git branches instead | D) There's no good way to compare approaches
- **Correct**: B
- **Explanation**: 分支策略：在干净状态时设置检查点，尝试方法A，记录结果，回退到同一个检查点，尝试方法B。比较两个结果。
- **Review**: 工作流程模式部分

---

## 第09课：高级功能

### Q1
- **Category**: 概念
- **Question**: Claude Code 中有哪六种权限模式？
- **Options**: A) read, write, execute, admin, root, sudo | B) default, acceptEdits, plan, auto, dontAsk, bypassPermissions | C) safe, normal, elevated, admin, unrestricted, god | D) view, edit, run, deploy, full, bypass
- **Correct**: B
- **Explanation**: 六种模式是：default（提示所有操作）、acceptEdits（自动接受文件编辑）、plan（只读分析）、auto（后台分类器决定）、dontAsk（自动拒绝，除非预先批准）、bypassPermissions（跳过所有检查）。
- **Review**: 权限模式部分

### Q2
- **Category**: 实践
- **Question**: 如何激活规划模式？
- **Options**: A) Only via `/plan` command | B) Via `/plan`, `Shift+Tab`/`Alt+M`, `--permission-mode plan` flag, or default config | C) Via `--planning` flag only | D) Planning is always on
- **Correct**: B
- **Explanation**: 规划模式可以通过多种方式激活：/plan 命令、Shift+Tab/Alt+M 键盘快捷键、--permission-mode plan CLI 标志，或配置中的默认值。
- **Review**: 规划模式部分

### Q3
- **Category**: 概念
- **Question**: `opusplan` 模型别名有什么作用？
- **Options**: A) Uses only Opus for everything | B) Uses Opus for planning phase and Sonnet for implementation | C) Uses a special planning-optimized model | D) Enables plan mode automatically
- **Correct**: B
- **Explanation**: `opusplan` 是一个模型别名，在规划阶段使用 Opus（更高质量的分析），在执行阶段使用 Sonnet（更快的实现）。
- **Review**: 规划模式部分

### Q4
- **Category**: 实践
- **Question**: 如何在会话期间切换扩展思考？
- **Options**: A) Type `/think` | B) Press `Option+T` (macOS) or `Alt+T` | C) Use `--thinking` flag | D) It's always enabled and cannot be toggled
- **Correct**: B
- **Explanation**: Option+T（macOS）或 Alt+T 切换扩展思考。它对所有模型默认启用。Opus 4.6 支持自适应努力级别。
- **Review**: 扩展思考部分

### Q5
- **Category**: 概念
- **Question**: "think" 或 "ultrathink" 是激活增强思考的特殊关键词吗？
- **Options**: A) Yes, they activate deeper reasoning | B) No, they are treated as regular prompt text with no special behavior | C) Only "ultrathink" is special | D) They work only with Opus
- **Correct**: B
- **Explanation**: 文档明确说明这些是常规提示指令，不是特殊的激活关键词。扩展思考通过 Alt+T 切换和环境变量控制。
- **Review**: 扩展思考部分

### Q6
- **Category**: 实践
- **Question**: 如何在 CI/CD 管道中运行 Claude 并使用结构化 JSON 输出和回合限制？
- **Options**: A) `claude --ci --json --limit 3` | B) `claude -p --output-format json --max-turns 3 "review code"` | C) `claude --pipeline --format json` | D) `claude run --json --turns 3`
- **Correct**: B
- **Explanation**: 打印模式（`-p`）配合 `--output-format json` 和 `--max-turns` 是标准的 CI/CD 集成模式。
- **Review**: 无头/打印模式部分

### Q7
- **Category**: 概念
- **Question**: 任务列表功能（Ctrl+T）提供什么？
- **Options**: A) A list of running background processes | B) A persistent to-do list that survives context compaction, shareable via `CLAUDE_CODE_TASK_LIST_ID` | C) A history of past sessions | D) A queue of pending tool calls
- **Correct**: B
- **Explanation**: 任务列表（Ctrl+T）在上下文压缩后持续存在，可以通过命名任务目录通过 `CLAUDE_CODE_TASK_LIST_ID` 在会话之间共享。
- **Review**: 任务列表部分

### Q8
- **Category**: 实践
- **Question**: 在规划模式期间如何在外部编辑器（你喜欢的编辑器）中编辑计划？
- **Options**: A) Copy-paste from the terminal | B) Press `Ctrl+G` to open the plan in an external editor | C) Use `/export-plan` command | D) Plans can't be edited externally
- **Correct**: B
- **Explanation**: Ctrl+G 在配置的外部编辑器中打开当前计划以进行修改。
- **Review**: 规划模式部分

### Q9
- **Category**: 概念
- **Question**: `dontAsk` 和 `bypassPermissions` 模式有什么区别？
- **Options**: A) They are the same | B) `dontAsk` auto-denies unless pre-approved; `bypassPermissions` skips all checks entirely | C) `dontAsk` is for files; `bypassPermissions` is for commands | D) `bypassPermissions` is safer
- **Correct**: B
- **Explanation**: dontAsk 自动拒绝权限请求，除非匹配预先批准的规则。bypassPermissions 完全跳过所有安全检查 —— 它对于常规使用是危险的。
- **Review**: 权限模式部分

### Q10
- **Category**: 实践
- **Question**: 如何将 CLI 会话交接给桌面应用？
- **Options**: A) Use `/export` command | B) Use `/desktop` command | C) Copy the session ID and paste in the app | D) Sessions can't transfer between CLI and desktop
- **Correct**: B
- **Explanation**: `/desktop` 命令将当前 CLI 会话交接给原生桌面应用程序，以进行可视化 diff 审查和多会话管理。
- **Review**: 桌面应用部分

---

## 第10课：CLI 参考

### Q1
- **Category**: 概念
- **Question**: Claude CLI 的两种主要模式是什么？
- **Options**: A) Online and offline mode | B) Interactive REPL (`claude`) and Print mode (`claude -p`) | C) GUI and terminal mode | D) Single and batch mode
- **Correct**: B
- **Explanation**: 交互式 REPL 是默认的对话模式。打印模式（-p）是非交互式的、可脚本化的、可管道的 —— 它在一次响应后退出。
- **Review**: CLI 架构部分

### Q2
- **Category**: 实践
- **Question**: 如何将文件通过管道输入 Claude 并获取 JSON 输出？
- **Options**: A) `claude --file error.log --json` | B) `cat error.log | claude -p --output-format json "explain this"` | C) `claude < error.log --format json` | D) `claude -p --input error.log --json`
- **Correct**: B
- **Explanation**: 通过 stdin 将内容通过管道传递到打印模式（-p），并使用 --output-format json 获取结构化输出。
- **Review**: 交互模式 vs 打印模式部分

### Q3
- **Category**: 概念
- **Question**: `-c` 和 `-r` 标志有什么区别？
- **Options**: A) Both do the same thing | B) `-c` continues the most recent session; `-r` resumes by name or ID | C) `-c` creates a new session; `-r` resumes | D) `-c` is for code; `-r` is for review
- **Correct**: B
- **Explanation**: `-c/--continue` 恢复最近的对话。`-r/--resume "name"` 按名称或会话 ID 恢复特定会话。
- **Review**: 会话管理部分

### Q4
- **Category**: 实践
- **Question**: 如何保证从 Claude 获得符合 schema 的 JSON 输出？
- **Options**: A) Just use `--output-format json` | B) Use `--output-format json --json-schema '{"type":"object",...}'` | C) Use `--strict-json` flag | D) JSON output is always schema-valid
- **Correct**: B
- **Explanation**: 单独使用 `--output-format json` 会产生尽力而为的 JSON。添加 `--json-schema` 和 JSON Schema 定义可以保证输出符合 schema。
- **Review**: 输出和格式部分

### Q5
- **Category**: 概念
- **Question**: 哪个标志只在打印模式（-p）下有效，在交互模式下无效？
- **Options**: A) `--model` | B) `--system-prompt-file` | C) `--verbose` | D) `--max-turns`
- **Correct**: B
- **Explanation**: `--system-prompt-file` 从文件加载系统提示，但只在打印模式下有效。在交互式会话中使用 `--system-prompt`（内联字符串）。
- **Review**: 系统提示标志对比表

### Q6
- **Category**: 实践
- **Question**: 如何限制 Claude 仅使用只读工具进行安全审计？
- **Options**: A) `claude --read-only "audit code"` | B) `claude --permission-mode plan --tools "Read,Grep,Glob" "audit code"` | C) `claude --safe-mode "audit code"` | D) `claude --no-write "audit code"`
- **Correct**: B
- **Explanation**: 结合 `--permission-mode plan`（只读分析）和 `--tools`（特定工具的白名单）来限制 Claude 只能进行只读操作。
- **Review**: 工具和权限管理部分

### Q7
- **Category**: 概念
- **Question**: 代理定义的优先级顺序是什么？
- **Options**: A) Project > User > CLI | B) CLI > User > Project | C) User > CLI > Project | D) All are equal priority
- **Correct**: B
- **Explanation**: CLI 定义的代理（--agents 标志）优先级最高，然后是用户级（~/.claude/agents/），最后是项目级（.claude/agents/）。
- **Review**: 代理配置部分

### Q8
- **Category**: 实践
- **Question**: 如何分叉现有会话以尝试不同方法而不丢失原始会话？
- **Options**: A) Use `/fork` command | B) Use `--resume session-name --fork-session "branch name"` | C) Use `--clone session-name` | D) Use `/branch session-name`
- **Correct**: B
- **Explanation**: `--resume` 配合 `--fork-session` 从恢复的会话创建一个新的独立分支，保留原始对话。
- **Review**: 会话管理部分

### Q9
- **Category**: 概念
- **Question**: 当用户已登录时，`claude auth status` 返回什么退出代码？
- **Options**: A) 1 | B) 0 | C) 200 | D) It doesn't return an exit code
- **Correct**: B
- **Explanation**: `claude auth status` 在已登录时以代码0退出，未登录时以代码1退出。这使其可用于 CI/CD 身份验证检查的脚本编写。
- **Review**: CLI 命令表

### Q10
- **Category**: 实践
- **Question**: 如何用 Claude 批量处理多个文件？
- **Options**: A) `claude --batch *.md` | B) Use a for loop: `for file in *.md; do claude -p "summarize: $(cat $file)" > ${file%.md}.json; done` | C) `claude -p --files *.md "summarize all"` | D) Batch processing is not supported
- **Correct**: B
- **Explanation**: 在打印模式下使用 shell for 循环处理文件。每次调用是独立的，可以产生结构化输出。
- **Review**: 批处理部分
