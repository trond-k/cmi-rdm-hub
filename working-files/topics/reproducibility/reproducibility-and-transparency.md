---
icon: lucide/eye
title: "Reproducibility and transparency"
description: "Make your research traceable: document tools, decisions, and AI use so that others can follow the path from raw data to findings."
tags:
  - Reproducibility
  - Transparency
  - Documentation
  - AI governance
notes: ""
date_updated: 2026-03-26
---

# Reproducibility and transparency

*Reproducibility means that someone else, working from your data and documentation, can follow the path you took and arrive at the same results. Transparency means they can see why you made the choices you did. Neither requires perfection; both require discipline. This page covers the practices that make research traceable across the lifecycle, from preregistration through to documenting AI tools.*

## What reproducibility requires

At its simplest, reproducibility asks: could another competent researcher, given your data, your code, and your documentation, produce the same findings? For fully scripted quantitative work, this is a concrete, testable standard. For qualitative and interpretive work, it takes a different form: not identical results, but a legible trail from source material to conclusions that allows others to assess the reasoning.

The practical requirements are the same regardless of method:

- **Record what you did.** Every consequential step, from data cleaning through analysis, should be documented. For scripted work, the code is the record. For manual steps, a processing log or decision memo serves the same purpose.
- **Record what you used.** Software, versions, packages, operating system, hardware where it matters (e.g., GPU-dependent computation). A result that depends on a specific version of a library is not reproducible if the version is not recorded.
- **Record why you chose it.** Methods sections in publications describe what was done. Reproducibility also requires knowing why: why this model and not that one, why these cases were excluded, why two codes were merged. Decision logs capture reasoning that methods sections compress or omit.

!!! tip "The test is simple"
    Ask yourself: if I were hit by a bus tomorrow, could a colleague pick up my project folder and understand what I did, how I did it, and why? If the answer is no, something is missing.

## Preregistration

Preregistration means committing to your research design and analysis plan before data collection begins, by lodging it in a public registry. It is well established in quantitative and experimental research and increasingly adopted in other traditions.

The purpose is to distinguish confirmatory analysis (testing pre-specified hypotheses) from exploratory analysis (investigating patterns that emerged from the data). Both are legitimate; the problem arises when exploratory findings are presented as if they were confirmatory, which inflates the apparent strength of the evidence.

For quantitative work, a preregistration typically specifies hypotheses, variables, sample size, and the statistical models to be used. Registries such as [OSF](https://osf.io/) and [AsPredicted](https://aspredicted.org/) provide templates and time-stamped records. For qualitative projects, preregistration is an emerging practice. The content focuses on research questions, methodological approach, and analytical framework rather than specific hypotheses and statistical tests. The [OSF qualitative preregistration template](https://osf.io/registries/) provides a starting point.

Preregistration does not lock you in. If your analysis plan changes (and it often does), you update the record and document the deviation: what you planned, what you did instead, and why. The value is in the transparency, not the rigidity.

## Documenting AI tools

If you use an AI tool at any point in the research process (transcription, translation, classification, text analysis, coding assistance), document it the same way you would document any other methodological choice. Record the tool, the model and version, the date of use, what task it performed, any relevant settings or parameters, how the output was handled (accepted, reviewed, corrected, discarded), and known limitations relevant to your data. Most of this fits in a single paragraph per use.

AI outputs should be treated as drafts that require human review, not as finished products. The [COLLECT](collect.md) and [PROCESS](process.md) stages cover this in more detail for transcription, translation, and coding.

!!! warning "Data protection and AI services"
    Cloud-based AI services typically process data on remote servers, and their terms of service may permit the provider to retain or train on your input. For personal or sensitive data, this may conflict with your GDPR obligations and your commitments to participants. Check the service's data processing terms, prefer services that offer data processing agreements and do not retain input, and consult [GDPR and legal compliance](gdpr-and-legal-compliance.md) if in doubt.

## Version control and environments

For scripted analysis, [Git](https://git-scm.com/) is the standard tool for tracking changes to code over time. It records what changed, when, and by whom, and allows you to return to any previous state. Host your repository on [GitHub](https://github.com/), [GitLab](https://about.gitlab.com/), or a CMI-hosted instance. Even if you are the only analyst on the project, Git provides a safety net and a record.

Software environments change. A script that runs today may fail in two years because a package has been updated, deprecated, or removed. For R, `renv` freezes package versions in a lockfile. For Python, `conda` or virtual environments with a `requirements.txt` serve the same purpose. For Stata, record the version number and any user-written packages in your `README.md` or `master.do`. For complex or long-lived projects, a Docker container can freeze the entire computational environment.

The effort required scales with the stakes. A short analysis for an internal report may need nothing more than a note in the README. A multi-year project producing findings for peer-reviewed publication should have a fully versioned, environment-locked workflow.

## Transparency about uncertainty

Reproducibility is not just about getting the same numbers. It is about being honest with the reader about how much confidence those numbers (or themes, or interpretations) deserve.

Report negative results. A model that shows no effect is a finding. Selective reporting, where only significant or supportive results are published, wastes the time of future researchers and distorts the evidence base. If you looked for an effect and did not find one, say so.

Report deviations from your plan. If you preregistered a design and then changed it, explain what changed and why. If you ran twenty model specifications and report the one that worked, say that too.

Report the limitations of your tools. If your automated transcription struggles with a particular language and you estimate that 10 per cent of the transcript may contain errors, that is information the reader needs. If your sample is not representative in a way that affects generalisability, state it directly rather than burying it in a footnote.

The goal is not to undermine your findings but to present them in a way that earns trust. Research that is transparent about its limitations is more credible, not less.