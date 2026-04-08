#!/usr/bin/env python3
"""检查 Markdown 文件中的外部 URL 是否可访问。"""

import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

IGNORE_DIRS = {
    ".venv",
    "node_modules",
    ".git",
    "blog-posts",
    "openspec",
    "prompts",
    ".agents",
    ".claude",
}
TIMEOUT = 10
# 要跳过的域名/模式：徽章、占位符和阻止机器人的主机
SKIP_DOMAINS = {
    "shields.io",
    "img.shields.io",
    "star-history.com",
    "api.star-history.com",
    "example.com",
    "localhost",
    "127.0.0.1",
    "my-webhook.example.com",
    "git.internal",
    # Wikipedia 阻止 HEAD 请求 — 在 CI 中没有网络的情况下 GET 也不可靠
    "en.wikipedia.org",
    "wikipedia.org",
    # GitHub API 需要认证 — 未认证请求对受保护端点返回 404
    "api.github.com",
}
SKIP_DOMAIN_SUFFIXES = (".example.com", ".example.org", ".internal")
# 故意无法解析的占位符/模板 URL
SKIP_URL_PATTERNS = {
    "github.com/org/",
    "github.com/user/",
    "github.com/your-org/",
    "docs.example.com",
}

URL_RE = re.compile(r"https?://[a-zA-Z0-9][a-zA-Z0-9\-._~:/?#\[\]@!$&'()*+,;=%]+")


def is_skipped(url: str) -> bool:
    try:
        domain = url.split("/")[2]
    except IndexError:
        return True  # 格式错误的 URL
    if any(skip == domain or domain.endswith("." + skip) for skip in SKIP_DOMAINS):
        return True
    if any(domain.endswith(suffix) for suffix in SKIP_DOMAIN_SUFFIXES):
        return True
    return any(pattern in url for pattern in SKIP_URL_PATTERNS)


def check_url(url: str) -> tuple[str, bool, str]:
    if is_skipped(url):
        return url, True, "skipped"
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "Mozilla/5.0"}, method="HEAD"
        )
        with urllib.request.urlopen(req, timeout=TIMEOUT):  # nosec B310
            return url, True, "ok"
    except urllib.error.HTTPError as e:
        # 403/429 通常表示服务器正常但阻止了机器人 — 视为正常
        if e.code in (401, 403, 405, 429):
            return url, True, f"http {e.code} (ignored)"
        return url, False, f"HTTP {e.code}"
    except Exception as e:
        return url, False, str(e)


def main(strict: bool = False) -> int:
    urls: dict[str, list[str]] = {}  # url -> [file, ...]

    md_files = [
        f
        for f in Path().rglob("*.md")
        if not any(part in IGNORE_DIRS for part in f.parts)
    ]

    for file_path in md_files:
        content = file_path.read_text()
        for raw_url in URL_RE.findall(content):
            # 剥离正则表达式可能过度捕获的尾随 Markdown/标点符号
            # 来自链接语法如 [text](https://url/) 或 **https://url)**
            clean_url = raw_url.rstrip(")>*_`':.,;").split("#")[0]
            urls.setdefault(clean_url, []).append(str(file_path))

    if not urls:
        print("✅ No external URLs found")
        return 0

    errors = []
    with ThreadPoolExecutor(max_workers=10) as pool:
        futures = {pool.submit(check_url, url): url for url in urls}
        for future in as_completed(futures):
            url, ok, reason = future.result()
            if not ok:
                errors.extend(f"{f}: dead link → {url} ({reason})" for f in urls[url])

    if errors:
        print("❌ Dead links found:")
        for e in sorted(errors):
            print(f"  - {e}")
        # 在非严格模式（pre-commit）下，报告但不阻止提交。
        # 设置 LINK_CHECK_STRICT=1（如 CI 所做）以强制失败。
        return 1 if strict else 0

    print(f"✅ All external URLs reachable ({len(urls)} checked)")
    return 0


if __name__ == "__main__":
    import os

    sys.exit(main(strict=os.environ.get("LINK_CHECK_STRICT") == "1"))
