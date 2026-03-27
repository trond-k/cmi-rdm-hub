---
icon: lucide/diamond
tags:
  - FAIR data
  - Open Science
  - Data sharing
---

# The FAIR Principles at CMI
*A practical guide to making research data Findable, Accessible, Interoperable, and Reusable*

The FAIR principles[^1] provide a framework for managing research data so that it can be discovered, understood, and reused — by both humans and machines. They are not the same as "open data." Data can be fully FAIR while access remains controlled or restricted. What matters is that data is *described* clearly, *stored* in the right places, *structured* in standard ways, and *documented* well enough for others to evaluate and reuse it.

This guide explains each FAIR principle, what it means in practice for CMI researchers, and what CMI provides to support it. Where relevant, it also addresses the tensions between FAIR and the realities of social science research in sensitive contexts — a tension CMI takes seriously.

!!! info "FAIR and CARE"
    CMI's [RDM and Sharing Policy](../../institutional/policies/rdm-and-sharing-policy.md) commits to both **FAIR** and **CARE** (Collective benefit, Authority to control, Responsibility, Ethics). For research involving Indigenous peoples or marginalised communities — common in CMI's Global South partnerships — CARE principles may shape *how* FAIR is implemented, particularly around who controls access and who benefits from data reuse. See the [Open Science](open-science.md) page for more on balancing openness with ethical responsibilities.

---

## Findable

The first step to reuse is discovery. If no one can find your data, nothing else matters — not the format, not the license, not the documentation. Findability requires persistent identifiers, rich metadata, and deposit in searchable repositories.

### F1. Data and metadata are assigned globally unique and persistent identifiers

**What this means:** Every dataset should have a stable, permanent identifier — typically a DOI (Digital Object Identifier) — that will resolve to the same resource regardless of where it is stored or how URLs change over time.

**What CMI researchers should do:**

