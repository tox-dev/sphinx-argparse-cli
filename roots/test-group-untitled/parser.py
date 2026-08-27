from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(prog="tool")
    parser.add_argument_group(description="only a description").add_argument("--x", help="x help")
    parser.add_argument_group(description="another").add_argument("--y", help="y help")
    parser.add_argument_group().add_argument("--z", help="z help")
    return parser
