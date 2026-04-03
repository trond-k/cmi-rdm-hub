---
icon: lucide/flask-conical
title: "What the largest replication study means for your research"
description: "The 2026 SCORE project tested thousands of social-science claims. Half did not replicate. Here is what the findings mean for how you plan, document, and share your work."
tags:
  - Reproducibility
  - Replication
  - Open science
  - SCORE
  - Data sharing
  - Preregistration
notes: ""
date_updated: 2026-04-03
---

# What the largest replication study means for your research

*In April 2026, the SCORE programme published the most comprehensive assessment of research credibility in the social and behavioural sciences to date. Across 865 researchers, ~3,900 papers, and 11 disciplines, the results confirmed what smaller studies had suggested: roughly half of published findings do not replicate, and effect sizes shrink substantially when they do. The single strongest predictor of whether a study's results could be reproduced was whether the authors had shared their data. These findings have direct implications for how you plan, document, and share your own work.*

## What the SCORE programme found

The Systematizing Confidence in Open Research and Evidence (SCORE) programme, led by the Center for Open Science, examined papers published between 2009 and 2018 in 62 journals spanning criminology, economics, educational science, health sciences, leadership, marketing, organisational behaviour, political science, psychology, public administration, and sociology. Four coordinated studies tested three dimensions of research credibility: reproducibility, replicability, and analytical robustness.[^1]

### Replicability

Independent teams attempted to replicate 274 claims from 164 quantitative papers, using high-powered designs (median power of 99.6% to detect the original effect size), original materials where available, and peer-reviewed protocols. Only 49.3% of the papers replicated with a statistically significant result in the same direction as the original.[^2] The median effect size dropped from r = 0.25 in the originals to r = 0.10 in the replications, an 82.4% reduction in shared variance. Replication rates varied modestly across disciplines (42.5–63.1%), though some estimates carried high uncertainty.

### Reproducibility

A separate study tested whether the same data and code could reproduce the original results for 143 papers. Only 54% were precisely reproducible; 74% were at least approximately reproducible.[^3] A critical finding: just 24% of the papers in the sample had made their data and code readily available. Those that did had substantially higher reproduction rates. Data availability was, in fact, the only factor that correlated strongly with reproducibility.

### Analytical robustness

When multiple independent teams reanalysed 100 social and behavioural science studies, 34% of the reanalyses closely matched the original results and 74% reached the same overall conclusion.[^4] A focused study of 110 economics and political science papers found higher rates: 85% were computationally reproducible, and 72% of statistically significant results survived robustness checks.[^5]

### Predicting replicability

The SCORE team tested whether replicability could be predicted in advance, using AI tools, prediction markets (where researchers bet on which studies would replicate), and study characteristics. No marker stood out as reliable.[^2] Neither machine learning models nor expert forecasters could consistently distinguish studies that would replicate from those that would not. The only strong correlate was data availability.

!!! note "Not a verdict on individual studies"
    These are aggregate findings. A 49% replication rate does not mean that any particular study in the sample is wrong. Some failures to replicate reflect limitations of the replication design, not flaws in the original. The findings are a diagnostic of systemic patterns, not a scorecard for individual papers.

## What this means for CMI researchers

The SCORE results are not abstract. They speak directly to decisions you make during every phase of a research project.

**Share your data and code.** Data availability was the only factor reliably associated with reproducibility. This is not just a funder compliance issue; it is the single most effective thing you can do to make your work credible and verifiable. For guidance on how to deposit data, choose repositories, and handle sensitive material, see [PUBLISH](lifecycle-8-publish.md) and [PLAN](lifecycle-3-plan.md).

**Preregister confirmatory studies.** Preregistration separates hypothesis-testing from exploration and reduces the temptation to present post-hoc findings as planned. The SCORE findings reinforce the value of this practice. Over 300 journals now accept Registered Reports, where peer review happens before data collection and publication is guaranteed regardless of outcome.[^6] See [Reproducibility and transparency](reproducibility-and-transparency.md) for details on preregistration and Registered Reports.

