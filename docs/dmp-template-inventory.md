---
icon: lucide/table-properties
title: "CMI DMP template (inventory-centred)"
description: "A compact, inventory-first DMP variant for internal team coordination, with per-record storage and sharing decisions at the core."
tags:
  - Plan
  - DMP
  - Template
  - Data inventory
date_updated: 2026-04-05
---

# CMI DMP template (inventory-centred)

*A compact DMP variant designed for internal project coordination rather than funder review. It promotes the data inventory from an annex to the core of the document, so per-record decisions on storage, sensitivity, and sharing live alongside the data they describe. Cross-cutting policies sit in a short Section 4 that states project-level positions once.*

## When to use this variant

Use this template when the primary audience is your project team and CMI's RDM adviser, not a funder review panel. It suits projects where:

- You already have a funder-facing DMP drafted from the [full CMI template](dmp-template-full.md) and need a working operational companion.
- The data inventory is the thing the team actually consults week to week.
- Per-record storage and sharing decisions vary enough across data records that a single prose narrative would obscure them.

It is not a substitute for a funder-facing DMP where one is contractually required.

!!! tip "Pair with the data inventory guide"
    This variant is the DMP companion to [Build a data inventory](data-inventory.md). The inventory captures the *what and where*; this DMP captures the *policy and responsibility* around it.

## Executive summary

Start with a scannable table — one row per research data collection — so a reader can see the whole project at a glance.

| Data collection | Type | Sensitivity | Storage | Sharing pathway |
|---|---|---|---|---|
| Village leader interviews | Qualitative | Red | TSD | Controlled access |
| Household survey | Quantitative | Yellow | CMI M365 | Open access |
| Administrative records | Secondary | Green | CMI M365 | No external sharing |

**Columns:** *Data collection* (short name); *Type* (qualitative / quantitative / mixed / secondary / administrative); *Sensitivity* (Green / Yellow / Red / Black per [Data classification](data-classification.md)); *Storage* (primary location); *Sharing pathway* (open access / registered access / controlled access / restricted access / no external sharing).

Below the table, add 3–5 bullets summarising the key data management decisions and any unresolved gaps. A reader who only sees this page should come away knowing what data you collect, what is sensitive, and what decisions remain.

## 1. Introduction

State the purpose of the DMP in 2–3 sentences. List the guiding principles as one-line bullets (FAIR and security; Do-No-Harm; sensitivity minimisation; proportionality; access control; shared responsibility; add conflict sensitivity, CARE, or data sovereignty if applicable).

!!! note "CMI default"
    This DMP is a living document and will be revised as the project evolves.

## 2. Project summary

Record each field on its own line:

- **Full title**
- **Acronym** (if applicable)
- **Lead researcher**
- **Funding source** and programme
- **Grant ID**
- **Project period** (start – end, duration)
- **Geographical scope**

Follow with a 1–2 paragraph **research objective** describing aims, approach, and work package structure.

## 3. Data inventory

This is the core of the document. Create one sub-section per data collection. State what will be done; rationale and institutional context belong in Section 4, not here. Target 20 lines or fewer per record.

### 3.1 [Name of data collection]

**Description and method:** what this data is and how it is collected or generated. One or two sentences.

**Formats and estimated volume:** file formats and approximate size or count. One line.

**Data flow:** chain from collection to end state. Use the concise arrow format:

> Field recording (WAV) → transcription (DOCX) → anonymised transcript (DOCX) → coded dataset (NVivo) → archived transcript (PDF/A)

**Personal data and sensitivity:**

- Categories: direct identifiers / indirect identifiers / special category / none
- Sensitivity tier: Green / Yellow / Red / Black
- Key risk: one sentence

**Storage and security:**

- Storage: where stored
- Access: who has access
- Fieldwork measures: if applicable

**Sharing and archiving:**

- Pathway: open / registered / controlled / restricted / no external sharing
- Target repository and licence (e.g., Zenodo, CC BY 4.0)
- Embargo: if applicable
- Metadata-only record: whether one will be deposited if data cannot be shared

Repeat for each record. For projects with six or more records of the same type (e.g., eight interview sets across participant groups), group similar records in a summary table and give full sub-sections only to records that differ materially in sensitivity, storage, or sharing pathway.

## 4. Cross-cutting policies

State project-level positions only. Do not repeat per-record details from Section 3.

