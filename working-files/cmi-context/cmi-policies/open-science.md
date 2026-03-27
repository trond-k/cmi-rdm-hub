---
version: "1.0"
date: 2026-03-11
notes:
  - Draft — should be reviewed with CMI research leadership and the REC.
  - Several repositories in the "Other" list are US-based (openICPSR, Harvard
    Dataverse, QDR, OSF/Zenodo hosted by US orgs). Given political shifts,
    consider prioritising European-based services where possible.
  - DataverseNO for CMI?
  - Consider creating an archive selector as a separate tool or manual.
---

# Open Science — CMI

<!-- WHAT CMI's positions are on open science, open access, data sharing, repositories,
     and how openness interacts with sensitive research contexts.

     This is the single authoritative source for repository defaults.


     For retention and deletion, see retention.md.
     For GDPR positions on data sharing, see gdpr-positions.md. -->

This document describes CMI's positions on open science, open access to publications, and research data sharing. These are institutional defaults. Individual projects may need to deviate, and the reasoning for deviation should be documented.


## CMI's position on open science

CMI is committed to open science as a means to strengthen research quality, transparency, and societal impact. The governing principle is **"open as possible, closed as necessary"** — openness is the default, but restrictions are required where legal, ethical, security, or contextual risks make sharing unsafe or unlawful.

This is not a compliance slogan. It means that the burden of justification falls on restriction, not on openness. A researcher who wants to share data openly does not need to justify doing so. A researcher who restricts access does need to document why — and the justification must be proportionate to the actual risk, not hypothetical worst cases.

### Principles

1. **Do no harm.** Openness must not expose participants, communities, partners, or staff to foreseeable harm. For CMI's research — often in politically sensitive, conflict-affected, or governance-critical contexts — this is not a theoretical concern.

2. **FAIR by default.** Research data should be as Findable, Accessible under defined conditions, Interoperable where appropriate, and Reusable. FAIR does not mean open — controlled-access data with good metadata is FAIR. Undocumented data dumped into a repository is not.

3. **CARE where relevant.** For research involving Indigenous peoples or marginalised communities, the CARE principles (Collective benefit, Authority to control, Responsibility, Ethics) should guide decisions about data authority, benefit, and access. This is particularly relevant for CMI's partnerships in the Global South, where data governance should be developed with partners and reflect local norms and power dynamics.

4. **Metadata is always open.** Even where data access is restricted, metadata describing the data — what was collected, when, by whom, under what conditions — should be publicly available. The only exception is when metadata itself creates risk (e.g., revealing that interviews were conducted with opposition figures in a specific country).

5. **Risk-based openness.** Projects must assess sensitivity, partner obligations, and contextual risks early and throughout the research lifecycle. Openness is not a one-time decision at project end — it is a design consideration from the start.


## Open access to publications

