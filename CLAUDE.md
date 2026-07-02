# CLAUDE.md — CMI Research Data Management Hub

## Project overview

This is a **static documentation site** for research data management (RDM) guidance at Chr. Michelsen Institute (CMI). It is built with [Zensical](https://zensical.org/) (a Python-based documentation generator) and deployed to GitHub Pages.

**Live site:** https://trond-k.github.io/cmi-rdm-hub/

## Tech stack

- **Generator:** Zensical (>= 0.0.29)
- **Language:** Python 3.12+
- **Package manager:** [uv](https://docs.astral.sh/uv/)
- **Hosting:** GitHub Pages via GitHub Actions
- **No database, no backend, no containers** — this is a pure static site

## Development commands

```bash
uv sync                          # Install dependencies
uv run zensical serve            # Dev server at http://localhost:8000
uv run zensical serve -a localhost:3000  # Custom port
uv run zensical serve -o         # Auto-open in browser
uv run zensical build            # Build static site to site/
python scripts/generate_llms_txt.py   # Regenerate docs/llms.txt and docs/llms-full.txt
```

## Repository structure

```
docs/                  Published content pages (Markdown)
  images/              Embedded images and diagrams
  stylesheets/         Custom CSS (hero.css)
  llms.txt             Auto-generated LLM page index (do not edit)
  llms-full.txt        Auto-generated full-content LLM file (do not edit)
  CROSS-*.md           Topics pages and Perspectives pieces
  lifecycle-*.md       12 lifecycle stage pages
  personal-data-decider.md  Personal data guidance (in nav under Tools and templates)
  index.md             Homepage
includes/              Shared snippets
  abbreviations.md     Global abbreviation definitions (rendered as hover tooltips)
overrides/             Zensical theme template overrides
  home.html            Custom homepage template
scripts/               Build-time utility scripts
  generate_llms_txt.py Generates llms.txt and llms-full.txt from zensical.toml nav
reports/               Funder requirement reports (ERC, Horizon Europe, Norad, RCN)
  themes-reports/      Theme-specific reports
working-files/         Drafts, research notes, and work-in-progress (not published)
  _archive/            Early drafts and archived interactive widget files
  _meta/               AI blueprints, prompt templates, and internal recommendations
  examples/            Example documents (e.g. DMPs)
  (+ subdirectories mirroring the site navigation: before/during/after-the-project,
     foundations, tools-and-templates, topics, data-inventory-approach-cmi)
zensical.toml          Site configuration (navigation, theme, features)
pyproject.toml         Python project metadata
STYLE-GUIDE.md         Content style and tone guidelines (MUST READ)
PERSPECTIVES-GUIDE.md  Style supplement for Perspectives pieces (READ for commentaries)
REVIEW-CHECKLIST.md    Pre-publication quality checklist (MUST READ)
base-content-architecture.md  Early content strategy and lifecycle stage details (predates the current nav)
```

## Content architecture

The site is organised into eight navigation sections defined in `zensical.toml` under the `nav` key:

| Section | Content |
|---------|---------|
| Start here | Landing page (`get-started.md`) |
| Before the project | Phase landing page + Frame, Fund, Plan |
| During the project | Collect, Store, Process, Analyse |
| After the project | Publish, Preserve, Discover, Access, Share & Reuse, Project closure |
| Topics | Nested subsections: Legal (GDPR pages, Sikt notification), Ethics (consent and information letters), Security and data classification, Reproducibility and transparency |
| Tools and templates | Personal data decider, data inventory, DMP template, Sikt form walkthrough, file naming, using the hub with AI assistants |
| Foundations | Core concepts: elements of RDM, CMI context, principles, data sharing, lifecycle overview |
| Perspectives | Short commentaries on recent research or policy developments (see `PERSPECTIVES-GUIDE.md`) |

The 12 lifecycle stages follow three phases (Before / During / After the project). Topics pages apply across all stages.

## Critical style and content rules

**Read `STYLE-GUIDE.md` and `REVIEW-CHECKLIST.md` before writing or editing any content.** For Perspectives pieces (short commentaries on recent research or policy developments), also read `PERSPECTIVES-GUIDE.md`, which supplements the main style guide with a distinct voice, tighter word count (500–800 words), and a canonical structure. Key rules:

### Language
- **British English throughout** (*organised*, *recognised*, *anonymisation*, *centre*, *colour*, *programme*)
- **No em dashes** (—). Use full stops, commas, semicolons, parentheses, or colons instead
- **Oxford comma** always (*data, code, and documentation*)
- **No full stops in abbreviations** (*RDM*, not *R.D.M.*)
- Single quotation marks for direct quotes; double for quotes within quotes
- Dates as *22 March 2026*, not *March 22, 2026*

### Tone
- Voice of a **senior CMI colleague** who is an expert in open science, GDPR, security, and RDM
- **Direct and practical** — lead with the point, not preamble
- Address the reader as **'you'** and **'your project'**, not 'researchers should'
- Honest about uncertainty and trade-offs; no false confidence
- **No AI buzzwords** — avoid *AI-powered*, *leverage AI*, *game-changer*, *cutting-edge*, *unlock insights*, *seamlessly*. Name specific tools and describe what they do

### Page structure
- Every page needs **YAML frontmatter**: `icon`, `title`, `description`, `tags`, `notes`, `date_updated`
- **Italic pyramid summary** (2-4 sentences) immediately below the H1 title
- No heading deeper than H3
- No paragraph exceeds 5 sentences
- No list exceeds 10 items
- No more than 3 consecutive paragraphs without a visual break
- Word count targets: situation pages 400-650 words, lifecycle/reference pages 800-1,500 words

### Markdown conventions
- **Zensical uses Python Markdown** (not CommonMark or GitHub-Flavoured Markdown)
- Internal links point to `.md` files using **relative paths**
- Use **admonitions** (`!!! note`, `!!! tip`, `!!! warning`, etc.) for callouts, not blockquotes. Always give admonitions descriptive custom titles
- Use collapsible admonitions (`???` / `???+`) for secondary content
- Content tabs (`=== "Tab title"`) for parallel alternatives (discipline-specific, tool comparisons)
- Footnotes for citations and legal references only
- No HTML where Markdown or Zensical extensions work (exception: grid card layouts)

### Abbreviations
- Each abbreviation uses **one** definition mechanism: tooltip OR inline expansion, never both
- **Tooltip:** Frequently used, cross-cutting abbreviations (4+ pages) go in `includes/abbreviations.md` in the format `*[ABBR]: Full expansion`. Do **not** also spell them out inline
- **Inline:** Niche or page-specific abbreviations (1-2 pages) are spelled out on first use with the abbreviation in parentheses. Do **not** add them to `abbreviations.md`

## CI/CD

The `.github/workflows/docs.yml` workflow:
- Triggers on push to `main`
- Regenerates the llms.txt files with `python scripts/generate_llms_txt.py`
- Builds with `zensical build --clean`
- Deploys the `site/` directory to GitHub Pages

## Git conventions

- Commit messages are descriptive and start with a verb (*Add*, *Update*, *Fix*, *Restructure*, *Remove*, *Consolidate*)
- Default branch is `main`
- The `site/` directory and `.venv` are git-ignored

## What not to edit

- `uv.lock` — managed automatically by uv
- `site/` — generated build output
- `working-files/` — drafts and research notes; do not publish these directly without review
- `docs/llms.txt` and `docs/llms-full.txt` — auto-generated; run `scripts/generate_llms_txt.py` to regenerate
- `overrides/home.html` — custom homepage template; modify with care

## Common tasks

### Adding a new content page
1. Create a `.md` file in `docs/` with proper YAML frontmatter
2. Add the page to the `nav` array in `zensical.toml`
3. Follow the style guide for tone, structure, and formatting
4. For cross-cutting abbreviations (4+ pages), add to `includes/abbreviations.md`; for niche terms, spell out inline on first use instead
5. Run `python scripts/generate_llms_txt.py` to update llms.txt files
6. Preview with `uv run zensical serve` before committing

### Editing existing content
1. Read `STYLE-GUIDE.md` and `REVIEW-CHECKLIST.md` first
2. Maintain British English spelling
3. Keep the pyramid summary up to date
4. Update `date_updated` in frontmatter
5. If you changed a page title or description, run `python scripts/generate_llms_txt.py`
6. Preview locally before committing
