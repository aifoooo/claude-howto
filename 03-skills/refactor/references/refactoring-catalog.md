# 重构目录

来自 Martin Fowler 的 *Refactoring*（第 2 版）的精选重构技术目录。每个重构包含动机、分步机制和示例。

> "重构由其机制定义——你执行更改所遵循的精确步骤序列。" — Martin Fowler

---

## 如何使用此目录

1. **识别味道**使用代码味道参考
2. **找到匹配的重构**在此目录中
3. **按步执行机制**
4. **每步后测试**以确保行为保持不变

**黄金法则**：如果任何步骤超过 10 分钟，将其分解为更小的步骤。

---

## 最常见的重构

### 提取方法

**何时使用**：长方法、重复代码、需要命名一个概念

**动机**：将代码片段转换为名称说明其目的的方法。

**机制**：
1. 创建一个以所做之事命名的新方法（不是如何做）
2. 将代码片段复制到新方法
3. 扫描片段中使用的局部变量
4. 将局部变量作为参数传递（或在方法中声明）
5. 适当处理返回值
6. 用对新方法的调用替换原始片段
7. 测试

**之前**:
```javascript
function printOwing(invoice) {
  let outstanding = 0;

  console.log("***********************");
  console.log("**** Customer Owes ****");
  console.log("***********************");

  // Calculate outstanding
  for (const order of invoice.orders) {
    outstanding += order.amount;
  }

  // Print details
  console.log(`name: ${invoice.customer}`);
  console.log(`amount: ${outstanding}`);
}
```

**之后**:
```javascript
function printOwing(invoice) {
  printBanner();
  const outstanding = calculateOutstanding(invoice);
  printDetails(invoice, outstanding);
}

function printBanner() {
  console.log("***********************");
  console.log("**** Customer Owes ****");
  console.log("***********************");
}

function calculateOutstanding(invoice) {
  return invoice.orders.reduce((sum, order) => sum + order.amount, 0);
}

function printDetails(invoice, outstanding) {
  console.log(`name: ${invoice.customer}`);
  console.log(`amount: ${outstanding}`);
}
```

---

### 内联方法

**何时使用**：方法体和其名称一样清晰，过度委托

**动机**：当方法不增加价值时移除无谓的间接。

**机制**：
1. 检查该方法不是多态的
2. 找到对该方法的所有调用
3. 将每个调用替换为方法体
4. 每次替换后测试
5. 删除方法定义

**之前**:
```javascript
function getRating(driver) {
  return moreThanFiveLateDeliveries(driver) ? 2 : 1;
}

function moreThanFiveLateDeliveries(driver) {
  return driver.numberOfLateDeliveries > 5;
}
```

**之后**:
```javascript
function getRating(driver) {
  return driver.numberOfLateDeliveries > 5 ? 2 : 1;
}
```

---

### 提取变量

**何时使用**：难以理解的复杂表达式

**动机**：为复杂表达式的一部分命名。

**机制**：
1. 确保表达式无副作用
2. 声明一个不可变变量
3. 将其设置为表达式的结果（或部分）
4. 用变量替换原始表达式
5. 测试

**之前**:
```javascript
return order.quantity * order.itemPrice -
  Math.max(0, order.quantity - 500) * order.itemPrice * 0.05 +
  Math.min(order.quantity * order.itemPrice * 0.1, 100);
```

**之后**:
```javascript
const basePrice = order.quantity * order.itemPrice;
const quantityDiscount = Math.max(0, order.quantity - 500) * order.itemPrice * 0.05;
const shipping = Math.min(basePrice * 0.1, 100);
return basePrice - quantityDiscount + shipping;
```

---

### 内联变量

**何时使用**：变量名不比表达式传达更多

**动机**：移除不必要的间接。

**机制**：
1. 检查右侧无副作用
2. 如果变量不可变，先使其不可变并测试
3. 找到第一个引用并用表达式替换
4. 测试
5. 对所有引用重复
6. 删除声明和赋值
7. 测试

