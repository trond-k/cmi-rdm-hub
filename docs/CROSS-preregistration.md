---
icon: lucide/clipboard-check
title: "Pre-registration and Registered Reports"
description: "Lodge your research design publicly before data collection to separate confirmatory from exploratory findings."
tags:
  - Preregistration
  - Registered Reports
  - Transparency
  - Reproducibility
  - Frame
  - Fund
notes: ""
date_updated: 2026-03-31
---

# Pre-registration and Registered Reports

*Pre-registration means depositing your research design, hypotheses, and analysis plan in a public registry before you collect data. It distinguishes what you set out to test from what you discovered along the way. Registered Reports take this further: a journal reviews and accepts your design before you have results. Both practices reduce publication bias, and both are increasingly expected by funders and publishers. This page explains how they work, which platforms to use, and what they look like for CMI researchers working across methods and disciplines.*

## What pre-registration does (and does not do)

Pre-registration addresses one specific problem: the temptation to present exploratory findings as if they were planned all along. When you analyse data without a prior plan, you will find patterns. Some will be real; others will be noise. Pre-registration creates a time-stamped record of what you intended to test, so that readers (and reviewers) can distinguish confirmatory analysis from exploration.

What it does not do: it does not lock you in. You can deviate from your plan. You should deviate if circumstances demand it. The requirement is that you document the deviation and explain why. A pre-registration that says 'we planned X but did Y because Z' is more transparent than no plan at all.

Pre-registration also does not substitute for good design, sound measurement, or adequate statistical power. It is one tool among several, not a guarantee of quality.

## When to pre-register

Pre-registration is most clearly valuable when your study has testable hypotheses specified before data collection. This includes:

- Randomised controlled trials and field experiments
- Survey-based hypothesis testing
- Quantitative analyses of existing datasets where the analytical strategy can be specified in advance
- Replication studies

For exploratory, inductive, or qualitative research, the picture is more nuanced. See the section on qualitative approaches below.

!!! tip "Pre-register before you see the data"
    The critical moment is before data collection or, for secondary data, before you access the dataset. A pre-registration filed after you have already explored the data offers no protection against post-hoc reasoning.

## Where to register

Several platforms serve as registries, each with a different audience and disciplinary focus.

