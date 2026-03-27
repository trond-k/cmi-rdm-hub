---
icon: lucide/scroll-text
title: "Origins of knowledge and data sharing"
description: "A short history of how and why researchers have shared knowledge and data, from early scholarly networks to modern open science."
tags:
  - Open science
  - History
  - Scholarly communication
notes: ""
date_updated: 2026-03-24
---

# Origins of knowledge and data sharing

*Scholars have built systems for sharing knowledge for millennia. The challenges they faced, discovery, attribution, trust, gatekeeping, and cross-cultural exchange, remain central to research data management today. Modern open science policy, from the FAIR principles to the CARE Principles for Indigenous Data Governance, is the latest chapter in this long history, not its beginning.*

## Knowledge before print

Ancient libraries served as nodes where texts were copied, translated, and debated. At Alexandria, the librarian Callimachus of Cyrene compiled the *Pinakes* in the third century BCE: a 120-volume catalogue that recorded each work's author, birthplace, title, opening words, and length.[^1] It was, in effect, the first metadata scheme, and the problems it addressed (discovery, attribution, deduplication) remain central to research data management today.

Knowledge-sharing infrastructure was not confined to the Mediterranean. The university at Nalanda in Bihar, India, operated continuously from the fifth to the twelfth century CE, drawing students from China, Korea, Tibet, and Southeast Asia. Its system of public oral disputation, where scholars defended their theses before critical audiences, served a function recognisable as an early form of peer review.[^2] In Timbuktu, private family libraries preserved hundreds of thousands of manuscripts spanning theology, law, astronomy, and medicine; their tradition of marginal annotation, where successive readers added glosses and commentaries across generations, is strikingly similar to modern collaborative scholarly annotation.[^3]

The Abbasid Translation Movement (eighth to tenth centuries CE), centred on Baghdad, rendered Greek, Persian, Sanskrit, and Syriac works into Arabic. It was a deliberately cross-cultural enterprise: Christian, Jewish, Sabian, and Muslim scholars worked side by side, and translators were handsomely compensated.[^4] The movement demonstrates that knowledge sharing, at its most productive, has often been ecumenical and multilingual.

??? example "The isnad as an early provenance system"
    Islamic hadith scholarship developed the *isnad* (chain of transmission) from the seventh century CE onward. Each report traced its lineage through named transmitters back to an eyewitness. Scholars compiled vast biographical dictionaries evaluating each transmitter's reliability, memory, and moral character, grading reports as sound, fair, weak, or fabricated.[^5] The parallels with modern data provenance tracking are direct: both systems ask who handled the information, whether the chain is unbroken, and whether each link is trustworthy. Women were active in this tradition; al-Sakhawi's fifteenth-century biographical dictionary records over a thousand women hadith scholars.

## Correspondence, journals, and the problem of trust

In early modern Europe, the 'Republic of Letters' connected natural philosophers through a web of private correspondence. Marin Mersenne's cell in Paris served as what contemporaries called 'the post-box of learned Europe', routing findings among Descartes, Fermat, Pascal, Galileo, and over a hundred others.[^6] Letters were often written to be circulated; a sender expected the recipient to copy passages and share them onward. The system worked, but it was slow, prone to priority disputes, and dependent on personal connections.

Henry Oldenburg's launch of the Royal Society's *Philosophical Transactions* in March 1665 was a direct response to these limitations. By fixing findings in print with a date, the journal created a public, timestamped record that could settle priority claims and reach a far wider audience than any letter network.[^7] The Royal Society's motto, *Nullius in verba* ('Take nobody's word for it'), captured the broader shift: from trusting persons to trusting evidence that could be independently examined. The research article, now so familiar that it seems inevitable, was a designed solution to a specific set of problems.

!!! info "Sharing was never universal"
    These early networks were exclusive. Participation depended on social standing, institutional affiliation, language, and geography. The history of knowledge sharing is also a history of knowledge gatekeeping, and that tension has not disappeared.

