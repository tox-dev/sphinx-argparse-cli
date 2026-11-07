from __future__ import annotations

import sys
from pathlib import Path
from typing import Final

sys.path.insert(0, str(Path(__file__).parent))
extensions = ["sphinx_argparse_cli"]
nitpicky: Final[bool] = True
sphinx_argparse_cli_prefix_document: Final[bool] = True
