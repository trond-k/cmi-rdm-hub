# Recommendation #4: Embedded RDM & Document Bundle

## Rationale

The previous recommendations establish structure (Teams), assessment (classification), and tracking (inventory). This recommendation delivers the tangible value: a "bundle" of project-specific, pre-filled documents that researchers would otherwise have to create from scratch.

By embedding rdm@cmi lightly into each project—through a dedicated channel and tailored documentation—the RDM function becomes a visible, accessible resource rather than a distant compliance office.

## Core Recommendation

Each project Team includes a dedicated **RDM channel** where rdm@cmi uploads a customised **document bundle** based on the initial assessment. The bundle contains pre-filled templates for information letters, consent forms, Sikt notifications, DMPs, and other relevant documentation. The channel also serves as a space for RDM-related questions, updates, and support throughout the project.

## Implementation

### 4.1 The RDM Channel

Every project Team (see Recommendation #1) includes an **RDM channel** with the following structure:

```
📁 RDM Channel
├── 📁 Documentation
│   ├── ProjectName_RDM_Summary.docx
│   ├── ProjectName_DataInventory.xlsx (or link to List)
│   └── ProjectName_ComplianceChecklist.docx
│
├── 📁 Templates
│   ├── ProjectName_InformationLetter.docx
│   ├── ProjectName_ConsentForm.docx
│   ├── ProjectName_SiktNotification_Draft.docx
│   ├── ProjectName_LightDMP.docx
│   ├── ProjectName_FunderDMP.docx (if applicable)
│   └── ProjectName_EthicsSummary.docx
│
└── 📁 Completed
    └── (Signed/submitted versions moved here)
```

**Channel purpose:**
- Central location for all RDM-related documentation
- Space for questions and discussion with rdm@cmi
- Record of RDM decisions and changes

### 4.2 The Document Bundle

The document bundle is the core deliverable of the RDM process. All documents are **pre-filled** with project-specific information derived from the initial assessment (Recommendation #2).

#### Core Documents (All Projects)

| Document | Purpose | Pre-filled Content |
|----------|---------|-------------------|
| **RDM Summary** | One-page overview of RDM setup for the project | Project name, PI, data entities, sensitivity classifications, risk level, storage recommendations, compliance requirements, key contacts |
| **Data Inventory** | Structured list of data entities (see Rec #3) | Entities identified from proposal, preliminary classifications, status, placeholders for documentation links |
| **Light-DMP** | Internal data management plan | Project details, data descriptions, storage locations, access arrangements, retention plans, responsibilities |
| **Compliance Checklist** | Tracks required documentation and status | List of applicable requirements (Sikt, REC, DPA, etc.) with status and deadlines |

#### Data Collection Documents (Projects Collecting Personal Data)

| Document | Purpose | Pre-filled Content |
|----------|---------|-------------------|
| **Information Letter(s)** | Privacy notice for data subjects | Project title, purpose, data controller (CMI), data types collected, legal basis, retention period, rights, contact details |
| **Consent Form(s)** | Records data subject consent | Linked to information letter; checkboxes for specific consent elements; signature/date fields |
| **Sikt Notification Draft** | Ready-to-submit notification | Project details, data categories, legal basis, storage, transfers, retention—mapped to Sikt form fields |

**Note on Sikt submissions:** The PI is formally responsible for Sikt notifications, but this is ultimately an institutional responsibility. rdm@cmi assists with preparation and it is recommended that rdm@cmi is added as contributor/editor when the project is registered with Sikt. This enables ongoing support and ensures institutional oversight.

#### Conditional Documents (Where Applicable)

| Document | When Needed | Pre-filled Content |
|----------|-------------|-------------------|
| **Funder DMP** | RCN, Horizon, ERC, or other funder requirement | Funder-specific format; project details, FAIR principles, data sharing plans, costs |
| **Ethics Summary** | Projects with ethical sensitivities | Summary of ethical considerations, risk mitigation, relevant approvals |
| **DPIA Template** | High-risk processing identified | Data processing details, necessity assessment, risk identification—for completion with DPO |
| **Data Sharing Agreement Template** | Multi-partner projects, secondary data | Parties, data description, permitted uses, security requirements, responsibilities |

### 4.3 Document Generation Process

**Step 1: Assessment complete (Recommendation #2)**
- Data entities, classifications, and compliance requirements identified

**Step 2: LLM-assisted drafting**
- LLM generates first drafts of all applicable documents
- Draws on: project proposal, assessment outputs, CMI templates, regulatory requirements

**Step 3: rdm@cmi review**
- Reviews and refines LLM outputs
- Ensures consistency across documents
- Flags any items needing PI input

**Step 4: Bundle uploaded**
- Documents uploaded to RDM channel in project Team
- PI notified that bundle is ready for review

**Step 5: PI verification**
- PI reviews documents, particularly:
  - Data descriptions (accuracy)
  - Information letters (appropriate for context)
  - Consent forms (covers intended uses)
- Provides corrections or approval

**Step 6: Finalisation**
- rdm@cmi incorporates feedback
- Final versions uploaded
- Compliance checklist updated

### 4.4 What Pre-filling Means in Practice

**Example: Information Letter**

Instead of starting from a blank template, the researcher receives:

| Field | Pre-filled With |
|-------|-----------------|
| Project title | From proposal |
| Project purpose (lay summary) | Extracted/summarised from proposal |
| Data controller | "Chr. Michelsen Institute (CMI), Bergen" |
| Contact details | PI name and CMI contact |
| What data we collect | From data entity inventory |
| Why we collect it (legal basis) | From assessment (e.g., "Your consent") |
| How long we keep it | From retention plan |
| Your rights | Standard GDPR text |
| Complaints | Datatilsynet contact |

The researcher reviews for accuracy and tone, adjusts for context, and the document is ready.

**Example: Sikt Notification**

| Sikt Field | Pre-filled With |
|------------|-----------------|
| Institution | Chr. Michelsen Institute |
| Project title | From proposal |
| Project period | Start/end dates |
| Project description | Summary from proposal |
| Categories of personal data | From data inventory |
| Special categories | Flagged from assessment |
| Legal basis | From assessment |
| Data subjects | From proposal (e.g., "local government officials in India") |
| Data sources | From data inventory |
| Third parties / transfers | From partner list |
| Security measures | From storage recommendations |
| Retention / deletion | From retention plan |

The researcher verifies, adjusts, and submits—rather than puzzling over each field from scratch.

### 4.5 Light-Embedded Presence

rdm@cmi's presence in the project is **supportive, not intrusive**:

**Available for:**
- Questions about data handling, storage, documentation
- Clarification of compliance requirements
- Ad-hoc advice on emerging issues
- Support with Sikt submissions or ethics applications
- Mid-project changes (new data, new partners)

**Not involved in:**
- Day-to-day research decisions
- Reviewing research outputs
- Monitoring researcher activity
- Approving routine project activities

**Communication:**
- RDM channel is primary contact point
- rdm@cmi monitors channels; **24-hour response time** can realistically be expected
- Milestone check-ins scheduled proactively (see 4.6)

### 4.6 Milestone Check-ins

rdm@cmi initiates brief check-ins at key project phases:

| Milestone | Timing | Purpose |
|-----------|--------|---------|
| **Post-bundle** | ~2 weeks after bundle delivered | Confirm documents reviewed; answer questions; verify Sikt submitted |
| **Data collection start** | When fieldwork/collection begins | Confirm storage in place; documentation distributed; any issues? |
| **Mid-project** | ~Halfway (for projects >18 months) | Review inventory; any changes to data or scope? Update classifications if needed |
| **Pre-closure** | ~3 months before project end | Prepare for closure; confirm retention/deletion plans; identify final deliverables |

**Note:** Four milestones are defined, but for many projects three may be sufficient (start, mid, end). The mid-project check-in is most relevant for longer projects (>18 months) or those with evolving scope. rdm@cmi adjusts frequency based on project risk and complexity.

**Format:** Brief Teams message or short call (15 min max); not formal meetings.

**Researcher burden:** Responding to check-in, confirming status—typically 5–10 minutes.

### 4.7 Handling Changes During Project

Projects evolve. The document bundle and RDM setup accommodate this:

| Change | Process |
|--------|---------|
| **New data collection** (not originally planned) | PI notifies rdm@cmi → Assessment of new entity → Update inventory → Additional templates if needed → Sikt amendment if required |
| **New partner added** | Assess data sharing implications → DPA or data sharing agreement if needed → Update DMP |
| **Scope reduction** | Update inventory (mark entities as "not collected") → Simplify documentation if appropriate |
| **Sensitivity change** | Reassess classification → Adjust storage/access if needed → Update documentation |
| **Extension** | Update retention plans → Sikt amendment if dates change significantly |

rdm@cmi supports these changes; researcher initiates by flagging in RDM channel.

### 4.8 LLM Integration

**Document generation:**

| Input | LLM Task | Output |
|-------|----------|--------|
| Proposal text + assessment | Extract project summary in lay language | Information letter draft (purpose section) |
| Data inventory + classifications | Generate data descriptions | Information letter draft (data section), Sikt notification draft |
| Compliance checklist | Map requirements to templates | Prioritised document list |
| CMI templates + project details | Populate template fields | Pre-filled documents |
| Ethics issues catalogue + project description | Identify applicable concerns | Ethics summary draft |

**Quality assurance:**
- LLM drafts are always reviewed by rdm@cmi before upload
- Sensitive content (legal basis justifications, ethics rationale) verified carefully
- PI verification is final check

**Prompt library:**
- Standardised prompts for each document type
- Version-controlled and refined based on experience
- Context includes: CMI policies, Norwegian regulations, funder requirements

### 4.9 Template Maintenance

rdm@cmi maintains master templates that feed LLM generation:

| Template | Review Frequency | Triggers for Update |
|----------|------------------|---------------------|
| Information letters | Annually | Regulatory changes, CMI policy changes |
| Consent forms | Annually | Regulatory changes |
| Sikt notification guide | As needed | Sikt form changes |
| Light-DMP | Annually | Best practice evolution |
| Funder DMPs | Per call | Funder requirement changes |

Templates stored in a central location (outside project Teams) managed by rdm@cmi.

## What Researchers Receive

To summarise, a researcher starting a new project receives:

✅ A dedicated RDM channel in their project Team  
✅ A document bundle with pre-filled, project-specific templates  
✅ A clear compliance checklist showing what's needed and what's done  
✅ A point of contact (rdm@cmi) for questions  
✅ Proactive check-ins at key milestones  
✅ Support for changes and issues as they arise  

**Time investment:** Reviewing bundle and responding to check-ins—approximately 1–2 hours across the life of a typical project.

**Time saved:** Not writing information letters, consent forms, Sikt notifications, or DMPs from scratch—potentially many hours per project.

## Success Indicators

- Document bundles delivered within 2 weeks of project initiation
- Researcher feedback indicates documents are useful and accurate
- Sikt notifications submitted without significant revision
- Compliance checklists are completed by project closure
- RDM channel used for questions (indicates awareness and accessibility)