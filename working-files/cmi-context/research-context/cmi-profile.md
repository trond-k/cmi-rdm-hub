---
version: "1.0"
date: 2026-03-11
notes:
  - Verify staff count (~105) and active project count (~90) are still current.
  - CMI's institutional AI policy is referenced but not yet available in context/.
---

# CMI Institutional Profile

<!-- WHO CMI is: identity, research profile, geographic focus, partnership philosophy.
     This is stable institutional context — it changes with strategy updates, not
     with operational or policy changes. Used by LLM prompts to understand the
     institution they are generating guidance for.

     For how CMI is organised for RDM, see organisation-and-compliance.md.
     For operational defaults, see the topic-specific modules. -->


## About CMI

Chr. Michelsen Institute (CMI) is an independent development research institute based in Bergen, Norway, located on the campus of the University of Bergen. Founded in 1930, CMI conducts research primarily focused on low- and middle-income countries in Africa, Asia, the Middle East, and Latin America. CMI is not a university — it is an independent research institute. Staff do not have teaching obligations. CMI has approximately 105 employees and runs around 90 externally funded projects at any given time.

CMI's vision is "research for a just and equal world." Its mission is to address global challenges by providing research-based knowledge that shapes policy and practice.


## Research profile

### Disciplines

CMI is a social science institute. The main disciplines are:
- Economics (development economics, public finance, impact evaluation)
- Political science (governance, democracy, elections, authoritarianism)
- Social and cultural anthropology (ethnography, migration, displacement)

Research is multidisciplinary. Many projects combine methods and perspectives from two or more of these disciplines.

### Thematic research groups

CMI's research is organised into seven multidisciplinary research groups:

1. **Tax & Public Finances** — tax policy, revenue administration, fiscal governance. Close collaboration with national tax administrations (e.g., Zanzibar Revenue Authority, Norwegian Tax Administration).
2. **Rights & Gender** — transitional justice, women's rights, conflict-related sexual violence, legal empowerment.
3. **Democracy & Governance** — elections, political participation, governance challenges, authoritarian politics.
4. **Poverty & Global Health** — development economics, health systems, impact evaluation, poverty measurement.
5. **Climate & Natural Resources** — environmental security, climate adaptation, natural resource governance, smallholder agriculture.
6. **Corruption (U4 Anti-Corruption Resource Centre)** — anti-corruption research, training, and advisory services. The U4 Centre is funded by eight partner countries and serves a global audience.
7. **Humanitarianism & Migration** — refugee studies, humanitarian action, displacement, urban refugees, humanitarian diplomacy.

### Common research methods

CMI researchers use a wide range of social science methods. The most common include:

- Semi-structured and in-depth interviews (individual and group)
- Ethnographic fieldwork and participant observation
- Household and individual surveys (both paper-based and digital, often via Nettskjema or similar tools)
- Document and policy analysis
- Registry data and administrative data analysis
- Randomised controlled trials and quasi-experimental designs (primarily in economics)
- Mixed-methods designs combining qualitative and quantitative approaches
- Evaluations and commissioned studies (using varied methods)

- **Survey and data collection**: For larger surveys, CMI often works with external data collection providers (e.g., EconInsight in Africa) using tools such as SurveyCTO, KoboToolbox, and ODK. Smaller-scale data collection may use simpler tools.

- **Transcription**: Practices vary across researchers and projects. Methods include manual transcription, professional transcription services, software-assisted transcription (e.g., NVivo's built-in transcription), and AI-based transcription tools (e.g., Whisper). There is no single institutional standard.

- **Qualitative analysis**: NVivo, Atlas.ti, and MAXQDA are all in use, alongside manual/Word-based analysis. Choice depends on researcher preference and project needs.

- **Quantitative analysis**: Stata and R are the most common tools. SPSS is also used, and Python to a limited extent among some researchers.

- **AI tools**: Researchers increasingly use AI-based tools for various tasks. CMI has an institutional AI policy that sets boundaries for acceptable use. When generating guidance, the tool should remind researchers to check the AI policy when AI-assisted processing of research data is involved.

For data protection requirements when using survey platforms, transcription services, and AI tools with research data, see `tools-and-services.md`.

### Common data types

Given CMI's research profile, the most frequently encountered data types are:

- Interview recordings (audio, occasionally video) and transcripts
- Survey data (individual, household, firm-level)
- Field notes, research diaries, and observation protocols
- Policy documents, legal texts, and institutional records
- Administrative and registry data (obtained from national or local government agencies)
- Photographs from fieldwork settings
- Correspondence with research participants and partners
- Financial and organisational data from partner institutions
- Geospatial data (occasionally, in climate and natural resource research)


## Geographic and partnership context

### Research regions

CMI's primary geographic focus is:
- **Africa**: extensive and long-standing partnerships in Sudan, Tanzania (including Zanzibar), Ghana, Ethiopia, Mozambique, Zambia, Kenya, and other countries across Sub-Saharan Africa.
- **Asia**: research in Afghanistan, Nepal, Bangladesh, Myanmar, and other Asian contexts.
- **Middle East**: Palestine, Jordan, Lebanon, Syria (refugee contexts).
- **Latin America and the Balkans**: to a lesser extent.

### Partnership philosophy

CMI's strategy (2023–2028) emphasises **equal knowledge production** and **inclusive partnerships** with researchers and institutions in the Global South. This has direct implications for data management:

- Research projects frequently involve co-investigators and fieldwork partners at institutions in partner countries.
- Data is often collected by local research assistants or partner-institution staff.
- Data may be stored, transferred, or processed across national borders — including between Norway and countries with limited or no data protection frameworks.
- Partners' perspectives are meant to be integrated into all research phases, including decisions about data ownership, access, and archiving.
- CMI is committed to combating Eurocentric perspectives in research, including in how data is managed and who has access to it.

### Implications for data management guidance

When generating data management guidance, the guide should be sensitive to:
- The practical realities of fieldwork in low-resource and conflict-affected settings (unreliable internet, limited secure storage options, physical security concerns for data and researchers).
- The ethical complexities of research with vulnerable and marginalised populations in the Global South.
- The tension between open science norms (which favour data sharing) and the need to protect participants in sensitive political, conflict, or human rights contexts.
- The question of data ownership in collaborative partnerships — who controls the data, who benefits from it, and who decides on archiving and sharing.
