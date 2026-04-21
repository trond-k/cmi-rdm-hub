---
icon: lucide/layers
title: "The elements of research data management"
description: "A four-layer framework for understanding how external constraints, institutional structures, temporal stages, and implementation choices interact in research data management."
tags:
  - Governance
  - Lifecycle
  - Framework
  - Getting started
notes: "Conceptual companion to the lifecycle model. Consider adding to Foundations nav section."
date_updated: 2026-03-27
---

# The elements of research data management

*Research data management involves decisions at many levels simultaneously: funder mandates shape what you can do, institutional policies shape how you do it, the stage of your project determines when things happen, and the tools and people available determine what is practical. This page maps those elements into a four-layer framework that makes the dependencies visible. It is not a replacement for the [lifecycle model](research-data-lifecycle.md) but a complementary lens, useful when you need to understand why a particular decision is constrained or why changing one thing forces changes elsewhere.*

## Why a framework helps

It is tempting to treat data management as a checklist: write a Data Management Plan (DMP), choose a storage solution, deposit the data. But checklists do not capture the fact that your choice of storage depends on jurisdiction, your jurisdiction depends on where your partners are, and your partners' expectations depend on institutional norms you may not share. A framework that shows these layers and their relationships helps you:

- **Spot constraints early.** If you know that cross-border data transfers require a legal basis under the General Data Protection Regulation (GDPR), you can address this at the planning stage rather than discovering it when you try to move files between Oslo and Nairobi.
- **Trace problems to their source.** When something goes wrong (a tool does not meet security requirements, a consent process does not cover future reuse), the framework helps you identify which layer the problem originates in and what else it affects.
- **Communicate across roles.** A principal investigator, a data manager, and an IT administrator think about data management from different starting points. The framework provides shared vocabulary for aligning their perspectives.

## Four layers

The framework organises the elements of research data management into four layers, from broad external factors to specific implementation choices. Each layer constrains the ones below it, but implementation realities also feed back upward, revealing gaps or conflicts that require adjustment.

### Context: external constraints and enablers

These elements are largely outside your direct control but shape every subsequent decision.

| Element | What it covers | CMI examples |
|---|---|---|
| **Policy** | Funder mandates, national guidelines, disciplinary norms, professional codes of conduct | Horizon Europe open science requirements, Research Council of Norway data sharing mandates, CARE Principles for work with indigenous communities |
| **Jurisdiction** | Legal and regulatory environment determined by geography and institutional affiliation | GDPR as baseline for all CMI projects; Norwegian Personal Data Act; varying data protection regimes in partner countries across Africa, Asia, and Latin America |
| **Resources** | Budget, time, personnel, and infrastructure capacity | Project funding envelopes, CMI's [Microsoft 365 E5 environment](lifecycle-5-store.md), availability of data management support |

Policy and jurisdiction interact constantly. A funder may require open data, but the jurisdictions in which you work may restrict cross-border transfers of personal data. CMI researchers routinely navigate this tension, particularly in multi-country projects where [regulatory fragmentation](cmi-institutional-context.md) means no single legal framework governs the entire dataset.

!!! tip "Clarify jurisdiction before choosing tools"
    For projects involving data collection in multiple countries, establishing the applicable legal frameworks early prevents costly surprises. A survey platform that stores data on US servers may not be acceptable for data subject to the GDPR. See [Store](lifecycle-5-store.md) for guidance on storage choices and [Plan](lifecycle-3-plan.md) for how to address this in your DMP.

### Institution: internal frameworks and relationships

This layer bridges external requirements and your day-to-day work. It is where your organisation interprets and operationalises the constraints from above.

| Element | What it covers | CMI examples |
|---|---|---|
| **Institutional policies** | Internal guidelines, ethics requirements, IT security standards, data sharing mandates | CMI's data management standards, ethics review procedures, IT security requirements for SharePoint and Teams |
| **Stakeholder engagement** | Relationships with participants, communities, partner organisations, and collaborators | Participant information processes, community partnerships, data sharing agreements with Global South institutions, collaborative governance of sensitive datasets |

