---
icon: lucide/file-signature
title: "Contracts and agreements"
description: "Choosing the right data protection contracts and partnership agreements in research."
tags:
  - Contracts
  - GDPR
notes: ""
date_updated: 2026-03-24
---

# Contracts and agreements

*A practical guide for choosing the right data protection contracts and partnership agreements in research*

Most CMI projects involve partners, field staff, or service providers in other countries. This guide helps you figure out two things: whether your collaboration needs a formal data protection contract, and if so, which one. It also covers the non-GDPR agreements that matter for research partnerships.

The guide reflects CMI's interpretive position that GDPR must be applied **proportionally** to research. The safeguards appropriate for a technology company processing millions of records are not the same safeguards appropriate for a qualitative study with 30 participants. If you want the full reasoning behind the positions described here, see the [GDPR Interpretive Positions](../institutional-context/gdpr-stance.md) document.

---

## Do you need a data protection contract?

Not every collaboration requires a formal GDPR contract. The determining factor is whether your collaborator acts as an **independent party** with respect to personal data, or whether they work **under CMI's authority**.

### When you probably don't need one

If the person or organisation operates under CMI's direct instruction and does not independently decide why or how personal data is processed, a formal Data Processing Agreement (DPA) is usually unnecessary. They are functioning as part of CMI's operations, not as a separate entity.

This typically applies to:

| Who | Why no DPA | What you need instead |
|---|---|---|
| CMI employees | Covered by employment contract and internal policies | Internal data protection training |
| Affiliated researchers (fellows, visiting researchers, PhD students) | Formally associated with CMI, follow CMI's guidelines | NDA or confidentiality clause; documented scope of authority |
| Short-term consultants or data analysts | Processing data solely under CMI's instructions | NDA or confidentiality clause in their contract; documented tasks and limitations |
| Research assistants (including field-based) | Acting as part of CMI's data collection operation | Clear data handling instructions; confidentiality agreement; encrypted equipment or secure upload |
| Collaborative partners functioning as extensions of CMI | Following CMI's instructions without independent decision-making over data | NDA; documented roles and instructions |

!!! warning "When in doubt, use a DPA"
    The categories above describe typical cases. If a collaborator begins to exercise independent judgement over data processing (deciding what data to collect, how to analyse it, or whom to share it with), the relationship may have shifted toward processor or joint controller. When the boundary is unclear, a DPA provides a more structured legal foundation. Ask your DPO if you're unsure.

### When you do need one

You need a formal data protection contract when an external organisation or individual:

- Processes personal data **on CMI's behalf** but as a separate legal entity (→ DPA)
- **Jointly decides** with CMI on the purposes and methods of data processing (→ Joint Controller Agreement)
- **Receives personal data** that is transferred across borders, particularly outside the EEA (→ Data Transfer Agreement)

