---
icon: lucide/arrow-right-left
title: "PROCESS"
description: "Transform raw data into analysis-ready form: clean, convert, pseudonymise, and document every step so the chain from source to result is traceable."
tags:
  - Process
  - Quality
  - Pseudonymisation
  - Documentation
  - Reproducibility
notes: ""
date_updated: 2026-03-26
---

# PROCESS: data transformation

*Processing is the bridge between raw collection and analysis-ready data. It includes cleaning, transcription, format conversion, pseudonymisation, coding, and integration. Every transformation you apply must be documented; if a step cannot be traced, the resulting data cannot be trusted. The goal is not just a tidy dataset but a clear chain of provenance from source to final form.*

## Clean and assess quality

Raw data almost always needs work before it can be analysed. Survey responses contain entry errors, missing values, and inconsistencies. Interview recordings vary in audio quality. Administrative records use coding schemes that do not match your variables. Cleaning is the process of identifying and addressing these problems systematically.

Start with an assessment of what you have. For quantitative data, check completeness (how many missing values, and are they random or patterned?), accuracy (do values fall within plausible ranges?), consistency (do related variables agree with each other?), and duplication (are there records that appear more than once?). For qualitative data, the equivalent questions concern audibility, transcription accuracy, and whether identifiers and labels have been applied consistently.

Document every cleaning decision. If you remove outliers, record which values were removed and why. If you impute missing data, record the method. If you recode a variable, record the mapping from old to new values. A processing log or script that captures these decisions is not optional; it is what makes the difference between a dataset that others can scrutinise and one they must take on faith.

!!! warning "Never overwrite raw data"
    Save cleaned outputs in your `processed/` folder and leave the originals in `raw/` untouched. See [Name files and structure folders](file-and-folder-naming.md). If you discover an error in your cleaning logic, you need to be able to go back to the source and start again. Once raw data is overwritten, that option is gone.

## Pseudonymise and protect

If your data contains personal information, processing is where pseudonymisation happens. Pseudonymisation replaces direct identifiers (names, ID numbers, contact details) with codes, while keeping a separate key file that links the codes back to the originals. This reduces the risk of identification if the research data are accessed without authorisation, but it does not eliminate it.

The distinction between pseudonymisation and anonymisation matters. Pseudonymised data is still personal data under the GDPR, because re-identification remains possible through the key file. Truly anonymised data, where re-identification is no longer reasonably possible, falls outside the GDPR's scope, but achieving genuine anonymisation is harder than it sounds. Contextual details in qualitative data, small population sizes, unusual combinations of variables, and geospatial precision can all make participants identifiable even after direct identifiers are removed.

!!! tip "Think about identifiability, not just identifiers"
    Removing names and ID numbers is necessary but often not sufficient. A description of a specific role in a small organisation, a distinctive combination of age, profession, and location, or a recognisable narrative in a life history can identify someone just as effectively. Consider what someone with local knowledge could infer from the data, not just what a stranger could read directly.

For practical guidance on techniques (generalisation, suppression, aggregation) and on assessing re-identification risk, see the pseudonymisation and anonymisation decision guide (forthcoming).

## Transcribe and digitise

Many CMI projects work with audio recordings, handwritten field notes, or physical documents that need to be converted into machine-readable text before they can be analysed.

