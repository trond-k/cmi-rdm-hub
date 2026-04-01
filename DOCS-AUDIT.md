# Documentation Audit and Content Plan

**Date:** 2026-04-01
**Scope:** All files in `docs/`, `working-files/`, `reports/`, `includes/`, and root-level content strategy documents.

---

## 1. Current state summary

### Published guide (`docs/`)

The live guide has **20 substantive pages** organised into 6 navigation sections, plus a landing page (`index.md`) and 4 unused placeholder stubs:

| Nav section | Pages | Status |
|---|---|---|
| Start here | `get-started.md` | Complete |
| Foundations | `elements-of.md`, `cmi-institutional-context.md`, `foundations-of-data-sharing.md`, `research-data-lifecycle.md` | Complete |
| Before the project | `lifecycle-1-frame.md`, `lifecycle-2-fund.md`, `lifecycle-3-plan.md` | Complete |
| During the project | `lifecycle-4-collect.md`, `lifecycle-5-store.md`, `lifecycle-6-process.md`, `lifecycle-7-analyse.md` | Complete |
| After the project | `lifecycle-8-publish.md`, `lifecycle-9-preserve.md`, `lifecycle-10-discover.md`, `lifecycle-11-access.md`, `lifecycle-12-share-and-reuse.md` | Complete |
| Cross-cutting guidance | `reproducibility-and-transparency.md`, `file-and-folder-naming.md`, `data-inventory.md` | Complete |

**Orphaned/unused files in `docs/`:**

| File | Status | Recommendation |
|---|---|---|
| `CROSS-ethics.md` | Placeholder stub ("Placeholder stub.") | **Delete.** Not in nav. If ethics becomes a cross-cutting page, create it fresh from working-files material. |
| `CROSS-gdpr-and-legal-compliance.md` | Placeholder stub | **Delete.** Same reasoning. |
| `CROSS-legal.md` | Placeholder stub | **Delete.** Overlaps with CROSS-gdpr-and-legal-compliance. |
| `CROSS-reproducability.md` | Placeholder stub (note typo: "reproducability") | **Delete.** The real page already exists as `reproducibility-and-transparency.md` in nav. |

### Working files (`working-files/`)

17 subdirectories containing ~65 markdown files and 15 Word documents (DMP examples). Material ranges from polished near-publishable drafts to rough early notes.

### Supporting infrastructure

| Location | Contents |
|---|---|
| `reports/` | 4 funder requirement research reports + 2 theme reports. Research inputs, not publishable pages. |
| `includes/abbreviations.md` | 12 abbreviation tooltips for the site. |
| `base-content-architecture.md` | Master content blueprint. Authoritative reference for scope and structure. |
| `STYLE-GUIDE.md` | Writing style rules. |
| `REVIEW-CHECKLIST.md` | QA checklist. |

---

## 2. Complete working-files inventory and disposition

### Category A: Ready to develop into new guide pages

These files contain substantial, well-structured content that fills clear gaps in the published guide. They should be developed into new `docs/` pages and added to the nav.

| Working file | Content summary | Quality | Proposed guide page | Nav placement |
|---|---|---|---|---|
| `blueprints/CROSS-ai-blueprint.md` | Blueprint for cross-cutting AI governance page. Well-structured proposal with section outlines, scoping decisions, and lifecycle cross-references. | High — clear blueprint ready for execution | `docs/ai-in-research.md` | Cross-cutting guidance |
| `ethics/ethics-guidelines.md` | Curated catalogue of ethics guidelines with links to Norwegian law, EU frameworks, international codes. | High — well-organised reference table | `docs/ethics-guidelines.md` | Cross-cutting guidance |
| `legal-and-agreements/contract-guide.md` | Practical guide to GDPR contracts (DPA, joint controller, transfer agreements). Clear decision logic for when contracts are needed. | High — near-publishable | `docs/contracts-and-agreements.md` | Cross-cutting guidance |
| `legal-and-agreements/personal-data-guide.md` | Thinking guide: does your project use personal data? Design-oriented, not compliance-heavy. | High — well-written, clear voice | `docs/personal-data-guide.md` | Cross-cutting guidance (or link from lifecycle-1-frame) |
| `cmi-context/regulations/gdpr-demystifier.md` | Plain-language GDPR reference. Concepts explained thematically with CMI interpretive positions. | High — substantial, well-structured | `docs/gdpr-demystifier.md` | Cross-cutting guidance |
| `lifecycle-and-planning/data-classification.md` | Four-tier classification scheme with application guidance. | High — polished draft | `docs/data-classification.md` | Cross-cutting guidance |
| `lifecycle-and-planning/access-control-decision-tree.md` | Decision guide for choosing open/embargoed/restricted/closed access. | High — practical, well-structured | `docs/access-control-decision-tree.md` | Cross-cutting guidance (or link from lifecycle-11-access) |
| `sikt/sikt.md` | When and how to file a Sikt notification, CMI's institutional agreement with Sikt. | High — practical, CMI-specific | `docs/sikt-notification.md` | Cross-cutting guidance |
| `infrastructure/security-in-ms365.md` | Researcher-facing guide to M365 security, encryption, CLOUD Act, when to use alternatives. | High — clear, well-written | `docs/security-in-ms365.md` | Cross-cutting guidance (or link from lifecycle-5-store) |

