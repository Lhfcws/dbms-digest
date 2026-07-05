#!/usr/bin/env python3
"""Extract the "PostgreSQL" and "Wider DBMS & distributed data" sections from every
digest and print them as a single continuous feed, newest-first.

Each item is numbered sequentially and prefixed with its week.

Usage:  python3 scripts/extract_pg_wider.py
"""

from __future__ import annotations

import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIGESTS = ROOT / "digests"

# Sections to extract, in order of appearance.
TARGET_SECTIONS = [
    "## PostgreSQL",
    "## Wider DBMS & distributed data",
    "## DBMS & distributed data",          # renamed in some digests
]


def _section_range(lines: list[str], start_heading: str) -> tuple[int, int | None]:
    """Return (start, end) line indices (zero-based) for a section heading.
    *start* is the line containing the heading; *end* is the line just before the
    next ``## `` heading (or None for end-of-file).  Returns (0, 0) if not found."""
    hlevel = start_heading.count("#")
    for i, ln in enumerate(lines):
        if ln.strip() == start_heading.strip():
            for j in range(i + 1, len(lines)):
                if re.match(rf'^{"#" * hlevel}\s', lines[j].strip()):
                    return i, j
            return i, None
    return 0, 0


def extract_items(text: str) -> list[str]:
    """Return every list item (lines starting with ``- `` or ``  - ``) from *text*."""
    items: list[str] = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        ln = lines[i]
        stripped = ln.strip()
        if re.match(r'^- |^  - ', stripped):
            buf = [lines[i]]
            i += 1
            # capture sub-bullets (indented with 4+ spaces or tabs)
            while i < len(lines):
                sub = lines[i]
                if sub.strip() == "":
                    i += 1
                    continue
                if re.match(r'^( {4,}|\t)\S', sub) or re.match(r'^    - ', sub):
                    buf.append(sub)
                    i += 1
                    continue
                break
            items.append("\n".join(buf))
        else:
            i += 1
    return items


def extract_section(lines: list[str], heading: str) -> list[str]:
    """Return list items from the named section of *lines*."""
    start, end = _section_range(lines, heading)
    if start == end:
        return []
    if end is None:
        section_lines = lines[start + 1:]
    else:
        section_lines = lines[start + 1:end]
    return extract_items("\n".join(section_lines))


def main() -> None:
    digest_files = sorted(
        (dt.date.fromisoformat(p.stem), p)
        for p in DIGESTS.glob("20[2-9][0-9]-[01][0-9]-[0-3][0-9].md")
    )
    digest_files.sort(key=lambda t: t[0], reverse=True)  # newest first

    item_count = 0
    for monday, path in digest_files:
        sunday = monday + dt.timedelta(days=6)
        lines = path.read_text(encoding="utf-8").splitlines()
        week_items: list[str] = []
        for heading in TARGET_SECTIONS:
            week_items.extend(extract_section(lines, heading))
        if not week_items:
            continue
        print(f"\n## Week of {monday:%Y-%m-%d} – {sunday:%Y-%m-%d}")
        print()
        for item in week_items:
            item_count += 1
            # strip leading "## " or "### " from sub-headings if they ended up in items
            print(f"{item_count}. {item.strip()}")

    if item_count == 0:
        print("No items found.")
    else:
        print(f"\n---\n{item_count} items across {len(digest_files)} digests.")


if __name__ == "__main__":
    main()
