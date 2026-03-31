---
icon: lucide/eye
title: "Reproducibility and transparency"
description: "Make your research traceable: document tools, decisions, and AI use so that others can follow the path from raw data to findings."
tags:
  - Reproducibility
  - Transparency
  - Documentation
  - AI governance
  - FAIR
  - CARE
  - Preregistration
notes: ""
date_updated: 2026-03-26
---

# Reproducibility and transparency

*Reproducibility means someone else can follow the path from your data and documentation to your results. Transparency means they can see why you made the choices you did. These principles apply across methods, but they look different for a scripted regression than for a coded interview. This page covers what reproducibility requires in practice, how to navigate the tension between openness and participant protection, and what funders and publishers now expect.*

## Why this matters now

Research credibility is under pressure. High-profile fabrication cases, a documented replication crisis, and the spread of AI-generated content have all raised the stakes. But the picture is not bleak: large-scale replication projects consistently find that methodological reforms (preregistration, adequate statistical power, transparent reporting) improve replicability. The practices on this page are a tested response to systemic problems. They were, however, designed primarily for quantitative, lab-based research. If your work involves qualitative interviews, fieldwork in sensitive contexts, or participatory methods in the Global South, the standard prescriptions need adaptation. This page takes both the principles and the complications seriously.

## What reproducibility requires

At its simplest, reproducibility asks: could another competent researcher, given your data, your code, and your documentation, produce the same findings? For scripted quantitative work, this is concrete and testable. For qualitative and interpretive work, it takes a different form: not identical results, but a legible trail from source material to conclusions that allows others to assess the reasoning.

The practical requirements hold regardless of method:

- **Record what you did.** Every consequential step should be documented. For scripted work, the code is the record. For fieldwork and qualitative projects, interview logs, processing notes, and decision memos serve the same purpose.
- **Record what you used.** For computational work: software, versions, packages, and operating system. For qualitative work: interview guide versions, recording equipment, transcription method and tool, analytical software, and coding framework. If a result depends on a specific version of a tool, protocol, or instrument, it is not reproducible unless the version is recorded.
- **Record why you chose it.** Methods sections describe what was done. Reproducibility also requires knowing why: why this analytical approach, why these cases were excluded, why two codes were merged, why this sampling strategy. Decision logs capture reasoning that methods sections compress or omit.

!!! tip "The bus test"
    If you were hit by a bus tomorrow, could a colleague pick up your project folder and understand what you did, how you did it, and why? If the answer is no, something is missing.

## Transparency in qualitative and fieldwork-based research

For interpretive work, the goal is not replication of results but transparency of process. Others should be able to trace how you moved from raw material to conclusions and assess whether your interpretive choices are defensible.

- **Analytical memos.** Document your reasoning at each stage of coding or thematic development: not just what codes you applied, but why, and how your thinking evolved.
- **Codebook versioning.** If your coding scheme develops iteratively, keep dated versions. A final codebook alone does not show how categories emerged from the data.
- **Reflexivity as rigour.** Make your positionality, assumptions, and relationship to the research context explicit. This is the qualitative equivalent of declaring your priors.
- **Active citation.** Where data cannot be shared, precise references to specific passages in source material allow readers to assess your claims without access to the complete dataset.[^1]

These are not a lesser standard than scripted reproducibility. They are the appropriate standard for research where human judgement is the analytical instrument.

## Preregistration

Preregistration means lodging your research design and analysis plan in a public registry before data collection begins. The purpose is to distinguish confirmatory analysis (testing pre-specified hypotheses) from exploratory analysis (investigating patterns that emerged from the data). Both are legitimate; the problem arises when exploratory findings are presented as confirmatory.

