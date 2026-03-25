# Review Checklist — CMI RDM Guide

Use this checklist when reviewing content before publishing or merging. It complements the [Style Guide](STYLE-GUIDE.md), which governs voice, tone, and language during writing and generation.

---

## Page metadata

Every content page must include YAML frontmatter with the following fields:

```yaml
---
icon: lucide/icon-name
title: "Page title"
description: "One-sentence summary of the page."
tags:
  - Topic tag
  - Another tag
notes: ""
date_updated: 2026-03-24
---
```

- **`icon`**: A Lucide icon name. Optional for body pages, recommended for index and stage pages.
- **`title`**: The page title as it appears in navigation. Derive from the H1 heading if in doubt.
- **`description`**: A one-sentence summary used in search results and social previews.
- **`tags`**: Topic tags for cross-cutting discovery (e.g. `GDPR`, `Frame`, `Security`, `Tool`). Use an empty list `[]` for index pages. See [Zensical tags documentation](https://zensical.org/docs/setup/tags/) for rendering details.
- **`notes`**: Internal editorial notes (e.g. `"Stub — content pending"`, `"align or merge with X"`). Use `""` when there is nothing to flag.
- **`date_updated`**: The date the page content was last substantively updated, in `YYYY-MM-DD` format.

## Currency and review dates

Pages covering rapidly evolving topics (AI tools, specific funder policies, data protection law) should include a **review note** at the bottom of the page:

```markdown
!!! info "Last reviewed"
    This page was last reviewed on 22 March 2026. For rapidly changing
    topics, verify against the latest source.
```

This is not required for stable, foundational content (glossary definitions, general principles) but should be used wherever the guidance has a shelf life.

---

## Zensical and Markdown conventions

### Markdown flavour

Zensical uses **Python Markdown** with extensions. This is not CommonMark or GitHub-Flavoured Markdown; be aware of minor syntax differences (e.g. indentation rules for nested content). Refer to the [Zensical authoring documentation](https://zensical.org/docs/authoring/markdown/) for specifics.

### Internal links

Always link to the **Markdown source file**, not to the generated HTML path. Zensical translates these to the correct output URLs automatically.

```markdown
See the [PLAN stage](../stages/plan.md) for details.
```

Use **relative paths**, not absolute paths. This ensures links survive site restructuring and work correctly regardless of the `use_directory_urls` setting.

### Abbreviations and the global glossary file

Zensical supports automatic abbreviation tooltips via the `abbr` extension and `pymdownx.snippets`. This is the primary mechanism for making abbreviations accessible throughout the guide without repeating definitions on every page.

Maintain a single file at `includes/abbreviations.md` (a dotfile inside `docs/`, hidden from navigation) containing all abbreviation definitions:

```markdown
*[RDM]: Research Data Management
*[DMP]: Data Management Plan
*[DOI]: Digital Object Identifier
*[ORCID]: Open Researcher and Contributor ID
*[FAIR]: Findable, Accessible, Interoperable, Reusable
*[GDPR]: General Data Protection Regulation
*[CARE]: Collective Benefit, Authority to Control, Responsibility, Ethics
*[PID]: Persistent Identifier
*[LLM]: Large Language Model
*[OCR]: Optical Character Recognition
*[API]: Application Programming Interface
```

Configure auto-append in the project configuration so that every page inherits these definitions:

```toml
[project.markdown_extensions.pymdownx.snippets]
auto_append = [".abbreviations.md"]
```

**When to add to the abbreviations file:** whenever a new abbreviation or acronym is introduced in any content page, add its definition to `includes/abbreviations.md`.

### Admonitions

Use admonitions for call-outs, warnings, tips, and notes. Do not use blockquotes for this purpose; blockquotes are for quoted text.

```markdown
!!! note
    While these twelve stages are presented as a sequence, research data
    management is not a strictly linear process.
```

Available types and their intended use in this guide:

| Type | Use for |
|---|---|
| `note` | General observations, clarifications, contextual information |
| `tip` | Practical recommendations, useful shortcuts, template suggestions |
| `warning` | Risks, common mistakes, things that could go wrong |
| `info` | Background information, definitions, conceptual clarifications |
| `example` | Worked examples, scenarios, discipline-specific illustrations |
| `quote` | Attributed quotations from policies, standards, or publications |
| `danger` | Legal obligations, data protection requirements, serious risks |
| `question` | Prompts for the reader to reflect, self-assessment questions |

**Custom titles.** Always provide a descriptive title rather than relying on the default type label:

```markdown
!!! warning "Do not confuse backup with archiving"
    Active project backups and long-term preservation serve different
    purposes. See the [PRESERVE stage](../stages/preserve.md) for the
    distinction.
```

**Collapsible admonitions.** Use `???` for content that is useful but secondary, so the reader can expand it on demand. Use `???+` if it should be expanded by default:

```markdown
??? example "Budgeting for RDM: a worked example"
    A three-year social sciences project with interview data might
    budget for...
```

### Content tabs

Use content tabs to present parallel alternatives, such as discipline-specific variants, tool comparisons, or format options:

```markdown
=== "Quantitative"

    For structured, numerical data, consider depositing in a
    domain-specific repository such as PANGAEA or ICOS.

=== "Qualitative"

    For interview transcripts and field notes, repositories such as
    the UK Data Service or DANS may be appropriate.
```

Do not overuse tabs. They are best suited for genuinely parallel content where the reader needs one variant, not all of them.

### Grids and cards

Use card grids for landing pages, navigation aids, or visual overviews (e.g. the stage overview page or discipline entry points):

```html
<div class="grid cards" markdown>

- :material-lightbulb-outline: **FRAME**

    Define the problem space and articulate research questions.

    [Read more](stages/frame.md)

- :material-cash: **FUND**

    Align data planning with funder requirements.

    [Read more](stages/fund.md)

</div>
```

Do not use grids for body content. They are a navigation and layout tool, not a substitute for prose.

### Footnotes

Use footnotes for citations, legal references, and detailed attributions that would interrupt the flow of the text:

```markdown
The FAIR principles were first articulated in 2016.[^1]

[^1]: Wilkinson, M. D. et al. (2016). The FAIR Guiding Principles
    for scientific data management and stewardship. *Scientific Data*,
    3, 160018.
```

Do not use footnotes for content that belongs in the body text. If the information is important enough to include, put it in the text or in an admonition.

### Tooltips on links

Add tooltip text to links where a brief explanation helps the reader without requiring a full glossary detour:

```markdown
[CoreTrustSeal](https://www.coretrustseal.org/ "A certification for trustworthy data repositories")
```

### Icons

Zensical supports Material Design icons and FontAwesome. Use icons sparingly, primarily in card grids and navigation elements. Do not scatter icons through body text.

---

## File and section naming

- Use lowercase and hyphens for file names: `data-management-plan.md`, not `DataManagementPlan.md`.
- Stage files use the stage name: `frame.md`, `fund.md`, `plan.md`, etc.
- Discipline files use a short descriptor: `natural-physical-sciences.md`, `humanities.md`.
- The glossary is a single file: `glossary.md`.
- The global abbreviations file is at `includes/abbreviations.md` (a dotfile, hidden from navigation).

---

## Pre-publish checklist

Before any content is published or merged, check that it meets the following:

**Language and style**

- [ ] British English spelling throughout.
- [ ] No em dashes. Sentences restructured where needed.
- [ ] Oxford comma used consistently.
- [ ] No gendered language; inclusive examples across disciplines.
- [ ] Headings in sentence case.
- [ ] Tone is direct, clear, and respectful of the reader's time.

**Inclusivity and accessibility**

- [ ] All abbreviations explained on first use (spelled out, glossary-linked, or both).
- [ ] All tools, platforms, and standards linked to their homepage on first use.
- [ ] Descriptive link text (no 'click here').
- [ ] Alt text provided for all images and diagrams.
- [ ] New abbreviations added to `includes/abbreviations.md`.

**Content**

- [ ] No AI buzzwords or hype language (see the table in the Style Guide).
- [ ] Specific tools named where AI is discussed, not just 'AI'.
- [ ] Guidance is distinguished from legal requirements and funder mandates.
- [ ] Cross-references used instead of duplicating content.
- [ ] Glossary entries created for any new terms introduced.

**Page design**

- [ ] Page meets word-count target for its type: situation 400–650, lifecycle/reference 800–1,500 (excluding collapsible content).
- [ ] Italic pyramid summary present below the H1 title: two to four sentences previewing the page's key points.
- [ ] No paragraph exceeds five sentences.
- [ ] No list exceeds ten items.
- [ ] No heading deeper than H3 in body content.
- [ ] No more than three to four visible admonitions (collapsible sections excluded).
- [ ] All admonitions have descriptive custom titles.
- [ ] No more than three consecutive paragraphs without a visual break (heading, list, admonition).
- [ ] Review date admonition added for pages covering rapidly evolving topics.

**Zensical and Markdown**

- [ ] Internal links point to `.md` files using relative paths.
- [ ] Admonitions used instead of blockquotes for call-outs (with descriptive titles).
- [ ] Content renders correctly in a local Zensical preview before merging.
- [ ] No HTML used where Markdown or a Zensical extension can achieve the same result (exception: grid layouts).
