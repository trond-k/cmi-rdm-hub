# Recommendation #2: Initial Assessment & Classification

## Rationale

Early assessment of research data enables appropriate storage, security, and documentation from project start. By classifying data entities and project risk at intake, rdm@cmi can provide tailored recommendations and identify compliance requirements (DMP, DPIA, ethics review, contracts) before data collection begins.

## Core Recommendation

rdm@cmi is connected to all new research projects at initiation. Based on project proposals and descriptions, an initial assessment identifies data entities, assigns preliminary sensitivity and risk classifications, and determines documentation requirements. This assessment drives automated generation of project-specific recommendations and document templates.

## Implementation

### 2.1 Intake Trigger

**When:** rdm@cmi is notified when a new project is confirmed (contract signed / funding awarded).

**Optional early engagement:** For complex or high-risk projects, rdm@cmi can be consulted at proposal stage to advise on data management plans and budget for RDM activities.

**How:** Notification via:
- Automatic alert when new project Team is created, or
- Manual notification from project administration/finance, or
- Regular check-in with research coordinators

### 2.2 Intake Process

**Step 1: Documentation gathering**

rdm@cmi collects available project documentation:
- Proposal / grant application
- Contract / award letter
- Funder requirements
- Ethics applications (if submitted)
- Consortium agreement (if applicable)

**Step 2: Initial assessment (LLM-assisted)**

Using project documentation, rdm@cmi (with LLM assistance) identifies:

| Element | Description |
|---------|-------------|
| **Data entities** | Distinct data types, samples, or products in the project (see 2.3) |
| **Sensitivity classification** | Per data entity (see 2.4) |
| **Project risk level** | Overall project complexity and risk (see 2.5) |
| **Compliance requirements** | DMP, DPIA, ethics, contracts needed (see 2.6) |

**Step 3: Verification**

Assessment is reviewed with PI/project coordinator to:
- Confirm data entities are correctly identified
- Validate or adjust classifications
- Clarify any ambiguities
- Identify any data not apparent from documentation

**Step 4: Recommendations generated**

