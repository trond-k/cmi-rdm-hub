---
icon: lucide/send
---

# Sikt Notification Form — A CMI Guide
*Trond Kvamme · 20 min read*

<!-- Manual content for the RDM Hub.
     Located at: /content/manual/before/sikt-notification.md

     This is a walkthrough of the Sikt notification form from CMI's
     institutional perspective. It explains what each section asks,
     what CMI's typical answers are, and where the common pitfalls lie.

     This is the static guide. The dynamic Sikt Guide tool (accessible
     from a project page) can suggest specific answers for a specific
     project based on the parsed description and data inventory. -->

## What the Sikt notification is (and isn't)

The Sikt notification is a requirement for research projects that process personal data. Since most CMI research involves identifiable participants, most CMI projects need one. File it before data collection begins.

Two things to understand clearly:

**It is not an approval.** Sikt does not approve or reject your research design. The notification tells Sikt that data processing will take place and describes the processing and safeguards. Sikt's role is to assess whether what you describe is consistent with data protection requirements and to advise if they see concerns.

**It is not a barrier.** The form looks long, but most sections have straightforward answers for typical CMI projects. If you know your project's methods, participants, and data, you can fill it in within an hour. The guide below tells you what CMI typically answers for each section and where you actually need to think.

The form deals with concepts from the GDPR — lawful basis, special categories, data subject rights, third-country transfers. If any of these are unfamiliar, the [GDPR demystifier](gdpr-demystifier.md) explains each one in plain language with CMI-specific guidance.

!!! tip "Use the Sikt Guide tool"
    If you have created a project in the Hub, the Sikt Guide can suggest answers for each field based on your project description and data inventory. This walkthrough explains the form; the tool does the filling.

## Before you open the form

The Sikt form is easier and faster if you gather what you need before you start. Here is what to have ready:

- **Project description** — title, summary, methods, and participant groups. If you have a proposal or project document, keep it open for reference.
- **Draft information letter** — Sikt asks you to upload it. The [Informing participants](informing-participants.md) page has CMI's template and guidance on adapting it.
- **Knowledge of your participant groups** — who they are, approximately how many, where they are located, and whether any are in vulnerable categories (refugees, children, people in conflict zones, ethnic minorities).
- **Personal data categories you will process** — both general (name, contact info, recordings, background details) and special (health, ethnicity, political opinions). Think about what will come up in interviews, not just what you plan to ask directly.
- **Storage and security plan** — which systems you will use (M365, TSD, other), encryption, access controls. CMI's [data security policy](../../institutional/data-security.md) describes the approved infrastructure.
- **Partner and collaboration arrangements** — are there joint controllers? Data processors (transcription services, survey firms)? Partners in countries outside the EU/EEA?
- **Estimated project timeline** — when data collection starts, when the project ends (including any data retention period beyond active research).
- **Any required approvals** — REK approval if the project falls under the Health Research Act, or other permissions specific to your fieldwork context.

Sikt also recommends preparing questionnaires or interview guides for upload, and checking your institution's security guidelines before you begin.

