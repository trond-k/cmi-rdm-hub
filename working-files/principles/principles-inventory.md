# Principles inventory — all principle and principle-adjacent statements across the CMI RDM Hub

*Compiled 28 March 2026; updated 29 March 2026. Sources: `docs/`, `working-files/`, `base-content-architecture.md`.*

This document inventories every principle framework, institutional principle, and principle-adjacent statement found across the codebase. It is organised in three tiers: (A) external/international frameworks CMI draws on, (B) CMI's own institutional principles, and (C) operational and epistemic commitments embedded in guidance pages. Each entry notes where it appears and how it currently functions in the site.

---

## A. External and international principle frameworks

These are established frameworks that CMI references and builds upon but does not own.

### A1. FAIR Principles (2016)

**Findable, Accessible, Interoperable, Reusable.**

- Operationalise Merton's norm of organised scepticism into a practical framework for data management.
- FAIR does not mean open. Controlled-access data with good metadata is FAIR. Undocumented data in a repository is not.
- Adopted by Horizon Europe, NIH, G7, Australian Research Data Commons, RCN, ERC.
- Cost of not having FAIR data estimated at EUR 10.2 billion per year (European Commission study).

**Where referenced:**

- `docs/foundations-of-data-sharing.md` (definition, epistemic argument)
- `docs/reproducibility-and-transparency.md` (operational use alongside CARE)
- `docs/lifecycle-2-fund.md` (funder requirements)
- `docs/lifecycle-8-publish.md` (archives implement FAIR by design)
- `docs/lifecycle-9-preserve.md` (metadata accessibility, A2)
- `docs/lifecycle-10-discover.md` (metadata always open)
- `docs/lifecycle-11-access.md` (tombstone records, A2)
- `working-files/open-science/fair-principles.md` (full sub-principle breakdown F1–R1.3)
- `working-files/principles/core-principles.md` (Principle 7 footnote)
- `working-files/cmi-context/cmi-policies/open-science.md` (FAIR by default)

---

### A2. CARE Principles for Indigenous Data Governance (2019)

**Collective Benefit, Authority to Control, Responsibility, Ethics.**

- Complement FAIR by asking who has the right to govern data, not just how to make it technically usable.
- Extended beyond Indigenous contexts to any population whose data can be weaponised: displaced persons, civilians under occupation, humanitarian crises (Suchikova and Nazarovets, 2025).
- FAIR and CARE are complementary, not competing.

**Where referenced:**

- `docs/foundations-of-data-sharing.md` (definition, extension to conflict settings)
- `docs/cmi-institutional-context.md` (partnership dynamics, Ubuntu)
- `docs/reproducibility-and-transparency.md` (neither framework complete without the other)
- `docs/lifecycle-11-access.md` (community governance of access)
- `docs/lifecycle-12-share-and-reuse.md` (ethical reuse, sovereignty)
- `docs/elements-of.md` (policy layer)
- `working-files/principles/core-principles.md` (Principle 7 footnote)
- `working-files/principles/why-rdm-matters.md` (data is voice)
- `working-files/cmi-context/cmi-policies/open-science.md` (CARE where relevant)
- `working-files/foundations/philosophical-foundations-of-data-sharing.md`
- `working-files/ethics/ethics-guidelines.md`

---

### A3. OCAP Principles (1998)

**Ownership, Control, Access, Possession.**

- Articulated by Canada's First Nations.
- Precursor and complement to CARE; focused specifically on Indigenous data sovereignty.

**Where referenced:**

- `docs/foundations-of-data-sharing.md`
- `working-files/foundations/origins-of-knowledge-and-data-sharing.md`

---

### A4. Merton's Norms of Science (1942)

**Communalism, Universalism, Disinterestedness, Organised Scepticism.**

- Communalism: scientific findings are a common heritage; publicly funded knowledge belongs to the commons.
- Organised scepticism: findings must be open to scrutiny; data sharing is a precondition.
- Philosophical backbone for contemporary open science policy.

**Where referenced:**

- `docs/foundations-of-data-sharing.md` (detailed treatment)
- `working-files/foundations/philosophical-foundations-of-data-sharing.md`

---

### A5. 'As open as possible, as closed as necessary'

- Used by the European Commission (Horizon Europe Programme Guide) and echoed in the UNESCO Recommendation on Open Science (2021).
- Openness is the default aspiration; restrictions require justification proportionate to actual risk.
- The burden of justification falls on closure, not on openness.

