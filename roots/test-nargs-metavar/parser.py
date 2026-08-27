from __future__ import annotations

from argparse import REMAINDER, ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(prog="tool", add_help=False)
    parser.add_argument("--opt", nargs="?", help="optional value")
    parser.add_argument("--many", nargs="*", help="zero or more")
    parser.add_argument("--two", nargs=2, help="exactly two")
    parser.add_argument("--rest", nargs=REMAINDER, help="the rest")
    parser.add_argument("--out", metavar="<file>", help="output")
    parser.add_argument("--dir", metavar="path/to/dir", help="dir")
    parser.add_argument("--format", choices=["json", "xml"], help="output format")
    parser.add_argument("pair", nargs=2, metavar=("SRC", "DST"), help="copy pair")
    return parser
