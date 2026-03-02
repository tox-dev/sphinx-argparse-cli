from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(prog="nargs")
    parser.add_argument("pos_optional", nargs="?", default="default_val", help="optional positional")
    parser.add_argument("pos_zero_or_more", nargs="*", help="zero or more positional")
    parser.add_argument("pos_one_or_more", nargs="+", help="one or more positional")
    parser.add_argument("--pair", nargs=2, metavar=("KEY", "VALUE"), help="exactly two args")
    return parser
