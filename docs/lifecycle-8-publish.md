---
icon: lucide/upload
title: "PUBLISH"
description: "Make your data, code, and outputs formally citable through trustworthy archives: choose the right repository, provide rich metadata, and link everything together."
tags:
  - Publish
  - FAIR
  - Archives
  - DOI
  - Data citation
  - Open access
notes: ""
date_updated: 2026-03-26
---

# PUBLISH: formal dissemination of data and outputs

*Publishing research data is not the same as uploading files. It means depositing well-documented datasets in trustworthy archives that assign persistent identifiers, enforce metadata standards, and provide access controls and long-term preservation by design. The single most impactful decision you make for the findability, accessibility, and longevity of your data is where you deposit it. Get that right, provide rich metadata, and the archive does much of the rest.*

## Choose the right archive

A trustworthy archive is one that commits to long-term stewardship: it assigns persistent identifiers, curates metadata, migrates formats, enforces access controls, and remains operational independently of any single funder or project. Certification schemes such as [CoreTrustSeal](https://www.coretrustseal.org/ "A certification for trustworthy data repositories") provide a formal benchmark, but the practical test is simpler. Does the repository assign DOIs? Does it require structured metadata? Does it support access restrictions where needed? Will it still exist in ten years?

For most CMI projects, the default choice is the [Sikt Research Data Archive](https://sikt.no/en/tjenester/arkivering-av-forskningsdata), which provides curation support, handles sensitive data under Norwegian and EU frameworks, and meets funder requirements for the Research Council of Norway and Horizon Europe. For projects that need a generalist alternative, [Zenodo](https://zenodo.org/) and the [Open Science Framework (OSF)](https://osf.io/) accept all data types and assign DOIs on deposit.

Code and scripts belong in a version-controlled repository such as [GitHub](https://github.com/) or [GitLab](https://about.gitlab.com/), with a snapshot archived in Zenodo to generate a citable DOI. Articles and other text outputs should be registered in [NVA (Nasjonalt vitenarkiv)](https://sikt.no/en/tjenester/nasjonalt-vitenarkiv-nva), Norway's national research output archive.

!!! tip "One decision, many benefits"
    Choosing a trustworthy archive is not just about compliance. It gives you persistent identifiers, standardised metadata, access controls, preservation, and discoverability in a single step. Much of what the FAIR principles require is handled by the archive itself. Your most important contributions are selecting the right repository for each dataset and providing thorough, accurate metadata and documentation.

## Prepare your deposit

A deposit is only as useful as the documentation that accompanies it. Before uploading, check that your package includes:

- The dataset itself, in open, preservation-friendly formats where possible (CSV rather than Excel, PDF/A rather than Word). See the [PROCESS](lifecycle-6-process.md) stage for format conversion guidance.
- A codebook or data dictionary describing every variable, its values, units, and coding scheme.
- A README file explaining what the dataset contains, how it was collected, what processing was applied, and any known limitations.
- Scripts or code used to produce derived datasets or results, with documentation of the software environment.
- Any supplementary materials needed for interpretation: interview guides, survey instruments, sampling documentation.

Archives vary in what they require and what they accept. Check the repository's deposit guidelines before packaging your data. Sikt, for instance, provides curation support and will work with you on metadata and documentation; Zenodo accepts deposits with minimal review but places more responsibility on the depositor to get things right.

!!! warning "Do not deposit and forget"
    Depositing data is not the end of your responsibility. If you discover an error after publication, most repositories support versioning and corrections. If access conditions need to change (an embargo expires, a restriction is no longer justified), update the record. A deposit that is never maintained becomes misleading.

## Assign persistent identifiers and cite data properly

A Digital Object Identifier (DOI) makes your dataset permanently findable and citable, regardless of where it moves. Trustworthy archives assign DOIs automatically on deposit. If you are archiving code through Zenodo's GitHub integration, the DOI is generated when you create a release.

Use DOIs consistently. Cite your own data in your publications, just as you would cite someone else's. Follow the [FORCE11 data citation principles](https://force11.org/info/joint-declaration-of-data-citation-principles-final/ "Joint Declaration of Data Citation Principles"): include the creator, title, year, repository, and identifier. Link datasets to the articles that use them, and link articles back to the datasets. This bidirectional linking is what makes the relationship between outputs visible to readers, indexers, and funders.

Beyond DOIs for datasets, use [ORCIDs](https://orcid.org/) for researchers and [ROR IDs](https://ror.org/) for institutions. These identifiers connect your outputs to the people and organisations that produced them, reducing ambiguity and ensuring credit flows to the right place.

## Write a clear data availability statement

Most journals now require a data availability statement in published articles. This is not a formality; it is the point at which a reader learns whether they can access your data, where it is, and what conditions apply.

A good statement is specific. It names the repository, provides the DOI or accession number, and states the access conditions. If the data are restricted, it explains why and describes what is available instead (metadata, summary statistics, anonymised subsets). If different datasets have different access levels, the statement should distinguish them.

=== "Open access"

    The dataset supporting this study is available in the Sikt Research Data Archive at https://doi.org/10.xxxxx. The data are released under a CC BY 4.0 licence.

=== "Restricted access"

    Interview transcripts are deposited in the Sikt Research Data Archive at https://doi.org/10.xxxxx with restricted access to protect participant confidentiality. Access is available to qualified researchers on application to the archive. Survey data are available without restriction at the same DOI.

=== "Data not available"

    The data supporting this study cannot be made publicly available because they contain sensitive personal information collected under conditions of confidentiality in a conflict-affected setting. Metadata describing the dataset are available at https://doi.org/10.xxxxx. Enquiries about access may be directed to the corresponding author.

!!! warning "Do not promise what you cannot deliver"
    If your data availability statement says the data are openly available and they are not, you have a problem with both the journal and the funder. If restrictions apply, state them honestly. It is far better to publish a clear, justified restriction than to claim openness and fail to provide it.

## Reproducibility packages

For quantitative and computational work, consider publishing a reproducibility package alongside the article: a bundled deposit containing the data, code, and documentation needed for an independent researcher to reproduce your results. At minimum, this includes the analysis scripts, the input data (or a pointer to it, if the data are restricted), a description of the software environment, and instructions for running the code.

For qualitative and mixed-methods work, full computational reproducibility is rarely possible or appropriate. The equivalent is thorough documentation: a clear account of the analytical process, the coding framework, and the relationship between evidence and interpretation. What matters is that another researcher can understand what you did, assess your reasoning, and build on your work, even if they cannot press a button and regenerate your output.

## Finalise the data inventory

Update the [data inventory](data-inventory.md) with publication details for each dataset: repository, persistent identifier, access conditions, embargo timelines, and licence. For datasets not deposited, record the rationale.