from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(prog="prog", add_help=False)
    parser.add_argument("root", help="root positional")
    first = parser.add_subparsers(title="commands").add_parser("first", aliases=["f"], add_help=False)
    first.add_argument("--flag", help="first flag")
    first.add_subparsers(title="commands").add_parser("nested", add_help=False).add_argument("--deep", help="deep flag")
    return parser
