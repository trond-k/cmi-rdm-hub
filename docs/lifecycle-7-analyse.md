---
icon: lucide/microscope
title: "ANALYSE"
description: "Generate findings from your processed data: choose methods deliberately, document every analytical decision, and ensure that you can reproduce your own work."
tags:
  - Analyse
  - Reproducibility
  - Transparency
  - Documentation
notes: ""
date_updated: 2026-03-26
---

# ANALYSE: data analysis and interpretation

*Reproducibility starts with the analyst, not the reader. If you cannot reproduce your own work six months from now, nobody else will be able to either. This stage is where processed data becomes findings, and where the quality of your documentation determines whether those findings can be scrutinised, verified, and built upon. Document decisions, not just results.*

## Choose methods deliberately

The analytical methods you use should follow from your research questions and the nature of your data, not from habit or convenience. This sounds obvious, but in practice the choice of method is often shaped more by what software the researcher already knows than by what the data requires.

For quantitative work, specify your statistical approach before you begin. If you preregistered an analysis plan at the [PLAN](plan.md) stage, follow it; if you deviate, document the deviation and the reason. For qualitative work, name your analytical framework (thematic analysis, grounded theory, discourse analysis, process tracing, or whatever fits) and be explicit about how it guides your engagement with the data. For mixed-methods projects, describe how the qualitative and quantitative components relate to each other: do they converge on the same questions, or do they address different aspects of the problem?

Whatever your approach, the tools you use to implement it should be recorded. Note the software (including version numbers), any packages or libraries, and relevant settings or parameters. This is not bureaucracy; it is the minimum needed for someone (including your future self) to understand how the findings were produced. See [Reproducibility and transparency](reproducibility-and-transparency.md) for broader guidance.

## Document analytical decisions, not just outputs

The most common documentation gap in research is not missing data or missing code. It is missing reasoning. A table of regression coefficients tells the reader what the results are; it does not explain why you chose that specification, how you handled collinearity, or what happened when you tried a different model. A thematic map shows the final coding structure; it does not explain why you merged two codes, split another, or dropped a theme that did not hold up.

Keep an analytical notebook, decision log, or memo trail alongside your analysis. For each consequential decision, record what you did, what alternatives you considered, and why you chose the path you did. This serves three purposes: it makes your analysis reproducible, it provides material for the methods section of your publications, and it protects you if your findings are questioned.

!!! tip "Write the memo when you make the decision"
    Analytical reasoning fades quickly. If you decide to exclude a variable, merge two coding categories, or change a model specification, write down why at the moment you do it. A one-paragraph memo written today is worth more than a half-remembered reconstruction six months later.

## Qualitative analysis

Qualitative analysis involves interpretive judgement in ways that quantitative work does not, and this makes documentation both more difficult and more important. The fact that two competent researchers might code the same transcript differently is not a flaw; it is intrinsic to the method. What matters is that your coding decisions are traceable and your reasoning is visible.

If you are working with a coding framework, maintain a codebook that evolves alongside the analysis. For each code, record a definition, inclusion and exclusion criteria, and examples. If your codes change during the process (as they should in most inductive approaches), version the codebook so you can see how your categories developed. If multiple researchers are coding the same material, establish a procedure for comparing coding, discussing disagreements, and reaching resolution. Inter-coder agreement does not need to be perfect, but the process should be documented.

Analytical memos are the qualitative equivalent of a lab notebook. Use them to record emerging patterns, surprising findings, contradictions, and your own reflexive responses to the material. These memos are not published, but they are the audit trail that connects your raw data to your conclusions.

## Reproducibility in practice

The gold standard for quantitative reproducibility is a scripted workflow that takes your processed data and produces your results without manual intervention. Version your code in Git. Record the software environment: which version of R, Python, or Stata you used, which packages, and which operating system. Tools such as `renv` (R), `conda` (Python), or Docker containers can freeze the environment so that someone can reconstruct it later.

