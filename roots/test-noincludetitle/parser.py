from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser()
    parser.add_argument("--root", action="store_true", help="root flag")
    return parser