### 4.1 Legal basis and data subject rights

!!! note "CMI default"
    Lawful basis for processing personal data is public interest (GDPR Art. 6(1)(e)), supported by the Norwegian Personal Data Act §8 and Art. 89. Special category data is processed under Art. 9(2)(j) (scientific research purposes). GDPR consent is not the lawful basis and is only used to supplement public interest for specific bounded activities (recording, name use, archiving for reuse).

Summarise data subject rights in 2–3 sentences, citing Art. 89(2) and PDA §17. State whether data crosses borders and the applicable safeguard mechanism (joint controllership Art. 26, research derogation Art. 49(1)(d), or platform-based solution). See [GDPR and legal compliance](CROSS-gdpr-and-legal-compliance.md).

### 4.2 Security and storage

State the project-wide security baseline, any higher-assurance options in use (reference the Section 3 records that use them), and the fieldwork protocol if applicable.

!!! note "CMI default"
    M365 ecosystem with encryption at rest and in transit, MFA, and role-based access. For fieldwork: device encryption, upload within 24 hours, deletion from local devices after verification.

### 4.3 Sharing and archiving

State the project-level sharing position, documentation standards (README per dataset, codebooks, data dictionaries), the repositories and licences that apply to this project, and the embargo position. Metadata is always deposited, even when data cannot be shared.

!!! note "CMI default"
    'Open as possible, closed as necessary.' Default licences: CC0 (preferred) or CC BY 4.0 for data; MIT, BSD, or Apache 2.0 for code. Default embargo: 1–2 years after project completion. Restriction beyond that requires specific justification.

### 4.4 Retention and disposal

!!! note "CMI default retention periods"
    Primary research data 10 years; administrative records 5 years; contact information up to 3 years; audio and video deleted after transcription unless it is the research data; consent documentation retained as long as related data exists. Maintain a deletion log covering all systems including partner copies.

Note any project-specific deviations.

### 4.5 Ethics and oversight

State the ethical context in 1–2 sentences, list key ethical risks and mitigation measures (max 5 bullets), and the approvals and notifications that apply.

!!! note "CMI default"
    NESH guidelines apply. Sikt notification required; CMI REC consultation voluntary; partner-country ethics boards where applicable; REK only for medical or health research. Additional frameworks (Declaration of Helsinki, ALLEA) only where they apply.

Close with the project's position on IP and data ownership.

## 5. Roles, responsibilities, and resources

### 5.1 Institutions and roles

List all institutions and describe each one's role in data management. For partners, note what data they collect, process, or store and their controller or processor role. Name the PI's responsibilities and CMI's Research Data Management Adviser role.

!!! note "CMI default"
    Chr. Michelsen Institute (CMI), Norway, is the host institution and project coordinator, responsible for overall data storage, security, GDPR compliance, and repository deposit.

### 5.2 Resources and costs

Estimate data management costs. Use this table as a starting point:

| Item | Estimated cost | Notes |
|---|---|---|
| Repository deposit fees |  | e.g., QDR per-deposit fee |
| Transcription |  | In-house or outsourced |
| Data storage above baseline |  | CMI M365 included in overhead; TSD or similar priced separately |
| Research assistant time for data management |  |  |

Note which costs are covered by CMI overhead versus the ones that need to be budgeted in the grant.

## 6. FAIR operationalisation

Summarise how the project implements each FAIR principle. One line per principle:

- **Findable:** datasets deposited with a DOI; metadata-only records for restricted data; PI's ORCID linked.
- **Accessible:** open datasets via the chosen repository; controlled access where needed; standard protocols throughout.
- **Interoperable:** tabular data in CSV with codebook; transcripts in PDF/A; DDI metadata for survey data.
- **Reusable:** CC0 or CC BY 4.0 as per Section 4.3; README and codebook per dataset; analysis code in an open repository.

If a principle cannot be fully implemented (common for sensitive qualitative research), state what will be done and what constraint prevents full implementation.

## 7. Monitoring and updates

!!! note "CMI default"
    This DMP is a living document. The PI and CMI's Research Data Management Adviser are jointly responsible for updates. Review points: after ethical approvals; at project mid-point; before archiving and final outputs; ad hoc for significant changes.

| Version | Date | Changes | Author |
|---|---|---|---|
| 1.0 |  | Initial DMP |  |
