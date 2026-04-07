# Recommendation #1: Teams-based Project Structure

## Rationale

Moving from shared folders to Microsoft Teams as the primary project workspace enables fine-grained access control, better collaboration features, and a clearer project lifecycle. Teams integrates naturally with other Microsoft 365 tools (Lists, SharePoint, Planner) that support RDM workflows.

## Core Recommendation

All new research projects are created as dedicated Teams, replacing the current practice of creating project folders within a shared "projects" directory.

## Implementation

### 1.1 Team Creation

**For all new projects:**
- A dedicated Team is created at project initiation
- rdm@cmi is added as a member to all project Teams (see Recommendation #2)
- Project PI/coordinator is assigned as Team owner

**Naming convention (existing):**
```
[ProjectNumber]-[Funder]-[ProjectName]
```
Example: `25098-NFR-Pre-projectIndia`

This existing convention is retained. It provides:
- Unique project identification via number
- Quick funder identification (NFR, Horizon, ERC, etc.)
- Human-readable project name

### 1.2 Standard Team Template

All project Teams are created from a standard template with the following channel structure, mapped from the current SharePoint folder organisation:

| Channel | Purpose | Subfolders (in Files tab) |
|---------|---------|---------------------------|
| **General** | Project-wide announcements, key links, quick access | — |
| **Admin** | Administrative and contractual documentation | `Contract`, `Proposal`, `Project-Management`, `Meetings-And-Minutes` |
| **RDM** | Research data management (rdm@cmi integration, document bundle, data inventory) | `Documentation`, `Templates` |
| **Research** | Working documents, data, analysis, fieldwork materials | As needed by project |
| **Outputs** | Publications, reports, deliverables, dissemination | `Output`, `Research-Communication` |

**Mapping from current structure:**

| Current SharePoint Folder | → Teams Location |
|---------------------------|------------------|
| Contract | Admin channel → Contract folder |
| Meetings-And-Minutes | Admin channel → Meetings-And-Minutes folder |
| Project-Management | Admin channel → Project-Management folder |
| Proposal | Admin channel → Proposal folder |
| Output | Outputs channel → Output folder |
| Research-Communication | Outputs channel → Research-Communication folder |
| Workspace | Research channel (working area) |

Additional channels can be added by project teams as needed (e.g., Work Packages, Fieldwork, Partner Coordination).

### 1.3 Access Control Principles

| Role | Access Level | Granted By |
|------|--------------|------------|
| PI / Project Coordinator | Owner | IT/Admin at project creation |
| Core project team (CMI) | Member | PI |
| rdm@cmi | Member | Automatic at creation |
| External collaborators | Guest | PI (with documented justification) |

**Guest access (external collaborators):**
- Limited to specific channels where needed (not full Team access by default)
- Documented in project registry with start date and expected end date
- Subject to periodic review (see 1.5)

**Note: Partial openness within Teams**

Microsoft Teams does not natively support making specific channels open to all CMI staff while keeping others restricted to project members. The options are:
- *Public Teams* (entire Team open—not suitable for most research projects)
- *Private channels* (restrict access to fewer people, not more)

**Recommended approach:** Keep project Teams private. For transparency and knowledge sharing, consider a separate **CMI Research Hub** (public Team or SharePoint site) where projects can *push* content when ready to share (project summaries, published outputs, presentations, news). This maintains a clear boundary: project workspaces are private until content is deliberately shared.

This two-layer model:
- Protects working documents, contracts, and data documentation
- Supports compliance and access control clarity
- Still enables institutional visibility and knowledge sharing
- Can be implemented later without affecting project Team structure

### 1.4 Project Registry

A central **Project Registry** (SharePoint List) is maintained by rdm@cmi, serving as a single source of truth for all projects:

| Field | Description |
|-------|-------------|
| Project ID | Unique identifier (e.g., CMI-2025-GOVTRUST) |
| Project Title | Full project name |
| PI | Principal Investigator |
| Start Date | Project start |
| End Date (planned) | Anticipated completion |
| Status | Active / On hold / Completed / Archived |
| Team Link | URL to project Team |
| Sensitivity Level | Overall project classification (see Rec #2) |
| Risk Level | Low / Medium / High (see Rec #2) |
| External Collaborators | Count and institutional affiliations |
| Funder | RCN, Horizon, ERC, Other, Internal |
| Notes | Any relevant comments |

This registry:
- Provides oversight without requiring access to individual Teams
- Supports annual reporting and compliance checks
- Enables identification of projects approaching closure

### 1.5 Team Lifecycle

**Phase 1: Active**
- Full collaboration functionality
- Regular use by project team
- rdm@cmi check-ins at defined milestones

**Phase 2: Completed → Archived**
- Triggered when project is formally concluded
- Team is archived in Microsoft Teams (read-only access preserved)
- Final documentation completed (see Recommendation #5)
- External collaborator access reviewed and revoked where appropriate
- Retention period: [X years - to be determined based on funder requirements and CMI policy]

**Phase 3: Archived → Deleted or Cold Storage**
- After retention period expires
- Data either deleted (with documentation) or migrated to long-term storage
- Team deleted from active environment
- Registry entry updated to reflect final status

### 1.6 Migration Plan

**Immediate (new projects):**
- All projects initiated from [implementation date] use Teams structure

**Short-term (active projects):**
- Ongoing projects migrated to Teams within [6 months]
- Priority given to projects with external collaborators or sensitive data
- Migration includes setting up RDM channel and baseline documentation

**Medium-term (completed projects):**
- Finalised projects assessed for archival status
- Relevant materials migrated to archived Teams or long-term storage
- Defunct project folders removed after verification

**Access review:**
- One-time audit of external collaborator access across all projects
- Revocation of access for collaborators no longer actively involved
- Establishment of annual access review cycle

## Considerations and Dependencies

- **IT capacity**: Team creation and template management requires IT support initially; consider whether this can be delegated to rdm@cmi or project administrators
- **Training**: Brief guidance for PIs on Team management, guest access, and channel use
- **Sensitivity labels**: Consider implementing Microsoft Purview sensitivity labels at Team level for projects classified as Confidential or Highly Confidential (may require IT/security involvement)
- **Storage limits**: Monitor SharePoint storage associated with Teams; establish guidelines for large file handling

## Success Indicators

- All new projects have dedicated Teams within [1 month] of initiation
- Project registry is complete and current
- No new project folders created in legacy "projects" structure
- External collaborator access documented and reviewed annually