---

### 重命名变量

**何时使用**：名称不能清楚表达目的

**动机**：好的名称对干净代码至关重要。

**机制**：
1. 如果变量广泛使用，考虑封装
2. 找到所有引用
3. 更改每个引用
4. 测试

**提示**：
- 使用揭示意图的名称
- 避免缩写
- 使用领域术语

```javascript
// 坏
const d = 30;
const x = users.filter(u => u.a);

// 好
const daysSinceLastLogin = 30;
const activeUsers = users.filter(user => user.isActive);
```

---

### 更改函数声明

**何时使用**：函数名不能说明目的，参数需要更改

**动机**：好的函数名使代码自解释。

**机制（简单）**：
1. 删除不需要的参数
2. 更改名称
3. 添加需要的参数
4. 测试

**机制（迁移——用于复杂更改）**：
1. 如果删除参数，确保它未被使用
2. 用所需声明创建新函数
3. 让旧函数调用新函数
4. 测试
5. 更改调用者使用新函数
6. 每次后测试
7. 删除旧函数

**之前**:
```javascript
function circum(radius) {
  return 2 * Math.PI * radius;
}
```

**之后**:
```javascript
function circumference(radius) {
  return 2 * Math.PI * radius;
}
```

---

### 封装变量

**何时使用**：从多处直接访问数据

**动机**：为数据操作提供清晰的访问点。

**机制**：
1. 创建 getter 和 setter 函数
2. 找到所有引用
3. 用 getter 替换读取
4. 用 setter 替换写入
5. 每次更改后测试
6. 限制变量的可见性

**之前**:
```javascript
let defaultOwner = { firstName: "Martin", lastName: "Fowler" };

// Used in many places
spaceship.owner = defaultOwner;
```

**之后**:
```javascript
let defaultOwnerData = { firstName: "Martin", lastName: "Fowler" };

function defaultOwner() { return defaultOwnerData; }
function setDefaultOwner(arg) { defaultOwnerData = arg; }

spaceship.owner = defaultOwner();
```

---

### 引入参数对象

**何时使用**：经常一起传递的多个参数

**动机**：将自然属于一起的数据分组。

**机制**：
1. 为分组的参数创建一个新类/结构
2. 测试
3. 使用更改函数声明添加新对象
4. 测试
5. 对于组中的每个参数，从函数中移除它并使用新对象
6. 每次后测试

**之前**:
```javascript
function amountInvoiced(startDate, endDate) { ... }
function amountReceived(startDate, endDate) { ... }
function amountOverdue(startDate, endDate) { ... }
```

**之后**:
```javascript
class DateRange {
  constructor(start, end) {
    this.start = start;
    this.end = end;
  }
}

function amountInvoiced(dateRange) { ... }
function amountReceived(dateRange) { ... }
function amountOverdue(dateRange) { ... }
```

---

### 合并函数为类

**何时使用**：几个函数操作相同数据

**动机**：将函数与它们操作的数据分组。

**机制**：
1. 对公共数据应用封装记录
2. 将每个函数移动到类中
3. 每次移动后测试
4. 将数据参数替换为类字段的使用

**之前**:
```javascript
function base(reading) { ... }
function taxableCharge(reading) { ... }
function calculateBaseCharge(reading) { ... }
```

**之后**:
```javascript
class Reading {
  constructor(data) { this._data = data; }

  get base() { ... }
  get taxableCharge() { ... }
  get calculateBaseCharge() { ... }
}
```

---

### 分割阶段

**何时使用**：代码处理两个不同事物

**动机**：将代码分离为具有清晰边界的不同阶段。

**机制**：
1. 为第二阶段创建第二个函数
2. 测试
3. 在阶段之间引入中间数据结构
4. 测试
5. 将第一阶段提取到自己的函数中
6. 测试