Computational notebooks (Jupyter, R Markdown, Quarto) combine code, output, and narrative in a single document. They are useful for both exploratory analysis and for producing reproducible reports, but they require discipline: a notebook that runs out of order, or that depends on objects created in cells that have since been deleted, is worse than useless. If you use notebooks, make sure they execute cleanly from top to bottom.

Not all analysis can be scripted. Qualitative coding, visual interpretation of images, and expert judgement calls resist automation. Where manual steps are unavoidable, document them as described above. The goal is not to eliminate human judgement but to make it visible.

??? example "A minimal reproducibility setup"
    A project using Stata for quantitative analysis might organise its analytical workflow as follows:

    ```text
    analysis/
    ├── scripts/
    │   ├── 01_descriptives.do
    │   ├── 02_main_models.do
    │   └── 03_robustness_checks.do
    ├── output/
    │   ├── tables/
    │   └── figures/
    ├── master.do           ← runs all scripts in order
    ├── README.md           ← how to run the analysis
    └── decision_log.md     ← why you made the choices you made
    ```

    The `master.do` file sets paths and runs each do-file in sequence, so the full analysis can be reproduced with a single command. The `README.md` records the Stata version, any required user-written packages (and where to install them), and any external dependencies. The `decision_log.md` captures the reasoning behind analytical choices. Anyone with access to the processed data and this folder should be able to reproduce the results.

## Collaborative analysis

Multi-researcher analysis raises coordination questions that solo work does not. If two people are coding the same dataset, they need shared definitions. If three people are running models on different subsets, they need consistent variable handling. If a team spans multiple institutions and time zones, they need a shared workspace.

Agree on conventions before the analysis begins: shared codebooks, common variable names, a single authoritative version of the processed data, and a clear division of labour. Use version control (Git for code, tracked changes or versioned documents for qualitative memos) so that everyone can see what has changed and why. If the analysis involves iterative cycles (common in mixed-methods and grounded-theory work), schedule regular check-ins to reconcile interpretations and update shared documents.

!!! warning "One authoritative copy of the data"
    If team members are each working from their own copy of the dataset, it is only a matter of time before the copies diverge. Keep one authoritative version in a shared location, and have all analysis scripts point to it. If someone needs a modified version for a specific analytical task, create a clearly labelled derived file and document the modification.

## Validate and stress-test your findings

Findings that only hold under one set of assumptions, one model specification, or one coding decision are fragile. Build validation into the analysis rather than treating it as an afterthought.

For quantitative work, this means robustness checks: alternative model specifications, different operationalisations of key variables, sensitivity to outlier removal, cross-validation where appropriate. Report these alongside your main results, not as an afterthought buried in a supplementary file.

For qualitative work, validation takes different forms: triangulation across data sources or methods, searching for disconfirming evidence, checking your interpretations against the perspectives of participants or collaborators, and examining whether your conclusions hold across different segments of the data.

In both cases, the question is the same: would your conclusions survive a different reasonable set of choices? If not, that does not necessarily mean the findings are wrong, but it does mean the uncertainty should be reported honestly.

## Research integrity and transparency

If you preregistered an analysis plan at the [PLAN](plan.md) stage, follow it. If you deviate (and most projects do, to some extent), document the deviation clearly: what you planned, what you did instead, and why. Distinguish confirmatory analysis (testing pre-specified hypotheses) from exploratory analysis (investigating patterns that emerged from the data). Both are legitimate; presenting exploratory findings as if they were confirmatory is not.

Report negative results and null findings. A model that shows no effect is a finding, not a failure. Selective reporting, where only significant or supportive results are presented, distorts the evidence base and wastes the effort of future researchers who will not know that a particular approach has already been tried.

Where AI tools have been used in the analysis (classification, pattern detection, text analysis, or any other application), document what was used, how, and with what limitations. Record the tool, the model version, the parameters, and the extent of human review applied to the output. Do not treat AI-generated results as unmediated findings; they are inputs that require the same critical scrutiny as any other analytical output. See [Reproducibility and transparency](reproducibility-and-transparency.md) for detailed guidance on documenting AI use.