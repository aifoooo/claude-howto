#!/bin/bash
# 记录所有 bash 命令
# Hook: PostToolUse:Bash

COMMAND="$1"
TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
LOGFILE="$HOME/.claude/bash-commands.log"

# 如果不存在则创建日志目录
mkdir -p "$(dirname "$LOGFILE")"

# 记录命令
echo "[$TIMESTAMP] $COMMAND" >> "$LOGFILE"

# 可选：也记录到系统日志
# logger -t "claude-bash" "$COMMAND"

exit 0
