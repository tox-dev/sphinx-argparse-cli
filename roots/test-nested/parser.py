from __future__ import annotations

from argparse import ArgumentParser


def make_1() -> ArgumentParser:
    return ArgumentParser(prog="basic-1")

def make_2() -> ArgumentParser:
    return ArgumentParser(prog="basic-2")