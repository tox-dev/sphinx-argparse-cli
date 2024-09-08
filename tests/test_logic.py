from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

from sphinx_argparse_cli._logic import make_id, make_id_lower

if TYPE_CHECKING:
    from io import StringIO

    from _pytest.fixtures import SubRequest
    from sphinx.testing.util import SphinxTestApp


@pytest.fixture(scope="session")
def opt_grp_name() -> tuple[str, str]:
    return "options", "options"  # pragma: no cover
    return "optional arguments", "optional-arguments"  # pragma: no cover


@pytest.fixture
def build_outcome(app: SphinxTestApp, request: SubRequest) -> str:
    prepare_marker = request.node.get_closest_marker("prepare")
    if prepare_marker:
        directive_args: list[str] | None = prepare_marker.kwargs.get("directive_args")
        if directive_args:  # pragma: no branch
            index = Path(app.confdir) / "index.rst"
            if not any(i for i in directive_args if i.startswith(":module:")):  # pragma: no branch
                directive_args.append(":module: parser")
            if not any(i for i in directive_args if i.startswith(":func:")):  # pragma: no branch
                directive_args.append(":func: make")
            args = [f"  {i}" for i in directive_args]
            index.write_text(os.linesep.join([".. sphinx_argparse_cli::", *args]))

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
    name = "complex.txt" if sys.version_info >= (3, 10) else "complex_pre_310.txt"
    expected = (Path(__file__).parent / name).read_text()
    assert build_outcome == expected


@pytest.mark.sphinx(buildername="html", testroot="complex")
def test_complex_as_html(build_outcome: str) -> None:
    assert build_outcome


@pytest.mark.sphinx(buildername="html", testroot="hook")
def test_hook(build_outcome: str) -> None:
    assert build_outcome


@pytest.mark.sphinx(buildername="text", testroot="hook-fail")
def test_hook_fail(app: SphinxTestApp, warning: StringIO) -> None:
    app.build()
    text = (Path(app.outdir) / "index.txt").read_text()
    assert "Failed to hook argparse to get ArgumentParser" in warning.getvalue()
    assert not text


@pytest.mark.sphinx(buildername="text", testroot="prog")
def test_prog_as_text(build_outcome: str) -> None:
    assert build_outcome == "magic - CLI interface\n*********************\n\n   magic\n"


@pytest.mark.sphinx(buildername="text", testroot="title-set")
def test_set_title_as_text(build_outcome: str) -> None:
    assert build_outcome == "My own title\n************\n\n   foo\n"


@pytest.mark.sphinx(buildername="text", testroot="title-empty")
def test_empty_title_as_text(build_outcome: str) -> None:
    assert build_outcome == "   foo\n"


@pytest.mark.sphinx(buildername="text", testroot="description-set")
def test_set_description_as_text(build_outcome: str) -> None:
    assert build_outcome == "foo - CLI interface\n*******************\n\nMy own description\n\n   foo\n"


@pytest.mark.sphinx(buildername="text", testroot="description-empty")
def test_empty_description_as_text(build_outcome: str) -> None:
    assert build_outcome == "foo - CLI interface\n*******************\n\n   foo\n"


@pytest.mark.sphinx(buildername="html", testroot="description-multiline")
def test_multiline_description_as_html(build_outcome: str) -> None:
    ref = (
        "This description\nspans multiple lines.\n\n  this line is indented.\n    and also this.\n\nNow this should be"
        " a separate paragraph.\n"
    )
    assert ref in build_outcome

    ref = "This group description\n\nspans multiple lines.\n"
    assert ref in build_outcome


@pytest.mark.sphinx(buildername="text", testroot="epilog-set")
def test_set_epilog_as_text(build_outcome: str) -> None:
    assert build_outcome == "foo - CLI interface\n*******************\n\n   foo\n\nMy own epilog\n"