**About the Sikt portal:** The form lives at [minforskning.sikt.no](https://minforskning.sikt.no). When you start a new notification, Sikt asks you to create or select a project in their "My Research" system. If this is your first notification, you will create a new project. If you are amending a previous notification, select the existing project — you do not need to start over.

## CMI quick-reference defaults

For a typical CMI research project, these are the standard answers. Your project may differ — the section-by-section guide below explains when and why.

| Field | CMI default |
|---|---|
| Data controller | CMI (Chr. Michelsens Institutt) |
| Academic level | Research/PhD project |
| Primary purpose | Research or student paper |
| Lawful basis (Art. 6) | Research in the public interest |
| Lawful basis (Art. 9) | Research in the public interest |
| Primary storage | M365 (Teams/SharePoint/OneDrive) |
| Security measures | Encrypted storage, encrypted transmission, restricted access, MFA |
| Default retention | 10 years (primary data), 5 years (admin records) |
| Data at project end | Anonymisation (delete key, strip identifiers, delete recordings) |
| Identifiable in publications | No (default is anonymisation) |

## Section by section

### 1. Personal data types

**What it asks**: which categories of personal data your project will process, split into general categories (name, contact info, recordings, etc.) and special categories (health, ethnicity, political opinions, etc.).

**How to approach it**: Go through the list and check everything that applies. The common mistake is under-reporting — researchers check "name" and "voice on audio recordings" but forget that their interview data also contains background information that, combined, could identify someone. If you're doing qualitative research, you almost certainly need to check "background information that, when combined, can be used to identify an individual."

**For special categories**: CMI's GDPR positions document explains that special category data is common in CMI research and often arises incidentally. Don't over-classify (an interview about municipal budgeting where someone mentions attending a mosque is not automatically "religious beliefs"), but don't under-report either. If your research topic is governance, conflict, migration, or health, you will likely need to check at least one special category. The most common ones for CMI projects are:

- **Health data** — any project involving health outcomes, wellbeing, disability, or access to health services
- **Ethnicity** — any project where participants are identified by or selected based on ethnic, national, or minority group membership
- **Political opinions** — any project directly studying political participation, governance critique, or political mobilisation

If in doubt, check the box. It's better to declare and explain than to omit and have Sikt flag it later.

### 2. Data controller

**What it asks**: which institution is responsible for the project, who the project leader is, and whether multiple institutions share responsibility (joint controllers).

**CMI's default**: CMI (Chr. Michelsens Institutt for Videnskap og Åndsfrihet) is the data controller. The project leader is the PI — they must be formally affiliated with CMI.

**Joint data controllers**: this is where CMI's position on partnerships matters. If another institution (e.g., a university partner) co-determines the purposes and means of data processing — meaning they independently design research questions, collect data, and conduct analysis — then you likely have joint controllers. This is common for CMI's international research collaborations.

Select "Yes" for joint data controllers if:

- A partner university independently collects data as part of the project
- Both institutions co-designed the research and share decision-making over the data

Select "No" if:

- You have a contracted data collection firm (they are a data processor, not a controller)
- A partner provides you with existing data but doesn't co-determine your research
- You have individual research assistants working under your instruction

If you select "Yes," you will need a joint controllership agreement (see REC-PARTNER-01 in the recommendations). Prepare this before or alongside the notification.

### 3. Project information

**What it asks**: project title, summary, funding source, and academic level.

**Straightforward for CMI**: enter the project title and a brief summary. For funding, most CMI projects select "The Research Council of Norway" or "Other" (for Norad, EU, bilateral agreements, etc.). Academic level is "Research/PhD project" for all CMI research. If a PhD student is involved, this still applies — the project itself is a research project even if it includes a PhD component.

You can upload the full project description if the project is complex. This helps Sikt's assessor understand what you're doing. For large RCN or EU proposals, uploading the description is recommended.

### 4. Purpose

**What it asks**: the primary purpose of processing, a description of the research and why personal data is necessary, and the number of data subjects.

**Primary purpose**: select "Research or student paper" for almost all CMI projects. Select "Health research" only if the project falls under the Health Research Act (clinical trials, health registry studies, etc.) — most CMI health-related research is social science research *about* health, not health research in the regulatory sense.

**Description**: explain what you're researching and why you need personal data to do it. Keep it concise but specific. Sikt wants to see that there's a genuine research purpose and that personal data is necessary — not that anonymised or aggregate data would serve equally well. A sentence or two is often enough: "The project studies [topic] through [methods] with [participants]. Personal data is necessary because [reason — typically: the research requires understanding individual experiences, perspectives, or circumstances that cannot be captured through anonymised or aggregate data]."

**Number of data subjects**: select the range. For most CMI qualitative projects, this is "1-99." For larger mixed-methods or survey projects, estimate the total number of people whose personal data you'll process — including interviewees, survey respondents, and anyone identifiable in field notes or administrative records.

### 5. Legal basis

**For general personal data (Article 6)**: select **"Research in the public interest."** This is the standard legal basis for research projects in Norway. Sikt's own guidance states that "in many projects, public interest will be a more appropriate basis for processing" than consent, and that "research, as a general rule, is considered to be in the public interest" (see [Sikt's guidance on legal bases](https://sikt.no/en/legal-basis-personal-data-processing-research)). The [GDPR demystifier](gdpr-demystifier.md#public-interest-article-61e) explains the public interest basis and why CMI uses it as the default.

The form's intro text notes that "in student projects, the most common basis is consent." For research projects — whether at CMI, universities, or other research institutions — public interest is the standard basis.

Why not consent? Sikt identifies several situations where public interest is more appropriate, many of which apply routinely to CMI projects: long-duration or complex projects where future processing is hard to predict; research involving vulnerable groups where the requirements for valid consent may be difficult to meet; imbalanced power dynamics; and situations where documenting consent is impractical or culturally inappropriate. More broadly, consent as a lawful basis creates withdrawal instability (a participant who withdraws triggers a legal obligation to delete their data, which can seriously impair ongoing research) and specificity problems (qualitative research is inherently exploratory). The [GDPR demystifier entry on consent](gdpr-demystifier.md#gdpr-consent-article-61a) explains the strict GDPR requirements and why they are problematic for most research.

Importantly, using public interest as the legal basis does not mean participants are not asked for consent. Participants still give ethical consent to participate — they are informed, they agree voluntarily, they can withdraw from the research. But the *legal basis* for processing their data is public interest, not their consent.

**For special category data (Article 9)**: select **"Research in the public interest."** This invokes Article 9(2)(j) — processing necessary for scientific research purposes with appropriate safeguards.

**Supplementary legal basis and approvals**: most CMI projects do not need supplementary legal bases (these are mainly for health registry access, patient records, etc.). If your project involves accessing Norwegian health registries or patient records, you may need REK approval or confidentiality exemptions — consult the RDM Adviser.

!!! warning "The consent-public interest distinction matters for the rest of the form"
    Your choice here affects how you describe information to participants (Section 6), how you handle data subject rights (Section 8), and what happens at project end (Section 11). The Sikt Guide tool applies CMI's positions consistently across all sections.

### 6. Samples

**What it asks**: describe each distinct group of participants ("sample"), how you'll recruit them, their age range, whether vulnerable groups are included, which personal data categories apply to them, how data will be collected, and how they'll be informed.

**Create a sample for each distinct participant group.** If your project interviews government officials and also conducts household surveys with community members, these are two samples with different characteristics, data types, and information needs. Don't collapse them into one.

**Vulnerable groups**: Sikt's list includes patients, disabled people, ethnic minorities, asylum seekers, and children. Many CMI participant groups fall into these categories — refugees, people in conflict-affected areas, economically marginalised communities. Check the relevant boxes honestly. This doesn't prevent your research; it tells Sikt that you've considered the implications.

**"Persons residing in countries outside the EU/EEA"**: check this for essentially every CMI fieldwork project. It applies whenever your participants are located outside the EU/EEA, which is most CMI research sites (Sub-Saharan Africa, South and Southeast Asia, the Middle East, Latin America).

**How data is collected**: select all methods that apply. For a typical CMI qualitative project: "Personal interview." For mixed-methods: "Personal interview" and "Online survey" (or "Paper-based survey"). For ethnographic work: "Participant observation" in addition to interviews. "Workshop" is available for co-design or participatory research methods.

**Information to the sample**: select "Yes" — participants will receive information about data processing. This is the information letter, not GDPR consent. For the delivery method, select "Written (on paper or electronically)" for most contexts. Select "Oral" only when written delivery is genuinely inappropriate (see REC-CONSENT-02 for guidance on oral information delivery in fieldwork contexts). The [Informing participants](informing-participants.md) page has CMI's template and detailed guidance on adapting it to different contexts, literacy levels, and languages.

You will be asked to upload the information letter. Prepare it before filing the notification. The Hub's Information Letter Generator can help draft one based on your project.

!!! note "Multiple samples mean multiple information letters"
    Or one letter with clearly differentiated sections. Frontline workers and community members need different information because their relationship to the research, the data collected about them, and their vulnerability context are different.

### 7. Third persons

**What it asks**: whether your project collects information about people who are not direct participants — people that your participants talk about.

**This is common in CMI research.** An interview about governance may involve the participant describing their supervisor, local officials, or community members by name or in identifiable terms. An interview about household dynamics may include information about family members who aren't participating in the research.

Select "Yes" if:

- Participants will describe identifiable individuals who are not themselves participating
- Your interview protocol asks about specific people (e.g., "describe your experience with [role/person]")
- Focus groups may involve participants naming or describing third parties

Select "No" if:

- Your research focuses on the participant's own experiences without reference to identifiable third parties
- Any third-party references will be at a level of generality that doesn't identify individuals

If "Yes," you'll need to describe who the third persons are and whether they'll be informed. In most CMI research, informing third persons is not practicable (you don't know in advance who participants will mention). Explain this straightforwardly: "Third persons cannot be informed because their identities are not known to the researchers prior to data collection. Information about third persons will be anonymised in transcripts and publications."

### 8. Documentation (data subject rights)

**What it asks**: how participants can access, correct, or delete their personal data.

**CMI's standard answer**: "Participants can contact the project leader [name, email] or CMI's data protection contact [email] to request access to their personal data, request corrections, or request deletion. Requests will be handled in accordance with GDPR Articles 15-17 and the Norwegian Personal Data Act §17. Under the public interest basis, the right to erasure may be limited where deletion would seriously impair the research objectives (Article 17(3)(d)), but CMI's default practice is to accommodate deletion requests unless there is a documented, compelling reason to retain the data."

This is largely boilerplate, but it must be consistent with your choice of legal basis in Section 5. Under public interest, data subject rights are modified — the right to erasure is limited, and the right to data portability does not apply. The Sikt Guide tool inserts the correct rights language based on your legal basis.

### 9. Security measures

**What it asks**: whether identifiable data is stored separately, which technical measures are used, where data is processed, and a description of the data flow.

**Stored separately**: Sikt recommends using a linkage key (pseudonym) and storing identifiable data (names, contact details) separately from research data. For most CMI projects, this is good practice. Select "Yes" if you're using pseudonymised data with a separate key. Select "No" if the data is inherently identifiable and separation isn't practical (e.g., audio recordings where voice is the identifier) — and explain why.

**Technical and practical measures**: for a typical CMI project using M365 infrastructure, check:

- **Encrypted storage** (M365 provides encryption at rest)
- **Encrypted transmission** (M365 provides encryption in transit)
- **Restricted access** (Teams/SharePoint access controls)
- **Multi-factor authentication** (CMI's M365 requires MFA)

If using TSD, check all of the above plus note TSD's additional security in the data flow description. If fieldwork involves mobile devices, also check relevant measures and describe device encryption in the data flow. CMI's [data security policy](../../institutional/data-security.md) describes approved platforms and their security characteristics in detail.

**Where data is processed**: for CMI's standard infrastructure, select "Hardware" (CMI's M365 environment). If using TSD, also select "Hardware." If fieldwork involves tablets or phones, also select "Mobile devices." **Do not select "Private services"** — CMI's data security policy does not permit personal cloud services for research data.

**Data flow description**: this is the most important free-text field in this section. Describe the journey of data from collection to storage to analysis to deletion. For a typical CMI fieldwork project, something like:

> "Data is collected on encrypted tablets/recorders during fieldwork in [country]. Recordings and survey data are uploaded to CMI's M365 environment (Teams/SharePoint with restricted access) via encrypted connection when internet connectivity is available. Local copies are deleted after confirmed upload. Transcription is performed by [project staff / named service with DPA]. Transcripts are stored in M365 with access restricted to the project team. The anonymisation key linking pseudonyms to participant identities is stored in a separate M365 location accessible only to the PI. Analysis is conducted on CMI workstations connected to the institutional network."

Adapt this to your actual data flow. If you use TSD, Tresorit, or other platforms, describe those instead. The Data Security Policy has details on each platform's characteristics.

### 10. Recipients

**What it asks**: who has access to personal data and whether data is transferred to a third country (outside the EU/EEA).

**Who has access**: check all that apply. For a typical CMI project:

- **Project leader**: always
- **Internal co-workers**: if other CMI staff are on the project team
- **External co-workers/collaborators inside the EU/EEA**: if you have European partner institutions
- **Data processor**: if you use a contracted data collection firm, a transcription service, or any external service that processes personal data on your behalf

**Third-country transfer**: this is triggered by almost every CMI project. The [GDPR demystifier](gdpr-demystifier.md#third-country-transfer) explains what counts as a third-country transfer and the available legal mechanisms. Select "Yes" if:

- Your research partner (e.g., UNZA, a university in Ethiopia) will have access to personal data
- A US-based partner (e.g., a US university) will receive data for analysis
- A contracted data collection firm in a non-EEA country holds data during the collection phase
- You use a cloud service that processes data outside the EEA (though CMI's M365 EU Data Boundary reduces this concern for most tools)

**Legal basis for the transfer**: Sikt offers three options. For most CMI international research collaborations:

- **"Derogations for specific situations (Art. 49)"**: this includes the [research derogation](gdpr-demystifier.md#research-derogation-article-491d) — transfers necessary for important reasons of public interest, including scientific research. This is the simplest basis for CMI's typical fieldwork and collaboration transfers.
- **"Covered by necessary safeguards (Art. 46)"**: use this if you have a joint controllership agreement or a DPA with the partner, which provide contractual safeguards.
- **"Decision on adequate level of protection (Art. 45(3))"**: use this only if the recipient country has an EU adequacy decision (e.g., UK, Japan, South Korea, Canada — but not the US under a blanket adequacy, and not most CMI fieldwork countries).

For each third-country organisation, add an entry with the organisation name, country, and legal basis. Use the comment field to briefly explain the transfer arrangement (e.g., "UNZA is a joint controller under Article 26 agreement. Data is shared for collaborative research analysis.").

!!! tip "This is where the form gets tedious for CMI"
    A project with partners in Zambia, the US, and Ethiopia means three separate third-country entries with three legal basis selections and three comments. The Sikt Guide tool can pre-fill these from your data inventory's partnership records.

### 11. End of project

**What it asks**: project start and end dates, what happens to data at the end, and whether participants will be identifiable in publications.

**Project dates**: "project start" means when personal data processing begins (first contact with participants, first data collection). This is not the project's formal start date if setup precedes data collection. "Project end" means when data is anonymised, deleted, or archived — not when the last paper is published. This is typically the project end date plus the retention period, but Sikt asks for it as a single date.

**What happens to data**: for most CMI projects, select **"Personal data will be anonymised"** as the primary endpoint. Check:

- "The identification key will be deleted" (this converts pseudonymised data into anonymised data)
- "Personally identifiable information will be removed, re-written or categorized"
- "Any sound or video recordings will be deleted" (if applicable)

If you plan to archive data for reuse (which CMI encourages for data that can be meaningfully anonymised), you may select "Personal data will be stored temporarily" — meaning identifiable data is retained for the retention period (10 years) before anonymisation and archiving. Describe the retention purpose as "Documentation purposes" or "Archiving for data sharing and reuse."

**Identifiable in publications**: select "No" for almost all CMI projects. The default is anonymisation in publications. Select "Yes" only if you have specific consent from participants to use their real names — typically for public figures who have agreed to be quoted by name, or for participatory research where participants have chosen to be identified.

### 12. Additional information

**What it asks**: anything else relevant to Sikt's assessment.

**Use this field for context that doesn't fit elsewhere.** For CMI projects, this is a good place to note:

- Specific fieldwork security considerations for high-risk contexts
- That a joint controllership agreement is in preparation (if not yet finalised)
- Any unusual data collection methods or participant engagement approaches

Keep it brief. A few sentences of context can help Sikt's assessor understand your project without follow-up.

### 13. Privacy risk and DPIA

**What it asks**: whether your project requires a Data Protection Impact Assessment, and if so, a set of detailed questions about risk, transparency, data minimisation, accuracy, storage, and access. The [GDPR demystifier](gdpr-demystifier.md#data-protection-impact-assessment-dpia) explains what a DPIA is and when it is triggered.

**Does your CMI project need a DPIA?** The form lists ten risk factors. If two or more apply, a DPIA is generally expected. For typical CMI projects:

Factors that commonly apply:

- **Highly personal information**: yes, if you process health data, political opinions, or other special categories
- **Persons residing outside the EU/EEA**: yes for most CMI fieldwork (Sikt doesn't list this explicitly, but it's a factor they consider)
- **Vulnerable groups**: yes if your participants include refugees, people in conflict zones, economically marginalised communities

Factors that sometimes apply:

- **Large scale**: yes for survey projects with thousands of participants; no for most qualitative projects
- **Long duration**: yes if the project runs more than 10 years (rare for CMI)
- **Matching or combining datasets**: yes if you're linking survey data with administrative records or combining data from multiple sources

Factors that rarely apply to CMI research:

- **Automated decision-making**: almost never
- **Systematic monitoring**: almost never (unless GPS tracking or similar)
- **Evaluation or profiling**: rarely, unless the research involves individual-level performance assessment

**If a DPIA is required**: answer the detailed questions honestly and concisely. The key principle is proportionality — describe what you're doing, acknowledge the risks, and explain the safeguards. You don't need to eliminate all risk; you need to demonstrate that you've thought about it and taken reasonable measures.

For the free-text fields:

**Consulting data subjects**: if you've used co-design methods, community consultations, or advisory panels, describe them. If not (which is common for many CMI projects), explain why: "Direct consultation with data subjects was not feasible given the fieldwork context and the geographic distribution of participants. The research design was reviewed by [ethics committee / institutional review board] which includes assessment of participant perspectives."

**Transparent and fair**: describe how the information letter explains the research, how you ensure participants understand what's happening with their data, and any adaptations for vulnerable groups (simplified language, oral delivery, local language translation).

**Purpose clearly defined**: straightforward for research with clear research questions. Note that qualitative research is inherently exploratory, but the overall purpose (studying X through Y methods) is defined.

**All data necessary**: explain why personal data is needed and why the research can't be done with less. For qualitative research: individual experiences, perspectives, and contexts cannot be captured through anonymised or aggregate data.

**Data accuracy**: for interview data, accuracy is ensured through the research relationship — participants describe their own experiences. For survey data, describe validation measures (piloting, consistency checks). Note that "accuracy" in qualitative research is about faithful representation, not statistical precision.

**Storage period**: reference CMI's default retention (10 years for primary research data, 5 years for administrative records).

**Responsibility and roles**: describe the partnership structure. Name joint controllers and data processors. Reference the agreements you have or are preparing (joint controllership agreement, DPA).

**Access and systems**: list approximately how many people will have access, from which organisations, and through which systems (M365, TSD, etc.).

!!! tip "The DPIA section is where many researchers get stuck"
    If you can't answer all the questions, Sikt's own guidance says to leave fields empty and submit — an advisor will contact you to help. This is a reasonable approach if you're unsure, but the Sikt Guide tool can draft answers for most of these fields based on your project description and data inventory.

## After you submit

Once you submit the notification, Sikt takes over. Here is what to expect.

**Assessment timeline.** Sikt aims to complete assessments within 30 days. Low-risk projects — those without special category data, vulnerable groups, or third-country transfers — may receive an automatic same-day assessment. Standard assessments are reviewed by a Sikt adviser. The busiest period is November through February, when many projects file before spring data collection. Filing early gives you a buffer.

**What Sikt may come back with.** Sikt's response is advisory, not adversarial. Common feedback includes questions about your information letter (wording, completeness, consistency with the notification), requests for clarification on data flow or security measures, and suggestions for additional safeguards. If Sikt asks for changes, it is because they want the notification to accurately reflect your processing — not because your research is being questioned.

**Responding to Sikt.** Log into [minforskning.sikt.no](https://minforskning.sikt.no) to message the adviser assigned to your notification directly. Phone support is available Monday, Tuesday, and Thursday, 10:00–12:00.

**Amendments.** If the project changes after assessment — new data types, new partners, a changed timeline, an extended end date — notify Sikt through the portal. You do not need to re-submit the full form. Instead, you report changes to the existing notification and the adviser will review the update.

**Project completion.** When the project ends, report completion through Sikt's portal. This confirms that data has been anonymised or deleted as described in the notification. Closing the notification is a requirement, not just a formality — it tells Sikt (and your institution) that the data processing you described has ended as planned.

## Tips for a smooth notification

**File early.** Sikt's processing time varies. Filing well before data collection gives you time for any back-and-forth.

**Be specific but concise.** Sikt's assessors read hundreds of notifications. Clear, specific descriptions get faster assessments than vague or overly detailed ones.

**Don't overthink it.** The notification describes what you plan to do. It's not a contract. If your project evolves (new data types, new partners, changed timeline), you can amend the notification.

**Use the Hub tools.** The Sikt Guide can pre-fill most fields. The Information Letter Generator can draft the letter you need to upload. The Data Inventory tells you which personal data categories to check and which security measures to describe.
