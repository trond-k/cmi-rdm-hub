---
icon: lucide/clipboard-list
title: "The data inventory"
description: "A running register of every dataset in your project: what it is, where it lives, who is responsible, and how sensitive it is."
tags:
  - Frame
  - Plan
  - Data inventory
  - DMP
notes: ""
date_updated: 2026-04-04
---

# The data inventory

*A data inventory is a running register of every dataset your project creates or acquires. It records what each dataset contains, where it is stored, who is responsible for it, how sensitive it is, and what will happen to it when the project ends. Start it early, keep it current, and it becomes the single document that holds your entire data landscape together.*

## What a data inventory does

A DMP describes your intentions: how you plan to handle data across the project lifecycle. The data inventory is its factual counterpart. It records what actually exists. The two documents work in tandem: the DMP sets the framework, and the inventory tracks reality against it.

Without an inventory, common problems accumulate quietly. Datasets are collected but not documented. Files sit on personal laptops with no backup record. A team member leaves, and nobody knows which survey versions they used or where the consent forms are stored. Sensitive data ends up in locations that were never assessed for security. By the time you need to deposit, publish, or delete data, reconstructing what you have and where it is becomes a project in itself.

The inventory prevents this by making the data landscape visible from the start and keeping it visible throughout.

## What to record

A useful inventory does not need to be elaborate, but it does need to be specific. For each dataset, record at minimum:

| Field | What it captures |
|---|---|
| Dataset name | A short, recognisable label (e.g., 'Household survey, Kumasi') |
| Description | What the dataset contains and how it was produced |
| Research question or work package | Which part of the project this dataset serves |
| Data type and format | Quantitative, qualitative, geospatial, audiovisual; file formats used |
| Source | Primary collection, secondary acquisition, administrative records, etc. |
| Sensitivity classification | Personal data, special category data, politically sensitive, non-sensitive |
| Storage location | Where the authoritative copy lives (e.g., SharePoint, encrypted cloud service, local drive) |
| Backup location | Where backups are held and how often they are updated |
| Responsible person | Who manages this dataset day to day |
| Access restrictions | Who can access it and under what conditions |
| Retention plan | How long the data will be kept and what happens afterwards |
| Status | Current state of the dataset: Planned, Collecting, Processing, Complete, Archived, or Deleted |
| Persistent identifier | DOI or other identifier, once assigned |

You may need additional fields depending on your project. Multi-site studies benefit from a site or country column. Projects working with personal data should record the lawful basis for processing under the GDPR and whether a DPIA has been completed. Longitudinal projects may need to track collection waves.

!!! tip "Keep the format simple"
    A spreadsheet works well for most projects. If you are managing a large or complex portfolio, a structured database may be more appropriate. The format matters less than the discipline of keeping it up to date.

## How the inventory evolves

The data inventory is not a document you write once. It develops alongside the project, becoming more detailed and more authoritative as you move through the research lifecycle.

### Before data collection

At the concept stage, the inventory is a sketch: a preliminary list of the datasets you expect to create or acquire, based on your research questions and methods. It does not need to be precise. Its purpose is to make you think concretely about what data the project will involve, what sensitivities are likely, and whether your plans are feasible.

When you write the funding application, the inventory becomes more structured. Map each anticipated dataset to a research question or work package. Identify likely formats, estimate volumes, and flag sensitivity concerns. This version supports both the data management strategy and the ethics strategy in your proposal, and it helps you cost RDM activities realistically.

By the time you write your DMP, the inventory should be a formal, structured document. Specify metadata standards, file formats, sensitivity classifications, storage locations, and responsibility assignments for each dataset. The inventory is now a key component of the DMP, not a separate exercise.

### During data collection and analysis

Once fieldwork begins, the inventory shifts from planned to actual. Update it as datasets are created: record collection dates, actual formats and volumes, source details, and any deviations from what was planned. If a new dataset emerges that was not anticipated (as often happens in qualitative and mixed-methods research), add it.

The inventory should be reviewed at the same milestones you use to review the DMP: after major collection phases, after processing, and at reporting deadlines. Ask whether the inventory still reflects what you have. Have storage arrangements changed? Has someone new taken over responsibility for a dataset? Has a sensitivity classification shifted because of new information?

