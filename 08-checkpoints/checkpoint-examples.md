# 检查点示例

在 Claude Code 中有效使用检查点的真实示例。

注意：检查点会随着每个用户提示自动创建。你不需要手动保存。要回溯，按两次 `Esc`（`Esc+Esc`）或使用 `/rewind` 打开检查点浏览器。

## 示例 1：数据库迁移

### 场景
你需要从 MySQL 迁移到 PostgreSQL，但想探索直接迁移和渐进式双写方法两种方案。

### 工作流

```
用户：让我们实现从 MySQL 到 PostgreSQL 的直接迁移
      [检查点 A 自动创建]

Claude：I'll implement the direct migration...
[更改数据库驱动、更新查询、修改 schema]

用户：运行测试
      [检查点 B 自动创建]

Claude：Running tests...
❌ 15 tests failing - connection pool issues

用户：这个方法有问题。让我们尝试双写模式。
[用户按 Esc+Esc，选择检查点 A，选择"恢复代码和对话"]

用户：现在实现一个双写模式，同时写入两个数据库

Claude：I'll implement dual-write migration...
[实现双写层，渐进式迁移策略]

用户：运行测试

Claude：Running tests...
✅ All tests passing

用户：双写方法显然更安全。让我们提交这个。
```

## 示例 2：性能优化

### 场景
尝试多种性能优化策略。

### 工作流

```
用户：让我们优化 API 响应时间。当前：450ms
      [检查点"基准"自动创建]

Claude：I'll add database query caching...
[实现 Redis 缓存]

用户：运行性能测试

Claude：Results: 280ms average response time (38% improvement)

用户：让我尝试另一种方法。
[用户按 Esc+Esc，选择"基准"检查点，选择"恢复代码和对话"]

用户：尝试数据库查询优化

Claude：I'll optimize database queries...
[添加索引，优化 N+1 查询]

用户：运行性能测试

Claude：Results: 180ms average response time (60% improvement)

用户：让我再尝试第三种方法。
[用户按 Esc+Esc，选择"基准"检查点，选择"恢复代码和对话"]

用户：尝试响应压缩和 CDN

Claude：I'll add compression and CDN...
[实现 gzip，设置 CDN]

用户：运行性能测试

Claude：Results: 320ms average response time (29% improvement)

用户：查询优化是最好的。让我回去将它与缓存结合。
[用户按 Esc+Esc，选择查询优化后的检查点，选择"恢复代码和对话"]

用户：在这些优化查询的基础上添加 Redis 缓存

Claude：[在优化查询的基础上添加 Redis 缓存]

用户：运行性能测试

Claude：Results: 95ms average response time (79% improvement) 🎉

用户：完美！这就是最佳方案。让我们提交这个。
```

## 示例 3：UI/UX 迭代

### 场景
为仪表板尝试不同的布局。

### 工作流

```
用户：让我们用侧边栏布局重新设计仪表板
      [检查点"开始"自动创建]

Claude：[实现侧边栏布局]

用户：给我看截图

Claude：[显示截图]

用户：侧边栏太拥挤了。让我们尝试顶部导航。
[用户按 Esc+Esc，选择"开始"检查点，选择"恢复代码和对话"]

用户：尝试顶部导航布局

Claude：[实现顶部导航]

用户：给我看截图

Claude：[显示截图]

用户：更好，但让我们尝试基于卡片的网格布局
[用户按 Esc+Esc，选择"开始"检查点，选择"恢复代码和对话"]

用户：尝试基于卡片的网格布局

Claude：[实现卡片网格]

用户：给我看截图

Claude：[显示截图]

用户：很好！但我们能把顶部导航和卡片网格结合起来吗？
[用户按 Esc+Esc，选择卡片网格后的检查点，选择"恢复代码和对话"]

用户：在卡片网格布局中添加顶部导航

Claude：[在卡片网格中添加顶部导航]

用户：完美！这就是最终设计。
```

## 示例 4：调试会话

### 场景
用多种假设追踪一个棘手的 bug。

### 工作流

