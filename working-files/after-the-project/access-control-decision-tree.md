---
icon: lucide/git-fork
title: "Access control decision tree"
description: "A practical guide for choosing the right access level for your research data."
tags:
  - Data classification
  - Security
notes: ""
date_updated: 2026-03-24
---

# Access control decision tree

*A practical guide for choosing the right access level for your research data*

Not all data can — or should — be open. And not all data needs to be locked away. The challenge is landing on the right level: open enough to satisfy funders and support transparency, restricted enough to protect participants and partners.

This guide walks you through four access levels and helps you decide which one fits your data. It works for both quantitative datasets and qualitative materials (transcripts, field notes, audio, coded data).

---

## The four access levels

| Level | What it means | Typical use |
|---|---|---|
| **Open** | Anyone can download and use the data, no approval needed | Anonymised survey data, publicly available documents, aggregated statistics, code |
| **Embargoed** | Data will become open, but not yet — a time lock applies | Data tied to ongoing publications, PhD theses, or phased releases |
| **Restricted** | Available on request, subject to conditions | De-identified interview data, sensitive survey data, data covered by partner agreements |
| **Closed** | Not available externally — only metadata is shared | Identifiable recordings, politically sensitive materials, data where consent doesn't cover sharing |

Most CMI research data lands somewhere between restricted and closed. That's not a failure of openness — it reflects the realities of working with people in sensitive contexts.

---

## The decision tree

Work through these questions in order. Each answer narrows the options until you reach the right access level.

### Step 1 — Can the data identify anyone?

Does the dataset contain direct identifiers (names, voice, images, GPS coordinates of homes) or indirect identifiers that could be combined to identify someone (small village + age + occupation + topic)?