!!! warning "Do not let the inventory go stale"
    An outdated inventory is worse than no inventory at all, because it creates false confidence. If the document says a dataset is on SharePoint but it has since been moved to a secure storage environment, anyone relying on the inventory will look in the wrong place. Schedule regular reviews rather than treating the inventory as a one-off task.

### When to update and how long it takes

The inventory does not need continuous attention. Update it at key milestones, not every time a file changes.

| Milestone | What to do | Typical time |
|-----------|-----------|--------------|
| **Project initiation** | Create entries for anticipated datasets; set status to Planned | ~30 minutes |
| **Data collection start** | Update status to Collecting; confirm storage locations; link documentation (information letters, consent forms, Sikt reference) | ~15 minutes |
| **Mid-project review** | Verify entries; add any new datasets; update statuses and classifications | ~15 minutes |
| **Data collection complete** | Update status to Processing or Complete; verify all documentation is linked | ~15 minutes |
| **Project closure** | Finalise status for all datasets; confirm retention or deletion decisions; see [project closure](project-closure.md) | ~30 minutes |

The initial setup takes the most time. After that, milestone updates are brief because you are confirming and adjusting, not starting from scratch. The inventory tracks categories of data (e.g. "interview transcripts from local officials"), not individual files, so the scope remains manageable regardless of how much data the project generates.

### After the project

When you publish or deposit data, update the inventory with persistent identifiers (DOIs), access conditions, embargo timelines, and the repository where each dataset has been deposited. When data is destroyed at the end of its retention period, record the date and method of destruction.

At this point, the inventory becomes the authoritative record of the project's entire data lifecycle: what was collected, how it was processed, where it was stored, what was published, what was preserved, and what was deleted. For CMI, where projects span sensitive contexts and multiple jurisdictions, this record is not just good practice; it is essential for demonstrating compliance with the GDPR, funder mandates, and ethical commitments to participants.

## Connecting the inventory to other documents

The data inventory does not replace other project documentation. It complements it:

- The **DMP** describes policies and procedures; the inventory records the datasets those policies apply to.
- The **README** in your project folder describes the naming convention and folder structure; the inventory records what is in those folders and why.
- **Participant information sheets** document what participants were told about the research and how their data would be used; the inventory records which datasets are covered by which information arrangements.
- **Data processing agreements** specify the legal terms of data handling with third parties; the inventory records which datasets are subject to those agreements.

If these documents contradict each other, something has gone wrong. The inventory is often the quickest way to spot the discrepancy.

??? example "A data inventory in practice: multi-method fieldwork"
    A CMI project studying local governance in three East African countries might begin with an inventory listing four planned datasets: a household survey, key informant interviews, focus group discussions, and administrative records obtained from municipal authorities. By mid-project, the inventory has grown to include a fifth dataset (GPS coordinates of service delivery points, added after the first field visit revealed their relevance) and records that two of the original datasets required revised sensitivity classifications after a political crisis in one of the study countries. At project close, the inventory shows that the survey data was deposited in the Sikt Research Data Archive with a DOI and open access, the interview transcripts were deposited with restricted access and a five-year embargo, the GPS data was withheld entirely due to re-identification risk, and the administrative records were returned to the municipal authorities under the terms of the data sharing agreement.

??? example "A data inventory in practice: document-based research"
    Not all projects generate primary data through fieldwork. A commissioned policy review analysing climate adaptation legislation across ten countries might work entirely with published laws, government reports, and grey literature. An inventory is still useful. It records which documents were collected, from which sources, in which languages, and how they were selected. It tracks where the collection is stored, who compiled it, and whether any documents were obtained under access restrictions or confidentiality agreements. If the analytical outputs (a comparative coding framework, an annotated bibliography, a summary matrix) are to be deposited or shared with the commissioning body, the inventory records what was delivered and under what terms. Even when the underlying materials are publicly available, the curated collection and the analytical layer built on top of it are project outputs worth documenting.

!!! info "See also"
    Use the [Data classification](data-classification.md) scheme to fill the sensitivity classification field for each dataset, and pair the inventory with [Project closure](project-closure.md) when you wind the project down.

## Start now

If your project is already under way and you do not yet have a data inventory, start one today. Retrofitting is less convenient than building from scratch, but the alternative, continuing without a clear record of what you have, is riskier. List what you know, flag what you are unsure about, and fill in the gaps as you go. A partial inventory that you maintain is more valuable than a perfect template that nobody updates.