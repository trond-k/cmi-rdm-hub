---
version: "1.0"
date: 2026-03-11
notes:
  - Develop a one-page cloud service assessment checklist.
  - Verify current SurveyCTO, KoboToolbox, and Qualtrics DPA terms and data
    residency details. These change and should be reviewed annually.
  - Assess specific transcription services available to CMI and maintain a short
    approved list.
  - Add reference to CMI's institutional AI policy once available in context/.
---

# Cloud Services and Tool Assessment — CMI

<!-- WHICH external tools and services CMI researchers may use for different data
     classification tiers, and HOW to assess new tools. Covers survey platforms,
     transcription services, AI tools, and the general cloud service assessment
     framework.

     Consolidated from:
     - REC-TOOLS-01, 02, 03, 04 from rdm-recommendations.md
     - data-security-policy.md AI tools and data security section

     For storage infrastructure (M365, TSD, Tresorit), see data-security.md.
     For data classification tiers, see data-classification.md.
     For contracted data collection firms using survey tools, see also partnerships.md. -->


## Assessing cloud services for personal data

Before using any third-party cloud service (survey platform, transcription tool, translation tool, analysis software, AI tool) to process personal data, assess:

1. **Data residency**: where does the service store and process data? EEA or Swiss storage is preferred. If data is processed outside the EEA, additional transfer safeguards may be needed.
2. **Data Processing Agreement (DPA)**: does the service offer a GDPR-compliant DPA? Is it signed or accepted?
3. **Training data policy**: does the service use uploaded data for model training or product improvement? For AI tools: does the service retain input data after processing? Services that use customer data for training are not acceptable for Red or Black-tier data.
4. **Encryption**: is data encrypted at rest and in transit?
5. **Access controls**: can access be restricted to authorised project members?
6. **Subprocessors**: does the service use subprocessors, and where are they located?

**Action for the researcher**: complete the cloud service assessment before using the tool. Document the assessment in the DMP. If unsure, consult the RDM contact (rdm@cmi.no).


## Classification-based rules

The data classification tier (see `data-classification.md`) determines which tools are acceptable:

| Tier | Tool use |
|---|---|
| **Green** (Open) | Any tool. Published data and public documents carry no restriction. |
| **Yellow** (Internal) | Enterprise tools within CMI's M365 ecosystem preferred. General-purpose tools acceptable for non-sensitive tasks. Internal documents should not be uploaded to consumer AI tools. |
| **Red** (Confidential) | Enterprise tools with DPA only. No general-purpose consumer AI tools (ChatGPT, Claude consumer, Google Translate). No services that use uploaded data for training. |
| **Black** (Strictly Confidential) | No external cloud processing tools. Data remains within approved secure infrastructure determined case-by-case (see `data-security.md`). |


## Survey data collection platforms

**Applies when**: the project uses SurveyCTO, KoboToolbox, Qualtrics, or similar platforms to collect survey data containing personal data.

Apply the general cloud service assessment above. Additionally:

- **SurveyCTO**: data is stored on SurveyCTO's servers (hosted on AWS). SurveyCTO offers server-side encryption and a DPA. Acceptable for Red-tier data if the DPA is in place, but note that data transits through and is stored on US-hosted infrastructure. For projects where US jurisdiction is a concern, consider Nettskjema/TSD as an alternative for data collection. **When a contracted data collection firm uses its own SurveyCTO account** (see `partnerships.md`): the DPA between the firm and SurveyCTO covers that relationship, but CMI as data controller must be satisfied that the chain of agreements provides adequate protection. Consider whether a CMI-controlled SurveyCTO account with firm enumerators granted access would simplify the data chain.
- **KoboToolbox**: the self-hosted option (kobo-install) allows institutional hosting. The hosted version (kobotoolbox.org) stores data on servers managed by the Kobo team. Assess data residency before use.
- **Nettskjema/TSD**: Norwegian sovereign infrastructure. GDPR-compliant by design. Integrates with TSD for automatic secure storage. The strongest option for sensitive data collection, but requires a TSD project allocation and involves additional cost. See `data-security.md` for TSD details.
- **Qualtrics**: enterprise version with DPA is acceptable for Red-tier data. Consumer/free version is not.

