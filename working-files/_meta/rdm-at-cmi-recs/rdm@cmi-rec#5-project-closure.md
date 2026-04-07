# Recommendation #5: Project Closure

## Rationale

Project closure is when RDM decisions become permanent. Data is either preserved or deleted; documentation is finalised; access is revoked. Without a structured closure process, projects drift into ambiguity: data lingers in uncertain states, documentation remains incomplete, and former collaborators retain access indefinitely.

A clear closure process ensures:
- Data fate is documented (archived, deleted, deposited)
- Compliance obligations are fulfilled (retention periods, Sikt, funder requirements)
- Institutional knowledge is preserved
- Access controls reflect reality
- Funder deliverables are complete

## Core Recommendation

When a project reaches completion, rdm@cmi initiates a closure process that generates updated final documentation, confirms data retention or deletion, bundles deliverables for funders, and transitions the project Team to archived status.

## Implementation

### 5.1 Closure Trigger

**When:** Project closure is triggered when:
- Project end date is reached, or
- PI declares project complete, or
- Final report/deliverable is submitted to funder

**Pre-closure notification:** rdm@cmi contacts PI approximately **3 months before** anticipated project end (based on project registry) to initiate closure planning.

### 5.2 Closure Process Overview

```
┌─────────────────────────────────────────────────────────────┐
│  Step 1: Pre-closure Check-in (~3 months before end)        │
│  → Confirm project status and timeline                      │
│  → Identify outstanding RDM tasks                           │
│  → Plan for data disposition                                │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 2: Data Inventory Finalisation                        │
│  → Verify all data entities accounted for                   │
│  → Confirm final status of each entity                      │
│  → Document retention/deletion decisions                    │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 3: Final Documentation Generation                     │
│  → Update DMP to reflect actual practice                    │
│  → Generate closure report                                  │
│  → Bundle funder deliverables                               │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 4: Data Disposition                                   │
│  → Execute retention/deletion/deposit plan                  │
│  → Document actions taken                                   │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 5: Compliance Closure                                 │
│  → Close or update Sikt notification                        │
│  → Verify all requirements met                              │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  Step 6: Access Review & Team Archival                      │
│  → Revoke external collaborator access                      │
│  → Archive project Team                                     │
│  → Update project registry                                  │
└─────────────────────────────────────────────────────────────┘
```

### 5.3 Pre-closure Check-in

rdm@cmi initiates contact with PI to:

| Topic | Discussion Points |
|-------|-------------------|
| **Timeline** | Confirm expected end date; any extensions anticipated? |
| **Outstanding tasks** | Any data collection still ongoing? Publications pending? |
| **Data plans** | What should happen to each data entity? (See 5.5) |
| **Funder requirements** | What deliverables are due? DMP update? Data deposit? |
| **Access** | Which external collaborators still need access? For how long? |

**Output:** Closure plan with timeline and responsibilities.

### 5.4 Data Inventory Finalisation

