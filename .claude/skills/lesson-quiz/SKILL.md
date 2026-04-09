---
name: lesson-quiz
version: 1.0.0
description: Interactive lesson-level quiz for Claude Code tutorials. Tests understanding of a specific lesson (01-10) with 8-10 questions mixing conceptual and practical knowledge. Use before a lesson to pre-test, during to check progress, or after to verify mastery. Use when asked to "quiz me on hooks", "test my knowledge of lesson 3", "lesson quiz", "practice quiz for MCP", or "do I understand skills".
---

# 课程测验

交互式测验，通过 8-10 个问题测试对特定 Claude Code 课程的理解，提供每个问题的反馈，并识别需要复习的领域。

## 说明

### 步骤 1：确定课程

如果用户提供了课程作为参数（例如 `/lesson-quiz hooks` 或 `/lesson-quiz 03`），请将其映射到课程目录：

**课程映射：**
- `01`、`slash-commands`、`commands` → 01-slash-commands
- `02`、`memory` → 02-memory
- `03`、`skills` → 03-skills
- `04`、`subagents`、`agents` → 04-subagents
- `05`、`mcp` → 05-mcp
- `06`、`hooks` → 06-hooks
- `07`、`plugins` → 07-plugins
- `08`、`checkpoints`、`checkpoint` → 08-checkpoints
- `09`、`advanced`、`advanced-features` → 09-advanced-features
- `10`、`cli` → 10-cli

如果未提供参数，请使用 AskUserQuestion 呈现选择提示：

**问题 1**（标题："课程"）：
"你想测试哪一课？"
选项：
1. "斜杠命令 (01)" — 自定义命令、技能、frontmatter、参数
2. "记忆 (02)" — CLAUDE.md、记忆层次、规则、自动记忆
3. "技能 (03)" — 渐进式披露、自动调用、SKILL.md
4. "子代理 (04)" — 任务委托、代理配置、隔离

**问题 2**（标题："课程"）：
"你想测试哪一课？（续）"
选项：
1. "MCP (05)" — 外部集成、传输、服务器、工具搜索
2. "钩子 (06)" — 事件自动化、PreToolUse、退出码、JSON I/O
3. "插件 (07)" — 捆绑解决方案、市场、plugin.json
4. "更多课程..." — 检查点、高级功能、CLI

如果选择了"更多课程..."，请呈现：

**问题 3**（标题："课程"）：
"选择你的课程："
选项：
1. "检查点 (08)" — 回退、恢复、安全实验
2. "高级功能 (09)" — 规划、权限、打印模式、思考
3. "CLI 参考 (10)" — 标志、输出格式、脚本、管道

### 步骤 2：阅读课程内容

阅读课程 README.md 文件以刷新上下文：
- 阅读文件：`<lesson-directory>/README.md`

然后使用该课程的 `references/question-bank.md` 中的题库。题库为每课提供 10 道预写的问题，包含正确答案和解释。

### 步骤 3：呈现测验

询问用户测验时间上下文：

使用 AskUserQuestion（标题："时间"）：
"相对于课程，你什么时候进行这个测验？"
选项：
1. "之前（预测试）" — 我还没有阅读课程，测试我的先验知识
2. "期间（进度检查）" — 我正在学习课程中
3. "之后（掌握检查）" — 我已完成课程，想验证理解

此上下文影响结果的呈现方式（见步骤 5）。

### 步骤 4：分轮呈现问题

每轮呈现 2 个问题，共 5 轮（10 个问题）。每个问题使用 AskUserQuestion，包含问题文本和 3-4 个答案选项。

**重要**：每个问题使用 AskUserQuestion，最多 4 个选项，每轮 2 个问题。

每轮呈现 2 个问题。5 轮结束后，进入评分。

**每轮问题格式：**

题库中的每个问题包含：
- `question`：问题文本
- `options`：3-4 个答案选项（一个正确，在题库中标注）
- `correct`：正确答案标签
- `explanation`：为什么答案正确
- `category`："conceptual" 或 "practical"

