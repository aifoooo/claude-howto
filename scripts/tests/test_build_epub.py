"""EPUB 构建器模块的测试。"""

from __future__ import annotations

import logging
from pathlib import Path
from unittest.mock import patch

import pytest

# Fixtures 是由 pytest 自动从 conftest.py 导入的
# 从父目录导入（由 conftest.py 的 sys.path 处理）
from build_epub import (
    BuildState,
    ChapterCollector,
    EPUBConfig,
    ValidationError,
    create_chapter_html,
    extract_all_mermaid_blocks,
    get_chapter_order,
    sanitize_mermaid,
    setup_logging,
    validate_inputs,
)

# =============================================================================
# BuildState 测试
# =============================================================================


class TestBuildState:
    """BuildState 数据类的测试。"""

    def test_initial_state(self, state: BuildState) -> None:
        """测试初始状态为空。"""
        assert state.mermaid_counter == 0
        assert len(state.mermaid_cache) == 0
        assert len(state.mermaid_added_to_book) == 0
        assert len(state.path_to_chapter) == 0

    def test_state_modification(self, state: BuildState) -> None:
        """测试状态可以被修改。"""
        state.mermaid_counter = 5
        state.mermaid_cache["key"] = (b"data", "file.png")
        state.mermaid_added_to_book.add("file.png")
        state.path_to_chapter["README.md"] = "chap_01.xhtml"

        assert state.mermaid_counter == 5
        assert state.mermaid_cache["key"] == (b"data", "file.png")
        assert "file.png" in state.mermaid_added_to_book
        assert state.path_to_chapter["README.md"] == "chap_01.xhtml"

    def test_reset(self, state: BuildState) -> None:
        """测试 reset 清除所有状态。"""
        state.mermaid_counter = 5
        state.mermaid_cache["key"] = (b"data", "file.png")
        state.mermaid_added_to_book.add("file.png")
        state.path_to_chapter["README.md"] = "chap_01.xhtml"

        state.reset()

        assert state.mermaid_counter == 0
        assert len(state.mermaid_cache) == 0
        assert len(state.mermaid_added_to_book) == 0
        assert len(state.path_to_chapter) == 0


# =============================================================================
# EPUBConfig 测试
# =============================================================================


class TestEPUBConfig:
    """EPUBConfig 数据类的测试。"""

    def test_required_fields(self, tmp_path: Path) -> None:
        """测试必须提供必填字段。"""
        config = EPUBConfig(
            root_path=tmp_path,
            output_path=tmp_path / "out.epub",
        )
        assert config.root_path == tmp_path
        assert config.output_path == tmp_path / "out.epub"

    def test_default_values(self, tmp_path: Path) -> None:
        """测试默认值是否正确设置。"""
        config = EPUBConfig(
            root_path=tmp_path,
            output_path=tmp_path / "out.epub",
        )
        assert config.identifier == "claude-howto-guide"
        assert config.title == "Claude Code How-To Guide"
        assert config.language == "en"
        assert config.author == "Claude Code Community"
        assert config.request_timeout == 30.0
        assert config.max_concurrent_requests == 10
        assert config.max_retries == 3

    def test_custom_values(self, tmp_path: Path) -> None:
        """测试自定义值覆盖默认值。"""
        config = EPUBConfig(
            root_path=tmp_path,
            output_path=tmp_path / "out.epub",
            title="Custom Title",
            request_timeout=60.0,
            max_concurrent_requests=5,
        )
        assert config.title == "Custom Title"
        assert config.request_timeout == 60.0
        assert config.max_concurrent_requests == 5


# =============================================================================
# 验证测试
# =============================================================================


