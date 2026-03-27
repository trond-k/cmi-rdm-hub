# CMI RDM Pipeline: Assessment, Refinements & Expansions

## Overall Assessment

**Strengths of the current draft:**
- Appropriate scaling for institute size; avoids over-engineering
- Pragmatic "light-touch" philosophy that respects researcher autonomy
- Good use of Microsoft 365 ecosystem (Teams, Lists) already in place
- Clear lifecycle approach (project start → active phase → closure)
- Recognition that complexity requires human judgment, with machine assistance

**Gaps identified:**
- Limited attention to the *intake/trigger* mechanism (how does rdm@cmi learn of new projects?)
- No explicit handling of project amendments or scope changes mid-project
- Archival/preservation pathway underdeveloped
- LLM integration points mentioned but not operationalised
- Missing: researcher training/onboarding touchpoint
- Missing: handling of legacy/inherited data from previous projects

---

## Recommendation-by-Recommendation Refinements

### Recommendation #1: Teams-based Project Structure

**Current:** Projects as Teams for fine-grained access control.

**Refinements:**
- Define a **standard Team template** with pre-configured channels:
  - General
  - RDM (for rdm@cmi integration)
  - Data & Methods (optional, for technical discussions)
  - Outputs & Publications
- Establish **naming conventions** (e.g., `CMI-2025-ProjectAcronym`) for searchability
- Create a **Team lifecycle policy**: active → archived → deleted, with defined retention periods
- Consider **sensitivity labels** at Team level (Microsoft Purview) that inherit to documents

**Addition:** Create a lightweight **project registry** (could be a SharePoint list or simple database) that serves as the "single source of truth" for all projects, linking to their Teams, status, and key RDM metadata.

---

### Recommendation #2: Initial Assessment & Classification

**Current:** rdm@cmi assesses data entities, assigns sensitivity categories, identifies DMP/DPIA needs.

**Refinements:**
- Formalise the **intake trigger**: rdm@cmi should be notified at proposal submission (not just award), allowing pre-award RDM input
- Create a **structured intake form** (Microsoft Forms or similar) that project leads complete, providing:
  - Brief data description
  - Expected data types (interviews, surveys, register data, secondary data, etc.)
  - Partner institutions and countries
  - Funder requirements
  - Anticipated ethical sensitivities

**Proposed sensitivity classification matrix:**

| Category | Description | Storage | Access | Examples |
|----------|-------------|---------|--------|----------|
| Open | No restrictions anticipated | Teams/SharePoint | Project team + wider | Published datasets, public documents |
| Restricted | Internal use, some sensitivity | Teams (standard) | Project team | Working papers, non-sensitive interview notes |
| Confidential | Personal data, sensitive topics | Teams + encryption | Named individuals only | Identifiable interview data, health data |
| Highly Confidential | Special category data, high-risk | TSD or equivalent | Strict need-to-know | Vulnerable populations, security-sensitive |

**Risk classification (separate from sensitivity):**

| Risk Level | Indicators | RDM Response |
|------------|------------|--------------|
| Low | Single institution, open data, low complexity | Light-DMP, minimal monitoring |
| Medium | Multiple partners, personal data, funder requirements | Full DMP, periodic check-ins |
| High | Sensitive populations, cross-border transfers, novel methods | DPIA, ethics review, active RDM involvement |

**LLM integration point:** Use LLM to parse proposal documents and pre-populate the intake form, flag potential sensitivities, and suggest classification. Human validates.

---

### Recommendation #3: Data Inventory

**Current:** Lists-based inventory for tracking.

**Refinements:**
- Clarify inventory granularity: track **data entities**, not individual files
- Suggested inventory fields:
  - Entity ID (auto-generated)
  - Entity name/description
  - Type (primary/secondary; qualitative/quantitative)
  - Sensitivity category
  - Storage location (with link)
  - Legal basis (consent, legitimate interest, etc.)
  - Retention period
  - Status (planned, collecting, processing, archived, deleted)
  - Associated documents (consent forms, Sikt reference, etc.)
