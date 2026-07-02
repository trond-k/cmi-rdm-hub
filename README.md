# CMI Research Data Management Hub

Research data management guidance for researchers and staff at the Chr. Michelsen Institute (CMI). Built with [Zensical](https://zensical.org/).

**Live site:** <https://trond-k.github.io/cmi-rdm-hub/>

## Structure

```
docs/               Content pages (Markdown)
includes/           Shared snippets (abbreviations, etc.)
overrides/          Theme template overrides
reports/            Funder requirements and theme reports
scripts/            Build-time utilities (llms.txt generation)
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
| After the project  | Publish, Preserve, Discover, Access, Share & Reuse, Project closure |

Four further sections support the lifecycle stages:

- **Topics**: guidance that runs across stages (GDPR and legal, ethics and consent, Sikt notifications, data classification, reproducibility and transparency)
- **Tools and templates**: working instruments (personal data decider, data inventory, DMP template, Sikt form walkthrough, file naming, using the hub with AI assistants)
- **Foundations**: core concepts (elements of RDM, CMI's institutional context, RDM principles, data sharing, the lifecycle itself)
- **Perspectives**: short commentaries on recent research and policy developments