### Category B: Useful source material — merge into existing or new pages

These files contain valuable content that should be absorbed into existing guide pages or combined with Category A files rather than becoming standalone pages.

| Working file | Content summary | Quality | Merge target |
|---|---|---|---|
| `cmi-context/regulations/consent-and-information.md` | Consent and information letter guidance. | Good | Merge into personal-data-guide or sikt-notification page |
| `cmi-context/regulations/gdpr-positions.md` | CMI's GDPR interpretive positions (lawful basis, proportionality). | Good | Merge into gdpr-demystifier page |
| `ethics/ethics-assessment.md` | Ethics self-assessment guidance. | Moderate | Merge into lifecycle-3-plan or a new ethics cross-cutting page |
| `ethics/informing-participants.md` | Participant information and consent. | Moderate | Merge into personal-data-guide or sikt-notification |
| `ethics/elements-of.md` | Ethics angle on "elements of" framework. | Moderate | Merge into existing `docs/elements-of.md` if relevant content is missing |
| `legal-and-agreements/partners-and-data-roles.md` | Partner roles, data controller/processor distinctions. | Good | Merge into contracts-and-agreements page |
| `infrastructure/collaboration-in-m365.md` | Collaboration features in M365 (Teams, SharePoint). | Moderate | Merge into security-in-ms365 or lifecycle-5-store |
| `infrastructure/chatgpt-ms365.md` | ChatGPT/Copilot in M365 context. | Moderate | Merge into ai-in-research page |
| `cmi-context/tools/tools-and-services.md` | Cloud service and tool assessment framework. | Good | Merge into security-in-ms365 or create a tools reference page |
| `cmi-context/tools/data-security.md` | Storage infrastructure details (M365, TSD, Tresorit). | Good | Merge into security-in-ms365 or lifecycle-5-store |
| `cmi-context/cmi-policies/approved_repo_list.md` | List of approved repositories. | Reference list | Merge into lifecycle-8-publish |
| `cmi-context/cmi-policies/approved_storage_list.md` | List of approved storage solutions. | Reference list | Merge into lifecycle-5-store or security-in-ms365 |
| `cmi-context/cmi-policies/licenses.md` | Licence guidance for data and publications. | Good | Merge into lifecycle-12-share-and-reuse |
| `cmi-context/cmi-policies/identifiers_anonymisation.md` | Anonymisation and identifier handling. | Moderate | Merge into lifecycle-6-process or data-classification |
| `cmi-context/cmi-policies/open-science.md` | Open science policy context. | Moderate | Merge into foundations-of-data-sharing or lifecycle-2-fund |
| `cmi-context/cmi-policies/NEW_oa_policy_cmi.md` | New CMI open access policy. | Policy document | Merge into lifecycle-2-fund or lifecycle-8-publish |
| `open-science/fair-principles.md` | FAIR principles explanation. | Moderate | Already covered in foundations-of-data-sharing; merge any unique content |
| `open-science/funding-requirements.md` | Funder requirements overview (RCN focus). | Moderate | Superseded by `reports/` funder analyses; merge residual into lifecycle-2-fund |
| `open-science/open-science.md` | General open science introduction. | Moderate | Already covered in foundations-of-data-sharing |
| `lifecycle-and-planning/data-transformation-log.md` | Template/guide for documenting data transformations. | Good | Merge into lifecycle-6-process |
| `lifecycle-and-planning/research-data-lifecycle.md` | Working version of lifecycle model. | Moderate | Already published as `docs/research-data-lifecycle.md` |
| `foundations/origins-of-knowledge-and-data-sharing.md` | Working version of data sharing foundations. | Moderate | Already published as `docs/foundations-of-data-sharing.md` |
| `foundations/philosophical-foundations-of-data-sharing.md` | Philosophical angle on data sharing. | Moderate | Already absorbed into published version |
| `foundations/reproducibility-and-transparency.md` | Working version of reproducibility page. | Moderate | Already published |
| `data-inventory/data-inventory.md` | Working version of data inventory. | Moderate | Already published as `docs/data-inventory.md` |
| `data-inventory/data-inventory-guide.md` | Companion guide. | Good | Merge into `docs/data-inventory.md` if unique content |
| `data-inventory/data-inventory-template.md` | Template for data inventory. | Template | Link from or embed in `docs/data-inventory.md` |
| `data-inventory/dmp-cmi-data-inventory.md` | DMP-focused inventory guidance. | Moderate | Merge into lifecycle-3-plan or data-inventory |
| `cmi-context/research-context/cmi-institutional-context.md` | Working version. | Moderate | Already published |
| `cmi-context/research-context/cmi-profile.md` | Institutional profile. | Background | Merge into cmi-institutional-context if unique |
| `cmi-context/research-context/organisation-and-compliance.md` | Org structure and compliance landscape. | Moderate | Merge into cmi-institutional-context |
| `sikt/sikt-notification.md` | Sikt notification details. | Good | Merge into sikt.md before publishing |
| `sikt/sikt-notification-repl.md` | Sikt notification revision/replacement. | Moderate | Merge into sikt.md |
| `sikt/siktify_attach_claude_opus4-6-modified.md` | AI-assisted Sikt form completion experiment. | Experimental | Internal reference only; do not publish |

