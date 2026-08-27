from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(prog="prog", add_help=False)
    parser.add_argument("--flag", help="a flag")
    parser.add_subparsers().add_parser("run", add_help=False).add_argument("--magic", help="magic")
    return parser
