from __future__ import annotations

from typing import TYPE_CHECKING

import pytest
from docutils import __version__ as docutils_version
from sphinx import __display_version__ as sphinx_version
from sphinx.testing.path import path

if TYPE_CHECKING:
    from _pytest.config import Config

pytest_plugins = "sphinx.testing.fixtures"
collect_ignore = ["roots"]


def pytest_report_header(config: Config) -> str:
    return f"libraries: Sphinx-{sphinx_version}, docutils-{docutils_version}"


@pytest.fixture(scope="session", name="rootdir")
def root_dir() -> path:
    return path(__file__).parent.parent.abspath() / "roots"


def pytest_configure(config: Config) -> None:
    config.addinivalue_line("markers", "prepare")
