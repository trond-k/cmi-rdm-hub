# Research Report: Reproducibility and Transparency

**Purpose:** Feed into a revised draft of `reproducibility-and-transparency.md`
**Date:** 2026-03-26
**Scope:** Recent developments (2024–2026), CMI relevance, gap analysis against current draft

---

## 1. Gap Analysis: Current Draft vs. What's Missing

The current page is well-structured and clearly written. It covers preregistration, AI documentation, version control/environments, and transparency about uncertainty. However, several significant gaps and opportunities for improvement emerge from the research.

### Gaps

| Area | Current state | What's missing |
|---|---|---|
| **AI governance** | One paragraph on documentation + GDPR warning box | Publisher policies now converging (Nature, Elsevier, Wiley, COPE, ICMJE); EU AI Act implications; EDPB Opinion 28/2024 on AI and personal data; documented hallucination cases (100+ at NeurIPS 2025); Norwegian-specific guidance (Datatilsynet NTNU/Copilot sandbox finding that DPIA is required) |
| **Preregistration** | Good basics, mentions OSF and AsPredicted | Qualitative preregistration debate has matured significantly; the "transparency model" vs. "constraining model" distinction is now important; adoption stats available (800K+ registrations on OSF); criticisms are more sophisticated (strategic ambiguity, quality concerns); EGAP registry relevant for CMI's development research |
| **Registered Reports** | Not mentioned | Over 300 journals now offer the format; dramatically higher null-result rates (~60% vs ~5%); strongest mechanism against publication bias; directly relevant as a publishing strategy for CMI researchers |
| **Equity and Global South** | Not mentioned | Central to CMI's mission; tension between transparency mandates and participant protection; CARE principles and data sovereignty; WEIRD bias in reproducibility standards; language barriers; parachute research; qualitative transparency alternatives (APSA QTD framework) |
| **Reproducibility crisis context** | Not mentioned | Provides motivation — researchers need to know *why* this matters now; Gino/Ariely scandals; I4R systematic replications; Protzko et al. finding that well-powered preregistered studies replicate at ~85–90% |
| **Norwegian infrastructure** | Mentions Git, GitHub, GitLab | NVA fully launched (replacing Cristin + 67 repos); next-gen NIRD Research Data Archive (Sigma2, CKAN-powered); CodeRefinery Phase 4 funded (2025–2028); Nordic-RSE community; Sikt CoreTrustSeal certification |
| **Funder requirements** | Not mentioned | Horizon Europe requires FAIR data, immediate OA, DMPs; RCN aligned with Plan S; Nelson Memo (US); convergence across funders on reproducibility expectations |
| **Research assessment reform** | Not mentioned | DORA (25,000 signatories); CoARA (837 signatories, 18 national chapters); shift from journal prestige to research quality — directly affects incentives for reproducibility practices |
| **Transparency standards and frameworks** | Not mentioned | TOP Guidelines 2025 major update; TIER Protocol 4.0; CRediT taxonomy; CODECHECK; these give structure to what "being transparent" actually means in practice |
| **Tools landscape** | Mentions renv, conda, Docker, Git | Quarto 1.4+ manuscript project type now dominant; Code Ocean v4; targets package (R); CITATION.cff + Software Heritage (SWHID now ISO standard); mybinder.org sustainability concerns; GitHub Codespaces for reproducible environments |
| **Qualitative reproducibility** | Mentioned briefly | Deserves more space given CMI's methods profile; distinction between reproducibility and transparency for interpretive work; analytical memos, codebook versioning, active citation, annotated appendices |
| **Collaborative reproducibility** | Not mentioned | Multi-site, multi-institution projects (common at CMI); shared codebooks, one authoritative data copy, coordination conventions |

### What the Current Draft Does Well

- Clear, accessible prose without jargon overload
- The "bus test" framing is effective and memorable
- Good structure: what/how/why for documentation
- GDPR warning box on AI tools is well-placed
- Practical about scaling effort to stakes
- Does not oversell reproducibility or make it sound like bureaucracy

---

## 2. Recent Developments by Topic

