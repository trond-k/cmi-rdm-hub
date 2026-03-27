---
icon: lucide/file-text
title: "PLAN"
description: "Formalise how your project will handle data: who is responsible, what legal frameworks apply, and how the DMP will evolve."
tags:
  - Plan
  - DMP
  - Data inventory
  - GDPR
  - Ethics
  - Preregistration
notes: ""
date_updated: 2026-03-26
---

# PLAN: data management planning

*The Data Management Plan is where intentions become commitments. It formalises how data will be handled, who is responsible, what legal and ethical frameworks apply, and what agreements govern collaboration. Treat it as a living document that evolves with the project, not a form you fill in once to satisfy a funder.*

## The DMP as a working document

A Data Management Plan (DMP) serves two purposes that are easy to confuse. The first is external: funders require one, and it forms part of your contractual obligations. The second is internal: it is the document your team actually uses to coordinate data handling across the life of the project. These two purposes sometimes pull in different directions. Funder templates tend to be generic and front-loaded, asking you to describe things you cannot yet know in detail. The operational DMP needs to be specific, revisable, and grounded in what is actually happening.

The pragmatic solution is to maintain both. Write the funder-facing DMP to meet the requirements of the call (Horizon Europe, the Research Council of Norway, Norad, or whoever is funding the work). Then use it as the skeleton for an internal version that your team keeps current. The internal version can be more detailed, more honest about uncertainties, and more tightly linked to your [data inventory](data-inventory.md), which by this stage should be a formal, structured companion document.

