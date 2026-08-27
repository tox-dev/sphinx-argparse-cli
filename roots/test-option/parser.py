from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(description="argparse tester", prog="prog")
    parser.add_argument("--root", "-r", action="store_true", help="root flag")
    run = parser.add_subparsers().add_parser("run", help="run it")
    run.add_argument("target")
    run.add_argument("--magic", help="magic")
    return parser
