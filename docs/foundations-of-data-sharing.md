---
icon: lucide/book-open
title: "Foundations of knowledge and data sharing"
description: "Why sharing research data matters: the historical, epistemic, ethical, and political arguments that underpin open science and responsible data governance."
tags:
  - Open science
  - Ethics
  - Epistemology
  - FAIR
  - CARE
  - History
notes: ""
date_updated: 2026-03-27
---

# Foundations of knowledge and data sharing

*Scholars have built systems for sharing knowledge for millennia. The challenges they faced, discovery, attribution, trust, gatekeeping, and cross-cultural exchange, remain central to research data management today. Data sharing rests on epistemic commitments, not just funder mandates: Merton's communalism norm treats knowledge as a collective inheritance, the FAIR principles operationalise reproducibility, and the CARE Principles insist that responsible sharing must also account for power and the rights of communities. This page traces the line from ancient knowledge networks to the policy landscape you navigate today.*

## Knowledge before print

Ancient libraries served as nodes where texts were copied, translated, and debated. At Alexandria, the librarian Callimachus of Cyrene compiled the *Pinakes* in the third century BCE: a 120-volume catalogue that recorded each work's author, birthplace, title, opening words, and length.[^1] It was, in effect, the first metadata scheme, and the problems it addressed (discovery, attribution, deduplication) remain central to research data management today.

Knowledge-sharing infrastructure was not confined to the Mediterranean. The university at Nalanda in Bihar, India, operated continuously from the fifth to the twelfth century CE, drawing students from China, Korea, Tibet, and Southeast Asia. Its system of public oral disputation served a function recognisable as an early form of peer review.[^2] In Timbuktu, private family libraries preserved hundreds of thousands of manuscripts; their tradition of marginal annotation, where successive readers added glosses across generations, is strikingly similar to modern collaborative scholarly annotation.[^3]

The Abbasid Translation Movement (eighth to tenth centuries CE), centred on Baghdad, rendered Greek, Persian, Sanskrit, and Syriac works into Arabic. Christian, Jewish, Sabian, and Muslim scholars worked side by side, and translators were handsomely compensated.[^4] The movement demonstrates that knowledge sharing, at its most productive, has often been ecumenical and multilingual.

??? example "The isnad as an early provenance system"
    Islamic hadith scholarship developed the *isnad* (chain of transmission) from the seventh century CE onward. Each report traced its lineage through named transmitters back to an eyewitness. Scholars compiled vast biographical dictionaries evaluating each transmitter's reliability, memory, and moral character, grading reports as sound, fair, weak, or fabricated.[^5] The parallels with modern data provenance tracking are direct: both systems ask who handled the information, whether the chain is unbroken, and whether each link is trustworthy.

## Correspondence, journals, and the problem of trust

