from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(prog="choices")
    parser.add_argument("--format", choices=["json", "xml", "csv"], help="output format")
    parser.add_argument("--level", type=int, choices=[1, 2, 3], help="verbosity level")
    return parser
