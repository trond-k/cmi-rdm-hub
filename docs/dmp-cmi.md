# Data Management Plan — CMI Institutional Template

<!-- CMI's own institutional DMP template, derived from the structure used in actual CMI
     project DMPs (ATTACH, CoM-Financing, StaR, Fisher of Corpses, RETURNEC). Unlike the
     funder templates (Science Europe, RCN, Horizon Europe), this is structured around how
     CMI actually writes DMPs: guiding principles up front, roles broken down by institution,
     legal/ethical considerations as an integrated block, and a data inventory annex populated
     from the parsed project description.

     This template is deliberately concise. The full institutional positions on GDPR, data
     security, open science, and standard recommendations are already in the system prompt
     (loaded from the institutional/ content files). The template defines the SECTION STRUCTURE
     and short CMI defaults — the LLM synthesises the detailed guidance from the policy
     documents when filling in each section. -->


## 1. Introduction

### 1.1 Purpose and scope of the DMP

- State that this DMP outlines the project's approach to managing research data responsibly, ethically, and transparently.
- Note commitment to legal compliance, institutional policies, and the FAIR principles.
- **CMI default:** "This DMP is a living document and will be revised as the project evolves."

### 1.2 Guiding principles

- Describe the principles guiding the project's data management, tailored to the project context.
- **CMI default principles** (include all that apply, adapt language to the project):
  - **FAIR, transparency, and security:** FAIR balanced with ethical responsibility and participant protection. "As open as possible, as closed as necessary."
  - **Do-No-Harm:** No action, output, or outcome shall adversely affect participants, stakeholders, or third parties.
  - **Sensitivity minimisation:** Only data essential to the research objectives will be collected and retained.
  - **Proportionality:** Security measures matched to the sensitivity and risk level of each dataset.
  - **Access control (principle of least privilege):** Role-based, limited to individuals with a justified need.
  - **Shared responsibility:** All project members share accountability for lawful and ethical data management.
- **Context-specific principles** — add where relevant:
  - **Conflict sensitivity:** for projects in conflict-affected or politically sensitive contexts.
  - **CARE principles:** for research involving communities in the Global South (Collective benefit, Authority to control, Responsibility, Ethics).
  - **Data sovereignty:** for projects involving indigenous or marginalised communities.


## 2. Project data summary

### 2.1 About the project

Format each field as its own paragraph using **Label:** Value, with a blank line between fields:

- **Full title:** the project's full title
- **Acronym:** if applicable
- **Funding source:** funder name and programme
- **Grant ID:** grant or project number
- **Project period:** start date – end date (duration)
- **Geographical scope:** countries and regions

Follow the metadata fields with the research objective in one to two paragraphs.

### 2.2 Purpose of data collection

- Why data is collected, organised by work package or research question.
- How each major data collection activity contributes to the project's objectives.


## 3. Roles and responsibilities

### 3.1 Institutions

- List all institutions and describe each one's role in data management.
- **CMI default:** "Chr. Michelsen Institute (CMI), Norway — Host institution and project coordinator. CMI is responsible for overall project management, data storage and security, GDPR compliance, and repository deposit of open-access publications. CMI's Research Data Management Adviser supports development of the Data Management Plan."
- For each partner institution: what data they collect/process/store, their controller or processor role, any infrastructure they provide.
- Note external compliance partners (e.g., Sikt Data Protection Services for Research).

### 3.2 Governance and project groups