### Category C: Historical/superseded — archive or delete

These files have been superseded by published content or newer working files. They should be retained as historical record but need no further development.

| Working file | Reason |
|---|---|
| `early-drafts/get-started.md` | Superseded by published `docs/get-started.md` |
| `early-drafts/origins-of-knowledge-and-data-sharing-v1.md` | Superseded by `foundations/` version and published page |
| `early-drafts/core-principles-v1.md` | Superseded by `principles/core-principles.md` |
| `early-drafts/why-rdm-matters-v1.md` | Superseded by `principles/why-rdm-matters.md` |
| `early-drafts/data-inventory-first-draft.md` | Superseded by `data-inventory/` versions |
| `early-drafts/data-inventory-template-first-draft.md` | Superseded by `data-inventory/data-inventory-template.md` |
| `early-drafts/gdpr-stance.md` | Superseded by `regulations/gdpr-positions.md` |
| `early-drafts/data-classification-opus-new.md` | Superseded by `lifecycle-and-planning/data-classification.md` |
| `early-drafts/contracts-and-agreements.md` | Superseded by `legal-and-agreements/contract-guide.md` |
| `early-drafts/markdown.md` | Markdown syntax reference — not guide content |
| `early-drafts/siktify_attach_claude_opus4-6-interface.md` | AI experiment log — internal only |
| `principles/core-principles.md` | Content absorbed into `docs/elements-of.md` |
| `principles/data-principles.md` | Content absorbed into `docs/elements-of.md` |
| `principles/why-rdm-matters.md` | Content absorbed into `docs/get-started.md` and `docs/elements-of.md` |
| `sikt/sikt-form-fields-json/*.json` (13 files) | Structured form field definitions for Sikt. Internal tooling, not guide content. |
| `prompts/draft-prompts.md` | AI prompt templates — internal process, not guide content |

### Category D: Institutional reference — keep but do not publish

These files serve as internal institutional knowledge. They inform guide content but are not themselves publishable pages.

