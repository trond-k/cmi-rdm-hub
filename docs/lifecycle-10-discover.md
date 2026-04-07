---
icon: lucide/search
title: "DISCOVER"
description: "Make your data findable: provide rich metadata, use persistent identifiers, and ensure that even restricted datasets are visible to those who need them."
tags:
  - Discover
  - FAIR
  - Metadata
  - Persistent identifiers
  - Sensitive data
notes: ""
date_updated: 2026-03-26
---

# DISCOVER: findability

*If nobody can find your data, it does not matter how well you documented it. Findability depends on rich metadata, persistent identifiers, and indexing infrastructure, most of which a trustworthy archive provides by design. Your most impactful contributions are choosing the right archive and describing your data thoroughly and accurately. For restricted or sensitive datasets, making the metadata openly discoverable is especially important: others should know the data exists, even when they cannot access it directly.*

## What makes data findable

A dataset is findable when a researcher who does not already know it exists can locate it through a search. This requires three things working together: metadata that describes the data in terms someone would search for, a persistent identifier that provides a stable link, and indexing that exposes the metadata to search engines, catalogues, and aggregators.

If your data sits in a trustworthy archive, the archive handles the third element. It creates a landing page, exposes machine-readable metadata to harvesters, and registers the identifier with resolvers such as [DataCite](https://datacite.org/). What the archive cannot do is describe your data for you. The metadata you provide at deposit is the single most important factor in whether someone finds your dataset or overlooks it.

## Provide rich, accurate metadata

Metadata is the description that tells others what your data contains, who created it, when, how, and under what conditions it can be accessed. The more precise and complete your metadata, the more likely your data will surface in relevant searches.

The specific metadata schema depends on the archive. The [Sikt Research Data Archive](https://sikt.no/en/tjenester/arkivering-av-forskningsdata) uses the [Data Documentation Initiative (DDI)](https://ddialliance.org/) standard, which is designed for social science data and supports detailed variable-level description, making it a natural fit for most CMI projects. Generalist repositories such as [Zenodo](https://zenodo.org/) use [DataCite](https://datacite.org/) metadata, which is broader but less granular. For projects that generate geospatial data (GPS coordinates, settlement maps, resource mapping), ISO 19115 provides a specialist standard where the repository supports it.

Regardless of the schema, the following elements matter most for findability:

- **Title.** Specific and descriptive. 'Household survey data, Kumasi, Ghana, 2024–2025' is findable; 'Project data' is not.
- **Description or abstract.** A clear summary of what the dataset contains, how it was collected, and what it covers. Include the geographic scope, the time period, and the population or subject matter.
- **Subject keywords.** Use controlled vocabularies where available (e.g., [CESSDA Topic Classification](https://vocabularies.cessda.eu/vocabulary/TopicClassification) for social science, [LCSH](https://id.loc.gov/authorities/subjects.html) for general subjects). Free-text keywords complement controlled terms but should not replace them; standardised vocabulary is what enables systematic cross-dataset discovery.
- **Creator and contributor identifiers.** Attach [ORCIDs](https://orcid.org/) to every named creator. This links the dataset to the researcher's other outputs and reduces ambiguity.
- **Temporal and geographic coverage.** State the dates and locations the data cover, not just when the deposit was made. For geospatial data, include bounding coordinates where the repository supports them.
- **Access conditions.** Make it unambiguous whether the data are open, embargoed, or restricted, and state what a potential user must do to gain access.

!!! tip "Write metadata for the searcher, not for yourself"
    You already know what your dataset contains. The person searching does not. Use terms they would type into a search box, not internal project shorthand. If the dataset covers governance in Kumasi, say 'governance' and 'Kumasi', not 'GOVTRUST WP2 output'. Think of the metadata as a shop window: it must make sense to someone passing by, not just to the shopkeeper.

## Use persistent identifiers consistently

A DOI gives your dataset a permanent, resolvable address. It ensures the dataset can be found and cited even if the repository changes its URL structure, and it enables automated linking between outputs. Trustworthy archives assign DOIs on deposit. The task here is to use them consistently.

Cite your dataset by its DOI in your publications. Link the dataset to the articles that use it, and link those articles back to the dataset. Use [ORCIDs](https://orcid.org/) for researchers and [ROR IDs](https://ror.org/) for institutions to connect outputs to the people and organisations that produced them. This network of identifiers is what makes cross-referencing work: a reader who finds your article can follow the DOI to the data; a reader who finds the data can follow the link back to the article.

!!! warning "A DOI without metadata is a dead end"
    A persistent identifier makes a dataset permanently addressable, but if the metadata behind it is sparse or inaccurate, the identifier leads to a landing page that tells the reader almost nothing. The identifier and the metadata work as a pair: the identifier gets the reader to the door, and the metadata tells them what is inside.

## Make restricted data discoverable

For CMI, where much research data is sensitive, the principle that metadata should always be open is especially important. A dataset that cannot be shared openly should still be findable. Others should know it exists, what it contains, how it was produced, and under what conditions access might be possible.

This means publishing a full metadata record even when the data itself is restricted, embargoed, or withheld entirely. The Sikt Research Data Archive supports this directly: you can deposit metadata and documentation for a restricted dataset, so that it appears in searches and catalogues, while the underlying data remain accessible only to approved users or held under embargo.

The practical value is substantial. A researcher studying local governance in West Africa who discovers that a relevant dataset exists, even under restricted access, can contact the depositor, apply for access through the archive, or design a complementary study. If the metadata had not been published, they would never have known the data were there.

!!! tip "Describe what exists, not just what is available"
    Your data availability statement in a published article should distinguish between what is openly accessible, what is restricted, and what is metadata-only. For each category, provide the DOI or a clear pointer so the reader knows where to look. See the [PUBLISH](lifecycle-8-publish.md) stage for examples.

## Multilingual metadata

CMI's research spans countries, languages, and communities where English is not the working language. Where your data were collected in a specific linguistic context, providing metadata in both English and the relevant local language improves discoverability for researchers working in either language. At minimum, include an English-language title, abstract, and keywords to ensure the dataset surfaces in international searches. Where the archive supports it, add equivalent metadata in the language of the data.

This is not a formality. A dataset documenting community governance in francophone West Africa is more likely to be found and reused by researchers in the region if the metadata includes French-language descriptions and subject terms alongside the English ones.

## What the archive handles

It is worth understanding what the archive does for you, so that you do not duplicate effort or worry about things that are already taken care of.

A trustworthy archive provides machine-readable metadata (structured for harvesting by aggregators such as [OpenAIRE](https://www.openaire.eu/), [DataCite Commons](https://commons.datacite.org/), and [Google Dataset Search](https://datasetsearch.research.google.com/)), a landing page for each dataset that is indexed by search engines, and protocols (such as OAI-PMH) that expose your metadata to catalogues and discovery services. It also ensures that identifiers resolve correctly over time.

You do not need to understand the technical details of metadata harvesting or search engine optimisation. You need to provide accurate, complete metadata at the point of deposit, and the infrastructure does the rest. If your metadata is thin, no amount of technical infrastructure will compensate.

## Findability is not a separate task

Much of what makes data findable is a by-product of other decisions: the choice of archive, the quality of metadata provided at deposit, and the consistent use of persistent identifiers. This page draws those threads together and makes the reasoning explicit. If your archive is trustworthy and your metadata is thorough, discoverability largely takes care of itself. The value of thinking about findability as a distinct concern is that it helps you check whether anything has been missed, particularly for restricted datasets where the data are hidden but the metadata should not be.

!!! info "Last reviewed"
    This page was last reviewed on 26 March 2026. Metadata standards, repository features, and discovery infrastructure evolve; verify current capabilities against the relevant documentation.