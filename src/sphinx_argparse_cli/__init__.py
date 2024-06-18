"""Sphinx generator for argparse."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .version import __version__

if TYPE_CHECKING:
    from sphinx.application import Sphinx


def setup(app: Sphinx) -> dict[str, Any]:
    app.add_css_file("custom.css")

    from ._logic import SphinxArgparseCli

    app.add_directive(SphinxArgparseCli.name, SphinxArgparseCli)
    app.add_config_value("sphinx_argparse_cli_prefix_document", False, "env")  # noqa: FBT003

    return {"parallel_read_safe": True}


__all__ = [
    "__version__",
]
