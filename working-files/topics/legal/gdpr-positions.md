---
version: "1.0"
date: 2026-03-11
notes:
  - Draft — should be reviewed with CMI's Research Ethics Committee and legal
    counsel before finalising as institutional positions.
  - Stricter interpretations from other Norwegian institutions are noted inline;
    review whether CMI's positions need adjustment.
---

# GDPR Interpretive Positions — CMI

<!-- HOW CMI interprets and applies GDPR for research: lawful basis, consent,
     special categories, data minimisation, cross-border transfer, data subject rights.

     Refactored from the former gdpr-stance.md. Sections that moved to their
     own modules:
     - Storage period and deletion → retention.md
     - Sikt notification → sikt.md

     For data classification and tier definitions, see data-classification.md.
     For storage infrastructure, see data-security.md.
     For operational partnership recommendations, see partnerships.md.
     For information letter operational guidance, see consent-and-information.md. -->

This document describes how CMI interprets and applies GDPR in the context of its research. These positions inform all RDM Hub tools — the Data Inventory Generator, DMP Generator, Sikt Notification Form Guide, and chat contexts. They are institutional defaults. Individual projects may need to deviate, and the reasoning for deviation should be documented.

**This is a draft.** These positions should be reviewed with CMI's research ethics committee and, where necessary, legal counsel. They represent defensible, research-enabling interpretations of GDPR — not the only possible interpretations. Where CMI's position diverges from more conservative readings, this is noted explicitly.


## The governing principle: proportionality

GDPR was designed to regulate large-scale data processing — tech companies, public registries, commercial data brokers, health systems. It was not designed to regulate a researcher conducting 20 interviews in Zanzibar or running a survey of 300 households in rural Ethiopia. The regulation nonetheless applies to research, but its provisions must be interpreted **proportionally**. GDPR itself requires this: Recital 4 states that the right to data protection "must be considered in relation to its function in society and be balanced against other fundamental rights, in accordance with the principle of proportionality." Scientific research is explicitly recognised as a legitimate societal purpose throughout the regulation (Recitals 156–159, Article 89).

What proportionality means in practice: the safeguards appropriate for a technology company processing millions of user records are not the same safeguards appropriate for a qualitative research project with a small number of participants. CMI's interpretive positions are calibrated to the scale, nature, and risk profile of social science research — not to the regulatory worst case.

> **Note on stricter interpretations**: some Norwegian institutions and data protection officers adopt more conservative positions than those described here, often out of an abundance of caution or because their guidance is designed to cover all cases (including large-scale, high-risk processing). These stricter positions are not wrong — they are risk-averse. CMI's positions are designed to be legally defensible while minimising unnecessary administrative burden on researchers. Where significant interpretive disagreements exist, they are flagged below.


## Lawful basis: public interest is the default

### The position

CMI's default lawful basis for processing personal data in research is **public interest (Article 6(1)(e))**, supported by the **Norwegian Personal Data Act §8** and the research-specific provisions in **GDPR Article 89**. This applies to the full range of CMI research — qualitative, quantitative, mixed methods, interviews, surveys, ethnography, register studies, evaluations.

Public interest is not limited to registry-based or large-scale research. It is the basis designed for scientific research, and it applies to a semi-structured interview study as much as to a national survey.

### Why not consent as the default?

Using GDPR consent (Article 6(1)(a)) as the primary lawful basis for research creates several problems:

**Withdrawal instability.** If consent is the lawful basis, a participant who withdraws consent triggers a legal obligation to delete their data. In a research project that has been running for two years, where the participant's data is woven into analytical frameworks and may have influenced other interpretations, deletion can seriously impair the research. Under the public interest basis, the right to erasure is limited by Article 17(3)(d) — data can be retained where deletion would seriously impair the research objectives.

**Specificity requirements.** GDPR consent must be specific to defined processing purposes. Qualitative and ethnographic research is inherently exploratory — the scope of relevant data often cannot be fully specified in advance. This creates an uncomfortable mismatch between the consent requirement and the reality of research practice.

