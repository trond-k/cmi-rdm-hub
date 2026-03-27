---
icon: lucide/shield-check
title: "Data classification at CMI"
description: "How CMI's four-tier classification scheme works and how to apply it to your data."
tags:
  - Data classification
  - Security
notes: ""
date_updated: 2026-03-24
---

# Data classification at CMI

<!-- Manual content for the RDM Hub.
     Located at: /content/manual/cross-cutting/data-classification.md

     Describes the four-tier classification scheme and how to
     apply it. The sensitivity classifier widget can be embedded
     at the end of the "How to classify" section.

     Companion documents:
     - data-security.md (storage infrastructure, access control)
     - tools-and-services.md (tool use by tier)
     - fieldwork.md (fieldwork data handling)

     This page is referenced by the Data Security Policy, the
     Data Flow and Inventory guide, and the sensitivity classifier
     widget itself. Keep it consistent with those documents.

     CMI voice. Prose-forward. No GDPR article numbers in the
     body text — link to the GDPR pages where needed. -->

*Trond Kvamme · 7 min read*

Every data object in a research project — a recording, a transcript, a dataset, a contact list — needs to be stored somewhere, shared with someone, and eventually deleted or preserved. The right decisions depend on how sensitive the data is. CMI uses a four-tier classification scheme to make those decisions consistent and proportionate: security measures should match actual risk, not worst-case imagination.

Classification is per data object, not per project. A single project will typically contain data at different tiers — published background documents at Green, working drafts at Yellow, interview transcripts at Red. The most sensitive object in a project does not set the classification for everything else. Each object is assessed on its own terms.

Classification can change over the life of a data object. Raw interview recordings start at Red or Black. Anonymised transcripts may move to Yellow. A published, de-identified dataset moves to Green. The tier reflects the data's current state, not its origin or its intended destination.


## The four tiers

=== ":green_circle: Green — Open"

    Data that can be freely shared. No personal data, no contractual restrictions, no institutional sensitivity.

    At CMI this includes published datasets and their codebooks, publicly available documents collected for analysis, project metadata, methodology documentation, de-identified aggregate statistics, literature reviews, and published reports.

    Green is the target end-state for much of CMI's research output. During active projects, most data starts at a higher tier and arrives here through anonymisation, aggregation, or publication.

    **Storage:** CMI M365 environment (OneDrive, SharePoint) during active work. Can be published to repositories such as Sikt, OSF, or Zenodo with open Creative Commons licences.

    **Access:** Unrestricted, beyond any contractual or funder terms.

    **Tools:** Any tool can be used without restriction.

=== ":yellow_circle: Yellow — Internal"

    Data not intended for public sharing but where exposure would not cause significant harm. This includes working documents, pre-publication material, institutional records, and — in limited circumstances — personal data that meets the conditions described below.

    At CMI this includes draft manuscripts and working papers, internal project reports, project budgets and administrative records, anonymised working datasets, general project correspondence, meeting notes without sensitive content, and workshop logistics.

    **Storage:** CMI M365 environment with standard access controls. At the end of the project, delete or anonymise any personal data that is no longer needed.

    **Access:** Limited to the project team and relevant CMI staff. Not shared externally without review.

    **Tools:** Enterprise tools within CMI's M365 ecosystem are preferred. General-purpose tools are acceptable for non-sensitive tasks, but internal documents should not be uploaded to consumer AI tools.

    ??? info "Personal data at Yellow"

        Personal data defaults to Red. Yellow is available only when **all three** of the following conditions are met:

        1. The data contains only **limited identifiers** — names, institutional email addresses, professional titles, institutional affiliations. No private contact details unless freely given for logistical purposes.
        2. The research context is **non-sensitive** — a person's participation or association with the project would not cause embarrassment, reputational risk, or harm if it became known.
        3. The individuals are **not in a vulnerable position** — they are not research participants in a sensitive study, not in a dependent relationship with the data controller, and not in a context where being identified could create risk.

        If any of these conditions is not met, the data is Red.

        Yellow classification does not reduce GDPR obligations. Personal data at Yellow still requires a legal basis for processing, must be included in your Sikt notification, and must be deleted or anonymised when no longer needed. The tier affects storage requirements and access controls, not whether privacy rules apply.