**Action for the researcher**: choose the survey platform during project design. If using SurveyCTO or KoboToolbox, confirm the DPA is in place and document the data residency. If the project involves Black-tier data or the CLOUD Act concern is specifically relevant, use Nettskjema/TSD. Budget for TSD costs if applicable.

**Escalation**: consult the RDM contact (rdm@cmi.no) if the project involves Black-tier data, if no survey platform meets the requirements, or if a contracted firm's data handling capacity is unclear.


## Transcription services

**Applies when**: the project will transcribe audio or video recordings containing personal data.

Transcription services process identifiable audio data — voice is inherently personal and arguably biometric. Apply the general cloud service assessment, with additional requirements:

- The service must **not** use uploaded audio for training or product improvement
- The service must store data within the EEA (or a jurisdiction with adequate protections)
- A DPA must be in place
- Prefer institutional tools over consumer services

**Options by preference**:
1. **Manual transcription by project staff**: no third-party processing. Most secure. Labour-intensive.
2. **Institutional transcription tools**: if available through CMI's M365 ecosystem or TSD. Check current availability.
3. **Enterprise transcription services with DPA**: (e.g., enterprise-tier Otter.ai, Verbit, or similar). Verify DPA, data residency, and training data policy before use.
4. **General-purpose AI tools** (consumer ChatGPT, Claude, Whisper API): not acceptable for Red or Black-tier audio data unless the service offers an enterprise tier with DPA and no-training guarantees.

**Action for the researcher**: decide on transcription method during project planning. If using an external service, complete the cloud service assessment. Document the choice in the DMP.

**Escalation**: consult the RDM contact (rdm@cmi.no) if no available transcription service meets the requirements and manual transcription is not feasible.


## AI tools for analysis and writing

**Applies when**: researchers use AI tools (ChatGPT, Claude, Copilot, Gemini, etc.) during research — for writing assistance, summarising literature, exploring analytical ideas, or processing data.

AI tool use is governed by the classification tier of the data being processed:

- **Green/Yellow data**: general-purpose AI tools are acceptable. Published data, public documents, draft text, and literature summaries carry no restriction.
- **Red data**: do not upload, paste, or input identifiable personal data into general-purpose AI tools. Enterprise tools within CMI's M365 ecosystem (Microsoft Copilot with M365 data protections) may be acceptable. If using an external AI tool for Red-tier tasks, it must have a DPA and no-training policy.
- **Black data**: no AI tool use. Period.

**The practical boundary**: the question is not "are you using an AI tool?" but "what data are you putting into it?" A researcher using ChatGPT to draft a literature review section is fine. The same researcher pasting interview transcript excerpts into ChatGPT to help with coding is not (if the transcripts contain identifiable data).

**Practical guidance**:
- **Translation**: for translating documents containing personal data, use enterprise tools with DPA or translate manually. Do not paste identifiable data into Google Translate or similar consumer tools.
- **Summarising and analysis**: AI tools can be used to analyse anonymised or de-identified data. They should not be used to process identifiable personal data.
- When in doubt, anonymise or de-identify excerpts before using AI tools. Do not paste raw interview data, participant names, contact lists, or identifiable survey responses into consumer AI tools.
- **Check CMI's institutional AI policy** for the latest boundaries on acceptable AI use in research. The classification-based rules above are consistent with the AI policy but the policy may contain additional requirements.

**Escalation**: consult the RDM contact (rdm@cmi.no) if research data has been inadvertently uploaded to a consumer AI tool, or if no enterprise AI tool meets the project's requirements.