Use the [decision tree](#which-contracts-do-you-need-a-decision-tree) below to work through your specific situation.

---

## GDPR roles in 60 seconds

Three roles determine which contract you need. The question is always: **who decides why and how personal data is processed?**

| Role | Who decides? | CMI's typical position |
|---|---|---|
| **Data Controller** | Determines the purposes and means of processing | CMI is the controller when we initiate, lead, or own a project, even if we never touch the data directly |
| **Data Processor** | Processes data on the controller's instructions, with no independent decision-making | External data collection firms (e.g., EconInsight), transcription services, survey platforms (e.g., SurveyCTO) |
| **Joint Controllers** | Two or more parties jointly determine purposes and means | CMI and a partner institution that co-design the research, co-collect data, and jointly decide on analysis (a genuine research collaboration) |

CMI can hold **multiple roles in the same project**. You might be the sole controller for one work package (where CMI independently manages data collection), a joint controller with a partner for another (where you co-design the study), and have a processor relationship with a survey firm for a third.

!!! tip "Joint controllership and equal partnerships"
    CMI's strategy emphasises equal knowledge production with partners in the Global South. When a collaboration genuinely involves shared decision-making over research design and data (which is what equal partnership means in practice), joint controllership is the honest legal description of the relationship. It is also CMI's **preferred contractual approach** for genuine research collaborations, because it avoids imposing a hierarchical controller-processor framing on relationships that are not hierarchical.

---

## Which contract do you need?

### Data Processing Agreement (DPA)

**When to use it:** An external organisation processes personal data on CMI's behalf, following CMI's instructions. The processor does not decide the purpose of the processing or exercise independent judgement over the data.

**Typical CMI scenarios:**

- CMI hires EconInsight (based in Ethiopia) to collect household survey data. EconInsight follows CMI's research design, data collection protocols, and data handling instructions. They don't decide what to collect or how to use it.
- CMI uses SurveyCTO to administer a survey. The platform stores and processes response data on CMI's behalf.
- CMI outsources transcription of recorded interviews to a transcription service.

**What it must cover:** Processing purposes and scope, data handling instructions, security measures, sub-processor approval, breach notification, return or deletion of data at project end, and audit rights.

If the processor is located **outside the EEA**, you may also need Standard Contractual Clauses (SCCs). See [cross-border transfers](#cross-border-data-a-proportional-approach) below.

[CMI DPA template →](<!-- placeholder: link to CMI DPA template -->)

---

### Joint Controller Agreement (JCA)

**When to use it:** Two or more organisations jointly determine the purposes and means of processing personal data. Both parties shape the research: they co-design the study, co-decide on data collection methods, and share analytical responsibility.

**Why CMI prefers this for genuine collaborations:** A JCA reflects the reality of equal research partnerships better than a DPA. It distributes responsibilities without imposing a hierarchy. It is also lighter-weight than the controller-processor framework with SCCs, which was designed for commercial outsourcing, not academic collaboration.

**Typical CMI scenarios:**

- CMI partners with a university in Ghana to study public health challenges. Both institutions jointly decide on data collection methods and each has access to the data for analysis. Neither party simply follows the other's instructions.
- CMI, UiB, and NUPI collaborate on a study of renewable energy impacts. All three institutions contribute equally to research design, participant recruitment, and analysis.
- A multi-country consortium where CMI and partner institutions in India, Kenya, and Brazil co-develop research methodologies and share analytical responsibility.

**What it must cover:** Each party's responsibilities for GDPR compliance, who handles data subject requests (access, rectification, erasure), who manages breach notification, how data is shared between parties, security measures, and a contact point for data subjects.

**Key nuance on cross-border transfers:** The Norwegian Data Protection Authority (Datatilsynet) has indicated that in a joint controllership arrangement, where a non-EEA partner independently collects data and later shares findings with the EEA partner, this may not trigger GDPR's transfer provisions, provided no further data transfer (such as remote access) takes place. This can simplify compliance for genuinely collaborative projects. However, if CMI later accesses or receives the data, transfer safeguards may still be required. Define data flows clearly in the JCA.

[CMI JCA template →](<!-- placeholder: link to CMI JCA template -->)

---

### Data Transfer Agreement (DTA) and Standard Contractual Clauses (SCCs)

**When to use it:** Personal data is transferred outside the EEA to a country without an [EU adequacy decision](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en), and the transfer involves a separate legal entity (not someone acting under CMI's authority).

**What SCCs are:** Pre-approved contractual clauses issued by the European Commission that provide legal safeguards for cross-border personal data transfers. They are often incorporated into DPAs or DTAs rather than used as standalone contracts.

**When you might NOT need SCCs:** see the [cross-border section](#cross-border-data-a-proportional-approach) below. Not every data movement across a border is a "transfer" that requires the full SCC machinery.

**Typical CMI scenarios where SCCs apply:**

- CMI signs a DPA with a data collection firm in Ethiopia. Survey data (containing personal data) will be transmitted from Ethiopia to CMI's systems in Norway. The DPA should incorporate SCCs to cover this transfer.
- A partner institution in a non-EEA country holds a copy of project data under a JCA. If CMI accesses this data remotely or receives a copy, SCCs or equivalent safeguards may be needed alongside the JCA.

[EU Standard Contractual Clauses (official text) →](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/standard-contractual-clauses-scc_en)

[CMI DTA template →](<!-- placeholder: link to CMI DTA template -->)

---

### Non-Disclosure Agreement (NDA) / Confidentiality Agreement

**When to use it:** Sensitive information is shared with someone who is not processing personal data in a GDPR-relevant sense, but who needs access to confidential project details, methodologies, or preliminary findings.

Also the **default safeguard** for people working under CMI's authority who don't need a DPA: affiliated researchers, consultants, research assistants, and collaborative partners functioning as extensions of CMI.

**Typical CMI scenarios:**

- A visiting researcher joins a CMI project and needs access to project documentation, including descriptions of participants and field sites.
- An external adviser reviews a research design that involves sensitive political contexts.
- A short-term consultant analyses de-identified data under CMI's direct instruction.

[CMI NDA/confidentiality template →](<!-- placeholder: link to CMI NDA template -->)

---

### Contract-type summary

| Situation | Contract needed |
|---|---|
| External firm collects or processes data on CMI's instructions | **DPA** (+ SCCs if outside EEA) |
| Partner institution co-designs research and shares data decisions | **JCA** (+ SCCs if data crosses EEA border) |
| Personal data transferred to/from a non-EEA country | **DTA with SCCs** (often built into the DPA or JCA) |
| Collaborator needs access to confidential project info but isn't processing personal data | **NDA / Confidentiality Agreement** |
| Affiliate, RA, or consultant working under CMI's direct authority | **NDA + documented instructions** (no DPA needed) |
| Cloud service processes data on CMI's behalf | **Vendor DPA** (usually provided by the service) |

---

## Cross-border data: a proportional approach

CMI routinely collects and processes data outside the EEA. Under a strict reading of GDPR Chapter V, every instance of personal data existing outside the EEA constitutes a "transfer" requiring legal safeguards. CMI's position is that the safeguard should match the actual data flow and risk, not default to the heaviest available mechanism.

### Four common scenarios

| Scenario | What's happening | Appropriate safeguard |
|---|---|---|
| **CMI researcher abroad** | A CMI researcher conducts interviews in Tanzania on an encrypted device, uploads data to CMI storage in Norway | **Practical safeguards only.** Device encryption, secure upload, password protection. No SCC needed. The data never leaves CMI's control. |
| **Local research assistant** | An RA based in a partner country collects data under CMI's instruction, using CMI-provided or approved equipment | **Instructions + NDA.** The RA acts as part of CMI's operations. Clear data handling instructions, encrypted devices or immediate secure upload, confidentiality agreement. |
| **Partner institution with own data copy** | A partner university in Ethiopia holds project data, conducts independent analysis as part of a genuine collaboration | **JCA** (preferred) or **DPA + SCCs.** This is a genuine transfer to a separate legal entity. A JCA is appropriate if the partnership involves shared decision-making. If the partner acts only on CMI's instructions, use a DPA with SCCs. |
| **Cloud service** | CMI uses a survey platform, transcription tool, or AI tool that processes data on servers outside the EEA | **Vendor DPA.** Most established services (SurveyCTO, Microsoft 365, etc.) provide their own DPAs. Prefer services offering EEA-based or Swiss-based processing where available. |

!!! tip "Distinguish data sharing from data transfer"
    Datatilsynet distinguishes between data collected by a non-EEA controller (and subsequently shared with CMI) versus data transferred by CMI to a non-EEA processor. If a non-EEA partner independently collects data as a joint controller and does not act on CMI's behalf, the initial collection may not constitute a GDPR-regulated transfer. But for CMI to later access that data, transfer safeguards may still apply. Define roles and data flows from the outset. See [Datatilsynet's guidance on transfers](https://www.datatilsynet.no/en/).

---

## Beyond GDPR: other agreements you may need

GDPR contracts address data protection. But research collaborations involve more than data protection. They involve questions of ownership, credit, access, and what happens when the project ends. These are not GDPR questions, but they need to be settled in writing, and they matter just as much.

### Data ownership

Who owns the data? This is rarely straightforward in collaborative research, and GDPR doesn't answer it.

Consider:

- Does ownership sit with the collecting institution, the coordinating institution, or is it shared?
- Does the answer differ for raw data versus analysed or processed data?
- Do individual researchers retain any rights?

In CMI's context, the equal-partnership philosophy means ownership should be **negotiated, not assumed**. A model where CMI automatically retains full ownership of all data collected by partners in the Global South contradicts the partnership principles, even if it's legally defensible.

**Proportionality applies here too.** A small pilot study with a trusted long-term partner may not need a formal data ownership agreement. A clear paragraph in the project MoU may suffice. A large multi-country consortium with multiple institutions and funders probably does.

!!! tip "Put it in writing before data collection starts"
    Data ownership is easiest to negotiate when no one has results to protect yet. Include data provisions in your partnership MoU or consortium agreement at the outset. See also [Partner agreements](../before/partner-agreements.md).

### Publication and authorship

If the collaboration will produce joint publications, agree early on:

- Who has the right to publish from the data?
- How will authorship be determined?
- Do partners have a right to review or comment before publication?
- Can partners use the data for their own independent publications or follow-up studies?

These questions are especially important in North-South collaborations where publication access and credit have historically been unequal.

### Memoranda of Understanding (MoUs) with data provisions

Many CMI collaborations begin with an MoU that covers the broad terms of the partnership. Make sure the MoU addresses data, even briefly. Key provisions:

- Where shared data will be stored
- How data will be transferred between institutions
- What security standards apply
- Who decides on archiving, sharing, or deletion after the project
- What happens to copies held by partners when the project ends

An MoU with clear data provisions can reduce the need for separate, more formal agreements later, especially for collaborations that don't involve large-scale personal data processing.

### Data use agreements (for data CMI receives)

When CMI obtains data from external sources (registry data from a government agency, administrative data from a tax authority, existing datasets from another research institution), the **source** typically sets the access terms. These may include:

- Restrictions on who can access the data within CMI
- Prohibitions on sharing with third parties
- Requirements to delete data after a defined period
- Restrictions on linking with other datasets

Honour these agreements. They are contractual obligations, and violating them can jeopardise CMI's access to data sources for future projects.

---

## Which contracts do you need? A decision tree

Work through these steps in order. Each answer narrows the options until you reach a concrete recommendation.

### Step 1: Does the project involve personal data?

Personal data means any information that can identify a living person, directly (name, voice, photo) or indirectly (small village + age + occupation). If your project collects, stores, or analyses such data, GDPR applies.

- **No** → You don't need GDPR contracts (DPA, JCA, DTA). Skip to [Step 5](#step-5-beyond-gdpr-what-else-do-you-need).
- **Yes** → Continue to Step 2.

---

### Step 2: Who handles the personal data?

Think about every person or organisation involved in collecting, storing, or analysing personal data in your project. Are they all working under CMI's direct authority, or is a separate organisation involved?

- **Only CMI staff, affiliates, or people under CMI's instruction** (employees, fellows, research assistants, short-term consultants) → No DPA or JCA needed. Use **NDAs + documented instructions** for non-employees. Skip to [Step 4](#step-4-does-data-cross-the-eea-border).
- **An external organisation is involved** (partner institution, data collection firm, transcription service, survey platform) → Continue to Step 3.

---

### Step 3: What is the external organisation's role?

This is the key question. It determines the type of contract.

**Does the external organisation follow CMI's instructions without independent decision-making over the data?**
For example: a data collection firm that conducts surveys using CMI's questionnaire, following CMI's protocols, and returns the data to CMI.

→ They are a **processor**. You need a **Data Processing Agreement (DPA)**. Continue to [Step 4](#step-4-does-data-cross-the-eea-border).

**Does the external organisation co-determine the research design and data use?**
For example: a partner university that jointly designs the study, decides on data collection methods, and independently analyses the data.

→ They are a **joint controller**. You need a **Joint Controller Agreement (JCA)**. Continue to [Step 4](#step-4-does-data-cross-the-eea-border).

!!! tip "Not sure?"
    Ask: if CMI disappeared tomorrow, would the partner continue the research using this data for their own purposes? If yes, they're likely a joint controller. If they'd stop because they were only acting on CMI's behalf, they're likely a processor. When the boundary is genuinely unclear, a DPA is the safer default. Ask your DPO if unsure.

---

### Step 4: Does data cross the EEA border?

Is personal data transferred to or from a country outside the European Economic Area, either to a partner, a service provider, or CMI's own systems?

- **No** → You have your GDPR contracts. Skip to [Step 5](#step-5-beyond-gdpr-what-else-do-you-need).
- **Yes, but the data never leaves CMI's control** (e.g., a CMI researcher with an encrypted laptop abroad) → Practical safeguards only (encryption, secure upload). No SCCs needed. Skip to [Step 5](#step-5-beyond-gdpr-what-else-do-you-need).
- **Yes, to a separate organisation in a country with an [EU adequacy decision](https://commission.europa.eu/law/law-topic/data-protection/international-dimension-data-protection/adequacy-decisions_en)** → No additional transfer safeguards needed. Skip to [Step 5](#step-5-beyond-gdpr-what-else-do-you-need).
- **Yes, to a separate organisation in a country without an adequacy decision** → Add **Standard Contractual Clauses (SCCs)**, incorporated into your DPA or JCA, or via a standalone Data Transfer Agreement (DTA). Continue to [Step 5](#step-5-beyond-gdpr-what-else-do-you-need).

---

### Step 5: Beyond GDPR: what else do you need?

These apply whether or not personal data is involved.

- **Partners involved in the project?** → Agree on **data ownership** and **publication rights**. Include data provisions in your MoU or consortium agreement. See [Beyond GDPR](#beyond-gdpr-other-agreements-you-may-need) above.
- **Confidential information shared with people not processing personal data?** → Use an **NDA or confidentiality agreement**.
- **CMI receiving data from an external source** (registry data, administrative data)? → Check whether a **data use agreement** governs access terms.

---

### Quick-reference flowchart

```
Does the project involve personal data?
│
├── No ──────────────────────────────────── Skip to: partnership
│                                            agreements, data ownership,
│                                            NDA if confidential info
│                                            is shared
│
└── Yes
    │
    Does an external org handle personal data?
    │
    ├── No (only CMI staff/affiliates) ──── NDA + documented instructions
    │                                        for non-employees.
    │                                        Check cross-border (Step 4).
    │
    └── Yes
        │
        What is their role?
        │
        ├── Processor (follows ──── DPA
        │   CMI's instructions)      │
        │                             │
        └── Joint controller ──── JCA
            (co-determines             │
            research & data)           │
                                       │
                    Does data cross the EEA border
                    to a country without adequacy?
                                       │
                            ├── No ──── Done (GDPR contracts complete)
                            │
                            └── Yes ── Add SCCs
                                        (in DPA, JCA, or standalone DTA)
```

---

## Information to research participants

Every research project involving human participants must provide clear information about the project, the data collected, and participants' rights. This is handled through the **information letter**, the foundation of informed, voluntary participation.

The information letter is covered in detail in [Ethics and consent](../before/ethics-and-consent.md) and in CMI's [GDPR Interpretive Positions](../institutional-context/gdpr-stance.md#consent-ethical-practice-not-lawful-basis). The key point for contracts: the information letter is **not** a GDPR consent form. CMI's default lawful basis is public interest, not consent. Participants are informed and choose freely to take part, but their participation is not contingent on signing a consent form.

[CMI information letter template →](<!-- placeholder: link to information letter template -->)

---

## Contacts

If you are unsure which contract is appropriate for your project:

- **Data Protection Officer**: [dpo@cmi.no](mailto:dpo@cmi.no)
- **Research Data Management**: [trond.kvamme@cmi.no](mailto:trond.kvamme@cmi.no)
