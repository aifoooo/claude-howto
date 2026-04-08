"""EPUB 构建器测试的 Pytest 配置和共享 fixtures。"""

from __future__ import annotations

import logging
import sys
from pathlib import Path

import pytest

# 将父目录添加到路径以进行导入
sys.path.insert(0, str(Path(__file__).parent.parent))

from build_epub import BuildState, EPUBConfig, setup_logging


@pytest.fixture
def tmp_project(tmp_path: Path) -> Path:
    """创建用于测试的最小项目结构。"""
    # 创建根 markdown 文件
    readme = tmp_path / "README.md"
    readme.write_text("# Test Project\n\nThis is a test.")

    # 创建一个章节目录
    chapter_dir = tmp_path / "01-test-chapter"
    chapter_dir.mkdir()
    (chapter_dir / "README.md").write_text("# Chapter Overview\n\nOverview content.")
    (chapter_dir / "section.md").write_text("# Section\n\nSection content.")

    # 使用 PIL 创建一个正确的 PNG logo
    from PIL import Image as PILImage

    logo_path = tmp_path / "claude-howto-logo.png"
    img = PILImage.new("RGB", (100, 100), color=(26, 26, 46))
    img.save(logo_path, "PNG")

    return tmp_path


@pytest.fixture
def config(tmp_project: Path) -> EPUBConfig:
    """创建测试配置。"""
    return EPUBConfig(
        root_path=tmp_project,
        output_path=tmp_project / "test.epub",
    )


@pytest.fixture
def state() -> BuildState:
    """创建一个新的构建状态。"""
    return BuildState()


@pytest.fixture
def logger() -> logging.Logger:
    """创建一个测试日志记录器。"""
    return setup_logging(verbose=False)
