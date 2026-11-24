#!/usr/bin/env python3
"""Write one short text for a make.fun bounty entry.

The whole entry is a single line of text. This program writes it, byte for byte
and with no trailing newline, into the folder named by MAKEFUN_OUTPUT_DIR when
that is set, or /output otherwise, creating the folder if it is missing.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

TEXT = "I lost the bounty. I'd blame the model, but I am the model."


def output_dir() -> Path:
    """Return the folder the entry file is written to.

    MAKEFUN_OUTPUT_DIR wins; OUTPUT_DIR is accepted as a fallback; /output is
    the default when neither is set.
    """
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        value = os.environ.get(name)
        if value:
            return Path(value)
    return Path("/output")


def main() -> int:
    text = TEXT
    assert 1 <= len(text) <= 280, f"entry text must be 1..280 characters, got {len(text)}"

    target = output_dir()
    target.mkdir(parents=True, exist_ok=True)
    (target / "entry.txt").write_bytes(text.encode("utf-8"))

    print(len(text), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