| Platform | Disciplinary focus | Features |
|---|---|---|
| [OSF Registries](https://osf.io/registries) | All disciplines | Templates for many study types; over 800,000 registrations; links to data, code, and materials |
| [AEA RCT Registry](https://www.socialscienceregistry.org/) | Economics, development | Standard for randomised evaluations; requires pre-analysis plans for trials |
| [EGAP Registry](https://egap.org/registry/) | Governance, political science, development | Relevant for CMI's governance and political economy research |
| [AsPredicted](https://aspredicted.org/) | All disciplines | Lightweight; nine-question template; private until you choose to make it public |
| [ClinicalTrials.gov](https://clinicaltrials.gov/) | Health, clinical research | Legally required for many clinical trials; less relevant for most CMI work |

For most CMI researchers, **OSF** or **EGAP** will be the natural choice. Economists running randomised evaluations should use the **AEA RCT Registry**, which is the disciplinary standard.

!!! note "CMI researchers already using these platforms"
    Several CMI researchers have active registrations. Viola Asri has pre-registrations on OSF and the AEA RCT Registry, including trials on poverty targeting in Bangladesh and preferences in the Indian marriage market. Carlo Koos has registered cluster-randomised trials on the AEA RCT Registry studying development aid and democratisation in Sub-Saharan Africa. Charlotte Ringdal combines OSF for replication data, Harvard Dataverse for archiving, and the AEA RCT Registry for pre-analysis plans. These examples show that CMI researchers are already engaging with open science infrastructure; the question is how to make this more systematic.

## What to include in a pre-registration

The level of detail depends on the platform and study type, but at a minimum you should specify:

1. **Research questions and hypotheses.** State what you expect to find and why.
2. **Study design.** Describe the intervention (if any), the comparison conditions, and the unit of analysis.
3. **Sampling strategy.** How participants or cases will be selected, and the target sample size with a justification (e.g. power analysis).
4. **Outcome variables.** Primary and secondary outcomes, including how they will be measured.
5. **Analysis plan.** The statistical models or analytical procedures you will use, including how you will handle missing data, multiple comparisons, and covariates.
6. **Deviations protocol.** How you will report any changes to the plan.

??? example "A pre-analysis plan for a field experiment"
    A CMI researcher planning a field experiment on tax compliance in East Africa might register on the AEA RCT Registry with the following elements:

    - **Hypothesis:** Providing taxpayers with information about how revenue is spent increases voluntary compliance.
    - **Design:** Cluster-randomised at the ward level; treatment group receives information leaflets, control group does not.
    - **Sample:** 80 wards (40 treatment, 40 control), approximately 4,000 taxpayers.
    - **Primary outcome:** Tax payment rates in the six months following the intervention, measured through administrative records.
    - **Analysis:** Intent-to-treat estimation using OLS regression with ward-level clustering of standard errors.
    - **Secondary analyses:** Heterogeneity by income level, urban/rural location, and prior compliance history (labelled as exploratory).

## Registered Reports

Registered Reports are a publishing format in which a journal peer-reviews your research design (Stage 1) before you collect data, and commits to publishing the results regardless of outcome (Stage 2). The format directly addresses publication bias: studies published as Registered Reports show null results around 60 per cent of the time, compared with roughly 5 per cent in standard publications.[^1]

Over 300 journals now offer the format, including journals relevant to development research, political science, and economics. The [Registered Reports directory](https://www.cos.io/initiatives/registered-reports) maintained by the Center for Open Science lists participating journals.

### How the process works

1. **Stage 1.** You submit your introduction, literature review, research design, and analysis plan. The journal reviews this for theoretical motivation, methodological rigour, and statistical power. Reviewers may request revisions.
2. **In-Principle Acceptance (IPA).** If the Stage 1 submission passes review, the journal issues an IPA, committing to publish the final paper regardless of results, provided you follow the approved protocol.
3. **Data collection and analysis.** You carry out the study as registered, documenting any necessary deviations.
4. **Stage 2.** You submit the complete manuscript with results. The journal checks adherence to the protocol and the quality of reporting.

### When Registered Reports make sense

The format works best for **confirmatory research where null findings would be informative**. If your research question is 'does X affect Y?', and the answer 'no' would be as useful to the field as 'yes', a Registered Report protects the value of that finding.

The format adds time. Stage 1 review typically takes 6–12 months. Factor this into your project timeline, particularly for funded projects with fixed end dates.

!!! warning "Not a fit for every study"
    Registered Reports are less suited to exploratory, inductive, or iterative research designs. They also require that you can specify your design in sufficient detail before data collection. If your methodology is likely to evolve substantially during fieldwork, other transparency mechanisms (decision logs, analytical memos, preregistration with a transparency model) may be more appropriate.

## Pre-registration for qualitative research

Pre-registration was designed for hypothesis-testing research, and applying it directly to qualitative, interpretive, or participatory methods raises legitimate concerns. Committing to a fixed analytical procedure before entering the field can conflict with the iterative, emergent nature of qualitative inquiry.

The emerging solution distinguishes two models:[^2]

- **Constraining model.** Commits to specific procedures and codes in advance. This is closer to the quantitative template and may suit structured qualitative designs (e.g. framework analysis with pre-defined themes).
- **Transparency model.** Documents the starting point (research questions, initial approach, theoretical orientation) without restricting methodological emergence. The purpose is an auditable record, not a constraint.

The transparency model is gaining traction because it respects qualitative epistemology while still providing a public record of the researcher's intentions. [OSF](https://osf.io/) hosts a [qualitative preregistration template](https://osf.io/j7ghv/overview) designed specifically for this purpose.

!!! tip "Start with a transparency registration"
    If you are new to pre-registration and work with qualitative or mixed methods, a transparency registration on OSF is a low-cost way to begin. It documents your starting point without requiring you to predict where the analysis will lead.

## What funders expect

No major funder currently mandates pre-registration for non-clinical research, but the direction is clear:

- **Horizon Europe** encourages pre-registration and open research practices.
- **Research Council of Norway** encourages pre-registration as part of its open science policy.
- **ERC** encourages pre-registration but does not require it.
- **NIH** requires registration for clinical trials but not for other study types.

Pre-registration is increasingly mentioned in funder guidance as good practice. Even where it is not required, reviewers may view it favourably as evidence of methodological rigour.

For a fuller overview of funder requirements, see the [FUND](lifecycle-2-fund.md) stage and the [reproducibility and transparency](reproducibility-and-transparency.md) page.

[^1]: Scheel, A.M. et al. (2021). [An excess of positive results](https://doi.org/10.1177/25152459211007467). *Advances in Methods and Practices in Psychological Science*.
[^2]: Haven, T. & Van Grootel, L. [Preregistration template for qualitative studies](https://osf.io/j7ghv/overview), OSF Registries.

!!! info "Last reviewed"
    This page was last reviewed on 31 March 2026. Registry platforms, journal participation, and funder policies are evolving; verify against the latest source.
