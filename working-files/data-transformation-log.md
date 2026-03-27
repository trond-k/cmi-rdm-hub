---
icon: lucide/file-diff
title: "Data transformation log template"
description: "A template for recording transformations applied to research data during processing and analysis."
tags:
  - Process
  - Documentation
  - Template
notes: ""
date_updated: 2026-03-24
---

# Data Transformation Log Template

**Project:** _______________________________________________
**Researcher(s):** _______________________________________________
**Data type:** ☐ Quantitative  ☐ Qualitative  ☐ Mixed
**Log maintained by:** _______________________________________________
**Date started:** _______________________________________________

---

## How to use this log

Record every significant change made to your data after collection — including cleaning, recoding, restructuring, anonymisation, and format conversion. Each entry should be sufficient for another researcher (or your future self) to understand *what* was changed, *why*, and *how* to reverse or reproduce it. Do not overwrite raw data; always work on copies and store originals separately.

---

## Section A — File & Version Register

Track which files are in use and how they relate to one another.

| Version ID | Filename | Format | Date created | Derived from | Notes |
|---|---|---|---|---|---|
| v1.0 | | | | Raw file | Original, unmodified |
| v1.1 | | | | v1.0 | |
| v2.0 | | | | v1.1 | |

> **Tip:** Use a consistent naming convention, e.g. `projectcode_datatype_version_YYYYMMDD`. See the *File Naming & Folder Structure Guide* for CMI conventions.

---

## Section B — Transformation Entries

Add one row per transformation action. For large projects, consider a separate log per dataset or fieldwork site.

| Entry # | Date | Performed by | Input file (version) | Output file (version) | Type of transformation | Description | Reason / justification | Reversible? | Script / tool used |
|---|---|---|---|---|---|---|---|---|---|
| 001 | | | | | | | | ☐ Yes  ☐ No | |
| 002 | | | | | | | | ☐ Yes  ☐ No | |
| 003 | | | | | | | | ☐ Yes  ☐ No | |

**Transformation types — select the most applicable:**

*Quantitative:*
- Variable recoding (e.g. collapsing categories, reversing scale)
- Derived variable creation (e.g. index construction, calculated fields)
- Missing value handling (e.g. imputation, exclusion, flagging)
- Outlier treatment (e.g. winsorising, removal, flagging)
- Merging / reshaping (e.g. wide-to-long, dataset joins)
- Format conversion (e.g. CSV to SPSS, Excel to Stata)
- Deduplication
- Subsetting / filtering

*Qualitative:*
- Anonymisation / pseudonymisation (e.g. replacing names, locations)
- Transcription (initial conversion from audio/video to text)
- Translation (language conversion — note source and target language)
- Transcript cleaning (e.g. removing filler words, correcting errors)
- Segmentation / chunking (e.g. splitting by speaker, topic, or time)
- Format conversion (e.g. audio to transcript, handwritten notes to digital)
- Document redaction (e.g. removing identifying information)
- Merging materials (e.g. combining interview notes and transcripts)

---

## Section C — Anonymisation & Pseudonymisation Record

*Complete this section for any data containing personal or sensitive information.*

| Entry # | Date | Data subject type | Information removed or substituted | Substitution method | Key stored separately? | Performed by |
|---|---|---|---|---|---|---|
| | | e.g. Interview participant | Full name → Participant code | Sequential code (P01, P02…) | ☐ Yes  ☐ No | |
| | | | | | ☐ Yes  ☐ No | |

> **Note:** If a re-identification key exists, store it in a separate, access-controlled location and document its location here (without reproducing it): _______________________

---

## Section D — Quality Checks

Record any checks performed to verify that transformations were applied correctly.

| Entry # | Date | Check performed | Method | Outcome | Performed by |
|---|---|---|---|---|---|
| | | e.g. Verified recoded variable against original | Frequency table cross-check | No discrepancies found | |
| | | | | | |

---

## Section E — Known Issues & Decisions

Use this section to flag unresolved issues, ambiguous decisions, or deviations from the original plan.

| # | Date | Issue or decision | Action taken | Outstanding? |
|---|---|---|---|---|
| | | | | ☐ Yes  ☐ No |
| | | | | ☐ Yes  ☐ No |

---

## Section F — Sign-off

| Role | Name | Signature | Date |
|---|---|---|---|
| Researcher | | | |
| Project lead (if applicable) | | | |

---

*This template is part of the CMI Research Data Management Manual. For guidance on processing stages, see the **Process** page of the lifecycle guide. For file format recommendations, see the **Preservation-Ready Formats Guide**.*