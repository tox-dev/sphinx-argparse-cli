from __future__ import annotations

from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser


def make() -> ArgumentParser:
    parser = ArgumentParser(
        prog="tool",
        formatter_class=ArgumentDefaultsHelpFormatter,
        description="%(prog)s does things",
        epilog="run %(prog)s --help",
        add_help=False,
    )
    parser.add_argument("--n", type=int, default=3, help="count (default: %(default)s)")
    parser.add_argument("--mode", choices=["a", "b"], default="a", help="pick one of %(choices)s")
    parser.add_argument("--pct", default=5, help="100%% of %(prog)s")
    parser.add_argument("--capital", default=3, help="Default: 3")
    parser.add_argument("--kind", type=float, help="parsed with %(type)s")
    group = parser.add_argument_group("tuning", description="tune %(prog)s")
    group.add_argument("--level", default=1, help="level")
    run = parser.add_subparsers().add_parser("run", description="%(prog)s runs", add_help=False)
    run.add_argument("--target", help="target for %(prog)s")
    return parser