### 2.1 The Reproducibility Landscape (2024–2026)

**The crisis is becoming a reform movement.** The discourse has shifted from diagnosing problems to implementing solutions. Key developments:

- **I4R (Institute for Replication):** Systematic replication of economics papers finds ~60–70% computationally reproducible, but robustness to alternative analytical choices is considerably lower.
- **Protzko et al. (2024, Nature Human Behaviour):** Well-powered, preregistered studies replicate at ~85–90%. The crisis is solvable through better practices.
- **Francesca Gino case (2023–ongoing):** Harvard Business School — Data Colada identified data fabrication in multiple papers. Gino sued Harvard and the whistleblowers. Ongoing legal proceedings through 2025. Major public attention.
- **Dan Ariely (Duke):** Continued scrutiny of work flagged by Data Colada.
- **Paper mills:** Wiley retracted 11,300+ Hindawi articles and shut 19 journals (2024). SAGE journal retracted 1,500+ papers. LLMs making detection harder.
- **Retraction wave:** Annual retractions climbing globally; AI-generated content now a significant driver.

**Implication for CMI:** Researchers need to understand *why* these practices matter — not as bureaucracy but as a response to documented, systemic problems in how research is conducted and reported.

### 2.2 AI Governance in Research

**Publisher consensus has crystallised (2024–2025):**

| Publisher | AI authorship | Disclosure requirement | Images |
|---|---|---|---|
| Nature/Springer | Prohibited | Methods section for generative use | Caution |
| Elsevier | Prohibited | Mandatory disclosure statement at submission | Prohibited except specific research |
| Wiley | Prohibited | Methods or Acknowledgements, "transparent and detailed" | Not addressed |
| Taylor & Francis | Prohibited | Required | Prohibited for generative creation |
| SAGE | Prohibited | Required for "generative" tier; not for "assistive" | Not addressed |

**Cross-publisher bodies:**
- **COPE:** AI cannot be listed as author; disclosure in Materials and Methods
- **ICMJE (updated Jan 2024):** No AI authorship; AI disclosure required at submission

**EU AI Act (entered into force 1 Aug 2024):**
- Research exemption exists but is narrower than it appears — applies to "development or use solely for scientific research," but the boundary between research and deployment is fuzzy
- AI literacy obligation (Article 4) applied since Feb 2025
- Norwegian AI Act incorporating EU regulation in consultation (closed Sep 2025), expected mid-2026
- Nkom proposed as Norwegian supervisory authority

**EDPB Opinion 28/2024 (Dec 2024):**
- LLMs "rarely achieve anonymisation standards" — models trained on personal data remain personal data processing
- Legitimate interest as legal basis faces a high bar
- AI models developed with unlawfully processed data may taint deployment lawfulness

**Datatilsynet NTNU/Copilot sandbox (Nov 2024):**
- NTNU found "not yet ready" for org-wide M365 Copilot deployment
- DPIA required when generative AI processes personal data
- Key issue: information governance and access controls must be in order first

**Italian Garante fined OpenAI EUR 15M (Dec 2024):**
- No lawful basis for training on personal data
- Failure to notify March 2023 data breach
- Lack of transparency, no age verification

**Hallucinated references are not hypothetical:**
- GPTZero audit of NeurIPS 2025: 100+ confirmed hallucinated citations across 51 accepted papers
- ICLR 2026 submissions: 50+ hallucinated citations found
- Legal sector: lawyers sanctioned for submitting AI-generated fake case citations

**Implication for CMI:** The current page's single paragraph on AI documentation is insufficient. This topic needs its own substantial section covering: (1) what to document, (2) publisher requirements, (3) GDPR/data protection, (4) specific risks (hallucination, bias, data leakage), and (5) the institutional requirement for DPIAs when processing personal data with AI tools.

**Emerging documentation minimum (synthesised across COPE, ICMJE, Wiley, Elsevier, Nature, AMEE Guide 192):**

