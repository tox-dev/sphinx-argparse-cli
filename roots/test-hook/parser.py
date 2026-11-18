from __future__ import annotations

from argparse import ArgumentParser


def main() -> None:
    print(ArgumentParser(prog="foo", add_help=False).parse_args())  # ruff:ignore[print]  # the directive's hook raises before the print runs