**Where referenced:**

- `docs/reproducibility-and-transparency.md` (core formulation)
- `docs/lifecycle-2-fund.md` (RCN policy)
- `working-files/principles/core-principles.md` (Principle 7)
- `working-files/cmi-context/cmi-policies/open-science.md` (governing principle)

---

### A6. UNESCO Recommendation on Open Science (2021)

**Four pillars: Open Scientific Knowledge, Open Science Infrastructures, Open Engagement of Societal Actors, Open Dialogue with Other Knowledge Systems.**

- First international normative framework for open science.
- Adopted unanimously by all 193 UNESCO member states.

**Where referenced:**

- `docs/foundations-of-data-sharing.md`
- `working-files/open-science/open-science.md` (full pillar breakdown)

---

### A7. Leonelli's 'Openness as Connection' (2023)

- Challenges object-oriented openness (equating openness with making outputs freely available).
- Proposes openness as 'judicious connection': attending to the conditions under which data were produced and the relationships that sustain their meaning.
- Grounded in a process-oriented epistemology; research is situated, embodied, and goal-directed.

**Where referenced:**

- `docs/foundations-of-data-sharing.md`
- `working-files/foundations/philosophical-foundations-of-data-sharing.md`

---

### A8. GDPR Principles (Articles 5 and 89)

- **Purpose limitation** (Art. 5(1)(b)): collected for specified, explicit, and legitimate purposes.
- **Data minimisation** (Art. 5(1)(c)): adequate, relevant, and limited to what is necessary.
- **Accountability** (Art. 5(2)): the controller must demonstrate compliance.
- **Proportionality** (Recital 4): data protection balanced against other fundamental rights.
- **Article 89**: permits processing of sensitive personal data for scientific research with appropriate safeguards.

**Where referenced:**

- `docs/CROSS-legal.md` (purpose limitation, accountability)
- `docs/CROSS-gdpr-and-legal-compliance.md` (proportionality, data minimisation)
- `docs/cmi-institutional-context.md` (GDPR as human-rights safeguard)

---

### A9. TRUST Code for Equitable Research Partnerships

- Global Code of Conduct for Equitable Research Partnerships.

**Where referenced:**

- `working-files/ethics/ethics-guidelines.md`

---

### A10. Bermuda Principles (1996) / Fort Lauderdale (2003) / Toronto Statement (2009)

- Release sequence data within 24 hours (Bermuda); extended rapid pre-publication sharing norms.
- Historical milestones in the evolution of open data norms.

**Where referenced:**

- `docs/foundations-of-data-sharing.md`

---

## B. CMI's own institutional principles

These are principles that CMI has articulated (or is developing) for its own practice.

### B1. Eight core principles for research data at CMI

Source: `working-files/principles/core-principles.md` (latest version); `working-files/early-drafts/core-principles-v1.md` (extended version with checklists).

1. **Manage data in ways that support good research.** RDM is part of research quality. Data should be organised, documented, understandable, and linked to methods.
2. **Apply proportionality.** Measures proportionate to the nature of the project and sensitivity of the material. Neither over-control nor under-management.
3. **Protect people, relationships, and context.** Risk from direct identifiers, context, political setting, power relations. Think beyond what is visible in the file.
4. **Document decisions as you go.** Documentation is part of responsible data management, not an afterthought.
5. **Match access and security to sensitivity.** Security reflects data, context, and access needs. Not only technical; depends on routines, limited access, and good judgement.
6. **Treat data management as a shared responsibility.** Not the researcher's burden alone. Shared does not remove individual responsibility.
7. **Be as open as possible, as closed as necessary.** Avoid both extremes. FAIR and CARE as complementary frameworks.
8. **Plan for the full lifecycle.** Decisions made early cascade through the whole project. Plan beyond collection and analysis.

---

### B2. Four data principles (philosophical framing)

Source: `working-files/principles/data-principles.md`; echoed in `working-files/principles/why-rdm-matters.md`.

1. **Data is political.** Data is never neutral. Transparency, accountability, equal value of diverse data forms.
2. **Data is voice.** Data is representation. Responsibility to amplify underrepresented perspectives. CARE Principles.
3. **Data is memory.** Data is institutional and societal memory. Loss of data means loss of knowledge.
4. **Data is value.** Data connects CMI's heterogeneous portfolio. Institutional resource that outlasts projects and careers.

