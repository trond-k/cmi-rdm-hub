# Data Management Plan — CMI Data Inventory Template

<!-- A data-inventory-centred variant of CMI's institutional DMP template. Designed for
     internal use where the primary audience is the project team and CMI's RDM adviser,
     not a funder review panel.

     Key differences from the standard CMI template (dmp-cmi.md):
     - Executive summary with a scannable table up front
     - Data inventory promoted from annex to Section 3 (the core of the document)
     - Legal/ethical compressed from 11 sub-sections to 5 cross-cutting policy sections
     - Per-record details (storage, sharing, sensitivity) live in the inventory, not
       repeated in the policy sections
     - FAIR operationalisation section added
     - Shorter target output (~250–350 lines vs 400–500)

     The full institutional positions on GDPR, data security, open science, and standard
     recommendations are already in the system prompt (loaded from the institutional/
     content files). This template defines the SECTION STRUCTURE — the LLM synthesises
     the detailed guidance from the policy documents when filling in each section. -->


## Output length and compression targets

This template is designed to produce **shorter, more focused output** than the standard CMI template. Follow these constraints:

- **Section 4 (Cross-cutting policies):** maximum 80 output lines. State project-level positions in 2–3 sentences per sub-section. Do not enumerate each GDPR right separately — summarise the position and cite the relevant articles. Do not repeat details already stated per-record in Section 3.
- **Section 1 (Introduction):** maximum 15 output lines. No background on what a DMP is.
- **Section 7 (Monitoring):** maximum 15 output lines.
- **Preferred phrasing:** use concise, direct sentences. Avoid padding phrases like "It is important to note that" or "In this regard, the project will."
- **Heading case:** use sentence case for all headings (e.g., "Cross-cutting policies", not "Cross-cutting Policies").
- **When institutional defaults apply unchanged:** state the default once and cite the recommendation ID. Do not elaborate on why the default is appropriate unless the project context creates a tension or exception.
- **Project-specific choices are recommendations, not decisions.** Storage tools, repositories, sharing pathways, and archiving plans are suggestions based on the project context. Use "the project will consider", "the recommended approach is", "prioritise archives such as" — not "must", "shall", or bare "will be". Institutional defaults (lawful basis, retention periods, security baseline) can be stated as facts.
- **For projects with 6 or more data records of the same type** (e.g., 8 interview sets across different participant groups): group similar records in a summary table within Section 3 instead of giving each its own full sub-section. Provide a full sub-section only for records that differ materially in sensitivity, storage, or sharing pathway.


## Executive summary

Produce a markdown table with one row per research data collection identified in the parsed project description. Columns:

| Data collection | Type | Sensitivity | Storage | Sharing pathway |
|---|---|---|---|---|

