from __future__ import annotations

from argparse import ArgumentParser


def main() -> None:
    parser = ArgumentParser(prog="foo", add_help=False)
    parser.add_argument("--flag", help="a flag")
    print(parser.parse_intermixed_args())  # noqa: T201  # the directive's hook raises before the print runs
