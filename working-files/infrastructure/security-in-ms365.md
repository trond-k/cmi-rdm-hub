---
icon: lucide/cloud
tags:
  - GDPR
---

# Security in Microsoft 365

*Trond Kvamme · draft · March 2026*

CMI runs on Microsoft 365 E5. Your files, emails, Teams messages, and SharePoint sites all live in Microsoft's cloud. This page explains what M365 does and does not protect you from, what the CLOUD Act is, and when you should consider keeping data elsewhere.

This is not an IT manual. It is a researcher's guide to understanding the security properties of the infrastructure you use every day.


## What encryption means in M365

Microsoft encrypts your data in two ways:

**In transit.** When you upload a file, send an email, or join a Teams call, the data is encrypted while it moves between your device and Microsoft's servers. This is standard HTTPS — the same encryption your browser uses for online banking. It prevents anyone who intercepts the traffic (on a hotel Wi-Fi, for instance) from reading the content.

**At rest.** When your file sits on a OneDrive or SharePoint server, it is encrypted on disk. If someone physically stole a hard drive from a Microsoft data centre, they could not read your files.

Both forms of encryption are automatic. You do not need to do anything to enable them, and you cannot accidentally turn them off.

### What encryption does *not* do

Encryption at rest protects against physical theft of hardware. It does not protect against access by someone who holds the keys — and Microsoft holds the keys. This is the normal arrangement for any cloud service: the provider encrypts your data, but the provider can also decrypt it, because they need to in order to deliver the service (search, indexing, malware scanning, and so on).

This means:

- Microsoft employees with sufficient access *could*, in principle, read your files. Microsoft has controls to prevent this (access logging, just-in-time access, background checks), but the technical capability exists.
- A court order or government request directed at Microsoft *could* compel them to hand over your data in readable form.

For the vast majority of CMI research, this is an acceptable risk — the same risk you accept when using any managed cloud service. But for a small number of projects, it matters. See the CLOUD Act section below.

!!! info "Customer Key — an additional layer CMI can enable"
    M365 E5 includes a feature called **Customer Key** that lets CMI manage its own encryption keys on top of Microsoft's encryption. With Customer Key enabled, even if Microsoft were compelled to hand over data, they would be handing over data encrypted with keys only CMI controls.

    This is a significant additional safeguard. Whether CMI has enabled Customer Key is a question for IT — it requires key management infrastructure and operational procedures.


## Where your data lives

CMI's M365 tenant is configured within Microsoft's **EU Data Boundary**. This means your data is stored and processed in data centres located in the EU and EFTA — not in the United States or elsewhere. For day-to-day operations, your data does not leave Europe.

This matters for GDPR compliance. The EU Data Boundary means CMI is not performing a third-country transfer simply by using M365 — the data stays within the EEA.

However, data residency and legal jurisdiction are not the same thing. Your data may be stored in Ireland or Norway, but the company that controls the infrastructure is American. This is where the CLOUD Act enters the picture.


## The CLOUD Act

The **Clarifying Lawful Overseas Use of Data Act** (2018) is a US law that allows US law enforcement and intelligence agencies to compel US-based technology companies to hand over data — regardless of where that data is physically stored. If your data is on a Microsoft server in Dublin, a US court can still issue an order requiring Microsoft to produce it.

### How realistic is this risk?

For most CMI research, the realistic risk of a CLOUD Act request is very low. US authorities are not interested in interview transcripts from a governance study in Tanzania or survey data about fisheries management in Myanmar. The CLOUD Act is primarily used in criminal investigations and national security cases.

The risk becomes more relevant when research touches areas where US interests are directly engaged:

- **Corruption and governance** in countries where US foreign policy is active
- **Sanctions-related contexts** — research involving individuals, organisations, or countries under US sanctions
- **Defence, security, and intelligence topics** — even from an academic perspective
- **Research involving US persons** or US-based institutions in sensitive contexts

If your project involves these areas, it is worth discussing storage alternatives with the RDM adviser.

### What Microsoft says

Microsoft has publicly committed to challenging government requests for EU customer data. They publish transparency reports on the number and type of requests received. As of their public statements, Microsoft has not disclosed EU customer data under the CLOUD Act.

