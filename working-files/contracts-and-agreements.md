---
icon: lucide/handshake
title: "Partnerships and agreements"
description: "Data management agreements for research partnerships: joint controllership, data processing, data sharing, and cross-border transfers."
tags:
  - Contracts
  - GDPR
notes: "Stub — content pending"
date_updated: 2026-03-24
---

# Partnerships and Agreements

<!-- Data management agreements for research partnerships: joint controllership,
     data processing agreements, data sharing agreements, research assistant
     arrangements, cross-border transfers, and cloud service agreements.
     Practical guidance on which agreement type applies when, and what each covers. -->

*Trond Kvamme · 9 min read*

## Why agreements belong in the planning stage

Data management agreements need to be in place before personal data moves between institutions. For CMI, where nearly every project involves international partners, this is a planning-stage concern, not an afterthought. But these agreements are not just compliance documents — they define who has authority over the data, who is responsible for participant protection, and what happens when the project ends.

There are only a few types of agreement, and which one you need follows from the nature of the relationship. A genuine research collaboration is different from a contracted data collection, which is different from a data-sharing arrangement with a government ministry. The type of relationship determines the type of agreement. This page walks through each one.

The [partnerships and data transfer](../../institutional/partnerships.md) module provides the institutional detail for all partnership types. The [GDPR demystifier](gdpr-demystifier.md) explains the regulatory framework for cross-border transfers.

---

## Joint controllership: when you share authority

The typical CMI international research collaboration involves partners who co-determine research purposes and methods — they co-design the research, independently collect data, and conduct analysis. Under GDPR, that makes them **joint controllers**, regardless of what the partnership agreement is called.

CMI's preferred mechanism for genuine research partnerships is the joint controllership agreement (Article 26). This is not the same as Standard Contractual Clauses, which are designed for commercial data transfers where one party instructs the other. A joint controllership agreement acknowledges shared authority and distributes responsibilities accordingly — it reflects the collaborative reality of the partnership rather than imposing an artificial hierarchy.

**What it covers:** Which institution handles data subject rights requests (typically each handles requests from its own participants). How participants are informed about the joint controllership (covered in the information letter). Data handling and security procedures at each institution. Retention and deletion obligations. What happens to the data if the partnership ends.

**When it applies:** A partner university independently collects data as part of the project. Both institutions co-designed the research and share decision-making over the data. These are the hallmarks of joint controllership — shared determination of purposes and means.

**When it does not apply:** You have a contracted data collection firm acting on your instructions (that is a processor, not a controller — see below). A partner provides existing data but does not co-determine your research. An individual research assistant works under your direct instruction.

**Practical note:** Draft the agreement during project setup, before data collection begins. The agreement should be signed by authorised representatives of both institutions. Template agreements are under development — contact the RDM Adviser.

---

## Data processing agreements: when someone acts on your behalf

When a service provider processes personal data on CMI's instructions — collecting, storing, or transforming data according to specifications you define — a Data Processing Agreement (DPA) under Article 28 is required. This is one of the few CMI scenarios where the controller-processor framing genuinely fits.

The primary scenario at CMI: **contracted data collection firms**. When CMI contracts a firm like EconInsight to run a survey using their own enumerators and devices, CMI determines the research purpose and the data requirements; the firm determines the logistics of collection. That is a processor relationship.

**What the DPA covers:** What data the firm will collect, from whom, using what methods. That the firm processes data only on CMI's documented instructions. Security obligations — encryption on all enumerator devices, secure transmission, physical security during fieldwork. Confidentiality obligations for all staff with data access. Data return and deletion — after delivery to CMI, the firm deletes all copies and confirms in writing. Breach notification.

**The SurveyCTO account question.** When a firm uses its own SurveyCTO account, data sits on the firm's account on SurveyCTO's servers. CMI should have a named admin or viewer role, or receive data exports on an agreed schedule. After confirmed delivery, the firm should delete the project data from its account. Consider whether a CMI-controlled account with the firm's enumerators granted access would simplify the chain.

The DPA framework also applies to external transcription services, translation services, or any third-party cloud tool that processes personal data on CMI's behalf. Before using any such service, ensure a DPA is in place and the service meets the requirements in the [cloud services and tool assessment](../../institutional/tools-and-services.md) guidance.