- **Deposit data in a repository that assigns DOIs.** Zenodo, openICPSR, QDR, and Sikt's research data archive all assign DOIs automatically on deposit. OSF assigns DOIs or ARK identifiers.
- **Use your ORCID.** An ORCID iD is a persistent identifier for *you* as a researcher. It links your datasets to your publications and other outputs. Register at [orcid.org](https://orcid.org) if you haven't already.
- **Don't rely on project websites or personal pages.** URLs break. A dataset hosted on a personal page or institutional server without a DOI will become unfindable when the page moves, the server is decommissioned, or the project ends.

**What CMI provides:** The [repository defaults](../../institutional/open-science.md#repository-defaults) in CMI's open science guidance recommend repositories that assign persistent identifiers. The DMP Generator prompts you to specify where data will be deposited.

!!! note "Metadata-only records count"
    Even when data cannot be shared — because of participant safety, legal constraints, or partner agreements — a metadata-only record with a DOI makes the *existence* of the data findable. Someone studying the same topic can discover that relevant data was collected and contact the PI to discuss access. This is one of CMI's core positions: **metadata is always open**, even when data is not.

### F2. Data are described with rich metadata

**What this means:** A DOI alone is not enough. The dataset must be described with enough detail that someone can evaluate whether it is relevant to their needs without downloading it. "Rich" means going beyond a title and author — it means describing the content, methodology, geographic and temporal coverage, variables, and access conditions.

**What CMI researchers should do:**

- **Create a README file** for every dataset. At minimum, it should cover: what was collected, when and where, by whom, using what methods, what the variables or data elements are, and any known limitations.
- **Fill in repository metadata fields completely.** When depositing in Zenodo, openICPSR, QDR, or Sikt, fill in all available metadata fields — not just the required ones. Subject keywords, geographic coverage, temporal coverage, and methodology descriptions all improve discoverability.
- **Use keywords consistently.** Use established subject terms from your discipline where possible (e.g., JEL codes for economics, CESSDA vocabulary for social sciences). If the repository supports controlled vocabularies, use them.
- **Write a meaningful description.** "Survey data from Tanzania" is not rich metadata. "Household survey of 1,200 rural households in three districts of Mwanza Region, Tanzania, covering agricultural practices, food security, and livelihood strategies, conducted March–May 2024" is.

**What CMI provides:** CMI's [documentation standards](../../institutional/policies/rdm-and-sharing-policy.md#45-documentation-and-metadata) require minimum documentation including a README, data dictionaries or codebooks, collection methods, processing steps, and known limitations. The DMP Generator produces a data management plan that already captures much of this metadata during project planning.

### F3. Metadata clearly and explicitly include the identifier of the data they describe

**What this means:** The metadata record must contain the DOI (or other persistent identifier) of the dataset it describes, creating an unambiguous link between the description and the data itself. This is a machine-readability requirement — it ensures that automated systems can connect metadata to data.

**What CMI researchers should do:**

- **This is handled automatically by repositories.** When you deposit data in Zenodo, openICPSR, QDR, or Sikt, the repository links the metadata record to the dataset and includes the identifier in structured metadata fields. No manual action required.
- **When creating metadata-only records** (for data that cannot be shared), include the internal identifier or reference number for the dataset so it can be traced institutionally.

### F4. Data and metadata are registered or indexed in a searchable resource

**What this means:** Metadata must be available in systems that people (and machines) actually search. A dataset sitting on a local hard drive with a README file is documented but not findable.

**What CMI researchers should do:**

- **Deposit in an established repository.** All the [CMI-recommended repositories](../../institutional/open-science.md#repository-defaults) are indexed by services like DataCite, Google Dataset Search, OpenAIRE, and BASE. Depositing there makes your data discoverable through these search engines automatically.
- **Deposit internally at CMI as a baseline.** CMI's policy requires all projects to deposit data (or metadata) in the CMI internal repository, ensuring institutional discoverability regardless of external deposit.
- **Link datasets to publications.** When publishing, include the dataset DOI in the article's data availability statement. This creates a two-way link: readers of the paper can find the data, and users browsing the repository can find the paper.

---

## Accessible

Accessible does not mean open. It means that once someone finds your data (through its metadata), there is a clear, standardised way to obtain it — or to understand why they cannot. This is where CMI's "open as possible, closed as necessary" principle intersects directly with FAIR.

### A1. Data and metadata are retrievable by their identifier using a standardised communication protocol

**What this means:** When someone has a DOI or URL for your dataset, they should be able to retrieve it (or its metadata) using standard web protocols (HTTPS). The dataset should not require specialised software, proprietary networks, or personal connections to access.

**What CMI researchers should do:**

- **Use established repositories.** Zenodo, OSF, openICPSR, QDR, and Sikt all serve data over HTTPS and support standard APIs. This requirement is met automatically when you deposit in these repositories.
- **Avoid sharing data only through email or personal file transfers.** Even for controlled-access data, the *request process* should be documented and accessible via a standard URL — not dependent on knowing the right person to email.

### A1.1. The protocol is open, free, and universally implementable

**What this means:** The technical infrastructure for accessing the data should not require paid software, proprietary protocols, or vendor-specific tools. HTTPS and standard repository APIs meet this requirement. This is about the *protocol*, not the data — even restricted data should be accessible through open protocols.

**What CMI provides:** All recommended repositories use open protocols. No action required beyond using approved repositories.

### A1.2. The protocol allows for authentication and authorisation where necessary

**What this means:** For data that cannot be openly shared, the access mechanism must support controlled access — login systems, access request workflows, data use agreements. FAIR explicitly accommodates restricted data. The key is that the *process* for requesting access is clear and standardised.

**What CMI researchers should do:**

- **Choose the right sharing pathway.** CMI defines [five sharing pathways](../../institutional/open-science.md#the-five-pathways) — from open access to no external sharing. For controlled or restricted access, use repositories that support mediated access:
    - **QDR** provides expert-curated mediated access for qualitative data, including disclosure risk evaluation — the strongest option for sensitive interview and ethnographic data.
    - **Sikt's research data archive** provides mediated access for quantitative survey data, where applicants must apply and be approved.
    - **Zenodo** supports restricted access with embargo periods.
    - **openICPSR** supports restricted access with data use agreements for quantitative social science data.
- **Document the access conditions clearly.** In the metadata record, state exactly what is required to gain access: Who can apply? What conditions must they meet? What agreement must they sign? How long does the process take? Who should they contact?
- **Respond to access requests.** If you restrict access, you take on the responsibility of responding to legitimate requests. Factor this into your post-project planning.

!!! tip "Restricted access is still FAIR"
    A qualitative dataset deposited in QDR with a metadata-only public record, a documented access request process, and a data use agreement is fully FAIR — even though no one can download it freely. The same applies to survey data in Sikt's archive or a restricted dataset on Zenodo. What would *not* be FAIR is having no public record of the data's existence, no documented way to request access, and no standardised infrastructure for delivering it.

### A2. Metadata are accessible, even when the data are no longer available

**What this means:** Metadata should persist even if the data itself is deleted, embargoed, or withdrawn. The record of what was collected, by whom, and under what conditions has lasting scholarly value — it informs future research design, prevents duplication of effort, and provides evidence of research activity.

**What CMI researchers should do:**

- **Use repositories with long-term preservation commitments.** Zenodo (CERN-backed), Sikt, and QDR all commit to preserving metadata indefinitely, even if data is removed.
- **Create metadata-only records for deleted data.** When data must be destroyed (as required by GDPR storage limitation or participant agreements), create a metadata-only record in a repository documenting what was collected, why it was deleted, and who to contact for more information. CMI's [open science guidance](../../institutional/open-science.md) makes this an institutional expectation.
- **Include deletion rationale.** When data is removed from a repository, the metadata record should explain why (e.g., "personal data deleted per GDPR storage limitation after 10-year retention period" or "data destroyed per participant agreement").

---

## Interoperable

Interoperability means that data can be combined with other data and work with standard tools, applications, and workflows. This is about formats, standards, and documentation — not about whether the data is open.

### I1. Data and metadata use a formal, accessible, shared, and broadly applicable language for knowledge representation

**What this means:** Data should be in formats that are widely understood, well-documented, and not dependent on proprietary software to read. Metadata should use standard schemas that machines can parse.

**What CMI researchers should do:**

- **Use open or widely-supported file formats.** Prefer formats that do not require specific commercial software:

    | Data type | Preferred formats | Avoid |
    |---|---|---|
    | Tabular data | CSV, TSV, or open spreadsheet formats (ODS) | Excel-only formats (.xlsx with macros, .xlsb) |
    | Statistical data | CSV with codebook; Stata .dta or R .rds with documentation | SPSS .sav without documentation |
    | Text | Plain text (.txt), Markdown, PDF/A | Word-only without plain text alternative |
    | Qualitative coding | Open export formats from NVivo, Atlas.ti, MAXQDA | Project files only (no export) |
    | Geospatial | GeoJSON, GeoPackage, Shapefile | Proprietary GIS formats |
    | Audio/video | WAV, MP4 (H.264), MP3 | Proprietary codecs |
    | Images | TIFF (archival), PNG, JPEG | RAW formats without conversion |

- **Export data alongside project files.** If your analysis is in Stata or R, save the final dataset as CSV as well. If your qualitative coding is in NVivo, export a structured summary alongside the project file. The analysis software may not be available to future users.
- **Use UTF-8 encoding** for all text-based files. This ensures correct handling of non-Latin characters — relevant for CMI's multilingual research contexts.

### I2. Data and metadata use vocabularies that follow FAIR principles

**What this means:** When describing your data, use established controlled vocabularies and classification systems rather than ad hoc terminology. This enables data from different projects to be compared and combined.

**What CMI researchers should do:**

- **Use standard subject classifications.** When depositing data, use controlled vocabulary terms for subject area (e.g., CESSDA Topic Classification for social sciences, JEL codes for economics, OECD Fields of Research).
- **Use ISO standards for geographic and temporal references.** Use ISO 3166 country codes, ISO 639 language codes, and ISO 8601 date formats (YYYY-MM-DD). Say "TZA" or "Tanzania, United Republic of," not "TZ" or "Tanz."
- **Document your own variables clearly.** For variables unique to your project, the codebook serves as the vocabulary. Each variable should have a name, label, description, value labels, and units of measurement.

### I3. Data and metadata include qualified references to other data and metadata

**What this means:** Data should link to related resources — the publications it underpins, the datasets it builds on, the codebooks that define it, and the projects that produced it. "Qualified" means the relationship type is stated (e.g., "is supplement to," "is derived from," "is documented by").

**What CMI researchers should do:**

- **Link datasets to publications.** In your repository metadata, use the "related works" or "related publications" field to link to the journal article, report, or working paper. Specify the relationship (e.g., "is supplement to").
- **Link derived datasets to source data.** If your dataset is derived from another (e.g., you merged two existing survey rounds), reference the source datasets by their DOIs.
- **Link to codebooks and documentation.** If your codebook or README is deposited as a separate item (common in Zenodo), link the two records.
- **Reference external data sources.** If your analysis uses third-party data (e.g., World Bank indicators, DHS surveys), cite them with proper identifiers in your metadata and documentation.

---

## Reusable

The ultimate goal of FAIR: data that is documented, licensed, and described well enough that someone else can evaluate whether it is useful for their purpose and, if so, use it correctly. This is where research data management pays off.

### R1. Data and metadata are richly described with a plurality of accurate and relevant attributes

**What this means:** Beyond basic metadata (title, author, date), data should be described with enough detail to evaluate fitness for purpose: methodology, sampling, geographic and temporal scope, processing steps, known biases, and limitations. This overlaps with F2 but emphasises depth over discoverability.

**What CMI researchers should do:**

- **Create comprehensive documentation.** CMI's policy requires[^2]:
    - **README file:** Purpose, scope, methodology, data collection context, funding, contact information
    - **Codebook or data dictionary:** Variable names, labels, descriptions, value labels, units, missing value codes
    - **Methods documentation:** Sampling strategy, data collection instruments, quality assurance procedures, processing steps
    - **Known limitations:** Response rates, missing data patterns, geographic or temporal gaps, known biases
- **Describe the research context.** For CMI research, context is often essential for correct interpretation. A survey conducted during an election period, in a conflict-affected area, or immediately after a policy change should note these circumstances — they affect how the data should be interpreted and reused.
- **Document data processing.** If you cleaned, recoded, or transformed data, describe what you did and why. Ideally, provide the code or scripts that performed the transformation (see R1.3).

### R1.1. Data and metadata are released with a clear and accessible data usage license

**What this means:** Without a license, potential reusers cannot know what they are legally permitted to do with the data. "No license" does not mean "free to use" — it means "no one knows, so no one uses it."

**What CMI researchers should do:**

- **Apply a standard license.** CMI's [open science guidance](../../institutional/open-science.md#licensing) recommends:
    - **CC0** (preferred) for openly shared datasets — places data in the public domain with no restrictions
    - **CC BY 4.0** when attribution is required
    - **Data use agreements** for controlled or restricted access — specifying permitted uses, security requirements, attribution, and prohibitions on re-identification
    - **MIT, BSD, or Apache 2.0** for code and scripts
- **Do not use Creative Commons licences with ND (NoDerivatives) or NC (NonCommercial) clauses for data.** These restrict reuse in ways that undermine the purpose of sharing and are generally inappropriate for research data.
- **State the licence explicitly** in the metadata record and in the README file.

!!! warning "No licence = no reuse"
    If you deposit data without specifying a licence, most researchers and institutions will not use it — they cannot determine whether they are legally allowed to. Always choose a licence, even if it is restrictive. A data use agreement that says "available for non-commercial academic research with PI approval" is better than silence.

### R1.2. Data and metadata are associated with detailed provenance

**What this means:** Provenance describes where data came from, how it was collected, and what happened to it. It answers the question: "Can I trust this data for my purposes?" Provenance includes who collected it, when, under what conditions, with what instruments, and how it was processed.

**What CMI researchers should do:**

- **Document the data collection process.** When, where, and how was data collected? What instruments were used (survey tools, interview guides, observation protocols)? Who collected it (CMI researchers, local research assistants, contracted firms)?
- **Document data cleaning and transformation.** What steps were taken to clean, validate, or transform raw data? Were outliers removed? Were variables recoded? Were datasets merged?
- **Preserve data collection instruments.** Archive the survey questionnaire, interview guide, or observation protocol alongside the data. Without the instrument, the data may be misinterpreted.
- **Note version history.** If the dataset was updated or corrected after initial deposit, use versioning in the repository and document what changed.

### R1.3. Data and metadata meet domain-relevant community standards

**What this means:** Different disciplines have established standards for how data should be structured, documented, and described. Following these standards makes data interoperable within your research community and signals that it meets quality expectations.

**What CMI researchers should do:**

- **Follow discipline-specific standards where they exist:**
    - **Survey data:** Use DDI (Data Documentation Initiative) metadata standard. Sikt's archive and many social science repositories support DDI.
    - **Qualitative data:** Use QuDEx (Qualitative Data Exchange Format) or document according to CESSDA guidelines for qualitative data.
    - **Economics/development:** Follow AEA Data Editor requirements for replication packages. Include code, data, and a master script that reproduces results.
    - **Mixed methods:** Document both quantitative and qualitative components according to their respective standards.
- **Provide analysis code.** Where feasible, share the Stata do-files, R scripts, or Python notebooks used for analysis. This is the strongest form of methodological transparency and the most effective support for replication.
- **Use standard file structures.** A common convention for replication packages:

    ```
    project-name/
    ├── README.md              # Overview, instructions, requirements
    ├── data/
    │   ├── raw/               # Unmodified source data
    │   └── processed/         # Cleaned, analysis-ready data
    ├── code/
    │   ├── 01_clean.do        # Data cleaning scripts
    │   ├── 02_analysis.do     # Analysis scripts
    │   └── 03_figures.do      # Visualization scripts
    ├── output/
    │   ├── tables/            # Result tables
    │   └── figures/           # Figures and charts
    └── docs/
        ├── codebook.pdf       # Variable documentation
        └── questionnaire.pdf  # Data collection instrument
    ```

---

## Implementing FAIR at CMI: a summary

The table below maps each FAIR principle to CMI's current practices, institutional supports, and typical actions for researchers.

| Principle | What CMI provides | What researchers should do |
|---|---|---|
| **F1** Persistent identifiers | Recommended repositories assign DOIs | Deposit in DOI-issuing repository; use ORCID |
| **F2** Rich metadata | DMP Generator; documentation standards | Complete all metadata fields; write meaningful descriptions |
| **F3** Identifier in metadata | Automatic in recommended repositories | No manual action needed |
| **F4** Searchable index | Recommended repositories indexed by DataCite, Google Dataset Search | Deposit in established repository; link datasets to publications |
| **A1** Standardised retrieval | Repositories use HTTPS and standard APIs | Use established repositories; avoid email-only sharing |
| **A1.1** Open protocol | Met by all recommended repositories | No additional action |
| **A1.2** Authentication support | QDR, Sikt, Zenodo, openICPSR support mediated access | Choose appropriate sharing pathway; document access conditions |
| **A2** Persistent metadata | Repositories preserve metadata long-term | Create metadata-only records when data is deleted |
| **I1** Standard formats | Format guidance in this guide | Use open file formats; export alongside proprietary formats |
| **I2** Standard vocabularies | Repository metadata schemas | Use controlled vocabularies for subjects, geography, time |
| **I3** Qualified references | Repository "related works" fields | Link datasets to publications, source data, and documentation |
| **R1** Rich description | Documentation standards; DMP template | Create README, codebook, methods documentation |
| **R1.1** Clear licence | Licensing guidance in open science policy | Apply CC0, CC BY, or data use agreement |
| **R1.2** Provenance | DMP captures collection and processing plans | Document collection, cleaning, transformation, versioning |
| **R1.3** Community standards | Discipline-specific guidance | Follow DDI, AEA, or relevant community standards; share code |

---

## Common questions

??? question "Our data is too sensitive to share. Does FAIR still apply?"
    Yes. FAIR does not require open access. A dataset that is clearly described (rich metadata), deposited in a repository with a controlled access mechanism (QDR for qualitative data, Sikt for survey data, openICPSR or Zenodo for other data), documented with a codebook and README, and licensed under a data use agreement is fully FAIR — even if only three researchers ever access it. What is *not* FAIR is having no record that the data exists, no way to request access, and no documentation of what it contains.

??? question "We're doing qualitative research. How can interview transcripts be FAIR?"
    Focus on the principles you can implement. You may not be able to share full transcripts openly, but you can: create a metadata-only record with a DOI (F1, F4), describe the data richly — number of interviews, topics, geographic and temporal scope, languages (F2, R1), document your methodology and analytical approach (R1.2), specify access conditions — even if the answer is "contact the PI" (A1.2), and archive the data securely with proper documentation for potential future controlled access (R1.1). For sensitive qualitative data, QDR provides expert curation and mediated access specifically designed for this kind of material (per-deposit fees apply). A well-documented, findable, restricted-access dataset is more FAIR than an undocumented open dataset.

??? question "What about the CARE principles?"
    FAIR and CARE are complementary, not competing. FAIR addresses how data should be *managed*. CARE addresses who should *benefit* and who should *decide*. For CMI research with Global South partners, CARE may mean: discussing data governance with partners during project design, not after collection; giving partner institutions authority over access decisions for data they helped produce; ensuring data reuse benefits the communities studied, not just external researchers; and respecting local norms about data ownership and knowledge sharing. In practice, this often means adding CARE-informed conditions to the access and licensing decisions that FAIR requires you to make explicit.

??? question "Our funder doesn't require FAIR compliance. Should we still bother?"
    CMI's [RDM and Sharing Policy](../../institutional/policies/rdm-and-sharing-policy.md) commits to FAIR as an institutional principle, regardless of individual funder requirements. But beyond policy compliance: well-documented, findable data is easier to manage within your own team during the project, easier to hand off to colleagues, and more likely to generate citations and collaboration opportunities after the project ends. FAIR is not just about external reuse — it is good research practice.

---

## Further reading

- CMI [Open Science](../../institutional/open-science.md) — CMI's positions on data sharing, repositories, and licensing
- CMI [Data Security](../../institutional/data-security.md) — storage infrastructure and security by classification tier
- CMI [Data Classification](../../institutional/data-classification.md) — the four-tier classification scheme
- CMI [Sharing and Archiving](../../institutional/sharing-and-archiving.md) — anonymisation and repository selection guidance

[^1]: Wilkinson, M., Dumontier, M., Aalbersberg, I. et al. "The FAIR Guiding Principles for scientific data management and stewardship." *Sci Data* 3, 160018 (2016). [https://doi.org/10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18)

[^2]: CMI Research Data Management and Sharing Policy, section 4.5: Documentation and metadata.

*[FAIR]: Findable, Accessible, Interoperable, Reusable
*[CARE]: Collective benefit, Authority to control, Responsibility, Ethics
*[DOI]: Digital Object Identifier
*[ORCID]: Open Researcher and Contributor ID
*[DDI]: Data Documentation Initiative
*[DMP]: Data Management Plan
*[GDPR]: General Data Protection Regulation
*[APC]: Article Processing Charge
*[CSV]: Comma-Separated Values
*[TSV]: Tab-Separated Values
*[DPA]: Data Processing Agreement
*[CESSDA]: Consortium of European Social Science Data Archives
*[AEA]: American Economic Association
*[QDR]: Qualitative Data Repository
*[ICPSR]: Inter-university Consortium for Political and Social Research
*[OSF]: Open Science Framework