- Describe the project's internal governance for data management.
- **CMI default elements** (adapt to project scale): core leadership team or PMT chaired by the PI; ethics oversight (CMI Research Ethics Committee, external ethics boards); data protection coordination (CMI's Data Management Adviser, DPO, Sikt); advisory board or stakeholder group if applicable.


## 4. Legal and ethical considerations

### 4.1 GDPR compliance

- State whether the project processes personal data and from whom.
- Note which data protection frameworks apply (GDPR, partner-country legislation).

#### 4.1.1 Legal basis for processing

- **CMI default:** public interest (GDPR Art. 6(1)(e)), supported by the Norwegian Personal Data Act §8 and GDPR Art. 89. This applies to all CMI research — not limited to registry-based or large-scale studies.
- For special category data: Art. 9(2)(j) — scientific research purposes.
- **Two-track consent:** GDPR consent is NOT the lawful basis for general data processing. It supplements public interest for specific bounded activities only: recording, name use in publications, archiving for future reuse. Apply the institutional GDPR positions on consent.

#### 4.1.2 Types of personal data

- List categories: direct identifiers, indirect identifiers, special category data (Art. 9), other sensitive data (financial, immigration, etc.).
- Note any third-person data in interviews or field notes.

#### 4.1.3 Information and consent

- **The information letter is the primary instrument** — it informs, it does not ask for GDPR consent to process data.
- **Separate consent elements** for: recording, name use, archiving for reuse.
- Describe how voluntariness is ensured (gatekeepers, power dynamics).
- Describe adaptation for fieldwork contexts (oral delivery, high-risk settings). Apply institutional positions on information letters and consent.

#### 4.1.4 Data minimisation and anonymisation

- Describe how data minimisation is applied and the anonymisation/pseudonymisation strategy.
- **CMI default:** direct identifiers removed or pseudonymised as early as possible. Linkage keys stored separately, accessible only to PI and designated data steward.

#### 4.1.5 Data security

- **CMI default:** M365 ecosystem with encryption, MFA, role-based access, tiered restrictions by sensitivity.
- For higher assurance: TSD/Nettskjema, Tresorit, or Proton Drive. Apply institutional Data Security Policy positions for storage tier selection.
- For fieldwork: device encryption, daily upload, local encrypted backup. **CMI default:** recordings uploaded within 24 hours, deleted from local devices after verification.

#### 4.1.6 Data subject rights

- Under the public interest basis, rights are modified by Art. 89(2) and the Norwegian Personal Data Act §17. Apply the institutional GDPR positions — in particular: no GDPR consent to withdraw (only ethical withdrawal and right to object); right to erasure is limited (Art. 17(3)(d)); right to data portability does not apply.
- The information letter should include a concrete deadline after which deletion may no longer be feasible.

#### 4.1.7 International data transfers

- State whether personal data crosses borders, between which countries, and under what circumstances.
- Apply CMI's proportional approach from the institutional GDPR positions: practical safeguards for CMI researchers abroad and research assistants; joint controllership agreements (Art. 26) preferred over SCCs for partner institutions; research derogation (Art. 49(1)(d)) as an alternative; platform-based solutions for US-based partners.

#### 4.1.8 Retention and disposal

- **CMI default retention periods:** primary research data 10 years; administrative records 5 years; contact information up to 3 years (if stated in information letter); audio/video recordings deleted after transcription unless they are the research data; consent documentation retained as long as related data exists.
- Describe the deletion procedure across all systems including partner copies. **CMI default:** maintain a deletion log.

### 4.2 Intellectual property rights and data ownership

- Identify data ownership. For multi-partner projects: describe how ownership is formalised (partnership agreements, joint controllership).
- **CMI default:** publications under CC BY 4.0 deposited in CMI's institutional repository. Datasets under CC BY 4.0 or CC0.
- Note licensing terms for external or secondary data.

### 4.3 Research ethics

- Describe the ethical context — what makes the project ethically sensitive.
- **Key ethical issues** — select and adapt: emotional/psychological distress; social/reputational risks; legal/administrative consequences; professional/institutional risks; physical security risks; power dynamics; third-party risks.
- **Mitigation measures** — describe specific actions.
- **Ethical guidelines and oversight:**
  - **CMI default:** NESH guidelines. CMI Research Ethics Committee is advisory, not approval-based — consultation is voluntary but encouraged for ethically complex projects.
  - List applicable frameworks (Declaration of Helsinki, ALLEA, Good Clinical Practice, Montreal Statement, etc.).
  - **Approvals and notifications:** Sikt notification (required, filed 30+ days before data collection); CMI REC consultation (voluntary); REK (only for medical/health research); partner-country ethics boards.


## 5. Expected data and sensitivity

- Overview of data types organised by sensitivity level.
- **CMI classification:** Green/Yellow/Red/Black based on risk of harm from exposure. Personal data is Red by default. Apply the institutional Data Classification Scheme for tier definitions and examples.
- A single project will typically have data objects at multiple tiers. Classification applies to the data object in its current state.
- Reference the Data Inventory (Annex 1) for details.
- For secondary data: describe source, access conditions, and sensitivity.


## 6. Processing, quality, and analysis

- Describe the data processing pipeline from collection through to analysis-ready form.
- Transcription procedures (who, when, what language).
- Anonymisation/pseudonymisation steps in the pipeline.
- Quality assurance: during collection (training, pilots, back-translation, validation) and after (cleaning, consistency checks, transcription verification).
- Analysis tools (NVivo, MAXQDA, Atlas.ti, Stata, R, SPSS, etc.).
- Cross-work-package coordination if applicable (shared codebooks, analysis workshops).


## 7. Data documentation, metadata standards, and archiving

### 7.1 Documentation

- **CMI default:** "At minimum, each dataset should have a README file describing the data contents, collection context, variable definitions, and any known limitations."
- Additional documentation: codebooks, interview guides, observation protocols, data dictionaries.

### 7.2 Metadata standards

- Recognised metadata standards (DDI for survey data, Dublin Core for general datasets).
- File naming conventions and folder structure.

### 7.3 Data sharing and archiving

- Apply CMI's five sharing pathways from the institutional Open Science Policy: open access, registered access, controlled access, restricted access, no external sharing. Select the most open pathway feasible for each dataset.
- **CMI default:** "Open as possible, closed as necessary." Restriction requires specific justification.
- Note that full sharing of qualitative data is rarely feasible — controlled access to de-identified excerpts or metadata-only records is the realistic pathway.
- **Metadata is always shared** unless it creates risk.
- **CMI default repositories:** Zenodo (open datasets, code, supplementary materials), OSF (replication packages combining data, code, and manuscripts), openICPSR (quantitative social science data), QDR (qualitative data with mediated access — per-deposit fees apply), Sikt's Research Data Archive (quantitative survey data), CMI internal repository (minimum baseline).
- **CMI default embargo:** 1–2 years after project completion.
- **CMI default licences:** CC0 (preferred) or CC BY 4.0 for data. MIT/BSD/Apache 2.0 for code.


## 8. Monitoring and updates

- **CMI default:** "This DMP is a living document and will be revised as the project progresses."
- **CMI default:** PI and CMI's Research Data Management Adviser are jointly responsible.
- **CMI default review points:** after ethical approvals; at project mid-point; before archiving and final outputs; ad hoc for significant changes.
- Updates logged with version numbers, dates, and description of changes.


## Annex 1: Data inventory

The data inventory lists all research data records collected or generated by the project. Each record represents a coherent data collection activity — not an individual file. The inventory is derived from the parsed project description and should be reviewed and amended by the researcher.

For each data record, describe:

- **Name and description:** What this data is and where it comes from.
- **Collection method:** How the data is collected or generated.
- **Participant group:** Which participant group(s) this relates to, if applicable.
- **Formats and estimated volume:** Expected file formats and approximate size or number of records.
- **Artifacts:** Concrete data objects produced (e.g., audio recordings, transcripts, anonymised datasets, coded datasets, field notes).
- **Data flow:** How data moves from collection through processing to end state.
- **Personal data categories:** What personal data is involved, if any.
- **Sensitivity level:** Green/Yellow/Red/Black classification (per section 5).
- **Responsible party:** Who collects, stores, and manages this data.
