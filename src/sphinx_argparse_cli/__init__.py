"""Sphinx generator for argparse."""

from __future__ import annotations

from ._extension import setup
from .version import __version__

__all__ = [
    "__version__",
    "setup",
]