Stakeholder engagement is not a one-off activity at the start of a project. Relationships with participants and communities shape what data can be collected, how it can be shared, and who retains governance rights over it. For CMI, where research often depends on trust built over years in politically sensitive settings, these relationships are not peripheral to data management; they are [central to it](cmi-institutional-context.md#partnership-dynamics-and-power).

!!! warning "Do not conflate stakeholder engagement with consent forms"
    A signed form does not constitute meaningful engagement. In conflict-affected or authoritarian contexts, participants may sign under duress, may not fully understand future data uses, or may face risks from the very act of participating. Genuine engagement means ongoing communication, community involvement in governance decisions, and willingness to restrict or withdraw data when circumstances change.

### Process: when things happen and what you do

This layer maps onto the [research data lifecycle](research-data-lifecycle.md) and captures the temporal dimension of data management.

| Element | What it covers | How it connects |
|---|---|---|
| **Temporal stage** | The phase of the research lifecycle: before, during, or after the project | Each stage has distinct priorities. Planning-stage decisions become commitments; active-phase decisions are operational; post-project decisions concern preservation and access. See the [lifecycle overview](research-data-lifecycle.md) for the full twelve-stage model. |
| **Action** | Specific activities that create, transform, move, or govern data | Data collection, cleaning, pseudonymisation, analysis, backup, metadata creation, archiving. Each action has requirements that depend on decisions in the layers above and resources in the layer below. |

The lifecycle model is the practical expression of this layer. The framework adds analytical value by making explicit that every action at every stage is constrained by context and institution, and enabled (or limited) by implementation resources.

### Implementation: who does what, with what, to what

This is where plans become operational. The choices here are the most visible, but they are shaped by everything above.

| Element | What it covers | CMI examples |
|---|---|---|
| **Role** | Functions and responsibilities assigned to people and teams | Principal investigator (PI) (overall accountability), field researchers (data collection), data manager (processing and curation), IT support (infrastructure and security), [CMI's data protection contact](lifecycle-3-plan.md) (GDPR guidance) |
| **Tool** | Software, hardware, methodological standards, and protocols | [KoBoToolbox and Open Data Kit (ODK)](lifecycle-4-collect.md) for mobile collection, SharePoint for project storage, [Sikt Research Data Archive](lifecycle-8-publish.md) for long-term deposit, Git for version control of code |
| **Data** | The information assets themselves, characterised by type, sensitivity, format, and lifecycle requirements | Quantitative datasets, qualitative transcripts, fieldwork materials, geospatial data, policy documents. See [CMI's data landscape](cmi-institutional-context.md#a-diverse-data-landscape) for the full picture. |

Role clarity matters more than most teams expect. Data management fails most often not because of technical problems but because nobody was clearly responsible for a specific task. The [Plan](lifecycle-3-plan.md) stage addresses this directly.

## How the layers interact

The layers are hierarchical but not one-directional. Context constrains institution, institution constrains process, and process constrains implementation. But influence also flows upward:

- A tool limitation (implementation) may reveal that an institutional policy needs updating.
- A fieldwork reality (process) may show that a funder requirement (context) cannot be met as written, requiring negotiation or a justified exception.
- Sensitivity discovered during data collection (process) may force a reassessment of the access regime you planned (institution) and the legal basis you relied on (context).

These feedback loops are normal, not signs of failure. The framework helps you trace them so that when you change one element, you can identify what else needs to change.

??? example "A multi-country survey: tracing dependencies across layers"
    You are planning a household survey across three countries in East Africa for a Horizon Europe-funded project.

    - **Context.** Horizon Europe requires open data. The GDPR applies because CMI is the data controller. Each country has its own data protection regime, with varying requirements for local ethics approval and data residency.
    - **Institution.** CMI's policies require a DMP and Sikt notification for personal data. Partner institutions in each country have their own ethics review processes and may require data to remain on local servers.
    - **Process.** Data collection happens in the field on tablets; data must be transmitted securely to a central server. Pseudonymisation must occur before cross-border transfer. The data inventory must track which datasets contain personal data and where they are stored.
    - **Implementation.** You select KoBoToolbox for collection (encrypted transmission), SharePoint for working storage, and plan to deposit pseudonymised data in Sikt's archive. The PI is accountable, but each country team has a designated data contact responsible for local compliance.

    The framework makes visible that your tool choice (KoBoToolbox) depends on your jurisdictional constraints (GDPR, local laws), which in turn depend on your funder's requirements (Horizon Europe) and your partners' institutional policies. Changing any one element ripples through the others.

## Using the framework

This is a thinking tool, not a form to fill in. Use it when you need to:

- **Plan a complex project.** Walk through each layer to check whether you have addressed the constraints and dependencies. The framework complements the [data inventory](data-inventory.md) and [DMP](lifecycle-3-plan.md) by providing a structured way to think about what shapes your choices.
- **Diagnose a problem.** If a data management issue arises mid-project, identify which layer the problem sits in. A tool that cannot handle your data volume is an implementation problem. A partner who will not share data may be an institutional or context problem. The solution depends on the layer.
- **Communicate with your team.** The four layers provide shared vocabulary for conversations that otherwise get tangled between technical, legal, ethical, and practical concerns.

The framework does not replace the lifecycle model. The lifecycle tells you *when* to do things; this framework helps you understand *why* certain choices are constrained and *where* the dependencies lie. Together, they give you a map for navigating data management decisions from concept to long-term preservation.

A complementary lens looks inward rather than outward: not the constraints on data management, but the [documentation layers around the data itself](foundations-of-documentation.md). Where this framework maps context, institution, process, and implementation, the documentation-layer model maps what must be maintained around the data to make it understandable, accountable, and reusable over time.

!!! info "Last reviewed"
    This page was last reviewed on 27 March 2026. For rapidly changing
    topics, verify against the latest source.
