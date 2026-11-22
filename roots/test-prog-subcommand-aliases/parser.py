from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(prog="tool")
    parser.add_subparsers().add_parser("run", aliases=["r", "go"], help="run help")
    return parser