**Conflation with ethical consent.** When researchers use GDPR consent as their lawful basis, they typically bundle it into the consent form alongside ethical consent (voluntary participation, right to withdraw). This conflation confuses two different things and creates consent forms that are simultaneously too detailed (GDPR requirements) and too vague (trying to cover open-ended research). Separating them is cleaner.

**False sense of control.** In many CMI research contexts — fieldwork with vulnerable populations, research in conflict zones, research involving power imbalances — the "freely given" requirement of GDPR consent is difficult to establish with certainty. Relying on consent as the lawful basis in these contexts creates a legal foundation that may be shakier than it appears.

> **Stricter interpretation**: many Norwegian institutions default to consent as the lawful basis for interview and survey research, reserving the public interest basis for registry studies. This is a risk-averse position, not a legal requirement. The Norwegian Data Protection Authority (Datatilsynet) and the Norwegian Personal Data Act explicitly support the public interest basis for scientific research. Sikt's own guidance acknowledges both bases.


## Consent: ethical practice, not lawful basis

### The distinction

There are two different kinds of consent in research, and they must not be confused:

**Ethical consent** is the obligation — rooted in research ethics, not data protection law — to ensure that research participation is voluntary, informed, and revocable. Ethical consent is always required when research involves human participants, regardless of the GDPR lawful basis. It is documented through the information letter and the participant's agreement to take part. Ethical consent is governed by the NESH guidelines, not by GDPR.

**GDPR consent** (Article 6(1)(a)) is a specific lawful basis for processing personal data. It has strict legal requirements (freely given, specific, informed, unambiguous, withdrawable) and specific legal consequences (withdrawal triggers deletion rights). GDPR consent is one of several possible lawful bases. It is not the only one, and it is not always the most appropriate one for research.

### The information letter as the vehicle of consent

At CMI, **all research involving human participants must be conducted on the basis of informed, voluntary participation**. The information letter is the vehicle through which this is achieved: it informs participants about the research, and by agreeing to take part, participants confirm their voluntary, informed engagement. The information letter is therefore not merely a transparency document — it is the foundation of the participant's informed, voluntary *consent* to take part. This is non-negotiable.

Consent does not need to be documented in writing. In research contexts, participation itself constitutes consent: a person who receives an information letter and then shows up for an interview, fills in a questionnaire, or otherwise engages with the research has consented by their conduct. A signed form or a checkbox is not required to make that consent valid — what matters is that the participant was properly informed and chose freely to take part. Written documentation may sometimes be appropriate (for instance, where the research involves highly sensitive topics, vulnerable groups, or activities with particular implications), but it is not a general requirement.

Because the information letter carries so much weight, it must be drafted with care. Depending on the nature of the research, certain issues should be explicitly addressed in the letter to ensure that consent is genuinely informed. These include, where relevant:

- **Audio or video recording.** Recording is a distinct processing activity with its own implications (voice is arguably biometric data; recordings are inherently identifiable). If the research involves recording, this should be clearly described and participants should have the opportunity to agree or decline.
- **Use of real names or identifiable information in publications.** The default is anonymisation. If a researcher wants to use identifiable information, this must be explained, and the participant's agreement to it made explicit.
- **Archiving data for future reuse.** If data will be deposited in a repository for secondary use beyond the original project, participants must be informed of this so their consent extends to that purpose.
- **Specific sensitive processing** that goes beyond the core research activity — for example, sharing identifiable data with a named third party for a defined purpose.

This approach keeps consent meaningful, specific, and manageable. A well-drafted information letter covers both the transparency obligations and the elements above where they apply.


## The information letter as the primary instrument

### What it does

The information letter fulfils GDPR's transparency obligations under Articles 13 and 14. It tells participants:

- Who is responsible for the research (CMI, the named researcher)
- What the research is about and why their data is being processed
- What data will be collected and how
- The lawful basis for processing (public interest, with reference to the Norwegian Personal Data Act)
- How data will be stored and secured
- How long data will be retained
- Who will have access to the data
- Their rights (access, rectification, complaint to Datatilsynet)
- That participation is voluntary and they can withdraw at any time (ethical consent)
- Contact details for the researcher and the RDM contact (rdm@cmi.no)

### What it does not do

