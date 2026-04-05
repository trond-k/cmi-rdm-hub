---
icon: lucide/clipboard-list
title: "CMI DMP template (full)"
description: "CMI's institutional Data Management Plan template, structured around CMI's own project experience and mappable to major funder formats."
tags:
  - Plan
  - DMP
  - Template
date_updated: 2026-04-05
---

# CMI DMP template (full)

*This is CMI's own institutional DMP template, derived from the structure used in actual CMI projects. It covers the topics required by the Research Council of Norway, Horizon Europe, and Science Europe through a familiar but differently arranged structure. Use it as your starting point, then remap sections to a specific funder format if required.*

## How to use this template

Copy each section below into your own DMP document and adapt the content to your project. Where a **CMI default** callout appears, you can use the text verbatim unless your project has a specific reason to deviate. Where a section says *what to cover*, that is the prompt for your own project-specific writing.

The template is deliberately comprehensive. Some sections (for example, international transfers or CARE principles) may not apply to your project, and it is fine to drop them with a short note explaining why. The [inventory-centred variant](dmp-template-inventory.md) suits internal team coordination, and the [Light-DMP checklist](dmp-template-light.md) is a shorter starting point for small, low-risk projects.

!!! tip "Keep it living"
    A DMP written once and filed away is a compliance artefact, not a management tool. Schedule reviews at key milestones and update both this document and the [data inventory](data-inventory.md) together.

## 1. Introduction

### 1.1 Purpose and scope

State that the DMP outlines the project's approach to managing research data responsibly, ethically, and transparently, and note commitment to legal compliance, institutional policies, and the FAIR principles.

!!! note "CMI default"
    This DMP is a living document and will be revised as the project evolves.

### 1.2 Guiding principles

Describe the principles guiding the project's data management, tailored to the project context. Select the principles that apply:

- **FAIR, transparency, and security:** FAIR balanced with ethical responsibility and participant protection. 'As open as possible, as closed as necessary.'
- **Do-No-Harm:** no action, output, or outcome shall adversely affect participants, stakeholders, or third parties.
- **Sensitivity minimisation:** only data essential to the research objectives is collected and retained.
- **Proportionality:** security measures matched to the sensitivity and risk level of each dataset.
- **Access control (principle of least privilege):** role-based, limited to individuals with a justified need.
- **Shared responsibility:** all project members share accountability for lawful and ethical data management.

Add context-specific principles where relevant: **conflict sensitivity** (for projects in conflict-affected or politically sensitive contexts), **CARE principles** (for research involving communities in the Global South), **data sovereignty** (for projects involving indigenous or marginalised communities).

## 2. Project data summary

### 2.1 About the project

Record each field as its own line, with a blank line between fields:

- **Full title:** the project's full title
- **Acronym:** if applicable
- **Funding source:** funder name and programme
- **Grant ID:** grant or project number
- **Project period:** start date – end date (duration)
- **Geographical scope:** countries and regions

Follow the metadata with a one-to-two-paragraph statement of the research objective.

### 2.2 Purpose of data collection

Describe why data is collected, organised by work package or research question, and how each major data collection activity contributes to the project's objectives.

## 3. Roles and responsibilities

### 3.1 Institutions

List all institutions and describe each one's role in data management. For each partner: what data they collect, process, or store; their controller or processor role; any infrastructure they provide. Note external compliance partners such as Sikt.

!!! note "CMI default"
    Chr. Michelsen Institute (CMI), Norway, is the host institution and project coordinator. CMI is responsible for overall project management, data storage and security, GDPR compliance, and repository deposit of open-access publications. CMI's Research Data Management Adviser supports development of the Data Management Plan.

### 3.2 Governance and project groups

Describe the project's internal governance for data management. Adapt to project scale: core leadership or project management team chaired by the PI; ethics oversight (CMI Research Ethics Committee, external ethics boards); data protection coordination (CMI's Data Management Adviser, DPO, Sikt); advisory board or stakeholder group if applicable.