---

### B3. CMI's five open science principles

Source: `working-files/cmi-context/cmi-policies/open-science.md`.

1. **Do no harm.** Openness must not expose participants, communities, partners, or staff to foreseeable harm.
2. **FAIR by default.** Data should be findable, accessible under defined conditions, interoperable, and reusable.
3. **CARE where relevant.** For research involving Indigenous peoples or marginalised communities.
4. **Metadata is always open.** Even when data is restricted, metadata should be public (exception: when metadata itself creates risk).
5. **Risk-based openness.** Projects must assess sensitivity and contextual risks early and throughout.

---

### B4. Five data sharing pathways

Source: `working-files/cmi-context/cmi-policies/open-science.md`.

1. Open access (CC0 or CC BY)
2. Registered access (authenticated users, standard terms)
3. Controlled access (approved applicants, data use agreements)
4. Restricted access (strict agreements, secure environments)
5. No external sharing (metadata-only record where feasible)

---

## C. Operational and epistemic commitments embedded in guidance

These are principle-like statements that function as rules or commitments within specific lifecycle stages or cross-cutting pages.

### C1. Reproducibility and transparency

- 'Reproducibility means someone else can follow the path from your data and documentation to your results. Transparency means they can see why you made the choices you did.' (`docs/reproducibility-and-transparency.md`)
- Three requirements: record what you did, record what you used, record why you chose it.
- Reproducibility starts with the analyst, not the reader.

### C2. Metadata accessibility

- 'Metadata should always be open' (FAIR A2). Even restricted data should be findable. (`docs/lifecycle-10-discover.md`, `docs/lifecycle-9-preserve.md`)

### C3. Raw data separation

- 'The key structural principle is to separate raw data from derived and working files.' (`docs/lifecycle-5-store.md`, `docs/file-and-folder-naming.md`)

### C4. Format sustainability

- 'Prefer open, widely adopted, non-proprietary formats.' (`docs/lifecycle-9-preserve.md`)

### C5. Archive as the key FAIR decision

- 'Choosing the right archive is the single most impactful FAIR decision a researcher makes.' (`docs/lifecycle-8-publish.md`)

### C6. Every transformation documented

- 'Every transformation must be documented. Undocumented processing is irreproducible processing.' (`docs/lifecycle-6-process.md`, `base-content-architecture.md`)

### C7. Trust as the underlying purpose

- 'Research that others can examine, reuse, and build upon is research that earns trust.' (`docs/foundations-of-data-sharing.md`)

### C8. Openness is not always ethical

- 'Sharing sensitive data without adequate safeguards can cause harm. Sharing data extracted from vulnerable communities without their involvement in governance can reproduce colonial dynamics.' (`docs/foundations-of-data-sharing.md`)

### C9. Data quality at the point of collection

- 'Data quality is determined at the point of collection. Errors introduced here are the hardest to fix later.' (`base-content-architecture.md`, Stage 4)

### C10. DMP as a living document

- 'The DMP is a living document, not a compliance exercise.' (`base-content-architecture.md`, Stage 3)

### C11. Storage decisions shape the lifecycle

- 'Storage decisions during the project directly affect what can be preserved, shared, and reused afterwards.' (`base-content-architecture.md`, Stage 5)

---

## D. Summary: how the layers relate

```
External frameworks (FAIR, CARE, OCAP, Merton, UNESCO, GDPR, etc.)
    ↓ inform
CMI's institutional principles (8 core, 4 data, 5 open science)
    ↓ operationalised through
Lifecycle guidance and cross-cutting commitments (C1–C11)
```

The eight core principles (B1) are the most developed CMI-specific articulation and are closest to being publishable. The four data principles (B2) provide a philosophical framing. The five open science principles (B3) overlap substantially with B1 but are focused on the openness/sharing dimension.

---

## E. Observations and gaps

1. **Overlap between B1, B2, and B3.** The eight core principles, four data principles, and five open science principles share concepts (proportionality, protection, openness, FAIR, CARE) but are structured differently and live in different working-files. A published page should consolidate rather than duplicate.

2. **~~No single published principles page exists.~~** Resolved: `docs/rdm-principles.md` was published on 29 March 2026. It consolidates the eight core principles (B1) with a framing drawn from the four data principles (B2). A tone revision is underway to make the page work better as a clear institutional statement for both internal and external audiences.

