---
icon: lucide/list-plus
title: "When to add more detail"
description: "Optional field groups for projects that need more than the CMI starter inventory."
tags:
  - data inventory
  - optional fields
  - CMI
date_updated: 2026-04-28
---

# When to add more detail

The starter inventory should be the default. Add fields only when they help the project make or document a real decision.

The larger inventory model is useful as a menu, not as a mandatory template. A sensitive interview project, a partner-data project, and a document-based review do not need the same columns.

## Add GDPR and personal data detail when needed

Add detail when a data object contains or may contain personal data, special category data, direct identifiers, indirect identifiers, or contextual identifiability.

Useful extra fields:

| Field | Use when |
| --- | --- |
| Personal data status | You need to distinguish no personal data, possible personal data, confirmed personal data, or anonymised data |
| Identifier types | Names, contact details, voice, image, location, role, rare characteristics, IP address, free text |
| Special category data | Health, ethnicity, political opinion, religion, biometric data, or similar GDPR Article 9 categories |
| Contextual identifiability | People, groups, organisations, or places may be identifiable through context |
| Lawful basis | The project needs the Article 6 or Article 9 basis visible at object level |
| Sikt relevance | The object is covered by or relevant to Sikt notification |

Do not add all of these for public documents or aggregate non-personal data unless there is a specific reason.

## Add ethics and contextual risk detail when needed

Add detail when legal categories do not capture the full risk. This is common in politically sensitive environments, research involving exposed participants, or work where re-identification could create harm.

Useful extra fields:

| Field | Use when |
| --- | --- |
| Risk notes | The reason for concern needs to be visible |
| Participant or data subject group | The group represented in the data affects risk or obligations |
| Country or location | Place affects security, interpretation, identifiability, or sharing |
| Ethics conditions | An ethics review, local approval, or project commitment sets conditions |
| Reuse limitations | Future use or sharing is limited by context, consent, or participant expectations |

## Add partner, provider, or agreement detail when needed

Add detail when data are received from, created with, transferred to, or processed by another organisation.

Useful extra fields:

| Field | Use when |
| --- | --- |
| Partner or provider | A partner, authority, company, NGO, consultant, or data provider is involved |
| Partner responsibility | Responsibility is shared or distributed across organisations |
| Agreement reference | A data sharing agreement, processing agreement, joint controller arrangement, or contract applies |
| Transfer method | Data move between people, institutions, countries, or systems |
| Contractual restrictions | An agreement limits storage, access, retention, use, publication, or sharing |

## Add documentation detail when needed

Add detail when the object needs to be understood later by the project team, a reviewer, a repository, a partner, or a future researcher.

Useful extra fields:

| Field | Use when |
| --- | --- |
| Documentation available | The project needs to know whether explanatory documentation exists |
| Documentation type | README, codebook, metadata record, method note, processing log, consent documentation |
| Documentation location | Documentation lives outside the inventory |
| Documentation gaps | Missing documentation needs follow-up |
| Codebook status | Structured data require variable-level explanation |
| Processing notes | Cleaning, transcription, translation, coding, anonymisation, or aggregation should be documented |

## Add sharing and archiving detail when needed

Add detail when the object may be deposited, shared, restricted, cited, or described in a data availability statement.

Useful extra fields:

| Field | Use when |
| --- | --- |
| Sharing status | Sharing is open, restricted, not possible, under review, or limited to derived data |
| Archive or repository | A repository or archive has been chosen or considered |
| Access terms | Licence, embargo, request procedure, or restricted access conditions apply |
| Data availability statement | The object is connected to a publication |
| Archive documentation | README, metadata, codebook, or restriction notes must accompany deposit |

## Add closure and deletion detail when needed

Add detail at project closeout, or earlier for objects with short lifetimes such as contact lists, raw audio, temporary transfer copies, or pseudonymisation keys.

Useful extra fields:

| Field | Use when |
| --- | --- |
| Deletion or review date | The object should be deleted or reviewed at a defined time |
| Closure status | Follow-up remains pending or unresolved |
| Final disposition | Deleted, retained internally, archived externally, transferred, or shared |
| Verification | The project needs evidence that deletion, deposit, transfer, or archive happened |
| Custodian after project | Someone needs responsibility after active funding ends |

## Key idea

The starter inventory is the front door. Optional fields are added because the project needs them, not because the model contains them.