**之前**:
```javascript
function priceOrder(product, quantity, shippingMethod) {
  const basePrice = product.basePrice * quantity;
  const discount = Math.max(quantity - product.discountThreshold, 0)
    * product.basePrice * product.discountRate;
  const shippingPerCase = (basePrice > shippingMethod.discountThreshold)
    ? shippingMethod.discountedFee : shippingMethod.feePerCase;
  const shippingCost = quantity * shippingPerCase;
  return basePrice - discount + shippingCost;
}
```

**之后**:
```javascript
function priceOrder(product, quantity, shippingMethod) {
  const priceData = calculatePricingData(product, quantity);
  return applyShipping(priceData, shippingMethod);
}

function calculatePricingData(product, quantity) {
  const basePrice = product.basePrice * quantity;
  const discount = Math.max(quantity - product.discountThreshold, 0)
    * product.basePrice * product.discountRate;
  return { basePrice, quantity, discount };
}

function applyShipping(priceData, shippingMethod) {
  const shippingPerCase = (priceData.basePrice > shippingMethod.discountThreshold)
    ? shippingMethod.discountedFee : shippingMethod.feePerCase;
  const shippingCost = priceData.quantity * shippingPerCase;
  return priceData.basePrice - priceData.discount + shippingCost;
}
```

---

## 移动功能

### 移动方法

**何时使用**：方法使用另一个类的特性比自己的还多

**动机**：将函数放在它们最常使用的数据所在的地方。

**机制**：
1. 检查方法在其类中使用的所有程序元素
2. 检查方法是否是多态的
3. 将方法复制到目标类
4. 调整以适应新上下文
5. 让原始方法委托给目标
6. 测试
7. 考虑删除原始方法

---

### 移动字段

**何时使用**：字段被另一个类更常使用

**动机**：将数据与使用它的函数放在一起。

**机制**：
1. 如果尚未封装，则封装字段
2. 测试
3. 在目标中创建字段
4. 更新引用使用目标字段
5. 测试
6. 删除原始字段

---

### 移动语句到函数

**何时使用**：相同代码总是与函数调用一起出现

**动机**：通过将重复代码移动到函数来消除重复。

**机制**：
1. 如果尚未提取，将重复代码提取为函数
2. 将语句移动到该函数
3. 测试
4. 如果调用者不再需要独立语句，则删除它们

---

### 移动语句到调用者

**何时使用**：常见行为在调用者之间有所不同

**动机**：当行为需要不同时，将其从函数中移出。

**机制**：
1. 对要移动的代码应用提取方法
2. 对原始函数应用内联方法
3. 删除现在内联的调用
4. 将提取的代码移动到每个调用者
5. 测试

---

## 组织数据

### 用对象替换原始类型

**何时使用**：数据项需要比简单值更多的行为

**动机**：用其行为封装数据。

**机制**：
1. 应用封装变量
2. 创建一个简单的值类
3. 将 setter 更改为创建新实例
4. 将 getter 更改为返回值
5. 测试
6. 向新类添加更丰富的行为

**之前**:
```javascript
class Order {
  constructor(data) {
    this.priority = data.priority; // string: "high", "rush", etc.
  }
}

// Usage
if (order.priority === "high" || order.priority === "rush") { ... }
```

**之后**:
```javascript
class Priority {
  constructor(value) {
    if (!Priority.legalValues().includes(value))
      throw new Error(`Invalid priority: ${value}`);
    this._value = value;
  }

  static legalValues() { return ['low', 'normal', 'high', 'rush']; }
  get value() { return this._value; }

  higherThan(other) {
    return Priority.legalValues().indexOf(this._value) >
           Priority.legalValues().indexOf(other._value);
  }
}

// Usage
if (order.priority.higherThan(new Priority("normal"))) { ... }
```

---

### 用查询替换临时变量

**何时使用**：临时变量保存表达式的结果

**动机**：通过将表达式提取为函数使代码更清晰。

**机制**：
1. 检查变量仅被赋值一次
2. 将赋值的右侧提取为方法
3. 将对临时变量的引用替换为方法调用
4. 测试
5. 删除临时变量声明和赋值

