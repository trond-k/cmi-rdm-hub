# Style Guide — CMI RDM Guide

This style guide governs all content produced for the CMI Research Data Management Hub. It applies to human-written and AI-generated content alike. Every contributor and every prompt used to generate content should reference this document.

---

## Purpose and identity

This guide exists to be **genuinely useful** to researchers, research support staff, and administrators at Chr. Michelsen Institute (CMI) dealing with research data management (RDM). It is not a generic university library leaflet. It is not a compliance checklist dressed up as guidance. It is a serious, focused, inclusive source of information on everything RDM, grounded in practical workflows and real research contexts.

The voice is that of a **senior CMI colleague** who is an expert in open science, GDPR, security, and RDM. They genuinely advocate for data sharing but are honest about the complexities involved, whether legal, ethical, or practical. They take researchers and their dilemmas seriously, know exactly where people run into trouble, and address those points head-on. Not a university library guide; not cheerleading for openness without nuance.

---

## Language and spelling

- **British English throughout.** Use British spelling, grammar, and conventions consistently.
  - *organised*, not *organized*
  - *recognised*, not *recognized*
  - *anonymisation*, not *anonymization*
  - *licence* (noun), *license* (verb)
  - *centre*, not *center*
  - *colour*, not *color*
  - *programme* (but *program* when referring to software)
  - *focussed* or *focused* are both acceptable in British English; pick one and be consistent. This guide uses **focused**.
  - *judgement*, not *judgment*

- **No em dashes.** Do not use em dashes (—) or their spaced variants ( — ). Restructure the sentence instead. Acceptable alternatives:
  - A full stop and a new sentence (preferred when the clause is substantial).
  - A comma, if the grammar allows it.
  - A semi-colon, for closely related independent clauses.
  - Parentheses, for genuinely parenthetical asides.
  - A colon, to introduce an explanation or list.

  **Instead of:**
  > Data management is often facility-driven — not researcher-driven.

  **Write:**
  > Data management is often facility-driven, not researcher-driven.

  **Instead of:**
  > The regulatory framework is not just a compliance requirement but the object of analysis — this creates a distinctive reflexivity about data governance.

  **Write:**
  > The regulatory framework is not just a compliance requirement but the object of analysis. This creates a distinctive reflexivity about data governance.

---

## Tone and register

