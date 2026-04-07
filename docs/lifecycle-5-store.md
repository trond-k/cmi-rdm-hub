---
icon: lucide/hard-drive
title: "STORE"
description: "Keep your data secure, backed up, and organised while the project is active: choose the right storage, separate sensitive material, and make sure the whole team can find what they need."
tags:
  - Store
  - Security
  - Backup
  - Sensitive data
  - MS365
notes: "Resolve all issue concering checks for researcher to do themselves; this guide should have the answers, not list more tasks for reseaarchers to do."
date_updated: 2026-04-04
---

# STORE: active data storage

*Where your data lives during the project determines how secure it is, how easily your team can collaborate, and how smoothly you can preserve and share it later. CMI's default infrastructure covers most needs, but sensitive data, large files, and multi-site collaboration all require deliberate choices. Get storage right early; retrofitting security or reorganising a chaotic folder structure mid-project is far more expensive than setting things up properly from the start.*

## Start with the CMI default

CMI provides Microsoft 365 E5 as its standard working environment. For most projects, this is where your data should live during the active research phase. OneDrive handles individual working files, SharePoint provides shared project spaces, and Teams integrates communication with document collaboration. The E5 licence includes built-in access controls, multi-factor authentication, versioning, and endpoint security.

This default handles a broad range of research data, from non-sensitive project documents to data with moderate sensitivity, provided that access permissions are configured correctly and limited to those who need them. The E5 security features, including conditional access policies and multi-factor authentication, give you meaningful control over who can reach what. Before looking elsewhere, check whether the standard setup meets your needs. Adding tools without a clear reason creates complexity and fragments your data across platforms.

CMI organises each research project as a dedicated Microsoft Team with a standard channel structure:

| Channel | What goes here |
|---------|----------------|
| **General** | Project-wide announcements, key links, quick-access documents |
| **Admin** | Contracts, proposals, project management documents, meeting notes |
| **RDM** | Data management documentation, templates, compliance records |
| **Research** | Working documents, data files, analysis, fieldwork materials |
| **Outputs** | Publications, reports, deliverables, dissemination materials |

This structure means your project data has a defined home from the start, with access controls managed at the Team level. The PI is the Team owner and controls who has access. External collaborators are added as guests to specific channels rather than given access to the entire workspace.

!!! tip "Set up the project Team before collection starts"
    Ensure the project Team exists, the channel structure is in place, and permissions are set before fieldwork begins. If team members start storing files on personal OneDrive accounts or local drives because no shared space exists yet, you will spend weeks consolidating later. See [Name files and structure folders](file-and-folder-naming.md) for conventions.

## When you need something more

Some data cannot or should not be stored in the standard MS365 environment. The most common reasons are data sensitivity, regulatory requirements, and the need for end-to-end encryption that the institution does not control.

### Sensitive personal data

If your project processes personal data that falls into the GDPR's special categories (health data, political opinions, ethnic origin, biometric data), or if the risk profile is elevated because of the research context (conflict zones, authoritarian settings, vulnerable populations), consider a dedicated secure environment.

