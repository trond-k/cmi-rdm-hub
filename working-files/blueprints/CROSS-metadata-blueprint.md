# Blueprint: Cross-cutting guidance on metadata, FAIR, CARE, and repository-specific pages

*Status: Draft blueprint for discussion*
*Date: 1 April 2026*

---

## Purpose of these pages in the hub

Metadata is referenced throughout the hub but never consolidated. The lifecycle pages address metadata in context (planning metadata standards in Stage 3, writing codebooks in Stage 6, rich metadata for discoverability in Stage 10, metadata persistence in Stage 11), and the FAIR working file (`working-files/open-science/fair-principles.md`) treats metadata extensively under F2, F3, R1, and R1.2. But no page answers the researcher's basic question: *What is metadata, what kinds do I need, and how do I create it well?*

This blueprint proposes **five or more pages**:

1. **CROSS-metadata.md** (new) — practical guidance on creating, managing, and sustaining metadata across the research lifecycle
2. **CROSS-fair.md** (publish the existing working file) — the FAIR principles at CMI, refocused on how archives and repositories implement FAIR; links to unpublished institutional pages removed
3. **CROSS-care.md** (new) — dedicated page for the CARE principles (Collective benefit, Authority to control, Responsibility, Ethics), operationalised for CMI's research context
4. **Repository-specific pages** (new, one per repository) — practical guidance for depositing data in each CMI-recommended repository, with repository-specific metadata fields, access options, and workflows:
    - **CROSS-repo-zenodo.md** — Zenodo
    - **CROSS-repo-sikt.md** — Sikt (Norwegian Agency for Shared Services in Education and Research)
    - **CROSS-repo-qdr.md** — QDR (Qualitative Data Repository)
    - **CROSS-repo-openicpsr.md** — openICPSR
    - **CROSS-repo-osf.md** — OSF (Open Science Framework)

The pages are connected: FAIR provides the *why* (especially F2, R1) with a focus on what repositories provide; the metadata page provides the *how*; CARE addresses the *who benefits and who decides*; and the repository pages give concrete, platform-specific guidance. This avoids bloated pages and allows researchers to find exactly what they need.

---

## Relationship between the pages

| Question | FAIR page answers | Metadata page answers | CARE page answers | Repository pages answer |
|---|---|---|---|---|
| Why does metadata matter? | Findability, reusability, persistence principles | (Links to FAIR) | Community benefit from well-described data | (Links to FAIR/metadata) |
| What metadata do I need? | Principle-level (F2: "rich metadata") | Concrete: descriptive, structural, administrative, provenance | Metadata that respects community authority | Specific fields per repository |
| What standards exist? | Mentions DDI, DataCite in passing | Dedicated comparison of standards relevant to CMI | Community-defined standards | Repository-native standards |
| How do archives implement FAIR? | How each principle is supported by repositories | (Links to FAIR) | CARE-informed access decisions | Step-by-step deposit workflows |
| What about restricted data? | A2: metadata persists; metadata-only records | How to create a metadata-only deposit | Who decides access? | Repository-specific access controls |
| Who benefits from data sharing? | (Mentions briefly) | (Links to CARE) | Full treatment: community rights, reciprocity | Repository features for controlled access |

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

## Page 2: CROSS-fair.md — Publishing the existing draft, refocused on repository implementation

The FAIR principles working file (`working-files/open-science/fair-principles.md`) is comprehensive and well-structured. Publishing it requires significant editorial changes: refocusing on how archives and repositories implement FAIR, removing broken links to unpublished institutional pages, and extracting CARE content into its own page.

### Editorial direction: focus on repositories

The published FAIR page should emphasise **how archives and repositories provide FAIR compliance**. For each principle, the page should explain what the repository does automatically and what the researcher must do. This shifts the framing from abstract principles to practical infrastructure. The "What CMI provides" column in the summary table becomes "What repositories provide", grounded in the five CMI-recommended repositories (Zenodo, Sikt, QDR, openICPSR, OSF). Detailed repository-specific guidance belongs on the individual repository pages (see Page 4 onwards), not here.

### Changes needed

1. **Update frontmatter** to match the published page format:

```yaml
---
icon: lucide/diamond
title: "The FAIR principles at CMI"
description: "A practical guide to making research data Findable, Accessible, Interoperable, and Reusable, with a focus on how archives and repositories support each principle."
tags:
  - FAIR data
  - Open Science
  - Data sharing
  - Metadata
  - Data management
  - Repositories
notes: ""
date_updated: 2026-04-01
---
```

