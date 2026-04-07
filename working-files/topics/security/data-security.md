---
version: "1.0"
date: 2026-03-11
notes:
  - Customer Lockbox and Customer Key status unconfirmed — left out for now.
  - Storage recommendations should be reviewed with CMI IT.
  - Confirm whether CMI needs to apply for a TSD project allocation or whether
    access can be arranged through an existing agreement with UiO or another institution.
  - Document CMI's actual backup arrangements.
---

# Data Security — CMI

<!-- WHERE data lives and HOW it is protected: storage infrastructure, access control,
     and backup. The companion to data-classification.md, which defines WHAT tier data
     falls into.

     Refactored from the former data-security-policy.md. Sections that moved to their
     own modules:
     - Fieldwork data security → fieldwork.md
     - Retention and deletion → retention.md
     - AI tools and data security → tools-and-services.md
     - Archiving and long-term storage → open-science.md (repository defaults)

     For the classification scheme and tier definitions, see data-classification.md.
     For GDPR interpretive positions, see gdpr-positions.md. -->

**This is a draft.** Storage recommendations should be reviewed with CMI's IT team. Specific infrastructure details (e.g., exact M365 configurations, TSD project setup) should be verified against current institutional arrangements.


## Guiding principle: proportional security

Data security at CMI follows the same proportionality principle that governs our GDPR interpretation. The security measures applied to a data object should match its actual sensitivity and the realistic risk of harm if it were exposed. Over-securing low-sensitivity data wastes researcher time and creates friction that discourages compliance. Under-securing high-sensitivity data creates real risk to participants and the institution.

The goal is that a researcher can quickly determine: what kind of data do I have, where does it go, and who can access it? The four-tier classification scheme in `data-classification.md` answers the first question. This document answers the second and third.


## Storage infrastructure

### CMI's primary ecosystem: Microsoft 365 E5

CMI uses Microsoft 365 E5 as its primary digital infrastructure. This includes OneDrive, SharePoint, Teams, and associated services. Default security features include:

- **EU Data Boundary**: CMI's M365 tenant stores data within EU/EFTA data centres. Data does not leave Europe for operational purposes.
- **Encryption at rest and in transit**: all data stored in M365 is encrypted at rest; all connections use TLS encryption in transit.
- **Access controls**: SharePoint and Teams permissions control who can view, edit, and share files. Researchers manage access at the project level through Teams channel membership and SharePoint site permissions.
- **Multi-factor authentication (MFA)**: required for all CMI accounts.
- **Data Loss Prevention (DLP)**: policies that can prevent accidental sharing of sensitive data via email, Teams, or SharePoint.

### Storage by classification tier

| Tier | Primary storage | Notes |
|---|---|---|
| **Green** (Open) | M365 (OneDrive/SharePoint), public repositories (Zenodo, openICPSR, OSF) | No restrictions. Can use any storage, but it is recommended to use M365 Sharepoint or OneDrive as the default for CMI-related files. |
| **Yellow** (Internal) | M365 (OneDrive/SharePoint/Teams) | Access limited to project team and relevant CMI staff. Standard M365 access controls. |
| **Red** (Confidential) | M365 (Teams/SharePoint/OneDrive) as default. For projects requiring higher assurance, consider external services: TSD (especially Nettskjema for data collection), Tresorit, Proton Drive, or other high-security services. | Access limited to project team, granted by PI. Choice of platform depends on the specific data, the collaboration context, and the risk assessment. See guidance below. |
| **Black** (Strictly confidential) | Case-by-case assessment. No single default solution. Options include TSD, Tresorit, Proton Drive, encrypted local storage, or purpose-built secure environments depending on the project's specific risk profile. | The PI, in consultation with the RDM contact (rdm@cmi.no) and IT, determines the appropriate storage solution for each Black-tier project. |

### Choosing storage for Red-tier data

M365 (Teams, SharePoint, OneDrive) is the default for most Red-tier data. Teams channels with restricted membership provide adequate access control for most projects involving personal data — interview transcripts, survey datasets, consent forms, participant contact lists.

However, some projects may benefit from or require external services:

- **TSD / Nettskjema**: particularly relevant when the project involves survey data collection from identifiable participants. Nettskjema (which integrates with TSD) provides a GDPR-compliant survey tool with data stored in Norwegian sovereign infrastructure. Useful when the data collection method itself needs to be secure, not just the storage.
- **Tresorit**: end-to-end encrypted, zero-knowledge architecture, Swiss jurisdiction (not subject to CLOUD Act). Useful for projects where the CLOUD Act concern is specifically relevant or where collaboration with external partners requires a high-security sharing tool outside M365.
- **Proton Drive**: similar Swiss jurisdiction advantages. Simpler and cheaper than Tresorit, but fewer collaboration features.
- **Other high-security services**: assess on a case-by-case basis. The key criteria are: encryption (at rest and in transit), access controls, data residency (EU/EEA or adequate jurisdiction), and data processing agreements.

**Note**: CMI does not currently have a TSD agreement. TSD and all external services involve additional costs. The decision to use an external service should be based on a proportional assessment of the data's sensitivity and the project's specific requirements — not a blanket policy.

### Choosing storage for Black-tier data

There is no single default solution for Black-tier data. The appropriate storage depends on the specific nature of the risk:

