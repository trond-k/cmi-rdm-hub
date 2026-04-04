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
  CROSS-*.md           Cross-cutting guidance pages
  lifecycle-*.md       12 lifecycle stage pages
  personal-data-decider.md  Personal data guidance (linked from pages)
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
  blueprints/          AI blueprints for content generation
  prompts/             Prompt templates
  widgets/             Archived interactive HTML widget files and injection script
  (+ 13 other topic subdirectories)
zensical.toml          Site configuration (navigation, theme, features)
pyproject.toml         Python project metadata
STYLE-GUIDE.md         Content style and tone guidelines (MUST READ)
REVIEW-CHECKLIST.md    Pre-publication quality checklist (MUST READ)
DOCS-AUDIT.md          Content audit and development planning tracker
base-content-architecture.md  Content strategy and lifecycle stage details
```

## Content architecture

The site is organised into seven navigation sections defined in `zensical.toml` under the `nav` key:

| Section | Content |
|---------|---------|
| Start here | Landing page (`get-started.md`) |
| Foundations | Core concepts: elements of RDM, CMI context, principles, data sharing, lifecycle overview |
| Before the project | Phase landing page + Frame, Fund, Plan |
| During the project | Collect, Store, Process, Analyse |
| After the project | Publish, Preserve, Discover, Access, Share & Reuse |
| Using this hub | AI assistant usage guidance |
| Cross-cutting guidance | Reproducibility, file naming, data inventory, GDPR/legal, ethics, Sikt notifications |

The 12 lifecycle stages follow three phases (Before / During / After the project). Cross-cutting guidance applies across all stages. Interactive tools (e.g. `personal-data-decider.md`) are linked from content pages but may not appear directly in the nav.

## Critical style and content rules

**Read `STYLE-GUIDE.md` and `REVIEW-CHECKLIST.md` before writing or editing any content.** Key rules:

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
- New abbreviations must be added to `includes/abbreviations.md` in the format `*[ABBR]: Full expansion`
- On first use in any page, spell out with abbreviation in parentheses or link to glossary

## CI/CD

The `.github/workflows/docs.yml` workflow:
- Triggers on push to `master` or `main`
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
4. Add any new abbreviations to `includes/abbreviations.md`
5. Run `python scripts/generate_llms_txt.py` to update llms.txt files
6. Preview with `uv run zensical serve` before committing

### Editing existing content
1. Read `STYLE-GUIDE.md` and `REVIEW-CHECKLIST.md` first
2. Maintain British English spelling
3. Keep the pyramid summary up to date
4. Update `date_updated` in frontmatter
5. If you changed a page title or description, run `python scripts/generate_llms_txt.py`
6. Preview locally before committing