For each AI use in a research project, record:
1. Tool name, model version, and date of use
2. Task performed (transcription, translation, coding, drafting, analysis)
3. Input description (and whether personal data was involved)
4. Relevant parameters/settings
5. How output was handled (accepted / reviewed and corrected / discarded)
6. Verification method applied
7. Known limitations relevant to the data or task
8. Whether a DPA was in place (if personal data involved)

### 2.3 Preregistration

**Adoption stats:** OSF Registries surpassed 800,000 registrations. Psychology leads non-clinical fields; development economics well-served by AEA Registry and EGAP.

**Qualitative preregistration debate has matured:**
- Two models: "constraining" (commits to specific plan) vs. "transparency" (documents starting point without constraining emergence). The transparency model is gaining traction for qualitative work.
- Haven & Van Grootel's qualitative preregistration template on OSF asks for epistemological stance, methodology, sampling strategy, and analytical approach — while acknowledging iterative nature.
- Levitt et al. (2021, American Psychologist) argue "methodological integrity" is a better framework than preregistration for qualitative research.
- No widely adopted mixed-methods preregistration template exists yet.

**Criticisms are more sophisticated:**
- Quality problem: many preregistrations are too vague to serve their purpose (Hardcastle et al., 2023)
- Strategic ambiguity: deliberately vague preregistrations that appear transparent but preserve flexibility (Van den Akker et al., 2023)
- Limited scope: addresses only one threat (HARKing/outcome switching), not measurement, design, or theory problems (Szollosi et al., 2020)
- Burden without proportionate benefit for exploratory/descriptive studies
- Mismatch with post-positivist epistemologies

**Registered Reports (300+ journals):**
- Dramatically higher null/negative result rate (~60% vs ~5% in standard papers) — strongest evidence they reduce publication bias
- Journals: Nature Human Behaviour, PLOS ONE, Cortex, Royal Society Open Science, Political Analysis
- Challenges: slow (adds 6–12 months), low submission rates, better for confirmatory than exploratory research
- Peer Community In Registered Reports (PCI-RR) offers journal-independent peer review

**Funder position:** No major funder broadly mandates preregistration for non-clinical research. Horizon Europe and RCN encourage but do not require it. Push comes more from journals than funders.

**Development research relevance (EGAP):**
- EGAP registry prominent for governance and political science field experiments in Global South
- AEA Registry dominant for development economics RCTs
- 3ie/RIDIE for impact evaluations
- Tension: preregistration can entrench Northern-designed studies conducted in the South without local input, but can also make research agendas transparent to Southern partners

**Implication for CMI:** The preregistration section should (1) note the qualitative debate and the transparency model, (2) mention EGAP alongside OSF/AsPredicted as relevant for CMI's research profile, (3) address Registered Reports as a distinct publishing strategy, and (4) be honest about limitations and criticisms.

### 2.4 Transparency Standards and Frameworks

**TOP Guidelines 2025 — major update (first since 2015):**
- Three types: Research Practices, Verification Practices, Verification Studies
- Seven Research Practices: study registration, study protocol, analysis plan, materials sharing, data sharing, analytic code sharing, reporting transparency
- Three levels: Disclosure → Sharing and Citation → Independent Certification
- Preprint: https://osf.io/preprints/metaarxiv/nmfs6

**TIER Protocol 4.0:** Advanced guidance on folder structure and relative paths for portable, replicable projects.

**Research assessment reform:**
- DORA: 25,000 signatories (May 2024), 1,500+ institutions, 159 countries
- CoARA: 837 signatories (May 2025), 18 national chapters, cascade funding for reform projects
- Both push away from journal impact factor toward assessing actual research quality — creating incentive space for reproducibility practices

**COS 2025 metrics:** 47% increase in OSF users engaging with lifecycle open science actions; 138,943 new public outputs added.

**CODECHECK:** Community-driven independent verification of computational results. Several journals adopted/piloted CODECHECK workflows by 2024.

### 2.5 Tools and Infrastructure

**Quarto (Posit):**
- Now dominant for reproducible scientific publishing (succeeding R Markdown)
- Quarto 1.4 (2024): dedicated manuscript project type, dashboards, Typst support
- Quarto 1.8 (2025): improved brand support, HTML accessibility
- Produces LaTeX, Word, HTML from single source with companion manuscript website
- Journal-specific submission templates

