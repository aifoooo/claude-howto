# 代码味道目录

基于 Martin Fowler 的 *Refactoring*（第 2 版）的全面代码味道参考。代码味道是更深层问题的症状——它们表明你的代码设计可能有问题。

> "代码味道是通常对应于系统更深层问题的表面指示。" — Martin Fowler

---

## 臃肿者

代表某些东西已经变得太大而无法有效处理的代码味道。

### 长方法

**迹象：**
- 方法超过 30-50 行
- 需要滚动才能看到整个方法
- 多层嵌套
- 解释各部分的注释

**为什么不好：**
- 难以理解
- 难以单独测试
- 更改有意想不到的后果
- 重复逻辑隐藏在内部

**重构：**
- 提取方法
- 用查询替换临时变量
- 引入参数对象
- 用方法对象替换方法
- 分解条件

**示例（之前）：**
```javascript
function processOrder(order) {
  // 验证订单（20 行）
  if (!order.items) throw new Error('No items');
  if (order.items.length === 0) throw new Error('Empty order');
  // ... 更多验证

  // 计算总计（30 行）
  let subtotal = 0;
  for (const item of order.items) {
    subtotal += item.price * item.quantity;
  }
  // ... 税、运费、折扣

  // 发送通知（20 行）
  // ... 邮件逻辑
}
```

**示例（之后）：**
```javascript
function processOrder(order) {
  validateOrder(order);
  const totals = calculateOrderTotals(order);
  sendOrderNotifications(order, totals);
  return { order, totals };
}
```

---

### 大类

**迹象：**
- 类有许多实例变量（>7-10）
- 类有许多方法（>15-20）
- 类名模糊（Manager、Handler、Processor）
- 方法不使用所有实例变量

**为什么不好：**
- 违反单一职责原则
- 难以测试
- 更改波及不相关的功能
- 难以重用部分

**重构：**
- 提取类
- 提取子类
- 提取接口

**检测：**
```
代码行数 > 300
方法数量 > 15
字段数量 > 10
```

---

### 原始类型痴迷

**迹象：**
- 使用原始类型表示领域概念（邮箱用 string、钱用 int）
- 原始类型的数组而非对象
- 类型代码的字符串常量
- 魔法数字/字符串

**为什么不好：**
- 类型级别无验证
- 逻辑分散在代码库中
- 容易传递错误值
- 缺少领域概念

**重构：**
- 用对象替换原始类型
- 用类替换类型代码
- 用子类替换类型代码
- 用状态/策略替换类型代码

**示例（之前）：**
```javascript
const user = {
  email: 'john@example.com',     // 只是个字符串
  phone: '1234567890',           // 只是个字符串
  status: 'active',              // 魔法字符串
  balance: 10050                 // 美分作为整数
};
```

**示例（之后）：**
```javascript
const user = {
  email: new Email('john@example.com'),
  phone: new PhoneNumber('1234567890'),
  status: UserStatus.ACTIVE,
  balance: Money.cents(10050)
};
```

---

### 长参数列表

**迹象：**
- 方法有 4+ 参数
- 参数总是一起出现
- 布尔标志改变方法行为
- 经常传递 null/undefined

**为什么不好：**
- 难以正确调用
- 参数顺序混淆
- 表明方法做太多
- 难以添加新参数

**重构：**
- 引入参数对象
- 保留整个对象
- 用方法调用替换参数
- 删除标志参数

**示例（之前）：**
```javascript
function createUser(firstName, lastName, email, phone,
                    street, city, state, zip,
                    isAdmin, isActive, createdBy) {
  // ...
}
```

**示例（之后）：**
```javascript
function createUser(personalInfo, address, options) {
  // personalInfo: { firstName, lastName, email, phone }
  // address: { street, city, state, zip }
  // options: { isAdmin, isActive, createdBy }
}
```

---

### 数据块

**迹象：**
- 相同的 3+ 字段重复出现
- 参数总是一起旅行
- 具有属于一起的字段子集的类

**为什么不好：**
- 重复处理逻辑
- 缺少抽象
- 难以扩展
- 表明隐藏的类

**重构：**
- 提取类
- 引入参数对象
- 保留整个对象

**示例：**
```javascript
// 数据块：(x, y, z) 坐标
function movePoint(x, y, z, dx, dy, dz) { }
function scalePoint(x, y, z, factor) { }
function distanceBetween(x1, y1, z1, x2, y2, z2) { }

// 提取 Point3D 类
class Point3D {
  constructor(x, y, z) { }
  move(delta) { }
  scale(factor) { }
  distanceTo(other) { }
}
```

