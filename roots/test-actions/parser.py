from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(prog="actions")
    parser.add_argument("-v", "--verbose", action="count", default=0, help="increase verbosity")
    parser.add_argument("--include", action="append", help="paths to include")
    parser.add_argument("--required-opt", required=True, help="a required optional argument")
    return parser
