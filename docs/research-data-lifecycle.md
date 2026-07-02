---
icon: lucide/refresh-cw
title: "The research data lifecycle"
description: "How the twelve-stage lifecycle model works, why it matters, and how to use it as a practical framework for managing research data at CMI."
tags:
  - Lifecycle
  - Getting started
  - Data inventory
notes: ""
date_updated: 2026-07-02
---

# The research data lifecycle

*This hub organises its guidance around a twelve-stage lifecycle, grouped into three phases: before, during, and after the project. The model is a practical framework, not a rigid sequence. You will revisit earlier stages, skip ahead, and find that some decisions only make sense in hindsight. The value is not in following the stages in order but in knowing what questions to ask at each point and how your choices now affect what is possible later.*

## Why a lifecycle model

Research data management is often treated as a set of isolated tasks: write a DMP before the project starts, deposit data in a repository when it ends, fill in the forms in between. This misses the point. Decisions made at every stage shape what is possible at every other stage. The file format you choose during collection determines whether your data can be preserved in ten years. The sensitivity screening you do at the concept stage determines whether you can share the data at all. The metadata you record during fieldwork (interview settings, survey setup, contextual notes) determines whether anyone can fully interpret your results.

A lifecycle model makes these dependencies visible. It does not add work; it surfaces work that would otherwise need to be done reactively, under pressure, and at greater cost.

## Three phases, twelve stages

The lifecycle groups naturally into three phases, each with a distinct character.

### Before the project

You are designing, applying for funding, or setting up. The decisions here are largely about scope, commitment, and anticipation.

| Stage | What you are doing |
|---|---|
| [**Frame**](lifecycle-1-frame.md) | Defining what data you need, checking what already exists, and screening for sensitivity |
| [**Fund**](lifecycle-2-fund.md) | Aligning data plans with funder requirements and budgeting for data management |
| [**Plan**](lifecycle-3-plan.md) | Formalising data handling in a DMP, assigning roles, and addressing legal and ethical requirements |

These three stages set the trajectory. What you promise in a funding application, what you declare in an ethics protocol, and what you sketch in a preliminary [data inventory](data-inventory.md) all become commitments that the rest of the project must honour or explicitly revise.

### During the project

You are actively working with data. The decisions here are operational: quality, security, documentation, and analytical transparency.

| Stage | What you are doing |
|---|---|
| [**Collect**](lifecycle-4-collect.md) | Gathering data through fieldwork, surveys, interviews, or secondary acquisition |
| [**Store**](lifecycle-5-store.md) | Keeping data secure, backed up, and organised during active use |
| [**Process**](lifecycle-6-process.md) | Cleaning, transforming, and pseudonymising raw data into analysis-ready form |
| [**Analyse**](lifecycle-7-analyse.md) | Generating findings and documenting analytical decisions so others can follow your reasoning |

This is where plans meet reality. New datasets emerge that were not anticipated. Sensitivity classifications shift as political contexts change. A tool that worked in a pilot fails at scale. The DMP and data inventory should be living documents, updated as the project evolves, not artefacts frozen at the proposal stage.

### After the project

You are wrapping up, publishing, and ensuring that your data remains usable and findable in the long term.

| Stage | What you are doing |
|---|---|
| [**Publish**](lifecycle-8-publish.md) | Making outputs citable, linking data, code, and publications together |
| [**Preserve**](lifecycle-9-preserve.md) | Depositing data in formats and archives that will remain accessible |
| [**Discover**](lifecycle-10-discover.md) | Applying metadata standards so others can find what you have produced |
| [**Access**](lifecycle-11-access.md) | Defining who can use your data and under what conditions |
| [**Share and Reuse**](lifecycle-12-share-and-reuse.md) | Licensing data and documenting it well enough for responsible reuse |

A recurring principle across these stages is that [trustworthy, certified archives](lifecycle-8-publish.md) handle much of the technical infrastructure by design: persistent identifiers, standardised metadata, access controls, format migration, and long-term storage. Your most important contributions are choosing the right archive and providing rich, accurate documentation.

## Not a straight line

The numbered stages suggest a sequence, but research rarely works that way. A few common patterns:

- **Iteration.** You collect a first round of data, process and analyse it, and then redesign your collection instruments for the next round. Stages 4 through 7 may cycle several times within a single project.
- **Backward dependencies.** When you reach the Publish stage and realise your metadata is thin, you are effectively working back through Discover and Process. When a funder asks for a data availability statement, you may need to revisit Access decisions you have not yet formalised.
- **Parallel work.** Storage, documentation, and sensitivity management run continuously alongside collection and analysis. They are not separate phases waiting for their turn.
- **Late-emerging sensitivity.** A dataset that seemed low-risk at the Frame stage may become sensitive if a political crisis erupts, a participant is identified through contextual detail, or a partner withdraws consent for sharing. The lifecycle model accommodates this by treating sensitivity as a thread that runs across all stages, not a box to tick once.

The lifecycle is a map, not a conveyor belt. Use it to orient yourself, not to constrain the order in which you work.

## Themes that cut across stages

Some concerns do not belong to any single stage. They surface repeatedly and are better addressed in dedicated pages than scattered across twelve separate discussions:

- **[Reproducibility and transparency](reproducibility-and-transparency.md)** runs from how you document analytical decisions (Stage 7) to how you disclose AI tool use (Stages 4, 6, 7) to what funders and publishers require at the point of dissemination (Stage 8).
- **[File and folder naming](file-and-folder-naming.md)** matters from the moment you create your first file (Stage 4) through to the deposit you prepare years later (Stage 8).
- **[The data inventory](data-inventory.md)** is a living document that begins as a sketch at the concept stage (Stage 1), is formalised in the DMP (Stage 3), populated during collection (Stage 4), and closed out with persistent identifiers at publication (Stage 8) and preservation (Stage 9).

Sensitivity, legal compliance, and AI governance are additional cross-cutting themes addressed within individual stages and, where the topic requires it, in dedicated guidance.

!!! tip "Start with where you are"
    You do not need to read every stage before acting. If your project is already under way, go to the stage that matches your current situation. Each page is self-contained enough to be useful on its own, with links to earlier and later stages where your decisions depend on them.

!!! info "Last reviewed"
    This page was last reviewed on 2 July 2026. The lifecycle model itself is stable; the stage pages it links to are updated more often.
