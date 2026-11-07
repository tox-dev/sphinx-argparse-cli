from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(prog="test")

    sub_parser = parser.add_subparsers().add_parser("subparser")
    sub_parser.add_argument("foo")

    sub_parser.add_subparsers().add_parser("child_two").add_argument("--bar")

    return parser
