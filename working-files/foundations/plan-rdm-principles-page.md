# Plan: RDM principles page for the CMI RDM Hub

*28 March 2026*

## Purpose

Create a single, authoritative, published page that articulates CMI's principles for research data management. The page should:

1. **Guide practice** — give researchers and support staff a concise reference for data-related decisions.
2. **Be citable in DMPs** — provide a stable URL that can be linked to in Data Management Plans submitted to RCN, Horizon Europe, ERC, Norad, and other funders.
3. **Signal institutional commitment** — demonstrate to funders, partners, and review panels that CMI has a coherent, principled approach to RDM.

---

## What already exists

| Source | Content | Status |
|---|---|---|
| `working-files/principles/core-principles.md` | Eight core principles (concise, well-structured) | Draft, not published |
| `working-files/early-drafts/core-principles-v1.md` | Extended version with checklists | Earlier draft |
| `working-files/principles/data-principles.md` | Four philosophical data principles (political, voice, memory, value) | Draft, not published |
| `working-files/principles/why-rdm-matters.md` | Motivational framing page | Draft, not published |
| `working-files/cmi-context/cmi-policies/open-science.md` | Five open science principles + sharing pathways | Policy draft, not published |
| `docs/foundations-of-data-sharing.md` | Epistemic and historical arguments (FAIR, CARE, Merton, Leonelli) | Published |
| `docs/cmi-institutional-context.md` | Contextual challenges (sensitivity, partnerships, sovereignty) | Published |
| `docs/reproducibility-and-transparency.md` | Reproducibility/transparency as principles | Published |

**Key finding:** The eight core principles in `core-principles.md` are well developed and close to publishable. The four data principles provide useful framing. The five open science principles overlap significantly with the core eight. Consolidation, not new writing, is the main task.

---

## Recommended approach

### Option A: Single principles page (recommended)

Create one page, `docs/rdm-principles.md`, that:

- Opens with a pyramid summary explaining what the page is for (guidance + DMP reference).
- States CMI's eight core principles in the concise style of `core-principles.md`.
- Integrates the four data principles as a short framing section ('How CMI thinks about data') before the eight operational principles.
- References FAIR, CARE, and the 'as open as possible, as closed as necessary' formulation within the relevant principles (as the current `core-principles.md` already does), rather than listing them as separate items.
- Includes a collapsible quick-check section (the six questions from `core-principles.md`).
- Links out to the detailed treatment in `foundations-of-data-sharing.md`, `reproducibility-and-transparency.md`, and `cmi-institutional-context.md` rather than repeating their content.
- Ends with a brief 'Using this page in a DMP' section that explains how to cite or link to it.

**Why this works:**
- A single page with a clear URL is easy to reference in DMPs and funder submissions.
- It avoids duplicating the rich contextual content already published on other pages.
- It keeps the principles concise and actionable, not philosophical.
- It consolidates three overlapping working-files drafts into one published output.

### Option B: Principles page + separate policy statement

An alternative is to create two pages:

1. **Principles page** (`docs/rdm-principles.md`) — the eight core principles, as above.
2. **Open science and data sharing policy** (`docs/open-science-policy.md`) — CMI's institutional positions on open access, repositories, sharing pathways, licensing. This draws primarily from `working-files/cmi-context/cmi-policies/open-science.md`.

**Why this might be useful:**
- The open science policy document is more operational (repository defaults, sharing pathways, licensing) and may be better suited as a separate reference for project managers and administrative staff.
- It keeps the principles page focused on the conceptual framework.
- A DMP could link to both: 'CMI's RDM principles' for the institutional stance, 'CMI's data sharing policy' for the operational detail.

**Trade-off:** Two pages means two things to maintain. The principles page alone covers most of what a DMP needs.

### Option C: Principles embedded in a 'Get started' or overview page

Rather than a standalone page, integrate the principles into the existing `get-started.md` or a new overview page. This avoids adding another navigation item but makes the principles harder to cite directly.

**Not recommended** — the principles need a stable, standalone URL for DMP referencing.

---

## Recommended page structure (Option A)

