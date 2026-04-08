#!/usr/bin/env python3
"""验证 Markdown 文件中的交叉引用、锚点和代码栅栏。"""

import re
import sys
from pathlib import Path

IGNORE_DIRS = {
    ".venv",
    "node_modules",
    ".git",
    "blog-posts",
    "openspec",
    "prompts",
    ".agents",
}
IGNORE_FILES = {"README.backup.md"}


def iter_md_files():
    for f in Path().rglob("*.md"):
        if (
            not any(part in IGNORE_DIRS for part in f.parts)
            and f.name not in IGNORE_FILES
        ):
            yield f


def heading_to_anchor(heading: str) -> str:
    # 匹配 GitHub 的锚点生成：剥离非 ASCII（emoji）、剥离标点符号、
    # 小写、将空格替换为连字符、剥离首尾连字符。
    heading_ascii = heading.encode("ascii", "ignore").decode()
    return re.sub(r"[^\w\s-]", "", heading_ascii.lower()).replace(" ", "-").rstrip("-")


def strip_code_blocks(content: str) -> str:
    """移除带栅栏的代码块和内联代码跨度以避免扫描示例链接。"""
    # 剥离带栅栏的代码块（``` ... ```）
    content = re.sub(r"```[^\n]*\n.*?```", "", content, flags=re.DOTALL)
    # 剥离内联代码跨度（` ... `）
    content = re.sub(r"`[^`\n]+`", "", content)
    return content


def main() -> int:
    errors = []

    for file_path in iter_md_files():
        content = file_path.read_text()
        # 在扫描链接/锚点之前剥离代码块以避免代码栅栏内文档示例的误报
        scannable = strip_code_blocks(content)

        # 相对 .md 链接必须能解析
        errors.extend(
            f"{file_path}: broken cross-reference → '{link_path}'"
            for link_path in re.findall(r"\[[^\]]+\]\(([^)#]+\.md)[^)]*\)", scannable)
            if not (file_path.parent / link_path).resolve().exists()
        )

        # 页内锚点必须匹配真实标题
        anchors = re.findall(r"\[[^\]]+\]\(#([^)]+)\)", scannable)
        if anchors:
            headings = re.findall(r"^#{1,6}\s+(.+)$", content, re.MULTILINE)
            valid_anchors = {heading_to_anchor(h) for h in headings}
            errors.extend(
                f"{file_path}: broken anchor → '#{anchor}'"
                for anchor in anchors
                if anchor not in valid_anchors
            )

        # 不匹配的代码栅栏（仅计算行首的栅栏）
        if len(re.findall(r"^```", content, re.MULTILINE)) % 2 != 0:
            errors.append(f"{file_path}: unmatched code fences")

    # 所有编号课程目录必须有 README.md
    for i in range(1, 11):
        errors.extend(
            f"{d}: missing README.md"
            for d in Path().glob(f"{i:02d}-*")
            if d.is_dir() and not (d / "README.md").exists()
        )

    if errors:
        print("❌ Cross-reference errors:")
        for e in errors:
            print(f"  - {e}")
        return 1

    md_count = sum(1 for _ in iter_md_files())
    print(f"✅ All cross-references valid ({md_count} files checked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
