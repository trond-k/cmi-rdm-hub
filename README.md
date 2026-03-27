# CMI Research Data Management Hub

Research data management guidance for researchers and staff at the Chr. Michelsen Institute (CMI). Built with [Zensical](https://zensical.org/).

**Live site:** <https://trond-k.github.io/cmi-rdm-hub/>

## Structure

```
docs/               Content pages (Markdown)
includes/           Shared snippets (abbreviations, etc.)
overrides/          Theme template overrides
reports/            Funder requirements and theme reports
working-files/      Drafts, early documents, and working notes
zensical.toml       Site configuration
```

## Local development

Requires Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```bash
# Install dependencies
uv sync

# Start the dev server (default: http://localhost:8000)
uv run zensical serve

# Start on a custom port
uv run zensical serve -a localhost:3000

# Open the site in your browser automatically
uv run zensical serve -o

# Build the static site
uv run zensical build
```

## Content organisation

The site follows a 12-stage research data lifecycle grouped into three phases:

| Phase              | Stages                                    |
|--------------------|-------------------------------------------|
| Before the project | Frame, Fund, Plan                         |
| During the project | Collect, Store, Process, Analyse          |
| After the project  | Publish, Preserve, Discover, Access, Share & Reuse |

Cross-cutting guidance (reproducibility, file naming, data inventory) applies across all stages.
