---
icon: lucide/clipboard-check
title: "Worked example: service access study"
description: "A publishable composite example showing a small starter inventory for a mixed-methods project with different participant groups and survey modules."
tags:
  - data inventory
  - worked example
  - composite example
  - CMI
date_updated: 2026-04-28
---

# Worked example: service access study

This is a fictionalised composite example. It shows how a CMI project might use the starter inventory without turning it into a full metadata system.

The project studies how households experience access to public services in two districts. It uses a household survey and semi-structured interviews. Some parts of the project are low risk. Other parts are more sensitive because they involve exposed participant groups or questions about complaints, informal payments, health, political pressure, or trust in local authorities.

The example has six data objects. That is enough to show the main decisions without listing every file.

## Project sketch

| Field | Entry |
| --- | --- |
| Project type | Mixed-methods study of service access and household wellbeing |
| Methods | Household survey; interviews with service providers; interviews with residents and informal workers |
| Participant groups | Municipal staff, service providers, residents, informal workers |
| Main sensitivity issue | The same method is not equally sensitive for every group or topic |
| Inventory stage | Before data collection |

## Why the inventory is split this way

The project does not create one row called "interview data" and one row called "survey data". That would hide important differences.

The interview data are split by participant group because interviews with municipal staff and service providers have a different risk profile from interviews with residents or informal workers who may describe grievances, informal payments, or fear of consequences.

The survey data are handled in two steps. The raw survey export contains all modules and must be governed according to the most sensitive content it contains. Later, the team creates a separate restricted extract for the sensitive modules, and a de-identified analytical dataset for wider analysis.

## Starter inventory

This table compresses the twelve starter fields so the decision logic is easy to see. A real project template would use the full starter inventory columns.

| Data object | What it covers | Why this row exists | Sensitivity and restrictions | Storage and access | Status and end state |
| --- | --- | --- | --- | --- | --- |
| Recruitment and contact records | Names, phone numbers, emails, appointment notes, and follow-up information for interviewees and survey follow-up participants | Contact details need different handling from research data and should not sit in analysis folders | Direct identifiers; access should be very limited | Restricted project storage; PI and field coordinator only | Planned; delete when recruitment and follow-up are complete |
| Interviews with service providers and municipal staff | Audio recordings and transcripts from interviews with people speaking in professional roles | This group may be identifiable by role, but the risk profile differs from residents or informal workers | Personal data through voice, role, and institution; some contextual identifiability | Restricted project storage; project interview team | Planned; delete audio after transcript verification; retain pseudonymised transcripts internally |
| Interviews with residents and informal workers | Audio recordings and transcripts from interviews with residents, informal workers, or people describing service problems | This participant group may face higher risk if critical views or personal circumstances become identifiable | Higher contextual sensitivity; may include grievances, informal payments, economic stress, or fear of consequences | More restricted access than other interview material; PI and named qualitative researchers only | Planned; delete audio after transcript verification; review transcripts before wider team access |
| Raw household survey export | Full export from the survey platform, including household characteristics, service access, satisfaction, complaints, health, income shocks, and free-text fields | The raw export contains both ordinary and sensitive modules, so the whole export must be protected at the higher level until split or cleaned | Personal data possible through household composition, location, free text, and sensitive modules | Restricted project storage; survey lead and data manager only | Planned; retain until cleaned datasets are verified; review deletion or restricted retention |
| Sensitive survey module extract | Subset containing modules on complaints, informal payments, health, trust, or political pressure | A separate extract allows the team to limit access to the most sensitive survey content while allowing broader access to lower-risk analytical variables | Higher sensitivity than general service-access variables; small-cell and re-identification risks to review | Restricted analysis folder; data manager and named analysts only | Planned; retain only while needed; use aggregate outputs where possible |
| De-identified analytical dataset and codebook | Cleaned dataset for analysis, with direct identifiers removed and variables documented | This is the version most likely to support analysis, publication, and possible archiving | Intended lower risk, but must be checked for indirect identification and sensitive combinations | Project analysis folder; wider project team after review | Planned; archive open or restricted only after disclosure review |

## What this example shows

The right inventory row is not determined only by method. It is determined by the decisions that need to be made.

For interviews, participant group matters. Interviews with officials may require care because people are identifiable by role. Interviews with residents or informal workers may require stronger protection because participants may describe experiences that could expose them socially, politically, or economically.

For surveys, module content matters. A service-access module may ask relatively ordinary questions about water, transport, or school access. Another module in the same survey may ask about health, informal payments, political pressure, debt, violence, or fear of retaliation. If both modules are in the same raw export, the raw export should be handled according to the more sensitive content. If the project later separates the sensitive module into a restricted extract, that extract can become its own data object.

This does not mean every participant group or survey module always needs its own row. Split only when the handling decision changes:

- different access group
- different storage location
- different sensitivity level
- different retention period
- different sharing or archiving possibility
- different documentation or review need

## Before data collection

Before fieldwork starts, this project should clarify:

- which survey modules are sensitive
- whether free-text survey fields are needed
- whether household location is precise enough to identify respondents
- which participant groups require stronger protection
- who can access raw interviews, raw survey exports, and sensitive module extracts
- when audio recordings and contact records should be deleted
- which version of the data could be used for publication or archiving

## At project closure

At closure, the inventory should not just say "survey data complete" or "interviews complete". It should record the actual outcome for each object:

- contact records deleted
- audio recordings deleted or retained with justification
- transcripts retained internally or archived under restriction
- raw survey export deleted or retained under restriction
- sensitive module extract deleted, restricted, or aggregated
- de-identified analytical dataset archived openly or under controlled access

## Key point

Use the inventory to preserve the distinctions that matter. The same method can involve different participant groups, and the same survey can include modules with different sensitivity. The inventory should make those differences visible without forcing the project to document every file separately.

