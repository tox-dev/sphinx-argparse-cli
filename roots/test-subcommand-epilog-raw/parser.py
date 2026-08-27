from __future__ import annotations

from argparse import ArgumentParser, RawDescriptionHelpFormatter


def make() -> ArgumentParser:
    parser = ArgumentParser(
        prog="prog",
        description="root description\n  kept as is",
        epilog="root epilog\n  kept as is",
        formatter_class=RawDescriptionHelpFormatter,
        add_help=False,
    )
    sub = parser.add_subparsers()
    sub.add_parser(
        "raw",
        description="raw description\n  kept as is",
        epilog="raw epilog\n  kept as is",
        formatter_class=RawDescriptionHelpFormatter,
        add_help=False,
    ).add_argument("--flag", help="raw flag")
    sub.add_parser(
        "plain", description="plain description\n  reflowed", epilog="plain epilog\n  reflowed", add_help=False
    )
    return parser
