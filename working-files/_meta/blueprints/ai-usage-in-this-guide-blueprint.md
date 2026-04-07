# Blueprint: AI usage in this guide

*Status: Draft blueprint for discussion*
*Date: 28 March 2026*

---

## Purpose of this page in the hub

This page provides **transparency about how AI tools were used in producing the RDM Hub itself**. It is not about AI in research (that is the separate CROSS-ai page). It is a meta-disclosure: practising what the hub preaches on documentation and transparency.

The hub's Reproducibility and transparency page tells researchers to document their AI use. This page applies that same standard to the guide's own production process. It also models the kind of disclosure statement that CMI researchers could adapt for their own projects.

**Proposed file:** `docs/ai-in-this-guide.md`
**Navigation placement:** Standalone item at the bottom of the nav (outside any section group), or under a new "About this hub" section alongside any future colophon/credits page.

---

## Proposed structure

```
# How AI was used in this guide

[Italic pyramid summary: 2-4 sentences]

## Why we disclose this
## What AI tools were used
## How AI was used
## What AI did not do
## Editorial and quality controls
## Limitations and known risks
## A model you can adapt
```

---

## Section-by-section blueprint

### 1. Why we disclose this

**Content:** The hub advises researchers to document AI tool use transparently. It would be inconsistent not to apply the same standard to the guide itself. This section frames the disclosure as a matter of credibility, not apology. Using AI tools in content production is neither inherently good nor bad; what matters is that the reader knows, so they can assess the content accordingly.

**Key points:**
- This hub recommends AI documentation for research (link to reproducibility page)
- The same principle applies to the guide's own production
- Transparency builds trust; omission undermines it

### 2. What AI tools were used

**Content:** Name the specific tools, model versions (where known), and the period of use. Be concrete, not vague.

**Suggested format:** A short table or list:

| Tool | Provider | Purpose | Period of use |
|---|---|---|---|
| Claude (Opus/Sonnet) | Anthropic | Drafting, structuring, editing content | [dates] |
| [Other tools if applicable] | | | |

**Issues to discuss:**
- Which specific models and versions were used? This should be as precise as the hub's own checklist recommends (tool name, model version, date of use)
- Were any other AI tools involved (e.g., for image generation, diagramming, spell-checking beyond standard tools)?

### 3. How AI was used

**Content:** Describe the roles AI played in the production process. Be specific about the workflow, not just a general statement that "AI assisted." Possible categories:

- **Content drafting:** AI generated initial drafts of pages based on outlines, source material, and style guide instructions
- **Structural design:** AI helped develop the content architecture, navigation structure, and page templates
- **Research synthesis:** AI summarised funder policies, regulatory frameworks, and institutional requirements from source documents
- **Style enforcement:** AI was prompted with the style guide and review checklist to produce content consistent with CMI's editorial standards
- **Editing and revision:** AI was used for copyediting, consistency checking, and rewriting passages

**Issues to discuss:**
- What proportion of content was AI-drafted vs. human-drafted? (A rough indication is more honest than silence)
- Were blueprints and prompts human-authored, with AI executing them? Or did AI also contribute to the strategic framing?
- Was AI used iteratively (human reviews and re-prompts) or in a single pass?

### 4. What AI did not do

**Content:** Equally important: what was not delegated to AI. This section sets boundaries and reassures the reader about editorial control.

Possible items:
- **Policy decisions** were not made by AI. CMI's institutional positions, recommendations, and interpretive judgements reflect human editorial decisions
- **Source verification.** All factual claims, citations, URLs, and regulatory references were verified by a human editor against primary sources
- **Stakeholder input.** Decisions about what to include, what to emphasise, and how to frame sensitive topics (e.g., Global South contexts, data sovereignty) involved human judgement informed by CMI's institutional knowledge
- **Final editorial sign-off.** No page was published without human review

### 5. Editorial and quality controls

**Content:** Describe the quality assurance process that sits between AI output and published content.

- Human review of every page against the style guide and review checklist
- Fact-checking of citations, URLs, and regulatory claims
- Sensitivity review for content touching on ethics, GDPR, and Global South contexts
- Iterative revision cycles (not single-pass AI output)
- [Any peer review or stakeholder feedback processes]

**Issues to discuss:**
- How many review cycles did each page go through?
- Were subject-matter experts consulted on specific pages (e.g., GDPR section reviewed by data protection officer)?

### 6. Limitations and known risks

**Content:** Honest acknowledgement of what can go wrong when AI contributes to content production.

- **Hallucination risk.** AI models can generate plausible but incorrect information. Despite verification efforts, errors may remain. Readers are encouraged to verify critical claims against primary sources.
- **Bias in framing.** AI models reflect patterns in their training data, which may introduce subtle biases in how topics are framed, what is emphasised, and what is omitted.
- **Currency.** AI model knowledge has a training cutoff. Rapidly evolving areas (funder policies, GDPR guidance, tool capabilities) may have changed since the content was produced. The "Last reviewed" dates on each page indicate when content was last checked.
- **Homogeneity of voice.** AI-assisted writing can produce a uniform tone that lacks the texture of multiple human contributors. The style guide mitigates this by enforcing a specific voice, but the risk remains.

### 7. A model you can adapt

**Content:** Short section offering this disclosure as a template that CMI researchers can adapt for their own projects or publications. Link to the reproducibility page's AI documentation checklist. The point is that disclosure does not need to be elaborate; it needs to be honest and specific.

---

## Relationship to existing pages

| Existing page | Relationship |
|---|---|
| Reproducibility and transparency | This page applies the reproducibility page's AI documentation principles to the hub itself. Link to the 8-item checklist. |
| CROSS-ai (planned) | That page covers AI in research governance. This page covers AI in the hub's own production. Distinct but complementary. |

---

## Tone and style notes

Per the style guide:
- British English throughout
- No em dashes
- No AI buzzwords. Do not say the guide was "AI-powered" or that AI "enhanced" it. Say what was done.
- Direct, matter-of-fact tone. Neither defensive nor promotional about AI use.
- Address the reader as "you" where appropriate (especially in section 7)
- 400-650 words (this is a situation/reference page, not a lifecycle page)
- "Last reviewed" admonition at the bottom

---

## Suggested frontmatter

```yaml
---
icon: lucide/message-square-code
title: "AI in this guide"
description: "How AI tools were used in producing this hub, what editorial controls were applied, and what this means for readers."
tags:
  - AI governance
  - Transparency
  - Documentation
notes: "Update with specific model versions and dates once confirmed"
date_updated: 2026-03-28
---
```

---

## Navigation placement options

**Option A:** Add to the bottom of the nav as a standalone item:
```toml
{ "How AI was used in this guide" = "ai-in-this-guide.md" },
```

**Option B:** Create an "About this hub" section:
```toml
{ "About this hub" = [
  { "How AI was used in this guide" = "ai-in-this-guide.md" },
]}
```

Option A is simpler and sufficient for now. Option B makes sense if additional meta-pages are planned (credits, methodology, changelog).

---

## Next steps

1. **Confirm facts.** The author(s) should fill in the specific tools, versions, dates, and workflow details. The page cannot be honest without these specifics.
2. **Decide on navigation placement.**
3. **Draft the page** using the structure above.
4. **Review for consistency** with the reproducibility page's AI documentation advice.
5. **Add to `zensical.toml` nav.**