=== ":red_circle: Red — Confidential"

    Data containing personal data or sensitive institutional information where exposure could cause harm or distress. This is the default tier for personal data in active research projects at CMI, and the most common classification for research data overall.

    At CMI this includes interview recordings and transcripts, survey datasets with direct or indirect identifiers, signed consent forms, participant contact lists, fieldwork notes with identifiable information, correspondence with research participants, key informant details, data shared under confidentiality agreements, and draft reports containing identifiable participant data.

    This is not an unusual or burdensome classification. CMI's M365 infrastructure is set up to handle Red-tier data as standard.

    **Storage:** CMI M365 environment with restricted access — named project members only. External collaborator access requires explicit arrangement. Additional M365 E5 controls may be appropriate depending on the project: conditional access policies, restricted SharePoint sharing settings, information barriers, or audit logging. Contact [help@cmi.no](mailto:help@cmi.no) (IT Helpdesk) to set these up.

    For projects where the risk profile is elevated — particularly research involving sensitive personal information in politically sensitive contexts, or where US jurisdiction over cloud infrastructure is a specific concern — external high-security services are available. These include TSD/Nettskjema (Norwegian sovereign infrastructure, particularly useful for survey data collection), Tresorit and Proton Drive (Swiss jurisdiction, outside CLOUD Act reach). These involve additional project costs and should be budgeted in the proposal if anticipated. See the Data Security guide for detailed guidance on choosing between these options.

    **Access:** Restricted to named project members approved by the PI.

    At the end of the project, anonymise or delete identifiable data. Anonymised versions may move to Green for archiving and reuse.

    !!! danger "Tool restrictions at Red"

        Do not upload, paste, or input identifiable personal data into general-purpose consumer AI tools (ChatGPT, Claude consumer, Google Translate, or similar). Only enterprise tools with a Data Processing Agreement and a no-training guarantee are acceptable for Red-tier data. This includes transcription and translation services — if you are transcribing recordings containing personal data, the service must have a DPA and must not use uploaded audio for training. See the Cloud Services and Tool Assessment guide for details.

    A Data Protection Impact Assessment (DPIA) may be required for Red-tier data, particularly when the data includes sensitive personal information (health, ethnicity, political opinion), when the research context is politically sensitive, or when the processing is large-scale (hundreds of participants or more). Contact [dpo@cmi.no](mailto:dpo@cmi.no) for DPIA guidance.

=== ":black_circle: Black — Strictly confidential"

    Data where exposure could cause serious harm to participants or others. This applies to a small proportion of CMI data but is disproportionately important to get right.

    At CMI this includes data from research in conflict-affected or authoritarian settings where participants could face arrest, violence, or persecution if identified; sensitive personal information (health, ethnicity, political opinion) collected in high-risk political contexts; and large-scale datasets combining sensitive personal information with contextual risk.

    **Storage:** Determined case-by-case. Options include TSD (Norwegian sovereign infrastructure), air-gapped systems, or encrypted local storage depending on the threat model. M365 may be appropriate with additional controls for some Black-tier data. Contact [help@cmi.no](mailto:help@cmi.no) (IT Helpdesk) for secure storage setup. These solutions involve additional costs — budget for them in the project proposal.

    **Access:** Strictly limited to named individuals with a demonstrated need.

    !!! danger "No external cloud tools for Black-tier data"

        Data remains within the approved secure infrastructure determined for the project. No AI tools, no cloud-based transcription, no external survey platforms unless they are part of the approved infrastructure.

    A DPIA is almost certainly required. Contact [dpo@cmi.no](mailto:dpo@cmi.no) before data collection begins.

    For fieldwork involving Black-tier data, develop explicit data handling protocols: device encryption, transfer procedures, and deletion schedules for field devices. Do not proceed with data collection until storage and handling arrangements have been confirmed.


## How to classify

