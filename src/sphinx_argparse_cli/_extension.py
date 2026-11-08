from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sphinx.application import Sphinx


def setup(app: Sphinx) -> dict[str, bool]:
    """Register the ``sphinx_argparse_cli`` directive, its config value and its stylesheet with Sphinx."""
    from ._logic import SphinxArgparseCli  # noqa: PLC0415  # keeps docutils out of the package import

    app.add_directive(SphinxArgparseCli.name, SphinxArgparseCli)
    app.add_config_value("sphinx_argparse_cli_prefix_document", False, "env")  # noqa: FBT003  # positional default
    app.add_css_file("sphinx_argparse_cli.css")
    app.connect("build-finished", _write_css)

    return {"parallel_read_safe": True}


def _write_css(app: Sphinx, exception: Exception | None) -> None:
    if exception or not app.builder or app.builder.format != "html":
        return

    static = Path(app.outdir) / "_static"
    static.mkdir(parents=True, exist_ok=True)
    (static / "sphinx_argparse_cli.css").write_text(
        ".sphinx-argparse-cli-wrap pre { white-space: pre-wrap; word-wrap: break-word; }\n"
    )


__all__ = [
    "setup",
]
