# Blueprint: Cross-cutting theme on AI in research data management

*Status: Draft blueprint for discussion*
*Date: 27 March 2026*

---

## Purpose of this page in the hub

The base content architecture already identifies **AI governance** as a cross-cutting theme that surfaces across collection (Stage 4), processing (Stage 6), analysis (Stage 7), reuse (Stage 12), and reproducibility. Several lifecycle pages already address AI in context-specific ways:

| Page | What it covers on AI |
|---|---|
| Collect (Stage 4) | Automated transcription, NLP, machine translation; treating outputs as drafts |
| Process (Stage 6) | Whisper and automated transcription; documenting tool versions and parameters |
| Analyse (Stage 7) | AI classification, pattern detection, text analysis; cross-reference to reproducibility |
| Share & Reuse (Stage 12) | AI training pipelines as a reuser category; consent and representation concerns |
| Reproducibility and transparency | Documenting AI tools (8-item checklist); publisher policies; hallucinated citations; DPIA requirements |

The cross-cutting AI page should **not repeat** this material. Instead it should provide the overarching governance framework that connects these scattered references, address questions that do not belong to any single lifecycle stage, and link to CMI's institutional AI policy.

**Proposed file:** `docs/CROSS-ai.md`
**Navigation placement:** Under "Cross-cutting guidance" in the nav, after Reproducibility and transparency

---

## Proposed structure

```
# AI in research: governance, risk, and responsible use

[Italic pyramid summary: 2-4 sentences]

## CMI's AI policy and this guidance
## What counts as AI in a research context
## Data protection and AI services
## AI across the research lifecycle (signposting)
## AI in sensitive and Global South research contexts
## When your data becomes AI training data
## Choosing and evaluating AI tools
## What funders and publishers expect
```

---

## Section-by-section blueprint

### 1. CMI's AI policy and this guidance

**Content:** Link to and briefly summarise CMI's institutional AI policy. Explain how this page relates to it: the AI policy sets institutional rules; this page translates those rules into practical RDM decisions. The page does not replace the policy but operationalises it for the research lifecycle.

**Issues to discuss:**
- Where exactly does CMI's AI policy sit (intranet? public document?), and what is its scope? Does it cover only generative AI, or all ML/automated tools?
- Does the AI policy address research use specifically, or is it primarily an administrative/operational policy? If the latter, this page may need to fill the gap.
- Should this page reproduce key provisions of the AI policy, or only link and paraphrase?

### 2. What counts as AI in a research context

**Content:** A short, pragmatic definition. Not a technical taxonomy, but a scope statement that helps researchers recognise when this guidance applies to their work. Cover the spectrum: generative AI (ChatGPT, Claude, Gemini), transcription tools (Whisper, Otter.ai), translation tools, NLP classifiers, machine learning models, computer vision, and statistical/computational tools that blur the boundary (e.g., automated coding in NVivo).

**Issues to discuss:**
- Where to draw the line? Spell-check is not AI governance. Automated thematic coding might be. The page needs a practical test rather than a philosophical definition.
- Should the page use a table or decision tree to help researchers decide whether a specific tool falls within scope?

### 3. Data protection and AI services

**Content:** The GDPR and data protection implications of feeding research data into AI tools. This is arguably the highest-stakes section. Cover:

- **Consumer vs. enterprise tiers:** Consumer versions of ChatGPT, Gemini, etc. may train on input data; enterprise tiers with contractual protections (DPA, no training on input) are a different proposition. Researchers must know which they are using.
- **DPIA requirement:** The Norwegian Data Protection Authority (Datatilsynet) has confirmed a DPIA is required before deploying generative AI tools that process personal data (NTNU/Copilot sandbox exit report, November 2024). This applies to CMI.
- **Data residency and transfer:** Where does the data go? US-hosted services raise Schrems II questions for personal data. Enterprise agreements with EU data residency may mitigate this.
- **What must not go in:** Personal data, special category data, confidential partner-provided data, unpublished field material. The default should be: if in doubt, do not paste it into a cloud AI tool.
- **CMI's MS365 Copilot position:** If CMI has or is considering M365 Copilot, this is distinct from consumer ChatGPT and has its own DPA. Link to CMI's AI policy for the institutional position.

**Issues to discuss:**
- Does CMI currently have enterprise-tier AI service agreements (e.g., M365 Copilot, Azure OpenAI)? If so, these should be named as the sanctioned route.
- Does CMI have a position on researchers using personal/consumer AI accounts for research tasks? If not, this page should recommend one.
- Should the page include a simple decision flowchart: "Can I use this AI tool with this data?"
- How does Sikt's notification/DPIA process interact with AI tool use? Does each new AI tool require a separate Sikt notification?

### 4. AI across the research lifecycle (signposting)

