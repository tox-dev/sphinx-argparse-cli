from __future__ import annotations

from argparse import ArgumentParser


def main() -> None:
    parser = ArgumentParser(prog="foo", add_help=False)
    parser.add_argument("x", default=1, help="arg (default: True)")
    args = parser.parse_args()
    print(args)
