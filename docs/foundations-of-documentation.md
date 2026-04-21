---
icon: lucide/layers-3
title: "The documentation layers around research data"
description: "Research data is more than files. It is embedded in a documentation ecology that includes metadata, analytic definitions, methodological records, governance documents, and project-level stewardship records."
tags:
  - Documentation
  - Metadata
  - Data management
  - Governance
notes: ""
date_updated: 2026-04-07
---

# The documentation layers around research data

*Research data is never self-explanatory. Around every dataset sits a wider documentation ecology that makes the material understandable, accountable, and reusable. This page maps those layers and explains why each matters. It complements the [four-layer framework](elements-of.md) (which maps the constraints on data management) by mapping what must be maintained around the data itself.*

## Research data is more than files

A dataset without its documentation ecology is noise. A CSV with columns labelled V1 through V47 and values ranging from 1 to 5 tells no one anything, not even the original researcher returning after two years. The SCORE programme found that data availability was the single strongest predictor of reproducibility, but availability without documentation is not enough.[^1] Of the papers that did share data, only 54% were precisely reproducible. The gap between "shared" and "usable" is filled by documentation.

This is not only about metadata. Research data is embedded in a wider set of documents that together make it interpretable, legally usable, and methodologically intelligible. These documents answer different questions about the same material, and each is maintained by different people at different stages of the project.

## Six documentation layers

Each layer around a dataset answers a distinct question. Together they form the documentation ecology that makes research data meaningful.

| Layer | Main question | Typical contents |
|---|---|---|
| **Data** | What has been recorded? | Survey files, transcripts, fieldnotes, images, code, derived datasets |
| **Descriptive metadata** | What is this material? | Variable labels, file formats, dates, versions, provenance, creators |
| **Analytic documentation** | What does it mean in the analysis? | Codebooks, category definitions, derived variables, harmonisation rules, coding frameworks |
| **Methodological documentation** | How was it produced and transformed? | Protocols, instruments, sampling notes, cleaning decisions, fieldwork memos |
| **Governance documentation** | On what basis may it be used? | Consent forms, information letters, ethics approvals, legal basis, access restrictions |
| **Project-context documentation** | Why does it exist and who is responsible? | DMP, contracts, roles, funder terms, retention plans, archiving strategy |

### Descriptive metadata

Descriptive metadata is "the label on the jar." It identifies the dataset, makes it findable, and provides the structural information needed for management: what the variables are called, what format the files use, when they were created, who produced them, and where they came from. Most repository deposit forms and metadata standards (Dublin Core, DataCite, DDI) operate at this level.

Metadata is necessary but not sufficient. It tells you what exists without telling you what it means, how it was produced, or whether you are allowed to use it.

### Analytic documentation

This is the layer closest to the "semantic layer" concept from data analytics, adapted for research. It defines what variables, codes, categories, and cases mean within the research design. A codebook that specifies "household economic insecurity = score 4 or 5 on variable q2, excluding incomplete responses" is analytic documentation. So is a coding frame that defines what counts as "institutional mistrust" in a qualitative analysis, or a harmonisation table that maps education categories across countries into a common variable.

Without this layer, data can be read but not interpreted. Two researchers looking at the same file may construct different meanings from it.

### Methodological documentation

This layer explains how data came into being and how it was transformed. Protocols, interview guides, transcription conventions, sampling rationale, data cleaning decisions, and processing logs all sit here. Without it, the data can be misread because the reader does not know what shaped it.

For example: a survey dataset may show that 30% of respondents answered "don't know" on a sensitive question. Without a fieldwork memo explaining that the question was administered differently after the first two weeks due to interviewer feedback, that pattern is uninterpretable.

### Governance documentation

This layer defines the conditions under which data may be collected, processed, stored, linked, shared, and reused. It includes information letters, consent forms, ethics committee approvals, legal basis assessments, Data Protection Impact Assessments, data sharing agreements, and access restrictions.

Governance documentation is not metadata in the usual sense, but it is essential to whether data can be shared, reused, or even retained. A consent form that limits use to "the current study" determines the dataset's entire downstream trajectory. An ethics approval that requires deletion after five years shapes the preservation plan.

### Project-context documentation

