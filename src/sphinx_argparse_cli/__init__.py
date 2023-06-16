from __future__ import annotations

from typing import TYPE_CHECKING

from .version import __version__

if TYPE_CHECKING:
    from sphinx.application import Sphinx


def setup(app: Sphinx) -> None:
    app.add_css_file("custom.css")

    from ._logic import SphinxArgparseCli

    app.add_directive(SphinxArgparseCli.name, SphinxArgparseCli)
    app.add_config_value("sphinx_argparse_cli_prefix_document", False, "env")


__all__ = ("__version__",)