- If the risk is **state surveillance or intelligence interest** (e.g., corruption research, human rights research in authoritarian contexts): consider Swiss-jurisdiction services (Tresorit, Proton Drive) or TSD, which are outside US CLOUD Act reach.
- If the risk is **participant safety** (e.g., identification could endanger individuals): the priority is minimising the number of copies and access points. TSD's remote-access model (partners work within the environment, data never leaves) may be appropriate. Alternatively, encrypted local storage with no cloud component.
- If the risk is **legal or contractual** (e.g., data access agreements with strict handling requirements): follow the data provider's requirements, which may specify a particular infrastructure.
- If the risk is **reputational or institutional** (e.g., commercially sensitive partner data): M365 with strict access controls may be sufficient.

The PI should consult with the RDM contact (rdm@cmi.no) and IT to determine the right solution for each Black-tier project. Document the decision and the reasoning in the DMP.

**Action for the researcher**: determine storage requirements during project planning based on data classification. For Red-tier data, M365 is the default — document any decision to use external services. For Black-tier data, consult the RDM contact (rdm@cmi.no) and IT before data collection begins. Document storage decisions in the DMP.

### About TSD (Services for Sensitive Data)

TSD is the Norwegian national infrastructure for processing sensitive personal data in research. It is operated by the University of Oslo (USIT) and designed for GDPR compliance up to the highest sensitivity levels.

Key characteristics:
- Data is stored in Norway and never leaves Norwegian jurisdiction.
- Access is via web-based remote login with two-factor authentication.
- Researchers (including international partners) can access and work with data inside TSD without the data being transferred to their own devices or institutions.
- Built-in tools include virtual machines, Nettskjema integration for surveys, and file storage.
- Cost: approximately 20,500 NOK + VAT per project per year.

**CMI does not currently have a TSD agreement.** Using TSD requires applying for a project allocation through a Norwegian institution. Costs are per-project and should be budgeted in the project proposal if TSD is anticipated.

**When TSD is most relevant for CMI**:
- Projects using Nettskjema for survey data collection involving personal data (TSD/Nettskjema integration is the primary draw for many projects)
- Black-tier projects where Norwegian sovereign infrastructure is specifically needed
- Projects where funders or ethics boards require infrastructure outside US jurisdiction
- Projects involving sensitive data collection from international participants where TSD's remote-access model avoids cross-border transfer issues

**TSD is one option among several**, not the automatic default for all sensitive data. For many Red-tier projects, M365 with appropriate access controls is sufficient. For Black-tier projects, TSD competes with Swiss-jurisdiction alternatives that may offer better collaboration features for international partnerships.

**Note**: CMI's TSD access route is not yet confirmed — see front matter notes.

### About the CLOUD Act concern

Microsoft is a US company. Under the US CLOUD Act, US authorities can in theory compel Microsoft to hand over data regardless of where it is stored. This is a real legal exposure, but it should be assessed proportionally:

- CMI's M365 data is stored in the EU/EFTA Data Boundary and is operationally subject to EU law.
- Microsoft has committed to challenging US government requests for EU data and has stated it has not received CLOUD Act requests for EU customer data (as of public statements).
- If CMI enables Customer Key (included in E5), data is encrypted with CMI-managed keys — even if compelled to hand over data, Microsoft would be handing over encrypted data.
- CMI is a development research institute, not a high-value intelligence target. The realistic likelihood of a CLOUD Act request is very low for most CMI work.
- **Exception**: research involving corruption, governance in countries where US interests are significant, or partners in sanctioned countries could theoretically be of interest. For these projects, use TSD.

**Default position**: M365 E5 with appropriate access controls is adequate for the majority of CMI research data (Green, Yellow, and most Red-tier data). For Red-tier data with elevated risk or specific collaboration needs, external high-security services (TSD/Nettskjema, Tresorit, Proton Drive) are available but involve additional costs. For Black-tier data, the storage solution is determined case-by-case based on the specific risk profile.


## Access control

### Principles

- Access is granted on a **need-to-know basis**. Not everyone on a project team needs access to all data objects. A project controller needs access to budget data but not to interview recordings.
- The **PI (Principal Investigator)** is responsible for deciding who has access to project data and for revoking access when it is no longer needed.
- **External collaborators** (partner institution staff, research assistants) should have access only to the data they need for their role. For M365, this is managed through guest access with appropriate SharePoint/Teams permissions. For TSD, partners are added as named users.

### Default access by tier

| Tier | Default access |
|---|---|
| Green (Open) | Any CMI staff; public after publication |
| Yellow (Internal) | Project team and relevant CMI staff (project controller, group leader) |
| Red (Confidential) | Project team only, approved by PI. External collaborators with appropriate access restrictions. |
| Black (Strictly confidential) | PI and named individuals only. Access must be documented. Storage and access mechanisms determined case-by-case (TSD, Tresorit, encrypted local storage, etc.). |

### When people leave

- When team members leave the project or CMI, their access to project data should be revoked promptly.
- For M365: remove from relevant SharePoint/Teams groups.
- For external services (TSD, Tresorit, etc.): remove user account or revoke sharing.
- For data stored locally on the departing person's CMI device: ensure data is transferred to institutional storage or deleted as appropriate.


## Backup

**Note**: CMI's actual backup arrangements are not yet documented — see front matter notes. The following are recommended minimums.

- All research data on M365 is backed up through Microsoft's built-in redundancy and retention policies. Confirm that these are adequate and that backup retention aligns with CMI's needs.
- TSD provides its own backup within the TSD environment.
- Researchers should not maintain personal backups of Confidential or Strictly Confidential data on personal devices or personal cloud accounts.
- For fieldwork, separate backup procedures apply (see `fieldwork.md`).

**Action for the researcher**: review access controls at project milestones and when team membership changes. Ensure backup arrangements are adequate for the data's classification tier.

**Escalation**: consult the RDM contact (rdm@cmi.no) for guidance on storage selection for Black-tier data, CLOUD Act concerns, or TSD project setup.