**Content:** A brief table or annotated list showing where AI governance decisions arise at each lifecycle stage, with links to the relevant sections of existing pages. This is a navigation aid, not new substance. It makes the cross-cutting nature of AI visible without duplicating content.

**Format suggestion:**

| Stage | AI governance question | Link |
|---|---|---|
| Frame | Will AI tools be part of the methodology? Flag in the concept note | Link |
| Fund | Budget for enterprise AI tools and DPIA costs | Link |
| Plan | Document AI tools in the DMP; include in DPIA | Link |
| Collect | Transcription, translation, NLP; document tool use | Link |
| Process | Automated classification, coding; version and parameter logging | Link |
| Analyse | ML models, pattern detection; distinguish AI-generated from human judgement | Link |
| Publish | Publisher disclosure requirements | Link |
| Share & Reuse | AI training on your data; licence and consent implications | Link |

**Issues to discuss:**
- Is this redundant with the existing lifecycle pages, or does it add value as a single overview?
- Should this be a table, or an interactive timeline/diagram?

### 5. AI in sensitive and Global South research contexts

**Content:** This is where the page earns its place in CMI's hub rather than being generic. Cover:

- **Language and accent bias:** Automated transcription tools perform unevenly across languages, dialects, and accents. Whisper's accuracy drops significantly for lower-resource languages and non-standard speech. For CMI's multilingual fieldwork, this is a quality and equity issue, not just a technical limitation.
- **Cultural and contextual bias:** Large language models encode biases from their training data. Outputs about governance, conflict, religion, ethnicity, or gender in Global South contexts may reflect Western or majority-culture assumptions. Researchers must treat AI outputs as drafts requiring contextual judgement.
- **Surveillance and data exposure risks:** In authoritarian or conflict-affected contexts, sending research data (even seemingly non-sensitive metadata) to cloud AI services creates surveillance vectors. Data may be subject to legal demands in the hosting jurisdiction (CLOUD Act, national security laws).
- **Power dynamics in AI adoption:** If Northern research partners use AI tools to process data collected by Southern partners, who controls the analytical layer? This intersects with the hub's existing framing on partnership dynamics and data sovereignty.
- **AI-generated synthetic data:** A potential privacy-preserving technique (generating synthetic datasets that preserve statistical properties without exposing individuals). Promising but not yet mature; requires careful validation. Worth flagging as an emerging area.

**Issues to discuss:**
- How much of this is already covered by the CMI AI policy? If the policy is silent on research-specific Global South concerns, this section fills an important gap.
- Should the page recommend specific tools that have been evaluated for multilingual performance?
- Is there appetite for a "red lines" list: situations where AI tool use should be prohibited or require explicit approval (e.g., processing interview data from conflict zones, analysing data about persecuted minorities)?

### 6. When your data becomes AI training data

**Content:** The reverse perspective: not you using AI, but AI using your data. Cover:

