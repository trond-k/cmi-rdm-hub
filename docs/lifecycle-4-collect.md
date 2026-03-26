---
icon: lucide/database
title: "COLLECT"
description: "Gather data carefully: test your instruments, document as you go, and protect participants from the first recording onward."
tags:
  - Collect
  - Fieldwork
  - Quality
  - Ethics
  - Data inventory
notes: ""
date_updated: 2026-03-26
---

# COLLECT: data gathering

*Data quality is determined at the point of collection. Errors introduced here are the hardest to fix later, and ethical failures cannot be undone at all. Invest in protocols, pilot testing, and real-time documentation. The decisions you made at the [FRAME](frame.md), [FUND](fund.md), and [PLAN](plan.md) stages now meet reality.*

## Instruments and protocols

Whether you are conducting interviews, running a household survey, recording observations, or collecting biological samples, the quality of your data depends on the quality of the instruments and protocols that produce it.

Design your instruments with downstream use in mind. Interview guides should include consistent identifiers that link to your [file naming convention](file-and-folder-naming.md). Survey instruments should use validated scales where available and define variables precisely enough that a codebook can be generated directly from them. Observation schedules should specify what counts as an instance of the behaviour or event you are recording.

!!! tip "Pilot everything"
    Test instruments, protocols, and workflows before full-scale collection. A pilot reveals ambiguous questions, technical failures, unrealistic time estimates, and gaps in your documentation plan. It is far cheaper to discover that your recording equipment cannot handle background noise, or that a survey question is consistently misunderstood, before you are in the field with fifty participants scheduled.

For multi-site projects, harmonisation matters. If different teams are collecting data in different locations, agree on shared instruments, coding schemes, and quality thresholds before collection begins. Minor variations in question wording, response categories, or data entry conventions can make datasets incomparable. Document any site-specific adaptations and the reasons for them.

## Ethical conduct in the field

The ethical commitments in your participant information sheets are tested in practice during collection. Power dynamics, cultural context, and the unpredictability of fieldwork create situations that no protocol can fully anticipate.

Be attentive to coercion risks, even subtle ones. In contexts where the researcher is associated with authority, funding, or institutional power, participation may not feel genuinely voluntary. In conflict-affected or authoritarian settings, the act of being seen to participate in research can itself carry risk. Consider how and where interviews take place, who might observe participation, and whether the research context could change in ways that put participants in danger.

Have a plan for participant distress. Interviews about displacement, violence, corruption, or personal hardship can be emotionally difficult. Know in advance how you will respond if a participant becomes distressed, and what referral options exist locally.

!!! warning "Sensitivity can emerge during collection"
    You may discover during fieldwork that data is more sensitive than anticipated: a participant reveals information that changes the risk profile, a political situation shifts, or contextual details make someone identifiable in ways you did not foresee. When this happens, revisit your sensitivity classifications and update the [data inventory](data-inventory.md). Do not wait until the project ends to address it.

## Equipment and tools

Choose tools that support your data management commitments, not just your immediate collection needs.

