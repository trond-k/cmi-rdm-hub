# Perspectives Style Supplement

This supplement governs **Perspectives pieces**: short, opinionated commentaries on recent publications, policy developments, or events relevant to research practice at CMI. It builds on the main [Style Guide](STYLE-GUIDE.md). Everything in the style guide applies unless explicitly overridden below.

---

## What a Perspectives piece is

A Perspectives piece interprets an external development and connects it to the reader's work. It is not a guidance page, not a how-to, and not a reference. It is closer to a blog post or a short commentary in a professional journal: timely, focused, and willing to take a position.

Every Perspectives piece is **time-anchored**: it responds to a specific publication, dataset release, policy decision, or event, and names a date.

### When to write one

Write a Perspectives piece when:

- A significant study, framework, or policy is published with direct implications for CMI research practice.
- The hub's existing guidance pages do not cover the 'so what' of the development.
- The piece can connect meaningfully back to at least two or three existing hub pages.

### Examples

- [Half of findings do not replicate](docs/CROSS-replication-evidence.md) (April 2026 SCORE findings)
- [Trustworthiness is earned, not claimed](docs/CROSS-trustworthiness-framework.md) (February 2026 Nosek framework)

---

## What carries over from the main style guide

All of the following apply without modification:

- British English spelling and conventions
- No em dashes
- Oxford comma
- No full stops in abbreviations
- Footnotes for citations and legal references
- Admonitions with descriptive custom titles
- Internal links to `.md` files using relative paths
- YAML frontmatter (icon, title, description, tags, notes, date_updated)
- AI-related language rules (no buzzwords)
- Inclusivity and accessibility standards

---

## Language and voice

### No empty praise words

Do not use adjectives that flatter the source rather than inform the reader. Words like *prominent*, *leading*, *renowned*, *distinguished*, *world-class*, and *eminent* add nothing. The reader does not need to be told that the researchers are important; the work speaks for itself. Name the authors, name the institution, and move on.

| Avoid | Write instead |
|-------|---------------|
| *six prominent researchers* | *six researchers from the Center for Open Science and the National Academies* |
| *a leading expert in open science* | *Brian Nosek, who directs the Center for Open Science* |
| *a groundbreaking study* | *a study of ~3,900 papers across 11 disciplines* |

This extends to headings and framing. Do not write headings that tell the reader why something matters ('Why this matters', 'Why a Norwegian commentary matters'). Present the content; the reader is knowledgeable enough to judge its significance. A heading like 'The Norwegian response' is enough.

### Straight, flat register

The voice is direct and flat. No hype, no cheerleading, no selling. State what happened, state what it means, link to the relevant hub page. If a finding is significant, make that clear through the evidence, not through adjectives.

---

## What is different

| Aspect | Standard guidance pages | Perspectives pieces |
|--------|------------------------|---------------------|
| **Title** | Descriptive, functional | Editorial, opinion-forward: a claim, provocation, or framing that gives the reader a reason to care |
| **Pyramid summary** | 2–4 sentences, factual | 3–5 sentences, more narrative; may set the scene before stating the takeaway |
| **Word count** | 400–1,500 depending on type | 500–800 words (excluding frontmatter and footnotes) |
| **Structure** | Flexible by page type | Canonical (see template below) |
| **Voice** | Senior colleague giving guidance | Senior colleague **commenting on the news**: more interpretive, may take a position, more essayistic |
| **Contractions** | Sparingly | More freely, where they make the text flow naturally |
| **Headings** | Up to H3 | Prefer H2 only; use H3 only if a section genuinely needs subdivision |
| **Paragraph limit** | Max 5 sentences | Max 4 sentences |
| **Content tabs / collapsibles** | Used where appropriate | Avoid; keep the reading experience linear |
| **Published date** | Not shown | Shown below the H1 title (see template) |
| **Companion linking** | 'See also' sections discouraged | Encouraged: a tip admonition linking to related Perspectives pieces or key hub pages |
| **Shelf life** | Evergreen, reviewed periodically | Time-sensitive; no 'Last reviewed' admonition; review within 6 months of publication |

---

## Structure template

```markdown
# [Editorial title]

*Published [day month year]*

*[Narrative pyramid summary. What happened, why it matters, and what the
reader should take away. 3–5 sentences.]*

## What [source/study/framework] found

[Report the facts. What was published, by whom, when, and what are the key
findings or proposals. Keep this concise; the reader wants context, not a
literature review.]

## What this means for your project

[Connect the findings to the reader's research practice at CMI. Link to
specific hub pages. This is where the piece earns its place on the hub.]

## What you can do now

[Bulleted, actionable. 3–6 items. Each links to a relevant hub page where
the reader can follow through.]

!!! tip "Companion reading"
    [Link to related Perspectives pieces or key hub pages.]

[^1]: [Full citation in consistent format]

```

### Notes on the template

- The **'What [source] found'** heading should name the source concretely (e.g. 'What the SCORE programme found', 'What the framework proposes').
- A **'Why this matters'** section is optional. At 500–800 words, most pieces will fold broader context into the pyramid summary or the 'What this means' section.
- The **'What you can do now'** section is the bridge back to the hub. Every item should link to a lifecycle or cross-cutting guidance page.

---

## Titles

Titles should be editorial, not descriptive. They make a claim, frame an argument, or give the reader a reason to care. They do not summarise the source; they interpret it.

**Good titles:**

- *Trustworthiness is something you earn, not claim*
- *What the largest replication study means for your research*
- *Half of published findings do not replicate. Now what?*

**Avoid:**

- *Summary of the 2026 SCORE replication study* (too neutral, too descriptive)
- *New framework for assessing research trustworthiness* (reads like a press release)

---

## Published date and review cadence

Every Perspectives piece includes a **published date** as the first line after the H1 title, formatted as italic text:

```markdown
*Published 3 April 2026*
```

This date is permanent and records when the piece was first published. Perspectives pieces do not use a 'Last reviewed' admonition; the published date is sufficient.

**Review cadence:** Perspectives pieces should be reviewed within 6 months of publication. If the underlying research is superseded, corrected, or significantly recontextualised, update the piece or retire it with a note pointing to the newer content.

---

## File naming and navigation

- **File prefix:** `CROSS-` (consistent with cross-cutting guidance pages).
- **Navigation:** Perspectives pieces appear in a dedicated **Perspectives** section in `zensical.toml`, separate from the Foundations and Cross-cutting guidance sections.