- Include a **version/update log** field for tracking changes

**Alternative approach:** Consider whether this should be project-level (within each Team) or centralised (institute-wide register). A hybrid might work: project-level Lists that feed into a central Power BI dashboard for rdm@cmi oversight.

**LLM integration point:** LLM can draft initial inventory entries based on project documentation; researchers validate and refine.

---

### Recommendation #4: Embedded RDM Presence

**Current:** Dedicated RDM channel with document bundle.

**Refinements:**
- Standardise the **document bundle** contents:
  1. `ProjectName_RDM_Overview.docx` – summary of classifications, recommendations, key contacts
  2. `ProjectName_LightDMP.docx` – internal DMP (always)
  3. `ProjectName_FunderDMP.docx` – if required (RCN, Horizon, etc.)
  4. `ProjectName_InformationLetter_[Language].docx` – template(s)
  5. `ProjectName_ConsentForm_[Language].docx` – template(s)
  6. `ProjectName_SiktNotification_Draft.docx` – pre-filled if applicable
  7. `ProjectName_EthicsSummary.docx` – brief ethics assessment
  8. `ProjectName_DataInventory.xlsx` – or link to Lists

- Add **milestone prompts**: rdm@cmi sets reminders for key check-in points:
  - Data collection start
  - Mid-project review (for longer projects)
  - 3 months before project end
  - Project closure

**Alternative: RDM "Office Hours"** – Instead of (or in addition to) channel-based interaction, rdm@cmi could offer regular drop-in sessions for researchers. Lower friction for quick questions.

**LLM integration point:** LLM generates first drafts of all bundle documents based on intake form and proposal; populated with project-specific details. Researcher and rdm@cmi review and adjust.

---

### Recommendation #5: Project Closure

**Current:** Generate updated final docs.

**Refinements:**
- Create a **closure checklist**:
  - [ ] Data inventory finalised and verified
  - [ ] All data entities classified for retention/deletion/archival
  - [ ] Consent obligations fulfilled (data deleted if required)
  - [ ] Final DMP completed
  - [ ] Archival copies deposited (if applicable)
  - [ ] External access revoked
  - [ ] Sikt/REC notified of project completion (if required)
  - [ ] Funder deliverables submitted

- Define **preservation pathways**:
  - Deletion (with documentation)
  - Internal archive (CMI long-term storage)
  - External repository (NSD/DataverseNO, Zenodo, domain repository)
  - Restricted archive (TSD or similar for sensitive data with retention requirements)

- **Team archival**: Move to archived state in Teams; retain read access for specified period; then delete or migrate to cold storage.

**LLM integration point:** LLM compares final data inventory against initial plan, flags discrepancies, drafts closure report.

---

## Additional Recommendations

### Recommendation #6: Lifecycle Event Triggers

Add explicit handling for **mid-project changes**:
- Scope expansion (new data collection, new partners)
- Change of PI or key personnel
- Ethics amendments
- Funder changes

Each should trigger a mini-review by rdm@cmi to assess whether classifications or documentation need updating.

---

### Recommendation #7: Researcher Onboarding Touchpoint

For new CMI researchers or new project team members:
- Brief RDM orientation (can be asynchronous/recorded)
- Introduction to CMI systems and expectations
- Point of contact for questions

This reduces friction and ensures consistent baseline knowledge.

---

### Recommendation #8: External Collaborator Protocol

Given CMI's international partnerships:
- Standard process for granting/revoking external access
- Data sharing agreement templates (distinct from DPAs)
- Clear expectations document for external collaborators
- Periodic access review (e.g., annually or at project milestones)

---

### Recommendation #9: Legacy Data Handling

For projects using data from previous CMI projects or external sources:
- Provenance documentation requirements
- Verification of continued legal basis
- Clear chain of custody in data inventory