**Code Ocean v4 "Trusted Agents" (2025):**
- Lineage Graph showing full provenance of results
- Pipeline builder generating Nextflow
- Free Open Science Workbench for authors at Nature, IEEE, Elsevier

**Software Heritage:**
- SWHID became international standard ISO/IEC 18670 (April 2025)
- Recognised as Digital Public Good (January 2026)
- 27 billion unique source files from 421 million projects

**CITATION.cff:** GitHub renders citation info; Zenodo populates metadata from it; Software Heritage indexes it.

**mybinder.org:** Funding crisis after Google sponsorship ended (2023); shifted to federated model; sustainability fragile.

**Norwegian infrastructure:**
- NVA fully launched (replacing Cristin + 67 institutional repositories) — single platform for registering and sharing research outputs
- Next-gen NIRD Research Data Archive (Sigma2, CKAN-powered, DOI minting, enhanced metadata, FAIR features) — Norway's largest archive for scientific data
- Sikt Research Data Archive: CoreTrustSeal-certified, agreement with National Archives of Norway
- CodeRefinery Phase 4 funded (2025–2028) with partners including NTNU and Sigma2
- Nordic code repository hosting: nordic-gitlab.deic.dk (free for Nordic researchers)
- Nordic-RSE 2026 conference in Tromsø (June 9–10)

**Implication for CMI:** The tools section should be updated to mention Quarto (researchers using R/Python), CodeRefinery as a training resource, and the Norwegian infrastructure developments. The Docker/containerisation recommendation remains appropriate for complex projects but should be positioned as the high end of a spectrum.

### 2.6 Equity, Global South, and Development Research Contexts

This is the most significant gap in the current draft given CMI's mission and research profile.

**Core tension: transparency mandates vs. participant protection**
- Development research often involves politically sensitive topics, vulnerable populations, and contexts where data sharing could enable harm
- Anonymisation limits: in small communities (common in CMI fieldwork), true anonymisation may be impossible
- Temporal sensitivity: data safe to share now may not have been safe earlier (or vice versa)
- Funder mandates vs. ethics board restrictions: researchers may face contradictory requirements

**CARE principles (Carroll et al., 2020):**
- Collective Benefit, Authority to Control, Responsibility, Ethics
- Exist in deliberate tension with FAIR — FAIR maximises reuse, CARE ensures reuse doesn't harm
- "As open as possible, as closed as necessary" is the compromise formulation (Horizon Europe, RCN), but the burden of justifying closure falls on the researcher

**WEIRD bias in reproducibility standards:**
- Reproducibility movement catalysed by crises in WEIRD disciplines (psychology, biomedicine, economics)
- Standards designed for quantitative hypothesis-testing research; translate poorly to inductive, interpretive, participatory work
- Lab-based assumptions: "replication" assumes controlled conditions that can be recreated
- Publication as unit of analysis: misses policy briefs, technical reports, community outputs
- The "Bropenscience" critique: open science movement dominated by white men in WEIRD countries

**Qualitative transparency alternatives:**
- APSA Qualitative Transparency Deliberations (QTD) report (2020): recommends "active citation," annotated appendices, process-tracing standards as alternatives to full data sharing
- Distinction between production transparency, analytic transparency, and data access
- Process transparency over outcome replication: document how research was conducted and why decisions were made
- Reflexivity as rigor: researcher's explicit engagement with positionality as quality assurance

**Power dynamics:**
- Northern funder requirements for data deposit in Northern repositories: data leaves country of origin
- Compliance costs disproportionately borne by Southern partners
- Risk of "parachute research" exacerbated by open data mandates
- But transparency can also challenge asymmetries: open protocols allow Southern researchers to adopt methods; preregistration makes agendas visible to scrutiny

