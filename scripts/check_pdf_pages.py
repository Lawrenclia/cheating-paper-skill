#!/usr/bin/env python3
"""Check that a rendered PDF has the expected number of pages."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


def count_with_pypdf(path: Path) -> int | None:
    try:
        from pypdf import PdfReader  # type: ignore
    except Exception:
        return None
    try:
        return len(PdfReader(str(path)).pages)
    except Exception:
        return None


def count_with_pdfinfo(path: Path) -> int | None:
    try:
        proc = subprocess.run(
            ["pdfinfo", str(path)],
            check=False,
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        return None
    if proc.returncode != 0:
        return None
    match = re.search(r"^Pages:\s*(\d+)\s*$", proc.stdout, re.MULTILINE)
    return int(match.group(1)) if match else None


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--expect", type=int, default=2)
    args = parser.parse_args()

    if not args.pdf.exists():
        print(f"ERROR: PDF not found: {args.pdf}", file=sys.stderr)
        return 2

    pages = count_with_pypdf(args.pdf)
    if pages is None:
        pages = count_with_pdfinfo(args.pdf)
    if pages is None:
        print("ERROR: could not determine PDF page count", file=sys.stderr)
        return 3

    print(f"{args.pdf}: {pages} page(s)")
    if pages != args.expect:
        print(f"ERROR: expected exactly {args.expect} page(s)", file=sys.stderr)
        return 1
    print("OK: page count matches")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