These commitments are meaningful but not legally binding in the way that, say, an encryption key is. A sufficiently determined US government request, backed by a court order, would be difficult for Microsoft to resist indefinitely.

### CMI's position

M365 with EU Data Boundary is adequate for the large majority of CMI research — Green, Yellow, and most Red-tier data. The CLOUD Act is a theoretical exposure that should be assessed proportionally, not a reason to avoid M365 altogether.

For projects where CLOUD Act exposure is specifically concerning, alternatives exist (see below).


## The political climate: European digital sovereignty

The CLOUD Act concern is not new, but it has become more prominent since 2022. Several developments have sharpened the debate:

- **Schrems II** (2020): the EU Court of Justice invalidated the EU–US Privacy Shield, finding that US surveillance laws do not provide adequate protection for EU personal data. The subsequent **EU–US Data Privacy Framework** (2023) partially restored transatlantic data flows, but its long-term stability is uncertain — a "Schrems III" challenge is widely expected.
- **European public sector caution**: several EU member states and public institutions have begun restricting or re-evaluating their use of US cloud services. France, Germany, and the Netherlands have been particularly active. The European Data Protection Supervisor has questioned whether EU institutions should use M365 at all.
- **Sovereign cloud initiatives**: the EU is investing in European cloud alternatives (Gaia-X, national government clouds) to reduce dependence on US hyperscalers. Norway's approach has been more pragmatic — public sector use of M365 is widespread — but the direction of travel in Europe is toward greater scrutiny.

For CMI, the practical implication is not that M365 is suddenly unsafe. It is that the regulatory and political landscape is shifting, and decisions about where to store research data — particularly sensitive research data — should be made with awareness that what is considered adequate today may face additional scrutiny tomorrow.


## When to consider alternatives

M365 is CMI's default infrastructure and is appropriate for most work. Consider alternatives when:

| Scenario | Why | Options |
|---|---|---|
| Research topics with potential US interest (corruption, sanctions, governance in strategically sensitive countries) | CLOUD Act exposure is specifically relevant | TSD, Tresorit, Proton Drive |
| Participant safety depends on data not being accessible to any government | Zero-knowledge encryption needed | Tresorit, Proton Drive, encrypted local storage |
| Funder or ethics board requires non-US infrastructure | Compliance requirement | TSD (Norwegian sovereign infrastructure) |
| Data collection via online surveys with identifiable participants | Integrated GDPR-compliant collection and storage | TSD / Nettskjema |
| Black-tier data (any reason) | Requires case-by-case security assessment | See [Data Security](../../institutional/data-security.md) |

These alternatives involve additional cost and setup. The decision should be proportional — based on an honest assessment of the specific risks your project faces, not on a general anxiety about cloud services.

!!! tip "The practical test"
    Ask yourself: if a US law enforcement agency obtained a copy of this dataset, what could actually happen? If the answer is "nothing meaningful" — because the data is anonymised, or concerns topics of no US interest, or involves no one who could be harmed by US government attention — then M365 is fine. If the answer gives you pause, talk to the RDM adviser.


## What you can do today

Regardless of where your data is stored, these practices improve your security in M365:

1. **Use Teams channels with restricted membership** for project data — not broad, institute-wide channels.
2. **Apply sensitivity labels** when they become available (CMI is piloting these). Labels enforce encryption and access restrictions automatically.
3. **Don't share via links** unless you've set the right permissions. "Anyone with the link" is almost never appropriate for research data.
4. **Review access when people leave** the project. Remove former team members from SharePoint sites and Teams channels.
5. **Don't email research data** as attachments. Share a link to the file in its secure location instead.
6. **Keep personal data out of file names.** A file called `Interview_Ahmed_Mogadishu_corruption.docx` on a shared drive is a problem regardless of encryption.


*[M365]: Microsoft 365
*[DPA]: Data Processing Agreement
*[EEA]: European Economic Area
*[EFTA]: European Free Trade Association
*[TSD]: Tjenester for Sensitive Data — Norwegian national infrastructure for sensitive research data
*[PI]: Principal Investigator
*[DMP]: Data Management Plan
*[CLOUD Act]: Clarifying Lawful Overseas Use of Data Act
