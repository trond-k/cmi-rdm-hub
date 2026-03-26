# Horizon Europe: Data Management and Open Science Requirements

**Compiled: 2026-03-26 | For: CMI RDM Guidance Hub**

---

## 1. Overview

Open science is a **legal obligation** under Horizon Europe, enshrined in **Article 17** and **Annex 5** of the Model Grant Agreement (MGA). The framework establishes two categories:

**Mandatory practices (legally binding):**
- Immediate open access to peer-reviewed publications
- Open access to research data, following "as open as possible, as closed as necessary"
- Research data management in line with FAIR principles
- Provision of information about outputs/tools needed to validate research conclusions

**Recommended practices (assessed in evaluation, not legally binding):**
- Early and open sharing (preprints, preregistration, registered reports)
- Open peer review
- Citizen science and stakeholder co-creation
- Use of open research infrastructure
- Reproducibility measures
- Open access to non-peer-reviewed outputs (software, workflows, protocols)

The authoritative legal text is the Annotated Grant Agreement (AGA), most recently updated on 1 April 2025. The Horizon Europe Programme Guide (pp. 38-46) provides explanatory guidance.

---

## 2. Data Management Plan (DMP) Requirements

### 2.1 When is a DMP required?

A DMP is **mandatory for all Horizon Europe projects** that generate or reuse research data. It is both a proposal component and a grant deliverable.

### 2.2 Timeline

| Stage | Requirement |
|---|---|
| **Proposal submission** | Brief/initial DMP (~1 page) in Part B, Section 1.2 (Methodology) |
| **Month 6 after grant signature** | Comprehensive DMP submitted as mandatory deliverable |
| **Mid-project** (projects >12 months) | Updated DMP submitted as deliverable |
| **Project end** | Final DMP describing actual data management and sharing outcomes |

The DMP is a **living document** that must be updated whenever significant changes occur.

### 2.3 Relationship to the proposal

At proposal stage, open science and data management are in **Part B, Section 1.2 (Methodology)** under the Excellence criterion:
- ~1 page for the **Open Science subsection** (mandatory and recommended practices)
- ~1 page for the **Research Data Management subsection** (FAIR principles, data types, repositories)

The initial DMP should briefly address:
1. **Data Summary** -- types, estimated size, collection/reuse approach, origins
2. **FAIR Management** -- compliance approach, repositories, access provisions, standards
3. **Curation and Storage** -- responsible parties, quality assurance, estimated costs

### 2.4 Comprehensive DMP structure (post-award)

The EC provides an official [Horizon Europe DMP Template](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/temp-form/report/data-management-plan_he_en.docx). Seven sections:

1. **Data Summary** -- data types, formats, purpose, size, origin, reuse potential
2. **FAIR Data** (four subsections):
    - *Findability* -- persistent identifiers, keywords, metadata standards
    - *Accessibility* -- repository details, access protocols, metadata availability
    - *Interoperability* -- vocabularies, standards, formats
    - *Reusability* -- documentation, methodologies, licensing
3. **Other Research Outputs** -- software, models, workflows, protocols, materials
4. **Allocation of Resources** -- costs, personnel responsibilities
5. **Data Security** -- storage, backup, recovery, protection
6. **Ethics** -- legal issues, personal data, informed consent, long-term preservation
7. **Other Issues** -- additional procedures

### 2.5 DMP tools

- **Argos** (OpenAIRE) -- aligned with Horizon Europe template
- **DMPonline** (DCC) -- supports Horizon Europe template
- **Data Stewardship Wizard**
- **Sikt DMP** (plan.research-data.no) -- includes Horizon Europe questionnaire
- DMPs should ideally be **public deliverables** under CC BY

---

## 3. Open Access to Research Data

### 3.1 Default policy

Open access to research data is **mandatory by default**. Governing principle: **"As open as possible, as closed as necessary."**

Beneficiaries must:
- Manage digital research data in line with FAIR principles
- Deposit data in a trusted repository
- Provide open access as soon as possible, within DMP deadlines
- Apply **CC BY** (latest version) or **CC0** licensing