The information letter does **not** ask for GDPR consent to process data. It informs. The lawful basis is public interest, which does not require consent. Participants are free to decline to participate — that is their ethical right — but their participation is not contingent on signing a GDPR consent form.

### Adaptation for fieldwork contexts

CMI conducts research in contexts where standard written information procedures may be inappropriate:

- **Oral delivery**: the information letter content can be delivered orally when literacy, language, or cultural factors make a written letter inappropriate. The researcher should document that the information was provided (e.g., a note in the research log, recorded verbal confirmation from the participant).
- **Language**: information must be provided in a language the participant understands. For fieldwork in non-English, non-Norwegian settings, this typically means translation. The translated version does not need to be a formal legal document — it needs to be clear and comprehensible.
- **Community contexts**: in settings where community leaders or gatekeepers facilitate access, the information letter process may involve both community-level and individual-level communication. Community agreement does not replace individual informed participation.
- **Sensitive and high-risk contexts**: in conflict zones, authoritarian settings, or situations where documentation itself creates risk (e.g., a signed form linking a participant to research on political opposition), the information process should be adapted to protect participants. Oral information with no written record of the participant's identity may be the most ethical and GDPR-compliant approach.

> **Note**: the flexibility described here applies to the method of information delivery, not to the substance. Participants must always be informed about the research, regardless of the format.

For operational guidance on drafting information letters — including standard content, separate consent elements, oral delivery procedures, and translations — see `consent-and-information.md`.


## Special category data (Article 9)

### When it applies

Special category data includes: racial or ethnic origin, political opinions, religious or philosophical beliefs, trade union membership, genetic data, biometric data, health data, sex life or sexual orientation.

In CMI's research profile, special category data is **common**, often arising incidentally rather than by design. An interview about governance may capture political opinions. Ethnographic fieldwork in a multi-ethnic context captures ethnic origin. Research on conflict-related violence captures health data and potentially data about sexual orientation or sexual violence.

The threshold is **processing**, not **intent**. If the data is captured — even incidentally, even in an unstructured interview — Article 9 applies.

### The additional basis

When the lawful basis is public interest (Article 6(1)(e)), the additional basis for special category data is **Article 9(2)(j)**: processing necessary for scientific research purposes, subject to appropriate safeguards under Article 89(1). The Norwegian Personal Data Act §9 provides the national implementation.

The required safeguards under Article 89(1) are: technical and organisational measures, in particular data minimisation (interpreted proportionally — see below). For CMI research, this typically means: encrypted storage, access limited to the project team, pseudonymisation where practicable, and deletion or anonymisation when the research purpose is fulfilled.

### Practical guidance

Rather than requiring researchers to predict in advance exactly which special categories their data will contain, CMI's approach is:

1. **Anticipate at the project level.** Based on the research topic, methods, and participant groups, assess which special categories are likely to arise. A project on political participation will involve political opinions. A project on refugee health will involve health data and ethnic origin. Flag these in the project's data mapping.
2. **Handle incidental capture proportionally.** When a special category arises incidentally in an interview, the researcher does not need to stop the interview or seek additional consent. The Article 9(2)(j) basis covers research processing, including data that emerges naturally during data collection. The researcher should ensure the data is stored and handled with appropriate security.
3. **Don't over-classify.** Not every mention of a topic constitutes special category data processing. A participant who mentions in passing that they attend a mosque is not necessarily providing data about religious beliefs in a GDPR-relevant sense, if the research is about municipal budgeting. Context matters. The question is whether the data is being **processed** in a way that relates to the special category, not whether the topic has ever been mentioned.

**Classification tier mapping**: special category data is typically classified as Red (Confidential) or Black (Strictly Confidential) under CMI's data classification scheme, depending on the context and the risk of harm if exposed. An interview about health in Norway: Red. An interview about health in a context where the condition is criminalised or stigmatised: Black. See `data-classification.md` for the full classification criteria and the Red vs. Black decision test.

> **Stricter interpretation**: some DPOs and institutions take the position that any recording or transcript containing any mention of a special category topic constitutes special category data, regardless of context. This maximalist interpretation is defensible but creates significant overhead for qualitative researchers. CMI's position is that context and proportionality should guide classification.


