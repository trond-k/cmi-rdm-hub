---
icon: lucide/user-search
title: "Decide whether your project uses personal data"
description: "A thinking guide for deciding whether your project processes personal data and what follows if it does."
tags:
  - Personal data
  - GDPR
  - Frame
notes: ""
date_updated: 2026-03-24
---

# Decide whether your project uses personal data

<!-- Manual content for the RDM Hub.
     Located at: /content/manual/lifecycle/frame-personal-data.md

     A thinking guide for the Frame stage. Helps researchers
     determine whether their project will process personal data,
     understand situations where personal data is present but
     not obvious, and consider whether they actually need or
     want personal data for their research purposes.

     Deliberately does not use GDPR article numbers. References
     Sikt guidance where relevant. CMI voice throughout.

     This is not a compliance guide — it is a design guide.
     The question is not just "will I have personal data?"
     but "should I, and what follows from that choice?" -->

*Trond Kvamme · 6 min read*

This is one of the first questions to settle when shaping a project, and it is less straightforward than it sounds. Many researchers assume the answer is obvious — of course they will collect personal data, or of course they will not. In practice, the boundary is blurrier than expected, and the choice is more consequential than it appears.

Getting this right early matters. If your project involves personal data, you need a Sikt notification, a legal basis for processing, an information letter, a real storage and access setup, and a deletion plan. If it does not, none of that applies. The difference between the two paths is significant — not because the compliance burden is unmanageable, but because it shapes how you design data collection, what you can do with the data afterwards, and how freely you can share it.


## What counts as personal data

Personal data is any information that can be linked to an identifiable person, directly or indirectly. The definition is broader than most researchers expect.

The obvious cases are clear: names, national identity numbers, email addresses, photographs where someone is recognisable. A voice on an audio recording is personal data. A video of a person is personal data.

The less obvious cases are where projects get caught off guard. A combination of background variables — age, municipality of residence, occupation, workplace — can identify someone even without a name attached, particularly in small populations. If your survey collects exact age, village, and profession in a community of a few hundred people, that may be enough to single out an individual. Whether a combination is identifying depends on the variables, the population size, and the context.

A scrambling key or code list also makes data personal. If you collect data under pseudonyms but maintain a list linking those pseudonyms to real identities, the entire dataset is personal data — even if the research team working with the data never sees the key. The existence of the key is what matters, not who holds it.

Online data collection carries its own traps. Most survey platforms link responses to an email address or IP address by default. If the respondent's email or IP is recorded at any point during the process, the responses are personal data, even if the survey questions themselves contain nothing identifying. Using a genuinely anonymous survey solution — one that never records the respondent's identity or network address — requires deliberate setup, not just an assumption that the platform handles it.


## The case where you think you are anonymous but you are not

This is the most common mistake. A project intends to collect anonymous data, but some element of the design inadvertently makes participants identifiable:

You record interviews as audio. Even if you never ask for the participant's name, their voice is personal data. An interview recorded on audio cannot be anonymous.

You collect notes from observations in a small setting — a specific school, a particular village, a named organisation. Even without names, the combination of the setting and the details you record may identify individuals to anyone familiar with that context.

You run an online survey that you believe is anonymous, but the platform logs IP addresses or requires login. The survey is not anonymous.

You use a code list to track who has responded so you can send reminders. While the code list exists, the data is personal — even if you plan to delete the list when collection is complete. The processing requires a Sikt notification because personal data is handled at some point in the process.

You analyse publicly available social media posts. If the posts contain usernames, profile information, or are directly searchable, the data is personal even though it was publicly posted.

!!! warning "The real test"

    The test is not whether you *intend* to identify anyone. It is whether identification is *possible* — by you, by your institution, or by anyone with access to the data combined with reasonably available information.


## Can you design the project without personal data?

Before assuming personal data is necessary, it is worth asking whether your research questions can be answered without it. Some projects can be designed to avoid personal data entirely, and this is worth considering — not only because it simplifies compliance, but because it changes what you can do with the data after the project.

Sikt's guidance describes several approaches to collecting data without processing personal data. During interviews and observations, record data only as written notes, without audio or video, and ensure no names or identifiable background information appear in those notes. For surveys, use paper forms without names or identifying details, or use an online tool with a verified anonymous mode — meaning the respondent's email, IP address, and identity are never linked to the response. For registry or statistical data, work with aggregated or pre-anonymised data where no individual can be traced.

If your entire data collection is anonymous from the start — meaning personal data is never collected, not even temporarily — the project does not need a Sikt notification. But "anonymous from the start" is a high bar.

!!! info "Collecting anonymously vs. anonymising after collection"

    Collecting personal data and then anonymising it afterwards is still processing personal data, and still requires a Sikt notification. The distinction between collecting anonymously and anonymising after collection is fundamental.


## Why you might want personal data anyway