---

## 面向对象滥用者

表明 OOP 原则使用不完整或不正确的味道。

### Switch 语句

**迹象：**
- 长的 switch/case 或 if/else 链
- 多处相同的 switch
- 按类型代码 switch
- 添加新案例需要到处更改

**为什么不好：**
- 违反开闭原则
- 更改波及所有 switch 位置
- 难以扩展
- 通常表明缺少多态

**重构：**
- 用多态替换条件
- 用子类替换类型代码
- 用状态/策略替换类型代码

**示例（之前）：**
```javascript
function calculatePay(employee) {
  switch (employee.type) {
    case 'hourly':
      return employee.hours * employee.rate;
    case 'salaried':
      return employee.salary / 12;
    case 'commissioned':
      return employee.sales * employee.commission;
  }
}
```

**示例（之后）：**
```javascript
class HourlyEmployee {
  calculatePay() {
    return this.hours * this.rate;
  }
}

class SalariedEmployee {
  calculatePay() {
    return this.salary / 12;
  }
}
```

---

### 临时字段

**迹象：**
- 实例变量仅在某些方法中使用
- 条件设置的字段
- 某些情况的复杂初始化

**为什么不好：**
- 令人困惑——字段存在但可能为 null
- 难以理解对象状态
- 表明隐藏的条件逻辑

**重构：**
- 提取类
- 引入空对象
- 用局部变量替换临时字段

---

### 拒绝遗产

**迹象：**
- 子类不使用继承的方法/数据
- 子类覆盖为空
- 继承用于代码重用而非 IS-A 关系

**为什么不好：**
- 错误的抽象
- 违反里氏替换原则
- 误导的层次结构

**重构：**
- 下推方法/字段
- 用委托替换子类
- 用委托替换继承

---

### 具有不同接口的替代类

**迹象：**
- 两个类做相似的事情
- 相同概念的不同方法名
- 可以互换使用

**为什么不好：**
- 重复实现
- 无通用接口
- 难以切换

**重构：**
- 重命名方法
- 移动方法
- 提取超类
- 提取接口

---

## 变更阻止者

使更改困难的代码味道——更改一件事需要更改许多其他事情。

### 分散变化

**迹象：**
- 一个类因多个不同原因更改
- 不同区域的更改触发相同的类编辑
- 类是一个"上帝类"

**为什么不好：**
- 违反单一职责
- 高更改频率
- 合并冲突

**重构：**
- 提取类
- 提取超类
- 提取子类

**示例：**
`User` 类因以下原因更改：
- 认证更改
- 个人资料更改
- 计费更改
- 通知更改

→ 提取：`AuthService`、`ProfileService`、`BillingService`、`NotificationService`

---

### 霰弹手术

**迹象：**
- 一个更改需要在许多类中编辑
- 一个功能需要触及 10+ 文件
- 更改分散，难以找到所有

**为什么不好：**
- 容易错过一个地方
- 高耦合
- 更改容易出错

**重构：**
- 移动方法
- 移动字段
- 内联类

**检测：**
查找：添加一个字段需要在 >5 个文件中更改。

---

### 并行继承层次结构

**迹象：**
- 在一个层次结构中创建子类需要在另一个中创建子类
- 类前缀匹配（如 `DatabaseOrder`、`DatabaseProduct`）

**为什么不好：**
- 双重维护
- 层次结构之间的耦合
- 容易忘记一边

**重构：**
- 移动方法
- 移动字段
- 消除一个层次结构

---

## 可不必者

不必要的东西应该被删除。

### 过度注释

**迹象：**
- 解释代码做什么的注释
- 注释掉的代码
- 永远存在的 TODO/FIXME
- 注释中的道歉

**为什么不好：**
- 注释会撒谎（不同步）
- 代码应该是自解释的
- 死代码造成混淆

**重构：**
- 提取方法（名称解释做什么）
- 重命名（无需注释的清晰度）
- 删除注释掉的代码
- 引入断言

**好注释 vs 坏注释：**
```javascript
// 坏：解释做什么
// 遍历用户并检查是否活跃
for (const user of users) {
  if (user.status === 'active') { }
}

// 好：解释为什么
// 仅活跃用户 - 非活跃的由清理作业处理
const activeUsers = users.filter(u => u.isActive);
```

---

### 重复代码

**迹象：**
- 多处相同的代码
- 略有变化的相似代码
- 复制粘贴模式

