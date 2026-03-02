from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(prog="tool")
    parser.add_argument("--verbose", action="store_true", help="be verbose")
    return parser
