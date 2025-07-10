from __future__ import annotations


def test_version() -> None:
    import sphinx_argparse_cli  # noqa: PLC0415

    assert sphinx_argparse_cli.__version__