## 4. Legal and ethical considerations

### 4.1 GDPR compliance

State whether the project processes personal data and from whom, and note which data protection frameworks apply (GDPR, partner-country legislation). For detailed background, see [GDPR and legal compliance](CROSS-gdpr-and-legal-compliance.md).

???+ note "4.1.1 Legal basis for processing"
    **CMI default:** public interest (GDPR Art. 6(1)(e)), supported by the Norwegian Personal Data Act §8 and GDPR Art. 89. This applies to all CMI research, not only registry-based or large-scale studies. For special category data, the basis is Art. 9(2)(j) (scientific research purposes).

    GDPR consent is **not** the lawful basis for general data processing. It supplements public interest only for specific bounded activities: recording, name use in publications, and archiving for future reuse.

??? note "4.1.2 Types of personal data"
    List the categories involved: direct identifiers, indirect identifiers, special category data (Art. 9), and other sensitive data (financial, immigration, etc.). Note any third-person data in interviews or field notes.

??? note "4.1.3 Information and consent"
    The information letter is the primary instrument. It informs; it does not ask for GDPR consent to process data. Use separate consent elements for recording, name use, and archiving for reuse.

    Describe how voluntariness is ensured (gatekeepers, power dynamics), and any adaptation for fieldwork contexts (oral delivery, high-risk settings). See [Informed consent and information letters](CROSS-ethics.md).

??? note "4.1.4 Data minimisation and anonymisation"
    Describe how data minimisation is applied and the anonymisation or pseudonymisation strategy.

    **CMI default:** direct identifiers are removed or pseudonymised as early as possible. Linkage keys are stored separately, accessible only to the PI and a designated data steward.

??? note "4.1.5 Data security"
    **CMI default:** M365 ecosystem with encryption, MFA, role-based access, and tiered restrictions by sensitivity. For higher assurance: TSD or Nettskjema, Tresorit, or Proton Drive.

    For fieldwork: device encryption, daily upload, and local encrypted backup. Recordings uploaded within 24 hours, deleted from local devices after verification.

??? note "4.1.6 Data subject rights"
    Under the public interest basis, rights are modified by Art. 89(2) and the Norwegian Personal Data Act §17. In particular: there is no GDPR consent to withdraw (only ethical withdrawal and the right to object); the right to erasure is limited (Art. 17(3)(d)); the right to data portability does not apply. The information letter should include a concrete deadline after which deletion may no longer be feasible.

??? note "4.1.7 International data transfers"
    State whether personal data crosses borders, between which countries, and under what circumstances. Apply CMI's proportional approach: practical safeguards for CMI researchers abroad and research assistants; joint controllership agreements (Art. 26) preferred over SCCs for partner institutions; the research derogation (Art. 49(1)(d)) as an alternative; platform-based solutions for US-based partners.

??? note "4.1.8 Retention and disposal"
    **CMI default retention periods:** primary research data 10 years; administrative records 5 years; contact information up to 3 years (if stated in the information letter); audio and video recordings deleted after transcription unless they are the research data; consent documentation retained as long as related data exists.

    Describe the deletion procedure across all systems including partner copies. **CMI default:** maintain a deletion log.

### 4.2 Intellectual property and data ownership

Identify data ownership. For multi-partner projects, describe how ownership is formalised (partnership agreements, joint controllership). Note licensing terms for any external or secondary data.

!!! note "CMI default"
    Publications are released under CC BY 4.0 and deposited in CMI's institutional repository. Datasets are released under CC BY 4.0 or CC0.

### 4.3 Research ethics

Describe the ethical context — what makes the project ethically sensitive. Select and adapt key ethical issues: emotional or psychological distress; social or reputational risks; legal or administrative consequences; professional or institutional risks; physical security risks; power dynamics; third-party risks. Describe mitigation measures as specific actions.