## From journals to datasets

The journal solved the problem of disseminating findings but left the underlying data with the researcher. For centuries, the published article was treated as a self-contained record. This began to change in the twentieth century, driven by three forces:

1. **Large-scale collaboration.** Projects in physics, meteorology, and genomics generated datasets too large and too expensive for any single group to reproduce. Sharing became a practical necessity.
2. **Computing.** Digital data could be copied without degradation and transmitted without physical transport. The technical barrier to sharing dropped dramatically from the 1960s onward.
3. **Public accountability.** As public funding of research grew, so did the argument that publicly funded data should be publicly accessible.

The Bermuda Principles of 1996 marked a turning point: participants in the Human Genome Project agreed to release all sequence data within 24 hours of generation, before publication. The Fort Lauderdale Agreement (2003) and Toronto Statement (2009) extended this norm to other large-scale community resource projects, introducing a tripartite model of responsibility among data producers, data users, and funding agencies.[^8] Meanwhile, a growing body of evidence that many published findings could not be reproduced (only 36% of 100 psychology studies replicated in a landmark 2015 project) gave funders a powerful argument for requiring data to be shared alongside results.[^9]

## The open science movement and its policy landscape

The term 'open science' gained traction in the 2010s, but its roots are older. The Budapest Open Access Initiative (2002) and the Berlin Declaration (2003), together with the Bethesda Statement (2003), established the foundational case that publicly funded research outputs should be freely available. These 'BBB declarations' defined open access and set in motion two decades of policy development.[^10]

The FAIR principles, published in 2016, shifted the conversation from simple availability to structured usability: data should be Findable, Accessible, Interoperable, and Reusable.[^11] A European Commission study estimated the annual cost of not having FAIR research data at EUR 10.2 billion. FAIR has since been adopted by Horizon Europe, the NIH, the G7, and the Australian Research Data Commons, and extended to research software through the FAIR4RS principles (2022).

These frameworks are now converging into a global policy consensus. The UNESCO Recommendation on Open Science, adopted unanimously by all 193 member states in 2021, established the first international normative framework for open science.[^12] Plan S, launched by European funders in 2018, requires immediate open access to publications with no embargo period. The 2022 Nelson Memo directed all US federal agencies to eliminate publication embargo periods by the end of 2025. Infrastructure is following policy: the European Open Science Cloud (EOSC) aims to make FAIR data practices the operational default for European research.

??? example "Open science in practice at research institutes"
    For an institute like CMI, which works across disciplines and geographies, open science raises specific questions. How do you share qualitative interview data without compromising participant confidentiality? How do you respect the data sovereignty of communities in the Global South while meeting European funder mandates? These are not abstract dilemmas; they shape day-to-day decisions about what to deposit, where, and under what conditions.

## Power, provenance, and the politics of sharing

Any honest account of knowledge sharing must reckon with its politics. Colonial-era natural history expeditions systematically extracted specimens, vocabularies, and cultural artefacts from colonised peoples and deposited them in European institutions, often without consent or attribution. As Linda Tuhiwai Smith argued in *Decolonizing Methodologies* (1999), Western research paradigms have historically served colonial interests, and that legacy shapes who controls research data and who benefits from its reuse.[^13]

The response has been substantive. Canada's First Nations articulated the OCAP Principles (Ownership, Control, Access, Possession) in 1998. Aotearoa New Zealand's Te Mana Raraunga (Māori Data Sovereignty Network), founded in 2015, became a global model for indigenous data governance. The CARE Principles for Indigenous Data Governance (2019), developed by the Global Indigenous Data Alliance, provide an internationally applicable complement to FAIR: Collective Benefit, Authority to Control, Responsibility, Ethics.[^14] Where FAIR addresses how to make data technically usable, CARE asks who has the right to govern it. The two frameworks are complementary, not competing; FAIR's 'Accessible' does not mean 'open to everyone', and data can be both FAIR and access-controlled.

