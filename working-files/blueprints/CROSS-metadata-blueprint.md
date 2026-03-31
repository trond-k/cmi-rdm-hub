# Blueprint: Cross-cutting guidance on metadata

*Status: Draft blueprint for discussion*
*Date: 31 March 2026*

---

## Purpose of this page in the hub

Metadata is referenced throughout the hub but never consolidated. The lifecycle pages address metadata in context (planning metadata standards in Stage 3, writing codebooks in Stage 6, rich metadata for discoverability in Stage 10, metadata persistence in Stage 11), and the FAIR working file (`working-files/open-science/fair-principles.md`) treats metadata extensively under F2, F3, R1, and R1.2. But no page answers the researcher's basic question: *What is metadata, what kinds do I need, and how do I create it well?*

This blueprint proposes **two pages** rather than one:

1. **CROSS-metadata.md** (new) — practical guidance on creating, managing, and sustaining metadata across the research lifecycle
2. **CROSS-fair.md** (publish the existing working file) — the FAIR principles at CMI, adapted from the mature draft in `working-files/open-science/fair-principles.md`

The two pages are tightly connected: FAIR provides the *why* (especially F2, R1), and the metadata page provides the *how*. Each links to the other. This avoids a single page exceeding 3,000 words and allows researchers to find what they need: those who want the governance framework go to FAIR; those who need practical metadata guidance go to the metadata page.

---

## Relationship between the two pages

| Question | FAIR page answers | Metadata page answers |
|---|---|---|
| Why does metadata matter? | Findability, reusability, persistence principles | (Links to FAIR) |
| What metadata do I need? | Principle-level (F2: "rich metadata") | Concrete: descriptive, structural, administrative, provenance |
| What standards exist? | Mentions DDI, DataCite in passing | Dedicated comparison of standards relevant to CMI |
| How do I write good metadata? | General principle (R1: "richly described") | Step-by-step, with examples and templates |
| What about restricted data? | A2: metadata persists; metadata-only records | How to create a metadata-only deposit |
| What do repositories expect? | Table of principles mapped to repositories | Specific metadata fields per repository |

---

## Page 1: CROSS-metadata.md — Proposed structure

**Proposed file:** `docs/CROSS-metadata.md`
**Navigation placement:** Under "Cross-cutting guidance", after "Build a data inventory"
**Word count target:** 800-1,200 words (excluding collapsible sections)

### Suggested frontmatter

```yaml
---
icon: lucide/tags
title: "Document your data with metadata"
description: "What metadata is, why it matters, and how to create it at every stage of the research lifecycle."
tags:
  - Metadata
  - Documentation
  - FAIR data
  - Data management
notes: ""
date_updated: 2026-03-31
---
```

### Proposed heading structure

```
# Document your data with metadata

[Italic pyramid summary: 2-4 sentences — metadata as the description that
makes data findable, understandable, and reusable; not a bureaucratic
requirement but a practical investment; ties to FAIR and CMI's "metadata
is always open" principle]

## What metadata is (and is not)

## Types of metadata you need
### Descriptive metadata
### Structural metadata
### Administrative metadata
### Provenance metadata

## Metadata across the research lifecycle

## Metadata standards for CMI research

## Creating a metadata record: a practical walkthrough

## When data cannot be shared: metadata-only records

## Common mistakes
```

---

### Section-by-section blueprint

#### 1. What metadata is (and is not)

**Content:** A plain-language definition. Metadata is structured information that describes your data: what it contains, who created it, when and where it was collected, how it is organised, and under what conditions it can be accessed. It is not the data itself, not the analysis, and not the publication. Frame it as "the label on the jar": without it, no one (including your future self) can tell what is inside.

**Approach:** Short. Two paragraphs maximum. Avoid the cliche "data about data" definition; instead, use a concrete CMI example (a survey dataset deposited in a repository without description vs. with full metadata).

#### 2. Types of metadata you need

**Content:** Four categories, each with a brief definition and CMI-relevant examples:

