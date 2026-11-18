from __future__ import annotations

from argparse import ArgumentParser


def main() -> None:
    print(ArgumentParser(prog="foo", add_help=False))  # ruff:ignore[print]  # no parse call, so the hook finds no parser