使用 AskUserQuestion 呈现每个问题。记录用户的答案。

### 步骤 5：评分并呈现结果

所有轮次结束后，计算分数并呈现结果。

**评分：**
- 每个正确答案 = 1 分
- 总分 = 10 分

**等级量表：**
- 9-10：已掌握 — 理解优秀
- 7-8：熟练 — 掌握良好，有小缺口
- 5-6：发展中 — 理解基础，需要复习
- 3-4：起步 — 显著缺口，建议复习
- 0-2：尚未开始 — 从本课开头重新开始

**输出格式：**

```markdown
## 课程测验结果：[课程名称]

**分数：N/10** — [等级标签]
**测验时间**：课程 [之前/期间/之后]
**问题分解**：N 道概念题正确，N 道实践题正确

### 每题结果

| # | 类别 | 问题（简略）| 你的答案 | 结果 |
|---|----------|-----------------|-------------|--------|
| 1 | 概念 | [简略问题] | [他们的答案] | [正确/错误] |
| 2 | 实践 | ... | ... | ... |
| ... | ... | ... | ... | ... |

### 错误答案 — 复习这些

[对于每个错误答案，显示：]

**Q[N]：[完整问题文本]**
- 你的答案：[他们选择的]
- 正确答案：[正确选项]
- 解释：[为什么正确]
- 复习：[要重新阅读的课程 README 的具体章节]

### [时间特定消息]

[如果是预测试]：
**预测试分数：N/10。** 这为你提供了一个基准！将学习重点放在你错过的主题上。完成课程后，重新参加测验以衡量你的进步。

[如果是期间]：
**进度检查：N/10。** [如果是 7+：进步很大——继续加油！如果是 4-6：在继续之前复习错误的主题。如果是 <4：考虑从头重新阅读。]

[如果是之后]：
**掌握检查：N/10。** [如果是 9-10：你已掌握本课！继续下一课。如果是 7-8：快到了——复习错过的题目并重新测试。如果是 <7：在本课上多花时间，特别是上面标记的章节。]

### 建议的后续步骤

[根据分数和时间：]
- [如果已掌握]：继续学习路线图中的下一课：[下一课链接]
- [如果熟练]：复习这些具体章节，然后重新测试：[列出章节]
- [如果是发展中或以下]：重新阅读完整课程：[课程链接]。重点关注：[列出薄弱类别]
- [提供]："你想重新测试、测试其他课程，还是获得特定主题的帮助？"
```

### 步骤 6：提供后续选项

呈现结果后，使用 AskUserQuestion：

"你想接下来做什么？"
选项：
1. "重新测试" — 再试一次同一课程测验
2. "测试其他课程" — 切换到其他课程
3. "解释我错过的题目" — 获取错误答案的详细解释
4. "完成" — 结束测验会话

如果**重新测试**：返回步骤 4（跳过时间问题，使用相同的时间）。
如果**测试其他课程**：返回步骤 1。
如果**解释题目**：询问是哪个问题编号，然后从课程 README.md 中阅读相关章节并用示例解释。

## 错误处理

### 无效的课程参数
如果参数与任何课程都不匹配，请显示有效课程列表并让用户选择一个。

### 用户想在测验中途退出
如果用户在任何一轮中表示想停止，请呈现已回答问题的部分结果。

### 找不到课程 README
如果 README.md 文件不存在于预期路径，请通知用户并建议检查仓库结构。

## 验证

### 触发测试套件

**应该触发：**
- "quiz me on hooks"
- "lesson quiz"
- "test my knowledge of lesson 3"
- "practice quiz for MCP"
- "do I understand skills"
- "quiz me on slash commands"
- "lesson-quiz 06"
- "test me on checkpoints"
- "how well do I know the CLI"
- "quiz me before I start the memory lesson"

**不应该触发：**
- "assess my overall level"（使用 /self-assessment）
- "explain hooks to me"
- "create a hook"
- "what is MCP"
- "review my code"
