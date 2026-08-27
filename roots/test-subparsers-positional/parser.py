from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(prog="prog", add_help=False)
    parser.add_argument("root", help="root positional")
    run = parser.add_subparsers().add_parser("run", add_help=False)
    run.add_argument("target", help="run positional")
    run.add_subparsers().add_parser("go", add_help=False).add_argument("--flag", help="go flag")
    return parser
