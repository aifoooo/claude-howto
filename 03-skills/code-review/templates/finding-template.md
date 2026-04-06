# 代码审查发现模板

在代码审查期间记录每个发现的问题时使用此模板。

---

## 问题：[标题]

### 严重性
- [ ] Critical（阻止部署）
- [ ] High（合并前应修复）
- [ ] Medium（应尽快修复）
- [ ] Low（锦上添花）

### 类别
- [ ] 安全
- [ ] 性能
- [ ] 代码质量
- [ ] 可维护性
- [ ] 测试
- [ ] 设计模式
- [ ] 文档

### 位置
**文件：** `src/components/UserCard.tsx`

**行：** 45-52

**函数/方法：** `renderUserDetails()`

### 问题描述

**是什么：** 描述问题是什么。

**为什么重要：** 解释影响以及为什么需要修复。

**当前行为：** 展示有问题的代码或行为。

**预期行为：** 描述应该发生什么。

### 代码示例

#### 当前（有问题的）

```typescript
// 展示 N+1 查询问题
const users = fetchUsers();
users.forEach(user => {
  const posts = fetchUserPosts(user.id); // 每个用户一个查询！
  renderUserPosts(posts);
});
```

#### 建议的修复

```typescript
// 使用 JOIN 查询优化
const usersWithPosts = fetchUsersWithPosts();
usersWithPosts.forEach(({ user, posts }) => {
  renderUserPosts(posts);
});
```

### 影响分析

| 方面 | 影响 | 严重性 |
|--------|--------|----------|
| 性能 | 20 个用户 100+ 个查询 | High |
| 用户体验 | 页面加载慢 | High |
| 可扩展性 | 大规模时崩溃 | Critical |
| 可维护性 | 难以调试 | Medium |

### 相关问题

- `AdminUserList.tsx` 第 120 行有类似问题
- 相关 PR：#456
- 相关 issue：#789

### 额外资源

- [N+1 查询问题](https://en.wikipedia.org/wiki/N%2B1_problem)
- [数据库 Join 文档](https://docs.example.com/joins)

### 审查者备注

- 这是此代码库中的常见模式
- 考虑将其添加到代码风格指南中
- 可能值得创建一个辅助函数

### 作者回复（用于反馈）

*由代码作者填写：*

- [ ] 在提交 `abc123` 中实施了修复
- [ ] 修复状态：完成 / 进行中 / 需要讨论
- [ ] 问题或顾虑：（描述）

---

## 发现统计（供审查者使用）

审查多个发现时，跟踪：

- **发现的问题总数：** X
- **Critical：** X
- **High：** X
- **Medium：** X
- **Low：** X

**建议：** ✅ 批准 / ⚠️ 请求更改 / 🔄 需要讨论

**整体代码质量：** 1-5 星
