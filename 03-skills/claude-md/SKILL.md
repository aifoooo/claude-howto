---
name: claude-md
description: 按照最佳实践创建或更新 CLAUDE.md 文件，实现最佳的 AI 代理 onboarding
---

## 用户输入

```text
$ARGUMENTS
```

在继续之前你**必须**考虑用户输入（如果非空）。用户可以指定：
- `create` - 从头创建新的 CLAUDE.md
- `update` - 改进现有 CLAUDE.md
- `audit` - 分析并报告当前 CLAUDE.md 质量
- 特定路径以创建/更新（如 `src/api/CLAUDE.md` 用于目录级指令）

## 核心原则

**LLM 是无状态的**：CLAUDE.md 是每个对话自动包含的唯一文件。它作为 AI 代理进入你的代码库的主要 onboarding 文档。

### 黄金法则

1. **少即是多**：前沿 LLM 可以遵循约 150-200 条指令。Claude Code 的系统提示已经使用约 50 条。保持你的 CLAUDE.md 聚焦和简洁。

2. **普遍适用性**：只包含与每个会话相关的信息。特定任务的指令应放在单独的文件中。

3. **不要用 Claude 作为 Linter**：风格指南会膨胀上下文并降低指令遵循能力。使用确定性工具（prettier、eslint 等）代替。

4. **绝不自动生成**：CLAUDE.md 是 AI harness 的最高杠杆点。手工精心制作，考虑清楚。

## 执行流程

### 1. 项目分析

首先，分析当前项目状态：

1. 检查现有 CLAUDE.md 文件：
   - 根目录：`. /CLAUDE.md` 或 `.claude/CLAUDE.md`
   - 目录级：`**/CLAUDE.md`
   - 全局用户配置：`~/.claude/CLAUDE.md`

2. 识别项目结构：
   - 技术栈（语言、框架）
   - 项目类型（monorepo、单应用、库）
   - 开发工具（包管理器、构建系统、测试运行器）

3. 审查现有文档：
   - README.md
   - CONTRIBUTING.md
   - package.json、pyproject.toml、Cargo.toml 等

### 2. 内容策略（WHAT、WHY、HOW）

围绕三个维度组织 CLAUDE.md：

#### WHAT - 技术与结构
- 技术栈概览
- 项目组织（对 monorepo 尤其重要）
- 关键目录及其用途

#### WHY - 目的与上下文
- 项目做什么
- 为什么要做某些架构决策
- 每个主要组件负责什么

#### HOW - 工作流与约定
- 开发工作流（bun vs node、pip vs uv 等）
- 测试程序和命令
- 验证和构建方法
- 关键"陷阱"或非显而易见的 requirements

### 3. 渐进式披露策略

对于较大的项目，建议创建 `agent_docs/` 文件夹：

```
agent_docs/
  |- building_the_project.md
  |- running_tests.md
  |- code_conventions.md
  |- architecture_decisions.md
```

在 CLAUDE.md 中，用以下指令引用这些文件：
```markdown
详细构建说明，请参阅 `agent_docs/building_the_project.md`
```

**重要**：使用 `file:line` 引用而不是代码片段，以避免过时的上下文。

### 4. 质量约束

创建或更新 CLAUDE.md 时：

1. **目标长度**：300 行以内（最好 100 行以内）
2. **无风格规则**：删除任何 linting/格式指令
3. **无特定任务指令**：移到单独文件
4. **无代码片段**：使用文件引用代替
5. **无冗余信息**：不要重复 package.json 或 README 中的内容

### 5. 必需部分

结构良好的 CLAUDE.md 应包含：

```markdown
# 项目名称

简要的一行描述。

## 技术栈
- 主要语言和版本
- 关键框架/库
- 数据库/存储（如有）

## 项目结构
[仅适用于 monorepo 或复杂结构]
- `apps/` - 应用入口点
- `packages/` - 共享库

## 开发命令
- 安装：`command`
- 测试：`command`
- 构建：`command`

## 关键约定
[仅限不明显的、高影响的约定]
- 约定 1 + 简要说明
- 约定 2 + 简要说明

## 已知问题 / 陷阱
[总是绊倒开发者的事项]
- 问题 1
- 问题 2
```

### 6. 应避免的反模式

**不要包含：**
- 代码风格指南（使用 linters）
- 关于如何使用 Claude 的文档
- 显而易见模式的长解释
- 复制粘贴的代码示例
- 通用的最佳实践（"编写干净代码"）
- 特定任务的指令
- 自动生成的内容
- 冗长的 TODO 列表

### 7. 验证检查清单

定稿前，验证：

- [ ] 300 行以内（最好 100 行以内）
- [ ] 每行适用于所有会话
- [ ] 无风格/格式规则
- [ ] 无代码片段（使用文件引用）
- [ ] 命令经验证可用
- [ ] 复杂项目使用渐进式披露
- [ ] 记录了关键陷阱
- [ ] 与 README.md 无冗余

## 输出格式

### 对于 `create` 或默认：

1. 分析项目
2. 按照上面的结构起草 CLAUDE.md
3. 展示草稿供审查
4. 批准后写入适当位置

### 对于 `update`：

1. 读取现有 CLAUDE.md
2. 对照最佳实践审查
3. 识别：
   - 要删除的内容（风格规则、代码片段、特定任务）
   - 要精简的内容
   - 缺失的基本信息
4. 展示更改供审查
5. 批准后应用更改

### 对于 `audit`：

1. 读取现有 CLAUDE.md
2. 生成报告，包含：
   - 当前行数 vs 目标
   - 普遍适用内容的百分比
   - 发现的反模式列表
   - 改进建议
3. 不修改文件，仅报告

## AGENTS.md 处理

如果用户请求 AGENTS.md 创建/更新：

AGENTS.md 用于定义专业代理行为。与 CLAUDE.md（用于项目上下文）不同，AGENTS.md 定义：
- 自定义代理角色和能力
- 代理特定指令和约束
- 多代理场景的工作流定义

应用类似原则：
- 保持聚焦和简洁
- 使用渐进式披露
- 引用外部文档而非嵌入内容

## 注意事项

- 在包含命令之前始终验证它们可用
- 如有疑问，删掉它——少即是多
- 系统提示告诉 Claude CLAUDE.md"可能相关也可能不相关"——噪音越多，越容易被忽略
- Monorepo 最受益于清晰的 WHAT/WHY/HOW 结构
- 目录级 CLAUDE.md 文件应该更加聚焦