Avoiding personal data is not always desirable, even when it is technically possible. There are legitimate research reasons to collect and retain identifiable information, and pretending the data is anonymous when it is not — or stripping out identifying detail that your analysis actually needs — can produce worse research.

**Richer, more trustworthy data.** Qualitative research thrives on context, specificity, and the ability to capture how people actually talk about their experiences. Audio-recorded interviews preserve tone, emphasis, hesitation, and nuance that written notes cannot capture. Observational research is richer when you can describe individuals and their roles rather than abstracting them into interchangeable units. If your research questions require depth, stripping out the identifying detail may undermine exactly what makes the data valuable.

**Follow-up and longitudinal work.** If you may need to return to participants — for member-checking, follow-up interviews, longitudinal data collection, or clarification of earlier responses — you need to know who they are. An anonymous dataset cannot be followed up.

**Data linkage.** Some research designs require linking your data to other datasets — health registries, administrative records, prior survey waves. Linkage requires identifiers, at least temporarily. If you design the project as fully anonymous, linkage is impossible.

**Verification and quality control.** The ability to check whether a specific response is internally consistent, whether a participant meets the inclusion criteria, or whether duplicate responses have been submitted all depend on having some identifying information. Fully anonymous survey data cannot be de-duplicated or validated against external criteria.

**Credibility and transparency.** In some research contexts, the ability to attribute statements to named sources — with their consent — strengthens the research. Policy research, institutional analysis, and elite interviews often derive their value precisely from the fact that named individuals said specific things on the record.

**Archiving and reuse.** De-identified data (where identifiers are removed but the data retains enough structure for reanalysis) can be archived and shared for future research. Fully anonymous data can also be shared, but if the anonymisation required stripping out so much context that the data is no longer analytically useful, reuse becomes pointless. There is a trade-off between privacy protection and long-term utility, and the right balance depends on your data and your field. Use [Decide what can be shared](sharing-decisions.md) when the project starts making that choice explicitly.

The principle of data minimisation — collecting only the personal data you need for your stated purpose — does not mean collecting no personal data. It means being deliberate about what you collect, why, and for how long.


## Making the decision

The question is not only "will I process personal data?" but "should I, given what my research needs?" Work through these considerations for each data stream in your project:

**What does your method require?** Audio-recorded interviews involve personal data. So do surveys linked to respondent identities, ethnographic fieldwork in identifiable settings, and any analysis of named individuals' public statements. If your chosen method inherently produces personal data, the question is settled — plan for it.

**What do your research questions need?** If your analysis depends on individual-level detail, context, or the ability to link data across sources, you probably need personal data. If it depends only on aggregate patterns or thematic findings that do not require tracing responses to individuals, you may not.

**What is the risk profile of your participants?** Personal data about public officials commenting on public policy carries different risks than personal data about displaced persons discussing political violence. The sensitivity of the data should influence not whether you collect personal data, but how carefully you handle it. For high-risk participants, minimise what you collect, secure what you hold, and plan clearly for when and how it will be deleted.

**What do you want to do with the data afterwards?** If you want to archive data for reuse, you need to consider what form it will take at the end. Data collected with identifiers can be de-identified for archiving. Data collected anonymously is already shareable but may lack the structure needed for meaningful reuse. Plan the endpoint when you design the beginning.


## What follows from each path

If your project **will involve personal data**: [prepare a Sikt notification](sikt-notification.md) before data collection begins, establish your legal basis for processing, prepare an information letter for participants, [choose storage and control access](storage-and-access.md) in line with CMI's data handling requirements, and plan for anonymisation or deletion at the end of the project. These steps are part of the normal workflow for most CMI projects.

If your project **will not involve personal data**: confirm — genuinely confirm — that no element of the data collection process records identifying information at any point. No audio recordings of identifiable voices. No IP addresses logged by survey tools. No code lists linking responses to individuals. No background variable combinations that could identify someone in a small population. If you are confident the data is anonymous throughout, you do not need a Sikt notification, but you still have ethical obligations to inform participants about the research and obtain their agreement to take part.

!!! tip "If you are unsure"

    Err on the side of notifying Sikt. Their advisers assess over ten thousand projects a year and can tell you quickly whether your design involves personal data. It is better to ask than to discover halfway through fieldwork that your data is not as anonymous as you assumed.


<div style="border: 2px solid var(--md-primary-fg-color, #4051b5); border-radius: 12px; padding: 1.5em 2em; margin: 1.5em 0; background: color-mix(in srgb, var(--md-primary-fg-color, #4051b5) 6%, var(--md-default-bg-color, #fff));" markdown>

## :lucide-user-search: Quick check: will your project involve personal data?

Work through the questions below to get an initial indication. This is a starting point for reflection, not a legal determination.

--8<-- "templates-and-checklists/personal-data-decider.html"

</div>
