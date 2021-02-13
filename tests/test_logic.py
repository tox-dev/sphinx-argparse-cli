from __future__ import annotations

from pathlib import Path

import pytest
from _pytest.fixtures import SubRequest
from sphinx.testing.util import SphinxTestApp


@pytest.fixture()
def build_outcome(app: SphinxTestApp, request: SubRequest) -> str:
    app.build()
    ext = {"html": "html", "text": "txt"}
    ext = ext.get(request.node.get_closest_marker("sphinx").args[0])
    assert ext is not None
    return (Path(app.outdir) / f"index.{ext}").read_text()


@pytest.mark.sphinx("html", testroot="basic")
def test_basic_as_html(build_outcome: str) -> None:
    assert build_outcome


@pytest.mark.sphinx("text", testroot="complex")
def test_complex_as_text(build_outcome: str) -> None:
    expected = (Path(__file__).parent / "complex.txt").read_text()
    assert build_outcome == expected


@pytest.mark.sphinx("html", testroot="complex")
def test_complex_as_html(build_outcome: str) -> None:
    assert build_outcome


@pytest.mark.sphinx("text", testroot="prog")
def test_prog_as_text(build_outcome: str) -> None:
    assert build_outcome == "magic - CLI interface\n*********************\n\n   magic\n"


@pytest.mark.sphinx("text", testroot="title-set")
def test_set_title_as_text(build_outcome: str) -> None:
    assert build_outcome == "My own title\n************\n\n   foo\n"


@pytest.mark.sphinx("text", testroot="title-empty")
def test_empty_title_as_text(build_outcome: str) -> None:
    assert build_outcome == "   foo\n"
