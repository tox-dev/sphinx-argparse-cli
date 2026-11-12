from __future__ import annotations

from typing import TYPE_CHECKING

from docutils import __version__ as docutils_version
from sphinx import __display_version__ as sphinx_version

import sphinx_argparse_cli

if TYPE_CHECKING:
    import pytest


def test_version() -> None:
    assert sphinx_argparse_cli.__version__


def test_report_header(request: pytest.FixtureRequest) -> None:
    assert (
        f"libraries: Sphinx-{sphinx_version}, docutils-{docutils_version}"
        in request.config.hook.pytest_report_header(config=request.config, start_path=request.config.rootpath)
    )