class TestValidation:
    """输入验证的测试。"""

    def test_valid_inputs(self, config: EPUBConfig, logger: logging.Logger) -> None:
        """测试有效输入通过验证。"""
        # 不应抛出异常
        validate_inputs(config, logger)

    def test_missing_root_path(self, tmp_path: Path, logger: logging.Logger) -> None:
        """测试缺少根路径时抛出 ValidationError。"""
        config = EPUBConfig(
            root_path=tmp_path / "nonexistent",
            output_path=tmp_path / "out.epub",
        )
        with pytest.raises(ValidationError, match="Root path does not exist"):
            validate_inputs(config, logger)

    def test_root_path_is_file(self, tmp_path: Path, logger: logging.Logger) -> None:
        """测试将文件作为根路径时抛出 ValidationError。"""
        file_path = tmp_path / "file.txt"
        file_path.write_text("content")
        config = EPUBConfig(
            root_path=file_path,
            output_path=tmp_path / "out.epub",
        )
        with pytest.raises(ValidationError, match="Root path is not a directory"):
            validate_inputs(config, logger)

    def test_no_markdown_files(self, tmp_path: Path, logger: logging.Logger) -> None:
        """测试没有 markdown 文件的目录时抛出 ValidationError。"""
        empty_dir = tmp_path / "empty"
        empty_dir.mkdir()
        config = EPUBConfig(
            root_path=empty_dir,
            output_path=tmp_path / "out.epub",
        )
        with pytest.raises(ValidationError, match="No markdown files found"):
            validate_inputs(config, logger)

    def test_missing_output_directory(
        self, tmp_project: Path, logger: logging.Logger
    ) -> None:
        """测试缺少输出目录时抛出 ValidationError。"""
        config = EPUBConfig(
            root_path=tmp_project,
            output_path=tmp_project / "nonexistent" / "out.epub",
        )
        with pytest.raises(ValidationError, match="Output directory does not exist"):
            validate_inputs(config, logger)


# =============================================================================
# Mermaid 处理测试
# =============================================================================


class TestMermaidProcessing:
    """Mermaid 图表处理的测试。"""

    def test_sanitize_mermaid_numbered_list(self) -> None:
        """测试方括号中的编号列表被转义。"""
        input_code = 'A["1. First item"] --> B["2. Second item"]'
        expected = 'A["1\\. First item"] --> B["2\\. Second item"]'
        assert sanitize_mermaid(input_code) == expected

    def test_sanitize_mermaid_no_change(self) -> None:
        """测试没有编号列表的代码保持不变。"""
        input_code = "A --> B --> C"
        assert sanitize_mermaid(input_code) == input_code

    def test_extract_mermaid_blocks(
        self, tmp_path: Path, logger: logging.Logger
    ) -> None:
        """测试从文件中提取 Mermaid 块。"""
        # 创建包含 mermaid 块的测试文件
        md_file = tmp_path / "test.md"
        md_file.write_text(
            """# Test

```mermaid
graph TD
    A --> B
```

Some text

```mermaid
graph LR
    C --> D
```
"""
        )

        diagrams = extract_all_mermaid_blocks([(md_file, "Test")], logger)

        assert len(diagrams) == 2
        assert diagrams[0][0] == 1  # 第一个图表索引
        assert diagrams[1][0] == 2  # 第二个图表索引
        assert "A --> B" in diagrams[0][1]
        assert "C --> D" in diagrams[1][1]

    def test_extract_mermaid_blocks_deduplication(
        self, tmp_path: Path, logger: logging.Logger
    ) -> None:
        """测试重复的 Mermaid 块被去重。"""
        md_file1 = tmp_path / "test1.md"
        md_file2 = tmp_path / "test2.md"

        same_diagram = """```mermaid
graph TD
    A --> B
```"""

        md_file1.write_text(f"# File 1\n\n{same_diagram}")
        md_file2.write_text(f"# File 2\n\n{same_diagram}")

        diagrams = extract_all_mermaid_blocks(
            [(md_file1, "Test1"), (md_file2, "Test2")], logger
        )

        # 由于图表相同，应该只有一个
        assert len(diagrams) == 1


# =============================================================================
# 章节收集测试
# =============================================================================