## Data minimisation: interpreted for research, not against it

GDPR requires that personal data be "adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed" (Article 5(1)(c)).

### What this means for CMI research

**It does not mean restricting data collection to a pre-approved script.** Qualitative research — interviews, ethnography, participant observation — is inherently open-ended. A researcher conducting an interview about taxation policy may learn about the participant's family situation, health, political affiliations, and community relationships, not because they sought this information but because that is how human conversations work. Data minimisation does not require researchers to interrupt participants or refuse to listen.

**What data minimisation does require:**

1. **Intentionality.** The researcher should have a research purpose and collect data that relates to it. "I am studying local governance, so I conduct interviews with local officials" is intentional. "I am collecting data on everyone I meet in case it's useful later" is not.
2. **No gratuitous collection.** Don't collect data that is clearly unrelated to the research purpose. If you are studying tax compliance, you do not need to photograph participants' identity documents.
3. **Proportional retention.** Don't retain identifiable data longer than needed. Once analysis is complete and the data has been anonymised or the retention period has passed, identifiable data should be deleted. See `retention.md` for CMI's default retention periods.
4. **Review and clean.** If, after data collection, it becomes clear that certain data is irrelevant to the research, consider deleting it — especially if it contains sensitive personal information.

> **The spirit of the principle**: data minimisation is about discipline and purpose, not restriction. A well-designed research project that collects rich, detailed data from a clearly defined participant group for a clearly articulated purpose is consistent with data minimisation, even if the data is extensive.


## Cross-border data transfer: proportional approaches

### The landscape

CMI researchers routinely collect data in countries outside the EEA — across Africa, Asia, the Middle East, and Latin America. Most of these countries do not have EU adequacy decisions. Under a strict reading of GDPR Chapter V, every instance of personal data being collected, stored, or processed outside the EEA constitutes a "transfer" requiring legal safeguards.

### CMI's proportional approach

Not all data movements are the same, and they should not all require the same legal machinery.

**Scenario 1: A CMI researcher collects data during fieldwork abroad.**
A researcher travels to Tanzania, conducts interviews on an encrypted device (laptop, recorder), and uploads the data to CMI's institutional storage in Norway upon return or during fieldwork when connectivity allows.

This is technically a transfer under GDPR, but the data never leaves the researcher's control. The appropriate safeguards are **practical, not contractual**: device encryption, secure upload procedures, password-protected files, not leaving devices unattended. Requiring Standard Contractual Clauses for this scenario is disproportionate — there is no data processor, no data sharing, no third-party access. The researcher is acting as part of CMI (the data controller) throughout.

**Scenario 2: A local research assistant collects data on behalf of CMI.**
A research assistant based in a partner country conducts interviews or distributes surveys as part of a CMI project, using their own or CMI-provided equipment.

If the research assistant acts under CMI's instruction and authority (which is the typical arrangement), they are acting as part of the data controller's operations, not as a separate processor. The safeguards are: clear instructions on data handling, encrypted devices or secure upload to CMI storage, a confidentiality agreement as part of their contract. This can be handled through CMI's standard research assistant agreements without separate SCCs.

**Scenario 3: A partner institution stores or processes personal data in their country.**
A partner university in Ethiopia has its own copy of research data, conducts its own analysis, or manages data collection independently.

This is a genuine transfer to a third party and requires appropriate safeguards. But SCCs — which are long, complex, and designed for commercial data processing relationships — are rarely the right instrument for an academic collaboration between two research institutions. More appropriate mechanisms include:

