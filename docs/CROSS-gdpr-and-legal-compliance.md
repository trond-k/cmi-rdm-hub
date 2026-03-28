---
icon: lucide/shield-check
title: "GDPR and legal compliance"
description: "How the GDPR applies to CMI research, and the recommended interpretive approach: proportionality, lawful basis, special categories, cross-border transfers, and data subject rights."
tags:
  - GDPR
  - Legal compliance
  - Data protection
  - Proportionality
  - Cross-cutting
notes: ""
date_updated: 2026-03-28
---

# GDPR and legal compliance

*The GDPR applies to virtually all CMI research involving people. This page sets out the recommended interpretive approach: proportional, research-enabling, and grounded in the regulation's own provisions for scientific research. It covers lawful basis, the consent distinction, special category data, cross-border transfers, and data subject rights. For plain-language explanations of GDPR terminology, see [GDPR concepts for researchers](CROSS-legal.md). For operational guidance on information letters, see [Informed consent and information letters](CROSS-ethics.md).*

!!! info "Guidance under development"
    This page reflects CMI's recommended approach to GDPR compliance in research. These recommendations are based on defensible, research-enabling interpretations of the regulation, but they have not yet been formally adopted as institutional policy. Individual projects may need to deviate, and the reasoning for any deviation should be documented. Contact rdm@cmi.no for project-specific questions.

## Proportionality: the governing principle

The GDPR was designed to regulate large-scale commercial data processing. It was not designed for a researcher conducting 20 interviews in Zanzibar or running a survey of 300 households in rural Ethiopia. The regulation nonetheless applies to research, but its provisions should be interpreted **proportionally**. The GDPR itself requires this: Recital 4 states that the right to data protection 'must be considered in relation to its function in society and be balanced against other fundamental rights, in accordance with the principle of proportionality.' Scientific research is explicitly recognised as a legitimate societal purpose (Recitals 156–159, Article 89).

In practice, proportionality means that the safeguards appropriate for a technology company processing millions of user records are not the same safeguards appropriate for a qualitative research project with a small number of participants. The recommendations on this page are calibrated to the scale, nature, and risk profile of social science research.

??? note "A note on stricter interpretations"
    Some Norwegian institutions and data protection officers adopt more conservative positions than those described here, often because their guidance is designed to cover all cases, including large-scale, high-risk processing. These stricter positions are not wrong; they are risk-averse. The approach recommended here aims to be legally defensible while minimising unnecessary administrative burden on researchers. Where significant interpretive differences exist, they are flagged on this page.

## Lawful basis: public interest as the recommended default

The recommended default lawful basis for processing personal data in CMI research is **public interest (Article 6(1)(e))**, supported by the Norwegian Personal Data Act §8 and the research-specific provisions in GDPR Article 89. This applies across the full range of CMI research: qualitative, quantitative, mixed methods, interviews, surveys, ethnography, register studies, and evaluations.

Public interest is not limited to registry-based or large-scale research. It is the basis designed for scientific research, and it applies to a semi-structured interview study as much as to a national survey. Sikt's own guidance acknowledges that public interest is often more appropriate than consent for research.

??? warning "Why not consent as the default lawful basis?"
    Using GDPR consent (Article 6(1)(a)) as the primary lawful basis for research creates several practical problems:

    - **Withdrawal instability.** If consent is the lawful basis, a participant who withdraws triggers a legal obligation to delete their data. In a project running for two years, where the participant's data is woven into analytical frameworks, deletion can seriously impair the research. Under the public interest basis, the right to erasure is limited by Article 17(3)(d).
    - **Specificity requirements.** GDPR consent must be specific to defined processing purposes. Qualitative and ethnographic research is inherently exploratory, and the scope of relevant data often cannot be fully specified in advance.
    - **Conflation with ethical consent.** Bundling GDPR consent into the same form as ethical consent confuses two different things and produces consent forms that are simultaneously too detailed and too vague.
    - **False sense of control.** In many CMI research contexts (fieldwork with vulnerable populations, research in conflict zones, power imbalances), the 'freely given' requirement of GDPR consent is difficult to establish with certainty.

    Many Norwegian institutions default to consent for interview and survey research, reserving public interest for registry studies. This is a risk-averse position, not a legal requirement.

## The consent distinction: ethical consent and GDPR consent

Two different kinds of consent operate in research, and they should not be confused:

- **Ethical consent** is the obligation, rooted in research ethics and the NESH guidelines, to ensure that participation is voluntary, informed, and revocable. Ethical consent is always required when research involves human participants, regardless of the GDPR lawful basis. It is documented through the [information letter](CROSS-ethics.md).
- **GDPR consent** (Article 6(1)(a)) is a specific lawful basis for processing personal data, with strict legal requirements and specific legal consequences. It is one of several possible lawful bases. When public interest is the lawful basis, GDPR consent is not required.

