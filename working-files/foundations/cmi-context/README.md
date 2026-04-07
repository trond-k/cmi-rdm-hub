# Context — reference materials for content generation

This folder contains reference materials that Claude Code uses when generating
documentation content for the RDM Hub. **Nothing here is published to the site.**

## How it works

When asked to write or revise a documentation page, Claude Code reads relevant
files from this folder first, then produces content grounded in CMI-specific
details rather than generic guidance.

## Folder structure

| Folder | Contents |
|---|---|
| `research-context/` | CMI institutional profile, organisational structure, funding context |
| `regulations/` | GDPR interpretive positions, Sikt notification, consent and information letters |
| `cmi-policies/` | Data classification, fieldwork, open science, sharing/archiving, partnerships, retention |
| `tools/` | Storage infrastructure, data security, platform options |
| `examples/` | Sample DMPs, folder structures, metadata files (empty — to be populated) |

## Current files

| File | Location | Description |
|---|---|---|
| `cmi-profile.md` | `research-context/` | Institutional identity, research profile, geographic focus, partnerships |
| `organisation-and-compliance.md` | `research-context/` | Roles, ethics structures, external bodies, funding context |
| `gdpr-positions.md` | `regulations/` | CMI's interpretive positions on GDPR for research |
| `consent-and-information.md` | `regulations/` | Information letter guidance, oral delivery, translations |
| `sikt.md` | `regulations/` | Sikt notification process and CMI's institutional agreement |
| `data-classification.md` | `cmi-policies/` | Four-tier classification scheme (Green/Yellow/Red/Black) |
| `fieldwork.md` | `cmi-policies/` | Device preparation, daily upload, high-risk contexts |
| `open-science.md` | `cmi-policies/` | Open access, data sharing pathways, anonymisation feasibility, repository defaults |
| `data-management-planning.md` | `cmi-policies/` | DMP requirements by funder, initial data mapping, typical DMP content |
| `partnerships.md` | `cmi-policies/` | Partnership types, data agreements, cross-border transfers |
| `retention.md` | `cmi-policies/` | Retention periods, deletion procedures, withdrawal handling |
| `data-security.md` | `tools/` | M365 infrastructure, storage by tier, TSD, access control |
| `tools-and-services.md` | `tools/` | Cloud service assessment, survey platforms, transcription, AI tools |

## Conventions

- All files include YAML front matter with `version`, `date`, and optional `notes`.
- Notes in front matter flag open questions, items to confirm, or dependencies.
- Cross-references between files use filename only (e.g., `gdpr-positions.md`).
- Plain-text Markdown (`.md`) is preferred so Claude Code can read files directly.
- Keep files focused — one topic per file.
