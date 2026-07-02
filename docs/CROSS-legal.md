---
icon: lucide/book-open
title: "GDPR concepts for researchers"
description: "A plain-language reference to GDPR terminology and concepts as they apply to CMI research: roles, personal data, legal basis, principles, safeguards, transfers, rights, and Norwegian institutions."
tags:
  - GDPR
  - Legal concepts
  - Data protection
  - Reference
  - Cross-cutting
notes: ""
date_updated: 2026-07-02
---

# GDPR concepts for researchers

*This is a plain-language reference to GDPR concepts as they apply to CMI research. Each entry explains what the concept means, why it matters, and how it works in practice. It is not a legal textbook; it is a working reference for researchers filling in Sikt notifications, drafting information letters, or trying to understand what a DPO is asking them. For CMI's recommended interpretive approach, see [GDPR and legal compliance](CROSS-gdpr-and-legal-compliance.md). For operational guidance on information letters and consent, see [Informed consent and information letters](CROSS-ethics.md).*

## Where the GDPR comes from

The GDPR is the latest expression of a European tradition that treats personal data protection as a fundamental right. The EU Charter of Fundamental Rights (Article 8) states: 'Everyone has the right to the protection of personal data concerning him or her.' The regulation, which took effect in 2018, replaced the earlier Data Protection Directive (1995) with a framework that applies directly and uniformly across the EU and EEA.

The GDPR was driven by the explosion of large-scale commercial data processing. Its default mental model is a technology company processing millions of customer records. A researcher conducting 25 interviews in rural Zambia operates in the same legal framework, but at a completely different scale, with completely different risks, and for a completely different purpose. The regulation recognises this through the principle of **proportionality** (Recital 4) and through specific provisions for scientific research (Recitals 156–159, Article 89).

??? note "The historical lineage"
    The lineage runs through the Council of Europe's Convention 108 (1981), the EU Charter of Fundamental Rights, and the Data Protection Directive (1995). Norway is not an EU member state, but the GDPR applies in Norway through the EEA Agreement. The Norwegian implementation is the Personal Data Act (*Personopplysningsloven*, 2018).

## Roles

**Data controller.** The institution that decides why and how personal data is processed. For CMI projects, CMI is the data controller. The PI acts on behalf of CMI, but CMI carries legal responsibility for GDPR compliance.

**Joint controllers.** Two or more institutions that together decide why and how personal data is processed (Article 26). This is the natural framing for CMI's international research collaborations where both institutions shape the research design. A joint controllership agreement defines each party's responsibilities.

**Data processor.** An organisation that processes personal data on your instructions, without deciding the purpose or design of the research. Examples: a contracted survey firm, a transcription service, a cloud storage platform. If you use a data processor, you need a Data Processing Agreement (Article 28).

**Data subject.** The person whose personal data you are processing: usually a research participant (interviewee, survey respondent, someone observed during fieldwork). It can also be a third person whom your participant talks about and who becomes identifiable in the data. Data subjects have rights under GDPR regardless of whether they are in the EU.

**Data Protection Officer (DPO).** A person designated to advise an institution on data protection compliance (Article 37). CMI's data protection contact serves this advisory function for researchers.

## Legal basis

**Lawful basis (Article 6).** GDPR requires a legal justification for every instance of personal data processing. There are six possible bases; for research, only two are commonly relevant: public interest and consent. You choose your lawful basis before you start collecting data, and the choice has consequences for participant rights and what happens if someone withdraws.

**Public interest (Article 6(1)(e)).** Processing necessary to perform a task carried out in the public interest. Scientific research is recognised as a public interest task under Norwegian law (Personal Data Act §8). This is the standard lawful basis for research projects in Norway and the recommended default for CMI projects.

**GDPR consent (Article 6(1)(a)).** A lawful basis where the data subject's explicit agreement is the legal justification for processing. GDPR consent has strict requirements: freely given, specific, informed, unambiguous, documented, and as easy to withdraw as to give. Withdrawal triggers a legal obligation to delete the data. This is not the recommended default for CMI research; see [GDPR and legal compliance](CROSS-gdpr-and-legal-compliance.md) for the rationale.

**Ethical consent.** Not a GDPR term. This is the research ethics obligation, grounded in the NESH guidelines, to ensure that participation is voluntary, informed, and revocable. Ethical consent is always required at CMI, regardless of which GDPR lawful basis is used. See [Informed consent and information letters](CROSS-ethics.md).

## Personal data

**Personal data.** Any information relating to an identified or identifiable natural person (Article 4(1)). 'Identifiable' is broad: a name is personal data, but so is a combination of age, occupation, village, and family size if that combination could single someone out.

**Special category data (Article 9).** A subset of personal data that GDPR considers particularly sensitive: racial or ethnic origin, political opinions, religious or philosophical beliefs, trade union membership, genetic data, biometric data, health data, and data about sex life or sexual orientation. Processing special category data requires an additional legal basis; for CMI research, this is Article 9(2)(j) (scientific research purposes with appropriate safeguards).

**Pseudonymisation.** Replacing direct identifiers (names, ID numbers) with a code, while keeping a separate key that links the code back to the person (Article 4(5)). The data is still personal data, but pseudonymisation reduces risk: if the research dataset is exposed, identities are not immediately revealed.

**Anonymisation.** Removing or transforming personal data so that the individual can no longer be identified, even by combining the remaining data with other available information. Truly anonymised data is no longer personal data and falls outside GDPR entirely (Recital 26). Anonymisation is harder than it sounds, especially for qualitative data: a transcript with the name removed but detailed descriptions of role, location, and experiences may still be identifiable.