!!! note "CMI default — guidelines and oversight"
    NESH guidelines apply. The CMI Research Ethics Committee is advisory, not approval-based; consultation is voluntary but encouraged for ethically complex projects. Add other applicable frameworks (Declaration of Helsinki, ALLEA, Good Clinical Practice, Montreal Statement) as relevant.

    **Approvals and notifications:** Sikt notification (required, filed 30+ days before data collection); CMI REC consultation (voluntary); REK (only for medical or health research); partner-country ethics boards.

## 5. Expected data and sensitivity

Give an overview of data types organised by sensitivity level. Reference the [data inventory](data-inventory.md) annex for per-record details. For secondary data, describe source, access conditions, and sensitivity.

!!! note "CMI default — classification"
    Use CMI's Green / Yellow / Red / Black classification based on risk of harm from exposure. Personal data is Red by default. See [Data classification](data-classification.md) for tier definitions. A single project typically has data objects at multiple tiers — classification applies to the object in its current state.

## 6. Processing, quality, and analysis

Describe the data processing pipeline from collection through to analysis-ready form. Cover:

- Transcription procedures (who, when, what language).
- Anonymisation and pseudonymisation steps in the pipeline.
- Quality assurance during collection (training, pilots, back-translation, validation) and after (cleaning, consistency checks, transcription verification).
- Analysis tools (NVivo, MAXQDA, Atlas.ti, Stata, R, SPSS, etc.).
- Cross-work-package coordination if applicable (shared codebooks, analysis workshops).

## 7. Documentation, metadata, and archiving

### 7.1 Documentation

Describe the documentation that accompanies each dataset: codebooks, interview guides, observation protocols, data dictionaries.

!!! note "CMI default"
    At minimum, each dataset has a README file describing the data contents, collection context, variable definitions, and any known limitations.

### 7.2 Metadata standards

Name the metadata standards used (DDI for survey data, Dublin Core for general datasets) and the file-naming conventions and folder structure. See [Name files and structure folders](file-and-folder-naming.md).

### 7.3 Data sharing and archiving

Apply CMI's five sharing pathways from the institutional Open Science Policy: open access, registered access, controlled access, restricted access, no external sharing. Select the most open pathway feasible for each dataset. Full sharing of qualitative data is rarely feasible: controlled access to de-identified excerpts or metadata-only records is often the realistic pathway. **Metadata is always shared** unless doing so creates risk.

!!! note "CMI default — repositories, licences, embargo"
    **Preferred repositories:** Zenodo (open datasets, code, supplementary materials), OSF (replication packages), openICPSR (quantitative social science), QDR (qualitative data, mediated access, per-deposit fees apply), Sikt's Research Data Archive (quantitative survey data), CMI's internal repository (minimum baseline).

    **Default licences:** CC0 (preferred) or CC BY 4.0 for data; MIT, BSD, or Apache 2.0 for code.

    **Default embargo:** 1–2 years after project completion. Restriction beyond that requires specific justification.

## 8. Monitoring and updates

Describe how the plan is kept current.

!!! note "CMI default"
    This DMP is a living document and will be revised as the project progresses. The PI and CMI's Research Data Management Adviser are jointly responsible. Review points: after ethical approvals; at project mid-point; before archiving and final outputs; ad hoc for significant changes. Updates are logged with version numbers, dates, and a description of changes.

## Annex 1: Data inventory

The data inventory lists all research data records the project collects or generates. Each record represents a coherent data collection activity, not an individual file. For the standalone guide and full template, see [Build a data inventory](data-inventory.md).

For each data record, describe:

- **Name and description:** what this data is and where it comes from.
- **Collection method:** how the data is collected or generated.
- **Participant group:** which participant group(s) this relates to, if applicable.
- **Formats and estimated volume:** expected file formats and approximate size or number of records.
- **Artefacts:** concrete data objects produced (audio recordings, transcripts, anonymised datasets, coded datasets, field notes).
- **Data flow:** how data moves from collection through processing to end state.
- **Personal data categories:** what personal data is involved, if any.
- **Sensitivity level:** Green / Yellow / Red / Black classification.
- **Responsible party:** who collects, stores, and manages this data.
