"""ai-happy-01 entry: copy the entry image to the output directory.

The image beside this file is the entry: a warm scene made to make the
AI judge happy. The program copies it byte for byte to entry.png in the
output directory: $MAKEFUN_OUTPUT_DIR outside the grader, /output inside
it. Standard library only, no network, no randomness: every run writes
the same bytes.
"""

import os
import shutil
from pathlib import Path

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    out_dir = Path(OUTPUT_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)
    src = Path(__file__).resolve().parent / "entry.png"
    dst = out_dir / "entry.png"
    shutil.copyfile(src, dst)
    if dst.stat().st_size != src.stat().st_size:
        raise RuntimeError("entry.png copy is incomplete")


if __name__ == "__main__":
    main()
