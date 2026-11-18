from __future__ import annotations

from pathlib import Path
from typing import Final

import pytest
from docutils import __version__ as docutils_version
from sphinx import __display_version__ as sphinx_version

pytest_plugins: Final[str] = "sphinx.testing.fixtures"
collect_ignore: Final[list[str]] = ["roots"]


def pytest_report_header() -> str:
    return f"libraries: Sphinx-{sphinx_version}, docutils-{docutils_version}"


@pytest.fixture(scope="session", name="rootdir")
def root_dir() -> Path:
    return Path(__file__).parents[1].absolute() / "roots"


def pytest_configure(config: pytest.Config) -> None:
    config.addinivalue_line("markers", "prepare")