3. **Linkability for DMPs.** Resolved in practice: `docs/rdm-principles.md` is now the stable, citable page. Funders (RCN, Horizon Europe, ERC) can be pointed to it directly from a DMP.

4. **CARE is well integrated** across the site but never given a standalone, concise summary with CMI-specific application.

5. **Proportionality** is a strong and distinctive CMI position (given GDPR + sensitive contexts) but appears only in working-files and the GDPR page.

6. **Trust** as the overarching purpose is stated beautifully in `foundations-of-data-sharing.md` but not foregrounded as a principle.

7. **Tone.** The initial published version of `docs/rdm-principles.md` was substantively complete but read too much like academic guidance. A rewrite (29 March 2026) targets a clearer institutional statement: authoritative but readable, suitable for both CMI researchers and external stakeholders (funders, partners) who access the page via DMP links. Structural changes include moving the philosophical framing into a collapsible section and removing the DMP referencing boilerplate (since the page itself is the linkable resource).

---

## F. DMP gap analysis (added 29 March 2026)

Fourteen documents in `working-files/early-operational-docs/` were reviewed. These include DMPs for Fisher of Corpses, ATTACH (two versions), CoM-Financing (two versions), ENVPEACE, LANDAPT, StaR, RETURNEC, Invisible Ceiling, Mozambique War, and Truth Commissions (two versions), plus a master data description template. All DMPs use a consistent set of guiding principles in their Section 1.2.

### Principles used in DMPs vs. the eight core principles

| Principle in DMPs | Frequency | Covered by B1? | Notes |
|---|---|---|---|
| FAIR | All DMPs | Yes (Principle 7) | DMPs frame as top-level; B1 integrates into Principle 7 |
| 'As open as possible, as closed as necessary' | All DMPs | Yes (Principle 7) | Direct match |
| Do-No-Harm | All DMPs | Partially (Principle 3) | DMPs use 'Do-No-Harm' as an explicit named principle. B1 subsumes under 'Protect people' but does not use the phrase. **Gap addressed in published page.** |
| Sensitivity minimisation / Data minimisation | All DMPs | Implicit (Principles 2, 5) | Covered through proportionality and access/security |
| Proportionality | All DMPs | Yes (Principle 2) | Direct match |
| Access control / Least privilege | All DMPs | Yes (Principle 5) | Direct match |
| Shared responsibility | All DMPs | Yes (Principle 6) | Direct match |
| Conflict sensitivity | 3 DMPs | Not explicitly | Project-specific; appropriate for individual DMPs, not institutional principles |
| Data sovereignty | 1 DMP (ENVPEACE) | Via CARE in Principle 7 | **Gap addressed in published page** with explicit mention in Principle 7 |
| DMP as living document | All DMPs | Yes (Principle 8) | Implicit in lifecycle planning |

### Conclusions

1. **No missing principles.** Everything in the DMPs maps to the eight core principles. The DMPs use more specific operational language that sits underneath the eight principles.
2. **Two gaps addressed.** The published page (`docs/rdm-principles.md`) adds 'Do no harm' to Principle 3's heading and makes data sovereignty explicit in Principle 7.
3. **The eight core principles are the right level of abstraction** for an institutional page. DMP sub-principles (sensitivity minimisation, conflict sensitivity, least privilege) are project-specific operationalisations.

---

## G. Published page

The principles were first published as `docs/rdm-principles.md` on 29 March 2026, added to the Foundations section in navigation. The page consolidates B1 (eight core principles) with a framing section drawn from B2 (four data principles) and addresses the two DMP gaps identified in section F.

**Revision (29 March 2026).** The page is being rewritten to work better as a clear institutional statement. Changes:

- **Tone:** Shifted from academic guidance toward a confident, readable institutional frame. Professional but approachable; plain language; occasional contractions. Suitable for both CMI researchers and external readers (funders, partners) accessing the page via a DMP link.
- **Structure:** Philosophical framing ('How CMI thinks about data') moved into a collapsible admonition. Each principle now leads with an italic one-sentence summary for scannability.
- **DMP section removed.** The earlier version included boilerplate text for referencing the principles in a DMP. This was removed because the page itself is the linkable institutional reference; a separate 'how to link to us' section was redundant.
- **Substance unchanged.** The eight principles, their content, the admonitions, the footnotes, and the quick-check questions are all retained.
