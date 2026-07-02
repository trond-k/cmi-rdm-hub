---
icon: lucide/file-text
title: "Data management plan template"
description: "CMI's institutional DMP template: section structure and default language you can copy into any DMP tool, with pointers to the underlying guidance."
tags:
  - DMP
  - Plan
  - Template
notes: ""
date_updated: 2026-07-02
---

# CMI data management plan template

*This is CMI's institutional DMP template, structured around how CMI projects actually write DMPs rather than around any single funder format. Copy it into your DMP tool of choice, keep the section order, and adapt the default language to your project. The template is deliberately concise: it sets the structure and the CMI defaults, while the institutional positions on GDPR, security, ethics, and sharing live in the linked guidance pages.*

## How to use this template

Each section below states what it should cover and supplies the default CMI language you can keep verbatim, edit, or replace. Lines marked as *CMI default* are recommended starting language; everything else is a prompt for your project-specific content.

This template stays short on purpose. Work with these pages alongside it for the underlying institutional positions:

- [GDPR and legal compliance](CROSS-gdpr-and-legal-compliance.md) for lawful basis, consent, transfers, and retention.
- [Data classification](data-classification.md) for the Green, Yellow, Red, and Black tiers.
- [Build a data inventory](data-inventory.md) for the structured register that Annex 1 points to.
- [Foundations of data sharing](foundations-of-data-sharing.md) for the five sharing pathways and licensing.
- [Sikt form walkthrough](sikt-form-walkthrough.md) as a companion to filing the notification.

The template covers the topics required by major funders (the Research Council of Norway, Horizon Europe, Science Europe) through a similar but differently arranged structure. If a funder requires a specific format, this template maps onto it without loss.

## 1. Introduction

### 1.1 Purpose and scope

State that the DMP outlines how the project manages research data responsibly, ethically, and transparently, and note the project's commitment to legal compliance, institutional policies, and the FAIR principles.

??? tip "CMI default language"
    "This DMP is a living document and will be revised as the project evolves."

### 1.2 Guiding principles

Set out the principles guiding data management for the project, adapted to its context. The defaults below are the CMI baseline; add context-specific principles where they apply.

??? tip "CMI default principles"
    Include all that apply, adapting the language to the project:

    - **FAIR, transparency, and security:** FAIR balanced with ethical responsibility and participant protection. "As open as possible, as closed as necessary."
    - **Do-no-harm:** no action, output, or outcome shall adversely affect participants, stakeholders, or third parties.
    - **Sensitivity minimisation:** only data essential to the research objectives is collected and retained.
    - **Proportionality:** security measures matched to the sensitivity and risk level of each dataset.
    - **Access control (least privilege):** role-based access, limited to individuals with a justified need.
    - **Shared responsibility:** all project members share accountability for lawful and ethical data management.

??? tip "Context-specific principles to add where relevant"
    - **Conflict sensitivity** for projects in conflict-affected or politically sensitive contexts.
    - **CARE principles** for research involving communities in the Global South.
    - **Data sovereignty** for projects involving indigenous or marginalised communities.

## 2. Project data summary

### 2.1 About the project

Format each metadata field as its own paragraph using **Label:** Value, with a blank line between fields. Follow the metadata with the research objective in one to two paragraphs.

??? tip "Metadata fields"
    - **Full title:** the project's full title.
    - **Acronym:** if applicable.
    - **Funding source:** funder name and programme.
    - **Grant ID:** grant or project number.
    - **Project period:** start date – end date (duration).
    - **Geographical scope:** countries and regions.

### 2.2 Purpose of data collection

Describe why data is collected, organised by work package or research question, and how each major collection activity contributes to the project's objectives.

## 3. Roles and responsibilities

### 3.1 Institutions

List each institution and describe its role in data management. For each partner, note what data they collect, process, or store, whether they act as controller or processor, and any infrastructure they provide. Note external compliance partners such as Sikt Data Protection Services for Research.

??? tip "CMI default language for the host institution"
    "Chr. Michelsen Institute (CMI), Norway, is the host institution and project coordinator. CMI is responsible for overall project management, data storage and security, GDPR compliance, and repository deposit of open-access publications. CMI's Research Data Management Adviser supports development of the Data Management Plan."

### 3.2 Governance and project groups

Describe internal governance for data management, adapted to project scale.