[TSD (Tjenester for Sensitive Data)](https://www.uio.no/english/services/it/research/sensitive-data/) is the standard Norwegian solution for sensitive research data. It provides an isolated environment with strict access controls, two-factor authentication, and data residency within Norway. TSD is appropriate when your DPIA or institutional policy requires a higher level of protection than the standard MS365 configuration offers.

For projects involving encrypted file sharing with external partners, particularly in contexts where participants or collaborators face surveillance risks, [Tresorit](https://tresorit.com/) and [ProtonDrive](https://proton.me/drive) offer end-to-end encryption. These are useful for transit and collaboration, but they are not a substitute for a managed research environment like TSD for long-term storage of sensitive data.

### Large files and specialist formats

Audio and video recordings, geospatial datasets, and high-resolution imagery can exceed the practical limits of cloud-synced storage. If your project generates large volumes of binary data, plan for where these will live. SharePoint has per-file and per-library size limits that may not accommodate raw video or satellite imagery. Discuss options with CMI's IT team early, before collection produces files that have nowhere to go.

## Separate identifiers from research data

For projects involving personal data, store direct identifiers (names, contact details, ID numbers) separately from the research data itself. A linking key file connects the two; this file should be stored in a different location with more restrictive access than the main dataset.

This principle of data compartmentalisation reduces the impact of a breach. If someone gains access to the research data, they find pseudonymised records. If they access the key file, they find identifiers without context. Neither is useful alone. Document where each component is stored and who has access in the [data inventory](data-inventory.md).

!!! warning "Do not store key files alongside research data"
    Keeping the linking key in the same folder, drive, or environment as the pseudonymised data defeats the purpose of separation. If both are compromised together, pseudonymisation offers no protection. Store the key file in a separate, more restricted location, and limit access to those who genuinely need it.

## Back up deliberately

MS365 provides built-in versioning and retention policies that protect against accidental deletion and overwrites. For most project files stored in SharePoint or OneDrive, this is sufficient as a day-to-day safeguard.

However, built-in cloud versioning is not a comprehensive backup strategy. Consider whether your project needs additional protection in the following situations:

- Data that exists only on local devices (field laptops, recording equipment) before it has been uploaded.
- Data stored in environments outside MS365 (TSD, external partner systems, specialist databases).
- Data where loss would be catastrophic and reconstruction impossible (unique field recordings, one-time survey responses).

For field collection, the most vulnerable period is between the moment data is created and the moment it reaches secure storage. Establish a routine for transferring data from devices to the project's storage environment at the end of each collection day, or more frequently if conditions allow. Carry encrypted portable storage as a fallback when internet access is unreliable.

!!! tip "Test your recovery, not just your backup"
    A backup that has never been tested is a hope, not a plan. Periodically verify that you can actually restore a file from your backup arrangement. This is especially important before major fieldwork phases.

## Organise for your future self

Storage is not just about where files live; it is about whether anyone can find them six months from now. The folder structure and naming conventions described in [Name files and structure folders](file-and-folder-naming.md) are your primary tools here. The key structural principle is to separate raw data from derived and working files:

- `raw/` for untouched source material.
- `processed/` for cleaned or transformed versions.
- `analysis/` for scripts, coding frameworks, and working outputs.
- `outputs/` for deliverables.

Never edit raw files in place. If a recording needs trimming or a dataset needs cleaning, save the result in `processed/` and leave the original intact. This preserves the chain of evidence and makes it possible to retrace your steps.

## Collaborate without chaos

Shared storage only works if the team agrees on how to use it. Common problems include conflicting edits on the same file, documents saved to personal drives instead of the shared space, and folders created outside the agreed structure.

For text documents and spreadsheets, MS365's real-time co-authoring and version history handle most collaboration needs. For code and scripts, use [Git](https://git-scm.com/) (with a remote repository on GitHub, GitLab, or a CMI-hosted instance) rather than relying on file naming to track versions. For projects with external partners who do not have access to CMI's MS365 environment, agree on a shared platform and transfer protocol before data starts flowing.

!!! warning "Sync conflicts are data risks"
    When files are edited offline and synced later, conflicting versions can be created. Cloud platforms usually flag these, but they do not resolve them automatically. If your project involves frequent offline work (common in field settings with intermittent connectivity), establish a protocol for checking and resolving sync conflicts after each reconnection.

## Meet compliance requirements

Your storage arrangements may be subject to external requirements beyond your own preferences:

- **GDPR data residency.** Microsoft stores CMI's MS365 data in EU/EEA data centres, which satisfies GDPR residency requirements for most purposes. The question becomes relevant when you move data outside the default infrastructure: sharing files through a non-EU cloud service, transferring data to a partner institution in a country without an EU adequacy decision (i.e. one whose data protection standards the EU has not recognised as essentially equivalent to the GDPR), or using a specialist platform hosted outside Europe. If your project involves any of these, check the legal basis for the transfer before data moves. See [GDPR and legal compliance](CROSS-gdpr-and-legal-compliance.md).
- **Funder mandates.** Some funders specify that data must be stored on institutional or national infrastructure during the project. Check the grant agreement.
- **Contractual obligations.** Commissioned research may include clauses on data handling, storage location, or access that constrain your choices.

Document your storage arrangements in the DMP and the [data inventory](data-inventory.md), and revisit them if circumstances change (a new partner joins, a dataset turns out to be more sensitive than anticipated, or a provider changes its terms of service).

!!! info "Last reviewed"
    This page was last reviewed on 26 March 2026. Storage services, pricing, and compliance features change frequently. Verify current capabilities against the provider's documentation before making decisions.