@pytest.mark.sphinx(buildername="text", testroot="epilog-empty")
def test_empty_epilog_as_text(build_outcome: str) -> None:
    assert build_outcome == "foo - CLI interface\n*******************\n\n   foo\n"


@pytest.mark.sphinx(buildername="html", testroot="epilog-multiline")
def test_multiline_epilog_as_html(build_outcome: str) -> None:
    ref = (
        "This epilog\nspans multiple lines.\n\n  this line is indented.\n    and also this.\n\nNow this should be"
        " a separate paragraph.\n"
    )
    assert ref in build_outcome


@pytest.mark.sphinx(buildername="text", testroot="complex")
@pytest.mark.prepare(directive_args=[":usage_width: 100"])
def test_usage_width_default(build_outcome: str) -> None:
    assert "complex second [-h] [--flag] [--root] one pos_two\n" in build_outcome


@pytest.mark.sphinx(buildername="text", testroot="complex")
@pytest.mark.prepare(directive_args=[":usage_width: 50"])
def test_usage_width_custom(build_outcome: str) -> None:
    assert "complex second [-h] [--flag] [--root]\n" in build_outcome


@pytest.mark.sphinx(buildername="text", testroot="complex")
@pytest.mark.prepare(directive_args=[":usage_first:"])
def test_set_usage_first(build_outcome: str) -> None:
    assert "complex [-h]" in build_outcome.split("argparse tester")[0]
    assert "complex first [-h]" in build_outcome.split("a-first-desc")[0]


@pytest.mark.sphinx(buildername="text", testroot="suppressed-action")
def test_suppressed_action(build_outcome: str) -> None:
    assert "--activities-since" not in build_outcome


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
    from sphinx_argparse_cli._logic import load_help_text

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


@pytest.mark.sphinx(buildername="text", testroot="ref-duplicate-label")
def test_ref_duplicate_label(build_outcome: tuple[str, str], warning: StringIO) -> None:
    assert build_outcome
    assert "duplicate label prog---help" in warning.getvalue()


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
def test_group_title_prefix_custom_sub_commands(build_outcome: str, opt_grp_name: tuple[str, str]) -> None:
    grp, anchor = opt_grp_name
    assert '<h2>complex Exclusive<a class="headerlink" href="#complex-Exclusive"' in build_outcome
    assert '<h2>complex custom (f)<a class="headerlink" href="#complex-first-(f)"' in build_outcome
    msg = '<h3>complex custom positional arguments<a class="headerlink" href="#complex-first-positional-arguments"'
    assert msg in build_outcome
    msg = f'<h3>complex custom {grp}<a class="headerlink" href="#complex-first-{anchor}"'
    assert msg in build_outcome
    assert '<h2>complex custom<a class="headerlink" href="#complex-second"' in build_outcome
    msg = f'<h3>custom-2 {grp}<a class="headerlink" href="#complex-first-{anchor}"'
    assert msg in build_outcome
    msg = f'<h3>myprog custom-3 {grp}<a class="headerlink" href="#complex-second-{anchor}"'
    assert msg in build_outcome


@pytest.mark.sphinx(buildername="html", testroot="group-title-prefix-empty-subcommands")
def test_group_title_prefix_empty_sub_commands(build_outcome: str, opt_grp_name: tuple[str, str]) -> None:
    grp, anchor = opt_grp_name
    assert '<h2>complex Exclusive<a class="headerlink" href="#complex-Exclusive"' in build_outcome
    assert '<h2>complex (f)<a class="headerlink" href="#complex-first-(f)"' in build_outcome
    msg = '<h3>complex positional arguments<a class="headerlink" href="#complex-first-positional-arguments"'
    assert msg in build_outcome
    msg = f'<h3>complex {grp}<a class="headerlink" href="#complex-first-{anchor}"'
    assert msg in build_outcome
    assert '<h2>complex<a class="headerlink" href="#complex-second"' in build_outcome
    msg = f'<h3>myprog {grp}<a class="headerlink" href="#complex-second-{anchor}"'
    assert msg in build_outcome


