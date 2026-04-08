#!/bin/bash
# 验证用户提示
# Hook: UserPromptSubmit

# 从 stdin 读取提示
PROMPT=$(cat)

echo "🔍 正在验证提示..."

# 检查危险操作
DANGEROUS_PATTERNS=(
  "rm -rf /"
  "delete database"
  "drop database"
  "format disk"
  "dd if="
)

for pattern in "${DANGEROUS_PATTERNS[@]}"; do
  if echo "$PROMPT" | grep -qi "$pattern"; then
    echo "❌ 已阻止：检测到危险操作: $pattern"
    exit 1
  fi
done

# 检查生产部署
if echo "$PROMPT" | grep -qiE "(deploy|push).*production"; then
  if [ ! -f ".deployment-approved" ]; then
    echo "❌ 已阻止：生产部署需要批准"
    echo "创建 .deployment-approved 文件以继续"
    exit 1
  fi
fi

# 检查某些操作中是否需要上下文
if echo "$PROMPT" | grep -qi "refactor"; then
  if [ ! -f "tests/" ] && [ ! -f "test/" ]; then
    echo "⚠️  警告：没有测试的重构可能存在风险"
  fi
fi

echo "✅ 提示验证通过"
exit 0