| Working file | Purpose |
|---|---|
| `rdm-at-cmi-recs/rdm@cmi-approach-overview.md` | Internal RDM strategy document. Informs overall approach. |
| `rdm-at-cmi-recs/rdm@cmi-pipline-assessment-recommendations.md` | Pipeline assessment recommendations. |
| `rdm-at-cmi-recs/rdm@cmi-rec#1-teams-based-structure.md` | Teams structure recommendation. |
| `rdm-at-cmi-recs/rdm@cmi-rec#2-assessment-and-classification.md` | Assessment and classification recommendation. |
| `rdm-at-cmi-recs/rdm@cmi-rec#3-data-inventory.md` | Data inventory recommendation. |
| `rdm-at-cmi-recs/rdm@cmi-rec#4-document-bundle.md` | Document bundle recommendation. |
| `rdm-at-cmi-recs/rdm@cmi-rec#5-project-closure.md` | Project closure recommendation. |
| `rdm-at-cmi-recs/repository-strategy.md` | Repository strategy. |
| `early-operational-docs/*.docx` (15 files) | Real project DMP examples. Valuable as internal templates/examples but contain project-specific information. |

### Category E: Reports — keep as research inputs

| File | Purpose |
|---|---|
| `reports/rcn-requirements.md` | RCN funder requirements analysis |
| `reports/horizon-europe-requirements.md` | Horizon Europe requirements analysis |
| `reports/erc-requirements.md` | ERC requirements analysis |
| `reports/norad-requirements.md` | Norad requirements analysis |
| `reports/themes-reports/reproducibility-and-transparency-research-report.md` | Research input for reproducibility page |
| `reports/themes-reports/store-page-issue-resolution.md` | Issue resolution notes for store page |

These are research inputs, not publishable content. They inform `lifecycle-2-fund.md` and other pages. Keep as-is.

---

## 3. Proposed new navigation structure

The current nav has 3 cross-cutting pages. Based on the working-files audit, the cross-cutting section should expand significantly. This is where most of the actionable development work lies.

### Proposed nav (changes marked with *)

```
Start here
  └─ get-started.md

Foundations
  ├─ elements-of.md
  ├─ cmi-institutional-context.md
  ├─ foundations-of-data-sharing.md
  └─ research-data-lifecycle.md

Before the project
  ├─ lifecycle-1-frame.md
  ├─ lifecycle-2-fund.md
  └─ lifecycle-3-plan.md

During the project
  ├─ lifecycle-4-collect.md
  ├─ lifecycle-5-store.md
  ├─ lifecycle-6-process.md
  └─ lifecycle-7-analyse.md

After the project
  ├─ lifecycle-8-publish.md
  ├─ lifecycle-9-preserve.md
  ├─ lifecycle-10-discover.md
  ├─ lifecycle-11-access.md
  └─ lifecycle-12-share-and-reuse.md

Cross-cutting guidance
  ├─ reproducibility-and-transparency.md
  ├─ file-and-folder-naming.md
  ├─ data-inventory.md
  ├─ * data-classification.md            (NEW — from working-files)
  ├─ * personal-data-guide.md            (NEW — from working-files)
  ├─ * gdpr-demystifier.md               (NEW — from working-files)
  ├─ * contracts-and-agreements.md        (NEW — from working-files)
  ├─ * sikt-notification.md              (NEW — from working-files)
  ├─ * ai-in-research.md                 (NEW — from blueprint)
  ├─ * access-control-decision-tree.md   (NEW — from working-files)
  ├─ * security-in-ms365.md              (NEW — from working-files)
  └─ * ethics-guidelines.md              (NEW — from working-files)
```

### Navigation design considerations

**Option A (above):** Flat cross-cutting section. Simple. Works if 12 pages is not too many for a single sidebar group.

**Option B:** Split cross-cutting into sub-groups:

```
Cross-cutting guidance
  ├─ Practical tools
  │   ├─ data-inventory.md
  │   ├─ file-and-folder-naming.md
  │   ├─ data-classification.md
  │   ├─ access-control-decision-tree.md
  │   └─ sikt-notification.md
  ├─ Legal and ethics
  │   ├─ personal-data-guide.md
  │   ├─ gdpr-demystifier.md
  │   ├─ contracts-and-agreements.md
  │   └─ ethics-guidelines.md
  └─ Technology and methods
      ├─ reproducibility-and-transparency.md
      ├─ ai-in-research.md
      └─ security-in-ms365.md
```

