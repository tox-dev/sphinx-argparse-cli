from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(prog="basic")
    parser.add_argument("-d")
    parser.add_argument("-D")
    return parser