---

## Data sharing agreements: when a partner provides or receives data

When a non-research partner — an NGO, government ministry, or international organisation — provides administrative data to your project or receives research findings for operational purposes, a data sharing agreement is appropriate. These partners are typically not co-determining research purposes, so joint controllership does not apply.

**What it covers:** What data is shared, in which direction, for what purpose. Restrictions on use, publication, or further sharing. Security and handling requirements at the receiving institution. Retention and deletion obligations. Whether the partner has expectations about how results involving their data are reported (particularly relevant for government partners, where quality assessments or performance data may carry political sensitivity).

**Lead times matter.** Government ministries and NGO partners often have internal approval processes for data sharing that take weeks or months. A ministry that informally agrees to share administrative records may need formal sign-off from a legal department, a data protection officer, and sometimes a political appointee. Budget time for this in the project setup phase — and start the conversation early.

---

## Research assistants: authority, not contract

Local research assistants collecting data on CMI's behalf are not processors — they act under CMI's instruction as part of the controller's operations. No DPA or Standard Contractual Clauses are needed. What is needed is simpler but must be explicit:

**A confidentiality clause** in the employment or consultancy contract. **Clear written data handling instructions** covering what to collect, how to store it, when and how to transfer it to CMI-controlled storage, and what to delete afterwards. **Device encryption** on every device that touches research data — CMI-provided devices are preferable, but if personal devices are used, encryption must be enabled. **A briefing** that verifies the assistant understands the procedures, not just that they received a document.

The [partnerships](../../institutional/partnerships.md) and [fieldwork](../../institutional/fieldwork.md) modules detail the full requirements.

---

## Cross-border data transfers

CMI takes a proportional approach to cross-border transfers, matching the legal mechanism to the actual data flow and risk rather than applying the heaviest machinery to every situation.

**For genuine research collaborations with non-EEA partners:** the joint controllership agreement itself provides the contractual safeguards for the transfer. The agreement documents the shared authority, the data handling procedures at each institution, and the responsibilities for participant protection.

**For researchers doing fieldwork:** the data never leaves the researcher's control. Practical safeguards — device encryption, secure upload, minimal data on devices — are proportionate. Standard Contractual Clauses for a researcher carrying an encrypted laptop to Tanzania would be disproportionate.

**The research derogation** (Article 49(1)(d)) covers transfers necessary for scientific research in the public interest. This is a legitimate basis for research data transfers, not a loophole — but it should be used with specificity, documenting why the transfer is necessary for the research.

**Standard Contractual Clauses** are reserved for sustained data-sharing arrangements where other mechanisms are not appropriate — primarily commercial or semi-commercial relationships where the partner processes data under instruction rather than as a collaborator.

!!! warning "Document the legal basis for every non-EEA data transfer"
    For every partner outside the EEA who will access personal data, there should be a documented legal basis — joint controllership agreement, research derogation, SCCs, or adequacy decision. This also appears in the Sikt notification (Section 10), where you need to specify the legal basis for each third-country transfer.

---

## Cloud services: the agreement you might forget

If you use a cloud service to process personal data — a survey platform, a transcription tool, a collaboration app — check that a Data Processing Agreement exists between CMI (or you) and the provider. This is easy to overlook. A researcher who signs up for a transcription service and uploads interview recordings has created a data processing relationship that needs a legal foundation.

The [cloud services and tool assessment](../../institutional/tools-and-services.md) guidance provides a checklist: data residency, DPA, training data policy (critical for AI tools), encryption, access controls, subprocessors. Classification-based rules apply: enterprise tools with DPA for Red-tier data, no external cloud tools for Black-tier data.

---

## When to prepare

During project setup, before data collection begins. Joint controllership agreements, government data sharing approvals, and data processing agreements with survey firms all require negotiation and institutional sign-off. Have agreements signed before sharing any personal data.

??? tip "Template agreements are being developed"
    CMI is developing template agreements for the most common partnership arrangements — joint controllership, data processing for contracted firms, and data sharing with institutional partners. Contact the RDM Adviser for the current templates and for guidance on adapting them to your project.
