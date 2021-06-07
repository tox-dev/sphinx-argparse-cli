from __future__ import annotations

import os
from io import StringIO
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
    text = (Path(app.outdir) / f"index.{ext}").read_text()
    return text


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


@pytest.mark.sphinx(buildername="html", testroot="ref")
def test_ref_as_html(build_outcome: str) -> None:
    ref = (
        '<p>Flag <a class="reference internal" href="#prog---root"><span class="std std-ref">prog --root</span></a> and'
        ' positional <a class="reference internal" href="#prog-root"><span class="std std-ref">prog root</span></a>.'
        "</p>"
    )
    assert ref in build_outcome


@pytest.mark.sphinx(buildername="html", testroot="ref-prefix-doc")
def test_ref_prefix_doc(build_outcome: str) -> None:
    ref = (
        '<p>Flag <a class="reference internal" href="#prog---root"><span class="std std-ref">prog --root</span></a> and'
        ' positional <a class="reference internal" href="#prog-root"><span class="std std-ref">prog root</span></a>.'
        "</p>"
    )
    assert ref in build_outcome


_REF_WARNING_STRING_IO = StringIO()  # could not find any better way to get the warning


@pytest.mark.sphinx(buildername="text", testroot="ref-duplicate-label", warning=_REF_WARNING_STRING_IO)
def test_ref_duplicate_label(build_outcome: tuple[str, str]) -> None:
    assert build_outcome
    warnings = _REF_WARNING_STRING_IO.getvalue()
    assert "duplicate label prog---help" in warnings


@pytest.mark.sphinx(buildername="html", testroot="group-title-prefix-default")
def test_group_title_prefix_default(build_outcome: str) -> None:
    assert '<h2>prog positional arguments<a class="headerlink" href="#prog-positional-arguments"' in build_outcome


@pytest.mark.sphinx(buildername="html", testroot="group-title-prefix-empty")
def test_group_title_prefix_empty(build_outcome: str) -> None:
    assert '<h2>positional arguments<a class="headerlink" href="#prog-positional-arguments"' in build_outcome


@pytest.mark.sphinx(buildername="html", testroot="group-title-prefix-custom")
def test_group_title_prefix_custom(build_outcome: str) -> None:
    assert '<h2>custom positional arguments<a class="headerlink" href="#prog-positional-arguments"' in build_outcome


@pytest.mark.sphinx(buildername="html", testroot="group-title-prefix-prog-replacement")
def test_group_title_prefix_prog_replacement(build_outcome: str) -> None:
    assert '<h2>barfoo positional arguments<a class="headerlink" href="#bar-positional-arguments"' in build_outcome


@pytest.mark.sphinx(buildername="html", testroot="group-title-prefix-custom-subcommands")
def test_group_title_prefix_custom_sub_commands(build_outcome: str) -> None:
    assert '<h2>complex Exclusive<a class="headerlink" href="#complex-exclusive"' in build_outcome
    assert '<h2>complex custom (f)<a class="headerlink" href="#complex-first-(f)"' in build_outcome
    msg = '<h3>complex custom positional arguments<a class="headerlink" href="#complex-first-positional-arguments"'
    assert msg in build_outcome
    msg = '<h3>complex custom optional arguments<a class="headerlink" href="#complex-first-optional-arguments"'
    assert msg in build_outcome
    assert '<h2>complex custom<a class="headerlink" href="#complex-second"' in build_outcome
    msg = '<h3>custom-2 optional arguments<a class="headerlink" href="#complex-first-optional-arguments"'
    assert msg in build_outcome
    msg = '<h3>myprog custom-3 optional arguments<a class="headerlink" href="#complex-second-optional-arguments"'
    assert msg in build_outcome


@pytest.mark.sphinx(buildername="html", testroot="group-title-prefix-empty-subcommands")
def test_group_title_prefix_empty_sub_commands(build_outcome: str) -> None:
    assert '<h2>complex Exclusive<a class="headerlink" href="#complex-exclusive"' in build_outcome
    assert '<h2>complex (f)<a class="headerlink" href="#complex-first-(f)"' in build_outcome
    msg = '<h3>complex positional arguments<a class="headerlink" href="#complex-first-positional-arguments"'
    assert msg in build_outcome
    msg = '<h3>complex optional arguments<a class="headerlink" href="#complex-first-optional-arguments"'
    assert msg in build_outcome
    assert '<h2>complex<a class="headerlink" href="#complex-second"' in build_outcome
    msg = '<h3>myprog optional arguments<a class="headerlink" href="#complex-second-optional-arguments"'
    assert msg in build_outcome


@pytest.mark.sphinx(buildername="html", testroot="group-title-empty-prefixes")
def test_group_title_empty_prefixes(build_outcome: str) -> None:
    assert '<h2>Exclusive<a class="headerlink" href="#complex-exclusive"' in build_outcome
    assert '<h2>(f)<a class="headerlink" href="#complex-first-(f)"' in build_outcome
    assert '<h3>positional arguments<a class="headerlink" href="#complex-first-positional-arguments"' in build_outcome
    assert '<h3>optional arguments<a class="headerlink" href="#complex-first-optional-arguments"' in build_outcome
    assert '<h2><a class="headerlink" href="#complex-second"' in build_outcome


@pytest.mark.sphinx(buildername="html", testroot="group-title-prefix-subcommand-replacement")
def test_group_title_prefix_sub_command_replacement(build_outcome: str) -> None:
    assert '<h2>bar optional arguments<a class="headerlink" href="#bar-optional-arguments"' in build_outcome
    assert '<h2>bar Exclusive<a class="headerlink" href="#bar-exclusive"' in build_outcome
    assert '<h2>bar baronlyroot (f)<a class="headerlink" href="#bar-root-first-(f)"' in build_outcome
    assert '<h3>bar baronlyroot first positional arguments<a class="headerlink"' in build_outcome