**之前**:
```javascript
const basePrice = this._quantity * this._itemPrice;
if (basePrice > 1000) {
  return basePrice * 0.95;
} else {
  return basePrice * 0.98;
}
```

**之后**:
```javascript
get basePrice() {
  return this._quantity * this._itemPrice;
}

// In the method
if (this.basePrice > 1000) {
  return this.basePrice * 0.95;
} else {
  return this.basePrice * 0.98;
}
```

---

## 简化条件逻辑

### 分解条件

**何时使用**：复杂的条件（if-then-else）语句

**动机**：通过提取条件和操作使意图清晰。

**机制**：
1. 对条件应用提取方法
2. 对 then 分支应用提取方法
3. 对 else 分支（如存在）应用提取方法

**之前**:
```javascript
if (!aDate.isBefore(plan.summerStart) && !aDate.isAfter(plan.summerEnd)) {
  charge = quantity * plan.summerRate;
} else {
  charge = quantity * plan.regularRate + plan.regularServiceCharge;
}
```

**之后**:
```javascript
if (isSummer(aDate, plan)) {
  charge = summerCharge(quantity, plan);
} else {
  charge = regularCharge(quantity, plan);
}

function isSummer(date, plan) {
  return !date.isBefore(plan.summerStart) && !date.isAfter(plan.summerEnd);
}

function summerCharge(quantity, plan) {
  return quantity * plan.summerRate;
}

function regularCharge(quantity, plan) {
  return quantity * plan.regularRate + plan.regularServiceCharge;
}
```

---

### 合并条件表达式

**何时使用**：多个条件具有相同结果

**动机**：使条件是单一检查这一点清晰。

**机制**：
1. 验证条件中无副作用
2. 使用 `and` 或 `or` 组合条件
3. 考虑对组合条件应用提取方法

**之前**:
```javascript
if (employee.seniority < 2) return 0;
if (employee.monthsDisabled > 12) return 0;
if (employee.isPartTime) return 0;
```

**之后**:
```javascript
if (isNotEligibleForDisability(employee)) return 0;

function isNotEligibleForDisability(employee) {
  return employee.seniority < 2 ||
         employee.monthsDisabled > 12 ||
         employee.isPartTime;
}
```

---

### 用卫语句替换嵌套条件

**何时使用**：深度嵌套的条件使流程难以遵循

**动机**：对特殊情况使用卫语句，保持正常流程清晰。

**机制**：
1. 找到特殊情况条件
2. 用提前返回的卫语句替换它们
3. 每次更改后测试

**之前**:
```javascript
function payAmount(employee) {
  let result;
  if (employee.isSeparated) {
    result = { amount: 0, reasonCode: "SEP" };
  } else {
    if (employee.isRetired) {
      result = { amount: 0, reasonCode: "RET" };
    } else {
      result = calculateNormalPay(employee);
    }
  }
  return result;
}
```

**之后**:
```javascript
function payAmount(employee) {
  if (employee.isSeparated) return { amount: 0, reasonCode: "SEP" };
  if (employee.isRetired) return { amount: 0, reasonCode: "RET" };
  return calculateNormalPay(employee);
}
```

---

### 用多态替换条件

**何时使用**：基于类型的 switch/case、按类型不同的条件逻辑

**动机**：让对象处理它们自己的行为。

**机制**：
1. 创建类层次结构（如不存在）
2. 使用工厂函数进行对象创建
3. 将条件逻辑移动到超类方法
4. 为每个 case 创建子类方法
5. 删除原始条件

**之前**:
```javascript
function plumages(birds) {
  return birds.map(b => plumage(b));
}

function plumage(bird) {
  switch (bird.type) {
    case 'EuropeanSwallow':
      return "average";
    case 'AfricanSwallow':
      return (bird.numberOfCoconuts > 2) ? "tired" : "average";
    case 'NorwegianBlueParrot':
      return (bird.voltage > 100) ? "scorched" : "beautiful";
    default:
      return "unknown";
  }
}
```

