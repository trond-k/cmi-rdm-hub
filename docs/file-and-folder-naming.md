---
icon: lucide/folder-tree
title: "Name files and structure folders"
description: "Agree on a simple naming pattern and folder layout before the project drifts into confusion."
tags:
  - Documentation
  - Storage
  - Organisation
notes: ""
date_updated: 2026-03-25
---

# Name files and structure folders

*Agree on a simple naming pattern and folder layout before the project drifts into confusion. The two most common causes of lost or duplicated research files are inconsistent names and missing version information. Fix both early, document the convention once, and the whole team can find what they need without guessing.*

## Start with one naming pattern

Choose a single convention and use it from the first day of data collection. For most CMI projects, a good default is:

```text
[project]_[site]_[datatype]_[identifier]_[date]_v[version].ext
```

For example:

```text
GOVTRUST_KUM_interview_P012_2025-03-12_v01.docx
```

That gives you five things at a glance: project, location, type, case, and version. Not every file needs all five elements. A project with a single site can drop the site code; a dataset with no meaningful version history can drop the version number. The point is to decide which elements matter for your project and apply them consistently.

!!! tip "Agree on codes before collection starts"
    Write down the project code, site abbreviations, and any participant or sample identifiers before fieldwork begins. If different team members invent their own shorthand, you will spend hours reconciling files later.

## Keep names sortable

A few mechanical rules make file names sort predictably across operating systems and file browsers:

- Use ISO dates: `YYYY-MM-DD` (so `2025-03-12` sorts before `2025-04-01`).
- Use only letters, numbers, underscores, and hyphens.
- Use leading zeros for numbered sequences: `01`, `02`, ... `12`.
- Never use spaces, dots (other than the file extension), or special characters such as `& ? ! # %`.
- Keep names under 40–50 characters where possible.[^1] Long names get truncated in file browsers and cause problems on some systems.

If you cannot sort and recognise files without opening them, the naming scheme is not doing its job.

???+ example "Common naming mistakes and how to fix them"
    Most of these will look familiar. The left column is what happens when people name files in a hurry; the right column shows what a consistent convention produces instead.

    | Instead of | Try |
    |---|---|
    | `data-1.xlsx` | `GOVTRUST_KUM_survey_01.xlsx` |
    | `interviews.docx` | `GOVTRUST_KUM_interview_P003_2025-03-12_v01.docx` |
    | `Data_NEW(2).csv` | `GOVTRUST_ACC_survey_cleaned_2025-04-01_v02.csv` |
    | `draft.docx` | `GOVTRUST_report_v01.docx` |
    | `final version.docx` | `GOVTRUST_report_v03.docx` |
    | `FINAL-final-revised_TK.docx` | `GOVTRUST_report_v04_2025-06-10_TK.docx` |
    | `Maria's stuff/notes.txt` | `analysis/fieldnotes_KUM_2025-03-14.md` |
    | `Copy of Copy of budget.xlsx` | `GOVTRUST_budget_v03.xlsx` |

    The names on the right are longer, but they tell you what the file is without opening it, they sort predictably, and they still make sense six months later.

## Connect related files with a shared identifier

In qualitative and mixed-methods research, a single data collection event often produces several files: an audio recording, a transcript, field notes, and photographs. Give all files from the same event the same identifier so they stay together:[^2]

```text
GOVTRUST_KUM_interview_P012_2025-03-12_audio.wav
GOVTRUST_KUM_interview_P012_2025-03-12_transcript_v01.docx
GOVTRUST_KUM_interview_P012_2025-03-12_fieldnotes.md
```

This makes it straightforward to find everything connected to one interview, one focus group, or one observation session, even when files are stored in different subfolders by type.

## Track versions in the file name

Use numbered versions: `v01`, `v02`, `v03`. For minor revisions, extend the number: `v01_01`, `v01_02`.[^3] When sharing drafts with colleagues, you can append initials and the date: `report_v02_2025-04-10_TK.docx`.

Never use `final`, `final2`, `FINAL_revised`, or similar labels. They lose all meaning the moment someone makes another change, and they do not sort reliably.

!!! warning "Do not confuse versioning with backup"
    Version numbers in file names track deliberate revisions to a document. They are not a substitute for regular backups or for the change history that a version control system like Git provides. If your project involves code or scripts, consider using Git alongside your file naming convention.

## Separate raw data from everything else

Folder structure matters as much as file names. The most durable organising principle is to keep raw source material physically separate from anything derived from it:

- `raw/` for untouched source files (recordings, survey exports, and scanned documents)
- `processed/` for cleaned, transcribed, or transformed versions
- `analysis/` for working files, scripts, or coding outputs
- `outputs/` for tables, figures, drafts, and deliverables

Do not edit raw files in place. If you need to correct or transform something, save the result in `processed/` and leave the original intact. This protects the chain of evidence and makes it possible to retrace your steps if something goes wrong downstream.

## Keep the folder tree shallow

Most projects do not need a deep hierarchy. If someone has to click through six levels to reach an interview transcript, the structure is working against them. Three or four levels is usually enough:[^4]

```text
GOVTRUST/
├── raw/
│   ├── interviews/
│   └── survey/
├── processed/
│   ├── transcripts/
│   └── survey_cleaned/
├── analysis/
└── outputs/
```

Name folders after project content (interviews, survey, fieldwork photos), not after the person currently using them. A folder called `Maria's stuff` tells nobody anything once Maria has moved on.

## Document the pattern once

Put a short `README.txt` or `README.md` at the top of the project folder. It should describe:

- the naming pattern, with one or two examples
- any project codes, site codes, or participant identifier schemes
- the meaning of version labels
- where raw, processed, and final outputs live

If a new team member cannot understand the folder structure from the README alone, the README is missing something.

??? example "A minimal project README"
    ```text
    PROJECT: GOVTRUST
    Naming pattern: [project]_[site]_[datatype]_[ID]_[YYYY-MM-DD]_v[NN].ext

    Site codes:
      KUM = Kumasi
      ACC = Accra

    Participant IDs: P001–P050 (assigned in order of recruitment)

    Folder structure:
      raw/         — untouched source files; do not edit
      processed/   — cleaned and transcribed versions
      analysis/    — scripts, coding frameworks, working notes
      outputs/     — tables, figures, report drafts

    Versions: v01, v02, etc. Minor revisions: v01_01, v01_02.
    ```

## Set this up early

Establishing a convention is easiest before data collection begins, but it still pays off mid-project. Retrofitting a naming scheme is tedious, but less tedious than continuing without one. If you are renaming a large batch of existing files, tools such as Ant Renamer (Windows), Renamer (macOS), or the `rename` command (Linux) can handle bulk operations without manual file-by-file editing.

[^1]: Harvard Biomedical Data Management. 'File Naming Conventions'. Available at [datamanagement.hms.harvard.edu](https://datamanagement.hms.harvard.edu/plan-design/file-naming-conventions).

[^2]: CESSDA Data Management Expert Guide. 'File Naming and Folder Structure'. Available at [dmeg.cessda.eu](https://dmeg.cessda.eu/Data-Management-Expert-Guide/2.-Organise-Document/File-naming-and-folder-structure).

[^3]: University of Cambridge Research Data Management. 'File Organisation, Naming and Version Control'. Available at [data.cam.ac.uk](https://www.data.cam.ac.uk/organising-storing/file-organisation-naming-version-control).

[^4]: Harvard Biomedical Data Management. 'Directory Structure'. Available at [datamanagement.hms.harvard.edu](https://datamanagement.hms.harvard.edu/plan-design/directory-structure).