CMI is a **Green Open Access institution**. This means CMI complies with open access requirements through self-archiving (depositing versions of publications in CMI's institutional repository), not by paying for Gold OA publication.

### Core requirements

- **Mandatory deposit.** All written research outputs — journal articles, book chapters, reports, briefs, working papers — must be registered in the Norwegian Research Information Repository (NVA) and deposited in the institutional repository (cmi.no).
- **Best available version.** Deposit the best version the publisher permits: publisher PDF (preferred), author accepted manuscript (post-print), or pre-print.
- **Embargoes.** If the publisher requires an embargo period before open access, the embargo end date must be recorded at deposit. The deposit itself happens immediately; access opens when the embargo expires.
- **Rights retention.** Authors should use an author addendum when needed to retain the right to self-archive. Check publisher policies via Sherpa/Romeo and prefer journals covered by Norwegian Open Access agreements (Openscience.no).
- **Repository completeness.** The institutional repository is the authoritative archive for CMI research outputs. All outputs should be deposited there, not only those required by funders.

### Registration in the Norwegian Research Information Repository (NVA)

All research output from CMI must be registered in [NVA](https://nva.sikt.no/) (Nasjonalt vitenarkiv), the national platform operated by Sikt for registering, archiving, and making research outputs openly discoverable. NVA replaced the former Cristin system and institutional Brage repositories, combining research information registration with open-access repository functions in a single service.

- **What to register.** All scholarly publications (journal articles, monographs, book chapters, reports, working papers), as well as research datasets, projects, and other research activities. Peer-reviewed full-text versions should be uploaded where publisher agreements allow.
- **Why it matters.** Registration in NVA is required for publications to be reported to the Norwegian Scientific Index (NVI). NVI reporting is the basis for result-based budget redistribution across the health, institute, and higher education sectors — including the institute sector where CMI sits. Publications that are not registered in NVA cannot be counted toward CMI's reported research output.
- **NVI eligibility.** To qualify for NVI reporting, a publication must present new insight, be peer-reviewed before publication in an approved channel (Level 1 or 2 in the Norwegian Register), and be published for the first time. Revised editions, translations, and reprints do not qualify.
- **Reporting deadlines.** NVI reporting is annual. The typical deadline for registering publications from the previous year is 31 January, with the final NVI reporting deadline in early April. CMI's library or research administration coordinates the reporting process.
- **Open access via NVA.** When a peer-reviewed full text is uploaded to NVA, it is made openly available through the national repository (subject to any publisher embargo). This complements CMI's Green OA approach — depositing in NVA can satisfy both the national registration requirement and the open access obligation in a single step.

### Article processing charges (APCs)

CMI does not normally pay APCs because Green OA through self-archiving satisfies funder requirements. Exceptions are possible when all of the following apply:

- The journal is fully open access (not hybrid)
- The journal is Level 1 or 2 in the Norwegian Register
- The corresponding author is affiliated with CMI
- The Research Director approves the request

For books and book chapters, open access fees should be budgeted in funding applications (e.g., Research Council of Norway projects) when relevant.


## Data sharing expectations

### The five pathways

Projects must select the most open sharing pathway compatible with legal, ethical, and security requirements, and document the choice in the DMP:

1. **Open access** — data publicly available under an open license (CC0 or CC BY preferred). The target for de-identified quantitative data, codebooks, methodology documentation, and replication packages.

2. **Registered access** — data available to authenticated users who accept standard terms. Appropriate for data that is not sensitive but where tracking use is desirable.

3. **Controlled access** — data shared with approved applicants under specific conditions (data use agreements). Appropriate for de-identified data with residual re-identification risk, or data where partner agreements require tracking.

4. **Restricted access** — data shared only under strict agreements or in secure environments. Appropriate for sensitive data that has ongoing research value but cannot be safely opened.

5. **No external sharing** — data retained internally or securely destroyed; metadata-only record where feasible. Appropriate when sharing is genuinely incompatible with participant safety, legal constraints, or partner requirements.

### Default expectations

- **Quantitative data** underlying publications should be shared at the most open level feasible — ideally open access with a replication package.
- **Qualitative data** (interview transcripts, field notes, ethnographic material) is more complex. Full transcripts are rarely shareable given the re-identification risk inherent in rich qualitative data, particularly from CMI's small-population, sensitive-context research. The realistic sharing pathway is usually controlled access to selected de-identified excerpts, or metadata-only records with contact information for access requests.
- **Administrative and compliance data** (consent records, contact lists, project administration) is not shared.
- **Metadata is always shared.** Even when data cannot be shared, a metadata record describing the dataset should be publicly discoverable.

### Licensing

- Open datasets: use CC0 (preferred for maximum reuse) or CC BY 4.0.
- Controlled or restricted access: use data use agreements specifying permitted uses, security measures, attribution, and restrictions on re-identification.
- Code and scripts: use permissive open-source licenses (MIT, BSD, Apache 2.0) unless there are specific reasons not to.


## Anonymisation feasibility assessment

**Applies when**: the project intends to share data after completion, and the data contains or contained personal data.

Assess whether meaningful anonymisation is feasible given:

1. **Sample size and specificity**: small samples in specific communities (e.g., "20 interviews with village leaders in Choma District") may be indirectly identifiable even after removing names and direct identifiers. The combination of role, location, and topic may uniquely identify individuals.
2. **Depth of qualitative data**: rich interview transcripts may contain enough contextual detail to identify participants even without names — descriptions of personal experiences, family situations, workplace details.
3. **Geographic granularity**: village-level or facility-level data in small communities carries higher re-identification risk than district or national-level data.
4. **Public profile of participants**: interviews with officials, leaders, or public figures may be identifiable regardless of anonymisation efforts.

**If anonymisation is feasible**: plan for it in the project design. Budget time for anonymisation work. Document the anonymisation approach in the DMP.

**If anonymisation is not feasible**: the data cannot be shared openly. Consider:
- **Mediated-access sharing** through a repository that supports controlled access — Sikt's archive (for survey and qualitative data) or other repositories with mediated access, where secondary researchers must apply for access
- **Sharing aggregate or summary data** rather than individual-level data
- **Metadata-only records** so the dataset is discoverable even if the data is not accessible

**Action for the researcher**: assess anonymisation feasibility during project planning (preliminary) and again after data collection (definitive). Document the assessment and decision in the DMP.


## Repository defaults

This is the single authoritative repository list for CMI. Other modules reference this section rather than maintaining their own lists.

### Primary repositories

These are CMI's default options. Most projects will use one or more of these.

| Repository | Best for | Access model | Cost | Notes |
|---|---|---|---|---|
| **CMI internal repository** | All projects (minimum baseline) | Internal | N/A | At minimum, all research data should be deposited internally with appropriate metadata for institutional accountability. This is the mandatory baseline for every project. |
| **Sikt's research data archive** (default for external archiving) | Survey data, quantitative data matrices, register data | Mediated access — secondary researchers apply | Free (state-funded institutions) | Norway's national archive for research data on people and society. Part of CESSDA. Assigns DOIs. Sikt's core strength is quantitative survey and register data, where its curation and access infrastructure is strongest. **Also accepts qualitative data** (interview transcripts, text-based materials), but the researcher must document that participants were informed about archiving for secondary reuse — this should be covered in the information letter (see `consent-and-information.md`). A data processing agreement between CMI and Sikt is required for datasets containing personal data. Most existing CMI qualitative data was collected without archiving disclosed in the information letter and is ineligible retroactively; new projects must address archiving in the information letter from the start. Embargo limited to 3 years after collection or 1 year after deposit. |
| **Zenodo** | Open datasets, code, supplementary materials | Open, embargo, restricted by request | Free | Hosted by CERN. Assigns DOIs. Widely accepted by funders. CMI has an institutional community for branded deposit. Good alternative when Sikt is not suitable (non-survey data, international collaborations, openly downloadable datasets). |
| **OSF** | Replication data, pre-registrations, open research workflows | Open or restricted | Free | Integrates code, data, and manuscripts in a single project. Good for transparency and replication. Assigns DOIs. |

**For publications and research outputs** (as distinct from research data): all output must be registered in NVA (see [Registration in NVA](#registration-in-the-norwegian-research-information-repository-nva) above).

### Other repositories

Use these when the primary repositories are not suitable or when funders, journals, or disciplinary norms require a specific archive.

| Repository | Best for | Access model | Cost | Notes |
|---|---|---|---|---|
| **NIRD (Sigma2)** | Large datasets from funded projects | Open access (default), restricted possible | Free for academically funded Norwegian researchers | Norwegian national infrastructure. Good for large-scale datasets. |
| **EOSC Hub / EUDAT** | EU-funded projects, cross-border research data | Open or restricted | Free for eligible projects | European Open Science Cloud services. Relevant for Horizon Europe projects that require European infrastructure for data sharing and long-term preservation. |
| **openICPSR** | Quantitative social science data, international/comparative datasets | Open, restricted with data use agreements | Free | Strong social science heritage. Open to all researchers worldwide. Assigns DOIs. |
| **Harvard Dataverse** | Replication data for journal publications, quantitative social science data | Open (default), restricted possible | Free | Open to all researchers worldwide. Assigns DOIs. Many political science and economics journals require or recommend Dataverse deposits (AJPS, Political Analysis, QJE, and others). Relevant when a journal mandates Dataverse as the deposit target. Norway has a national instance, [DataverseNO](https://dataverse.no/) (operated by UiT), which offers curated deposit for partner institutions; CMI is not currently a partner (non-partners get up to 10 GB free). |
| **QDR** | Qualitative data — interview transcripts, field notes, ethnographic material | Mediated and restricted access | $500–1,500 per deposit (fee waivers may be available) | The Qualitative Data Repository at Syracuse University. Purpose-built for qualitative social science data. An option when Sikt's qualitative data prerequisites cannot be met but the data has secondary research value. Assigns DOIs. |
| **Discipline-specific archives** | Data with established disciplinary repositories | Varies | Varies | Use when funders or disciplinary norms require a specific archive. |

### Quick decision path

0. **All projects** → Deposit in **CMI's internal repository** (mandatory baseline for every project).
1. **Is the data quantitative survey or register data?** → **Sikt's research data archive** (free, mediated access, DOIs, part of CESSDA). This is CMI's default for external archiving.
2. **Is the data qualitative and was archiving disclosed in the information letter?** → **Sikt** is an option. Otherwise, consider **Zenodo** (free) or other mediated-access repositories.
3. **Is the data openly shareable (de-identified, no restrictions)?** → **Zenodo** (free, open access, DOIs, CMI institutional community).
4. **Is this a replication package (data + code + documentation)?** → **OSF** (links code, data, manuscripts in one project) or **Zenodo**.
5. **Is this an EU-funded project?** → Consider **EOSC Hub / EUDAT** for European infrastructure requirements.
6. **Can the data not be shared externally at all?** → Create a **metadata-only record** in Zenodo or OSF so the dataset is discoverable.

For the full repository list including other options (NIRD, openICPSR, Harvard Dataverse, QDR, discipline-specific archives), see the tables above. Note that several of these are US-based; prefer European-based services where possible.

### Practical guidance

- Choose the repository before data collection starts and document the choice in the DMP.
- Prefer repositories that assign DOIs and guarantee long-term preservation (10+ years).
- If a funder mandates a specific repository, use it.
- **Start with Sikt** as the default for external archiving. For survey and quantitative data, Sikt should be the first choice — it is Norway's national archive, free, assigns DOIs, and provides mediated access. For qualitative data, Sikt is also an option if archiving was disclosed in the information letter; if not, consider Zenodo instead.
- For **quantitative data** that does not fit Sikt (e.g., international collaborations where open download is preferred): Zenodo is available immediately at no cost. openICPSR and Harvard Dataverse are alternatives for comparative social science data or when journals mandate a specific deposit target.
- For **qualitative data**: if archiving was disclosed in the information letter, deposit at Sikt. Zenodo is a free alternative for less sensitive qualitative data that can be openly shared. QDR is a specialised option for sensitive qualitative research but involves per-deposit fees.
- For **replication packages** (data + code + documentation): OSF is well suited because it can link code repositories, datasets, and publications in a single project. Zenodo is also a good option.
- For data that cannot be shared externally, create a **metadata-only record** in a public repository (Zenodo or OSF) so the dataset is discoverable even if the data is not accessible.
- **Plan for Sikt from the start.** If you intend to archive qualitative data at Sikt, include explicit archiving-for-reuse language in your information letter before data collection begins. Retroactively adding archiving disclosure is rarely feasible.

**Minimum requirement**: every completed CMI research project should deposit its data (or a documented subset) in at least the CMI internal data repository, with metadata describing the data, its classification, and any access restrictions.

**Escalation**: if none of the recommended repositories fit the data type or sensitivity level, or if funder requirements conflict with available options, contact the RDM contact (rdm@cmi.no).


## Embargo and retention defaults

- **Default embargo period: 1–2 years** after project completion. Data intended for publication and sharing should be made openly available after this period unless legal or ethical restrictions apply. (Note: Sikt's archive limits embargoes to 3 years after data collection or 1 year after deposit, whichever is shorter. If using Sikt, align the embargo with their requirements.)
- **Default retention period: 10 years** after project completion, in line with Research Council of Norway guidelines and common funder requirements.
- **Personal data retention** follows GDPR storage limitation — retain only as long as necessary for the stated research purpose, then delete or de-identify. See `retention.md` for detailed retention guidance including withdrawal rights, funder requirements, and deletion procedures.
- **Embargo is not restriction.** An embargo delays open access while the research team publishes from the data. It does not justify permanent restriction. If data is still embargoed after the stated period, the PI should either open it or document why restriction is necessary.


## Open science in CMI's sensitive research contexts

The tension between open science norms and CMI's research profile is real and must be navigated honestly. Much of CMI's research involves:

- Politically sensitive topics in authoritarian or semi-authoritarian settings
- Vulnerable populations (refugees, displaced persons, conflict-affected communities)
- Research in contexts where participant identification could cause serious harm
- Partnerships where data governance expectations differ between Norwegian norms and local contexts
- Small populations where even "de-identified" data may be re-identifiable

**The "open as possible, closed as necessary" principle handles this.** The answer is not that CMI research is too sensitive for open science — it is that openness takes different forms depending on the context:

- A corruption study may share methodology, analytical code, and aggregate findings openly, while keeping raw data restricted.
- An interview-based study in a conflict zone may create a metadata-only record so the dataset is discoverable, without making any data accessible.
- A household survey in a stable context may share a fully de-identified dataset openly.

The key requirement is that the researcher documents the reasoning — what is shared, what is restricted, and why — in the DMP and the repository record. "This data is sensitive" is not sufficient justification for permanent restriction. The researcher must specify which data, what the risk is, and whether partial sharing (de-identified subsets, aggregate tables, metadata-only) is feasible.

### CARE principles in practice

For research involving communities in the Global South — which includes most CMI research — data governance is not solely the researcher's decision. Partners and communities may have legitimate expectations about who controls data, who benefits from it, and how it is shared. These expectations should be:

- Discussed during project design, not after data collection
- Reflected in partnership agreements and DMPs
- Respected even when they are more restrictive than Norwegian open science norms would suggest

This is consistent with CMI's strategy emphasis on equal knowledge production and inclusive partnerships.
