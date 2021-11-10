from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(prog="basic")
    parser.add_argument("--no-foo", dest="foo", action="store_false")
    parser.add_argument("--bar", dest="bar", action="store_true")
    return parser
