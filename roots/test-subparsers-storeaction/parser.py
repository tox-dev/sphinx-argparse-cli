from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(prog="test")

    sub_parsers = parser.add_subparsers()
    sub_parser = sub_parsers.add_parser("subparser")
    sub_parser.add_argument("foo")

    sub_sub_parsers = sub_parser.add_subparsers()
    sub_sub_parser = sub_sub_parsers.add_parser("child_two")
    sub_sub_parser.add_argument("--bar")

    return parser