- **Data collection:** short name (e.g., "Village leader interviews")
- **Type:** qualitative / quantitative / mixed / secondary / administrative
- **Sensitivity:** Green / Yellow / Red / Black (per CMI's data classification scheme)
- **Storage:** primary storage location (e.g., "CMI M365", "TSD", "Tresorit")
- **Sharing pathway:** one of CMI's five pathways — open access / registered access / controlled access / restricted access / no external sharing

Below the table, write **3–5 bullet points** summarising the key data management decisions and any unresolved gaps. These bullets should give a reader who only reads this section a clear picture of what data the project collects, what's sensitive, and what decisions remain. State each decision or gap at a higher level than the Section 3 details — name the issue and the conclusion, not the full rationale. Do NOT use `[RESEARCHER INPUT NEEDED]` marker syntax in these bullets — describe gaps in plain language (e.g., "Cross-border transfer mechanisms with partner institutions have not yet been established"). The formal markers belong in Sections 3–4 where they render as callout blocks. Do not add a sub-heading above the bullets — they follow directly after the table.


## 1. Introduction

- State the purpose of this DMP in 2–3 sentences. Do not explain what a DMP is in general.
- **CMI default:** "This DMP is a living document and will be revised as the project evolves."
- List guiding principles as **one-liner bullets** — select from:
  - FAIR, transparency, and security
  - Do-No-Harm
  - Sensitivity minimisation
  - Proportionality
  - Access control (least privilege)
  - Shared responsibility
  - Conflict sensitivity (if applicable)
  - CARE principles (if applicable)
  - Data sovereignty (if applicable)


## 2. Project summary

Format each field as its own paragraph using **Label:** Value, with a blank line between fields. If a field value is unknown, place the `[RESEARCHER INPUT NEEDED]` marker on its own line below the label — not inline after the colon.

- **Full title**
- **Acronym** (if applicable)
- **Lead researcher**
- **Funding source** and programme
- **Grant ID**
- **Project period** (start – end, duration)
- **Geographical scope**

Follow the metadata fields with:

**Research objective:** 1–2 paragraphs describing the project's aims, approach, and work package structure. Same bold-label format as the fields above.


## 3. Data inventory

This is the core of the document. Create one sub-section (### 3.N) per research data collection identified in the parsed project description. Each record represents a coherent data collection activity — not an individual file.

For each data record, use this structure. **State what will be done, not why** — rationale and institutional context belong in Section 4, not here. Target **20 lines or fewer per record.**

### 3.N [Name of data collection]

**Description and method:** What this data is and how it is collected or generated. 1–2 sentences.

**Formats and estimated volume:** File formats and approximate size or count. One line.

**Data flow:** Chain from collection to end state. Use the concise chain format: "Field recording (WAV) → transcription (DOCX) → anonymised transcript (DOCX) → coded dataset (NVivo) → archived transcript (PDF/A)". Expand to a short paragraph only if the flow has branches or non-obvious steps.

**Personal data and sensitivity:**

- Categories: [direct identifiers, indirect identifiers, special category, none]
- Sensitivity tier: [Green / Yellow / Red / Black]
- Key risk: [one sentence]

**Storage and security:**

- Storage: [where stored]
- Access: [who has access]
- Fieldwork measures: [if applicable; omit if not]

**Sharing and archiving:**

- Pathway: [open / registered / controlled / restricted / no external sharing]
- Target repository and licence: [e.g., "Zenodo, CC BY 4.0"]
- Embargo: [if applicable; omit if not]
- If restricted: [whether a metadata-only record will be deposited]

Each field must use this bullet-list format — a blank line after the bold label, then each item on its own line starting with a dash. Do not place multiple items on the same line. Do not explain why a measure is needed — just state the measure.

Do NOT include institutional defaults in each record (e.g., CMI's general retention policy, MFA requirements, encryption standards). Those belong in Section 4. Do NOT add sub-headings beyond the six fields above.


## 4. Cross-cutting policies

This section states **project-level positions only**. Do not repeat per-record details from Section 3. For each sub-section, state the position in 2–3 sentences, cite the relevant legal basis or recommendation ID, and note any project-specific exceptions or tensions.

### 4.1 Legal basis and data subject rights

- Legal basis for processing personal data. **CMI default:** public interest (GDPR Art. 6(1)(e)), supported by the Norwegian Personal Data Act §8 and Art. 89. For special category data: Art. 9(2)(j). State this in 1–2 sentences — do not discuss consent as a separate topic (consent is not the lawful basis).
- Data subject rights under the public interest basis: summarise the position in 2–3 sentences citing Art. 89(2) and the Norwegian Personal Data Act §17. Do not enumerate each right separately.
- International transfers: state whether data crosses borders and the applicable safeguard mechanism (joint controllership Art. 26, research derogation Art. 49(1)(d), or platform-based solution). One paragraph maximum.

### 4.2 Security and storage

- Project-wide security baseline. **CMI default:** M365 ecosystem, encryption at rest and in transit, MFA, role-based access.
- Higher-assurance options in use (TSD, Tresorit, Proton Drive) — reference which data records use them (by name, pointing back to Section 3).
- Fieldwork protocol if applicable. **CMI default:** device encryption, upload within 24 hours, delete from local devices after verification.

### 4.3 Sharing and archiving

- Project-level sharing position (CMI's "open as possible, closed as necessary" default).
- Documentation standards: README per dataset, codebooks, data dictionaries.
- **CMI default repositories and licences:** reference the institutional defaults (CC0/CC BY 4.0 for data, MIT/BSD/Apache for code). Do not list all repository options — only those that apply to this project's data records.
- **CMI default embargo:** 1–2 years after project completion.
- Note that metadata is always deposited, even when data cannot be shared.

### 4.4 Retention and disposal

- **CMI default retention periods:** primary research data 10 years; administrative records 5 years; contact information up to 3 years; audio/video deleted after transcription unless it is the research data; consent documentation retained as long as related data exists.
- Deletion procedure across all systems including partner copies. **CMI default:** maintain a deletion log.
- Any project-specific deviations from the defaults.

### 4.5 Ethics and oversight

- Ethical context: what makes this project ethically sensitive (1–2 sentences).
- Key ethical risks and mitigation measures (bullet list, maximum 5 bullets).
- **Approvals and notifications:** Sikt notification (required); CMI Research Ethics Committee consultation (voluntary but encouraged); partner-country ethics boards; REK only if medical/health research.
- **Guidelines:** NESH as default; note additional frameworks only if they apply (Declaration of Helsinki, ALLEA, etc.).
- **IP and ownership:** data ownership position; licensing approach; partnership agreements if multi-partner.


## 5. Roles, responsibilities, and resources

### 5.1 Institutions and roles

- List all institutions and describe each one's role in data management.
- **CMI default:** "Chr. Michelsen Institute (CMI), Norway — Host institution and project coordinator. Responsible for overall data storage, security, GDPR compliance, and repository deposit."
- For partners: what data they collect/process/store, controller or processor role.
- Note the PI's responsibilities and CMI's Research Data Management Adviser role.

### 5.2 Resources and costs

- Estimated data management costs or resource needs. Use placeholder rows if the parsed description does not specify:

| Item | Estimated cost | Notes |
|---|---|---|
| Repository deposit fees | [RESEARCHER INPUT NEEDED: estimate or "no cost" for free repositories] | e.g., QDR per-deposit fee |
| Transcription | [RESEARCHER INPUT NEEDED: estimate] | In-house or outsourced |
| Data storage (above baseline) | [RESEARCHER INPUT NEEDED: estimate if TSD or similar] | CMI M365 included in overhead |
| Research assistant time for data management | [RESEARCHER INPUT NEEDED: estimate] | |

- Note which costs are covered by CMI overhead vs. need to be budgeted in the grant.


## 6. FAIR operationalisation

Summarise how the project implements each FAIR principle in a compact list. One line per principle — no elaboration unless the project context creates a notable exception or tension.

- **Findable:** [e.g., "All datasets deposited with DOI in Zenodo/QDR/Sikt. Metadata-only records for restricted data. PI's ORCID linked."]
- **Accessible:** [e.g., "Open datasets via Zenodo. Controlled access to qualitative data via QDR. All access mechanisms use standard protocols."]
- **Interoperable:** [e.g., "Tabular data in CSV with codebook. Transcripts in PDF/A. DDI metadata for survey data."]
- **Reusable:** [e.g., "CC0 for quantitative data, CC BY 4.0 for qualitative metadata. README and codebook per dataset. Analysis code in project OSF repository."]

If a principle cannot be fully implemented (common for sensitive qualitative research), state what will be done and what constraint prevents full implementation.


## 7. Monitoring and updates

- **CMI default:** "This DMP is a living document. PI and CMI's Research Data Management Adviser are jointly responsible for updates."
- **Review points:** after ethical approvals; at project mid-point; before archiving and final outputs; ad hoc for significant changes.
- Version log table:

| Version | Date | Changes | Author |
|---|---|---|---|
| 1.0 | [project start date] | Initial DMP | [PI name] |