For mobile data collection, platforms such as [KoBoToolbox](https://www.kobotoolbox.org/), [ODK](https://getodk.org/), and [REDCap](https://www.project-redcap.org/) offer structured data entry with built-in validation, skip logic, and offline capability. They produce consistently formatted outputs that are easier to clean and analyse than manually entered data.

For audio and video recording, consider file size, format, and how recordings will be transferred and stored securely. Recording in an open format (such as WAV or FLAC for audio) avoids format conversion later, but produces larger files. Encrypted recorders or encrypted transfer from recording devices add a layer of protection for sensitive interviews.

For document and archival collection, establish a consistent system for tracking provenance: where each document came from, when it was obtained, under what terms, and any access restrictions that apply.

!!! tip "Test the full chain, not just the tool"
    It is not enough to know that your survey app works. Test the complete workflow: data entry in the field, transfer to secure storage, backup, and export into your analysis environment. If any link in that chain fails or loses data, you need to know before collection starts.

## Secondary and external data

Not all data collection involves fieldwork. Your project may acquire existing datasets, administrative records, policy documents, licensed databases, or materials from archives and online sources.

For secondary data, document the source, the date of acquisition, the version (if applicable), and the terms under which you obtained it. If the data came from a repository, record the persistent identifier. If it came from a government agency or partner institution, record the agreement or correspondence that authorised access. If you are scraping web content or using APIs, document the query parameters, the date of extraction, and any terms of service that apply.

The same standards of documentation apply whether you collected the data yourself or acquired it from someone else. A dataset whose provenance is unclear is a liability, not an asset.

## Document as you go

Field documentation is the layer of context that makes raw data interpretable. Without it, a recording is just audio; a spreadsheet is just numbers. The time to capture this context is at the point of collection, not weeks later from memory.

For each data collection event, record at minimum:

- Who collected the data, when, and where.
- What instrument or protocol was used, and which version.
- Any deviations from the planned protocol and the reasons for them.
- Contextual information that affects interpretation: interruptions, environmental conditions, the participant's apparent comfort or discomfort, translation issues, technical problems.

Field notes, interview logs, and collection diaries serve this purpose. They do not need to be literary; they need to be specific and contemporaneous. Link them to the corresponding data files using the shared identifiers from your [naming convention](file-and-folder-naming.md).

??? example "What a field documentation entry looks like"
    ```text
    Date: 2025-03-12
    Site: Kumasi (KUM)
    Participant: P012
    Instrument: GOVTRUST semi-structured interview guide v02
    Interviewer: TK
    Duration: 48 min
    Language: English with occasional Twi (not translated in real time)
    Files: GOVTRUST_KUM_interview_P012_2025-03-12_audio.wav
           GOVTRUST_KUM_interview_P012_2025-03-12_fieldnotes.md

    Notes: Interview conducted at participant's workplace (private office,
    door closed). Participant initially hesitant to discuss local government
    procurement — became more forthcoming after recorder was briefly paused
    at their request. Two passages in Twi will need translation before
    transcription. Audio quality good throughout.
    ```

## Quality control during collection

Do not wait until processing to check data quality. Build verification into the collection workflow itself:

- **Structured data.** Use validation rules, range checks, and skip logic in your survey instruments. Review incoming data regularly for patterns that suggest misunderstanding, fabrication, or systematic error. If you are running a multi-enumerator survey, compare data across enumerators early enough to catch problems.
- **Qualitative data.** Spot-check recordings and transcripts as they come in. Are recordings audible? Are identifiers consistently applied? Are field notes being completed the same day? Early feedback to field teams prevents small problems from compounding.
- **Multi-site consistency.** If data is being collected at multiple sites, compare early batches to check that instruments are being applied consistently and that site-specific adaptations have not introduced incompatibilities.

!!! tip "Fix problems in the field, not at your desk"
    If quality checks reveal a problem, the cheapest time to fix it is now, while you still have access to participants, field sites, and collection teams. A question that is consistently misunderstood can be reworded. A recording device that clips audio can be replaced. An enumerator who is skipping validation steps can be retrained. None of these are possible six months later.

## AI-assisted collection

Tools that use speech recognition, natural language processing, or machine translation are increasingly part of data collection workflows. Automated transcription services can produce a first draft of an interview transcript within hours. Translation tools can help researchers work across languages they do not speak fluently. Classification tools can assist with sorting and tagging large volumes of text or image data.

Use these tools, but document them. Record which tool or service was used, the version or model, the date, and any settings or parameters. Note known limitations: automated transcription handles some accents and languages better than others; machine translation can distort meaning in context-dependent ways. Treat AI-assisted outputs as drafts that require human review, not as finished products. For more on documenting AI use in research, see [Reproducibility and transparency](reproducibility-and-transparency.md).

## Update the data inventory

As data comes in, the [data inventory](data-inventory.md) shifts from planned to actual. Update it with each dataset as it is created: record collection dates, actual formats and volumes, source details, and any deviations from what was anticipated. If new datasets emerge that were not planned (as often happens in qualitative and mixed-methods research), add them. If sensitivity classifications need revising, revise them. The inventory should reflect what you have, not what you expected to have.