---

## LLM/Agent Integration Architecture

### Proposed "RDM Assistant" Capabilities

| Function | Input | Output | Human Role |
|----------|-------|--------|------------|
| Intake parsing | Proposal PDF, grant application | Pre-filled intake form, flagged sensitivities | Validate, adjust |
| Classification suggestion | Intake form data | Proposed sensitivity/risk levels | Approve or override |
| Document generation | Classification + project details | Draft bundle documents | Review, edit, approve |
| Inventory drafting | Project description, methods section | Initial data entity list | Verify, complete |
| Compliance checking | Project docs + regulatory requirements | Gap analysis, missing items | Address gaps |
| Closure review | Final inventory vs. initial plan | Discrepancy report, draft closure docs | Verify, finalise |
| Query answering | Researcher questions | Guidance based on CMI policies, regulations | Escalate complex cases |

### Implementation Considerations

- **Prompt library**: Develop and version-control prompts for each function
- **Context provision**: Ensure LLM has access to CMI policies, Norwegian regulations, funder requirements
- **Audit trail**: Log LLM suggestions and human decisions for accountability
- **Guardrails**: Human approval required for all classifications and external-facing documents
- **Feedback loop**: Track where LLM suggestions are modified to improve prompts

---

## Artefacts Library (Expanded)

### Policy & Guidance Documents
- CMI Research Data Policy (if not existing, recommend creating)
- Storage and security decision tree
- Sensitivity classification guide with examples
- Data sharing principles

### Templates (Document Bundle)
- Light-DMP template
- Funder-specific DMP templates (RCN, Horizon Europe, ERC)
- Information letter templates (Norwegian, English; various data types)
- Consent form templates
- Data sharing agreement template
- External collaborator expectations document

### Checklists
- Project intake checklist
- Mid-project review checklist
- Closure checklist
- External access review checklist

### Reference Materials
- Ethics issues catalogue (as mentioned)
- Common data types at CMI and their typical classifications
- Regulatory quick-reference (GDPR, Health Research Act, etc.)
- Funder requirements summary

### For LLM Context
- Consolidated CMI RDM policies
- Norwegian research data regulations summary
- Ethics issues catalogue (structured for LLM parsing)
- Example completed documents (anonymised)

---

## Implementation Roadmap

### Phase 1: Foundation (Months 1-3)
- Finalise policy decisions and classification matrices
- Create Team template and naming conventions
- Develop core document templates
- Set up project registry
- Pilot with 2-3 new projects

### Phase 2: Operationalise (Months 4-6)
- Roll out to all new projects
- Develop LLM prompts and test
- Create researcher onboarding materials
- Establish milestone reminder system

### Phase 3: Extend (Months 7-12)
- Migrate active projects to new structure
- Refine based on feedback
- Develop Power BI dashboard for oversight
- Document lessons learned

### Phase 4: Mature (Year 2+)
- Address legacy projects
- Enhance LLM capabilities based on experience
- Consider automation of routine tasks
- Regular policy review cycle

---

## Alternative Approaches Considered

### Full Automation Pipeline
**Rejected because:** CMI's diverse project portfolio (development research, mixed methods, varied geographies and partners) makes rule-based automation brittle. Human judgment remains essential for edge cases.

### Centralised Data Repository Model
**Partially adopted:** Rather than requiring all data in a central repository, the recommendation maintains flexibility (Teams, TSD, etc.) with central *tracking* through the registry and inventory.

### Minimal/Reactive RDM
**Rejected because:** Regulatory requirements (GDPR, funder mandates) and reputational considerations require proactive engagement. The "light-embedded" model balances this with researcher autonomy.

### Heavy Compliance Model
**Rejected because:** Disproportionate to CMI's scale and would create friction that reduces researcher engagement. The tiered approach (light for low-risk, intensive for high-risk) is more appropriate.