**Document your analytical decisions.** When multiple teams analysed the same data, they often reached different conclusions. This underlines the importance of recording not just what you did but why: which model specifications you tried, which you chose, and what your reasoning was. For scripted work, share the code. For qualitative work, maintain analytical memos and versioned codebooks. See [ANALYSE](lifecycle-7-analyse.md) and [Reproducibility and transparency](reproducibility-and-transparency.md).

**Plan for smaller effects.** Effect sizes shrank by more than half on replication. If you are designing a quantitative study, power it for a realistic effect size, not the one reported in a single prior study. The SCORE data suggest that published effect sizes are systematically inflated.

**Recognise that qualitative research faces different challenges.** The SCORE programme tested quantitative claims. For interpretive and qualitative work, the relevant standard is not identical replication but transparency of process: can others trace how you moved from data to conclusions? The hub's guidance on [transparency in qualitative research](reproducibility-and-transparency.md#transparency-in-qualitative-and-fieldwork-based-research) addresses this directly.

## What you can do now

- **Default to sharing.** Deposit data and code in a [trustworthy archive](lifecycle-8-publish.md) unless there is a documented reason not to (participant protection, legal restriction, data sovereignty). Justify exceptions; do not treat them as the default.
- **Preregister.** Use [OSF](https://osf.io/), [AsPredicted](https://aspredicted.org/), or [EGAP](https://egap.org/registry/) for quantitative and mixed-methods work. Consider the [transparency model](reproducibility-and-transparency.md#preregistration) for qualitative studies.
- **Consider Registered Reports.** If your study tests a pre-specified hypothesis and null findings would be informative, the format eliminates publication bias by design. Over 300 journals now offer it, including *Nature* for social and behavioural research.
- **Record your decisions.** Keep a decision log or analytical memo throughout the project. This is the single cheapest investment in long-term credibility.
- **Use the hub.** The [Reproducibility and transparency](reproducibility-and-transparency.md) page covers practical implementation in detail, including tools, infrastructure, and funder expectations.

!!! tip "The SCORE collection in Nature"
    The full set of SCORE papers, editorials, and commentary is available as a curated collection: [Reliable research in the social and behavioural sciences](https://www.nature.com/collections/idajfifcfg) (*Nature*, April 2026).[^7]

[^1]: The four SCORE studies and related commentary were published in *Nature*, volume 652, issue 8108 (2 April 2026). For a news summary, see Sanderson, K. (2026). 'Half of social-science studies fail replication test in years-long project'. *Nature*. [doi:10.1038/d41586-026-00955-5](https://doi.org/10.1038/d41586-026-00955-5).
[^2]: Tyner, A. H., Abatayo, A. L., Daley, M. et al. (2026). 'Investigating the replicability of the social and behavioural sciences'. *Nature*, 652, 143–150. [doi:10.1038/s41586-025-10078-y](https://doi.org/10.1038/s41586-025-10078-y).
[^3]: 'Investigating the reproducibility of the social and behavioural sciences'. *Nature* (2026). [doi:10.1038/s41586-026-10203-5](https://doi.org/10.1038/s41586-026-10203-5).
[^4]: Aczel, B. et al. (2026). Analytical robustness study within the SCORE programme. Reported in 'Huge meta-research project puts claims in social-science papers to the test'. *Nature* (2026). [doi:10.1038/d41586-026-00805-4](https://doi.org/10.1038/d41586-026-00805-4).
[^5]: Brodeur, A. et al. (2026). 'Reproducibility and robustness of economics and political science research'. *Nature* (2026). [doi:10.1038/s41586-026-10251-x](https://doi.org/10.1038/s41586-026-10251-x).
[^6]: 'More self-reflection in research can lead to better science'. *Nature* (2 April 2026). [doi:10.1038/d41586-026-00965-3](https://doi.org/10.1038/d41586-026-00965-3). See also 'Why science has a credibility problem, and how to address it'. *Nature* (2 April 2026). [doi:10.1038/d41586-026-00972-4](https://doi.org/10.1038/d41586-026-00972-4).
[^7]: Nature collection: [Reliable research in the social and behavioural sciences](https://www.nature.com/collections/idajfifcfg) (April 2026).

!!! info "Last reviewed"
    This page was last reviewed on 3 April 2026.