**Recommendation:** Start with Option A. If the flat list feels unwieldy after all pages are developed, restructure into Option B. The content itself does not change either way.

---

## 4. What is missing

Gaps not covered by any existing file (published or working):

| Gap | Description | Priority | Source material |
|---|---|---|---|
| **Project closure checklist** | What to do when a project ends: final DMP update, inventory completion, archival, access decisions, destruction schedules. | High | `rdm-at-cmi-recs/rdm@cmi-rec#5-project-closure.md` has some material |
| **DMP writing guide** | Practical "how to write your DMP" page — linking Sikt DMP tool, templates, and the inventory. Currently described in lifecycle-3-plan but not a standalone actionable guide. | Medium | `base-content-architecture.md` Stage 3 section |
| **Funder requirements summary** | A concise reference table: what RCN, Horizon Europe, ERC, and Norad each require. The `reports/` folder has deep analysis but no researcher-facing summary page. | Medium | `reports/*.md` (4 funder reports) |
| **Information letter templates/guide** | How to write participant information letters. Referenced repeatedly but not a standalone page. | Medium | `ethics/informing-participants.md`, `regulations/consent-and-information.md` |
| **Fieldwork data handling** | Data management during fieldwork: device security, offline workflows, field encryption, cross-border data movement. | Medium | Scattered references in lifecycle stages |
| **Code and software management** | Version control, dependency management, code archiving — currently touched in lifecycle-7-analyse and reproducibility but not a standalone guide. | Low | Existing lifecycle pages |

---

## 5. Files to delete from `docs/`

These files are not in the nav, contain no content, and create confusion:

1. `docs/CROSS-ethics.md` — placeholder stub
2. `docs/CROSS-gdpr-and-legal-compliance.md` — placeholder stub
3. `docs/CROSS-legal.md` — placeholder stub
4. `docs/CROSS-reproducability.md` — placeholder stub (also has typo)

**Action:** Delete all four. They serve no purpose and the topics they gesture at are better served by the Category A pages above.

---

## 6. Recommended development priority

### Phase 1 — High-value, near-ready pages (minimal new writing)

These working files are already close to publishable quality. They fill the most important gaps (GDPR, data classification, Sikt) that researchers actively need.

1. **`data-classification.md`** — Four-tier scheme. Referenced by many pages. Foundational.
2. **`personal-data-guide.md`** — "Do I have personal data?" entry point. High researcher demand.
3. **`gdpr-demystifier.md`** — Plain-language GDPR reference. Reduces anxiety and support requests.
4. **`sikt-notification.md`** — Practical CMI-specific workflow. Immediate utility.
5. **`contracts-and-agreements.md`** — When you need a DPA, joint controller agreement, etc.

### Phase 2 — Important supporting pages (moderate development)

6. **`access-control-decision-tree.md`** — Complements lifecycle-11-access.
7. **`security-in-ms365.md`** — Researcher-facing infrastructure guide.
8. **`ethics-guidelines.md`** — Reference catalogue (mostly link curation).

### Phase 3 — New content requiring more development

9. **`ai-in-research.md`** — Blueprint exists but page needs writing from scratch.
10. **Funder requirements summary page** — Synthesise from reports/ into a concise table.
11. **Project closure checklist** — Develop from rec#5 material.

### Housekeeping (can happen any time)

- Delete 4 CROSS-* stubs from `docs/`
- Clean `early-drafts/` — move to an `archive/` folder or delete
- Review `includes/abbreviations.md` — add abbreviations for terms introduced by new pages (DPIA, DPA, TSD, NSD, PID, etc.)

---

## 7. Summary statistics

| Metric | Count |
|---|---|
| Published guide pages (in nav) | 20 |
| Orphaned stubs in docs/ (delete) | 4 |
| Working files ready to develop (Category A) | 9 |
| Working files to merge into other pages (Category B) | ~30 |
| Superseded/historical files (Category C) | ~15 |
| Internal reference files (Category D) | ~23 |
| Research input reports (Category E) | 6 |
| Identified content gaps (missing pages) | 6 |
| **Projected guide size after full development** | **~29-31 pages** |