In early modern Europe, the 'Republic of Letters' connected natural philosophers through a web of private correspondence. Marin Mersenne's cell in Paris served as what contemporaries called 'the post-box of learned Europe', routing findings among Descartes, Fermat, Pascal, Galileo, and over a hundred others.[^6] Henry Oldenburg's launch of the Royal Society's *Philosophical Transactions* in March 1665 was a direct response to the limitations of letter networks. By fixing findings in print with a date, the journal created a public, timestamped record that could settle priority claims and reach a far wider audience.[^7] The Royal Society's motto, *Nullius in verba* ('Take nobody's word for it'), captured the shift from trusting persons to trusting evidence.

!!! info "Sharing was never universal"
    These early networks were exclusive. Participation depended on social standing, institutional affiliation, language, and geography. The history of knowledge sharing is also a history of knowledge gatekeeping, and that tension has not disappeared.

## From journals to datasets

The journal solved the problem of disseminating findings but left the underlying data with the researcher. This began to change in the twentieth century, driven by three forces:

1. **Large-scale collaboration.** Projects in physics, meteorology, and genomics generated datasets too large for any single group to reproduce. Sharing became a practical necessity.
2. **Computing.** Digital data could be copied without degradation and transmitted without physical transport. The technical barrier to sharing dropped dramatically from the 1960s onward.
3. **Public accountability.** As public funding of research grew, so did the argument that publicly funded data should be publicly accessible.

The Bermuda Principles of 1996 marked a turning point: participants in the Human Genome Project agreed to release all sequence data within 24 hours of generation, before publication. The Fort Lauderdale Agreement (2003) and Toronto Statement (2009) extended this norm.[^8] Meanwhile, evidence that many published findings could not be reproduced (only 36% of 100 psychology studies replicated in a landmark 2015 project) gave funders a powerful argument for requiring data to be shared alongside results.[^9]

## Knowledge as a collective enterprise

The most influential epistemic argument for data sharing traces back to Robert K. Merton, who in 1942 described four norms essential to the functioning of science: communalism, universalism, disinterestedness, and organised scepticism.[^10] Communalism holds that scientific findings are the product of collective effort and therefore constitute a common heritage. No individual's claim to ownership can override the community's need for access.

This norm provides the philosophical backbone for contemporary open science policy. When funders require you to deposit your data in a repository, they are operationalising a Mertonian principle: the research was publicly funded, the knowledge it produces belongs to the commons, and withholding it without justification undermines the epistemic machinery of science itself.

Organised scepticism, another of Merton's norms, demands that findings be open to scrutiny. Data sharing is a precondition for this. The FAIR principles (Findable, Accessible, Interoperable, Reusable), articulated by Wilkinson and colleagues in 2016, formalise this insight into a practical framework.[^11] A European Commission study estimated the annual cost of not having FAIR research data at EUR 10.2 billion.

Yet reproducibility is not a neutral technical standard. It privileges certain kinds of evidence (quantitative, structured, computationally tractable). Qualitative researchers, ethnographers, and scholars working with sensitive populations often cannot share their data without violating the trust on which the research depends. The epistemic ideal of openness must be balanced against the epistemic value of the relationships that made the research possible.

## The open science policy landscape

The Budapest Open Access Initiative (2002), the Berlin Declaration (2003), and the Bethesda Statement (2003) established the foundational case that publicly funded research outputs should be freely available.[^12] FAIR has since been adopted by Horizon Europe, the NIH, the G7, and the Australian Research Data Commons. The UNESCO Recommendation on Open Science (2021), adopted unanimously by all 193 member states, established the first international normative framework.[^13] Plan S requires immediate open access with no embargo. The European Open Science Cloud (EOSC) aims to make FAIR data practices the operational default.

??? example "Open science in practice at research institutes"
    For an institute like CMI, which works across disciplines and geographies, open science raises specific questions. How do you share qualitative interview data without compromising participant confidentiality? How do you respect the data sovereignty of communities in the Global South while meeting European funder mandates? These are not abstract dilemmas; they shape day-to-day decisions about what to deposit, where, and under what conditions.

## Openness as connection, not extraction

Sabina Leonelli's philosophical work on open science challenges the dominant 'object-oriented' framing, in which openness is equated with making research outputs freely available.[^14] She argues that this interpretation risks constraining epistemic diversity and worsening epistemic injustice. When openness means depositing datasets in formats and infrastructures designed by and for well-resourced institutions, researchers working in different contexts may find their knowledge devalued or misappropriated.

Leonelli proposes an alternative: openness as 'judicious connection', grounded in a process-oriented epistemology that recognises research as situated, embodied, and goal-directed. Sharing data responsibly means attending not just to access but to the conditions under which data were produced and the relationships that sustain their meaning. This resonates strongly with research at CMI, where fieldwork often depends on trust built over years with communities that have their own legitimate interests in how their stories are told.

## Power, provenance, and data sovereignty

Any honest account of knowledge sharing must reckon with its politics. Colonial-era natural history expeditions systematically extracted specimens, vocabularies, and cultural artefacts from colonised peoples and deposited them in European institutions, often without consent or attribution. As Linda Tuhiwai Smith argued in *Decolonizing Methodologies* (1999), Western research paradigms have historically served colonial interests, and that legacy shapes who controls research data and who benefits from its reuse.[^15]

The response has been substantive. Canada's First Nations articulated the OCAP Principles (Ownership, Control, Access, Possession) in 1998. Aotearoa New Zealand's Te Mana Raraunga became a global model for indigenous data governance. The CARE Principles for Indigenous Data Governance (2019) provide an internationally applicable complement to FAIR: Collective Benefit, Authority to Control, Responsibility, Ethics.[^16] Where FAIR addresses how to make data technically usable, CARE asks who has the right to govern it. The two frameworks are complementary, not competing; FAIR's 'Accessible' does not mean 'open to everyone', and data can be both FAIR and access-controlled.

The logic of CARE extends beyond Indigenous contexts. Suchikova and Nazarovets have argued that the same principles apply to any population whose data can be weaponised against them: internally displaced persons, civilians under military occupation, and communities in humanitarian crises.[^17] In occupied territories, routine digital records become tools for targeting individuals. Biometric databases assembled for humanitarian aid can be repurposed for surveillance. For CMI researchers working in or on conflict-affected regions, the CARE framework offers a principled basis for restricting access, mandating data destruction, or withholding data entirely when the risks of sharing outweigh the benefits.

!!! warning "Openness is not always ethical"
    Data sharing is the default aspiration in most funder policies, but it is not an unconditional good. Sharing sensitive data without adequate safeguards can cause harm. Sharing data extracted from vulnerable communities without their involvement in governance can reproduce colonial dynamics. The question is not simply 'should you share?' but 'how, with whom, and on whose terms?'

## Why this history matters for your work

You do not need to become a historian of science to manage your data well. But knowing that data sharing has always been shaped by technology, power, and institutional norms helps you navigate the present landscape with more confidence. When a funder asks for a Data Management Plan (DMP), they are drawing on a policy lineage that stretches from the Bermuda Principles through the OECD guidelines to the UNESCO Recommendation. When a repository asks you to assign a Digital Object Identifier (DOI) and structured metadata, they are extending practices that Callimachus would have recognised.

The tools and expectations will continue to evolve. What remains constant is the underlying logic: research that others can examine, reuse, and build upon is research that earns trust. And the conditions under which that trust is built, maintained, and sometimes justifiably withheld deserve the same serious attention as the data itself.

[^1]: Lionel Casson, *Libraries in the Ancient World* (Yale University Press, 2001).
[^2]: Sukumar Dutt, *Buddhist Monks and Monasteries of India* (George Allen & Unwin, 1962).
[^3]: Shamil Jeppie and Souleymane Bachir Diagne (eds.), *The Meanings of Timbuktu* (HSRC Press, 2008).
[^4]: Dimitri Gutas, *Greek Thought, Arabic Culture: The Graeco-Arabic Translation Movement in Baghdad and Early Abbasid Society* (Routledge, 1998).
[^5]: Jonathan A. C. Brown, *Hadith: Muhammad's Legacy in the Medieval and Modern World* (Oneworld, 2009).
[^6]: Anne Goldgar, *Impolite Learning: Conduct and Community in the Republic of Letters, 1680–1750* (Yale University Press, 1995).
[^7]: Adrian Johns, *The Nature of the Book: Print and Knowledge in the Making* (University of Chicago Press, 1998).
[^8]: Toronto International Data Release Workshop Authors (2009). 'Prepublication data sharing.' *Nature*, 461(7261), 168–170.
[^9]: Open Science Collaboration (2015). 'Estimating the reproducibility of psychological science.' *Science*, 349(6251), aac4716.
[^10]: Merton, R. K. (1942). 'The Normative Structure of Science'. In *The Sociology of Science: Theoretical and Empirical Investigations*. Chicago: University of Chicago Press. See also Anderson, M. S. et al. (2010). 'Extending the Mertonian Norms'. *The Journal of Higher Education*, 81(3), 366–393.
[^11]: Wilkinson, M. D. et al. (2016). 'The FAIR Guiding Principles for scientific data management and stewardship'. *Scientific Data*, 3, 160018.
[^12]: Budapest Open Access Initiative (2002). Available at budapestopenaccessinitiative.org.
[^13]: UNESCO (2021). *UNESCO Recommendation on Open Science*. 41st General Conference, 41 C/Res. 24.
[^14]: Leonelli, S. (2023). *Philosophy of Open Science*. Cambridge: Cambridge University Press.
[^15]: Linda Tuhiwai Smith, *Decolonizing Methodologies: Research and Indigenous Peoples* (Zed Books, 1999; 3rd ed. Otago University Press, 2021).
[^16]: Carroll, S. R. et al. (2020). 'The CARE Principles for Indigenous Data Governance.' *Data Science Journal*, 19(1), 43. See also Carroll, S. R. et al. (2021). 'Operationalizing the CARE and FAIR Principles for Indigenous data futures.' *Scientific Data*, 8, 108.
[^17]: Suchikova, Y. and Nazarovets, S. (2025). 'Extending the CARE Principles: managing data for vulnerable communities in wartime and humanitarian crises'. *Scientific Data*, 12, 413.
