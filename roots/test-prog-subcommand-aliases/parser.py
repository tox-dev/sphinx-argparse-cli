from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(prog="tool")
    run = parser.add_subparsers().add_parser("run", aliases=["r", "go"], help="run help")
    run.add_subparsers().add_parser("local", aliases=["l"], help="run locally")
    return parser
