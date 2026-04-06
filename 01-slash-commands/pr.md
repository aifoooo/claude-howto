---
description: 清理代码、stage 更改，并准备 Pull Request
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git diff:*), Bash(npm test:*), Bash(npm run lint:*)
---

# Pull Request 准备清单

创建 PR 前，执行以下步骤：

1. 运行 linting：`prettier --write .`
2. 运行测试：`npm test`
3. 审查 git diff：`git diff HEAD`
4. Stage 更改：`git add .`
5. 按约定式提交创建 commit 消息：
   - `fix:` 修复 bug
   - `feat:` 新功能
   - `docs:` 文档
   - `refactor:` 代码重构
   - `test:` 添加测试
   - `chore:` 维护

6. 生成 PR 总结，包括：
   - 更改了什么
   - 为什么更改
   - 执行的测试
   - 潜在影响