**Language barriers:**
- Most reproducibility infrastructure is English-centric (OSF, GitHub, reporting guidelines, training materials)
- Preregistrations in non-English languages are rare and may not be recognised by journals
- Code documentation assumes English literacy
- SciELO, Redalyc, AfricArXiv provide partial alternatives

**Relevant frameworks:**
- Global Code of Conduct for Research in Resource-Poor Settings (TRUST project, EU, 2018)
- KFPE 11 Principles for Research Partnerships (Swiss, 2018)
- DIME Analytics "Development Research in Practice" handbook (World Bank, 2021) — closest to field-specific reproducibility manual for development research, but quantitative-focused
- Research Fairness Initiative (COHRED)

**Tiered access models:**
- Sikt Research Data Archive, UK Data Service, ICPSR offer restricted access
- Metadata sharing: share what data exist, how collected, what they contain — without sharing the data themselves
- This supports discoverability and partial reproducibility without exposure risk

**Implication for CMI:** This is perhaps the most important addition to the page. CMI researchers work in exactly these contexts — interviews in sensitive political environments, small communities, cross-cultural partnerships, Global South fieldwork. A section on navigating the tension between transparency and protection, with specific reference to CARE, tiered access, and qualitative transparency alternatives, would make this page distinctively relevant rather than generic.

### 2.7 Funder Requirements

**Convergence across major funders:**

| Funder | Open access | Data sharing | DMP required | Preregistration |
|---|---|---|---|---|
| Horizon Europe | Immediate OA, no embargo | FAIR by default, "as open as possible" | Yes | Encouraged, not required |
| RCN (Norway) | Immediate OA (Plan S) | FAIR principles, archive in suitable repos | Yes | Encouraged, not required |
| ERC | Immediate OA | FAIR, deposit in trusted repository | Yes | Encouraged |
| Norad | Varies by programme | Increasingly expected | Varies | Not specified |
| UKRI | Immediate OA (from Apr 2022) | Data supporting publications openly available | Yes | Encouraged |
| NIH (US) | Immediate OA from Jul 2025 (Nelson Memo) | Data sharing plan required | Yes | Required for clinical trials only |

**Implication for CMI:** A brief mention of funder convergence on reproducibility expectations would contextualise the page — these practices are not optional extras but increasingly expected by the funders CMI researchers work with.

---

## 3. Recommendations for the Revised Draft

### Structural Recommendations

1. **Add a framing section** on why reproducibility matters now — brief (2–3 paragraphs), referencing the reform movement, documented scandals, and the finding that good practices produce replicable results.

2. **Expand the AI section substantially.** It should cover: publisher requirements, documentation checklist, GDPR/data protection (DPIA requirement, DPA requirement, consumer vs enterprise tiers), specific risks (hallucination, bias, data leakage), and the Norwegian context (Datatilsynet findings).

3. **Add a section on navigating transparency and protection.** This is the CMI-distinctive addition. Cover: the tension between openness and participant safety, tiered access models, metadata sharing, qualitative transparency (analytic transparency, active citation), CARE principles alongside FAIR, and the honest acknowledgement that some data cannot and should not be shared openly.

4. **Add Registered Reports** as a distinct subsection under or alongside preregistration. Researchers should know this option exists.

5. **Expand preregistration to address qualitative/mixed-methods.** Mention the transparency model, EGAP, and be honest about criticisms.

6. **Update the tools section.** Add Quarto, mention CodeRefinery and nordic-gitlab.deic.dk as Nordic resources, update the infrastructure picture (NVA, NIRD).

7. **Add a brief section on funder expectations** — not exhaustive (the lifecycle pages cover this), but enough to contextualise why these practices are increasingly non-optional.

8. **Consider mentioning research assessment reform** (DORA/CoARA) — briefly, as motivation. Researchers may feel reproducibility practices are unrewarded; the assessment reform movement is changing this.

### Content Tone Recommendations