- **Descriptive metadata** — Title, creator, subject keywords, geographic and temporal coverage, abstract/description. This is what makes data findable. Maps to FAIR F2.
- **Structural metadata** — How the dataset is organised: file formats, number of files, variable lists, relationships between files, codebook structure. This is what makes data understandable.
- **Administrative metadata** — Access conditions, licence, embargo dates, funder, grant number, ethics approval reference, data classification tier (per CMI's four-tier scheme). This is what makes data governable.
- **Provenance metadata** — Collection methods, instruments used, processing steps, software versions, quality assurance procedures, who collected the data and under what conditions. This is what makes data trustworthy. Maps to FAIR R1.2.

**Format:** Use a content tab set (`=== "Descriptive"`, `=== "Structural"`, etc.) so the page stays compact while giving each type proper treatment.

**Issues to discuss:**
- Should we include a fifth category for "preservation metadata" (file integrity checksums, format migration history, storage conditions)? This is standard in digital preservation (PREMIS) but may be too technical for most CMI researchers. Could be a collapsible section.

#### 3. Metadata across the research lifecycle

**Content:** A concise signposting table showing where metadata decisions arise at each lifecycle stage, linking to the relevant pages. This mirrors the approach in the AI blueprint (section 4) and reinforces that metadata is not a one-time activity at the end.

| Phase | Stage | Metadata activity | Link |
|---|---|---|---|
| Before | Frame | Identify likely data types and preliminary metadata needs | lifecycle-1-frame.md |
| Before | Plan | Specify metadata standards in the DMP; formalise the data inventory | lifecycle-3-plan.md |
| During | Collect | Record collection context: dates, locations, instruments, languages | lifecycle-4-collect.md |
| During | Process | Create codebooks and data dictionaries; document transformations | lifecycle-6-process.md |
| During | Analyse | Document analytical decisions, software, and parameters | lifecycle-7-analyse.md |
| After | Publish | Complete repository metadata fields; write README; attach codebook | lifecycle-8-publish.md |
| After | Preserve | Ensure metadata survives format migration and platform changes | lifecycle-9-preserve.md |
| After | Discover | Optimise metadata for search: rich descriptions, controlled vocabularies, multilingual terms | lifecycle-10-discover.md |
| After | Access | Document access conditions, request procedures, contact information | lifecycle-11-access.md |

**Approach:** Keep the table brief (one line per stage). The lifecycle pages already contain the detail; this table is a navigation aid.

#### 4. Metadata standards for CMI research

**Content:** A focused comparison of the metadata standards most relevant to CMI's disciplines and repositories. Not an exhaustive catalogue, but enough to help a researcher choose.

| Standard | Domain | Used by | When to use it |
|---|---|---|---|
| Dublin Core | General | Most repositories (baseline) | Default for any deposit; 15 core elements |
| DataCite | General | Zenodo, DataCite-indexed repositories | Required when minting DOIs; extends Dublin Core |
| DDI (Data Documentation Initiative) | Social science surveys | Sikt, CESSDA archives, ICPSR | Quantitative survey data with complex variable structures |
| ISO 19115 | Geospatial | GIS repositories, national mapping agencies | Geospatial datasets with coordinate reference systems |
| QuDEx | Qualitative data | QDR, CESSDA | Qualitative interview and ethnographic data |

**Approach:**
- Lead with the practical question: "Which standard should I use?" Answer: most CMI researchers need Dublin Core (automatic in repositories) plus DDI if depositing survey data.
- Use a collapsible admonition for each standard with more detail for those who want it.
- Note that repositories handle much of this automatically; the researcher's job is to provide complete information, not to write XML.

**Issues to discuss:**
- Should we mention machine-actionable metadata and schema.org? This is increasingly relevant for FAIR compliance (especially I1) but may be too technical. Could be a collapsible "For advanced users" section.
- Should we reference the RDA (Research Data Alliance) metadata standards catalogue?

#### 5. Creating a metadata record: a practical walkthrough

**Content:** Step-by-step guidance for the most common CMI scenario: depositing a dataset in Zenodo (or a similar general repository). Walk through each metadata field, explain what it means, and give examples drawn from CMI research contexts.

Fields to cover:
- Title (descriptive, not cryptic)
- Description/abstract (the "elevator pitch" for the dataset)
- Creator(s) with ORCID
- Keywords (using controlled vocabularies where possible)
- Geographic coverage (ISO 3166 country codes)
- Temporal coverage (date ranges)
- Language(s) of the data
- Related publications (by DOI)
- Licence
- Access conditions
- Funder and grant number

**Approach:**
- Use a "good vs. poor" example format to illustrate each field. Concrete examples from development economics, governance research, or qualitative fieldwork.
- Include a tip admonition on the "metadata is always open" principle: even for restricted datasets, the metadata record should be as complete as possible.

**Issues to discuss:**
- Should we provide a downloadable metadata template (e.g., a structured text file or spreadsheet) that researchers can fill in before going to the repository? This would be a companion to the data inventory template.

#### 6. When data cannot be shared: metadata-only records

**Content:** This is one of CMI's distinctive positions: metadata should be open even when data is not. Explain how to create a metadata-only deposit:

- What it is: a full metadata record in a public repository, with no data files attached, but with a DOI and complete description.
- Why it matters: makes the existence of the data discoverable; enables contact between researchers; prevents duplication of effort; fulfils FAIR F1, F2, F4, A2 even for restricted data.
- How to do it: step-by-step for Zenodo (create an upload, select "restricted" or "closed" access, complete all metadata fields, publish the record without data files).
- What to include in the metadata: everything you would include for an open deposit, plus: a clear statement of why data cannot be shared, the access conditions (if any), who to contact, and when (if ever) access might change.

**Approach:** This section is important for CMI's context (sensitive data from conflict-affected settings, GDPR-restricted personal data, partner-controlled data). Frame it positively: a metadata-only record is not a failure to share; it is responsible transparency.

Link to the FAIR page (A2: metadata persist even when data are no longer available) and to the Access lifecycle page (lifecycle-11-access.md).

#### 7. Common mistakes

**Content:** A short, practical list (6-8 items) of metadata pitfalls CMI researchers should avoid. Framed as actionable corrections, not criticism.

Examples:
- **Vague titles:** "Survey data 2024" tells no one anything. Include the topic, geography, and time period.
- **Missing keywords:** If you skip the keywords field, your dataset will not appear in subject-based searches.
- **No licence specified:** Without a licence, no one can legally reuse your data, even if it is openly accessible.
- **Incomplete creator information:** Include all contributors with their ORCID iDs, not just the PI.
- **Ignoring controlled vocabularies:** Free-text keywords are less effective than standardised terms for cross-dataset discovery.
- **Forgetting the codebook:** A dataset without a codebook or data dictionary is a dataset no one else can use.
- **Assuming the repository handles everything:** Repositories provide the structure, but the quality of metadata depends on what you enter.

**Format:** Use a collapsible admonition (`???+ warning "Common metadata mistakes"`) to keep the main page concise.

---

## Page 2: CROSS-fair.md — Publishing the existing draft

The FAIR principles working file (`working-files/open-science/fair-principles.md`) is comprehensive, well-structured, and closely follows the style guide. Publishing it requires:

### Changes needed

1. **Update frontmatter** to match the published page format:

```yaml
---
icon: lucide/diamond
title: "The FAIR principles at CMI"
description: "A practical guide to making research data Findable, Accessible, Interoperable, and Reusable, grounded in CMI's research context."
tags:
  - FAIR data
  - Open Science
  - Data sharing
  - Metadata
  - Data management
notes: ""
date_updated: 2026-03-31
---
```

2. **Fix internal links** — The working file contains relative links to `../../institutional/...` paths that do not exist in the `docs/` directory. These need to be updated or removed. Options:
    - Replace with links to the published lifecycle and cross-cutting pages that cover the same topics
    - Remove links to unpublished institutional pages and note them for future addition
    - Check which institutional pages (open-science.md, data-security.md, data-classification.md, sharing-and-archiving.md, rdm-and-sharing-policy.md) exist in docs/ or should be created

3. **Add cross-reference to the metadata page** — Insert a link to `CROSS-metadata.md` in the sections on F2 (rich metadata) and R1 (rich description), e.g., "For practical guidance on creating metadata, see [Document your data with metadata](CROSS-metadata.md)."

4. **Move local abbreviation definitions to `includes/abbreviations.md`** — The working file defines abbreviations at the bottom of the file. These should be moved to the global abbreviations file (or confirmed as already present there).

5. **Review the "What CMI provides" references** — Several sections reference CMI's "DMP Generator", "repository defaults", "documentation standards", and "open science guidance". Verify that these either exist as published pages or are rewritten as general guidance.

6. **Add pyramid summary** — The current opening paragraph is close but should be reformatted as the standard italic pyramid summary (2-4 sentences).

### Issues to discuss

- **Broken internal links:** The working file references several `../../institutional/...` pages. Are any of these planned for publication? If not, the FAIR page needs to be self-contained or reference lifecycle pages instead.
- **CARE principles section:** The FAIR page mentions CARE but does not fully operationalise it. Should CARE get its own cross-cutting page, or is the treatment in the FAIR page sufficient?
- **Length:** At approximately 1,800 words (excluding collapsible FAQ sections), the FAIR page exceeds the 1,500-word target for reference pages. The collapsible "Common questions" section helps, but consider whether any sections can be shortened.

---

## Navigation placement

Add both pages to the nav in `zensical.toml` under "Cross-cutting guidance":

```toml
{ "Cross-cutting guidance" = [
    { "Reproducibility and transparency" = "reproducibility-and-transparency.md" },
    { "The FAIR principles at CMI" = "CROSS-fair.md" },
    { "Document your data with metadata" = "CROSS-metadata.md" },
    { "Name files and structure folders" = "file-and-folder-naming.md" },
    { "Build a data inventory" = "data-inventory.md" },
    { "GDPR and legal compliance" = "CROSS-gdpr-and-legal-compliance.md" },
    { "Informed consent and information letters" = "CROSS-ethics.md" },
    { "GDPR concepts for researchers" = "CROSS-legal.md" },
]}
```

**Rationale for placement:** FAIR and metadata sit after Reproducibility (which they complement) and before File naming and Data inventory (which are more operational). FAIR comes first because the metadata page references FAIR principles; a reader encountering them in order gets the framework before the practice.

---

## Cross-references to existing pages

The metadata page should link to (not duplicate) content in:

| Existing page | What it already covers | What the metadata page adds |
|---|---|---|
| lifecycle-3-plan.md | Metadata standards in the DMP; data inventory | When and how to choose a standard |
| lifecycle-6-process.md | Codebooks, data dictionaries | (Links only; no new content) |
| lifecycle-8-publish.md | README files, supplementary materials | Repository-specific metadata walkthrough |
| lifecycle-10-discover.md | Rich metadata, metadata schemas, multilingual metadata | Consolidated comparison of standards; practical examples |
| lifecycle-11-access.md | Metadata persistence for restricted data | How to create a metadata-only deposit |
| data-inventory.md | Structured inventory with per-record metadata | Metadata page focuses on *external* metadata (repository deposits); inventory focuses on *internal* metadata (project management) |
| CROSS-fair.md | FAIR principles (F2, R1, A2) | Practical implementation of those principles |

---

## Abbreviations to add

Confirm the following are in `includes/abbreviations.md` (add any that are missing):

```
*[DDI]: Data Documentation Initiative
*[QuDEx]: Qualitative Data Exchange Format
*[PREMIS]: Preservation Metadata: Implementation Strategies
*[DataCite]: DataCite Metadata Schema
*[CESSDA]: Consortium of European Social Science Data Archives
*[RDA]: Research Data Alliance
*[DOI]: Digital Object Identifier
*[ORCID]: Open Researcher and Contributor ID
*[FAIR]: Findable, Accessible, Interoperable, Reusable
*[DMP]: Data Management Plan
```

---

## Open questions for discussion

1. **One page or two?** This blueprint proposes two (metadata + FAIR). An alternative is a single combined page, but at 2,500+ words it would be long. A third option is three pages: FAIR, metadata basics, and metadata standards. Two pages seems the right balance. What do you think?

2. **Metadata template:** Should the metadata page include a downloadable template (spreadsheet or structured text file) that researchers fill in before depositing? This would complement the data inventory template.

3. **Repository-specific guidance:** How deep should the metadata page go on repository-specific fields? A general walkthrough (as proposed) or separate tabs for Zenodo, Sikt, QDR, and openICPSR?

4. **FAIR page internal links:** The working file references several unpublished institutional pages. Should we publish those pages first, rewrite the links, or simply remove them?

5. **CARE as a separate page:** The FAIR page references CARE but does not operationalise it fully. Is a dedicated CARE cross-cutting page needed, or is the current treatment sufficient?

6. **Preservation metadata:** Should the metadata page cover PREMIS and digital preservation metadata, or leave that to the Preserve lifecycle page (lifecycle-9-preserve.md)?

---

## Next steps

1. **Discuss this blueprint** to confirm the two-page approach and resolve open questions.
2. **Audit internal links** in the FAIR working file to determine which can be redirected to published pages.
3. **Draft CROSS-metadata.md** following the structure above.
4. **Adapt and publish CROSS-fair.md** from the working file, with updated links and frontmatter.
5. **Update `zensical.toml`** navigation to include both pages.
6. **Update `includes/abbreviations.md`** with any missing terms.
7. **Preview locally** with `uv run zensical serve` before committing.
