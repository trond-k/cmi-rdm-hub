#!/usr/bin/env python3
"""Inject widget HTML into Markdown pages at build time.

Scans docs/ for lines matching the pattern:

    <!-- widget: filename.html -->

and replaces them with the contents of includes/filename.html.

Run this before `zensical build` to embed interactive widgets without
needing the pymdownx.snippets extension (which overrides Zensical's
built-in markdown extension defaults).

Usage:
    python scripts/inject_widgets.py
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
INCLUDES_DIR = ROOT / "includes"

WIDGET_PATTERN = re.compile(r"^<!-- widget: (.+?) -->$")


def process_file(md_path: Path) -> bool:
    """Process a single markdown file. Returns True if modified."""
    lines = md_path.read_text(encoding="utf-8").splitlines(keepends=True)
    modified = False
    output = []

    # Track whether we're inside an already-injected widget block
    skip_until_end = False

    for line in lines:
        stripped = line.strip()

        # Skip previously injected content between markers
        if stripped == "<!-- widget-end -->":
            skip_until_end = False
            continue
        if skip_until_end:
            continue

        match = WIDGET_PATTERN.match(stripped)
        if match:
            widget_file = match.group(1)
            widget_path = INCLUDES_DIR / widget_file
            if not widget_path.exists():
                print(f"  Warning: {widget_file} not found in includes/")
                output.append(line)
                continue

            widget_html = widget_path.read_text(encoding="utf-8")
            output.append(line)  # Keep the marker comment
            output.append("\n")
            output.append(widget_html)
            output.append("\n")
            output.append("<!-- widget-end -->\n")
            modified = True
            skip_until_end = True
        else:
            output.append(line)

    if modified:
        md_path.write_text("".join(output), encoding="utf-8")

    return modified


def main():
    count = 0
    for md_path in sorted(DOCS_DIR.glob("*.md")):
        if process_file(md_path):
            print(f"  Injected widgets in {md_path.name}")
            count += 1

    if count:
        print(f"Processed {count} file(s)")
    else:
        print("No widget placeholders found")


if __name__ == "__main__":
    main()
