---
icon: lucide/lock-keyhole
title: "ACCESS"
description: "Decide who can use your data, under what terms, and through what mechanisms: define access levels, set governance conditions, and plan for eventual withdrawal."
tags:
  - Access
  - Governance
  - Sensitive data
  - FAIR
  - GDPR
notes: ""
date_updated: 2026-03-26
---

# ACCESS: conditions for data retrieval

*Sharing data does not mean giving it away without conditions. Access governance is the set of decisions about who can retrieve your data, what they may do with it, and what mechanisms enforce those terms. For most CMI research, the question is not whether to restrict access but how to calibrate restrictions so that legitimate reuse is possible while participants and communities remain protected. Trustworthy archives provide the infrastructure; your job is to define the terms.*

## Access is not binary

The simplest framing of data access is open or closed. In practice, most research data falls somewhere in between, and the right position depends on the dataset, the context, and the commitments you made to participants.

A tiered model recognises this:

| Level | What it means | Typical use |
|---|---|---|
| Open access | Anyone can download without conditions | De-identified survey data, code, documentation |
| Embargoed access | Open after a defined period | Data supporting a publication in progress, funder-permitted embargo |
| Controlled access | Available to approved users under specific terms | Interview transcripts, data with residual re-identification risk |
| Metadata only | Description published, data withheld | Highly sensitive data, data held by local partners under community governance |
| Closed | Neither data nor metadata publicly available | Rare; justified only where even the existence of the data could cause harm |

Most CMI projects will use more than one level across their datasets. A household survey may be suitable for open access after de-identification, while interview transcripts from the same project require controlled access because contextual details make participants identifiable. Geospatial data pinpointing locations in a conflict zone may warrant metadata-only publication. Each dataset needs its own assessment.

!!! tip "Decide access levels early, not at deposit"
    Access conditions are easiest to set when you can still consult your participant information sheets, your ethics approval, and your collaboration agreements. If you leave the decision until the archive asks for it, you risk either defaulting to closed (losing reuse value) or defaulting to open (breaching commitments). The [data inventory](data-inventory.md) should record the intended access level for each dataset from the planning stage onward.

## Define governance terms

An access level says who can reach the data. Governance terms say what they may do with it. For controlled-access datasets, these terms are typically formalised in a data use agreement that specifies:

- **Purpose limitations.** What the data may be used for (e.g., non-commercial research only, specific research questions, secondary analysis consistent with the original consent).
- **Redistribution prohibitions.** Whether the user may share the data with others, or must direct them to the archive to apply independently.
- **Derived data restrictions.** Whether findings, linked datasets, or other outputs derived from the data carry forward any conditions.
- **Reporting requirements.** Whether the user must notify the depositor of publications or other outputs based on the data.
- **Destruction obligations.** Whether the user must delete the data after a defined period or on completion of the approved project.

Archives such as the [Sikt Research Data Archive](https://sikt.no/en/tjenester/arkivering-av-forskningsdata) and the [UK Data Service](https://ukdataservice.ac.uk/) manage access request workflows on your behalf: a potential user applies, the archive (or the depositor, depending on the arrangement) reviews the application, and the archive handles authentication and download. This is substantially less work than managing access requests yourself, and it creates an audit trail that demonstrates responsible stewardship.

!!! warning "Do not confuse access governance with data protection"
    A data use agreement governs what a user may do with the data after they receive it. It does not replace your GDPR obligations, which govern what you may do with personal data throughout its lifecycle. If controlled-access data contain personal information, the legal basis for sharing must be established independently of the access agreement. See [GDPR and legal compliance](CROSS-gdpr-and-legal-compliance.md).

## Access mechanisms

How data is physically retrieved depends on the sensitivity and the infrastructure available.

For open and embargoed datasets in a repository, access is straightforward: the user downloads from the archive's landing page once the conditions are met. No special infrastructure is needed.

For controlled-access data, the mechanism depends on the level of protection required:

- **Licensed download.** The user signs a data use agreement and downloads a copy. Suitable for data where the main risk is misuse rather than exposure, and where the terms of use provide adequate protection.
- **Secure remote access.** The user logs into a controlled environment where the data can be analysed but not extracted. [Sikt's microdata.no](https://microdata.no/en/) provides this for Norwegian register data. Trusted Research Environments (TREs) operate on the same principle: the analysis travels to the data, rather than the data travelling to the analyst.
- **On-site access.** For the most sensitive material, physical presence at a designated facility may be required. This is rare in social science research but relevant for data where even encrypted transfer is considered too risky.

The choice of mechanism should be proportionate to the actual risk. Overly restrictive access (requiring on-site visits for data that could safely be shared under a licence) discourages legitimate reuse without meaningfully improving protection. Conversely, licensed download is insufficient for data where a single breach could cause serious harm to identifiable individuals.

## Community governance and partner-held data

For data collected in partnership with communities or local institutions, access governance may not be yours alone to define. The CARE Principles (Collective Benefit, Authority to Control, Responsibility, Ethics) hold that communities should retain meaningful influence over how data about them are used. In practice, this can mean:

- Joint decision-making on access applications, where the community or local partner reviews requests alongside (or instead of) the depositor.
- Local retention of some or all data, with metadata published centrally so that the data are discoverable without being directly accessible.
- Time-limited or purpose-limited access that reflects the community's preferences, not just the researcher's or the funder's.

These arrangements require negotiation during research design and formalisation in collaboration agreements, not improvisation at the deposit stage. They also require archives and infrastructure that can support non-standard governance models, which is an evolving space. Where standard repository workflows do not accommodate community governance, discuss the options with the archive or with CMI's RDM contact (rdm@cmi.no).

## Sunsetting and withdrawal

Data does not always remain available indefinitely. Circumstances change: a political situation shifts, new information makes participants identifiable, a participant exercises their right to withdraw, or a retention period expires. Access governance should account for these possibilities.

When data must be withdrawn from a repository, the metadata record should remain in place as a tombstone: a persistent landing page that records that the dataset existed, why it was withdrawn, and what (if any) alternative access arrangements apply. This preserves the citation record and prevents broken links. It also satisfies the FAIR principle that metadata should remain accessible even when the data are no longer available (Accessibility principle A2).

Plan for withdrawal rather than assuming permanence. If your information letter promises participants that their data will be deleted after a specific date, your access arrangements must be able to honour that promise. If an embargo has a defined end date, the archive should be configured to release the data automatically or notify you to confirm. If access conditions depend on a political situation remaining stable, build in a review mechanism.

!!! tip "Tombstones are better than silence"
    A withdrawn dataset with a tombstone record tells the research community what happened. A dataset that simply disappears leaves everyone guessing, and anyone who cited it holding a dead link. Archives such as Sikt maintain tombstone records by default; if you are using a different repository, check that it supports this.

!!! info "Last reviewed"
    This page was last reviewed on 26 March 2026. Access infrastructure, repository features, and legal frameworks evolve; verify current capabilities against the relevant documentation.