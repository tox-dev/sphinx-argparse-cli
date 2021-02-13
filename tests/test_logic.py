from __future__ import annotations

import os
from pathlib import Path
from typing import cast

import pytest
from _pytest.fixtures import SubRequest
from sphinx.testing.util import SphinxTestApp


@pytest.fixture()
def build_outcome(app: SphinxTestApp, request: SubRequest) -> str:
    prepare_marker = request.node.get_closest_marker("prepare")
    if prepare_marker:
        directive_args: list[str] | None = prepare_marker.kwargs.get("directive_args")
        if directive_args:  # pragma: no branch
            index = Path(cast(str, app.confdir)) / "index.rst"
            if not any(i for i in directive_args if i.startswith(":module:")):  # pragma: no branch
                directive_args.append(":module: parser")
            if not any(i for i in directive_args if i.startswith(":func:")):  # pragma: no branch
                directive_args.append(":func: make")
            args = [f"  {i}" for i in directive_args]
            index.write_text(os.linesep.join([".. sphinx_argparse_cli::"] + args))

    ext_mapping = {"html": "html", "text": "txt"}
    sphinx_marker = request.node.get_closest_marker("sphinx")
    assert sphinx_marker is not None
    ext = ext_mapping[sphinx_marker.kwargs.get("buildername")]

    app.build()
    return (Path(app.outdir) / f"index.{ext}").read_text()


@pytest.mark.sphinx(buildername="html", testroot="basic")
def test_basic_as_html(build_outcome: str) -> None:
    assert build_outcome


@pytest.mark.sphinx(buildername="text", testroot="complex")
def test_complex_as_text(build_outcome: str) -> None:
    expected = (Path(__file__).parent / "complex.txt").read_text()
    assert build_outcome == expected


@pytest.mark.sphinx(buildername="html", testroot="complex")
def test_complex_as_html(build_outcome: str) -> None:
    assert build_outcome


@pytest.mark.sphinx(buildername="text", testroot="prog")
def test_prog_as_text(build_outcome: str) -> None:
    assert build_outcome == "magic - CLI interface\n*********************\n\n   magic\n"


@pytest.mark.sphinx(buildername="text", testroot="title-set")
def test_set_title_as_text(build_outcome: str) -> None:
    assert build_outcome == "My own title\n************\n\n   foo\n"


@pytest.mark.sphinx(buildername="text", testroot="title-empty")
def test_empty_title_as_text(build_outcome: str) -> None:
    assert build_outcome == "   foo\n"


@pytest.mark.sphinx(buildername="text", testroot="complex")
@pytest.mark.prepare(directive_args=[":usage_width: 100"])
def test_usage_width_default(build_outcome: str) -> None:
    assert "complex second [-h] [--flag] [--root] one pos_two\n" in build_outcome


@pytest.mark.sphinx(buildername="text", testroot="complex")
@pytest.mark.prepare(directive_args=[":usage_width: 50"])
def test_usage_width_custom(build_outcome: str) -> None:
    assert "complex second [-h] [--flag] [--root]\n" in build_outcome


@pytest.mark.parametrize(
    ("example", "output"),
    [
        ("", ""),
        ("{", "{"),
        ('"', '"'),
        ("'", "'"),
        ("{a}", "``{a}``"),
        ('"a"', '``"a"``'),
        ("'a'", "``'a'``"),
    ],
)
def test_help_loader(example: str, output: str) -> None:
    from sphinx_argparse_cli._logic import load_help_text  # noqa

    result = load_help_text(example)
    assert result == output