### 3.2 Opt-out grounds (legitimate exceptions)

Data may be kept closed, restricted, or under embargo if open access would:

1. **Conflict with legitimate commercial interests**, including commercial exploitation
2. **Violate data protection rules** (GDPR, privacy)
3. **Breach confidentiality obligations**
4. **Compromise trade secrets**
5. **Harm EU competitive interests**
6. **Violate security rules**
7. **Infringe intellectual property rights**
8. **Contradict other obligations** specified in the Grant Agreement

**Critical requirement:** Any restriction must be **explicitly justified in the DMP**. Blanket opt-outs without specific reasoning are not acceptable.

### 3.3 Metadata must always be open

Even when data is restricted, **metadata must always be deposited openly** under CC0 or equivalent, including:
- Author(s), description/abstract, deposit/publication date
- Repository venue, license, embargo period (if any)
- Horizon Europe funding information (grant name, acronym, number)
- Persistent identifiers (DOI for dataset, ORCID for authors, ROR for organisations, grant DOI)

---

## 4. Open Access to Publications

### 4.1 Core requirement

**Immediate open access** to all peer-reviewed scientific publications. **No embargo periods permitted.** Deposit a machine-readable copy of:
- The **published version** (Version of Record), OR
- The **final peer-reviewed manuscript** (Author Accepted Manuscript)

in a **trusted repository** at the latest **at the time of publication**.

### 4.2 Licensing

| Publication type | Required license |
|---|---|
| **Journal articles** | CC BY or equivalent (mandatory) |
| **Monographs, book chapters** | CC BY, CC BY-NC, or CC BY-ND |

### 4.3 Rights retention strategy

When publishers require copyright transfer, apply the **Rights Retention Strategy** (cOAlition S):

Add at manuscript submission: *"This work was funded by the European Union [grant number]. For the purpose of Open Access, the author has applied a CC BY public copyright licence to any Author Accepted Manuscript version arising from this submission."*

Beneficiaries are legally required to **retain sufficient IP rights** to comply with open access obligations (Article 17 MGA).

### 4.4 Repository requirements

Acceptable: institutional repositories, subject-based/disciplinary repositories (arXiv, SSRN, RePEc), general-purpose (Zenodo, EU Open Research Repository).

**Not acceptable:** personal websites, cloud storage (Google Drive, OneDrive), academic networking sites (Academia.edu, ResearchGate).

Deposit required **even if published in a fully OA journal**.

### 4.5 Hybrid journals

Publishing in hybrid journals is permitted, **but the APC is NOT eligible for reimbursement**. Comply via Green OA (self-archiving AAM in repository).

---

## 5. FAIR Data Principles

FAIR is a **binding obligation**, not merely a recommendation.

**Findable:** Assign PIDs (DOIs) to all datasets; rich, standardised metadata; register in searchable resources; use ORCID/ROR.

**Accessible:** Deposit in trusted repositories with standardised access protocols; metadata must remain accessible even if data becomes unavailable; machine-actionable metadata.

**Interoperable:** Community-accepted formats and standards; controlled vocabularies and ontologies; qualified references to related datasets and publications.

**Reusable:** Clear open licenses (CC BY or CC0); detailed provenance; documentation of methodologies, parameters, software versions; information about tools needed for validation/reuse.

**FAIR for metadata specifically:** Must be open (CC0), machine-actionable, standardised, and include PIDs linking datasets, authors, organisations, grants, and related publications.

---

## 6. Data Sharing and Archiving

### 6.1 Repository requirements (order of preference)

1. **Certified repositories** -- CoreTrustSeal, Nestor Seal (DIN 31644), or ISO 16363
2. **Discipline-specific repositories** -- endorsed by research community (e.g., CESSDA for social science)
3. **Institutional repositories** -- with adequate security, metadata, preservation
4. **General-purpose** -- Zenodo, EU Open Research Repository
5. **EOSC-federated repositories** -- for calls requiring EOSC integration