Operational tools are emerging to put these principles into practice. The Local Contexts initiative has developed Traditional Knowledge Labels and Biocultural Labels, allowing indigenous communities to express culturally specific conditions of use for digital heritage materials. The San peoples of southern Africa published their own Code of Research Ethics in 2017.[^15] These are not marginal developments; they are reshaping how repositories, funders, and ethics committees approach data governance worldwide.

!!! warning "Openness is not always ethical"
    Data sharing is the default aspiration in most funder policies, but it is not an unconditional good. Sharing sensitive data without adequate safeguards can cause harm. Sharing data extracted from vulnerable communities without their involvement in governance can reproduce colonial dynamics. The question is not simply 'should you share?' but 'how, with whom, and on whose terms?'

## Why this history matters for your work

You do not need to become a historian of science to manage your data well. But knowing that data sharing has always been shaped by technology, power, and institutional norms helps you navigate the present landscape with more confidence. When a funder asks for a Data Management Plan (DMP), they are drawing on a policy lineage that stretches from the Bermuda Principles through the OECD guidelines to the UNESCO Recommendation. When a repository asks you to assign a Digital Object Identifier (DOI) and structured metadata, they are extending practices that Callimachus would have recognised.

The tools and expectations will continue to evolve. What remains constant is the underlying logic: research that others can examine, reuse, and build upon is research that earns trust.

[^1]: Lionel Casson, *Libraries in the Ancient World* (Yale University Press, 2001).
[^2]: Sukumar Dutt, *Buddhist Monks and Monasteries of India* (George Allen & Unwin, 1962). See also Xuanzang's seventh-century account in *Da Tang Xiyu Ji*.
[^3]: Shamil Jeppie and Souleymane Bachir Diagne (eds.), *The Meanings of Timbuktu* (HSRC Press, 2008).
[^4]: Dimitri Gutas, *Greek Thought, Arabic Culture: The Graeco-Arabic Translation Movement in Baghdad and Early Abbasid Society* (Routledge, 1998).
[^5]: Jonathan A. C. Brown, *Hadith: Muhammad's Legacy in the Medieval and Modern World* (Oneworld, 2009).
[^6]: Anne Goldgar, *Impolite Learning: Conduct and Community in the Republic of Letters, 1680–1750* (Yale University Press, 1995). On digital mapping of correspondence networks, see Howard Hotson and Thomas Wallnig (eds.), *Reassembling the Republic of Letters in the Digital Age* (Göttingen University Press, 2019).
[^7]: Adrian Johns, *The Nature of the Book: Print and Knowledge in the Making* (University of Chicago Press, 1998).
[^8]: Toronto International Data Release Workshop Authors (2009). 'Prepublication data sharing.' *Nature*, 461(7261), 168–170.
[^9]: Open Science Collaboration (2015). 'Estimating the reproducibility of psychological science.' *Science*, 349(6251), aac4716.
[^10]: Budapest Open Access Initiative (2002). Available at budapestopenaccessinitiative.org.
[^11]: Wilkinson, M. D. et al. (2016). 'The FAIR Guiding Principles for scientific data management and stewardship.' *Scientific Data*, 3, 160018.
[^12]: UNESCO (2021). *UNESCO Recommendation on Open Science*. 41st General Conference, 41 C/Res. 24.
[^13]: Linda Tuhiwai Smith, *Decolonizing Methodologies: Research and Indigenous Peoples* (Zed Books, 1999; 3rd ed. Otago University Press, 2021).
[^14]: Carroll, S. R. et al. (2020). 'The CARE Principles for Indigenous Data Governance.' *Data Science Journal*, 19(1), 43. See also Carroll, S. R. et al. (2021). 'Operationalizing the CARE and FAIR Principles for Indigenous data futures.' *Scientific Data*, 8, 108.
[^15]: South African San Institute (2017). *San Code of Research Ethics*. Available at trust-project.eu/san-code-of-research-ethics.