For interview and focus group recordings, you have a choice between manual transcription and automated tools. Manual transcription is slower but produces higher accuracy, especially for recordings with background noise, overlapping speakers, multiple languages, or dialect variation. Automated transcription services (such as [Whisper](https://openai.com/index/whisper/)) can generate a first draft quickly, but the output should always be reviewed and corrected by someone who knows the language and context. Speaker identification, non-verbal cues, and contextual notes typically require human attention regardless of the method used.

For physical documents, scanning followed by Optical Character Recognition (OCR) converts images to searchable text. OCR accuracy varies with document quality, script, and language; check a sample before processing a large batch.

Whichever method you use, record it. Note the tool or service, the version, the date, any settings or parameters, and the extent of human review applied. If you used an automated tool, note its known limitations for your data (e.g., lower accuracy for specific languages or accents). This documentation matters both for reproducibility and for transparency about how the data were produced. See [Reproducibility and transparency](reproducibility-and-transparency.md) for broader guidance on documenting AI-assisted workflows.

## Convert formats and structure data

The formats in which data arrive are not always the formats in which they should be analysed or preserved. Proprietary formats risk lock-in; inconsistently structured files resist systematic analysis. Processing is the stage to address both.

Where possible, convert proprietary formats to open ones: SPSS or Stata files to CSV, Word documents to plain text or Markdown, proprietary audio to WAV or FLAC. This is not about ideological purity; it is about ensuring that your data remain readable regardless of which software licences your institution holds in five years' time. When conversion involves any loss of information (formatting, variable labels, embedded metadata), document what was lost and keep the original.

For tabular data, structuring means making the data consistently machine-readable. Each variable should occupy one column, each observation one row, and each value one cell. Consistent variable names, explicit coding of missing values, and clear documentation of units and categories all belong at this stage. If you are combining data from multiple collection rounds or sites, harmonise variable names and coding schemes now rather than patching them during analysis.

## Code and classify

Qualitative data processing typically involves coding: assigning labels or categories to segments of text, audio, or visual material. Whether you are doing initial open coding, applying a pre-existing thematic framework, or working with a structured taxonomy, the processing stage is where you develop and apply the coding scheme.

Document the codebook as you go. For each code, record a definition, inclusion and exclusion criteria, and at least one example. If codes evolve during the process (as they do in most inductive approaches), version the codebook so you can trace how your categories developed. This documentation is essential both for your own analytical rigour and for anyone who might later need to understand how your coded data relates to the source material.

For quantitative data, the equivalent task is variable recoding and classification: collapsing categories, deriving new variables, or applying standard taxonomies. The same principle applies: document every transformation, and keep the mapping between original and recoded values explicit.

## Integrate and link datasets

Projects that draw on multiple data sources often need to combine them during processing. This might mean linking survey responses to administrative records, merging datasets collected at different sites, or combining qualitative and quantitative data around shared case identifiers.

Data integration introduces its own risks. Matching errors (linking records that do not belong together) and harmonisation failures (assuming that variables with the same name measure the same thing across sources) can corrupt your analysis without being obvious. Where you are linking datasets that contain personal information, the linkage itself can increase identifiability; two datasets that are individually safe may become identifying when combined.

Document the linkage method, the matching variables, the match rate, and how you handled non-matches. If the integration involves personal data, ensure the process is covered by your GDPR compliance arrangements and reflected in the [data inventory](data-inventory.md).

## Make processing reproducible

The gold standard for processing is a scripted workflow: a set of R, Python, or shell scripts that take raw inputs and produce analysis-ready outputs without manual intervention. If your processing can be re-run from scratch and produce the same result, it is reproducible. If it depends on steps that someone performed by hand in a spreadsheet, it is not.

Not every project can achieve full scripted reproducibility, and that is fine. Qualitative coding, for instance, involves interpretive judgement that cannot be reduced to a script. But even where manual steps are unavoidable, they can be documented. A processing log that records what was done, in what order, by whom, and with what tools is the minimum. For scripted steps, version your code in Git and record the software environment (R version, Python packages, operating system) so that someone can reconstruct your setup.

!!! tip "Start the processing log on day one"
    A processing log does not need to be elaborate. A dated list of what you did and why, kept in a text file alongside your data, is vastly better than relying on memory. If you wait until the end of the project to reconstruct your processing steps, you will forget things that matter.

??? example "What a processing log entry looks like"
    ```text
    Date: 2025-04-15
    Dataset: GOVTRUST_KUM_survey_raw.csv
    Action: Removed 12 duplicate records (identical respondent ID and
            timestamp). Duplicates appear to result from double submission
            via KoBoToolbox; confirmed by checking submission logs.
    Output: GOVTRUST_KUM_survey_deduped.csv
    Script: scripts/01_dedup_survey.R (commit 3fa82b1)
    Person: TK
    ```

## Update the data inventory

As you process data, the [data inventory](data-inventory.md) should reflect the new state of affairs. Record which datasets have been cleaned, what derived datasets have been created, and where processed versions are stored. If processing revealed new sensitivities (e.g., a transcript turned out to contain information that changes the risk profile), update the sensitivity classification. The inventory should always describe what you have now, not what you had at the start of the project.