- **Joint controllership agreement (Article 26)**: if both CMI and the partner institution determine the purposes and means of processing (which is the case in genuine research collaborations), a joint controllership arrangement is more appropriate than a controller-processor SCC. A joint controllership agreement is lighter-weight and better reflects the reality of equal research partnerships. This is CMI's preferred approach for collaborative research.
- **The research derogation (Article 49(1)(d))**: transfers necessary for important reasons of public interest, including scientific research carried out in the public interest, are permitted without additional safeguards. This is a legitimate basis for research data transfers, though it should not be used as a blanket exemption — document why the transfer is necessary for the research.
- **Practical safeguards**: regardless of the legal mechanism, practical safeguards matter more than contractual ones. Encrypted data, access controls, agreed data handling procedures, and clear agreements about retention and deletion are the real protections.
- **Platform-based solutions**: rather than transferring data to a partner institution, consider using a shared platform where partners access data without taking copies. TSD's remote-access model works this way. Swiss-jurisdiction services (Tresorit, Proton Drive) can also provide a shared workspace outside US jurisdiction. See `data-security.md` for CMI's storage infrastructure and available platforms.

SCCs remain an option for sustained data-sharing arrangements where other mechanisms are not appropriate, but they are not the default.

> **Stricter interpretation**: some institutions require SCCs for all data transfers to non-EEA countries, including all fieldwork and all partner collaborations. This is the safest legal position but creates significant administrative burden, especially for institutions like CMI that collaborate with dozens of partners across many countries. It also imposes a controller-processor framing on relationships that are genuinely collaborative, which conflicts with CMI's partnership philosophy. CMI's position is that proportionality requires matching the safeguard mechanism to the actual data flow and risk, and that joint controllership agreements, the research derogation, and practical security measures are often more appropriate than SCCs for research collaborations.

**Scenario 4: Cloud services and digital tools.**
When CMI uses cloud-based tools (survey platforms, transcription services, analysis software, AI tools) that process data on servers outside the EEA, the standard data processing agreements provided by the service are typically sufficient. Prefer tools that offer EEA-based or Swiss-based processing where available. For guidance on specific tools and their suitability for different data classification tiers — including AI tools — see `tools-and-services.md`.

For operational recommendations on partnership agreements, data sharing arrangements, and contracted data collection, see `partnerships.md`.


## Data Protection Impact Assessment (DPIA)

A DPIA is required under GDPR Article 35 when processing is likely to result in a high risk to data subjects. The trigger is the risk profile of the processing, not the classification tier — though in practice the two are closely related.

### When a DPIA applies at CMI

- Always for Black-tier data (see `data-classification.md`).
- When two or more of the following Article 35 indicators apply: large-scale processing of personal data, systematic evaluation or profiling of individuals, processing of special category data in sensitive contexts, processing data on vulnerable groups, combining datasets from different sources.
- When the funder or ethics board requires one.

Most CMI projects involving a small number of qualitative interviews at Red tier will not trigger a DPIA. A multi-country survey with thousands of respondents and sensitive topics likely will.

### What it involves

A DPIA documents: the nature and purpose of the processing, necessity and proportionality, risks to data subjects, and the measures in place to mitigate those risks. It is an internal assessment, not a regulatory submission — though Sikt or the DPO may review it. The RDM contact (rdm@cmi.no) or DPO can advise on whether a DPIA is needed and support the process.


## Data subject rights in research

Under the public interest basis, data subject rights are modified by Article 89(2) and the Norwegian Personal Data Act §17:

- **Right to information**: fully applies. This is what the information letter provides.
- **Right to access**: applies. Participants can request access to their data. For interview transcripts, provide the transcript. For field notes, provide the portions that relate to the specific participant.
- **Right to rectification**: applies. Participants can correct factual errors.
- **Right to erasure**: limited. Erasure can be refused if it would seriously impair the research objectives. However, a participant who withdraws from the research should have their data deleted unless there is a compelling, documented reason to retain it. In practice, CMI should default to deleting data upon withdrawal unless the researcher can articulate why retention is necessary.
- **Right to restriction**: applies in limited circumstances.
- **Right to data portability**: does not apply (this right applies only where the lawful basis is consent or contract).
- **Right to object**: limited under Article 89(2). However, researchers should take objections seriously and accommodate them where possible.

> **Practical approach**: most CMI research participants will never exercise these rights. The information letter should describe them clearly but concisely. Researchers should know these rights exist and have a plan for responding, but the plan does not need to be elaborate.

For CMI's positions on withdrawal, objection, and their practical limits (including the distinction between public interest and consent-based processing), see `retention.md`.

For Sikt notification requirements and procedures, see `sikt.md`.