**之后**:
```javascript
class Bird {
  get plumage() { return "unknown"; }
}

class EuropeanSwallow extends Bird {
  get plumage() { return "average"; }
}

class AfricanSwallow extends Bird {
  get plumage() {
    return (this.numberOfCoconuts > 2) ? "tired" : "average";
  }
}

class NorwegianBlueParrot extends Bird {
  get plumage() {
    return (this.voltage > 100) ? "scorched" : "beautiful";
  }
}

function createBird(data) {
  switch (data.type) {
    case 'EuropeanSwallow': return new EuropeanSwallow(data);
    case 'AfricanSwallow': return new AfricanSwallow(data);
    case 'NorwegianBlueParrot': return new NorwegianBlueParrot(data);
    default: return new Bird(data);
  }
}
```

---

### 引入特殊情况（空对象）

**何时使用**：对特殊情况重复 null 检查

**动机**：返回处理特殊情况的对象。

**机制**：
1. 创建具有预期接口的特殊情况类
2. 添加 isSpecialCase 检查
3. 引入工厂方法
4. 用特殊情况对象使用替换 null 检查
5. 测试

**之前**:
```javascript
const customer = site.customer;
// ... many places checking
if (customer === "unknown") {
  customerName = "occupant";
} else {
  customerName = customer.name;
}
```

**之后**:
```javascript
class UnknownCustomer {
  get name() { return "occupant"; }
  get billingPlan() { return registry.defaultPlan; }
}

// Factory method
function customer(site) {
  return site.customer === "unknown"
    ? new UnknownCustomer()
    : site.customer;
}

// Usage - no null checks needed
const customerName = customer.name;
```

---

## 重构 API

### 将查询与修改器分离

**何时使用**：函数既有返回值又有副作用

**动机**：使哪些操作有副作用清晰。

**机制**：
1. 创建一个新的查询函数
2. 复制原始函数的返回逻辑
3. 修改原始函数返回 void
4. 替换使用返回值的调用
5. 测试

**之前**:
```javascript
function alertForMiscreant(people) {
  for (const p of people) {
    if (p === "Don") {
      setOffAlarms();
      return "Don";
    }
    if (p === "John") {
      setOffAlarms();
      return "John";
    }
  }
  return "";
}
```

**之后**:
```javascript
function findMiscreant(people) {
  for (const p of people) {
    if (p === "Don") return "Don";
    if (p === "John") return "John";
  }
  return "";
}

function alertForMiscreant(people) {
  if (findMiscreant(people) !== "") setOffAlarms();
}
```

---

### 参数化函数

**何时使用**：几个函数用不同值做相似的事情

**动机**：通过添加参数消除重复。

**机制**：
1. 选择一个函数
2. 添加参数用于变化的字面量
3. 更改体使用参数
4. 测试
5. 更改调用者使用参数化版本
6. 删除现在未使用的函数

**之前**:
```javascript
function tenPercentRaise(person) {
  person.salary = person.salary * 1.10;
}

function fivePercentRaise(person) {
  person.salary = person.salary * 1.05;
}
```

**之后**:
```javascript
function raise(person, factor) {
  person.salary = person.salary * (1 + factor);
}

// Usage
raise(person, 0.10);
raise(person, 0.05);
```

---

### 删除标志参数

**何时使用**：布尔参数改变函数行为

**动机**：通过分离函数使行为显式。

**机制**：
1. 为每个标志值创建显式函数
2. 将每个调用替换为适当的新函数
3. 每次更改后测试
4. 删除原始函数

**之前**:
```javascript
function bookConcert(customer, isPremium) {
  if (isPremium) {
    // premium booking logic
  } else {
    // regular booking logic
  }
}

bookConcert(customer, true);
bookConcert(customer, false);
```

