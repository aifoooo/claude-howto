<picture>
  <source media="(prefers-color-scheme: dark)" srcset="resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">
</picture>

# 优秀资源列表

## 官方文档

| 资源 | 描述 | 链接 |
|----------|-------------|------|
| Claude Code Docs | 官方 Claude Code 文档 | [code.claude.com/docs/en/overview](https://code.claude.com/docs/en/overview) |
| Anthropic Docs | 完整 Anthropic 文档 | [docs.anthropic.com](https://docs.anthropic.com) |
| MCP Protocol | Model Context Protocol 规范 | [modelcontextprotocol.io](https://modelcontextprotocol.io) |
| MCP Servers | 官方 MCP 服务器实现 | [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| Anthropic Cookbook | 代码示例和教程 | [github.com/anthropics/anthropic-cookbook](https://github.com/anthropics/anthropic-cookbook) |
| Claude Code Skills | 社区 skills 仓库 | [github.com/anthropics/skills](https://github.com/anthropics/skills) |
| Agent Teams | 多代理协调与协作 | [code.claude.com/docs/en/agent-teams](https://code.claude.com/docs/en/agent-teams) |
| Scheduled Tasks | 使用 /loop 和 cron 的定期任务 | [code.claude.com/docs/en/scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks) |
| Chrome Integration | 浏览器自动化 | [code.claude.com/docs/en/chrome](https://code.claude.com/docs/en/chrome) |
| Keybindings | 键盘快捷键自定义 | [code.claude.com/docs/en/keybindings](https://code.claude.com/docs/en/keybindings) |
| Desktop App | 原生桌面应用程序 | [code.claude.com/docs/en/desktop](https://code.claude.com/docs/en/desktop) |
| Remote Control | 远程会话控制 | [code.claude.com/docs/en/remote-control](https://code.claude.com/docs/en/remote-control) |
| Auto Mode | 自动权限管理 | [code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions) |
| Channels | 多渠道通信 | [code.claude.com/docs/en/channels](https://code.claude.com/docs/en/channels) |
| Voice Dictation | Claude Code 语音输入 | [code.claude.com/docs/en/voice-dictation](https://code.claude.com/docs/en/voice-dictation) |

## Anthropic 工程博客

| 文章 | 描述 | 链接 |
|---------|-------------|------|
| Code Execution with MCP | 如何使用代码执行解决 MCP 上下文膨胀 - 98.7% token 减少 | [anthropic.com/engineering/code-execution-with-mcp](https://www.anthropic.com/engineering/code-execution-with-mcp) |

---

## 30 分钟掌握 Claude Code

_视频_：https://www.youtube.com/watch?v=6eBSHbLKuN0

_**所有技巧**_
- **探索高级功能和快捷键**
  - 定期在发布说明中查看 Claude 的新代码编辑和上下文功能。
  - 学习键盘快捷键以快速在聊天、文件和编辑器视图之间切换。

- **高效设置**
  - 使用清晰的名称/描述创建项目特定会话，以便于检索。
  - 固定最常用的文件或文件夹，以便 Claude 可以随时访问它们。
  - 设置 Claude 的集成（例如 GitHub、流行 IDE）以简化编码流程。

- **有效的代码库问答**
  - 向 Claude 询问有关架构、设计模式和特定模块的详细问题。
  - 在问题中使用文件和行引用（例如" `app/models/user.py` 中的逻辑是做什么的？"）。
  - 对于大型代码库，提供摘要或清单以帮助 Claude 集中注意力。
  - **示例提示**：_"你能解释一下 `src/auth/AuthService.ts:45-120` 中实现的身份验证流程吗？它如何与 `src/middleware/auth.ts` 中的中间件集成？"_

- **代码编辑和重构**
  - 使用代码块内的内联注释或请求来获得集中编辑（"重构此函数以提高清晰度"）。
  - 要求并排比较前后。
  - 让 Claude 在重大编辑后生成测试或文档以确保质量。
  - **示例提示**：_"重构 `api/users.js` 中的 `getUserData` 函数，使用 async/await 而不是 promises。向我展示前后对比，并为重构后的版本生成单元测试。"_

- **上下文管理**
  - 将粘贴的代码/上下文限制为仅与当前任务相关的内容。
  - 使用结构化提示（"这里是文件 A，这里是函数 B，我的问题是 X"）以获得最佳性能。
  - 删除或折叠提示窗口中的大文件以避免超出上下文限制。
  - **示例提示**：_"这里是 `models/User.js` 中的 User 模型和 `utils/validation.js` 中的 `validateUser` 函数。我的问题是：如何在保持向后兼容性的同时添加电子邮件验证？"_

- **集成团队工具**
  - 将 Claude 会话连接到团队的仓库和文档。
  - 使用内置模板或为重复性工程任务创建自定义模板。
  - 通过与队友共享会话记录和提示进行协作。

- **提升性能**
  - 给出清晰、目标导向的指令（例如"用五点概括这个类"）。
  - 从上下文窗口中修剪不必要的注释和样板。
  - 如果 Claude 的输出偏离轨道，重置上下文或重新措辞问题以获得更好的对齐。
  - **示例提示**：_"用五点概括 `src/db/Manager.ts` 中的 `DatabaseManager` 类，重点关注其主要职责和关键方法。"_

- **实际使用示例**
  - 调试：粘贴错误和堆栈跟踪，然后询问可能的原因和修复方法。
  - 测试生成：为复杂逻辑请求基于属性的单元测试或集成测试。
  - 代码审查：让 Claude 识别有风险的更改、边缘情况或代码味道。
  - **示例提示**：
    - _"我收到这个错误：'TypeError: Cannot read property 'map' of undefined at line 42 in components/UserList.jsx'。这是堆栈跟踪和相关代码。是什么原因，我该如何修复？"_
    - _"为 `PaymentProcessor` 类生成全面的单元测试，包括失败交易、超时和无效输入的边缘情况。"_
    - _"审查此拉取请求差异，识别潜在的安全问题、性能瓶颈和代码味道。"_

- **工作流自动化**
  - 使用 Claude 提示编写重复性任务（如格式化、清理和重复重命名）的脚本。
  - 使用 Claude 根据代码差异起草 PR 描述、发布说明或文档。
  - **示例提示**：_"根据 git diff，创建一个详细的 PR 描述，包括更改摘要、修改文件列表、测试步骤和潜在影响。同时为 2.3.0 版本生成发布说明。"_

**提示**：为获得最佳效果，结合这些实践 - 首先固定关键文件并总结目标，然后使用集中提示和 Claude 的重构工具逐步改进代码库和自动化。

---

**推荐使用 Claude Code 的工作流**

### 推荐使用 Claude Code 的工作流

#### 对于新仓库

1. **初始化仓库和 Claude 集成**
   - 使用基本结构设置新仓库：README、LICENSE、.gitignore、根配置。
   - 创建 `CLAUDE.md` 文件，描述架构、高级目标和编码指南。
   - 安装 Claude Code 并将其链接到您的仓库，以获取代码建议、测试脚手架和工作流自动化。

2. **使用计划模式和规格**
   - 在实现功能之前，使用计划模式（`shift-tab` 或 `/plan`）起草详细规格。
   - 向 Claude 询问架构建议和初始项目布局。
   - 保持清晰、目标导向的提示序列 - 询问组件大纲、主要模块和职责。

3. **迭代开发和审查**
   - 以小块方式实现核心功能，提示 Claude 进行代码生成、重构和文档编写。
   - 每次增量后请求单元测试和示例。
   - 在 CLAUDE.md 中维护运行任务列表。

4. **自动化 CI/CD 和部署**
   - 使用 Claude 搭建 GitHub Actions、npm/yarn 脚本或部署工作流。
   - 通过更新 CLAUDE.md 并请求相应的命令/脚本，轻松调整管道。

```mermaid
graph TD
    A[Start New Repository] --> B[Initialize Repository Structure]
    B --> C[Create README, LICENSE, .gitignore]
    C --> D[Create CLAUDE.md]
    D --> E[Document Architecture & Guidelines]
    E --> F[Install & Link Claude Code]

    F --> G[Enter Plan Mode]
    G --> H[Draft Feature Specification]
    H --> I[Get Architecture Suggestions]
    I --> J[Define Components & Modules]

    J --> K[Implement Feature Chunk]
    K --> L[Generate Code with Claude]
    L --> M[Request Unit Tests]
    M --> N[Review & Refactor]
    N --> O{More Features?}
    O -->|Yes| K
    O -->|No| P[Update Task List in CLAUDE.md]

    P --> Q[Setup CI/CD Pipeline]
    Q --> R[Scaffold GitHub Actions]
    R --> S[Create Deployment Scripts]
    S --> T[Test Automation]
    T --> U[Repository Ready]

    style A fill:#e1f5ff
    style G fill:#fff4e1
    style K fill:#f0ffe1
    style Q fill:#ffe1f5
    style U fill:#90EE90
```

#### 对于现有仓库

1. **仓库和上下文设置**
   - 添加或更新 `CLAUDE.md` 以记录仓库结构、编码模式和关键文件。对于旧仓库，使用 `CLAUDE_LEGACY.md` 涵盖框架、版本映射、说明、bug 和升级说明。
   - 固定或突出显示 Claude 应用于上下文的主要文件。

2. **上下文代码问答**
   - 向 Claude 询问代码审查、bug 解释、重构或迁移计划，引用特定文件/函数。
   - 给 Claude 明确的边界（例如"仅修改这些文件"或"无新依赖"）。

3. **分支、Worktree 和多会话管理**
   - 对隔离的功能或 bug 修复使用多个 git worktree，并为每个 worktree 启动单独的 Claude 会话。
   - 通过分支或功能组织终端标签/窗口，以实现并行工作流。

4. **团队工具和自动化**
   - 通过 `.claude/commands/` 同步自定义命令，以实现跨团队一致性。
   - 通过 Claude 的斜杠命令或钩子自动执行重复性任务、PR 创建和代码格式化。
   - 与团队成员共享会话和上下文，以进行协作故障排除和审查。

```mermaid
graph TD
    A[Start with Existing Repository] --> B{Legacy Codebase?}
    B -->|Yes| C[Create CLAUDE_LEGACY.md]
    B -->|No| D[Create/Update CLAUDE.md]
    C --> E[Document Frameworks & Version Maps]
    D --> F[Document Structure & Patterns]
    E --> G[Pin Key Files for Context]
    F --> G

    G --> H[Identify Task Type]
    H --> I{Task Category}
    I -->|Bug Fix| J[Ask Claude for Bug Analysis]
    I -->|Code Review| K[Request Code Review]
    I -->|Refactor| L[Plan Refactoring Strategy]
    I -->|Migration| M[Create Migration Plan]

    J --> N[Set Explicit Boundaries]
    K --> N
    L --> N
    M --> N

    N --> O{Multiple Features?}
    O -->|Yes| P[Create Git Worktrees]
    O -->|No| Q[Work on Main Branch]
    P --> R[Launch Separate Claude Sessions]
    R --> S[Organize Terminal Tabs]
    Q --> S

    S --> T[Setup Team Automation]
    T --> U[Sync .claude/commands/]
    U --> V[Configure Slash Commands]
    V --> W[Setup Hooks for Automation]
    W --> X[Share Session Context with Team]

    X --> Y{More Tasks?}
    Y -->|Yes| H
    Y -->|No| Z[Workflow Complete]

    style A fill:#e1f5ff
    style C fill:#ffecec
    style D fill:#fff4e1
    style P fill:#f0ffe1
    style T fill:#ffe1f5
    style Z fill:#90EE90
```

**提示**：
- 每个新功能或修复从规格和计划模式提示开始。
- 对于旧仓库和复杂仓库，在 CLAUDE.md/CLAUDE_LEGACY.md 中存储详细指导。
- 给出清晰、集中的指示，并将复杂工作分解为多阶段计划。
- 定期清理会话、修剪上下文并删除已完成的 worktree 以避免混乱。

这些步骤捕获了在新的和现有代码库中使用 Claude Code 顺利进行工作流的核心建议。

---

## 新功能和功能（2026 年 3 月）

### 关键功能资源

| 功能 | 描述 | 了解更多 |
|---------|-------------|------------|
| **Auto Memory** | Claude 自动跨会话学习和记住您的偏好 | [Memory Guide](02-memory/) |
| **Remote Control** | 从外部工具和脚本编程控制 Claude Code 会话 | [Advanced Features](09-advanced-features/) |
| **Web Sessions** | 通过基于浏览器的界面访问 Claude Code，用于远程开发 | [CLI Reference](10-cli/) |
| **Desktop App** | Claude Code 的原生桌面应用程序，增强 UI | [Claude Code Docs](https://code.claude.com/docs/en/desktop) |
| **Extended Thinking** | 通过 `Alt+T`/`Option+T` 或 `MAX_THINKING_TOKENS` 环境变量进行深度推理切换 | [Advanced Features](09-advanced-features/) |
| **Permission Modes** | 细粒度控制：default、acceptEdits、plan、auto、dontAsk、bypassPermissions | [Advanced Features](09-advanced-features/) |
| **7-Tier Memory** | 托管策略、项目、项目规则、用户、用户规则、本地、自动记忆 | [Memory Guide](02-memory/) |
| **Hook Events** | 25 个事件：PreToolUse、PostToolUse、PostToolUseFailure、Stop、StopFailure、SubagentStart、SubagentStop、Notification、Elicitation 等 | [Hooks Guide](06-hooks/) |
| **Agent Teams** | 协调多个代理共同处理复杂任务 | [Subagents Guide](04-subagents/) |
| **Scheduled Tasks** | 使用 `/loop` 和 cron 工具设置定期任务 | [Advanced Features](09-advanced-features/) |
| **Chrome Integration** | 使用无头 Chromium 进行浏览器自动化 | [Advanced Features](09-advanced-features/) |
| **Keyboard Customization** | 自定义键绑定，包括和弦序列 | [Advanced Features](09-advanced-features/) |
