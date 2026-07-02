---
icon: lucide/scroll-text
title: "Principles for research data management"
description: "CMI's 13 principles for planning, handling, documenting, securing, and sharing research data. A practical reference for researchers and a citable resource for data management plans."
tags:
  - Principles
  - Governance
  - FAIR
  - CARE
notes: ""
date_updated: 2026-07-02
---

# Principles for research data management

*These 13 principles set the direction for how you plan, collect, protect, document, and share research data at CMI. They are a shared reference point, not a rulebook: your project translates them into concrete decisions through its DMP and documents the reasoning wherever you adapt them. Cite this page in your DMP and explain how the relevant principles apply to your data.*

Two assumptions run through everything below. First, good data management is context-sensitive: what counts as sensitive data, adequate anonymisation, or meaningful consent depends on the setting, the population, and the discipline, so adapt this guidance to your research environment rather than applying it as a template. Second, responsibility is shared: the PI, the data manager, field researchers, and partners all carry it, and raising concerns about data practices should be welcomed on your team, not discouraged.

## Openness with judgement

**Treat FAIR as a framework, not a formula.** The [FAIR principles](https://www.go-fair.org/fair-principles/)[^1] point you towards data that others can find, access, and reuse, but they are not a score to maximise. Good metadata can make even closed data findable, and access can be controlled or embargoed where the context demands it. Document how you apply each dimension, and explain where you deliberately limit openness. [Foundations of data sharing](foundations-of-data-sharing.md) covers this in depth.

**Be as open as possible, as closed as necessary.** Openness serves accountability and scholarly exchange; it is a means, not an end in itself. Decide deliberately what you share and what you restrict, record decisions not to share alongside decisions to share, and be forthcoming with funders and partners about both. The [PRESERVE stage](lifecycle-9-preserve.md) describes the access levels available when you archive.

## Protect the people in your data

**Put participants' safety and interests first.** No output or decision from your project should expose participants, their communities, or associated individuals to foreseeable harm, and this commitment overrides openness whenever the two conflict. Harm includes physical, psychological, social, legal, economic, and reputational risk, assessed not only at collection but in light of how data might be linked or reinterpreted over time. Consent is an ongoing relationship, not a form: be honest about the limits of anonymisation, adapt consent processes to the setting, and revisit consent when the use of your data changes. The NESH guidelines[^2] and the [ethics pages](CROSS-ethics.md) set out what this means in practice.

**Collect only the data you need.** Minimisation is a legal obligation for personal data[^3] and sound practice for everything else: less sensitive material to protect, less to lose in a breach, less to justify. Be prepared to defend the necessity of each category of data you collect, especially with vulnerable populations. The [personal data decider](personal-data-decider.md) helps you work out what counts as personal data in the first place.

**Respect the communities behind the data.** The [CARE principles](https://www.gida-global.org/care)[^4] complement FAIR where data concerns Indigenous peoples or other communities with a stake in it: ask not only whether data can be shared, but who benefits from collection and reuse, and who has the authority to decide.

## Secure in proportion to risk

**Match protection to the actual sensitivity of your data.** Not all data carries the same risk, and over-restriction wastes effort and blocks legitimate collaboration just as under-protection endangers people. Classify your data honestly, apply safeguards that fit, and review them as the risk profile changes over the project. Start with [security and data classification](data-classification.md).

**Grant access on demonstrated need.** Give each person the minimum access their role requires, document who can see what, and review permissions when people join or leave the team. Agree the scope and conditions of any external access in advance. The [STORE stage](lifecycle-5-store.md) covers the practicalities.

## Make your data trustworthy

**Document provenance as you go.** Keep traceable records of collection, coding, transformation, and anonymisation steps while they happen; reconstructing them afterwards rarely works. A [data inventory](data-inventory.md) gives you a running record of what data exists and how it has been handled.

**Build quality in rather than auditing it in.** Consistent procedures, version control, and metadata that states a dataset's scope and limitations are what make your data credible, both for your own analysis and for anyone who reuses it later.

**Work so that others could reproduce your results.** Reproducibility is a property of the whole workflow: data, code, documentation, and the decisions that link them. [Reproducibility and transparency](reproducibility-and-transparency.md) shows how to get there step by step.

## Plan the whole lifecycle

**Plan data management before it becomes urgent.** The cheapest time to make good data decisions is before collection starts. Write your DMP at the [PLAN stage](lifecycle-3-plan.md) using the [CMI DMP template](dmp-cmi.md), and treat it as a living document rather than a funding formality.

**Decide what you keep, for how long, and what happens to the rest.** Not everything should be kept indefinitely. Define retention periods at the planning stage, distinguish data destined for long-term preservation from data that should be securely deleted, and document both decisions. [Project closure](project-closure.md) walks you through disposal at the end.

## When the law itself is a risk

**Where a national legal framework functions as an instrument of surveillance or control, prioritise participant safety over formal compliance with that framework.** In some countries where CMI works, data localisation mandates, broadly drafted cybercrime offences, or restrictions on encryption put research data and participants at risk rather than protecting them. Recognising and navigating these environments takes careful, case-by-case judgement, and it deserves more than a paragraph.

!!! info "Dedicated guidance in preparation"
    A full page on adverse legal environments, covering legal environment assessment, storage location decisions, and secure communication, is in preparation. Until it is published, raise any such situation with rdm@cmi.no before making decisions. For the standard legal landscape, see [GDPR and legal compliance](CROSS-gdpr-and-legal-compliance.md).

## Putting the principles to work

When you write a DMP or review your data practices:

- Reference the principles explicitly and note how each relevant one applies to your project.
- Explain adaptations and departures; the reasoning matters more than uniformity.
- Revisit them when circumstances change, especially the risk environment.
- Use them as a shared vocabulary with partners, funders, and ethics reviewers.

[^1]: Wilkinson, M. D. et al. (2016). 'The FAIR Guiding Principles for scientific data management and stewardship'. *Scientific Data*, 3, 160018. [doi.org/10.1038/sdata.2016.18](https://doi.org/10.1038/sdata.2016.18)
[^2]: NESH (2021). *Guidelines for Research Ethics in the Social Sciences and the Humanities*, 5th edition. Norwegian National Research Ethics Committees. [forskningsetikk.no](https://www.forskningsetikk.no/en/guidelines/social-sciences-humanities-law-and-theology/guidelines-for-research-ethics-in-the-social-sciences-humanities-law-and-theology/)
[^3]: GDPR, Article 5(1)(c). Regulation (EU) 2016/679.
[^4]: Carroll, S. R. et al. (2020). 'The CARE Principles for Indigenous Data Governance'. *Data Science Journal*, 19(1), 43. [doi.org/10.5334/dsj-2020-043](https://doi.org/10.5334/dsj-2020-043)
