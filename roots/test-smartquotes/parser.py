from __future__ import annotations

from argparse import ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(
        prog="smartquotes",
        description="Pass input via --text or stdin.",
        epilog="Read the --text docs; see also --2fa and --dry_run.",
    )
    parser.add_argument("--text", help="text to encode; combine with --output for files")
    parser.add_argument(
        "--typography", help="typography still applies to non-options like these north--south and 10--20"
    )
    parser.add_subparsers().add_parser("build", help="build things with --flair")
    return parser
