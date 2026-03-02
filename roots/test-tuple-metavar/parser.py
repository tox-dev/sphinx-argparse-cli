from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(prog="tool")
    parser.add_argument("--pair", nargs=2, metavar=("A", "B"), help="select a pair")
    parser.add_argument("--val", metavar="VAL", help="single val")
    return parser
