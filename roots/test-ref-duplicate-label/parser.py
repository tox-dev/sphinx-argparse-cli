from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(description="argparse tester", prog="prog")
    parser.add_argument("root")
    parser.add_argument("--root", action="store_true", help="root flag")
    return parser