```
用户：应用程序存在内存泄漏
      [检查点"调试前"自动创建]

Claude：Let me investigate...
[分析代码]

用户：我觉得是事件监听器的问题。让我们修复那些。

Claude：[修复事件监听器清理]

用户：运行内存分析器

Claude：Still leaking memory - event listeners weren't the issue

用户：让我回去尝试不同的假设。
[用户按 Esc+Esc，选择"调试前"检查点，选择"恢复代码和对话"]

用户：可能是数据库连接？

Claude：[实现连接池修复]

用户：运行内存分析器

Claude：Still leaking - not the connections either

用户：让我回去尝试另一个角度。
[用户按 Esc+Esc，选择"调试前"检查点，选择"恢复代码和对话"]

用户：让我们检查循环引用

Claude：[查找并修复缓存中的循环引用]

用户：运行内存分析器

Claude：✅ Memory leak fixed! The circular references in the caching layer were the culprit.

用户：太好了！让我们提交这个修复。
```

## 示例 5：API 设计演进

### 场景
设计一个有多次迭代的 REST API。

### 工作流

```
用户：为我们的博客平台创建一个 REST API
      [检查点"API 设计前"自动创建]

Claude：[创建基本 CRUD API]

用户：这太简单了。让我们添加分页和过滤

Claude：[添加分页和过滤]

用户：我们需要更好的资源关系

Claude：[实现 HATEOAS 链接]

用户：实际上，让我们尝试 GraphQL 而不是 REST
[用户按 Esc+Esc，选择"API 设计前"检查点，选择"恢复代码和对话"]

用户：改为我们的博客平台实现一个 GraphQL API

Claude：[实现 GraphQL API]

用户：我觉得 REST对我们的用例更好。
[用户按 Esc+Esc，选择 HATEOAS 后的检查点，选择"恢复代码和对话"]

用户：让我们完成 REST 方法。
```

## 示例 6：配置管理

### 场景
测试不同的配置方法。

### 工作流

```
用户：将配置移至环境变量
      [检查点"原始配置"自动创建]

Claude：[实现环境变量配置]

用户：在开发环境中测试

Claude：Works locally but deployment issues in production

用户：让我尝试不同的方法。
[用户按 Esc+Esc，选择"原始配置"检查点，选择"恢复代码和对话"]

用户：尝试带验证的配置文件方法

Claude：[实现带 JSON schema 验证的 YAML 配置]

用户：在开发环境中测试

Claude：✅ Works well, good validation errors

用户：我们也能支持环境变量来处理敏感值吗？

Claude：[为 secrets 添加环境变量覆盖]

用户：测试部署

Claude：✅ All environments working correctly

用户：完美！这可以投入生产了。
```

## 示例 7：测试策略

### 场景
实现全面的测试。

### 工作流

```
用户：为 auth 模块添加单元测试
      [检查点自动创建]

Claude：[添加 Jest 单元测试]

用户：运行测试

Claude：45 tests passing, 78% coverage

用户：也添加集成测试

Claude：[添加集成测试]

用户：运行测试

Claude：89 tests passing, 92% coverage, but tests are slow (3 minutes)

用户：测试太慢了。让我们优化。

Claude：[优化测试设置，添加并行执行]

用户：运行测试

Claude：89 tests passing, 92% coverage, 35 seconds ✅

用户：很好！现在为关键路径添加 E2E 测试

Claude：[添加 Playwright E2E 测试]

用户：运行所有测试

Claude：112 tests passing, 94% coverage, 2 minutes

用户：覆盖率和速度的完美平衡！
```

## 示例 8：从检查点使用总结

### 场景
在漫长的调试会话之后，你想在保留上下文的同时压缩对话。

### 工作流

```
用户：[经过 20+ 条调试和探索消息后]

[用户按 Esc+Esc，选择一个早期检查点，选择"从这里总结"]
[可选提供说明："专注于我们尝试了什么，什么有效"]

Claude：[生成从该点往后对话的摘要]
[原始消息保留在记录中]
[摘要取代可见的对话，减少上下文窗口使用]

用户：现在让我们继续有效的方法。
```

## 关键要点

1. **检查点是自动的**：每个用户提示都会创建检查点——无需手动保存
2. **使用 Esc+Esc 或 /rewind**：这是访问检查点浏览器的两种方式
3. **选择正确的恢复选项**：根据需要恢复代码、对话、两者，或总结
4. **不要害怕实验**：检查点让尝试激进更改变得安全
5. **与 git 结合使用**：使用检查点进行探索，使用 git 处理最终确定的工作
6. **总结长会话**：使用"从这里总结"保持对话可管理
