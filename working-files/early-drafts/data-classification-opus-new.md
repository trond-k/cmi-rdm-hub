# Data Classification

## Why classify data?

Not all research data carries the same risk. A published dataset and a transcript from an interview with a political dissident require fundamentally different handling. Classification helps you make the right call — quickly and consistently — about how to store, share, and protect the data you work with.

CMI uses four classification levels. Each reflects the potential harm that could result from unauthorised access, disclosure, or loss.

## The four levels at a glance

| Level | Label | Core question | Typical risk if breached |
|---|---|---|---|
| **Open** (Green) | *No label required* | Could this be posted on CMI's website without concern? | Negligible. The data is already public or intended to be. |
| **Restricted** (Yellow) | *Restricted / Internal* | Is this internal working material with no sensitive content? | Minor. Premature release could be inconvenient or professionally awkward, but causes no significant harm. |
| **In Confidence** (Red) | *Confidential / Sensitive* | Could disclosure harm individuals, partners, or CMI? | Serious. Breach could endanger participant safety, violate GDPR, damage trust, or carry legal consequences. |
| **Strictly In Confidence** (Black) | *Strictly Confidential* | Would disclosure cause severe or irreversible harm? | Severe. Risks to life, large-scale privacy violations, major legal liability, or loss of irreplaceable data. |

## How to assess your data

Ask three questions about any dataset, file, or collection you handle:

1. **Confidentiality** — Who is allowed to see this, and what happens if someone else does?
2. **Integrity** — How damaging would it be if this data were altered, corrupted, or lost?
3. **Availability** — How urgently and reliably does this data need to be accessible?

The highest concern among the three determines the classification. A dataset that is low-risk on confidentiality but critical on integrity (e.g., a master codebook for a longitudinal study) should be classified according to the integrity requirement.

## Level-by-level guidance with data examples

### Open (Green)

Data that is public, anonymised beyond re-identification risk, or produced specifically for dissemination.

**Research data examples:**
- Published, fully anonymised survey datasets
- Openly licensed secondary data downloaded from public repositories
- Aggregated statistics prepared for a policy brief or annual report
- Conference presentations and accompanying visualisations
- Anonymised field notes where no contextual details could re-identify participants

**Handling essentials:** No special restrictions. CMI recommends storing work files on Microsoft 365 (Teams, OneDrive, SharePoint) rather than local or private solutions, to benefit from built-in backup and version control.

---

### Restricted (Yellow)

Internal working data that is not sensitive but is not ready or intended for public release. May be shared with specific collaborators under controlled conditions.

**Research data examples:**
- Unpublished working drafts of papers, codebooks, or analysis scripts
- Preliminary or partially cleaned datasets still undergoing quality checks
- Anonymised datasets containing demographic variables (age, gender, region) but no direct identifiers
- Early-stage qualitative coding or thematic summaries derived from anonymised material
- Internal data-sharing logs or project planning documents

**Handling essentials:**
- Store exclusively on CMI's Microsoft 365 environment
- Share externally only through controlled, time-limited access and, where appropriate, under a data-sharing agreement
- Avoid third-party cloud platforms (Dropbox, Google Drive) unless specifically approved by IT
- Encryption is applied automatically in transit and at rest via Microsoft 365

---

### In Confidence (Red)

Data that is sensitive — to individuals, to CMI, or to partners — and where a breach could cause significant harm. This includes most datasets containing personal data.

**Research data examples:**
- Interview transcripts or field notes with identifiable participant information
- Datasets containing special-category personal data (health status, political opinion, ethnicity, religious belief)
- Research data from or about vulnerable populations, even if partially anonymised
- Qualitative material where identification of sources could lead to retaliation (e.g., informants in governance or conflict research)
- Unpublished findings whose premature release could compromise ongoing fieldwork or endanger collaborators
- Signed consent forms linking participant names to study IDs

**Handling essentials:**
- Access strictly on a need-to-know basis; document who has access and why
- Apply Microsoft sensitivity labels ("Confidential" or "Sensitive") to all files
- External sharing only under a signed confidentiality or data-processing agreement, and only via encrypted channels within Microsoft 365
- Two-factor authentication required; all access logged
- Review access permissions periodically and revoke promptly when no longer needed

---

### Strictly In Confidence (Black)

The most sensitive category, assessed case by case. Reserved for data where a breach could cause severe or irreversible harm.

**Research data examples:**
- Large-scale datasets of sensitive personal data (e.g., health records, biometric data, detailed political profiles of individuals in high-risk contexts)
- Research material involving participants in conflict zones or under authoritarian regimes, where disclosure could endanger lives
- Data subject to government-imposed confidentiality or classification restrictions
- Irreplaceable primary data whose loss cannot be recovered (e.g., a unique oral-history archive from a now-inaccessible region)

**Handling essentials:**
- Security and access arrangements evaluated on a case-by-case basis in consultation with the Head of IT and the Research Data Management Adviser
- Access limited to the smallest possible group; all access logged and audited
- Encryption, multi-factor authentication, and additional safeguards (e.g., air-gapped storage) may be required depending on the assessment
- External sharing only under strict legal agreements and with explicit authorisation

---

## A practical decision aid

When you are unsure how to classify a dataset, work through these prompts:

1. **Does the data contain personal information — directly or indirectly identifiable?** If yes, it is at minimum **Restricted (Yellow)**, and likely **In Confidence (Red)** or higher.
2. **Could someone be harmed — physically, professionally, legally, psychologically — if this data were exposed?** If yes, classify as **In Confidence (Red)** at minimum.
3. **Does the data involve vulnerable populations, conflict settings, or legal restrictions?** If yes, consider **Strictly In Confidence (Black)** and consult the Research Data Management Adviser.
4. **Is the data already published or fully anonymised beyond re-identification risk?** If yes, **Open (Green)** is likely appropriate.

When in doubt, classify higher and consult. It is easier to downgrade a classification than to undo a breach.

## Using sensitivity labels

For all data classified as Restricted, In Confidence, or Strictly In Confidence, apply the corresponding Microsoft sensitivity label to every file. Labels enforce encryption, access restrictions, and handling rules automatically. No label is needed for Open data.

| Classification | Sensitivity label to apply |
|---|---|
| Restricted (Yellow) | Restricted *or* Internal |
| In Confidence (Red) | Confidential *or* Sensitive |
| Strictly In Confidence (Black) | Strictly Confidential |

For step-by-step instructions, see the *CMI Guideline for Applying Sensitivity Labels in Microsoft Apps*.

## AI tools and data classification

Before uploading any data to an AI or GPT-based service, check its classification:

- **Open (Green):** Safe to use with AI services.
- **Restricted (Yellow):** May be used cautiously with the GDPR-compliant Sikt GPT, provided the data contains no personal identifiers or confidential content. Do not upload to general-purpose AI tools (e.g., ChatGPT, Google Gemini).
- **In Confidence (Red) and Strictly In Confidence (Black):** Never upload to any AI service.

If you need AI-assisted analysis of sensitive data, contact the Research Data Management Adviser to discuss compliant alternatives.