**为什么不好：**
- Bug 修复需要改多处
- 不一致风险
- 代码库臃肿

**重构：**
- 提取方法
- 提取类
- 提升方法（在层次结构中）
- 形成模板方法

**检测规则：**
重复 3+ 次的代码应该被提取。

---

### 懒散类

**迹象：**
- 类不足以证明其存在是合理的
- 无增加值的外包装
- 过度工程化的结果

**为什么不好：**
- 维护开销
- 不必要的间接
- 无收益的复杂性

**重构：**
- 内联类
- 折叠层次结构

---

### 死代码

**迹象：**
- 不可达的代码
- 未使用的变量/方法/类
- 注释掉的代码
- 不可能条件后的代码

**为什么不好：**
- 混淆
- 维护负担
- 减慢理解

**重构：**
- 删除死代码
- 安全删除

**检测：**
```bash
# 查找未使用的导出
# 查找未引用的函数
# IDE"未使用"警告
```

---

### 投机性通用性

**迹象：**
- 只有一个子类的抽象类
- "为了将来使用"而未使用的参数
- 仅委托的方法
- 一个用例的"框架"

**为什么不好：**
- 无收益的复杂性
- YAGNI（你不会需要它）
- 难以理解

**重构：**
- 折叠层次结构
- 内联类
- 删除参数
- 重命名方法

---

## 耦合者

代表类之间过度耦合的代码味道。

### 特性依恋

**迹象：**
- 方法使用另一个类的数据比自己的还多
- 许多对另一个对象的 getter 调用
- 数据和行为分离

**为什么不好：**
- 行为位置错误
- 封装性差
- 难以维护

**重构：**
- 移动方法
- 移动字段
- 提取方法（然后移动）

**示例（之前）：**
```javascript
class Order {
  getDiscountedPrice(customer) {
    // 大量使用 customer 数据
    if (customer.loyaltyYears > 5) {
      return this.price * customer.discountRate;
    }
    return this.price;
  }
}
```

**示例（之后）：**
```javascript
class Customer {
  getDiscountedPriceFor(price) {
    if (this.loyaltyYears > 5) {
      return price * this.discountRate;
    }
    return price;
  }
}
```

---

### 不当亲密

**迹象：**
- 类访问彼此的私有部分
- 双向引用
- 子类对父类了解太多

**为什么不好：**
- 高耦合
- 更改级联
- 难以修改一个而不修改另一个

**重构：**
- 移动方法
- 移动字段
- 将双向改为单向
- 提取类
- 隐藏委托

---

### 消息链

**迹象：**
- 长的方法调用链：`a.getB().getC().getD().getValue()`
- 客户端依赖于导航结构
- "火车残骸"代码

**为什么不好：**
- 脆弱——任何更改都会破坏链
- 违反得墨忒耳定律
- 耦合到结构

**重构：**
- 隐藏委托
- 提取方法
- 移动方法

**示例：**
```javascript
// 坏：消息链
const managerName = employee.getDepartment().getManager().getName();

// 更好：隐藏委托
const managerName = employee.getManagerName();
```

---

### 中间人

**迹象：**
- 仅委托给另一个的类
- 一半方法是委托
- 无增加值

**为什么不好：**
- 不必要的间接
- 维护开销
- 令人困惑的架构

**重构：**
- 删除中间人
- 内联方法

---

## 味道严重性指南

| 严重性 | 描述 | 行动 |
|----------|-------------|--------|
| **Critical** | 阻塞开发，导致 bug | 立即修复 |
| **High** | 重大维护负担 | 在当前 sprint 修复 |
| **Medium** | 明显但可管理 | 计划在近期修复 |
| **Low** | 小的不便 | 顺便修复 |

---

## 快速检测检查清单

扫描代码时使用此检查清单：

- [ ] 任何方法 > 30 行？
- [ ] 任何类 > 300 行？
- [ ] 任何方法有 > 4 个参数？
- [ ] 任何重复的代码块？
- [ ] 任何按类型代码的 switch/case？
- [ ] 任何未使用的代码？
- [ ] 任何大量使用另一个类数据的方法？
- [ ] 任何长的方法调用链？
- [ ] 任何解释"做什么"而非"为什么"的注释？
- [ ] 任何应该是对象的原始类型？

---

## 延伸阅读

- Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (第 2 版)
- Kerievsky, J. (2004). *Refactoring to Patterns*
- Feathers, M. (2004). *Working Effectively with Legacy Code*
