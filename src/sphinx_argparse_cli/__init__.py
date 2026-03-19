"""Sphinx generator for argparse."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .version import __version__

if TYPE_CHECKING:
    from sphinx.application import Sphinx


def setup(app: Sphinx) -> dict[str, Any]:
    from ._logic import SphinxArgparseCli  # noqa: PLC0415

    app.add_directive(SphinxArgparseCli.name, SphinxArgparseCli)
    app.add_config_value("sphinx_argparse_cli_prefix_document", False, "env")  # noqa: FBT003
    app.add_css_file("sphinx_argparse_cli.css")
    app.connect("build-finished", _write_css)

    return {"parallel_read_safe": True}


def _write_css(app: Sphinx, exception: Exception | None) -> None:
    if exception or not app.builder or app.builder.format != "html":
        return
    from pathlib import Path  # noqa: PLC0415

    static = Path(app.outdir) / "_static"
    static.mkdir(parents=True, exist_ok=True)
    (static / "sphinx_argparse_cli.css").write_text(
        ".sphinx-argparse-cli-wrap pre { white-space: pre-wrap; word-wrap: break-word; }\n"
    )


__all__ = [
    "__version__",
]