class TestChapterCollector:
    """ChapterCollector 类的测试。"""

    def test_collect_single_file(self, tmp_path: Path, state: BuildState) -> None:
        """测试收集单个 markdown 文件。"""
        readme = tmp_path / "README.md"
        readme.write_text("# Test")

        collector = ChapterCollector(tmp_path, state)
        chapters = collector.collect_all_chapters([("README.md", "Introduction")])

        assert len(chapters) == 1
        assert chapters[0].file_path == readme
        assert chapters[0].display_name == "Introduction"
        assert chapters[0].chapter_filename == "chap_01.xhtml"
        assert state.path_to_chapter["README.md"] == "chap_01.xhtml"

    def test_collect_folder(self, tmp_project: Path, state: BuildState) -> None:
        """测试收集包含多个文件的文件夹。"""
        collector = ChapterCollector(tmp_project, state)
        chapters = collector.collect_all_chapters([("01-test-chapter", "Test Chapter")])

        assert len(chapters) == 2  # README.md 和 section.md
        assert chapters[0].is_folder_overview is True
        assert chapters[0].folder_name == "Test Chapter"
        assert chapters[1].is_folder_overview is False

    def test_path_mapping(self, tmp_project: Path, state: BuildState) -> None:
        """测试路径映射是否正确构建。"""
        collector = ChapterCollector(tmp_project, state)
        collector.collect_all_chapters(
            [
                ("README.md", "Introduction"),
                ("01-test-chapter", "Test Chapter"),
            ]
        )

        assert "README.md" in state.path_to_chapter
        assert "01-test-chapter" in state.path_to_chapter
        assert "01-test-chapter/README.md" in state.path_to_chapter


# =============================================================================
# HTML 生成测试
# =============================================================================


class TestHTMLGeneration:
    """HTML 生成的测试。"""

    def test_create_chapter_html_overview(self) -> None:
        """测试为概述章节创建 HTML。"""
        html = create_chapter_html(
            display_name="Introduction",
            file_title="Introduction",
            html_content="<p>Content</p>",
            is_overview=True,
        )

        assert "<!DOCTYPE html>" in html
        assert '<html xmlns="http://www.w3.org/1999/xhtml"' in html
        assert "<h1>Introduction</h1>" in html
        assert "<p>Content</p>" in html

    def test_create_chapter_html_section(self) -> None:
        """测试为章节创建 HTML。"""
        html = create_chapter_html(
            display_name="Chapter",
            file_title="Section",
            html_content="<p>Content</p>",
            is_overview=False,
        )

        assert "<h2>Section</h2>" in html
        assert "<h1>" not in html

    def test_html_escaping(self) -> None:
        """测试 HTML 特殊字符被转义。"""
        html = create_chapter_html(
            display_name="<script>alert('xss')</script>",
            file_title="Test & Title",
            html_content="<p>Content</p>",
            is_overview=True,
        )

        assert "&lt;script&gt;" in html
        # 注意：Python 的 html.escape 对单引号使用 &#x27;
        assert "<script>alert" not in html


# =============================================================================
# 章节顺序测试
# =============================================================================


class TestChapterOrder:
    """章节排序的测试。"""

    def test_get_chapter_order(self) -> None:
        """测试章节顺序是否正确定义。"""
        order = get_chapter_order()

        assert len(order) > 0
        assert order[0] == ("README.md", "Introduction")

        # 检查所有预期的章节都存在
        chapter_names = [name for name, _ in order]
        assert "01-slash-commands" in chapter_names
        assert "02-memory" in chapter_names
        assert "resources.md" in chapter_names


# =============================================================================
# 日志测试
# =============================================================================


class TestLogging:
    """日志设置的测试。"""

    def test_setup_logging_default(self) -> None:
        """测试默认日志设置。"""
        logger = setup_logging(verbose=False)
        assert logger.name == "epub_builder"

    def test_setup_logging_verbose(self) -> None:
        """测试详细日志设置。"""
        logger = setup_logging(verbose=True)
        assert logger.name == "epub_builder"


# =============================================================================
# 集成测试
# =============================================================================


class TestIntegration:
    """完整构建过程的集成测试。"""

    @pytest.mark.asyncio
    async def test_build_without_mermaid(
        self, tmp_project: Path, logger: logging.Logger
    ) -> None:
        """测试构建不包含 Mermaid 图表的 EPUB。"""
        from build_epub import build_epub_async

        config = EPUBConfig(
            root_path=tmp_project,
            output_path=tmp_project / "test.epub",
        )

        # 覆盖章节顺序以进行最小化测试
        with patch("build_epub.get_chapter_order") as mock_order:
            mock_order.return_value = [("README.md", "Introduction")]

            result = await build_epub_async(config, logger)

            assert result.exists()
            assert result.suffix == ".epub"


# =============================================================================
# 运行测试
# =============================================================================


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