Classification is the responsibility of the principal investigator. It should happen early — ideally when you build your data inventory at the Frame or Plan stage — and be reviewed when circumstances change.

The key question at each step is not "what type of data is this?" but "what would realistically happen if this data were exposed?" A transcript is not Red because it is a transcript. It is Red because it contains the voice or words of an identifiable person in a context where exposure could cause them harm or distress. An anonymised version of the same transcript, where no individual can be identified, is Green.

Context is decisive. An interview about agricultural practices where the participant is identifiable is Red. The same interview conducted with political activists in an authoritarian state is Black. The data type is identical; the consequences of exposure are not.

!!! tip "When in doubt, classify one tier higher"

    It is easier to relax a classification later than to discover you underestimated the sensitivity of something already in circulation.

<div style="border: 2px solid var(--md-primary-fg-color, #4051b5); border-radius: 12px; padding: 1.5em 2em; margin: 1.5em 0; background: color-mix(in srgb, var(--md-primary-fg-color, #4051b5) 6%, var(--md-default-bg-color, #fff));" markdown>

### :lucide-scan-search: Classify a data object

Work through the questions below to determine the tier for a specific data object. The tool walks through the decision points described above and gives storage and handling guidance for the result.

--8<-- "templates-and-checklists/data-classifier-tool.html"

</div>


## What classification affects

Classification is not just a label — it determines concrete things about how you work with the data every day.

**Where you store it.** Green and Yellow data live in CMI's standard M365 environment. Red data lives there too, but with restricted access and potentially additional controls. Black data requires a case-by-case storage decision, often involving infrastructure outside M365. Moving beyond M365 involves additional costs that need to be budgeted in the project proposal.

**Which tools you can use.** This is the restriction researchers encounter most often. At Green, any tool is acceptable. At Yellow, enterprise tools are preferred but general-purpose tools are acceptable for non-sensitive tasks. At Red, only enterprise tools with a Data Processing Agreement are acceptable — no consumer AI tools, no services that use your data for training. At Black, no external cloud tools at all. See the Cloud Services and Tool Assessment guide for specific tool guidance.

**Who can access it.** Green data is unrestricted. Yellow is limited to the project team and relevant CMI staff. Red is restricted to named project members approved by the PI. Black is strictly limited to named individuals with a demonstrated need.

**What happens at the end.** Green data can be published and archived. Yellow and Red data containing personal information must be anonymised or deleted when no longer needed. Anonymised versions can move to Green for archiving. Black data requires documented end-of-project handling agreed in advance.


## Common mistakes

**Classifying by project instead of by data object.** A project studying public health policy may have Green-tier published statistics, Yellow-tier internal working notes, and Red-tier interview transcripts. The project does not have a single classification — each data object does.

**Classifying by intent instead of by current state.** "We plan to anonymise this" does not make the data Green now. Classification reflects what the data currently contains, not what you intend to do with it. The recordings are Red today; the anonymised transcripts will be Green when anonymisation is complete.

**Treating all personal data as equivalent.** A workshop invitation list and a dataset of interviews about political violence are both personal data. They are not the same risk. The classification scheme exists to make this distinction — use it.

**Assuming "not sensitive personal data" means "not sensitive."** Much of CMI's most consequential research — on governance, corruption, political economy, civic space — does not involve health, ethnicity, or the other categories that carry special legal protections. But the data can still be highly sensitive in context. A government official identifiable in a transcript criticising their own ministry faces real professional risk, even though nothing in the transcript falls into a legally protected category. Contextual sensitivity matters as much as data-type sensitivity.

**Forgetting that classification can change.** A dataset that is Red during active research may become Green after anonymisation. A project that starts in a stable context may escalate if the political situation changes. Review classification at project milestones and when circumstances shift.


## Contact

For questions about data classification and data management, contact [rdm@cmi.no](mailto:rdm@cmi.no). For DPIA, legal basis, and other GDPR concerns, contact [dpo@cmi.no](mailto:dpo@cmi.no). For IT support and secure storage setup, contact [help@cmi.no](mailto:help@cmi.no).