Under the recommended approach, GDPR consent is reserved for specific, bounded processing activities where it is the most natural fit, such as consent to be recorded, consent to be named in publications, or consent to have data archived for future reuse. These are layered on top of the public interest basis, not used instead of it.

## Special category data

Special category data (Article 9) includes racial or ethnic origin, political opinions, religious or philosophical beliefs, trade union membership, genetic data, biometric data, health data, and data about sex life or sexual orientation. In CMI's research profile, special category data is common and often arises incidentally. An interview about governance may capture political opinions; ethnographic fieldwork in a multi-ethnic context captures ethnic origin.

The recommended additional basis for special category data is Article 9(2)(j): processing necessary for scientific research purposes with appropriate safeguards under Article 89(1). The Norwegian Personal Data Act §9 provides the national implementation.

!!! tip "Practical approach to special category data"
    Rather than trying to predict every special category in advance, anticipate at the project level which categories are likely to arise given your topic, methods, and participant groups. Flag these in the Sikt notification and the data inventory. Handle incidental capture proportionally: if a special category arises naturally in an interview, the Article 9(2)(j) basis covers it. Context matters. A passing mention of attending a mosque in an interview about municipal budgets is not necessarily 'religious beliefs' in a GDPR-relevant sense.

## Data minimisation

Data minimisation (Article 5(1)(c)) requires that personal data be adequate, relevant, and limited to what is necessary for the research purpose. This does not mean restricting data collection to a pre-approved script. Qualitative research is inherently open-ended. What minimisation requires is intentionality (collect data related to your research purpose), no gratuitous collection (do not gather data you clearly do not need), and proportional retention (do not keep identifiable data longer than necessary). Retention periods and deletion are covered in forthcoming guidance on data retention.

## Cross-border data transfers

CMI researchers routinely collect data in countries outside the EEA, most of which lack EU adequacy decisions. Not all data movements are the same, and they should not all require the same legal machinery. The recommended approach matches the safeguard mechanism to the actual data flow and risk:

- **Fieldwork data collection.** A CMI researcher collecting data on an encrypted device abroad, with data uploaded to CMI storage in Norway, needs practical safeguards (device encryption, secure upload, password protection), not Standard Contractual Clauses. The data never leaves the researcher's control.
- **Local research assistants.** When a research assistant acts under CMI's instruction and authority, they are part of the controller's operations. Clear data handling instructions, encrypted devices, and a confidentiality agreement in their contract are sufficient.
- **Partner institutions.** For genuine research collaborations, a joint controllership agreement (Article 26) is often more appropriate than SCCs. The research derogation (Article 49(1)(d)) is a further option for transfers necessary for scientific research in the public interest.
- **Cloud services and digital tools.** Standard data processing agreements from the service provider are typically sufficient. Prefer tools that offer EEA-based or Swiss-based processing where available. Forthcoming guidance on tools and services will address specific platforms.

??? note "Standard Contractual Clauses"
    SCCs remain an option for sustained data-sharing arrangements where other mechanisms are not appropriate, but they are designed for commercial data processing relationships and can be disproportionate for academic research collaborations. Joint controllership agreements, the research derogation, and practical security measures are often more fitting for research partnerships.

## Data Protection Impact Assessment

A DPIA is required under Article 35 when processing is likely to result in a high risk to data subjects. Most CMI projects involving a small number of qualitative interviews will not trigger a DPIA. A multi-country survey with thousands of respondents and sensitive topics likely will. The RDM contact (rdm@cmi.no) can advise on whether a DPIA is needed and support the process.

??? example "When a DPIA is recommended"
    Consider a DPIA when two or more of the following apply: large-scale processing of personal data, systematic evaluation or profiling, processing of special category data in sensitive contexts, processing data on vulnerable groups, or combining datasets from different sources. A DPIA documents the nature and purpose of the processing, the risks to data subjects, and the measures in place to mitigate those risks. It is an internal assessment, not a regulatory submission.

## Data subject rights in research

Under the public interest basis, data subject rights are modified by Article 89(2) and the Norwegian Personal Data Act §17. The information letter should describe these rights clearly but concisely. In practice, most CMI research participants will not exercise them, but you should know how to respond if asked.

| Right | Status under public interest basis |
|---|---|
| Information | Fully applies (provided through the information letter) |
| Access | Applies (provide transcript or relevant records on request) |
| Rectification | Applies (correct factual errors on request) |
| Erasure | Limited: may be refused if deletion would seriously impair the research (Article 17(3)(d)). The recommended default is to accommodate deletion requests unless there is a compelling, documented reason to retain the data |
| Data portability | Does not apply (applies only under consent or contract basis) |
| Objection | Limited under Article 89(2), but objections should be taken seriously and accommodated where possible |

Forthcoming guidance on data retention will cover withdrawal, objection, and their practical limits in more detail.
