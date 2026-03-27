# Recommendation #3: Data Inventory

## Rationale

Research projects involve data, but the data "products" and data flows are often implicit rather than explicit. Project proposals and descriptions focus on research questions, methods, and outputs—they rarely detail the specific data entities that will be created, how data moves through the project, or who is responsible for what at each stage.

Establishing a data inventory makes the implicit explicit:

- **Data entities:** What data will actually exist in this project?
- **Data flows:** Where does data come from, where is it stored, where does it go?
- **Roles and responsibilities:** Who collects, processes, stores, and ultimately disposes of each data type?
- **Pipelines:** How does raw data become analysis-ready data become publishable output?

The inventory is preliminary and changeable—it captures assumptions at project start and is refined as the project develops. This visibility supports better planning, clearer responsibilities, and more manageable compliance.

A secondary function is tracking: connecting data entities to relevant documentation (consent forms, Sikt notifications, ethics approvals) and monitoring status throughout the project lifecycle.

## Core Recommendation

Each project maintains a lightweight data inventory using Microsoft Lists (within the project Team). The inventory tracks data entities identified in the initial assessment (Recommendation #2), their status, and links to associated documentation. This is a progress tracker, not a surveillance tool.

## Guiding Principles

- **Light touch:** Minimal administrative burden; updated at key milestones, not continuously
- **Entity-level tracking:** Tracks categories of data (e.g., "interview transcripts"), not individual files
- **Practical utility:** Serves the project team and rdm@cmi, not bureaucratic compliance
- **Living document:** Evolves as project develops; preliminary entries are refined over time

## Why This Isn't Just More Admin

At face value, a data inventory may seem like an additional layer of administration. This concern is legitimate—researchers are already stretched thin, and "more tracking" can feel like bureaucratic creep.

**The alternative ("sitting quietly in the boat"):**

Many institutes operate with minimal data oversight: high researcher autonomy, low institutional visibility, and a hope that no one asks difficult questions. This works—until it doesn't:
- A funder audit requests documentation of data handling
- Sikt asks for clarification on a notification
- A data subject exercises their rights and the project can't locate relevant records
- A PI leaves and no one knows where project data is or what agreements govern it
- Project closure requires a DMP that was never written

At that point, researchers face significant unplanned burden: reconstructing what should have been documented from the start.

**The trade-off this system offers:**

| Researcher Investment | What rdm@cmi Provides in Return |
|-----------------------|--------------------------------|
| ~30 min at project start: review and confirm data inventory | Pre-filled, project-specific information letters |
| ~15 min at key milestones: update status, add links | Pre-filled Sikt notification (ready to submit) |
| Brief verification of assumptions | Customised DMP (Light-DMP always; funder DMP where needed) |
| | Ethics summary document |
| | Storage and security recommendations |
| | Clear documentation trail if questions arise |
| | Support at project closure (final DMP, archival/deletion) |

**The bargain:**

> A modest, structured investment in visibility upfront—mostly handled by rdm@cmi with researcher verification—reduces reactive burden later and provides project-specific, ready-to-use documentation.

Researchers don't write information letters from scratch. They don't puzzle over Sikt forms. They don't scramble at project end to reconstruct what data existed and where it went. The machine-in-the-loop approach (LLM-assisted drafting, rdm@cmi coordination) means most of the work is done *for* researchers, not *by* them.

**What this system is not:**
- Not surveillance of researcher activity
- Not a compliance checkbox exercise
- Not a requirement to document every file
- Not an attempt to reduce researcher autonomy on research matters

It is an attempt to make data handling visible enough to support researchers when visibility is needed—and invisible enough to stay out of the way when it isn't.

## Implementation

### 3.1 Inventory Location

The data inventory is created as a **Microsoft List** within the project Team's RDM channel. This ensures:
- Accessibility to project team and rdm@cmi
- Integration with other Teams features (links, notifications)
- Familiar interface for CMI staff
- Easy export if needed for reporting

### 3.2 Inventory Structure

**Core fields:**

| Field | Type | Description |
|-------|------|-------------|
| **Entity ID** | Auto-number | Unique identifier (e.g., DE-001) |
| **Entity Name** | Text | Brief descriptive name (e.g., "Interview transcripts - local officials") |
| **Description** | Text (multi-line) | What the data contains, collection method, scope |
| **Data Type** | Choice | Primary / Secondary / Administrative / Output |
| **Format** | Text | File formats (e.g., MP3, DOCX, CSV, NVivo) |
| **Sensitivity** | Choice | Open / Restricted / Confidential / Highly Confidential |
| **Storage Location** | Text + link | Where data is stored (Teams folder, TSD, Tresorit, etc.) |
| **Status** | Choice | Planned / Collecting / Processing / Complete / Archived / Deleted |
| **Legal Basis** | Choice | Consent / Legitimate interest / Public interest / Contract / Other |
| **Retention Plan** | Choice | Delete at project end / Archive [X years] / Deposit in repository / To be determined |

**Documentation links:**

| Field | Type | Description |
|-------|------|-------------|
| **Information Letter** | Link | Link to relevant information letter/privacy notice |
| **Consent Form** | Link | Link to consent form template or collected consents |
| **Sikt Reference** | Text + link | Sikt notification reference number and link |
| **REC Reference** | Text + link | REC approval reference (if applicable) |
| **Other Documentation** | Link | Any other relevant documents (DPA, data sharing agreement, etc.) |

**Tracking fields:**

| Field | Type | Description |
|-------|------|-------------|
| **Created** | Date (auto) | When entry was added |
| **Last Updated** | Date | Last modification date |
| **Notes** | Text (multi-line) | Any comments, issues, or context |

### 3.3 Pre-population

Based on the initial assessment (Recommendation #2), rdm@cmi creates the inventory with:
- Data entities identified from proposal
- Preliminary sensitivity classifications
- Status set to "Planned" for anticipated data
- Empty or placeholder links for documentation not yet created

**LLM assistance:** The LLM drafts initial inventory entries based on the assessment; rdm@cmi reviews and uploads to the project Team.

### 3.4 Update Points

The inventory is updated at key project milestones, not continuously:

| Milestone | Updates |
|-----------|---------|
| **Project initiation** | Initial entries created (Planned status) |
| **Data collection start** | Status → Collecting; confirm storage locations; link documentation |
| **Mid-project review** (if applicable) | Verify entries; add any new data entities; update statuses |
| **Data collection complete** | Status → Processing or Complete; verify all documentation linked |
| **Project closure** | Final status for all entities; retention plans confirmed; deletion documented |

**Who updates:**
- Project team updates status and adds links as work progresses
- rdm@cmi reviews at milestones and prompts for updates if needed
- Light-touch reminders, not enforcement

### 3.5 Connecting to Documentation

The inventory serves as a **hub** linking to relevant documents, not duplicating them:

```
Data Entity: "Interview transcripts - local officials"
    │
    ├── Information Letter → /RDM/Templates/InfoLetter_Interviews_EN.docx
    ├── Consent Form → /RDM/Templates/Consent_Interviews_EN.docx
    ├── Sikt Reference → Sikt #123456 (link to notification)
    └── Storage Location → /Research/Interviews/Transcripts/
```

This creates traceability: for any data entity, you can find the legal basis, consent documentation, and current location.

### 3.6 Handling Changes

Projects evolve. The inventory accommodates this:

| Change | Action |
|--------|--------|
| New data entity identified | Add new row; assign preliminary classification; flag for documentation |
| Sensitivity changes | Update classification; review if storage/access needs adjustment |
| Scope reduction (data not collected) | Update status to "Not collected" or delete row; add note |
| Unexpected data received | Add entry; assess sensitivity; ensure documentation covers it |

Significant changes (e.g., new sensitive data category) may trigger a mini-review with rdm@cmi.

### 3.7 Relationship to Other Recommendations

| Recommendation | Relationship |
|----------------|--------------|
| **#2 Assessment** | Assessment identifies initial data entities → Inventory is populated |
| **#4 RDM Channel** | Inventory lives in RDM channel; links to document bundle |
| **#5 Project Closure** | Inventory is finalised; retention/deletion documented here |

### 3.8 Optional: Central Overview

For rdm@cmi oversight across all projects, a **summary view** can be created:
- Power BI dashboard pulling from all project inventories, or
- Central SharePoint list with one row per project summarising data entity count, highest sensitivity level, and status

This supports:
- Annual reporting (e.g., to management, funders)
- Identifying projects approaching closure
- Spotting patterns (common data types, recurring documentation needs)

**Note:** This is optional and should not create additional burden for project teams. It is rdm@cmi's responsibility to maintain if implemented.

## Example Inventory Entries

| Entity ID | Entity Name | Type | Sensitivity | Status | Legal Basis | Storage |
|-----------|-------------|------|-------------|--------|-------------|---------|
| DE-001 | Interview recordings - local officials | Primary | Confidential | Collecting | Consent | Teams > Research > Interviews > Audio |
| DE-002 | Interview transcripts - local officials | Primary | Confidential | Planned | Consent | Teams > Research > Interviews > Transcripts |
| DE-003 | Survey responses (anonymised) | Primary | Restricted | Complete | Consent | Teams > Research > Survey > Data |
| DE-004 | SSB register extract | Secondary | Confidential | Processing | Public interest | Tresorit > RegisterData |
| DE-005 | Published dataset (output) | Output | Open | Planned | N/A | DataverseNO (planned) |

## What the Inventory is NOT

- **Not a file register:** Does not track individual files, only categories/entities
- **Not a surveillance tool:** Not used to monitor researcher productivity
- **Not a compliance checkbox:** Exists to support the project, not satisfy bureaucracy
- **Not static:** Expected to evolve as project develops

## Success Indicators

- All active projects have a data inventory in their RDM channel
- Inventories are updated at key milestones (not necessarily real-time)
- Documentation links are functional and current
- Project teams find the inventory useful, not burdensome