#!/usr/bin/env python3
"""Generate llms.txt and llms-full.txt from Zensical site configuration.

Reads navigation structure from zensical.toml and YAML frontmatter from
each Markdown page to produce two files in docs/:

- llms.txt      — page index with titles, URLs, and descriptions
- llms-full.txt — full Markdown content of every page, concatenated

These files follow the llms.txt specification (https://llmstxt.org/) and
help large language models discover and ingest the site's content.

Usage:
    python scripts/generate_llms_txt.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

try:
    import tomllib
except ImportError:
    import tomli as tomllib  # Python < 3.11 fallback


ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = ROOT / "docs"
CONFIG_FILE = ROOT / "zensical.toml"
SITE_URL = None  # populated from config


def load_config() -> dict:
    with open(CONFIG_FILE, "rb") as f:
        return tomllib.load(f)


def extract_frontmatter(md_path: Path) -> dict:
    """Extract YAML frontmatter from a Markdown file."""
    text = md_path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}
    fm = {}
    for line in match.group(1).splitlines():
        # Simple key: value parser (handles quoted and unquoted values)
        kv = re.match(r'^(\w[\w_]*)\s*:\s*"?(.*?)"?\s*$', line)
        if kv:
            fm[kv.group(1)] = kv.group(2)
    return fm


def extract_body(md_path: Path) -> str:
    """Extract the body content (after frontmatter) from a Markdown file."""
    text = md_path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n.*?\n---\s*\n", text, re.DOTALL)
    if match:
        return text[match.end():]
    return text


def md_to_url(md_filename: str) -> str:
    """Convert a .md filename to a full site URL."""
    if md_filename == "index.md":
        return SITE_URL.rstrip("/") + "/"
    slug = md_filename.removesuffix(".md") + "/"
    return SITE_URL.rstrip("/") + "/" + slug


def walk_nav(nav_items: list) -> list[tuple[str, str, str]]:
    """Walk the nav tree and return flat list of (section, title, md_file).

    Each nav item is a dict with a single key (the title) mapping to either
    a string (filename) or a list (subsection).
    """
    results = []

    def _walk(items: list, section: str = ""):
        for item in items:
            if isinstance(item, str):
                # Bare filename entry (e.g. a section index page): derive the
                # title from the page's frontmatter, falling back to the slug.
                md_path = DOCS_DIR / item
                fm = extract_frontmatter(md_path) if md_path.exists() else {}
                title = fm.get("title") or item.removesuffix(".md").replace("-", " ").capitalize()
                results.append((section, title, item))
            elif isinstance(item, dict):
                for title, value in item.items():
                    if isinstance(value, str):
                        results.append((section, title, value))
                    elif isinstance(value, list):
                        _walk(value, section=title)

    _walk(nav_items)
    return results

def generate_llms_txt(nav_entries: list[tuple[str, str, str]]) -> str:
    """Generate llms.txt content."""
    config = load_config()
    site_name = config["project"].get("site_name", "Documentation")
    site_desc = config["project"].get("site_description", "")

    lines = [f"# {site_name}", ""]
    if site_desc:
        lines.append(f"> {site_desc}")
        lines.append("")

    current_section = None
    for section, title, md_file in nav_entries:
        md_path = DOCS_DIR / md_file
        if not md_path.exists():
            continue

        if section and section != current_section:
            lines.append(f"## {section}")
            lines.append("")
            current_section = section

        fm = extract_frontmatter(md_path)
        description = fm.get("description", "")
        url = md_to_url(md_file)

        if description:
            lines.append(f"- [{title}]({url}): {description}")
        else:
            lines.append(f"- [{title}]({url})")

    lines.append("")
    return "\n".join(lines)


def generate_llms_full_txt(nav_entries: list[tuple[str, str, str]]) -> str:
    """Generate llms-full.txt with full page content."""
    config = load_config()
    site_name = config["project"].get("site_name", "Documentation")
    site_desc = config["project"].get("site_description", "")

    lines = [f"# {site_name}", ""]
    if site_desc:
        lines.append(f"> {site_desc}")
        lines.append("")

    for section, title, md_file in nav_entries:
        md_path = DOCS_DIR / md_file
        if not md_path.exists():
            continue

        url = md_to_url(md_file)
        body = extract_body(md_path).strip()

        lines.append(f"---")
        lines.append(f"")
        lines.append(f"## [{title}]({url})")
        lines.append(f"")
        lines.append(body)
        lines.append("")

    return "\n".join(lines)


def main():
    global SITE_URL

    config = load_config()
    SITE_URL = config["project"].get("site_url", "https://example.com/")
    nav = config["project"].get("nav", [])

    if not nav:
        print("Error: no nav defined in zensical.toml", file=sys.stderr)
        sys.exit(1)

    nav_entries = walk_nav(nav)

    # Generate llms.txt
    llms_txt = generate_llms_txt(nav_entries)
    out_path = DOCS_DIR / "llms.txt"
    out_path.write_text(llms_txt, encoding="utf-8")
    print(f"Generated {out_path} ({len(nav_entries)} pages)")

    # Generate llms-full.txt
    llms_full = generate_llms_full_txt(nav_entries)
    out_full_path = DOCS_DIR / "llms-full.txt"
    out_full_path.write_text(llms_full, encoding="utf-8")
    print(f"Generated {out_full_path} ({len(llms_full)} chars)")


if __name__ == "__main__":
    main()