Based on confirmed classifications, rdm@cmi generates:
- Storage and security recommendations
- Document bundle (see Recommendation #4)
- Data inventory template (see Recommendation #3)

### 2.3 Identifying Data Entities

A **data entity** is a distinct category of data within the project that may have its own characteristics, sensitivity level, and handling requirements.

**Examples of data entities:**

| Data Entity | Description |
|-------------|-------------|
| Interview recordings | Audio/video files from qualitative interviews |
| Interview transcripts | Text transcriptions, potentially with personal identifiers |
| Survey responses | Structured data from questionnaires |
| Register data | Data obtained from public registries (SSB, tax records, etc.) |
| Secondary datasets | Existing datasets reused in the project |
| Field notes | Researcher observations and notes |
| Administrative data | Contracts, correspondence with partners, meeting notes |
| Code and scripts | Analysis code, statistical scripts |
| Output datasets | Processed/anonymised data for publication or archiving |

**LLM assistance:** Based on proposal text, the LLM drafts an initial list of probable data entities, flagging any that may require special handling. rdm@cmi and PI verify and adjust.

### 2.4 Sensitivity Classification

Each data entity is assigned a preliminary sensitivity level:

| Level | Description | Typical Examples | Storage Implication |
|-------|-------------|------------------|---------------------|
| **Open** | No restrictions; can be shared publicly | Published datasets, public documents, anonymised outputs | Standard Teams/SharePoint |
| **Restricted** | Internal use; low sensitivity | Working papers, aggregated data, administrative docs | Standard Teams/SharePoint |
| **Confidential** | Personal data; identifiable individuals | Interview transcripts, survey data with identifiers, contact lists | Teams with restricted access; encryption recommended |
| **Highly Confidential** | Special category data; high-risk if disclosed | Health data, vulnerable populations, politically sensitive content, security-related | TSD or equivalent secure environment |

**Classification parameters:**
- Nature of data subjects (general public, vulnerable groups, public figures)
- Identifiability (anonymous, pseudonymous, directly identifiable)
- Data content (opinions, health, ethnicity, political views, etc.)
- Source (primary collection, registers, secondary data)
- Contractual restrictions (data sharing agreements, NDAs)
- Geographic considerations (data from/about high-risk regions)

**Note:** Classification is preliminary and assumed; it may be adjusted as the project develops and actual data characteristics become clear.

### 2.5 Project Risk Classification

Separate from data sensitivity, the overall **project risk level** captures complexity and organisational risk:

| Level | Indicators | RDM Response |
|-------|------------|--------------|
| **Low** | Single institution, limited personal data, straightforward methods, internal/minor funding | Light-touch: Light-DMP, minimal check-ins |
| **Medium** | Multiple partners, personal data collection, external funding with requirements, cross-border elements | Standard: Full DMP, periodic check-ins, document bundle |
| **High** | Sensitive populations, special category data, complex partnerships, significant cross-border data transfers, novel/experimental methods | Enhanced: DPIA required, active rdm@cmi involvement, ethics review, legal/DPO consultation |

**Risk parameters:**
- Number and type of partners (academic, government, private sector, NGOs)
- Geographic scope (Norway only, EU, third countries)
- Funder requirements and scrutiny level
- Data volume and complexity
- Methodological novelty
- Public/political sensitivity of topic
- Duration and scale of project

### 2.6 Compliance Requirements Checklist

Based on classifications, rdm@cmi determines which compliance elements are needed:

| Requirement | When Needed | Responsible | Notes |
|-------------|-------------|-------------|-------|
| **Light-DMP** | All projects | rdm@cmi drafts, PI approves | Internal use; brief; auto-generated |
| **Funder DMP** | RCN, Horizon, ERC, etc. | rdm@cmi drafts, PI submits | Funder-specific format |
| **Sikt notification** | Projects with personal data (Norwegian context) | PI, with rdm@cmi support | Pre-filled draft provided |
| **DPIA** | High-risk processing; large-scale sensitive data; new technologies | rdm@cmi + DPO | Triggers legal review |
| **REC application** | Health research, human biological material | PI | May already exist from proposal stage |
| **Data Processing Agreement (DPA)** | External processors handling personal data | PI + legal/DPO | Template available |
| **Consortium/data sharing agreement** | Multi-partner projects with shared data | PI + legal | Clarifies controller/processor roles |
| **Data controller clarification** | All projects with personal data | rdm@cmi + DPO | CMI as controller, joint controller, or processor? |

### 2.7 Data Controller and Processor Roles

Clarifying CMI's role in relation to personal data is essential for determining responsibilities, liabilities, and contractual requirements. This is often a source of confusion, particularly in multi-partner projects.

**Key definitions (GDPR):**

| Role | Definition | Responsibilities |
|------|------------|------------------|
| **Data Controller** | Determines the purposes and means of processing personal data | Full compliance responsibility; responds to data subject requests; accountable for lawful basis, security, etc. |
| **Joint Controllers** | Two or more parties jointly determine purposes and means | Shared responsibilities; must have arrangement specifying respective duties |
| **Data Processor** | Processes personal data on behalf of a controller | Acts only on controller's instructions; requires Data Processing Agreement (DPA) |

**Determining CMI's role:**

| Scenario | Likely Role | Contractual Need |
|----------|-------------|------------------|
| CMI designs and conducts own research, collects data directly | **Controller** | Privacy notice to data subjects; internal GDPR documentation |
| CMI leads consortium, determines research questions, partners contribute data | **Controller** (possibly joint) | DPAs with partners who process on CMI's behalf; joint controller arrangement if partners co-determine purposes |
| CMI is partner in externally-led project, contributes to research design | **Joint Controller** | Joint controller arrangement with lead institution |
| CMI provides data/analysis services to external party who defines the research | **Processor** | DPA where CMI is processor |
| CMI receives existing dataset from another institution for secondary analysis | Depends on terms | Data sharing agreement; check original consent and legal basis |

**Common grey areas at CMI:**

1. **Commissioned research:** When CMI is contracted to conduct research for an external client (government, NGO, etc.), who is controller?
   - If client defines the research questions and CMI executes → CMI may be processor
   - If CMI has academic freedom to design methodology and analysis → CMI is likely controller or joint controller
   - *Clarify in contract; default assumption should not be that commissioner is automatically controller*

2. **Consortium projects (Horizon, NFR):** Often joint controllership, but not always formalised.
   - Check consortium agreement for data governance provisions
   - If silent, propose joint controller arrangement or clarify in data management plan

3. **Secondary data from partners:** CMI using data collected by others.
   - Verify legal basis covers CMI's intended use
   - Check if original consent permits sharing for research
   - May require data sharing agreement even if not a controller/processor relationship

4. **Interviews with professionals/officials:** Data about individuals in their professional capacity.
   - Still personal data under GDPR
   - CMI typically controller
   - Sensitivity may be lower, but compliance requirements remain

**Process:**
1. At intake, rdm@cmi makes preliminary determination of CMI's role
2. If unclear or complex, escalate to DPO for guidance
3. Document role determination in Project RDM Summary
4. Ensure appropriate agreements are in place before data processing begins

### 2.8 LLM Integration

**Input:** Proposal PDF, grant application, project description

**LLM tasks:**
1. Extract and summarise data collection plans from proposal text
2. Identify probable data entities
3. Flag potential sensitivities (vulnerable groups, health data, political content, etc.)
4. Suggest preliminary classifications
5. Identify mentioned partners and geographies
6. Note any stated ethical considerations or limitations
7. Pre-fill intake assessment template

**Output:** Draft assessment for rdm@cmi review

**Human role:** rdm@cmi validates all LLM suggestions, adjusts classifications based on contextual knowledge, and confirms with PI.

### 2.9 Storage and Security Recommendations Matrix

Based on sensitivity classification, standardised recommendations apply:

| Sensitivity | Primary Storage | Access Control | Additional Measures |
|-------------|-----------------|----------------|---------------------|
| **Open** | Teams/SharePoint | Project team; can be shared wider | None required |
| **Restricted** | Teams/SharePoint | Project team only | Standard Teams permissions |
| **Confidential** | Teams/SharePoint (restricted channel) or encrypted area | Named individuals only | Encryption at rest; MFA enforced; no guest access to sensitive channels |
| **Highly Confidential** | Secure environment (see note below) | Strict need-to-know; logged access | No local copies; dedicated secure analysis environment |

**Note on storage for Highly Confidential data:**

TSD (Tjenester for Sensitive Data) is commonly referenced in the Norwegian research context as an appropriate platform for sensitive data. However, TSD may not suit all CMI projects due to:
- Additional costs (per-project fees)
- Workflow constraints (isolated environment, limited tools)
- Project requirements that don't align with TSD model

**Alternatives to consider:**
- **Tresorit** – end-to-end encrypted cloud storage (Swiss-based)
- **Proton Drive** – encrypted storage (Swiss-based)
- **Other non-US services** with strong encryption and GDPR compliance

Selection criteria: encryption standards, data residency (preferably EU/EEA), compliance certifications, cost, and usability for project workflow. rdm@cmi advises on appropriate solution case-by-case.

**Note:** Projects may have data entities at multiple sensitivity levels. Each entity follows recommendations for its classification; the project Team accommodates this through channel/folder structure and access controls.

## Deliverables from Assessment

At completion of intake assessment, the following are produced:

1. **Project RDM Summary** (1-2 pages)
   - Overview of data entities and classifications
   - Risk level and rationale
   - Storage recommendations
   - Compliance requirements checklist
   - Key contacts (PI, rdm@cmi, DPO if relevant)

2. **Compliance action list**
   - Required documents and deadlines
   - Responsible parties
   - Status tracking (links to Recommendation #3)

3. **Document bundle** (see Recommendation #4)
   - Pre-filled templates based on assessment

## Timing

- Initial assessment completed within **2 weeks** of project Team creation
- Verification meeting with PI within **1 week** of draft assessment
- Document bundle uploaded to RDM channel within **1 week** of verification

## Considerations

- **Iterative process:** Assessment is preliminary; classifications may change as project develops. Mid-project review points allow for updates (see Recommendation #5).
- **Proportionality:** Low-risk projects should experience this as lightweight; high-risk projects receive more attention.
- **PI engagement:** Success depends on PI providing accurate information and engaging with verification step.