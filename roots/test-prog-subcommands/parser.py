from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(prog="original-name")
    parser.add_subparsers().add_parser("foo", help="foo help")
    return parser