- Maintain the current draft's pragmatic, non-preachy tone
- Acknowledge that reproducibility standards were designed for a specific kind of research, and that adaptation is needed for qualitative, fieldwork-based, and sensitive-context work
- Be specific about CMI-relevant methods: interviews, focus groups, ethnography, survey work in the Global South, mixed-methods, participatory approaches
- Give concrete examples grounded in CMI's research profile (governance research in authoritarian contexts, development evaluations, cross-cultural partnerships)
- Avoid the trap of making reproducibility sound like it applies mainly to quantitative work — give equal weight to qualitative transparency

### What to Cut or Compress

- The current "What reproducibility requires" section is fine but slightly generic — could be sharpened with a motivating sentence about documented failures
- The version control section could be compressed (moved to tools) and replaced with more substantive content on qualitative transparency and the transparency-protection tension

---

## 4. Key References for the Revised Draft

### Essential

- Carroll, S.R. et al. (2020). "The CARE Principles for Indigenous Data Governance." *Data Science Journal*, 19(1), 43.
- Büthe, T. & Jacobs, A.M. (2020). APSA Qualitative Transparency Deliberations Final Report.
- EDPB Opinion 28/2024 on AI models and personal data (Dec 2024).
- TOP Guidelines 2025 preprint (https://osf.io/preprints/metaarxiv/nmfs6).
- Protzko et al. (2024). "High Replicability of Newly Discovered Social-Behavioural Science Findings is Achievable." *Nature Human Behaviour*.
- COPE position on AI authorship (https://publicationethics.org/guidance/cope-position/authorship-and-ai-tools).
- Datatilsynet NTNU/Copilot sandbox exit report (Nov 2024).

### Valuable

- DIME Analytics. "Development Research in Practice." World Bank, 2021.
- Global Code of Conduct for Research in Resource-Poor Settings (TRUST project, 2018).
- Scheel et al. (2021). "An Excess of Positive Results." *Advances in Methods and Practices in Psychological Science* (on Registered Reports).
- Amano et al. (2023). Language barriers in science. *PLOS Biology*.
- KFPE "11 Principles for Research Partnerships" (2018).

### Norwegian Context

- NVA launch: https://sikt.no/en/tjenester/nasjonalt-vitenarkiv-nva
- NIRD Research Data Archive: https://www.sigma2.no/news/2025/launching-norways-largest-archive-scientific-data
- CodeRefinery: https://coderefinery.org/
- Nordic-RSE: https://nordic-rse.org/
- RCN Open Science policy: https://www.forskningsradet.no/en/research-policy-strategy/open-science/
- Datatilsynet AI and privacy: https://www.datatilsynet.no/en/regulations-and-tools/reports-on-specific-subjects/ai-and-privacy/

---

## 5. Suggested Revised Outline

```
# Reproducibility and transparency

[Intro paragraph — expanded to include why this matters now]

## What reproducibility requires
[Keep current content, sharpen with one motivating sentence about documented failures]

## Transparency in qualitative and fieldwork-based research
[NEW — analytical transparency, process documentation, reflexivity,
active citation, codebook versioning. Positioned as equally rigorous,
not a lesser standard.]

## Preregistration
[Expand — transparency model for qualitative work, EGAP, criticisms acknowledged]

### Registered Reports
[NEW — what they are, why they matter, journal list, practical implications]

## Documenting AI tools
[Substantially expanded — publisher consensus, documentation checklist,
GDPR/data protection section, risks (hallucination, bias, data leakage),
Norwegian context (Datatilsynet, DPIA requirement)]

## Transparency and protection: navigating the tension
[NEW — the core CMI-relevant section. FAIR and CARE. Tiered access.
Metadata sharing. Political sensitivity. Small communities.
Funder mandates vs ethics restrictions. Practical guidance.]

## Version control, environments, and tools
[Updated — add Quarto, CodeRefinery, Norwegian infrastructure,
keep renv/conda/Docker but scale to effort/stakes]

## Transparency about uncertainty
[Keep current content — it's strong]

## Funder expectations
[NEW — brief section on convergence. Table or short list.]
```

---

*Report compiled from five parallel research streams covering: (1) reproducibility crisis and reform, (2) AI governance in research, (3) preregistration developments, (4) transparency tools and standards, (5) equity and Global South contexts. Web searches conducted 2026-03-26.*
