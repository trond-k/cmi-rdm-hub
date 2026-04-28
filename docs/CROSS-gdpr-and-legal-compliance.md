---
icon: lucide/shield-check
title: "GDPR for your project"
description: "What to do about GDPR if your project involves people: lawful basis, the two consents, cross-border data, DPIAs, and participant requests."
tags:
  - GDPR
  - Legal compliance
  - Data protection
  - Cross-cutting
notes: ""
date_updated: 2026-04-28
---

# GDPR for your project

*If your project involves people, the GDPR applies. This page covers the practical decisions: choosing your lawful basis, ethical consent and what to inform participants about, handling cross-border data, deciding when a DPIA is needed, and responding to participant requests. Use it alongside the [Sikt notification](sikt-notification.md), the [DMP template](dmp-cmi.md), and [GDPR concepts for researchers](CROSS-legal.md) for terminology.*

## What you need to do

For most CMI projects involving personal data, the work breaks down into seven steps:

1. **Confirm whether you process personal data.** Use the [personal data decider](personal-data-decider.md). If unsure, treat the data as personal until you can show otherwise.
2. **Choose your lawful basis.** The CMI default is public interest. See below.
3. **Write the information letter.** This is the primary instrument for participants. See [Informed consent and information letters](CROSS-ethics.md).
4. **File the Sikt notification** at least 30 days before data collection. See [Prepare a Sikt notification](sikt-notification.md) and the [Sikt form walkthrough](sikt-form-walkthrough.md).
5. **Set storage to match data sensitivity.** See [Data classification](data-classification.md).
6. **Plan cross-border arrangements** when collecting or sharing data outside the EEA. See below.
7. **Know how to respond to participant requests.** See the rights table at the end of this page.

The interpretive choices behind these steps are summarised in the sections that follow; collapsible asides give the reasoning if you want it.

## Lawful basis: public interest

The CMI default lawful basis is **public interest (GDPR Art. 6(1)(e))**, supported by the Norwegian Personal Data Act §8 and the research-specific provisions in GDPR Art. 89. It applies across the full range of CMI research involving personal data: qualitative, quantitative, mixed methods, interviews, surveys, ethnography, register studies, and evaluations. It is not limited to large-scale or registry-based work.

For **special category data** under Art. 9 (racial or ethnic origin, political opinions, religious or philosophical beliefs, trade union membership, genetic data, biometric data, health data, data about sex life or sexual orientation), use the additional basis in **Art. 9(2)(j)** for scientific research purposes with appropriate safeguards under Art. 89(1). The Norwegian Personal Data Act §9 provides the national implementation.

GDPR consent (Art. 6(1)(a)) is **not** the lawful basis for general processing. Topics sometimes treated as requiring consent, such as recording, name use in publications, and archiving for reuse, are matters to inform participants about in the information letter. They are not GDPR consent elements layered on top of public interest.

??? note "Why not consent as the lawful basis?"
    Using GDPR consent as the primary lawful basis for research creates several practical problems:

    - **Withdrawal instability.** If consent is the lawful basis, a participant who withdraws triggers a legal obligation to delete their data. In a project running for two years, where that data is woven into analytical frameworks, deletion can seriously impair the research. Under the public interest basis, the right to erasure is limited by Art. 17(3)(d).
    - **Specificity requirements.** GDPR consent must be specific to defined processing purposes. Qualitative and ethnographic research is inherently exploratory, and the scope of relevant data often cannot be fully specified in advance.
    - **Conflation with ethical consent.** Bundling GDPR consent into the same form as ethical consent confuses two different things and produces forms that are simultaneously too detailed and too vague.
    - **False sense of control.** In fieldwork with vulnerable populations, in conflict zones, or where power imbalances are real, the 'freely given' requirement of GDPR consent is difficult to establish with certainty.

## Ethical consent and participant information

Ethical consent is separate from the GDPR lawful basis, and it is always required when research involves human participants, regardless of which lawful basis applies. The information letter is the primary instrument: it informs participants and asks them to agree to take part.