2. **Remove all links to unpublished institutional pages.** The working file contains links to paths that do not exist in `docs/`:
    - `../../institutional/policies/rdm-and-sharing-policy.md` — referenced in the CARE admonition, F2, common questions. **Remove these links.** Where the linked content is essential, rewrite the sentence to be self-contained (e.g., "CMI's RDM and Sharing Policy commits to FAIR as an institutional principle" needs no link).
    - `../../institutional/open-science.md` — referenced in F1 ("repository defaults"), F4, A1.2 ("five sharing pathways"), A2, R1.1 ("licensing"). **Remove these links.** Replace with references to the repository-specific pages where appropriate (e.g., "See the repository-specific guidance pages for details on each platform's access and licensing options").
    - `../../institutional/data-security.md` — referenced in "Further reading". **Remove.**
    - `../../institutional/data-classification.md` — referenced in "Further reading". **Remove.**
    - `../../institutional/sharing-and-archiving.md` — referenced in "Further reading". **Remove.**
    - `open-science.md` — referenced in the CARE admonition. **Remove** (this page does not exist in `docs/` either).
    - **Replace the "Further reading" section** with links to published pages: the metadata page, the CARE page, and the repository-specific pages.

3. **Refocus each principle section on repository implementation.** For each FAIR principle:
    - Lead with what the principle means.
    - Explain how CMI-recommended repositories implement it (e.g., F1: "Zenodo, Sikt, QDR, openICPSR, and OSF all assign DOIs automatically on deposit").
    - State what the researcher must do beyond what the repository provides.
    - Link to the relevant repository page(s) for platform-specific detail.

4. **Extract CARE content.** The CARE admonition and the "What about the CARE principles?" FAQ answer should be replaced with a brief cross-reference: "For guidance on the CARE principles (Collective benefit, Authority to control, Responsibility, Ethics), see [The CARE principles at CMI](CROSS-care.md)." Keep CARE to a single sentence or short paragraph on the FAIR page.

5. **Add cross-reference to the metadata page** — Insert a link to `CROSS-metadata.md` in the sections on F2 (rich metadata) and R1 (rich description).

6. **Move local abbreviation definitions to `includes/abbreviations.md`** — The working file defines abbreviations at the bottom of the file. These should be moved to the global abbreviations file (or confirmed as already present there).

7. **Review the "What CMI provides" references** — Rewrite references to "DMP Generator", "repository defaults", "documentation standards", and "open science guidance" as general guidance or link to published pages.

8. **Add pyramid summary** — Reformat the opening paragraph as the standard italic pyramid summary (2-4 sentences).

### Summary table revision

The existing summary table maps principles to "What CMI provides" and "What researchers should do." Revise this to three columns:

| Principle | What repositories provide | What you need to do |
|---|---|---|

This reinforces the page's focus on repository implementation and gives researchers a practical checklist.

---

## Page 3: CROSS-care.md — The CARE principles at CMI

**Proposed file:** `docs/CROSS-care.md`
**Navigation placement:** Under "Cross-cutting guidance", after FAIR
**Word count target:** 800-1,200 words

### Rationale for a separate page

The FAIR page currently mentions CARE in an admonition and a FAQ answer, but does not operationalise it. CARE deserves dedicated treatment because:

- CMI works extensively with Global South partners, Indigenous communities, and marginalised populations.
- CARE principles shape *who benefits* from data sharing and *who controls* access decisions, which are distinct from the technical FAIR questions of *how* data is managed.
- Funders (including the RCN and Horizon Europe) increasingly expect researchers to address both FAIR and CARE.
- Combining CARE with FAIR on a single page would make that page too long and blur the distinction between technical data management and ethical data governance.

### Suggested frontmatter

```yaml
---
icon: lucide/heart-handshake
title: "The CARE principles for research data"
description: "Guidance on applying the CARE principles — Collective benefit, Authority to control, Responsibility, and Ethics — to research data management at CMI."
tags:
  - CARE principles
  - Indigenous data
  - Data governance
  - Ethics
  - Global South
  - Data sovereignty
notes: ""
date_updated: 2026-04-01
---
```

### Proposed heading structure

