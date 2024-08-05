from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(description="argparse tester", prog="Prog")
    parser.add_argument("root")
    parser.add_argument("--build", "-B", action="store_true", help="build flag")
    parser.add_argument("--binary", "-b", action="store_true", help="binary flag")
    return parser
