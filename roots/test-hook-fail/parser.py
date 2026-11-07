from __future__ import annotations

from argparse import ArgumentParser


def main() -> None:
    print(ArgumentParser(prog="foo", add_help=False))  # noqa: T201
