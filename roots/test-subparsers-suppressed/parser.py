from __future__ import annotations

from argparse import SUPPRESS, ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(prog="prog", add_help=False)
    sub = parser.add_subparsers()
    sub.add_parser("run", help="run it", add_help=False)
    sub.add_parser("secret", help=SUPPRESS, add_help=False)
    return parser
