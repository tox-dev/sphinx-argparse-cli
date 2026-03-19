from __future__ import annotations

from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser, RawDescriptionHelpFormatter


class _Formatter(ArgumentDefaultsHelpFormatter, RawDescriptionHelpFormatter): ...


def make() -> ArgumentParser:
    return ArgumentParser(
        prog="foo",
        epilog="""This epilog
spans multiple lines.

  this line is indented.
    and also this.

Now this should be a separate paragraph.
""",
        formatter_class=_Formatter,
        add_help=False,
    )
