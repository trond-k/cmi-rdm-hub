---
icon: lucide/clipboard-list
title: "The data inventory"
description: "Why a data inventory belongs at the centre of your project, and how to build one."
tags:
  - Data inventory
  - DMP
  - Planning
notes: ""
date_updated: 2026-03-25
---

# The data inventory

*Every research project generates more data than its creators expect. A data inventory is a structured register of the research data your project collects, reuses, and produces. It is the document that every other data management decision refers back to: what you store, how you classify it, who can access it, and where it ends up. Building one early, and keeping it current, is the single most useful thing you can do for your project's data management.*

## What is a data inventory?

A data inventory is a systematic list of your project's research data, organised as a set of **data records**. Each record represents a coherent data collection activity or analytical output, not an individual file. A record called 'village leader interviews' would cover the full set of recordings, transcripts, and coded outputs from that interview series. A record called 'household baseline survey' would cover the questionnaire instrument, the raw response data, and the cleaned dataset.

The inventory is a living document. You draft it during project planning, refine it as fieldwork begins, and update it when new data emerges or plans change. By the end of the project it serves as a definitive account of what data you collected, what happened to it, and where it is now.

The inventory covers **primary research data** (data you collect or generate) and **secondary research data** (existing datasets you reuse or analyse).

## Why the inventory matters

### It anchors your Data Management Plan

The Data Management Plan (DMP) is the document that funders, ethics boards, and your own team rely on to understand how data will be handled. The inventory is its structural core. Your sensitivity classifications, storage decisions, sharing pathways, FAIR (Findable, Accessible, Interoperable, Reusable) operationalisation, and retention plans all refer back to specific data records. Without the inventory, these sections become vague generalisations that are difficult to act on or verify.

At CMI, the data inventory forms Section 3 of the institutional DMP template, and the executive summary table at the front of the DMP is generated directly from it. If the inventory is solid, the rest of the DMP largely writes itself.

### It catches what you overlook

Researchers naturally focus on their primary data collections: the interviews they will conduct, the surveys they will administer, the fieldwork they will carry out. The inventory forces you to also account for less obvious research data:

- **Secondary datasets** you plan to reuse or re-analyse (anonymised transcripts from a prior project, public survey data, policy document corpora)
- **Derived outputs** that constitute research data in their own right (coded qualitative datasets, statistical models, geo-referenced incident databases)
- **Data from supporting methods** that may not feel like 'real data' but still need managing (ethnographic field diaries, audio recordings made during participant observation, photographs of fieldwork contexts)

If it was collected or generated for the purposes of your research, it belongs in the inventory.

### It connects data to decisions

Different datasets within the same project often need different treatment. Interview recordings from a conflict zone require high-security storage and restricted access. A publicly available policy document corpus can be shared openly. A household survey dataset sits somewhere in between.

When each data record carries its own sensitivity tier, storage location, and sharing pathway, you avoid two common pitfalls: applying your most restrictive policy to everything (which makes open data unnecessarily difficult) or applying your most permissive policy to everything (which puts participants at risk). The inventory makes these per-dataset decisions visible and auditable.

### It supports accountability over time

A versioned data inventory is an audit trail. When a funder asks what data your project holds, or when a data protection authority queries your processing activities, or when a future researcher wants to understand what was collected and why, the inventory provides the answer. This is especially valuable for long-running projects and for the post-project period when team members move on and institutional memory fades.

## What goes into a data record

Each record in the inventory describes a single data collection or analytical output using six fields. The aim is to be specific enough to make real decisions, but concise enough that the inventory remains usable. Target roughly 15–20 lines per record.

### Description and method

What this data is and how it is collected or generated. One to two sentences.

> *Semi-structured interviews with savings group leaders and community health workers in three Zambian provinces, exploring implementation experiences and barriers to programme adoption.*

> *Digitised archival documents on regional Islamic movements and conflict history in Cabo Delgado, Mozambique, collected from provincial archives and private collections.*

### Formats and estimated volume

File formats and approximate size or count. One line is usually enough.