```
---
icon: lucide/scroll-text
title: "Principles for research data management"
description: "CMI's principles for planning, handling, documenting, securing, and sharing research data — a reference for practice and for Data Management Plans."
tags:
  - Principles
  - Governance
  - FAIR
  - CARE
notes: ""
date_updated: 2026-03-28
---

# Principles for research data management

*[Pyramid summary: 2–4 sentences. These principles guide data decisions at
CMI. They are a practical reference for researchers and can be cited in
DMPs to demonstrate CMI's institutional approach to RDM.]*

## How CMI thinks about data
[Brief framing from the four data principles: political, voice, memory,
value. 2–3 short paragraphs. Link to foundations-of-data-sharing.md and
cmi-institutional-context.md for the fuller argument.]

## Eight principles for research data

### 1. Manage data in ways that support good research
### 2. Apply proportionality
### 3. Protect people, relationships, and context
### 4. Document decisions as you go
### 5. Match access and security to sensitivity
### 6. Treat data management as a shared responsibility
### 7. Be as open as possible, as closed as necessary
### 8. Plan for the full lifecycle

[Each principle: 1–2 paragraphs. Same concise style as core-principles.md.
Principle 7 integrates FAIR, CARE, and the five sharing pathways by
reference.]

??? question "Quick check: applying the principles"
    [The six questions from core-principles.md]

## Referencing these principles in a DMP

[Short section explaining how to cite this page. Example text for DMPs.
Something like:

  'CMI's approach to research data management is guided by eight
  institutional principles covering research quality, proportionality,
  participant protection, documentation, security, shared responsibility,
  responsible openness, and lifecycle planning. These principles are
  aligned with the FAIR and CARE frameworks. For details, see:
  https://trond-k.github.io/cmi-rdm-hub/rdm-principles/']
```

**Estimated word count:** 800–1,200 words (within the lifecycle/reference page target).

---

## Navigation placement

Add to the 'Foundations' section in `zensical.toml`, after the institutional context page:

```toml
{ "Foundations" = [
    { "The elements of research data management" = "elements-of.md" },
    { "CMI's institutional context" = "cmi-institutional-context.md" },
    { "Principles for research data management" = "rdm-principles.md" },
    { "Foundations of data sharing" = "foundations-of-data-sharing.md" },
    { "The research data lifecycle" = "research-data-lifecycle.md" },
]}
```

Alternatively, it could go *first* in the Foundations section, before 'elements-of.md', since principles are the most general entry point. This depends on the intended reading order.

---

## Content sources and consolidation

| Section of new page | Primary source | Notes |
|---|---|---|
| Pyramid summary | New writing | Explain dual purpose (guidance + DMP reference) |
| How CMI thinks about data | `working-files/principles/data-principles.md` | Condense to 2–3 paragraphs; link out for depth |
| Eight principles | `working-files/principles/core-principles.md` | The latest draft is nearly ready; tighten prose, add cross-links |
| Quick check | `working-files/principles/core-principles.md` | Use as-is in a collapsible admonition |
| DMP referencing section | New writing | Example citation text; note the stable URL |

---

## Relationship to other pages

- **`foundations-of-data-sharing.md`** covers the *why* (history, epistemology, FAIR, CARE, Merton, Leonelli). The principles page covers the *what* (CMI's commitments). Link from principles to foundations.
- **`cmi-institutional-context.md`** covers the *where* (CMI's specific challenges). Link from principles to context.
- **`reproducibility-and-transparency.md`** operationalises principles 1 and 4 in detail. Link from the relevant principles.
- **Lifecycle pages** operationalise the principles stage by stage. The principles page provides the frame; lifecycle pages provide the detail.

---

## Additional suggestions

### Suggestion 1: DMP boilerplate snippets

In addition to (or as part of) the principles page, provide 2–3 ready-made text snippets that researchers can paste into DMPs when asked about institutional data management policies. These could be in a collapsible section or a separate companion page. Example:

> *'CMI is committed to research data management practices that are proportionate to the nature and sensitivity of the data, aligned with the FAIR and CARE principles, and planned across the full project lifecycle. CMI's institutional principles and guidance are available at [URL]. Data from this project will be managed in accordance with these principles, with specific measures documented in this plan.'*

### Suggestion 2: Versioning and review date

Since this page may be cited in funded projects lasting 3–5 years, include a version number or date and a review commitment (e.g., 'These principles were adopted [date] and are reviewed annually'). This signals to funders that the document is maintained.

### Suggestion 3: Consider a PDF/printable version

Some DMP tools and funder portals allow attaching documents. A clean PDF version of the principles page (generated from the site or maintained separately) could be useful for offline reference.

---

## Implementation steps

1. Create `docs/rdm-principles.md` using the structure above, drawing primarily from `working-files/principles/core-principles.md` and `working-files/principles/data-principles.md`.
2. Add the page to the nav in `zensical.toml`.
3. Add any new abbreviations to `includes/abbreviations.md`.
4. Review against `STYLE-GUIDE.md` and `REVIEW-CHECKLIST.md`.
5. Preview locally with `uv run zensical serve`.
6. Update cross-links from other pages (especially `foundations-of-data-sharing.md`, `cmi-institutional-context.md`, lifecycle stage pages) to point to the new principles page where relevant.
7. Consider whether the 'why-rdm-matters' content should be merged into a 'Get started' page or kept as a separate working file.
