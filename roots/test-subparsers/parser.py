from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(prog="test")

    sub_parsers = parser.add_subparsers()
    sub_parser = sub_parsers.add_parser("subparser")
    sub_parser.add_argument("--foo")

    sub_parser_no_child = sub_parsers.add_parser("no_child")
    sub_parser_no_child.add_argument("argument_one", help="no_child argument")

    sub_sub_parsers = sub_parser.add_subparsers()
    sub_sub_parser = sub_sub_parsers.add_parser("child_two")

    sub_sub_sub_parsers = sub_sub_parser.add_subparsers()
    sub_sub_sub_parser = sub_sub_sub_parsers.add_parser("child_three")
    sub_sub_sub_parser.add_argument("argument", help="sub sub sub child pos argument")
    sub_sub_sub_parser.add_argument("--flag", help="sub sub sub child argument")

    return parser