- **Academic but clear.** The writing should be informed by scholarship and professional practice, but it must never retreat into abstraction or padding. Say what you mean. If a sentence does not add information, remove it.
- **Avoid vague intensifiers.** Words like *robust*, *comprehensive*, *holistic*, and *key* often signal that the writer has not identified what is actually strong, complete, or important. Replace them with the specific quality you mean, or drop them entirely.
- **Direct.** Lead with the point. Do not bury the actionable content behind preamble.
- **Pyramid summary.** Each content page should open with a short italic summary immediately below the H1 title. This summary (two to four sentences) gives the reader the key takeaways up front, so they can decide whether to read on. Write it in the same direct, second-person voice as the rest of the guide. It is not an abstract; it is the top of an inverted pyramid.
- **Serious but not stiff.** This is professional writing, not bureaucratic writing. Contractions (*don't*, *can't*, *it's*) are acceptable where they make the text flow more naturally, but use them sparingly and not in formal definitions.
- **Respectful of the reader's time.** Assume the reader is busy and capable. Do not over-explain obvious things. Do not repeat the same point in different words.
- **Honest about uncertainty.** Where guidance is contested, evolving, or jurisdiction-dependent, say so. Do not paper over complexity with false confidence.
- **Address the reader as 'you'** and 'your project.' Not 'researchers should' or 'one might consider.' The reader is a colleague, not a subject.
- **Acknowledge trade-offs.** Data sharing is the default aspiration, but legal, ethical, and practical constraints are real. Name them honestly rather than glossing over them.
- **Link contextually** where the reader might need it. Do not add 'Related pages' or 'See also' sections at the bottom of pages.

---

## Inclusivity and accessibility

### Explain abbreviations and technical terms

Every abbreviation, acronym, or technical term must be made accessible to a reader encountering it for the first time. The site uses two mechanisms, and **each abbreviation should use only one**:

1. **Tooltip (via `includes/abbreviations.md`).** Abbreviations listed in the global abbreviations file get automatic hover tooltips on every page. For these terms, do **not** also spell them out inline. The tooltip provides the expansion. This is the right mechanism for frequently used, cross-cutting abbreviations (e.g., GDPR, DMP, FAIR, RDM, DPIA, DOI).
2. **Inline expansion.** For abbreviations that appear on only one or two pages, or that are niche or discipline-specific, spell them out on first use with the abbreviation in parentheses: *Systematizing Confidence in Open Research and Evidence (SCORE)*. Do **not** add these to `includes/abbreviations.md`.

In addition, link to the external source on first use: for tools, platforms, standards, organisations, and specifications, link to the official website or homepage, e.g., [Zenodo](https://zenodo.org), [DataCite](https://datacite.org).

**Do not assume the reader knows what things are.** A historian should be able to read the section on genomic data and understand what is at stake, even if the detail is not for them. A bioinformatician should be able to read the section on qualitative data and not feel excluded.

### Inclusive language

- When giving examples, draw from a range of CMI-relevant disciplines, career stages, and project sizes.
- Acknowledge that not all researchers or collaborators work in well-resourced institutional environments.

### Web accessibility

- Use descriptive link text. Write `[see the Zenodo deposit guide](url)`, not `[click here](url)`.
- Provide alt text for all images and diagrams.
- Use heading hierarchy correctly (do not skip levels).
- Ensure sufficient colour contrast in any visual elements.

---

## AI-related language

### Avoid buzzwords and hype

This guide takes AI seriously as a practical tool, not as a revolution. Avoid inflated, vague, or marketing-derived language. The following terms and phrases should be avoided or replaced:

| Avoid | Prefer |
|---|---|
| *AI-powered* | Describe what the tool actually does |
| *leverage AI* | *use* |
| *harness the power of AI* | *use AI tools to...* |
| *game-changer* | Describe the specific benefit |
| *cutting-edge* / *state-of-the-art* | Name the tool or technique |
| *unlock insights* | *identify patterns*, *analyse*, *examine* |
| *intelligent* (as an adjective for a tool) | Describe the function |
| *seamlessly* | Describe the integration concretely |
| *transform your workflow* | Describe what changes and how |
| *the AI* (as a singular noun implying agency) | *the tool*, *the model*, *the service* |
| *democratise AI* | Describe who gains access to what |
| *AI revolution* | Describe the specific change |
| *empower researchers with AI* | Describe what researchers can do |
| *next-generation* | Name the actual version or capability |

---

## Punctuation and typography

- **Oxford comma.** Use the serial comma: *data, code, and documentation*, not *data, code and documentation*.
- **Full stops in abbreviations.** Do not use full stops in abbreviations: *RDM*, not *R.D.M.*; *UK*, not *U.K.*.
- **Quotation marks.** Use single quotation marks for direct quotes and terms used in a special sense: *the concept of 'data' in the humanities*. Use double quotation marks for quotes within quotes.
- **Numbers.** Spell out numbers one to ten; use numerals for 11 and above. Always use numerals for technical measurements, versions, and identifiers.
- **Dates.** Use the format *22 March 2026*, not *March 22, 2026* or *22/03/2026*.
- **Hyphens.** Hyphenate compound modifiers before a noun: *long-term preservation*, *open-access journal*. Do not hyphenate after a noun: *the preservation is long term*.
- **En dashes.** Use en dashes (–) for ranges: *pages 10–15*, *2020–2025*. Do not use em dashes.

---

## Abbreviations and linking conventions

**The global abbreviations file** (`includes/abbreviations.md`) is a machine-readable list of abbreviation expansions that Zensical renders as hover tooltips on every page. Reserve this for frequently used, cross-cutting abbreviations only (appearing on four or more pages). Because tooltips appear on **every** occurrence of the term on every page, adding niche or single-page abbreviations here creates unnecessary visual noise.

**Important:** Do not both spell out an abbreviation inline and define it in `includes/abbreviations.md`. Use one mechanism or the other. See [Explain abbreviations and technical terms](#explain-abbreviations-and-technical-terms) for guidance on which to choose.

For terms without an abbreviation, define them in the text on first use, in one to three sentences or a parenthetical clause. For tools, platforms, and standards, link to the official homepage on first use.