> *Audio (WAV), transcripts (DOCX), coded dataset ([NVivo](https://lumivero.com/products/nvivo/) .nvp). Approximately 40 interviews, ~120 hours of audio.*

> *CSV and XLSX. Approximately 11,200 household records across baseline and follow-up waves.*

### Data flow

The chain from collection to end state. Use a concise chain format by default:

> *Field recording (WAV) → transcription (DOCX) → anonymised transcript (DOCX) → coded dataset (NVivo) → archived transcript (PDF/A)*

> *Tablet-based data entry ([CSPro](https://www.census.gov/data/software/cspro.html)) → transfer to secure server (CSV) → cleaned dataset ([Stata](https://www.stata.com) .dta) → analysis outputs (Stata .do/.log) → archived dataset (CSV + codebook)*

If the flow has branches or non-obvious steps, expand to a short paragraph.

### Personal data and sensitivity

Three sub-fields, each on its own line:

- **Categories**: direct identifiers, indirect identifiers, special category data, or none
- **Sensitivity tier**: Green (open), Yellow (internal), Red (restricted), or Black (strictly restricted)
- **Key risk**: one sentence identifying the principal risk

> *Categories: indirect identifiers (community role, location, programme participation details)*
> *Sensitivity tier: Yellow*
> *Key risk: combination of role and location could identify individuals in small communities*

### Storage and security

Where the data is stored and who has access. Omit fieldwork measures if not applicable.

- **Storage**: the platform or system (e.g., CMI M365, Services for Sensitive Data (TSD), [Tresorit](https://tresorit.com))
- **Access**: who has access and on what basis
- **Fieldwork measures**: device encryption, upload protocols, local deletion (if applicable)

### Sharing and archiving

How the data will (or will not) be shared after the project, and where it will be preserved.

- **Pathway**: open access, registered access, controlled access, restricted access, or no external sharing
- **Target repository and licence**: e.g., '[Zenodo](https://zenodo.org), CC BY 4.0' or 'Sikt Research Data Archive, Data Documentation Initiative (DDI) metadata'
- **Embargo**: if applicable
- **If restricted**: whether a metadata-only record will be deposited

## How to build your inventory

### Start from your methods

For each research method your project uses, ask: what data does this method produce? An interview study produces recordings, transcripts, and potentially a coded dataset. A survey produces the instrument, raw responses, and a cleaned dataset. Ethnographic fieldwork produces field diaries, photographs, and possibly audio or video recordings. List each distinct output as a candidate data record.

### Account for secondary data

If your project reuses existing datasets, whether from a prior project, a public archive, or a partner institution, these need their own records. Secondary data still requires decisions about storage, access, and any restrictions imposed by the original data holder. Note the source, any licensing or data-sharing agreements that govern your use, and how you will store your working copy.

### Trace the data flow

For each record, map the chain from the point of collection or acquisition to its final resting place. This step often reveals intermediate forms you hadn't considered (a transcription stage, a cleaning step, a format conversion for archiving) and helps you identify where sensitivity changes along the chain. Raw interview audio is highly sensitive; a fully anonymised summary may be open.

### Group similar records

!!! tip "Use a summary table for similar records"
    If your project has six or more data records of a similar type (e.g., interview series with eight different participant groups, or survey waves across multiple sites), you do not need a full entry for each. Use a summary table to describe the set, and provide a full record only for those that differ materially in sensitivity, storage, or sharing pathway.

### Revisit at project milestones

The inventory you draft at the proposal stage will not match reality at the mid-point. New data sources emerge, planned collections are dropped, formats change. Review and update the inventory:

- after ethical approvals are obtained
- when fieldwork begins
- at the project mid-point
- before archiving and final outputs
- whenever a significant change occurs in research design or data handling

## Worked examples

???+ example "Semi-structured interviews in a sensitive context"
    **Description and method:** Semi-structured interviews with fishermen and their families in Lampedusa, exploring experiences of encountering migrant remains at sea. Conducted face-to-face by the principal investigator (PI), who has long-standing relationships with the community.

    **Formats and estimated volume:** Audio (WAV), transcripts (DOCX), coded dataset (NVivo .nvp). Approximately 20 interviews.

    **Data flow:** Field recording (WAV) → transcription and translation (DOCX) → pseudonymised transcript (DOCX) → coded dataset (NVivo) → archived transcript (PDF/A)

    **Personal data and sensitivity:**

    - Categories: direct identifiers (voices, names in recordings), special category data (traumatic experiences, potentially criminalised activities)
    - Sensitivity tier: Red
    - Key risk: small community size and distinctive personal narratives make re-identification possible even after pseudonymisation

    **Storage and security:**

    - Storage: CMI M365 with restricted access; raw audio on encrypted device during fieldwork
    - Access: PI only; supervisor access to pseudonymised transcripts
    - Fieldwork measures: encrypted recording device, upload to secure storage within 24 hours, local deletion after verification

    **Sharing and archiving:**

    - Pathway: restricted access
    - Target repository and licence: metadata-only record in Zenodo; pseudonymised transcripts under permanent embargo at CMI
    - If restricted: metadata-only record deposited with full methodological documentation

??? example "Household survey dataset from a randomised controlled trial"
    **Description and method:** Baseline and follow-up household surveys administered to approximately 11,200 pregnant women across three Zambian provinces, capturing demographics, health-seeking behaviour, birth preparedness, and antenatal care (ANC) card data.

    **Formats and estimated volume:** Raw data (CSPro), cleaned dataset (Stata .dta, CSV). Approximately 22,400 survey records across two waves.

    **Data flow:** Tablet-based data entry (CSPro) → transfer to secure server (CSV) → cleaning and validation (Stata) → de-identified analytical dataset (CSV + Stata .dta) → archived dataset (CSV + codebook)

    **Personal data and sensitivity:**

    - Categories: indirect identifiers (geographic location, household composition, health data)
    - Sensitivity tier: Yellow
    - Key risk: combination of location, household size, and health outcomes could enable re-identification in small communities

    **Storage and security:**

    - Storage: secure server managed by authorised researchers; de-identified dataset on CMI M365
    - Access: research team members with data access authorisation

    **Sharing and archiving:**

    - Pathway: open access (de-identified dataset)
    - Target repository and licence: Zenodo or Sikt Research Data Archive, CC BY 4.0
    - Embargo: 1–2 years after project completion

??? example "Secondary dataset from a prior project"
    **Description and method:** Anonymised interview transcripts from the REMIMO project (Regulating Migration and Membership through Monetary Requirements), reused to augment and triangulate new ethnographic evidence on permanent residence and income-related attachment conditions.

    **Formats and estimated volume:** Anonymised transcripts (DOCX, PDF). Approximately 30 transcripts.

    **Data flow:** Received from REMIMO project (anonymised DOCX) → imported to NVivo for re-coding → coded dataset (NVivo .nvp) → analytical outputs integrated into project findings

    **Personal data and sensitivity:**

    - Categories: none (pre-anonymised by original project)
    - Sensitivity tier: Green
    - Key risk: minimal; data was anonymised before transfer

    **Storage and security:**

    - Storage: CMI M365
    - Access: project research team

    **Sharing and archiving:**

    - Pathway: subject to original data-sharing agreement with REMIMO project; re-coded outputs may be shared as part of new project's analytical documentation
    - Target repository and licence: governed by REMIMO data-sharing agreement