- **No** → The data is effectively anonymous. Move to [Step 4](#step-4-do-funder-or-journal-policies-require-open-access).
- **Yes, but they can be removed** → Consider whether a de-identified version could be shared. If yes, prepare that version and move to [Step 2](#step-2-what-does-your-consent-cover) for the de-identified copy.
- **Yes, and removal would destroy the data's value** → Move to [Step 2](#step-2-what-does-your-consent-cover).

!!! tip "Think combinations, not just names"
    A transcript from a "female district health officer in [small town]" may be identifying even without a name. In small populations or niche professional roles, indirect identifiers are enough. The Finnish Social Science Data Archive and the UK Data Service both provide practical guidance on assessing re-identification risk.

---

### Step 2 — What does your consent cover?

Go back to your informed consent form (or oral consent protocol). What did participants agree to?

- **Consent explicitly allows data sharing and archiving** → Move to [Step 3](#step-3-could-sharing-cause-harm).
- **Consent allows sharing in restricted/controlled form** → Access level is **restricted** at most. Move to [Step 3](#step-3-could-sharing-cause-harm).
- **Consent says nothing about sharing or archiving** → Access level is **closed**. You can still share metadata (a description of the data without the data itself). See [what to do with closed data](#what-to-do-with-closed-data).
- **Consent explicitly prohibits further sharing** → Access level is **closed**.

!!! warning "Consent is a ceiling, not a floor"
    Even if consent allows sharing, other factors (harm, legal restrictions, partner agreements) may still limit access. Consent opens the door — the next steps determine how far.

---

### Step 3 — Could sharing cause harm?

This is especially relevant for CMI's research contexts: conflict zones, authoritarian settings, marginalised communities, corruption investigations.

Consider:

- Could the data put participants at risk — even in de-identified form?
- Could it be used against communities, institutions, or political actors in ways you didn't intend?
- Could it compromise ongoing relationships with partners, gatekeepers, or authorities?
- Does the political or security situation in the research context make any disclosure risky?

If the answer to any of these is **yes**:

- Access level is **restricted** (with strong safeguards) or **closed**
- Document your reasoning — funders and ethics boards will accept justified restrictions

If **no harm is foreseeable** → Move to [Step 4](#step-4-do-funder-or-journal-policies-require-open-access).

---

### Step 4 — Do funder or journal policies require open access?

Many funders (the Research Council of Norway, EU Horizon programmes, NORAD, DFID/FCDO) have open data policies. Most follow the principle: **"as open as possible, as closed as necessary."**

- **Funder requires open access and no restrictions apply** → Access level is **open**.
- **Funder requires open access but restrictions are justified** → Use **restricted** access and document the justification. Most funders accept this — they want transparency, not recklessness.
- **Funder requires a time-limited hold** (e.g., embargo until publication) → Access level is **embargoed**.
- **No funder requirement** → Choose the most open level that the preceding steps allow.

---

### Step 5 — Are there partner or institutional agreements?

Check your partnership MoUs, consortium agreements, and data sharing agreements.

- Does a partner institution retain control over access decisions?
- Did you agree that data stays in-country or is jointly governed?
- Are there restrictions on third-party access?

If partner agreements limit sharing → honour them. The access level cannot be more open than what was agreed. If agreements are silent on access, discuss it with partners before making a unilateral decision.

---

### Step 6 — Are there legal constraints?

- **GDPR**: Personal data of EU/EEA residents (and data processed by Norwegian institutions) is subject to GDPR. Sharing personal data requires a legal basis.
- **Local laws**: Some countries require that research data remains in-country or that government approval is needed for sharing.
- **Contractual obligations**: Some data sources (administrative data, registry data) come with access restrictions built into the data use agreement.

If legal constraints apply → the access level cannot exceed what the law allows.

---

## Quick-reference flowchart

```
Can the data identify anyone?
│
├── No ──────────────────────────────────────────┐
│                                                 │
├── Yes, but removable ── prepare de-identified   │
│   version and continue ─────────────────────┐   │
│                                             │   │
└── Yes, inseparable ─┐                      │   │
                       │                      │   │
            What does consent cover?          │   │
            │                                 │   │
            ├── Allows sharing ───────────┐   │   │
            ├── Allows restricted ──┐     │   │   │
            ├── Silent ── CLOSED    │     │   │   │
            └── Prohibits ── CLOSED │     │   │   │
                                    │     │   │   │
                        Could sharing cause harm?
                                    │     │   │   │
                        ├── Yes ── RESTRICTED │   │
                        │    or CLOSED        │   │
                        │                     │   │
                        └── No ───────────────┘   │
                                    │             │
                        Funder requires open access?
                                    │
                        ├── Yes, no restrictions ── OPEN
                        ├── Yes, but justified ── RESTRICTED
                        ├── Embargo required ── EMBARGOED
                        └── No requirement ── most open
                              level allowed by above
```

---

## What each level looks like in practice

### Open access

- Data deposited in a public repository (Zenodo, DataverseNO, Figshare)
- Anyone can download without approval
- Assign a licence — **CC0** (public domain) or **CC BY 4.0** (attribution required) are the most common
- Include a README, codebook, and enough documentation for someone to understand and reuse the data

**Works for**: anonymised survey data, aggregated statistics, publicly available policy documents, replication code, codebooks.

### Embargoed access

- Data deposited in a repository but access is locked until a specified date
- After the embargo lifts, data becomes open (or restricted, depending on your setup)
- Set a clear end date and make sure someone is responsible for reviewing it

**Works for**: data supporting a forthcoming publication, PhD data before thesis defence, data from phased multi-site projects.

**Typical embargo periods**: 6–24 months after project end or publication.

### Restricted access

- Metadata is public (so people know the data exists and what it contains)
- Data is available only to approved applicants who meet defined conditions
- You (or the repository) review each request and grant or deny access

Set up an access protocol that defines:

- Who can apply (researchers only? same discipline? anyone with a justification?)
- What conditions apply (data use agreement, ethics approval, no re-identification attempts)
- How to apply (email, repository request form, institutional process)
- Who decides (PI, data steward, joint decision with partners)
- Response time (aim for a decision within 2–4 weeks)

**Works for**: de-identified interview transcripts, sensitive survey microdata, data covered by partner agreements, data from vulnerable populations.

### Closed access

- Metadata is public — a description of the data, how it was collected, and why it can't be shared
- The data itself is not available externally
- Store data securely with clear retention and deletion timelines

**Works for**: identifiable recordings, data where consent doesn't cover sharing, politically dangerous materials, data governed by strict legal agreements.

---

## What to do with closed data

Closed doesn't mean invisible. Even when data can't be shared, you should:

1. **Deposit metadata** in a repository — describe the dataset, its scope, methods, and the reason access is closed
2. **Provide a contact point** so other researchers can inquire about potential access
3. **Write a data availability statement** in your publications explaining the restriction
4. **Set a review date** — access decisions aren't permanent. Circumstances change (political situations stabilise, embargoes lift, retention periods end)

---

## Access control worksheet

Use this when preparing a dataset for deposit or archiving. Fill it out for each dataset in your project.

| Question | Your answer |
|---|---|
| Dataset name | |
| Contains personal/identifiable data? | Yes / No |
| Can identifiers be removed? | Yes / No / N/A |
| What does consent allow? | Open sharing / Restricted / Silent / Prohibits |
| Could sharing cause harm? | Yes / No — explain: |
| Funder open-access requirement? | Yes / No — which funder: |
| Partner agreement restrictions? | Yes / No — specify: |
| Legal constraints? | GDPR / Local law / Contract / None |
| **Chosen access level** | **Open / Embargoed / Restricted / Closed** |
| Justification | |
| Review date | |

Keep a copy of this worksheet in your project's `admin/` folder and reference it in your Data Management Plan.

---

## Common patterns at CMI

Based on CMI's research profile, here are access levels that commonly apply:

| Data type | Typical access level | Why |
|---|---|---|
| Anonymised household survey data | Open or embargoed | Low re-identification risk once cleaned; funders often require openness |
| Interview transcripts (de-identified) | Restricted | Rich qualitative data has re-identification risk; consent often limits sharing |
| Audio/video recordings | Closed | Voice and face are direct identifiers; rarely shareable |
| Field notes | Restricted or closed | May contain identifying details, reflexive observations, or sensitive context |
| Administrative/registry data | Restricted or closed | Usually governed by data use agreements with strict access terms |
| Coded qualitative data (NVivo exports) | Restricted | Useful for secondary analysis but may carry re-identification risk |
| Analysis code and scripts | Open | No personal data; supports reproducibility |
| Codebooks and data dictionaries | Open | Documentation supports reuse; contains no personal data |

---

## References

Finnish Social Science Data Archive. (n.d.). *Anonymisation and Personal Data*. [https://www.fsd.tuni.fi/aineistonhallinta/en/anonymisation-and-identifiers.html](https://www.fsd.tuni.fi/aineistonhallinta/en/anonymisation-and-identifiers.html)

Research Council of Norway. (2017). *Policy for Open Access to Research Data*. [https://www.forskningsradet.no/en/research-policy-strategy/open-science/research-data/](https://www.forskningsradet.no/en/research-policy-strategy/open-science/research-data/)

UK Data Service. (n.d.). *Access Control*. [https://ukdataservice.ac.uk/learning-hub/research-data-management/data-access/](https://ukdataservice.ac.uk/learning-hub/research-data-management/data-access/)

European Commission. (2021). *Horizon Europe Programme Guide — Open Science*. [https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/guidance/programme-guide_horizon_en.pdf](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/guidance/programme-guide_horizon_en.pdf)

Qualitative Data Repository. (n.d.). *Sharing Qualitative Data*. Syracuse University. [https://qdr.syr.edu/](https://qdr.syr.edu/)
