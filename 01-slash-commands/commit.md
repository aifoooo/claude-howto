---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*)
argument-hint: [message]
description: 带上下文创建 git 提交
---

## 上下文

- 当前 git 状态：!`git status`
- 当前 git diff：!`git diff HEAD`
- 当前分支：!`git branch --show-current`
- 最近提交：!`git log --oneline -10`

## 你的任务

根据以上更改，创建单个 git 提交。

如果通过参数提供了消息，使用它：$ARGUMENTS

否则，分析更改并按约定式提交格式创建合适的 commit 消息：
- `feat:` 新功能
- `fix:` 修复 bug
- `docs:` 文档更改
- `refactor:` 代码重构
- `test:` 添加测试
- `chore:` 维护任务
