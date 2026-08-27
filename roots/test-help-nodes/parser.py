from __future__ import annotations

from argparse import ArgumentParser, RawTextHelpFormatter


def make() -> ArgumentParser:
    parser = ArgumentParser(prog="prog", formatter_class=RawTextHelpFormatter, add_help=False)
    parser.add_argument("--blank", help="   ")
    parser.add_argument("--list", help="- item one\n- item two")
    parser.add_argument("--two", help="first paragraph\n\nsecond paragraph")
    return parser