```
# The CARE principles for research data

[Italic pyramid summary: 2-4 sentences — CARE as a complement to FAIR;
addresses who benefits and who decides; essential for CMI's partnerships
with Global South communities and research on marginalised populations]

## What the CARE principles are

## Collective benefit
### Data ecosystems should benefit Indigenous and local communities
### How this applies at CMI

## Authority to control
### Communities have the right to govern data about them
### How this applies at CMI

## Responsibility
### Those working with data have a responsibility to support community rights
### How this applies at CMI

## Ethics
### Data practices should align with community values and minimise harm
### How this applies at CMI

## CARE and FAIR together

## Practical steps for CMI researchers

## Further reading
```

### Section-by-section blueprint

#### 1. What the CARE principles are

**Content:** Plain-language introduction to the CARE principles (Research Data Alliance, 2019). CARE stands for Collective benefit, Authority to control, Responsibility, and Ethics. While FAIR addresses how data should be technically managed, CARE addresses the rights and interests of the people and communities the data describes or affects. Frame as complementary to FAIR, not competing.

#### 2. Each CARE principle (four sections)

**Content for each principle:**
- Definition and scope (drawing on the RDA CARE Principles)
- What it means in CMI's research context, with concrete examples from development economics, governance research, and qualitative fieldwork in the Global South
- Practical implications for data management decisions: who is consulted during project design, who controls access, who benefits from reuse, how community norms shape licensing and sharing

**Key examples to include:**
- **Collective benefit:** Data collected in partnership with a local institution should be available to that institution on equal terms, not only accessible through a European repository.
- **Authority to control:** A community that participated in a study about land rights should have a say in whether the data is shared openly, restricted, or embargoed.
- **Responsibility:** Researchers collecting data in conflict-affected settings have a responsibility to ensure that data cannot be used to identify or harm participants, even indirectly.
- **Ethics:** Depositing interview data from a marginalised community in an open repository without consent, even if anonymised, may violate community expectations about knowledge sharing.

#### 3. CARE and FAIR together

**Content:** How CARE-informed decisions interact with FAIR implementation. For example:
- FAIR says metadata should be rich (F2); CARE may require that certain descriptive metadata is withheld to protect community identity.
- FAIR says data should be accessible (A1); CARE may require that access is mediated through community representatives.
- FAIR says data should be reusable (R1); CARE may require that reuse conditions include benefit-sharing agreements.
- Show how repositories support CARE-informed access: QDR's mediated access, data use agreements in Zenodo and openICPSR.

#### 4. Practical steps for CMI researchers

**Content:** A concise checklist (6-8 items) for researchers to apply CARE in their projects:
- Discuss data governance with partners and communities during project design
- Include community representatives in decisions about data sharing and access
- Document community consent and governance arrangements in the DMP
- Choose repositories and access levels that respect community authority
- Include benefit-sharing provisions in data use agreements
- Ensure metadata does not expose community identity where this could cause harm
- Review data sharing decisions with partners before deposit
- Revisit governance arrangements if research context changes

#### 5. Further reading

Links to the RDA CARE Principles, the FAIR page, relevant lifecycle pages, and external resources (e.g., GIDA, Local Contexts, Traditional Knowledge Labels).

---

## Page 4 onwards: Repository-specific pages — One page per repository

Each CMI-recommended repository gets its own page with practical, platform-specific guidance. These pages answer the question: *I need to deposit data in [repository]. What do I need to know?*

### General structure for all repository pages

Each repository page follows the same structure for consistency:

```
# Depositing data in [Repository name]

[Italic pyramid summary: 2-4 sentences — what the repository is,
who it serves, and when CMI researchers should use it]

## When to use [Repository]

## What [Repository] provides for FAIR compliance

## Metadata fields and requirements

## Access options and restrictions

## Step-by-step deposit workflow

## Tips and common issues

## Further reading
```

### Section-by-section blueprint (applies to all repository pages)

#### 1. When to use this repository

**Content:** Clear guidance on when this repository is the right choice for CMI researchers. What types of data, disciplines, and access requirements make it appropriate. When to choose a different repository instead.

#### 2. What this repository provides for FAIR compliance

**Content:** Map the repository's features to FAIR principles. What does the repository handle automatically (DOI assignment, metadata indexing, protocol compliance) and what does the researcher need to provide? This reinforces the FAIR page's focus on repository implementation.

#### 3. Metadata fields and requirements

