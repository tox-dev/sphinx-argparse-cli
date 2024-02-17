from __future__ import annotations

from argparse import SUPPRESS, ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(prog="foo", description="desc", add_help=False)
    parser.add_argument(
        "--activities-since",
        metavar="TIMESTAMP",
        help=SUPPRESS,
    )
    return parser
