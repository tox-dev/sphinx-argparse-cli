from __future__ import annotations

from argparse import ArgumentParser, RawDescriptionHelpFormatter


def make() -> ArgumentParser:
    return ArgumentParser(
        prog="foo",
        description="""This description
spans multiple lines.

  this line is indented.
    and also this.

Now this should be a separate paragraph.
""",
        formatter_class=RawDescriptionHelpFormatter,
        add_help=False
    )
