from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(prog="python -m build")
    parser.add_argument("srcdir", help="source directory")
    return parser