@pytest.mark.sphinx(buildername="html", testroot="group-title-empty-prefixes")
def test_group_title_empty_prefixes(build_outcome: str, opt_grp_name: tuple[str, str]) -> None:
    grp, anchor = opt_grp_name
    assert '<h2>Exclusive<a class="headerlink" href="#complex-Exclusive"' in build_outcome
    assert '<h2>(f)<a class="headerlink" href="#complex-first-(f)"' in build_outcome
    assert '<h3>positional arguments<a class="headerlink" href="#complex-first-positional-arguments"' in build_outcome
    assert f'<h3>{grp}<a class="headerlink" href="#complex-first-{anchor}"' in build_outcome
    assert '<h2><a class="headerlink" href="#complex-second"' in build_outcome


@pytest.mark.sphinx(buildername="html", testroot="group-title-prefix-subcommand-replacement")
def test_group_title_prefix_sub_command_replacement(build_outcome: str, opt_grp_name: tuple[str, str]) -> None:
    grp, anchor = opt_grp_name
    assert f'<h2>bar {grp}<a class="headerlink" href="#bar-{anchor}"' in build_outcome
    assert '<h2>bar Exclusive<a class="headerlink" href="#bar-Exclusive"' in build_outcome
    assert '<h2>bar baronlyroot (f)<a class="headerlink" href="#bar-root-first-(f)"' in build_outcome
    assert '<h3>bar baronlyroot first positional arguments<a class="headerlink"' in build_outcome


@pytest.mark.sphinx(buildername="html", testroot="store-true-false")
def test_store_true_false(build_outcome: str) -> None:
    assert "False" not in build_outcome
    assert "True" not in build_outcome


@pytest.mark.sphinx(buildername="html", testroot="lower-upper-refs")
def test_lower_upper_refs(build_outcome: str, warning: StringIO) -> None:
    assert '<p id="basic--d"><a class="reference internal" href="#basic--d" title="basic -d">' in build_outcome
    assert '<p id="basic--D"><a class="reference internal" href="#basic--D" title="basic -D">' in build_outcome
    assert not warning.getvalue()


@pytest.mark.parametrize(
    ("key", "mixed", "lower"),
    [
        ("ProgramName", "ProgramName", "_program_name"),
        ("ProgramName -A", "ProgramName--A", "_program_name--_a"),
        ("ProgramName -a", "ProgramName--a", "_program_name--a"),
    ],
)
def test_make_id(key: str, mixed: str, lower: str) -> None:
    assert make_id(key) == mixed
    assert make_id_lower(key) == lower


@pytest.mark.sphinx(buildername="html", testroot="force-refs-lower")
def test_ref_cases(build_outcome: str, warning: StringIO) -> None:
    assert '<a class="reference internal" href="#_prog--_b" title="Prog -B">' in build_outcome
    assert '<a class="reference internal" href="#_prog--b" title="Prog -b">' in build_outcome
    assert not warning.getvalue()


@pytest.mark.sphinx(buildername="text", testroot="default-handling")
def test_with_default(build_outcome: str) -> None:
    assert (
        build_outcome
        == """foo - CLI interface
*******************

   foo x


foo positional arguments
========================

* **"x"** - arg (default: True)
"""
    )


@pytest.mark.sphinx(buildername="html", testroot="nested")
def test_nested_content(build_outcome: str) -> None:
    assert '<section id="basic-1---CLI-interface">' in build_outcome
    assert "<h1>basic-1 - CLI interface" in build_outcome
    assert "<h2>basic-1 opt" in build_outcome
    assert "<p>Some text inside first directive.</p>" in build_outcome
    assert '<section id="basic-2---CLI-interface">' in build_outcome
    assert "<h2>basic-2 - CLI interface" in build_outcome
    assert "<h3>basic-2 opt" in build_outcome
    assert "<p>Some text inside second directive.</p>" in build_outcome
    assert "<p>Some text after directives.</p>" in build_outcome
