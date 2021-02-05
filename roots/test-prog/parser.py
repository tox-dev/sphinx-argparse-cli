from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    return ArgumentParser(add_help=False)
