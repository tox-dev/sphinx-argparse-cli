from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    return ArgumentParser(prog="foo", add_help=False)