??? tip "CMI default elements"
    - Core leadership team or project management team chaired by the PI.
    - Ethics oversight (CMI Research Ethics Committee, external ethics boards).
    - Data protection coordination (CMI's Research Data Management Adviser, DPO, Sikt).
    - Advisory board or stakeholder group, if applicable.

## 4. Legal and ethical considerations

### 4.1 GDPR compliance

State whether the project processes personal data, from whom, and which data protection frameworks apply (GDPR, partner-country legislation). The eight points below cover the institutional position. Each maps to a section of the [GDPR and legal compliance](CROSS-gdpr-and-legal-compliance.md) page.

**Legal basis for processing.** State the lawful basis and the framework articles you rely on.

??? tip "CMI default"
    Public interest (GDPR Art. 6(1)(e)), supported by the Norwegian Personal Data Act §8 and GDPR Art. 89. This applies to all CMI research, not only registry-based or large-scale studies. For special category data, rely on Art. 9(2)(j) for scientific research purposes. GDPR consent is **not** the lawful basis for general processing. Topics sometimes treated as requiring consent, such as recording, name use in publications, and archiving for reuse, are matters to inform participants about in the information letter, not GDPR consent elements layered on top of public interest.

**Types of personal data.** List the categories you process: direct identifiers, indirect identifiers, special category data (Art. 9), and other sensitive categories such as financial or immigration data. Note any third-person data captured incidentally in interviews or field notes.

**Information and consent.** The information letter is the primary instrument: it informs participants and seeks ethical consent (voluntary, informed, revocable). It does not ask for GDPR consent to process data. The letter should cover recording (where applicable), whether and how participants may be identified or named in publications, archiving for future reuse, storage and retention, and how rights can be exercised. Where the participant has a meaningful choice, present it as a project decision they make, not as a separate GDPR consent element. Describe how voluntariness is ensured (gatekeepers, power dynamics) and how the letter is adapted for fieldwork (oral delivery, high-risk settings).

**Data minimisation and anonymisation.** Describe how data minimisation is applied and the anonymisation or pseudonymisation strategy.

??? tip "CMI default"
    Direct identifiers are removed or pseudonymised as early as possible. Linkage keys are stored separately, accessible only to the PI and the designated data steward.

**Data security.** Describe storage tiers, access control, and fieldwork practice. Storage tier should match data sensitivity, per the [data classification](data-classification.md) tiers.

??? tip "CMI default"
    M365 ecosystem with encryption, MFA, role-based access, and tiered restrictions by sensitivity. For higher assurance, use TSD/Nettskjema, Tresorit, or Proton Drive. For fieldwork, use device encryption, daily upload, and local encrypted backup. Recordings are uploaded within 24 hours and deleted from local devices after verification.

**Data subject rights.** Under the public interest basis, data subject rights are modified by Art. 89(2) and the Norwegian Personal Data Act §17. There is no GDPR consent to withdraw (only ethical withdrawal and the right to object), the right to erasure is limited (Art. 17(3)(d)), and the right to data portability does not apply. The information letter should give a concrete deadline after which deletion may no longer be feasible.

**International data transfers.** State whether personal data crosses borders, between which countries, and under what circumstances. Apply CMI's proportional approach: practical safeguards for CMI researchers abroad and research assistants; joint controllership agreements (Art. 26) preferred over SCCs for partner institutions; the research derogation (Art. 49(1)(d)) as an alternative for occasional, non-repetitive transfers; platform-based solutions for US-based partners.

**Retention and disposal.** Describe the deletion procedure across all systems, including partner copies, and maintain a deletion log.

??? tip "CMI default retention periods"
    - Primary research data: 10 years.
    - Administrative records: 5 years.
    - Contact information: up to 3 years (if stated in the information letter).
    - Audio and video recordings: deleted after transcription unless the recordings *are* the research data.
    - Consent documentation: retained as long as related data exists.

### 4.2 Intellectual property and data ownership

Identify data ownership. For multi-partner projects, describe how ownership is formalised through partnership agreements or joint controllership arrangements. Note licensing terms for any external or secondary data.

??? tip "CMI default"
    Publications under CC BY 4.0, deposited in CMI's institutional repository. Datasets under CC BY 4.0 or CC0.

### 4.3 Research ethics

Describe the ethical context: what makes the project ethically sensitive, the key risks, the mitigation measures, and the applicable ethical guidelines and oversight bodies.

??? tip "Key ethical issues to consider"
    Select and adapt: emotional or psychological distress; social or reputational risks; legal or administrative consequences; professional or institutional risks; physical security risks; power dynamics; third-party risks.

??? tip "CMI defaults: guidelines, approvals, and notifications"
    - **Primary framework:** NESH guidelines.
    - **CMI Research Ethics Committee (REC):** advisory, not approval-based; consultation is voluntary but encouraged for ethically complex projects.
    - **Other applicable frameworks:** Declaration of Helsinki, ALLEA, Good Clinical Practice, Montreal Statement, and others as relevant.
    - **Sikt notification:** required, filed 30 or more days before data collection.
    - **REK:** only for medical or health research.
    - **Partner-country ethics boards:** as required.

## 5. Expected data and sensitivity

Give an overview of data types organised by sensitivity level. CMI uses a four-tier classification (Green, Yellow, Red, Black) based on risk of harm from exposure; personal data is Red by default. A single project will typically have data objects at multiple tiers, and the classification applies to the data object in its current state. See [Data classification](data-classification.md) for full tier definitions, and reference the data inventory in Annex 1 for the per-dataset detail. For secondary data, describe the source, access conditions, and sensitivity.

## 6. Processing, quality, and analysis

Describe the data pipeline from collection through to analysis-ready form: transcription procedures (who, when, what language), the anonymisation or pseudonymisation steps, and quality assurance practices. Quality assurance has two phases: during collection (training, pilots, back-translation, validation) and after collection (cleaning, consistency checks, transcription verification). Name the analysis tools you expect to use, such as NVivo, MAXQDA, Atlas.ti, Stata, R, or SPSS, and any cross-work-package coordination such as shared codebooks or analysis workshops.

## 7. Documentation, metadata, and archiving

### 7.1 Documentation

State the minimum documentation expected for each dataset, and add codebooks, interview guides, observation protocols, and data dictionaries where relevant.

??? tip "CMI default"
    "At minimum, each dataset should have a README file describing the data contents, collection context, variable definitions, and any known limitations."

### 7.2 Metadata standards

Identify the metadata standards you will use (DDI for survey data, Dublin Core for general datasets) and note your file naming conventions and folder structure. See [Name files and structure folders](file-and-folder-naming.md) for the institutional convention.

### 7.3 Sharing and archiving

Apply CMI's [five sharing pathways](foundations-of-data-sharing.md): open access, registered access, controlled access, restricted access, and no external sharing. Select the most open pathway feasible for each dataset; restriction requires specific justification.

Full sharing of qualitative data is rarely feasible. Controlled access to de-identified excerpts or metadata-only records is the realistic pathway. Metadata is always shared unless it creates risk.

??? tip "CMI default repositories, embargo, and licences"
    - **Repositories:** Zenodo (open datasets, code, supplementary materials); OSF (replication packages); openICPSR (quantitative social science); QDR (qualitative data with mediated access; per-deposit fees apply); Sikt's Research Data Archive (quantitative survey data); CMI internal repository as the minimum baseline.
    - **Embargo:** 1 to 2 years after project completion.
    - **Licences:** CC0 (preferred) or CC BY 4.0 for data; MIT, BSD, or Apache 2.0 for code.

## 8. Monitoring and updates

The DMP is a living document. The PI and CMI's Research Data Management Adviser are jointly responsible for keeping it current.

??? tip "CMI default review points"
    - After ethical approvals.
    - At project mid-point.
    - Before archiving and final outputs.
    - Ad hoc for significant changes.

    Updates are logged with version numbers, dates, and a description of changes.

## Annex 1: Data inventory

The data inventory is a separate document that lists every research data record the project collects or generates. Each entry represents a coherent data collection activity, not an individual file. See [Build a data inventory](data-inventory.md) for the full guide. The fields below are the minimum a DMP-stage inventory should contain.

| Field | What it captures |
|---|---|
| Name and description | What this data is and where it comes from. |
| Collection method | How the data is collected or generated. |
| Participant group | Which participant group(s) this relates to, if applicable. |
| Formats and estimated volume | Expected file formats and approximate size or number of records. |
| Artefacts | Concrete data objects produced, such as audio recordings, transcripts, anonymised datasets, coded datasets, and field notes. |
| Data flow | How data moves from collection through processing to end state. |
| Personal data categories | What personal data is involved, if any. |
| Sensitivity level | Green, Yellow, Red, or Black, per section 5. |
| Responsible party | Who collects, stores, and manages this data. |

!!! info "Last reviewed"
    This page was last reviewed on 28 April 2026. DMP and GDPR guidance evolve; verify against the linked guidance pages and the latest funder requirements before relying on the defaults verbatim.
