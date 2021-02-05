from __future__ import annotations

from pathlib import Path

import pytest
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("html", testroot="basic")
def test_basic_as_html(app: SphinxTestApp) -> None:
    app.build()
    outcome = (Path(app.outdir) / "index.html").read_text()
    assert outcome


@pytest.mark.sphinx("html", testroot="complex")
def test_complex_as_html(app: SphinxTestApp) -> None:
    app.build()
    outcome = (Path(app.outdir) / "index.html").read_text()
    assert outcome


@pytest.mark.sphinx("text", testroot="prog")
def test_prog_as_text(app: SphinxTestApp) -> None:
    app.build()
    outcome = (Path(app.outdir) / "index.txt").read_text()
    assert outcome == "magic - CLI interface\n*********************\n\n   magic\n"


@pytest.mark.sphinx("text", testroot="noincludetitle")
def test_noincludetitle_as_text(app: SphinxTestApp) -> None:
    app.build()
    outcome = (Path(app.outdir) / "index.txt").read_text()
    assert outcome.startswith("   ")
    assert "CLI interface" not in outcome
    assert "optional arguments\n==================" in outcome
