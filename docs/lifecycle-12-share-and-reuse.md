---
icon: lucide/repeat
title: "SHARE & REUSE"
description: "Enable others to use your data responsibly: choose the right licence, document for a stranger, and think about who will reuse your data and what they need."
tags:
  - Share
  - Reuse
  - Licensing
  - FAIR
  - CARE
  - Documentation
  - Ethics
notes: ""
date_updated: 2026-03-26
---

# SHARE & REUSE: enabling downstream use

*Sharing is not a technical act; it is a governance decision. The [ACCESS](lifecycle-11-access.md) stage addresses who can retrieve your data and under what mechanisms. This stage addresses what happens next: whether others can legally reuse what they retrieve, whether they can understand it without your help, and whether the terms of reuse reflect the rights and risks involved. A well-chosen licence, thorough documentation, and honest attention to who your reusers are make the difference between data that sits in a repository and data that generates new knowledge.*

## Choose a licence

Without a licence, your data has no clear terms of reuse. Others may be able to access it, but they cannot know whether they are permitted to redistribute it, modify it, combine it with other data, or use it commercially. A licence removes this ambiguity.

For research data, the most common options are:

| Licence | What it permits | When to use it |
|---|---|---|
| [CC0](https://creativecommons.org/public-domain/cc0/) | Unrestricted use, no conditions | Data where maximum reuse is the goal and no restrictions are needed (e.g., fully de-identified quantitative data, metadata, codebooks) |
| [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | Reuse with attribution | The default for most open research data; requires users to credit the creator |
| [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) | Reuse with attribution, non-commercial only | Data where commercial exploitation would be inappropriate or was excluded by participant consent |
| Open Data Commons licences ([ODC-BY](https://opendatacommons.org/licenses/by/), [ODbL](https://opendatacommons.org/licenses/odbl/)) | Vary by licence | Databases and structured datasets where a database-specific licence is more appropriate |
| Bespoke terms | Defined by the depositor | Data under controlled access where standard licences do not capture the conditions (e.g., community-governed data, data with use-purpose restrictions) |

CC BY 4.0 is the safe default for most open CMI data. It satisfies funder requirements for openness while ensuring that creators are credited. CC0 is appropriate where attribution is impractical or unnecessary (reference datasets, lookup tables, simple metadata). Non-commercial restrictions (NC) should be used deliberately, not as a precaution: they prevent legitimate reuse by organisations that may count as commercial under the licence terms, including some NGOs, consultancies, and media outlets.

!!! warning "Licence compatibility matters when combining datasets"
    If your project integrates data from multiple sources, each with its own licence, the terms must be compatible. A dataset released under CC BY-SA (share-alike) cannot be combined with one under CC BY-NC without violating one or both licences. Check compatibility before combining, and document the licensing provenance of any composite dataset you create.

## Document for a stranger

Much of the documentation discussed in earlier stages ([PROCESS](lifecycle-6-process.md), [ANALYSE](lifecycle-7-analyse.md), [PUBLISH](lifecycle-8-publish.md)) serves the project team and the archive. Reuse documentation serves a different audience: someone who has never spoken to you and may work in a different discipline or country.

The test is whether that person can understand your data well enough to use it responsibly without contacting you. This means answering, in writing, the questions they would ask:

- **What does this dataset contain?** Not a technical variable list (that is the codebook), but a plain-language explanation of the scope, coverage, and purpose.
- **What are its limitations?** Known biases, coverage gaps, missing data patterns, and anything that could mislead an analyst unfamiliar with the context. Researchers are often reluctant to advertise limitations, but reusers who discover them unwarned lose trust in the data entirely.
- **Who are the likely reusers?** The answer shapes what documentation is needed. A policymaker needs a plain-language summary. A fellow researcher needs a codebook. An AI developer needs to know the licence and the population the data represent. Not every reuser will read a 40-page methodology report, but a clear README that points them to the relevant detail costs very little to produce.

!!! tip "Write the README before you forget"
    The best time to write reuse documentation is while the project is still active and the details are fresh. A README drafted at deposit is almost always thinner than one written during analysis, because by deposit time the team has moved on mentally. Build documentation into your workflow, not your exit checklist.

## Think about who will reuse your data

Reuse is not abstract. Different reusers bring different risks and different value:

- **Researchers in the same field** are the most common reusers and the easiest to anticipate. They need codebooks, methodology notes, and clear variable definitions.
- **Policymakers and journalists** may draw on your data to inform decisions or public debate. They need accessible summaries and honest statements of what the data can and cannot support.
- **Researchers in other fields** may combine your data with sources you did not anticipate. Documentation of sampling, coverage, and known limitations becomes critical here.
- **AI training pipelines.** Datasets in open repositories may be ingested into machine learning systems. If the data describe identifiable communities or reflect cultural knowledge, this raises questions about consent and representation that the original licence may not address. Where your consent language is narrow or where the data carry sensitivity, consider whether the access conditions set at the [ACCESS](lifecycle-11-access.md) stage adequately govern this kind of reuse.

You cannot control all downstream use. But you can shape it through the combination of licence terms, access conditions, and documentation. A dataset released under CC BY 4.0 with a clear README and an honest limitations section is far less likely to be misused than one released without context.

## Track reuse and impact

Once data are shared, it is worth knowing whether anyone uses them. Data citations, download counts, and altmetrics provide rough signals. Some repositories notify depositors when their data are cited in a new publication.

More useful, but harder to systematise, is direct feedback from reusers. If someone discovers an error, wants to contribute a correction, or has produced a derived dataset that complements yours, a clear contact channel (the depositor's ORCID-linked email, or the archive's messaging system) makes this possible. Research data improves through use; feedback loops are how that improvement happens.

Tracking reuse also strengthens the case for data as a research output. If your deposited dataset generates citations, informs policy, or enables work by other teams, that is evidence of impact that belongs in your CV, your institutional reporting, and your next funding application.

!!! info "Last reviewed"
    This page was last reviewed on 26 March 2026. Licensing frameworks, publisher expectations, and AI governance norms are evolving rapidly; verify against the latest source.