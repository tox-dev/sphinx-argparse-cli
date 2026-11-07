from __future__ import annotations

from argparse import ArgumentParser


def main() -> None:
    print(ArgumentParser(prog="foo", add_help=False).parse_args())  # noqa: T201  # the directive's hook raises before the print runs