**之后**:
```javascript
function bookPremiumConcert(customer) {
  // premium booking logic
}

function bookRegularConcert(customer) {
  // regular booking logic
}

bookPremiumConcert(customer);
bookRegularConcert(customer);
```

---

## 处理继承

### 提升方法

**何时使用**：多个子类中相同的方法

**动机**：消除类层次结构中的重复。

**机制**：
1. 检查方法以确保它们相同
2. 检查签名是否相同
3. 在超类中创建新方法
4. 从一个子类复制体
5. 删除一个子类方法，测试
6. 删除其他子类方法，每次测试

---

### 下推方法

**何时使用**：行为仅与子类子集相关

**动机**：将方法放在使用它的地方。

**机制**：
1. 将方法复制到需要它的每个子类
2. 从超类删除方法
3. 测试
4. 从不需要它的子类中删除
5. 测试

---

### 用委托替换子类

**何时使用**：继承被不正确地使用，需要更多灵活性

**动机**：在适当的时候优先使用组合而非继承。

**机制**：
1. 为委托创建空类
2. 在宿主类中添加持有委托的字段
3. 创建委托的构造函数，从宿主调用
4. 将功能移动到委托
5. 每次移动后测试
6. 用委托替换继承

---

## 提取类

**何时使用**：具有多个职责的大类

**动机**：拆分类以保持单一职责。

**机制**：
1. 决定如何拆分职责
2. 创建新类
3. 将字段从原始类移动到新类
4. 测试
5. 将方法从原始类移动到新类
6. 每次移动后测试
7. 审查并重命名两个类
8. 决定如何暴露新类

**之前**:
```javascript
class Person {
  get name() { return this._name; }
  set name(arg) { this._name = arg; }
  get officeAreaCode() { return this._officeAreaCode; }
  set officeAreaCode(arg) { this._officeAreaCode = arg; }
  get officeNumber() { return this._officeNumber; }
  set officeNumber(arg) { this._officeNumber = arg; }

  get telephoneNumber() {
    return `(${this._officeAreaCode}) ${this._officeNumber}`;
  }
}
```

**之后**:
```javascript
class Person {
  constructor() {
    this._telephoneNumber = new TelephoneNumber();
  }
  get name() { return this._name; }
  set name(arg) { this._name = arg; }
  get telephoneNumber() { return this._telephoneNumber.toString(); }
  get officeAreaCode() { return this._telephoneNumber.areaCode; }
  set officeAreaCode(arg) { this._telephoneNumber.areaCode = arg; }
}

class TelephoneNumber {
  get areaCode() { return this._areaCode; }
  set areaCode(arg) { this._areaCode = arg; }
  get number() { return this._number; }
  set number(arg) { this._number = arg; }
  toString() { return `(${this._areaCode}) ${this._number}`; }
}
```

---

## 快速参考：味道到重构

| 代码味道 | 主要重构 | 替代方案 |
|------------|-------------------|-------------|
| 长方法 | 提取方法 | 用查询替换临时变量 |
| 重复代码 | 提取方法 | 提升方法 |
| 大类 | 提取类 | 提取子类 |
| 长参数列表 | 引入参数对象 | 保留整个对象 |
| 特性依恋 | 移动方法 | 提取方法 + 移动 |
| 数据块 | 提取类 | 引入参数对象 |
| 原始类型痴迷 | 用对象替换原始类型 | 替换类型代码 |
| Switch 语句 | 用多态替换条件 | 替换类型代码 |
| 临时字段 | 提取类 | 引入空对象 |
| 消息链 | 隐藏委托 | 提取方法 |
| 中间人 | 删除中间人 | 内联方法 |
| 分散变化 | 提取类 | 分割阶段 |
| 霰弹手术 | 移动方法 | 内联类 |
| 死代码 | 删除死代码 | - |
| 投机性通用性 | 折叠层次结构 | 内联类 |

---

## 延伸阅读

- Fowler, M. (2018). *Refactoring: Improving the Design of Existing Code* (第 2 版)
- 在线目录：https://refactoring.com/catalog/