- **Default licence terms and AI scraping:** CC BY and CC0 licences do not explicitly address AI training. Data deposited under these licences may be ingested by training pipelines. This is a live debate with no settled resolution.
- **Participant expectations:** Did your participant information materials cover the possibility that data might be used to train AI models? For most existing CMI datasets, the answer is almost certainly no. This raises questions about the scope of original transparency obligations.
- **Repository terms:** Do Sikt, Zenodo, and other repositories used by CMI have policies on AI training use of deposited data? (Zenodo does not currently restrict it; Sikt's position may differ.)
- **Emerging governance models:** Data trusts, data cooperatives, and AI-specific licence clauses (e.g., "no machine learning" riders) are being developed. None is established practice yet, but CMI researchers should be aware of the landscape.
- **Representational harm:** AI models trained on CMI data about conflict, migration, or governance could generate misleading outputs about the populations described. The CARE Principles are directly relevant here.

**Issues to discuss:**
- Should CMI adopt a default position on AI training use of its deposited data (e.g., recommending specific licence clauses)?
- How should existing datasets be handled? Retrospective restriction may not be possible under current licence terms.
- Is this a question for individual researchers, or does it require an institutional stance?

### 7. Choosing and evaluating AI tools

**Content:** Practical guidance on selecting AI tools for research tasks. Not a product review, but a framework for evaluation:

- **Institutional vs. personal accounts:** Always prefer institutionally procured tools with DPAs over personal consumer accounts.
- **Open-source vs. proprietary:** Open-source tools (Whisper, local LLMs) can be run on CMI or Norwegian infrastructure, avoiding data transfer. Proprietary cloud services are often more capable but raise data protection questions.
- **Evaluation criteria:** Accuracy for your language/domain, data protection terms, model version stability, reproducibility (can you re-run the same analysis?), cost, and institutional approval.
- **Documentation as a minimum standard:** Whatever tool you use, the reproducibility checklist from the Reproducibility and transparency page applies. Link back rather than duplicate.

**Issues to discuss:**
- Should CMI maintain an approved/evaluated tools list? This would require institutional commitment to keep it current.
- Who at CMI is responsible for evaluating and approving AI tools for research use? IT? Research support? Individual PIs?
- Should the page recommend running local models (e.g., via Ollama or similar) for sensitive data, or is this too technically demanding for most researchers?
- What about AI tools used by research assistants, field teams, or Southern partners who may not have access to CMI's institutional infrastructure?

### 8. What funders and publishers expect

**Content:** Brief synthesis of the convergence in funder and publisher policies on AI disclosure. This partially overlaps with the Reproducibility and transparency page (which has the publisher policy table and the documentation checklist). The cross-cutting AI page should:

- Link to the existing table rather than reproduce it
- Add any funder-specific AI policies (RCN, Horizon Europe, Norad) that go beyond publisher disclosure
- Note the direction of travel: requirements are tightening, not loosening

**Issues to discuss:**
- Is there enough new content here to justify a section, or should it simply be a paragraph with a link to the reproducibility page?

---

## Open institutional questions

These are not content questions but governance questions that the page cannot answer alone. They should be raised with CMI leadership, IT, and legal/compliance:

1. **Does CMI's AI policy cover research use specifically, or only administrative/operational use?** If it is silent on research, this page and the AI policy need to be developed in dialogue.

2. **Does CMI have enterprise-tier AI agreements (M365 Copilot, Azure OpenAI, institutional ChatGPT)?** The answer determines what the "safe" option is for researchers.

3. **Who approves AI tool use for research?** Is this the PI's decision, or does it require institutional sign-off (e.g., through Sikt, the data protection officer, or an AI governance committee)?

4. **Should CMI maintain an approved tools list for AI in research?** This is useful but requires maintenance commitment.

5. **What is CMI's position on AI training use of its deposited research data?** This is an emerging question that most institutions have not yet answered.

6. **How should the DPIA process work for AI tools?** One DPIA per project, per tool, or a blanket assessment for institutionally approved tools?

7. **Should AI use in field contexts (by local RAs, translators, transcribers) be governed differently from AI use at CMI in Bergen?** The risk profiles are different.

---

## Relationship to existing pages

The AI cross-cutting page should **link to, not duplicate**, the following existing content:

| Existing page | What it already covers | What the AI page adds |
|---|---|---|
| Reproducibility and transparency | Documentation checklist, publisher policies, hallucinated citations, DPIA warning | Governance framework, institutional policy link, tool evaluation |
| Collect (Stage 4) | AI-assisted transcription, NLP, translation | Sensitivity-aware guidance for Global South fieldwork |
| Process (Stage 6) | Whisper documentation, parameter logging | Nothing new; link only |
| Analyse (Stage 7) | AI for classification, pattern detection | Distinguishing AI-generated from human analytical judgement |
| Share & Reuse (Stage 12) | AI training pipelines as reuser, consent concerns | Licence implications, institutional position, CARE framing |
| GDPR and legal compliance | Data protection framework (stub) | AI-specific GDPR questions (DPIA, DPA, data residency) |

---

## Tone and style notes

Per the style guide:

- British English throughout
- No em dashes (restructure sentences)
- No AI buzzwords ("AI-powered", "leverage AI", "game-changer", "unlock insights"). Name tools and describe what they do.
- Address the reader as "you"
- Pyramid summary (2-4 italic sentences) below the H1
- 800-1,500 words (excluding collapsible content)
- No more than 3-4 visible admonitions (use collapsibles for supplementary material)
- Link to CMI AI policy contextually, not in a "See also" section
- Review date admonition at the bottom (this topic evolves rapidly)

---

## Suggested frontmatter

```yaml
---
icon: lucide/bot
title: "AI in research"
description: "Governance, data protection, and responsible use of AI tools across the research lifecycle at CMI."
tags:
  - AI governance
  - Data protection
  - GDPR
  - Reproducibility
  - Ethics
notes: "Link to CMI AI policy when URL confirmed"
date_updated: 2026-03-27
---
```

---

## Next steps

1. **Discuss this blueprint** with stakeholders (research support, IT, legal/data protection) to resolve the open institutional questions above.
2. **Confirm the scope and URL of CMI's AI policy** so it can be linked.
3. **Decide on the approved tools question** (section 7): is CMI ready to maintain an evaluated list, or should the page provide a framework and leave tool selection to PIs?
4. **Draft the page** once the institutional questions are settled, following the structure above.
5. **Add to navigation** in `zensical.toml` under "Cross-cutting guidance".
6. **Populate the CROSS-ai.md stub** in `docs/` (currently does not exist; the other CROSS-*.md files are placeholder stubs).
