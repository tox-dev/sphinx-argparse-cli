"""Sphinx generator for argparse."""

from __future__ import annotations

from typing import TYPE_CHECKING  # simplint: ignore[init-module-content]  # keep setup at the public entry point

from .version import __version__

if TYPE_CHECKING:
    from sphinx.application import Sphinx


def setup(app: Sphinx) -> dict[str, bool]:  # ruff:ignore[non-empty-init-module]  # keep the Sphinx entry point here
    """
    Register the ``sphinx_argparse_cli`` directive, its config value and its stylesheet with Sphinx.

    :returns: Sphinx extension metadata.
    """
    from ._logic import SphinxArgparseCli  # ruff:ignore[import-outside-top-level]  # keeps docutils out of the package import

    app.add_directive(SphinxArgparseCli.name, SphinxArgparseCli)
    app.add_config_value("sphinx_argparse_cli_prefix_document", default=False, rebuild="env")
    app.add_css_file("sphinx_argparse_cli.css")
    app.connect("build-finished", _write_css)

    return {"parallel_read_safe": True}


def _write_css(app: Sphinx, exception: Exception | None) -> None:  # ruff:ignore[non-empty-init-module]  # setup uses this callback
    if exception or not app.builder or app.builder.format != "html":
        return

    from pathlib import Path  # ruff:ignore[import-outside-top-level]  # keep package imports light

    static = Path(app.outdir) / "_static"
    static.mkdir(parents=True, exist_ok=True)
    (static / "sphinx_argparse_cli.css").write_text(
        ".sphinx-argparse-cli-wrap pre { white-space: pre-wrap; word-wrap: break-word; }\n"
    )


__all__ = [
    "__version__",
    "setup",
]