The data inventory (Recommendation #3) is reviewed and updated to reflect final state:

| Field | Action |
|-------|--------|
| **Status** | Update to final status: Complete / Archived / Deleted / Deposited |
| **Storage location** | Confirm current location; update if moved |
| **Retention plan** | Confirm decision: delete / archive internally / deposit externally |
| **Retention period** | Specify end date if applicable (e.g., "Delete by 2030-12-31") |
| **Documentation links** | Verify all links functional; add final versions |

**Verification questions:**
- Are all data entities from the original inventory accounted for?
- Were any additional data entities created that weren't in the inventory?
- Does the final state match what was described in consent/information letters?
- Are retention decisions consistent with legal basis and funder requirements?

### 5.5 Data Disposition Options

Each data entity receives a disposition decision:

| Disposition | Description | When Appropriate | Documentation |
|-------------|-------------|------------------|---------------|
| **Delete** | Data permanently removed | Personal data where retention not justified; consent-based data at project end; no ongoing legal basis | Deletion confirmation (date, method, who) |
| **Archive internally** | Retained at CMI for specified period | Ongoing research value; funder requires retention; legal obligation | Archive location, access restrictions, retention end date |
| **Deposit externally** | Published to repository | Open data commitment; funder requirement; reuse value | Repository name, DOI/persistent identifier, access conditions |
| **Transfer** | Data moved to partner or successor | Joint project where partner continues; commissioned research | Transfer agreement, recipient, date |

**Deletion protocol:**
- Confirm deletion is consistent with consent and legal basis
- Delete from all locations (primary storage, backups, local copies)
- Document: what was deleted, when, by whom, method
- Retain documentation of deletion (not the data itself)

**Archival protocol:**
- Move to designated archive location
- Restrict access to need-to-know
- Set calendar reminder for retention review/deletion date
- Document: location, access list, retention end date

**Deposit protocol:**
- Select appropriate repository (see repository recommendations below)
- Prepare data for deposit (anonymisation, documentation, metadata)
- rdm@cmi assists with metadata package preparation and archive interface
- Complete deposit and obtain persistent identifier
- Document: repository, identifier, access conditions, embargo if any

**Repository recommendations:**

| Repository | Use Case | Notes |
|------------|----------|-------|
| **CMI Dataverse (via DataverseNO)** | Preferred default for CMI research data | Recommended: establish institutional Dataverse; see [DataverseNO pricing](https://zenodo.org/records/18199491) |
| **Sikt Research Data Archive** | Survey data, structured quantitative data | Established Norwegian infrastructure; good for social science data |
| **Zenodo** | Replication packages, code, supplementary materials | Free; DOI minting; GitHub integration |
| **OSF (Open Science Framework)** | Replication packages, preregistrations, project archives | Free; flexible; good for mixed materials |

**Note:** Establishing a CMI Dataverse through DataverseNO is recommended as a long-term investment, providing institutional branding, control, and streamlined deposit for CMI researchers.

### 5.6 Archive Preparation Support

For projects depositing data in external repositories, rdm@cmi provides practical support:

**Metadata package preparation:**
- Assist with structuring documentation for deposit
- Ensure metadata meets repository requirements
- Prepare README files, codebooks, data dictionaries
- Review anonymisation/de-identification

**Archive interface support:**
- Assist with repository registration and navigation
- Support upload and submission process
- Troubleshoot technical issues
- Liaise with repository staff if needed

**Machine-actionable metadata (LLM-assisted, beta):**

rdm@cmi can generate structured, machine-actionable metadata using an LLM-based tool:

| Input | Output |
|-------|--------|
| Existing project documentation (DMP, inventory, proposal, README) | Structured metadata in repository-required format |
| Data entity descriptions | Variable descriptions, keywords, subject classifications |
| Project details | Citation metadata, contributor roles, funding information |

This tool:
- Drafts metadata based on documentation already created during the project
- Outputs formats compatible with DataverseNO, Zenodo, and other repositories
- Reduces manual entry burden at deposit stage
- Requires human verification before submission

**Note:** This capability is in beta; outputs are reviewed and validated by rdm@cmi and PI before use.

### 5.7 Final Documentation Generation

Updated and final documents are generated:

#### Final DMP

The Light-DMP (or funder DMP) is updated to reflect **what actually happened**, not just what was planned:

| Section | Update |
|---------|--------|
| Data description | Confirm actual data collected; note any deviations from plan |
| Storage | Document where data was stored during project |
| Access | Who had access; any issues encountered |
| Preservation | Final disposition of each data entity |
| Sharing | What was/will be shared; repository details |

#### Project Closure Report

A brief document summarising RDM aspects of the project:

| Section | Content |
|---------|---------|
| Project overview | Title, PI, period, funder |
| Data summary | Number and types of data entities; sensitivity levels |
| Compliance summary | Sikt reference, REC reference (if any), DPAs executed |
| Data disposition | Summary table of what happened to each entity |
| Issues or lessons | Any challenges encountered; recommendations for future |
| PI approval | PI reviews and approves (implicit approval: no objection within 1 week) |

#### Funder Deliverables Bundle

For projects with external funders, relevant documents are bundled for submission:

| Funder | Typical Requirements |
|--------|---------------------|
| **NFR (RCN)** | Final DMP; data deposit confirmation; publication list |
| **Horizon Europe** | Updated DMP; FAIR data documentation; open access confirmation |
| **ERC** | Data management summary; repository deposit |
| **Other** | As specified in grant agreement |

rdm@cmi assists with bundling and formatting; PI reviews and submits.

### 5.8 Compliance Closure

#### Sikt Notification

| Scenario | Action |
|----------|--------|
| Project complete, data deleted | Close notification in Sikt; confirm end date |
| Project complete, data archived | Update notification with new end date reflecting retention period |
| Data deposited in repository | Update notification to reflect new storage; may close if fully anonymised |

**Process:** PI (with rdm@cmi support) updates Sikt notification to reflect project completion. rdm@cmi should be contributor/editor to assist.

#### Other Compliance

- **REC:** Notify if required by approval conditions
- **DPAs:** Confirm processor obligations fulfilled; retain agreements for documentation
- **Data sharing agreements:** Confirm terms fulfilled; note any ongoing obligations

### 5.9 Access Review & Team Archival

#### External Collaborator Access

| Step | Action |
|------|--------|
| **Review** | List all external collaborators (guests) with Team access |
| **Assess** | For each: is continued access needed? For how long? |
| **Revoke** | Remove access for collaborators no longer involved |
| **Document** | Note in closure report who retained access and why |

**Default:** External access is revoked at project closure unless explicitly justified.

#### Team Archival

Following the lifecycle defined in Recommendation #1:

| Action | Detail |
|--------|--------|
| **Archive Team** | Set Team to archived status (read-only) |
| **Retain access** | Core project team retains read access |
| **Retention period** | Team remains archived for [X years] per CMI policy / funder requirements |
| **Future deletion** | Calendar reminder set for eventual Team deletion |

#### Project Registry Update

Update central project registry (Recommendation #1):
- Status → Completed / Archived
- End date (actual)
- Closure date
- Notes on data disposition

### 5.10 LLM Integration

**Final documentation generation:**

| Input | LLM Task | Output |
|-------|----------|--------|
| Initial DMP + final inventory | Compare planned vs. actual | Discrepancy report; suggested DMP updates |
| Final inventory + disposition decisions | Generate summary | Data disposition table for closure report |
| Project documents + closure checklist | Verify completeness | Gap list; suggested actions |
| Funder requirements + project outputs | Match requirements to evidence | Funder deliverables checklist |
| Project documentation (DMP, inventory, proposal) | Generate archive metadata | Machine-actionable metadata for repository deposit (beta) |

**Quality assurance:** All LLM outputs reviewed by rdm@cmi; PI verifies accuracy of final documents.

### 5.11 Closure Checklist

rdm@cmi and PI work through the following checklist:

**Data Inventory**
- [ ] All data entities accounted for
- [ ] Final status confirmed for each entity
- [ ] Disposition decision documented for each entity
- [ ] Documentation links verified

**Data Disposition**
- [ ] Deletions executed and documented
- [ ] Archives established with access controls
- [ ] Repository deposits completed (if applicable)
- [ ] Metadata packages prepared and validated (if depositing)
- [ ] Transfers completed (if applicable)

**Documentation**
- [ ] Final DMP completed
- [ ] Closure report drafted
- [ ] Funder deliverables bundled (if applicable)
- [ ] PI reviewed (implicit approval if no objection within 1 week)

**Compliance**
- [ ] Sikt notification updated/closed
- [ ] REC notified (if applicable)
- [ ] DPA obligations confirmed fulfilled

**Access & Archival**
- [ ] External collaborator access reviewed
- [ ] Unnecessary access revoked
- [ ] Team archived
- [ ] Project registry updated

### 5.12 Post-Closure

After formal closure:

| Timeframe | Action |
|-----------|--------|
| **Ongoing** | Archived Team accessible (read-only) to project team |
| **As needed** | Data subject requests handled (if data retained) |
| **Retention end date** | Review archived data; delete if no longer justified |
| **Registry retention** | Project registry entry retained permanently for institutional memory |

**Handling late requests:**
- Publications arising after closure: access archived Team for data/documentation
- Funder audits: documentation available in archived Team
- Data subject requests: rdm@cmi coordinates response using archived records

## Timing

| Phase | Timeframe |
|-------|-----------|
| Pre-closure check-in | ~3 months before project end |
| Inventory finalisation | 1–2 weeks |
| Documentation generation | 1–2 weeks |
| Data disposition | Varies (deletion immediate; deposit may take longer) |
| Compliance closure | 1–2 weeks |
| Access review & archival | 1 week |
| **Total closure process** | ~4–8 weeks |

## Success Indicators

- All completed projects have documented data disposition
- Sikt notifications are closed or updated at project end
- External collaborator access is reviewed and revoked where appropriate
- Project Teams are archived (not left in active state indefinitely)
- Funder deliverables submitted on time
- No "orphaned" data of uncertain status