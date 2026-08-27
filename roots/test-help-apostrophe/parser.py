from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(prog="prog", add_help=False)
    parser.add_argument("--a", help="don't use it's value")
    parser.add_argument("--b", help="it's a 'thing' to see")
    return parser