For quantitative work, registries such as [OSF](https://osf.io/), [AsPredicted](https://aspredicted.org/), and [EGAP](https://egap.org/registry/) (relevant for governance and development research) provide templates and time-stamped records. Over 800,000 registrations are now held on OSF alone.

For qualitative work, preregistration is more contested. The emerging distinction is between a 'constraining' model that commits to specific procedures and a 'transparency' model that documents the starting point without restricting methodological emergence.[^2] The transparency model is gaining traction because it respects the iterative nature of qualitative inquiry while still providing an auditable record.

Preregistration does not lock you in. If your plan changes, update the record and document the deviation. Be aware, however, that preregistration addresses one specific threat (post-hoc hypothesis framing) and does not substitute for good design, measurement, or theory. For a fuller treatment of platforms, what to include, and how pre-registration works for qualitative research, see the dedicated [pre-registration and Registered Reports](CROSS-preregistration.md) page.

### Registered Reports

Registered Reports are a publishing format in which a journal peer-reviews your design and analysis plan before data collection and commits to publishing the results regardless of outcome. Over 300 journals now offer this format. Studies published as Registered Reports show dramatically higher rates of null results (around 60 per cent, compared with roughly 5 per cent in standard publications), the strongest available evidence that the format reduces publication bias.[^3]


The format adds time (typically 6–12 months for Stage 1 review) and works best for confirmatory research. For CMI researchers planning quantitative or mixed-methods studies where null findings would be informative, it is worth considering as a publishing strategy.

## Documenting AI tools

If you use generative AI or machine learning tools at any point in the research process, document them as you would any other methodological choice. Major publishers now uniformly prohibit listing AI tools as authors and require disclosure of generative AI use.[^4] These policies are converging rapidly.

??? example "What to record for each AI use"
    For each use of an AI tool in your research, record:

    1. Tool name, model version, and date of use
    2. Task performed (e.g., transcription, coding, translation, drafting)
    3. Whether personal data was included in the input
    4. Relevant parameters or settings
    5. How the output was handled: accepted, reviewed and corrected, or discarded
    6. The verification method you applied
    7. Known limitations relevant to your data or task
    8. Whether a Data Processing Agreement was in place (if personal data was involved)

!!! warning "Data protection and AI services"
    Cloud-based AI services process data on remote servers and may retain or train on your input. If personal data is involved, a Data Protection Impact Assessment (DPIA) may be required, along with a Data Processing Agreement with the provider. The Norwegian Data Protection Authority has confirmed that a DPIA is required before deploying generative AI tools that process personal data.[^5] Enterprise-tier services with contractual data protection commitments are not the same as consumer-tier tools; verify which you are using. See [GDPR and legal compliance](CROSS-gdpr-and-legal-compliance.md) for further guidance.

!!! danger "Hallucinated references are a documented problem"
    AI tools generate plausible but non-existent citations. Audits of recent major conferences found over 100 hallucinated references in accepted papers.[^6] Every AI-generated citation must be verified against the actual source.

??? example "Publisher AI policies at a glance (2025)"
    | Publisher | AI as author | Disclosure required | AI-generated images |
    |---|---|---|---|
    | Nature / Springer Nature | Prohibited | Methods section | Caution advised |
    | Elsevier | Prohibited | Mandatory statement | Prohibited (with exceptions) |
    | Wiley | Prohibited | Methods or Acknowledgements | Not addressed |
    | Taylor & Francis | Prohibited | Required | Prohibited for generation |
    | COPE | Prohibited | Materials and Methods | Not addressed |
    | ICMJE | Prohibited | At submission | Not addressed |

## Transparency and protection

CMI researchers frequently work in contexts where full transparency and participant protection pull in opposite directions. Interviews in authoritarian settings, fieldwork in small communities where true anonymisation may be impossible, partnerships where data sovereignty is at stake: these are the normal research environment, not edge cases.

The guiding formulation is 'as open as possible, as closed as necessary,' but the burden of justifying closure falls on you. Several principles help navigate the tension:

- **FAIR and CARE together.** The [FAIR principles](https://www.go-fair.org/fair-principles/) maximise data reuse. The [CARE Principles](https://www.gida-global.org/care) for Indigenous Data Governance (Collective Benefit, Authority to Control, Responsibility, Ethics) ensure that reuse does not cause harm.[^7] Neither framework is complete without the other.
- **Tiered access.** Not all data needs to be fully open. Repositories such as [Sikt Research Data Archive](https://sikt.no/en/tjenester/arkivere-data) and the [UK Data Service](https://ukdataservice.ac.uk/) offer restricted access, where approved researchers can use sensitive data under controlled conditions.
- **Metadata sharing.** When data cannot be shared, describe what the data are: how they were collected, what they contain, and under what conditions access might be negotiated. This supports discoverability without exposure risk.
- **Temporal sensitivity.** Data safe to share now may not have been safe earlier, and political contexts shift. Review sharing decisions at appropriate intervals rather than treating them as permanent.

!!! tip "When funder mandates and ethics restrictions conflict"
    If your funder requires open data but your ethics approval restricts sharing, document the conflict and the resolution. Both Horizon Europe and the Research Council of Norway accept justified exceptions. The important thing is a reasoned decision, not a default to either extreme.

## Tools and infrastructure

For scripted analysis, [Git](https://git-scm.com/) remains the standard for version control. Host repositories on [GitHub](https://github.com/), [GitLab](https://about.gitlab.com/), or [nordic-gitlab.deic.dk](https://nordic-gitlab.deic.dk/) (free for Nordic researchers). [CodeRefinery](https://coderefinery.org/) offers training in reproducible research practices across the Nordics.

For reproducible documents, [Quarto](https://quarto.org/) provides manuscript project types that produce publication-ready output in multiple formats from a single source, with embedded code and citations. If you work in R or Python, it is the natural choice for combining analysis and writing.

Software environments change. For R, `renv` freezes package versions. For Python, virtual environments or `conda` serve the same purpose. For complex projects, [Docker](https://www.docker.com/) containers freeze the entire computational environment. The effort scales with the stakes: an internal analysis may need only a README note; a multi-year published project should have a fully versioned, environment-locked workflow.

Norway's research infrastructure continues to develop. [NVA](https://sikt.no/en/tjenester/nasjonalt-vitenarkiv-nva) is the single platform for registering and sharing research outputs. The [NIRD Research Data Archive](https://www.sigma2.no/) handles large-scale scientific data with DOI minting. [Sikt Research Data Archive](https://sikt.no/en/tjenester/arkivere-data), CoreTrustSeal-certified, is the primary option for social science data with controlled access.

## Transparency about uncertainty

Reproducibility is not just about getting the same numbers. It is about being honest with the reader about how much confidence those numbers, themes, or interpretations deserve.

Report negative results. A model that shows no effect is a finding. Selective reporting distorts the evidence base and wastes future researchers' time.

Report deviations from your plan. If you preregistered a design and then changed it, explain what changed and why. If you ran twenty model specifications and report the one that worked, say that too.

Report the limitations of your tools. If your automated transcription struggles with a particular language and you estimate 10 per cent of the transcript contains errors, the reader needs to know. If your sample is not representative in a way that affects generalisability, state it directly rather than burying it in a footnote.

Research that is transparent about its limitations is more credible, not less.

## What funders expect

Major research funders have converged on expectations around transparency and reproducibility. No major funder currently mandates preregistration for non-clinical research, but the direction is clear: FAIR data management, immediate open access, and a Data Management Plan are increasingly standard. The [PLAN](lifecycle-3-plan.md) stage covers DMP requirements in detail.

??? example "Funder expectations at a glance"
    | Funder | Open access | Data sharing | DMP required | Preregistration |
    |---|---|---|---|---|
    | Horizon Europe | Immediate, no embargo | FAIR by default | Yes | Encouraged |
    | Research Council of Norway | Immediate (Plan S) | FAIR, suitable repository | Yes | Encouraged |
    | ERC | Immediate | FAIR, trusted repository | Yes | Encouraged |
    | Norad | Varies by programme | Increasingly expected | Varies | Not specified |
    | NIH (US) | Immediate from Jul 2025 | Sharing plan required | Yes | Clinical trials only |

The shift in research assessment matters too. Initiatives such as [DORA](https://sfdora.org/) and [CoARA](https://coara.eu/) are moving evaluation away from journal prestige toward research quality, creating institutional space for researchers to invest in reproducibility practices without fearing the effort goes unrewarded.

[^1]: Jacobs, A.M., Büthe, T. et al. (2021). [The Qualitative Transparency Deliberations: insights and implications](https://doi.org/10.1017/S1537592720001164). *Perspectives on Politics*, 19(1), 171–208.
[^2]: Haven, T. & Van Grootel, L. [Preregistration template for qualitative studies](https://osf.io/j7ghv/overview), OSF Registries.
[^3]: Scheel, A.M. et al. (2021). [An excess of positive results](https://doi.org/10.1177/25152459211007467). *Advances in Methods and Practices in Psychological Science*.
[^4]: [COPE position on authorship and AI tools](https://publicationethics.org/guidance/cope-position/authorship-and-ai-tools); [ICMJE Recommendations](https://www.icmje.org/recommendations/) (updated January 2024).
[^5]: Datatilsynet. [NTNU/Copilot regulatory sandbox exit report](https://www.datatilsynet.no/en/regulations-and-tools/sandbox-for-artificial-intelligence/reports/ntnu-exit-report-copilot-through-the-lens-of-data-protection/), November 2024.
[^6]: GPTZero. [Hallucinated citations in NeurIPS 2025 papers](https://gptzero.me/news/neurips/), January 2026.
[^7]: Carroll, S.R. et al. (2020). [The CARE Principles for Indigenous Data Governance](https://doi.org/10.5334/dsj-2020-043). *Data Science Journal*, 19(1), 43.

!!! info "Last reviewed"
    This page was last reviewed on 26 March 2026. AI governance, funder policies, and Norwegian research infrastructure are evolving rapidly; verify against the latest source.