!!! tip "Start from the CMI DMP template"
    CMI provides a default DMP template that covers all the topics required by major funders (the Research Council of Norway, Horizon Europe, Science Europe) through a similar but differently arranged structure. It integrates the [data inventory](data-inventory.md) as a component of the plan rather than treating it as a separate document. Use it as your starting point; if a funder requires a specific format, the CMI template maps onto it without loss. External DMP tools can help with structured drafting and version management: [Sikt DMP](https://sikt.no/en/data-management-plan), [DMPonline](https://dmponline.dcc.ac.uk/), and [DMPTool](https://dmptool.org/).

## What the DMP should cover

The specific headings vary by funder, but the core topics are consistent. Your DMP should address:

- **What data you will collect or acquire**, including types, formats, and estimated volumes. This draws directly on the work you did at the [FRAME](lifecycle-1-frame.md) stage and is detailed in the data inventory.
- **How data will be documented**, including metadata standards, codebooks, README files, and naming conventions. See [Name files and structure folders](file-and-folder-naming.md) for the practical side of this.
- **Where data will be stored** during the project, including backup arrangements and security measures.
- **Who is responsible** for each aspect of data management (see below).
- **How sensitive data will be handled**, including pseudonymisation, access controls, and any Data Protection Impact Assessments required.
- **What legal and ethical frameworks apply**, including GDPR compliance, ethics reviews, and participant information requirements.
- **How data will be shared and preserved** after the project, including repository choice, access conditions, licensing, and retention periods.

Not every section needs the same level of detail at the outset. Storage and security arrangements should be specific from the start. Preservation and sharing plans can be outlined in principle and refined as the project develops, provided you revisit them before the project ends.

## Assign roles and responsibilities

Data management fails most often not because of technical problems but because nobody was clearly responsible. The DMP should name who is accountable for each area:

| Role | Typical responsibilities |
|---|---|
| Principal investigator | Overall accountability for data management commitments; final decisions on access and sharing |
| Data manager or coordinator | Day-to-day oversight of storage, documentation, and inventory maintenance |
| IT or information security | Infrastructure, backup verification, access controls, incident response |
| Ethics or data protection officer | GDPR compliance, ethics applications, DPIA coordination |
| Collaborators and field teams | Following agreed protocols for collection, naming, and transfer |
| Students and research assistants | Adhering to project conventions; flagging uncertainties early |

Not every project has a dedicated data manager. In smaller projects, the PI may cover several of these roles. The point is not to create a bureaucracy but to ensure that for every task (backing up data, updating the inventory, handling an access request) there is a named person who knows it is theirs.

!!! warning "Departures and handovers"
    People leave projects. A postdoc finishes their contract; a field coordinator moves to another organisation. If data responsibilities are not documented and handed over, institutional memory walks out the door. The DMP should include a brief note on how handovers will be managed, and the [data inventory](data-inventory.md) should be kept current enough that a successor can pick it up without starting from scratch.

## Legal and ethics planning

By this stage, you need to move from the general awareness of the [FRAME](lifecycle-1-frame.md) stage to concrete planning.

### GDPR and data protection

If your project processes personal data (and most CMI projects do), you need to identify the lawful basis for processing, determine whether a notification to Sikt is required, and assess whether the nature and scale of processing triggers a Data Protection Impact Assessment (DPIA). International data transfers, particularly from the EU/EEA to countries without an adequacy decision, require additional legal mechanisms.

These are not boxes to tick after the fact. They shape how you design participant information, structure storage, and negotiate collaboration agreements. Get advice from CMI's data protection contact early. For detailed guidance, see [GDPR and legal compliance](CROSS-gdpr-and-legal-compliance.md).

### Ethics review

Your project may be subject to review by several bodies with different roles. [Sikt](https://sikt.no/en) assesses projects involving personal data and provides guidance on data protection compliance; it is a review and advisory body, not an approver. The Regional Committees for Medical and Health Research Ethics (REK) review health-related research and do grant formal approval. CMI's own Research Ethics Committee serves as a reviewer and discussion partner; it does not function as an institutional review board, but can provide an approval statement where a funder or partner institution requires one.

For multi-site and multi-jurisdictional projects, equivalent bodies in partner countries may also need to review the work, and their requirements can be inconsistent with Norwegian or European frameworks. Build time into your timeline for this; review processes are rarely fast, and revisions are common.

### Participant information

Draft your participant information sheets as part of the planning stage, not at the last minute before fieldwork. They should be written in clear, accessible language (not legalese), translated where needed, and tailored to the context. In settings where written documentation is inappropriate or unsafe, plan for alternative approaches (oral information, community-level briefings) and document the justification.

## Collaboration agreements

Multi-partner projects need formal agreements on data governance before data collection begins. Depending on the project, these may include:

- **Consortium or partnership agreements** covering data ownership, intellectual property, publication rights, and responsibilities for data management across partners.
- **Data sharing agreements** specifying what data will be shared between partners, under what conditions, and with what safeguards.
- **GDPR data processing agreements** where one partner processes personal data on behalf of another (controller–processor relationships).

These agreements are where the principles discussed in [CMI's institutional context](cmi-institutional-context.md) become operational. If your project involves partners in the Global South, questions of equitable data governance, shared custodianship, and community authority over data are not afterthoughts; they belong in the agreement from the start.

## Preregistration

If your project lends itself to preregistration, the planning stage is the time to do it: after the design is firm but before data collection begins. Preregistration is well established in quantitative and experimental research, and emerging as a practice in qualitative work. For a fuller discussion, including what to register, where, and how preregistration fits into the broader landscape of reproducibility and transparency, see [Reproducibility and transparency](reproducibility-and-transparency.md).

## Keep the plan alive

A DMP written in month one and never revisited is a compliance artefact, not a management tool. Schedule reviews at key milestones: after the main data collection phase, after processing, at annual or mid-term reporting deadlines, and before deposit or publication. At each review, check:

- Does the DMP still describe what the project is actually doing with data?
- Have new datasets, storage arrangements, or sensitivities emerged?
- Are roles and responsibilities still accurate?
- Has anything changed that affects legal compliance or ethics commitments?

Update the DMP and the [data inventory](data-inventory.md) together; they should always tell a consistent story. If you are using a versioned document, record what changed and when. If the funder requires an updated DMP at reporting milestones (as Horizon Europe does), the internal reviews feed directly into those submissions.

## Formalise the data inventory

By the end of this stage, the [data inventory](data-inventory.md) should be a structured, formal document, not the preliminary sketch from the FRAME stage. It should specify, for each anticipated dataset: metadata standards, file formats, sensitivity classifications, storage locations, backup arrangements, responsible persons, and access conditions. The inventory is now a core component of the DMP, and the two documents should cross-reference each other.