This layer connects data to the broader research process: why the dataset was collected, for which project, under whose responsibility, with what funder obligations, and according to what lifecycle plan. It includes proposals, DMPs, contracts, collaboration agreements, role assignments, and retention decisions.

This layer is often the first to decay. When a project ends and the team disperses, the institutional memory of why certain decisions were made walks out the door. The DMP and data inventory are the primary tools for preserving this context.

## Why each layer matters

Different layers decay at different rates. Descriptive metadata, once written into a repository record, is relatively stable. Analytic documentation (codebooks, coding frames) survives if it is stored alongside the data. But methodological documentation often lives in fieldwork memos that never leave a project folder, and governance documentation may sit in email inboxes or filing cabinets rather than being linked to the datasets it governs.

Three insights from this model:

1. **Metadata is necessary but not sufficient.** A dataset with complete repository metadata but no codebook is findable but not interpretable. A dataset with a codebook but no record of its consent conditions is interpretable but not legally reusable.
2. **Governance documentation shapes reuse as much as analytic documentation does.** What you may do with a dataset depends on information letters and ethics approvals, not only on variable definitions.
3. **The layers are maintained by different people.** Researchers create analytic and methodological documentation. Legal and ethics staff create governance documentation. Data managers maintain metadata and inventories. Good stewardship requires coordination across these roles.

## Four documentation families

For practical planning, the six layers can be grouped into four families that map onto different responsibilities and workflows.

| Family | Purpose | Includes |
|---|---|---|
| **Data description** | Identify and describe | Metadata, inventories, variable lists, provenance |
| **Analytic interpretation** | Explain meaning in use | Codebooks, variable construction, harmonisation, coding frames |
| **Research production** | Explain how data came into being | Protocols, instruments, processing notes, fieldwork memos |
| **Governance and stewardship** | Explain conditions of use and responsibility | Consent, ethics, legal basis, DMP, contracts, access rules, retention |

This grouping is useful for planning because each family has a different owner, timeline, and risk profile. Data description is largely handled at deposit time. Analytic interpretation should be built during processing but often is not. Research production documentation is best maintained in real time during fieldwork. Governance documentation must be in place before data collection begins.

## What this means for your project

Each documentation layer maps onto decisions at specific lifecycle stages.

- **At [FRAME](lifecycle-1-frame.md):** identify the documentation your project will need. Interviews imply information letters, consent procedures, and interview guides. Surveys imply codebooks and instrument versions. Administrative data implies access agreements and provenance records.
- **At [PLAN](lifecycle-3-plan.md):** assign documentation responsibilities in the DMP. Decide who maintains the codebook, who drafts information letters, who keeps the data inventory current.
- **At [COLLECT](lifecycle-4-collect.md):** produce and maintain methodological and governance documentation in parallel with data collection. Do not defer these to "after fieldwork."
- **At [PROCESS](lifecycle-6-process.md):** create codebooks and data dictionaries during processing, not after. Document every transformation in a processing log.
- **At [PUBLISH](lifecycle-8-publish.md):** write a README while details are fresh. Complete repository metadata thoroughly.
- **At [PRESERVE](lifecycle-9-preserve.md):** ensure all documentation layers survive format migration and platform changes. A dataset that outlives its documentation becomes unusable.

!!! tip "The data inventory as documentation map"
    The [data inventory](data-inventory.md) is the practical place where these layers come together. For each dataset, the inventory should record not only what the data is and where it lives, but also what documentation exists around it: which codebook applies, which consent arrangement covers it, which agreement governs access, and whether a README has been written.

!!! tip "Companion reading"
    This page presents the conceptual model. For practical guidance on creating metadata, see the hub's lifecycle pages on [PROCESS](lifecycle-6-process.md) (codebooks and data dictionaries), [PUBLISH](lifecycle-8-publish.md) (README files and repository deposits), and [DISCOVER](lifecycle-10-discover.md) (rich metadata for findability). For evidence on why documentation matters for reproducibility, see [What the largest replication study means for your research](CROSS-replication-evidence.md).

[^1]: Tyner, A. H., Abatayo, A. L., Daley, M. et al. (2026). 'Investigating the replicability of the social and behavioural sciences'. *Nature*, 652, 143-150. The reproducibility study within SCORE found that only 54% of 143 papers with shared data were precisely reproducible.

!!! info "Last reviewed"
    This page was last reviewed on 7 April 2026.
