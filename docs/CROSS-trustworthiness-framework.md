---
icon: lucide/shield-check
title: "Trustworthiness is earned, not claimed"
description: "A February 2026 PNAS paper by Nosek and colleagues sets out seven pillars of research trustworthiness. Here is what the framework proposes and how it maps onto the decisions you make across the research lifecycle."
tags:
  - Research integrity
  - Trustworthiness
  - Open science
  - Research assessment
  - CoARA
notes: "Khrono article author could not be confirmed at time of writing (site returned HTTP 403). Update footnote 2 with author name(s) when available."
date_updated: 2026-04-06
---

# Trustworthiness is earned, not claimed

*Published 6 April 2026*

*In February 2026, a team led by Brian Nosek published a framework for assessing the trustworthiness of scientific research findings in the Proceedings of the National Academy of Sciences. The paper identifies seven pillars of trustworthiness, organised across three levels: the research itself, the researchers, and the organisations that fund and evaluate them. A Norwegian commentary in Khrono read the framework as evidence that the research credibility crisis is solvable, provided incentives shift from counting publications to rewarding concrete trustworthiness behaviours. The framework gives practical language for what you already do, or should do, when you plan, document, and share your work.*

## What the framework proposes

In early 2026, six researchers from the Center for Open Science, the National Academies of Sciences, Engineering, and Medicine, and four US universities published a systems-level framework for evaluating whether scientific findings deserve trust.[^1] Their central argument is that trustworthiness is not the same as correctness. A finding can be trustworthy and still turn out to be wrong. What matters is whether the research was produced and evaluated in ways that make errors detectable and correction possible over time.

The paper proposes seven distinct pillars. Together they describe a set of behaviours and conditions, not a personality trait or institutional badge.

- **Accountability.** The researchers are identifiable and answerable for their work. Authorship is transparent, conflicts of interest are disclosed, and ethics approvals and consent are documented.
- **Evaluability.** Enough material is shared (data, code, methods, protocols) that others can check the claims against the evidence.
- **Evaluation.** The work has actually been examined by others through peer review, reanalysis, replication, or structured critique.
- **Formulation quality.** The research question, study design, and outcome measures are well-posed for the claim being made.
- **Bias control.** Recognised biases (confirmation bias, selection bias, publication bias, analytical flexibility) are identified and addressed in the design and analysis.
- **Error reduction.** Appropriate practices are in place for detecting and correcting mistakes in data, code, and reasoning.
- **Calibration.** The strength of the claim matches the strength of the evidence. Conclusions are proportionate to what the design can support.

!!! note "Three levels, not just individual researchers"
    The paper locates these pillars at three levels: the research itself, the researchers conducting and evaluating it, and the organisations (universities, journals, funders) that set the incentives. Trustworthiness does not rest on researcher virtue alone. If institutional incentives reward volume over rigour, individual good practice will always swim against the current.

## The Norwegian response

On 20 February 2026, Khrono, the Norwegian higher-education newspaper, published a commentary titled *En løsbar forskningskrise* ("A solvable research crisis").[^2] The piece argued that billions of kroner are spent on research that is poorly designed, never published, or selectively reported in ways that make findings unusable, and that the Nosek framework gives the sector both the language and the map it needs to distinguish good research from bad.

The commentary linked the PNAS framework to ongoing European reform efforts, in particular CoARA (Coalition for Advancing Research Assessment), which brings together universities and research institutions committed to replacing counting metrics and journal rankings with more meaningful quality indicators.[^5] Where CoARA addresses *how we assess researchers*, the Nosek framework addresses *what we should actually look for in the research itself*. The Khrono author argued that this combination makes the crisis solvable: not through trust ("trust me") but through demonstration ("show me").

The commentary also highlighted Registered Reports, a publication format where peer review happens before data collection and results are published regardless of outcome, as a concrete example of how the system can be restructured to favour trustworthiness over novelty.[^1]

## What this means for your project

Each pillar maps directly onto decisions you make during the research lifecycle. You do not need to adopt a new framework; you need to recognise the one you are already working within.

- **Accountability:** document roles, consent, and ethics approvals early. See [FRAME](lifecycle-1-frame.md) and [Informed consent and information letters](CROSS-ethics.md).
- **Evaluability:** share data, code, and protocols by default. See [PUBLISH](lifecycle-8-publish.md), [PLAN](lifecycle-3-plan.md), and [Reproducibility and transparency](reproducibility-and-transparency.md).
- **Bias control and formulation:** preregister confirmatory studies, or where relevant submit a Registered Report. See the [preregistration section](reproducibility-and-transparency.md#preregistration) of the reproducibility page.
- **Error reduction:** use version control, maintain analytical memos, and test your code. See [ANALYSE](lifecycle-7-analyse.md) and [Reproducibility and transparency](reproducibility-and-transparency.md).
- **Calibration:** write conclusions that match what your design can support. Avoid over-claiming from small, exploratory, or qualitative samples.
- **Evaluation:** invite critique early through internal review, working-paper venues, or peer feedback rather than leaving it entirely to post-publication review.

## Limits of the framework

The framework is a map, not a score. The authors acknowledge that indicators differ across disciplines, and that not every pillar applies with equal force to every type of research. Applying all seven pillars uniformly to interpretive or qualitative work would be a category error; the underlying principles of process transparency and calibrated claims still hold, but the specific indicators look different. For guidance on transparency in qualitative and fieldwork-based research, see the [relevant section](reproducibility-and-transparency.md#transparency-in-qualitative-and-fieldwork-based-research) of the reproducibility page.

Norwegian and European reform efforts such as CoARA and DORA (San Francisco Declaration on Research Assessment) provide the institutional scaffolding for change.[^5] The Nosek framework provides the evaluative content: a shared vocabulary for what trustworthy research actually looks like in practice.

## What you can do now

- Default to sharing data and code unless there is a documented reason not to (participant protection, legal restriction, data sovereignty).
- Preregister confirmatory analyses using [OSF](https://osf.io/), [AsPredicted](https://aspredicted.org/), or [EGAP](https://egap.org/registry/).
- Keep a decision log or analytical memo throughout the project.
- Calibrate your abstracts, conclusions, and any public-facing language to the actual evidence.
- Invite an internal reader or critical friend before submission.

!!! tip "Companion reading"
    This page complements [Half of findings do not replicate](CROSS-replication-evidence.md), which covers the April 2026 Systematizing Confidence in Open Research and Evidence (SCORE) findings on what goes wrong when trustworthiness practices are absent. Together, they make the case that the problem is well-documented and the solutions are within reach.

[^1]: Nosek, B. A., Allison, D. B., Jamieson, K. H., McNutt, M., Nielsen, A. B. & Wolf, S. M. (2026). 'A framework for assessing the trustworthiness of scientific research findings'. *Proceedings of the National Academy of Sciences*, 123(6), e2536736123. [doi:10.1073/pnas.2536736123](https://doi.org/10.1073/pnas.2536736123).
[^2]: 'En løsbar forskningskrise'. *Khrono* (20 February 2026). [https://www.khrono.no/en-losbar-forskningskrise/1038842](https://www.khrono.no/en-losbar-forskningskrise/1038842).
[^5]: CoARA (Coalition for Advancing Research Assessment). [https://coara.eu/](https://coara.eu/). See also the San Francisco Declaration on Research Assessment (DORA): [https://sfdora.org/](https://sfdora.org/).