Find repositories at [re3data.org](https://www.re3data.org/) or [FAIRsharing.org](https://fairsharing.org/).

### 6.2 Persistent identifiers required

- **DOI** for the dataset
- **ORCID** for authors
- **ROR** for organisations (where possible)
- **Grant DOI** for funding reference

### 6.3 Timing

- Deposit **as soon as possible** after generation
- **Latest by project end**
- Publications: deposit data **with or before** publication
- Public emergency: immediate open access may be required

---

## 7. Eligible Costs

### 7.1 Data management costs

Eligible if **budgeted in the proposal** and **incurred during the project**:
- Personnel time for data curation, preservation, management, quality assurance
- Technical infrastructure (storage, computing, archiving)
- Repository deposit fees
- Anonymisation/pseudonymisation processing
- Making data FAIR (formatting, metadata, documentation)
- Data security measures

### 7.2 Publication costs

| Cost type | Eligible? |
|---|---|
| APCs for **fully OA journals** | Yes |
| APCs for **hybrid journals** | **No** |
| Open Research Europe platform | Free (no APC) |
| Repository deposit fees | Yes |
| Post-project publication fees | No |

---

## 8. Open Science in Proposal Evaluation

### 8.1 Where it appears

| Proposal section | Content |
|---|---|
| **Part A** | Up to 5 outputs per key researcher (OA publications, FAIR datasets with DOIs) |
| **Part B, 1.2: Methodology (Excellence)** | OS subsection (~1 page): mandatory + recommended practices. RDM subsection (~1 page): FAIR across six dimensions |
| **Part B, 2.2: Impact** | Dissemination/exploitation aligned with OS practices |
| **Part B, 3.1: Work Plan** | DMP deliverables at months 6, mid-project, end. RDM activities + costs |
| **Part B, 3.2: Capacity** | Consortium track record in open science |

### 8.2 Evaluation criteria

**Excellence:** Quality of OS practices; how mandatory practices are addressed; appropriateness of recommended practices; justification when practices do not apply; data management quality.

**Quality and efficiency of implementation:** Consortium OS expertise and track record; publication significance assessed **qualitatively** (not by impact factor).

**Tie-breaking:** Excellence first, then Impact.

### 8.3 Tips

- Be specific: name the repository, the license, the timeline
- Justify opt-outs with precision
- Address recommended practices even if not all are relevant
- Demonstrate awareness and intentionality

---

## 9. Special Provisions for Sensitive Data

### 9.1 GDPR and personal data

Projects must comply with **GDPR (EU) 2016/679**: lawful basis, records of processing, DPIAs for high-risk processing, informed consent documentation, data minimisation.

### 9.2 Special categories

Enhanced protections for: racial/ethnic origin, political opinions, religious beliefs, trade union membership, genetic/biometric/health data, sex life/sexual orientation. Requires explicit consent or specific GDPR Art. 9 legal basis.

### 9.3 Balancing openness and protection

Open science requirements **do not override** GDPR. The framework requires:
- **Anonymisation** before public release where possible
- **Access restrictions** for data that cannot be anonymised
- **Controlled access** via repositories with authentication
- **Metadata-only deposit** when data cannot be shared (metadata still open)

GDPR compliance is an explicitly recognised **legitimate ground** for the "as closed as necessary" principle.

### 9.4 Relevance for CMI

Development studies research frequently involves interviews, surveys, and fieldwork with potentially vulnerable populations. The "as closed as necessary" principle explicitly supports keeping such data restricted. Document the reasoning thoroughly in the DMP.

---

## 10. Open Research Europe Platform

[Open Research Europe (ORE)](https://open-research-europe.ec.europa.eu/) is the EC's dedicated OA publishing platform for Horizon 2020/Europe beneficiaries:
- **Free to publish** (no APCs)
- **Free to read** (full OA)
- **CC BY** for publications, **CC0** for data
- **Open peer review** -- transparent, named reviews published alongside articles
- **Automatic compliance** with Horizon Europe OA requirements
- Platform contract extended to at least 2026

ORE is a publishing venue, **not a repository** -- still deposit in a trusted repository for preservation.

---

## 11. Recent Changes: 2026-2027 Work Programme

Published 12 December 2025. Key developments:

**EOSC expansion:** Federation of national/thematic nodes; uptake of FAIR practices; AI-readiness; trusted frameworks for data sharing.

**Administrative changes:** 35% fewer topics (larger calls); more two-stage and blind evaluations; lump sum funding for ~50% of budget; new horizontal calls (EUR 540M Clean Industrial Deal, EUR 90M "AI in Science").

**Open science infrastructure:** Non-profit OA institutional publishing support; FAIR skills training; machine actionability in EOSC.

**Core obligations unchanged:** Article 17 and Annex 5 requirements remain the same.

---

## 12. Norwegian Context

**Norway** was among the first Horizon Europe associated countries (September 2021) -- same conditions as EU Member States.

| Service | Relevance |
|---|---|
| **Sikt Research Data Archive** | CoreTrustSeal-certified; social science data; CESSDA member; meets "trusted repository" requirement |
| **NVA** | National research archive for publications |
| **TSD** | Sensitive data processing/storage |
| **Sikt personverntjenester** | GDPR compliance, DPIAs |

The Research Council of Norway requires full and immediate OA (Plan S-aligned), so obligations overlap substantially with Horizon Europe.

**Practical notes for CMI:** Sikt is the natural first-choice repository for social science data. Budget data management costs explicitly. Document GDPR basis for fieldwork data. Use the "as closed as necessary" provisions with metadata deposited openly.

---

## Key Reference Documents

**Primary legal sources:**
- [Model Grant Agreement (MGA), Art. 17 + Annex 5](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/agr-contr/unit-mga_he_v1.1_en.pdf)
- Annotated Grant Agreement (AGA) -- updated April 2025, via [EU Funding & Tenders Portal](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/home)
- [Horizon Europe DMP Template (DOCX)](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/temp-form/report/data-management-plan_he_en.docx)

**Compliance guidance:**
- [OpenAIRE: Comply with HE mandate for RDM](https://www.openaire.eu/how-to-comply-with-horizon-europe-mandate-for-rdm)
- [OpenAIRE: Comply with HE mandate for publications](https://www.openaire.eu/how-to-comply-with-horizon-europe-mandate-for-publications)
- [OpenAIRE: Open Science in HE proposal](https://www.openaire.eu/open-science-in-horizon-europe-proposal)
- [REA: Open Science overview](https://rea.ec.europa.eu/open-science_en)
- [Open Science in HE (Zenodo)](https://zenodo.org/communities/eu/pages/open-science)
- [Open Research Europe](https://open-research-europe.ec.europa.eu/)
- [re3data.org](https://www.re3data.org/) -- find repositories
- [FAIRsharing.org](https://fairsharing.org/) -- standards and policies

**Norwegian resources:**
- [Sikt Research Data Archive](https://sikt.no/en/archiving-research-data)
- [Sikt on re3data](https://www.re3data.org/repository/r3d100010493)

**Additional guidance:**
- [UCD LibGuide: HE Open Science](https://libguides.ucd.ie/openaccess/horizoneurope)
- [FFG: OA and RDM in HE](https://www.ffg.at/en/europe/heu/legal-financial/open-access)
- [Enspire: DMP in HE](https://enspire.science/data-management-plan-in-horizon-europe/)
- [Enspire: OA Guide](https://enspire.science/guide-to-open-access-in-horizon-europe/)
- [openscience.eu: OS in HE](https://openscience.eu/Open-Science-in-Horizon-Europe)
- [EC Ethics and Data Protection Guidance (PDF)](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/guidance/ethics-and-data-protection_he_en.pdf)
- [OECD: HE Open Science & MGA](https://www.oecd.org/en/publications/access-to-public-research-data-toolkit_a12e8998-en/horizon-europe-open-science-requirements-model-grant-agreement_c0bb3832-en.html)
