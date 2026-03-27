---
icon: lucide/archive
title: "PRESERVE"
description: "Ensure your data remains intact, interpretable, and accessible long after the project ends: choose sustainable formats, plan retention, and let trustworthy archives do the heavy lifting."
tags:
  - Preserve
  - Archiving
  - Formats
  - Retention
  - FAIR
notes: ""
date_updated: 2026-03-26
---

# PRESERVE: long-term data preservation

*Preservation is what keeps data usable after the project team has moved on. The good news is that trustworthy archives handle most of the technical work: format migration, integrity checks, and metadata curation. Your job is to choose the right archive (see the [PUBLISH](lifecycle-8-publish.md) stage), provide well-documented data in sustainable formats, and make deliberate decisions about what to keep, for how long, and what to destroy.*

## What the archive does for you

If you deposit your data in a trustworthy, certified archive such as the [Sikt Research Data Archive](https://sikt.no/en/tjenester/arkivering-av-forskningsdata), much of what people think of as 'preservation' is handled by the infrastructure. The archive assigns persistent identifiers, curates metadata, performs integrity checks (checksums, fixity verification), migrates formats when they become obsolete, and ensures that the data remains accessible as technology changes. This is what distinguishes an archive from a file share or a personal hard drive.

Understanding this division of labour matters because it tells you where to focus your effort. You do not need to become an expert in digital preservation standards. You need to provide data that is clean, well-documented, and in formats the archive can work with. The archive takes it from there.

!!! tip "Choose the archive before you worry about preservation"
    Most preservation decisions follow from the choice of archive. If you have not yet decided where to deposit, start with the [PUBLISH](lifecycle-8-publish.md) stage. The archive's deposit guidelines will tell you what formats it accepts, what metadata it requires, and what it will do with your data over time.

## Use sustainable formats

The most common threat to long-term data usability is not hardware failure or institutional collapse. It is format obsolescence. A dataset stored in a proprietary format that depends on software no longer available is effectively lost, even if the file itself is intact.

The principle is straightforward: prefer open, widely adopted, non-proprietary formats. For most CMI research data, this means:

| Data type | Preferred formats | Avoid |
|---|---|---|
| Tabular data | CSV, TSV (with an accompanying codebook) | Excel (.xlsx) as the sole format, SPSS (.sav), Stata (.dta) without CSV export |
| Text | Plain text (.txt), Markdown, PDF/A, ODF | Word (.docx) as the sole archival format |
| Audio | WAV, FLAC | Compressed proprietary formats (WMA) |
| Video | MPEG-4 (H.264), FFV1 (lossless) | Proprietary container formats |
| Images | TIFF (archival), PNG, JPEG | RAW formats without a converted copy |
| Geospatial | GeoJSON, GeoTIFF, Shapefile | Proprietary GIS project files as the sole format |

This does not mean you cannot work in Stata or SPSS during the project. It means that when you deposit, you also provide a format-neutral export. A CSV alongside the Stata file costs almost nothing to produce and ensures the data remains readable regardless of which software licences exist in twenty years.

!!! warning "Conversion can lose information"
    When you export from a proprietary format to an open one, check what survives. Stata and SPSS files carry variable labels, value labels, and missing-value codes that a plain CSV does not. If these are important (and they usually are), include them in the codebook or a separate data dictionary. The open format preserves the data; the documentation preserves the meaning.

## Preservation metadata

Metadata is what makes a file interpretable rather than merely accessible. At the point of deposit, the archive will ask you to provide descriptive metadata (what the data is, who created it, when, under what conditions) and may apply its own preservation metadata (technical format details, provenance records, fixity information).

Your contribution is the descriptive layer. Much of this should already exist if you have maintained a [data inventory](data-inventory.md) and documented your work through the [PROCESS](lifecycle-6-process.md) and [ANALYSE](lifecycle-7-analyse.md) stages. At deposit, check that the metadata you provide is accurate, complete, and consistent with the documentation accompanying the data. The metadata standards used depend on the archive and the discipline; common frameworks include DataCite, Dublin Core, and DDI (Data Documentation Initiative) for social science data.

## Retention and destruction

Not all data should be kept indefinitely. Retention decisions are shaped by legal obligations, funder requirements, institutional policy, and the commitments you made to participants.

**Legal minimums.** The GDPR requires that personal data be kept no longer than necessary for the purpose of processing. For research, this means identifiable data should be anonymised or deleted once the research purpose is fulfilled, unless a specific legal basis permits longer retention. See [GDPR and legal compliance](CROSS-gdpr-and-legal-compliance.md).

**Funder requirements.** Most funders specify minimum retention periods. The Research Council of Norway and Horizon Europe typically expect data to be preserved for at least ten years after the end of the project, though the specific requirement varies by call. Check your grant agreement.

**Participant commitments.** If your information letter promised participants that their data would be deleted after a specific date or event, you are bound by that promise. This is one reason to draft information letters carefully at the [PLAN](lifecycle-3-plan.md) stage; overly narrow retention promises can prevent you from archiving data that would otherwise have long-term value.

When data must be destroyed, do it properly. For digital files, secure deletion means overwriting, not just moving to the recycle bin. For data held by an archive under embargo, confirm the destruction procedure with the archive. Document when destruction took place, what was destroyed, and by whom. A certificate of destruction (even a brief internal record) closes the loop and demonstrates compliance.

!!! tip "Decide retention early, not at the end"
    Retention periods should be specified in the DMP and the [data inventory](data-inventory.md) during the [PLAN](lifecycle-3-plan.md) stage, not improvised when the project winds down. If retention planning is left to the end, researchers face pressure to keep everything (creating GDPR risk) or delete everything (losing research value).

## Dark archiving

Some data cannot be shared openly but must still be preserved. Sensitive interview transcripts under long-term embargo, datasets with unresolvable re-identification risks, and materials subject to contractual restrictions all fall into this category.

Dark archiving means depositing data in a secure environment where it is preserved and integrity-checked but not accessible to the public. The metadata remains discoverable (so that others know the data exists and can request access under defined conditions), while the data itself is withheld. This approach satisfies the FAIR principle that metadata should always be open, even when the data is not.

The Sikt Research Data Archive supports restricted and embargoed deposits. For data with especially high sensitivity, discuss the options with Sikt or with the RDM contact (rdm@cmi.no) before deposit. The key question is not whether to preserve the data, but under what conditions and for how long.

## Who pays for preservation

Long-term preservation costs money, even when the per-dataset cost is modest. Storage, integrity monitoring, format migration, and metadata curation are ongoing activities. For data deposited in publicly funded archives such as Sikt, these costs are covered by the archive's institutional funding. For data deposited elsewhere, check whether the archive charges deposit or maintenance fees and whether your funder permits these as eligible costs.

If your project generates data that requires long-term preservation beyond what a standard archive provides (e.g., very large datasets, highly specialised formats, or data requiring active curation), factor this into the budget at the [FUND](lifecycle-2-fund.md) stage. Preservation that is not funded is preservation that depends on goodwill, and goodwill has a shorter shelf life than research data.

## Close the inventory loop

The [data inventory](data-inventory.md) should now document the full chain for each dataset: where it was preserved, under what access conditions, for how long, and with what persistent identifiers. For destroyed data, record the date and method. This record demonstrates compliance with the GDPR, funder mandates, and commitments to participants.