**Ethical consent** is the obligation, rooted in research ethics and the NESH guidelines, to ensure participation is voluntary, informed, and revocable. See [Informed consent and information letters](CROSS-ethics.md) for letter mechanics.

**What the letter must inform participants about.** The letter must cover whatever the participant needs to understand the project and their role in it. For most CMI projects this includes:

- the purpose of the research;
- that the interview will be recorded, filmed, or photographed, where applicable;
- whether and how the participant may be identified or named in publications;
- how data will be stored and for how long;
- whether and where data may be archived for future reuse;
- how rights such as access, correction, and erasure can be exercised;
- whom to contact with questions.

Where the participant has a meaningful choice (for example, whether to be recorded, whether to be named, or whether their data may be archived for reuse), offer it as a project decision they make in the letter, not as a separate "GDPR consent" element layered on top of public interest.

## Data minimisation

Data minimisation (Art. 5(1)(c)) requires that personal data be adequate, relevant, and limited to what is necessary for the research purpose. In practice: collect with intention, do not gather data you do not need, and do not keep identifiable data longer than necessary. This does not mean restricting qualitative collection to a pre-approved script. Open-ended interviewing is compatible with minimisation if you are clear about what serves the research.

## Cross-border data

CMI researchers routinely collect data outside the EEA, in countries that lack EU adequacy decisions. Match the safeguard to the actual data flow:

- **Fieldwork data collection.** A CMI researcher collecting data on an encrypted device abroad and uploading to CMI storage in Norway needs practical safeguards (device encryption, secure upload, password protection), not Standard Contractual Clauses. The data never leaves the controller's operations.
- **Local research assistants.** When a research assistant works under CMI's instruction, they are part of the controller's operations. Clear data handling instructions, encrypted devices, and a confidentiality clause in their contract are sufficient.
- **Partner institutions.** For genuine research collaborations, a joint controllership agreement (Art. 26) is often the right fit. The research derogation (Art. 49(1)(d)) is a further option for transfers necessary for scientific research in the public interest.
- **Cloud services and digital tools.** A standard data processing agreement from the service provider is typically sufficient. Prefer tools that offer EEA-based or Swiss-based processing where available.

## When a DPIA is needed

A DPIA is required under Art. 35 when processing is likely to result in a high risk to data subjects. Most CMI projects with a small number of qualitative interviews will not trigger one. A multi-country survey with thousands of respondents on sensitive topics likely will. Contact rdm@cmi.no early if you are unsure; the assessment is easier to do alongside Sikt preparation than retroactively.

??? example "When a DPIA is recommended"
    Consider a DPIA when two or more of the following apply: large-scale processing of personal data; systematic evaluation or profiling; processing of special category data in sensitive contexts; processing data on vulnerable groups; or combining datasets from different sources. A DPIA documents the nature and purpose of the processing, the risks to data subjects, and the measures in place to mitigate those risks. It is an internal assessment, not a regulatory submission.

## Participant requests

Under the public interest basis, data subject rights are modified by Art. 89(2) and the Norwegian Personal Data Act §17. The information letter should describe these rights clearly but concisely. Most participants will not exercise them, but you should know how to respond if asked.

| Right | Status under public interest basis |
|---|---|
| Information | Fully applies (provided through the information letter). |
| Access | Applies (provide transcript or relevant records on request). |
| Rectification | Applies (correct factual errors on request). |
| Erasure | Limited under Art. 17(3)(d): may be refused if deletion would seriously impair the research. The default is to accommodate deletion requests unless there is a compelling, documented reason to retain the data. |
| Data portability | Does not apply (available only under consent or contract basis). |
| Objection | Limited under Art. 89(2), but objections should be taken seriously and accommodated where possible. |

For terminology and the regulation itself, see [GDPR concepts for researchers](CROSS-legal.md). For project-specific questions, contact rdm@cmi.no.

!!! info "Last reviewed"
    This page was last reviewed on 28 April 2026. GDPR interpretation evolves; verify against the official Norwegian Data Protection Authority (Datatilsynet) and Sikt guidance for the current position.
