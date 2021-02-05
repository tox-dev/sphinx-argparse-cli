from __future__ import annotations

from pathlib import Path

import pytest
from sphinx.testing.util import SphinxTestApp


@pytest.mark.sphinx("html", testroot="basic")
def test_basic_as_text(app: SphinxTestApp) -> None:
    app.build()
    outcome = (Path(app.outdir) / "index.html").read_text()
    assert outcome


@pytest.mark.sphinx("html", testroot="complex")
def test_complex_as_text(app: SphinxTestApp) -> None:
    app.build()
    outcome = (Path(app.outdir) / "index.html").read_text()
    assert outcome
