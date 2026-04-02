---
icon: lucide/user-search
title: "Decide whether your project uses personal data"
description: "A thinking guide and interactive tool for deciding whether your project processes personal data and what follows from that choice."
tags:
  - Personal data
  - GDPR
  - Frame
  - Plan
  - Tool
notes: ""
date_updated: 2026-04-02
---

# Decide whether your project uses personal data

*This is one of the first questions to settle when shaping a project. If your project involves personal data, you need a Sikt notification, a legal basis for processing, an information letter, and a deletion plan. If it does not, none of that applies. The difference between the two paths is significant, and the boundary is blurrier than most researchers expect. For plain-language explanations of GDPR terminology, see [GDPR concepts for researchers](CROSS-legal.md).*

## What counts as personal data

Personal data is any information that can be linked to an identifiable person, directly or indirectly. The obvious cases are clear: names, national identity numbers, email addresses, photographs where someone is recognisable, voices on audio recordings.

The less obvious cases are where projects get caught off guard:

- A combination of background variables (age, municipality, occupation) can identify someone in a small population, even without a name attached.
- A scrambling key or code list linking pseudonyms to real identities makes the entire dataset personal data, regardless of who holds the key.
- Most survey platforms log email addresses or IP addresses by default. If the respondent's identity is recorded at any point, the responses are personal data.
- Publicly available social media posts containing usernames or profile information are personal data, even though they were publicly posted.

!!! warning "The real test"
    The test is not whether you *intend* to identify anyone. It is whether identification is *possible* by you, by your institution, or by anyone with access to the data combined with reasonably available information.

## Common mistakes

The most frequent error is assuming data is anonymous when it is not. Audio-recorded interviews are always personal data, even if you never ask for the participant's name. Observations in small, identifiable settings may be personal data. Online surveys are only anonymous if the platform genuinely never records the respondent's identity or network address, and this requires deliberate setup.

!!! info "Collecting anonymously vs. anonymising after collection"
    Collecting personal data and then anonymising it afterwards is still processing personal data, and still requires a Sikt notification. The distinction is fundamental.

## Why you might want personal data anyway

Avoiding personal data is not always desirable. Audio recordings preserve nuance that written notes cannot. Follow-up interviews, data linkage, and quality control all require identifiers. De-identified data can be archived for reuse in ways that fully anonymous data sometimes cannot. The principle of data minimisation does not mean collecting no personal data; it means being deliberate about what you collect, why, and for how long.

## What follows from each path

**If your project will involve personal data:** [prepare a Sikt notification](sikt-notification.md) before data collection begins, establish your legal basis for processing ([public interest](CROSS-gdpr-and-legal-compliance.md#lawful-basis-public-interest-as-the-recommended-default) is the recommended default at CMI), prepare an [information letter](CROSS-ethics.md) for participants, and plan for anonymisation or deletion at the end of the project. Under the public interest basis, the information letter *informs* participants about the research; it does not ask for GDPR consent to process data. See [the consent distinction](CROSS-gdpr-and-legal-compliance.md#the-consent-distinction-ethical-consent-and-gdpr-consent) for why this matters.

Also consider whether your data includes [special category data](CROSS-gdpr-and-legal-compliance.md#special-category-data) (health, political opinions, ethnic origin, religious beliefs, etc.). Special categories are common in CMI research and require an additional legal basis under Article 9(2)(j).

**If your project will not involve personal data:** confirm genuinely that no element of the data collection process records identifying information at any point. If you are confident the data is anonymous throughout, you do not need a Sikt notification, but you still have ethical obligations to [inform participants and obtain their agreement](CROSS-ethics.md) to take part.

!!! tip "If you are unsure"
    Err on the side of notifying Sikt. Their advisers assess over ten thousand projects a year and can tell you quickly whether your design involves personal data.

!!! info "Review date"
    This page was last reviewed on 2 April 2026. Data protection guidance evolves as regulatory interpretations and institutional practice develop. Verify against current Sikt and Datatilsynet guidance for your specific situation.


<div style="border: 2px solid var(--md-primary-fg-color, #4051b5); border-radius: 12px; padding: 1.5em 2em; margin: 1.5em 0; background: color-mix(in srgb, var(--md-primary-fg-color, #4051b5) 6%, var(--md-default-bg-color, #fff));" markdown>

## :lucide-user-search: Quick check: will your project involve personal data?

Work through the questions below to get an initial indication. This is a starting point for reflection, not a legal determination.

--8<-- "templates-and-checklists/personal-data-decider.html"

</div>
