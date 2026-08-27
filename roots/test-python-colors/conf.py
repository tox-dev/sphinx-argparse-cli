from __future__ import annotations

import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
os.environ["PYTHON_COLORS"] = "1"
extensions = ["sphinx_argparse_cli"]
nitpicky = True