??? note "Biometric data and de-identification"
    **Biometric data** is data resulting from specific technical processing of physical, physiological, or behavioural characteristics that allows unique identification (Article 4(14)). The most relevant case for CMI: voice recordings. A voice on an audio recording is arguably biometric data because it can identify a person.

    **De-identification** is not a GDPR term, but is widely used (especially in US and health research contexts) to mean removing obvious identifiers. In practice, de-identification sits somewhere between pseudonymisation and full anonymisation. Data that has been 'de-identified' in a loose sense may still be personal data under GDPR if re-identification is reasonably possible.

## Principles

**Data minimisation (Article 5(1)(c)).** Collect only the personal data that is adequate, relevant, and necessary for your research purpose. This does not mean restricting interviews to a pre-approved script. It means being intentional about what you collect, not gathering data you clearly do not need, and not keeping identifiable data longer than necessary.

**Purpose limitation (Article 5(1)(b)).** Personal data must be collected for specified, explicit, and legitimate purposes. However, GDPR explicitly provides that further processing for scientific research purposes is not considered incompatible with the original purpose (Article 5(1)(b), second sentence). Your project can evolve without violating this principle, provided safeguards are in place.

**Storage limitation (Article 5(1)(e)).** Personal data should be kept in identifiable form no longer than necessary for the research purpose. After that, it should be anonymised or deleted. Forthcoming guidance on data retention will cover default retention periods.

**Accountability (Article 5(2)).** The controller must be able to demonstrate compliance with GDPR principles. This is why documentation matters: the Sikt notification, the data management plan, the information letter, agreements with partners and processors, and records of data handling decisions. You do not need a perfect paper trail; you need enough that, if asked, you can show what you did with personal data and why.

## Safeguards and security

**Appropriate safeguards (Article 89(1)).** GDPR requires 'appropriate technical and organisational measures' when processing personal data for research. What counts as appropriate depends on the risk. For most CMI projects, this means encrypted storage, access restricted to the project team, pseudonymisation where practicable, secure data transmission, and anonymisation or deletion when the research purpose is fulfilled.

**Encryption.** Encryption at rest means data is encrypted when stored on a disk or server (CMI's M365 environment and TSD both provide this automatically). Encryption in transit means data is encrypted while being transmitted over a network (HTTPS provides this). For fieldwork, ensure devices used for data collection have device-level encryption enabled.

**Data Processing Agreement (DPA).** A contract between a data controller and a data processor specifying what the processor may do with the data (Article 28). Required whenever you use an external service that handles personal data on your behalf: transcription services, contracted survey firms, cloud tools outside CMI's institutional infrastructure.

**Joint controllership agreement (Article 26).** An agreement between joint controllers defining each party's responsibilities. This is the recommended instrument for international research collaborations where both CMI and the partner institution shape the research.

**Standard Contractual Clauses (SCCs).** Pre-approved contract templates for transferring personal data to countries outside the EEA (Article 46(2)(c)). Designed for commercial data processing relationships. For research collaborations, joint controllership agreements or the research derogation are often more proportionate alternatives.

**DPIA.** A structured assessment of the risks that data processing poses to data subjects, and the measures taken to mitigate those risks (Article 35). Required when processing is likely to result in a high risk to individuals. See [GDPR and legal compliance](CROSS-gdpr-and-legal-compliance.md#when-a-dpia-is-needed) for when a DPIA applies.

## Data transfers

**Third-country transfer.** Any movement of personal data to a country outside the EU/EEA, including sending data to a partner, storing data on a non-EEA server, and collecting data on a device during fieldwork abroad. Most CMI projects involve third-country transfers.

**Adequacy decision (Article 45).** A finding by the European Commission that a country provides adequate data protection, so data can flow there without additional safeguards. Countries with adequacy decisions include the UK, Japan, and South Korea. Most CMI fieldwork countries do not have adequacy decisions.

**Research derogation (Article 49(1)(d)).** A provision allowing transfers necessary for important reasons of public interest, which includes scientific research. A practical option for occasional transfers where no other safeguard fits, but a derogation rather than a standing arrangement: the EDPB treats Article 49 as an exception for non-repetitive transfers, so systematic, repeated sharing needs an agreement under Articles 26 or 46 instead.

## Sikt and REK

**Sikt.** The Norwegian Agency for Shared Services in Education and Research. Sikt provides data protection advisory services for research. The Sikt notification form is the mechanism by which research institutions report personal data processing in research projects. Filing a notification is required under CMI's procedures: it is how the institution documents that its GDPR obligations are met, not a separate statutory approval. Sikt assesses whether the described processing is consistent with data protection requirements and advises if they see concerns; they do not approve or reject research.

**REK (Regional Committees for Medical and Health Research Ethics).** The ethics committees that review health research under the Health Research Act. REK approval is required for projects that fall under this act: clinical trials, health registry studies, and research that aims to generate new knowledge about health and disease. Most CMI health-related research is social science research about health (access to services, health policy, wellbeing outcomes) and does not require REK approval. If you are unsure, consult the RDM contact (rdm@cmi.no).

??? note "The difference between Sikt and REK"
    REK and Sikt serve different functions. REK reviews research ethics and design under the Health Research Act. Sikt assesses data protection compliance under the GDPR. A project that requires REK approval also needs a Sikt notification, but most CMI projects need only the Sikt notification.

??? note "Key sections of the Norwegian Personal Data Act"
    The most relevant national provisions for CMI researchers:

    - **Section 8** provides the legal basis for processing personal data in the public interest for scientific or historical research, statistical purposes, and archiving in the public interest. This anchors the use of public interest (Article 6(1)(e)) as the lawful basis for research in Norway.
    - **Section 9** implements the derogation for special category data processing for research purposes (Article 9(2)(j)).
    - **Section 17** implements research-specific modifications to data subject rights (Article 89(2)), allowing certain rights to be limited when processing serves the public interest and appropriate safeguards are in place.