**Content:** The specific metadata fields the repository requires or supports, with guidance on how to fill them in well. Distinguish between required fields and optional-but-recommended fields. Include CMI-relevant examples for each field.

#### 4. Access options and restrictions

**Content:** The access levels the repository supports (open, embargoed, restricted, closed/metadata-only). How to set up mediated access, data use agreements, or embargo periods. How this relates to CARE principles where relevant.

#### 5. Step-by-step deposit workflow

**Content:** A practical walkthrough of the deposit process, from account creation to publication. Screenshots or detailed descriptions of each step. Note any CMI-specific considerations (institutional affiliation, funder acknowledgement, linking to CMI's community/collection if applicable).

#### 6. Tips and common issues

**Content:** Practical advice based on common mistakes or questions. File size limits, format restrictions, versioning, DOI reservation, linking to publications, etc.

---

### Page 4a: CROSS-repo-zenodo.md — Zenodo

**Proposed file:** `docs/CROSS-repo-zenodo.md`
**Word count target:** 800-1,200 words

```yaml
---
icon: lucide/archive
title: "Depositing data in Zenodo"
description: "Practical guidance for CMI researchers depositing data in Zenodo, including metadata fields, access options, and a step-by-step deposit workflow."
tags:
  - Zenodo
  - Data deposit
  - Repository
  - FAIR data
  - DOI
notes: ""
date_updated: 2026-04-01
---
```

**Key content specific to Zenodo:**
- General-purpose repository hosted by CERN; suitable for any data type and discipline
- When to use: default choice for CMI researchers when no discipline-specific repository is more appropriate; good for supplementary materials, mixed-method datasets, code, and replication packages
- DOI assignment is automatic; supports DOI reservation before publication
- Metadata schema based on DataCite; supports communities and collections
- Access options: open, embargoed, restricted (request-based), closed
- Supports versioning (new DOI per version, concept DOI for all versions)
- Integration with GitHub for code archiving
- File size limit: 50 GB per record (can be increased on request)
- Zenodo Communities: CMI could set up a community page to group all CMI deposits
- Licence selection: supports CC0, CC BY, and custom licences
- Linking to publications, funders (OpenAIRE integration), and grants

---

### Page 4b: CROSS-repo-sikt.md — Sikt

**Proposed file:** `docs/CROSS-repo-sikt.md`
**Word count target:** 800-1,200 words

```yaml
---
icon: lucide/archive
title: "Depositing data in Sikt"
description: "Practical guidance for CMI researchers depositing data in Sikt's research data archive, with a focus on survey data and mediated access."
tags:
  - Sikt
  - Data deposit
  - Repository
  - FAIR data
  - Survey data
  - Norway
notes: ""
date_updated: 2026-04-01
---
```

**Key content specific to Sikt:**
- Norwegian national archive for research data; strong support for social science survey data
- When to use: quantitative survey data, especially when Norwegian funder requirements apply (RCN); preferred for data requiring mediated access with institutional oversight
- Supports DDI metadata standard natively; DDI codebook import
- Mediated access: applicants must apply and be approved; Sikt manages the process
- Norwegian-language interface (with English option); may require liaison with Sikt staff
- Long-term preservation commitment; part of CESSDA network
- Integration with NSD (now Sikt) data collection and archiving workflows
- Specific metadata fields: study description, universe, sampling, data collection methods, weighting, response rates
- Access categories: open, restricted (with application), by special permission only
- CMI's relationship with Sikt: institutional account, contact procedures

---

### Page 4c: CROSS-repo-qdr.md — QDR (Qualitative Data Repository)

**Proposed file:** `docs/CROSS-repo-qdr.md`
**Word count target:** 800-1,200 words

```yaml
---
icon: lucide/archive
title: "Depositing data in QDR"
description: "Practical guidance for CMI researchers depositing qualitative data in the Qualitative Data Repository, including mediated access and disclosure risk evaluation."
tags:
  - QDR
  - Qualitative data
  - Data deposit
  - Repository
  - FAIR data
  - Mediated access
notes: ""
date_updated: 2026-04-01
---
```

**Key content specific to QDR:**
- Specialist repository for qualitative and multi-method data; based at Syracuse University
- When to use: interview transcripts, ethnographic field notes, focus group data, case study materials, and other qualitative data; strongest option for sensitive qualitative data requiring expert curation
- Expert-curated mediated access: QDR staff evaluate disclosure risk and advise on what can be shared and how
- Per-deposit fees apply (note current fee structure or link to QDR's pricing page)
- Annotation for Transparent Inquiry (ATI): linking qualitative data to specific claims in publications
- Data use agreements: QDR can enforce custom access conditions
- Metadata fields: study description, data type, geographic scope, temporal coverage, access conditions, related publications
- Supports both full data deposit and metadata-only records
- Particularly valuable for CARE-sensitive data: mediated access allows community or partner input on access decisions

---

### Page 4d: CROSS-repo-openicpsr.md — openICPSR

**Proposed file:** `docs/CROSS-repo-openicpsr.md`
**Word count target:** 800-1,200 words

```yaml
---
icon: lucide/archive
title: "Depositing data in openICPSR"
description: "Practical guidance for CMI researchers depositing data in openICPSR, with a focus on quantitative social science data and replication packages."
tags:
  - openICPSR
  - ICPSR
  - Data deposit
  - Repository
  - FAIR data
  - Replication
notes: ""
date_updated: 2026-04-01
---
```

**Key content specific to openICPSR:**
- Self-service deposit platform for ICPSR; focused on quantitative social science data
- When to use: quantitative social science data, especially replication packages for journal publications; required or recommended by many economics and political science journals (AEA, APSR, etc.)
- No deposit fees for basic deposits
- Supports restricted access with data use agreements
- Metadata fields: study-level metadata, variable-level metadata, geographic and temporal coverage
- Integration with journal submission workflows (AEA Data Editor, etc.)
- DOI assignment; DataCite metadata
- Curation: openICPSR provides light-touch curation; full ICPSR curation available for higher tiers
- File format recommendations: prefers open formats (CSV, Stata .dta with documentation)
- Versioning support

---

### Page 4e: CROSS-repo-osf.md — OSF (Open Science Framework)

**Proposed file:** `docs/CROSS-repo-osf.md`
**Word count target:** 800-1,200 words

```yaml
---
icon: lucide/archive
title: "Depositing data in OSF"
description: "Practical guidance for CMI researchers using OSF for data sharing, preregistration, and project management."
tags:
  - OSF
  - Open Science Framework
  - Data deposit
  - Repository
  - FAIR data
  - Preregistration
notes: ""
date_updated: 2026-04-01
---
```

**Key content specific to OSF:**
- Multifunctional platform: project management, preregistration, data sharing, and archiving; run by the Center for Open Science
- When to use: preregistration of studies, project-level file management and collaboration, supplementary materials; also suitable as a general-purpose data repository when Zenodo is not preferred
- Assigns DOIs or ARK identifiers (DOI available for public registrations and files)
- Supports add-on integrations (Dropbox, Google Drive, GitHub, etc.)
- Access options: public or private (project-level or component-level); no built-in mediated access workflow (unlike QDR or Sikt)
- Metadata is lighter than discipline-specific repositories; researchers must provide rich documentation via README and supplementary files
- Preregistration: OSF is the standard platform for preregistering study designs; relevant for CMI researchers doing experimental or quasi-experimental work
- File storage: 5 GB per file (private), 50 GB per project (public); larger files via add-ons
- Licensing: supports standard licences (CC0, CC BY, etc.)
- Note: OSF is a good complement to a discipline-specific repository, not always a replacement; for archival purposes, a dedicated archive (Zenodo, Sikt, QDR) may be more appropriate

---

## Navigation placement

Add all pages to the nav in `zensical.toml` under "Cross-cutting guidance":

```toml
{ "Cross-cutting guidance" = [
    { "Reproducibility and transparency" = "reproducibility-and-transparency.md" },
    { "The FAIR principles at CMI" = "CROSS-fair.md" },
    { "The CARE principles for research data" = "CROSS-care.md" },
    { "Document your data with metadata" = "CROSS-metadata.md" },
    { "Depositing data in Zenodo" = "CROSS-repo-zenodo.md" },
    { "Depositing data in Sikt" = "CROSS-repo-sikt.md" },
    { "Depositing data in QDR" = "CROSS-repo-qdr.md" },
    { "Depositing data in openICPSR" = "CROSS-repo-openicpsr.md" },
    { "Depositing data in OSF" = "CROSS-repo-osf.md" },
    { "Name files and structure folders" = "file-and-folder-naming.md" },
    { "Build a data inventory" = "data-inventory.md" },
    { "GDPR and legal compliance" = "CROSS-gdpr-and-legal-compliance.md" },
    { "Informed consent and information letters" = "CROSS-ethics.md" },
    { "GDPR concepts for researchers" = "CROSS-legal.md" },
]}
```

**Rationale for placement:** FAIR and CARE sit after Reproducibility (which they complement). CARE follows FAIR because it builds on the access and governance decisions FAIR raises. The metadata page follows because it provides the practical *how* for the principles. Repository pages come next as the most concrete, platform-specific guidance. The remaining operational pages (file naming, inventory, GDPR, ethics, legal) follow after.

---

## Cross-references to existing pages

The new pages should link to (not duplicate) content in:

| Existing page | What it already covers | What the new pages add |
|---|---|---|
| lifecycle-3-plan.md | Metadata standards in the DMP; data inventory | Metadata page: when and how to choose a standard |
| lifecycle-6-process.md | Codebooks, data dictionaries | (Links only; no new content) |
| lifecycle-8-publish.md | README files, supplementary materials | Repository pages: platform-specific deposit walkthroughs |
| lifecycle-10-discover.md | Rich metadata, metadata schemas, multilingual metadata | Metadata page: consolidated comparison of standards |
| lifecycle-11-access.md | Metadata persistence for restricted data | Metadata page: how to create a metadata-only deposit |
| data-inventory.md | Structured inventory with per-record metadata | Metadata page: *external* metadata (repository deposits) vs. *internal* metadata (project management) |
| CROSS-fair.md | FAIR principles (F2, R1, A2) | Metadata page: practical implementation; repository pages: platform-specific FAIR support |
| CROSS-care.md | CARE principles and ethical data governance | FAIR page: brief cross-reference; repository pages: CARE-informed access options |

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
*[CARE]: Collective benefit, Authority to control, Responsibility, Ethics
*[DMP]: Data Management Plan
*[GIDA]: Global Indigenous Data Alliance
*[UNDRIP]: United Nations Declaration on the Rights of Indigenous Peoples
*[ATI]: Annotation for Transparent Inquiry
*[ARK]: Archival Resource Key
*[ICPSR]: Inter-university Consortium for Political and Social Research
*[QDR]: Qualitative Data Repository
*[OSF]: Open Science Framework
```

---

## Open questions for discussion

1. **Metadata template:** Should the metadata page include a downloadable template (spreadsheet or structured text file) that researchers fill in before depositing? This would complement the data inventory template.

2. **Preservation metadata:** Should the metadata page cover PREMIS and digital preservation metadata, or leave that to the Preserve lifecycle page (lifecycle-9-preserve.md)?

3. **Repository page depth:** The repository pages are blueprinted at 800-1,200 words each. Should they include screenshots of the deposit interface, or is text description sufficient? Screenshots risk becoming outdated when repositories update their interfaces.

4. **Repository page grouping:** Should the five repository pages be grouped under a sub-navigation heading (e.g., "Repository guides") or listed individually under "Cross-cutting guidance"? A sub-heading keeps the nav cleaner but adds a nesting level.

5. **Additional repositories:** Are there other repositories CMI researchers use that should get their own page? Candidates might include: DANS (Dutch data archive), UK Data Service, Harvard Dataverse, or Figshare.

6. **CARE depth:** How much detail should the CARE page include on specific legal frameworks (UNDRIP, Nagoya Protocol, national legislation in CMI partner countries)? Should this be a dedicated section or a collapsible "Legal context" admonition?

7. **CARE and repository pages:** Should each repository page include a section on CARE-relevant features (mediated access, community governance), or should the CARE page handle all repository-CARE connections centrally?

---

## Next steps

1. **Discuss this blueprint** to confirm the multi-page approach and resolve open questions.
2. **Adapt and publish CROSS-fair.md** from the working file: remove institutional links, refocus on repository implementation, extract CARE content.
3. **Draft CROSS-care.md** following the structure above.
4. **Draft CROSS-metadata.md** following the structure above.
5. **Draft repository pages** (Zenodo, Sikt, QDR, openICPSR, OSF) following the common structure.
6. **Update `zensical.toml`** navigation to include all new pages.
7. **Update `includes/abbreviations.md`** with any missing terms.
8. **Preview locally** with `uv run zensical serve` before committing.
