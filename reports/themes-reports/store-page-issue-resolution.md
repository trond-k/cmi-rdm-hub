# STORE page: resolving "check it yourself" issues

**Date:** 2026-03-26
**Source:** `docs/lifecycle-5-store.md`
**Purpose:** The STORE page should give researchers answers, not assign them more tasks. This report identifies every instance where the page tells researchers to check, consider, discuss, or investigate something themselves, and proposes concrete resolutions drawn from existing hub documentation and CMI infrastructure knowledge. Items that cannot be fully resolved are flagged.

---

## Issue 1: When is MS365 E5 sufficient vs when to escalate to TSD?

**Current text (lines 22–23, 34, 36):**

> "Before looking elsewhere, check whether the standard setup meets your needs."
> "consider a dedicated secure environment"
> "TSD is appropriate when your Data Protection Impact Assessment (DPIA) or institutional policy requires a higher level of protection"

**Problem:** Researchers are told to "check" and "consider" but have no criteria for the decision. The DPIA reference is circular — it assumes researchers already know when a DPIA triggers a move to TSD.

**Resolution — replace with a decision rule:**

MS365 E5 is sufficient when:

- The data contains no GDPR special-category personal data (health, political opinions, ethnic origin, biometric data, religious beliefs, trade union membership, genetic data, sexual orientation).
- The data does not involve elevated contextual risk (conflict zones, authoritarian settings, vulnerable populations where identification could cause retaliation or harm).
- Access can be adequately controlled through SharePoint permissions and the E5 conditional access policies.

Escalate to TSD when any of the following apply:

- The dataset contains GDPR special-category data.
- A DPIA has been completed (or is required) and its outcome indicates that MS365 access controls are insufficient — for example, because the data combines special-category variables with contextual identifiers, or because the research context involves surveillance risk.
- The project processes personal data from conflict-affected or authoritarian settings where a breach could result in physical danger, legal repercussions, or retaliation against participants.
- Institutional policy or a partner agreement requires an isolated environment with Norwegian data residency and no cloud synchronisation to external devices.

If uncertain, the default for CMI projects involving personal data from sensitive contexts should be TSD, not MS365. It is easier to relax restrictions than to move data to a more secure environment after collection has started.

**Source:** Synthesised from `lifecycle-1-frame.md` (sensitivity screening), `lifecycle-3-plan.md` (DPIA triggers, GDPR special categories), and `cmi-institutional-context.md` (elevated risk in CMI contexts).

---

## Issue 2: What to do about large files that exceed MS365 limits

**Current text (lines 40–42):**

> "SharePoint has per-file and per-library size limits that may not accommodate raw video or satellite imagery. Discuss options with CMI's IT team early, before collection produces files that have nowhere to go."

**Problem:** "Discuss options with CMI's IT team" is a task, not an answer. The researcher gets no information about what options exist, what thresholds matter, or what to ask for.

**Partial resolution — provide the thresholds and known options:**

SharePoint limits to be aware of:

- Maximum file size for upload: 250 GB per file (Microsoft 365).
- Maximum library storage: depends on tenant allocation (default 25 TB per site collection, expandable on request).
- Sync client limitations: files over ~10 GB can cause sync reliability issues; very large file counts (>300,000) in a single library slow sync performance.

For projects that will exceed these practical limits (common with raw video, high-resolution geospatial imagery, or large survey datasets with audiovisual components):

- **TSD** supports large file storage and transfer via its data lock mechanism and can handle datasets that are impractical in SharePoint. If the data is also sensitive, TSD is the obvious choice.
- **NIRD (National Infrastructure for Research Data)**, operated by Sigma2/Sikt, provides project-based research data storage for large datasets. Access is applied for through the Sigma2 resource allocation process.
- **Institutional network storage** (if available via CMI's IT) may provide higher-throughput access for local processing of large files.

> [!FLAG] **Needs CMI IT input:** The specific availability of NIRD allocations for CMI projects and any institutional network storage options should be confirmed with IT. The page should name the concrete options available rather than directing researchers to "discuss."

**Source:** Microsoft 365 service descriptions (public documentation); Sigma2/Sikt service descriptions; `reports/README.md` (CMI infrastructure defaults).

---

## Issue 3: Where exactly to store the key file for pseudonymised data

**Current text (lines 46–48, 50–51):**

> "this file should be stored in a different location with more restrictive access than the main dataset"
> "Store the key file in a separate, more restricted location, and limit access to those who genuinely need it."

**Problem:** The principle is stated twice but no concrete location is given. A researcher reading this still does not know where to put the key file.

**Resolution — provide CMI-specific placement guidance:**

| Main dataset location | Key file location | Access |
|---|---|---|
| SharePoint (project site) | A **separate** SharePoint site (not a subfolder of the project site) with permissions restricted to the PI and named data custodians only | Remove inheritance from the project site; do not grant team-wide access |
| TSD | A **separate TSD project** or a restricted directory within TSD accessible only to the PI | Use TSD's built-in access management; do not place key file in the same project directory as the pseudonymised data |
| Field devices (temporary) | Encrypted USB drive held by the PI or designated fieldwork lead, physically separate from the device holding the research data | Transfer to the permanent secure location as soon as connectivity allows |

In all cases:

- Record the key file location and access list in the data inventory.
- Never store the key file on a personal OneDrive, local laptop drive, or email.
- If the PI is the only person with access, designate one backup person (e.g., co-PI or CMI data protection contact) who can access it if the PI is unavailable.

**Source:** Synthesised from `data-inventory.md` (documenting storage locations and access), `lifecycle-3-plan.md` (responsibility assignment), and the STORE page's own principles.

---

## Issue 4: What to actually do when built-in backup is insufficient

**Current text (lines 57–63):**

> "Consider whether your project needs additional protection in the following situations: [list of three scenarios]. [...] Carry encrypted portable storage as a fallback when internet access is unreliable."

**Problem:** The page lists when additional backup is needed but not what to do about it. "Carry encrypted portable storage" is mentioned in passing without explaining what that means.

**Resolution — provide concrete backup protocols for each scenario:**

**Scenario A: Data on field devices before upload**

- At the end of each collection day, copy all new files from the collection device to an encrypted USB drive or portable SSD. This creates an immediate second copy.
- Transfer files from the device to the project's SharePoint or TSD environment as soon as internet access allows. Once the upload is confirmed and verified, the USB copy serves as a transit backup only.
- For audio/video recording devices that do not support encryption: transfer files to an encrypted laptop (BitLocker on Windows, FileVault on macOS) before the end of the day, then to an encrypted USB as a second copy.

**Scenario B: Data in environments outside MS365**

- TSD: has its own institutional backup infrastructure (automated snapshots and replication). No additional action needed by the researcher, but confirm with TSD documentation that backup covers your specific project space.
- External partner systems: include backup responsibilities in the data sharing agreement. Verify that the partner's system has backup provisions. Keep a local encrypted copy of data received from partners.
- Specialist databases or platforms: export data at regular intervals (weekly or after major updates) and store the export in the project's SharePoint or TSD environment.

**Scenario C: Irreplaceable data (unique recordings, one-time surveys)**

- Maintain at least two copies on physically separate media at all times during fieldwork. Example: one copy on the recording device and one on an encrypted USB held by a different team member.
- Designate one person per field team as backup responsible (per DMP roles table).
- For one-time survey responses collected via mobile platforms (KoBoToolbox, ODK): confirm that server-side storage is active before collection begins, so that responses are transmitted as they are submitted. If working offline, sync at the earliest opportunity and verify record counts.

**What "encrypted portable storage" means in practice:**

- **Software-encrypted USB drives:** Format a standard USB drive with BitLocker (Windows) or APFS encryption (macOS). Cost-effective; requires the researcher to set a strong passphrase.
- **Hardware-encrypted USB drives:** Devices such as Kingston IronKey or iStorage datAshur provide built-in encryption with physical keypads. More robust against tampering; useful when devices may be inspected at borders or checkpoints.
- **Encrypted portable SSDs:** Samsung T7 Shield or similar, with built-in AES 256-bit encryption. Suitable for larger datasets (video, audio archives).

In all cases, test that the encrypted drive can be read on the devices you will use in the field before departure.

**Source:** `lifecycle-4-collect.md` (field transfer protocols, equipment guidance), `lifecycle-3-plan.md` (roles and responsibilities), `reports/README.md` (CMI infrastructure: MS365 E5, TSD).

---

## Issue 5: How to test backup recovery

**Current text (lines 65–66):**

> "Periodically verify that you can actually restore a file from your backup arrangement. This is especially important before major fieldwork phases."

**Problem:** Good advice, but no instructions on how to do it.

**Resolution — provide a simple test protocol:**

Before each major fieldwork phase, run through this checklist:

1. **SharePoint/OneDrive version history:** Delete a non-critical test file from the project SharePoint site. Restore it from the SharePoint recycle bin. Confirm the file is intact and in the correct location. Then test version history: revert a test document to a previous version and confirm the content matches.
2. **Encrypted USB backup:** Copy a sample file to the encrypted USB. Eject the drive, connect it to a different device, unlock it, and confirm the file opens correctly.
3. **TSD (if applicable):** Confirm with TSD support that your project space is covered by the automated backup regime. If TSD provides user-accessible snapshots, restore a test file and verify.
4. **Field equipment chain:** Run the full transfer workflow — record a short test clip on the recording device, transfer it to the encrypted laptop, copy to the USB backup, and upload to cloud storage. Confirm all four copies are present and playable.

Document the test date and outcome in the project README or data inventory. If any step fails, resolve the issue before fieldwork begins.

**Source:** Original guidance in the STORE page, extended with practical steps.

---

## Issue 6: What shared platforms and protocols to use with external partners

**Current text (lines 83):**

> "agree on a shared platform and transfer protocol before data starts flowing"

**Problem:** Researchers are told to agree but not given any options to choose from.

**Resolution — provide a decision framework:**

| Partner situation | Recommended platform | Notes |
|---|---|---|
| Partner has MS365 (institutional licence) | SharePoint with guest access | Simplest option; partner gets direct access to a shared document library with CMI's access controls. Guest access must be configured by IT. |
| Partner lacks MS365 but data is not highly sensitive | SharePoint guest links with expiration + password, or a shared cloud folder (e.g. Tresorit for encrypted transit) | Avoid unencrypted consumer services (Dropbox, Google Drive) for personal data. |
| Partner in a context with surveillance risk or data is GDPR special-category | Tresorit or ProtonDrive for encrypted file exchange; TSD for processing and storage on the CMI side | End-to-end encryption protects data in transit. These are transit/collaboration tools, not long-term storage. |
| Shared code, scripts, or analytical workflows | GitHub or GitLab (private repository) | Add collaborators by username; do not store research data in the repository. |
| Large dataset transfer (tens of GB+) | NIRD/Sigma2 project storage with partner access, or TSD data lock for one-way transfers | For regular large transfers, agree on a scheduled transfer protocol (e.g. weekly upload via SFTP or the platform's transfer mechanism). |

In all cases:

- Document the agreed platform and transfer protocol in the DMP and data inventory.
- Agree on a file naming convention that both parties will follow (see file-and-folder-naming.md).
- Establish who is responsible for verifying that transferred files are complete and uncorrupted (e.g. checksum verification for large files).

> [!FLAG] **Needs CMI IT input:** The process for setting up SharePoint guest access for external partners (who requests it, what approval is needed, what access levels are available) should be documented. This is likely a CMI IT procedure that the page should reference rather than expect researchers to navigate independently.

**Source:** STORE page (Tresorit, ProtonDrive already mentioned), `lifecycle-4-collect.md` (equipment and tools), `lifecycle-3-plan.md` (collaboration agreements), `reports/README.md` (CMI infrastructure).

---

## Issue 7: What legal basis applies for international data transfers

**Current text (lines 90–92):**

> "The question becomes relevant when you move data outside the default infrastructure [...] If your project involves any of these, check the legal basis for the transfer before data moves. See GDPR and legal compliance."

**Problem:** "Check the legal basis" is a task with no guidance on what the options are. The referenced page (`gdpr-and-legal-compliance.md`) does not exist — it is a dead link. `CROSS-legal.md` is a placeholder stub.

**Resolution — provide the transfer mechanisms directly:**

When transferring personal data from the EU/EEA to a country outside the EU/EEA, one of the following legal mechanisms must apply:

1. **EU adequacy decision.** The European Commission has determined that the destination country provides essentially equivalent data protection. Transfers proceed as if within the EU. The current list of adequate countries includes Andorra, Argentina, Canada (PIPED Act), Faroe Islands, Guernsey, Israel, Isle of Man, Japan, Jersey, New Zealand, Republic of Korea, Switzerland, United Kingdom, and Uruguay. The US is covered under the EU-US Data Privacy Framework for certified organisations. *Always check the current EC adequacy list — it is updated periodically.*

2. **Standard Contractual Clauses (SCCs).** Pre-approved contract templates adopted by the European Commission that bind the data importer to GDPR-equivalent protections. This is the most common mechanism for transfers to non-adequate countries. SCCs must be executed between the data exporter (CMI or the controller) and the data importer (the partner institution). A Transfer Impact Assessment (TIA) should accompany the SCCs to evaluate whether the destination country's legal framework could undermine the protections.

3. **GDPR Article 49 derogations.** Narrow exceptions that allow transfers without adequacy decisions or SCCs in specific circumstances:
    - Explicit, informed consent of the data subject (must be genuinely specific and informed about the risks of the transfer).
    - Transfer necessary for performance of a contract between the data subject and the controller.
    - Transfer necessary for important reasons of public interest (recognised in EU or member state law).
    - Transfer necessary for the establishment, exercise, or defence of legal claims.
    - Transfer necessary to protect vital interests of the data subject.

    These derogations are interpreted strictly. Routine, bulk transfers of research data should not rely on Article 49; use SCCs instead.

**For most CMI projects involving partners in non-adequate countries:** SCCs are the appropriate mechanism. The data sharing agreement negotiated at the PLAN stage should incorporate SCCs as an annex or reference them directly. CMI's data protection contact can provide the current EC-approved SCC templates.

> [!FLAG] **Documentation gap:** `gdpr-and-legal-compliance.md` does not exist. `CROSS-legal.md` is a stub. This is a significant gap in the hub. The STORE page, PLAN page, and FUND page all reference it. Until this page is written, the transfer mechanism guidance above should be incorporated directly into the STORE page or into a new dedicated section.

**Source:** GDPR Articles 44–49; `lifecycle-3-plan.md` (GDPR and data protection section, collaboration agreements); `cmi-institutional-context.md` (cross-border regulatory complexity); European Commission adequacy decisions list.

---

## Issue 8: What funders actually require for active storage

**Current text (line 93):**

> "Some funders specify that data must be stored on institutional or national infrastructure during the project. Check the grant agreement."

**Problem:** "Check the grant agreement" is a task. The hub already has detailed funder reports — this information should be provided directly.

**Resolution — state the requirements from each funder:**

| Funder | Active storage requirement |
|---|---|
| **RCN** | The DMP must specify storage location, backup frequency, disaster recovery, and access controls (DMP area 5). RCN does not mandate a specific platform during the active project, but the Project Owner (CMI) must ensure "safe and secure" storage for at least 10 years after project end. For sensitive personal data during active research, TSD is the standard Norwegian solution. |
| **Horizon Europe** | The DMP must cover data security, including storage, backup, recovery, and transfer of sensitive data (DMP section 5). No specific platform is mandated during the project, but the Grant Agreement (MGA Article 17) requires that data be deposited in a trusted repository by project end. Cloud storage (OneDrive, Google Drive) is **not** acceptable as a repository — only as active working storage. |
| **ERC** | Follows Horizon Europe baseline. Same DMP data security section. Same repository requirements at project end. ERC Proof of Concept grants are exempt from open research data requirements. |
| **Norad** | No formal DMP or storage mandate. Contract terms vary by engagement. Under grants, CMI retains IP and manages data at its discretion. Under commissions (procurement), Norad may specify data handling or ownership clauses — these must be read case by case. |

**Practical implication for the STORE page:** For RCN, Horizon Europe, and ERC projects, CMI's default infrastructure (MS365 E5 for active storage, TSD for sensitive data, Sikt Research Data Archive for deposit) meets all requirements. No additional action is needed beyond configuring access controls appropriately and completing the DMP storage sections. For Norad commissions, researchers should review the specific contract terms — but this is a one-time check at project start, not an ongoing task.

**Source:** `reports/rcn-requirements.md`, `reports/horizon-europe-requirements.md`, `reports/erc-requirements.md`, `reports/norad-requirements.md`, `reports/README.md`.

---

## Issue 9: Sync conflict resolution protocol

**Current text (lines 85–86):**

> "establish a protocol for checking and resolving sync conflicts after each reconnection"

**Problem:** Minor — this is a warning admonition, and a full protocol may be excessive for the page. But the advice to "establish a protocol" is another task.

**Resolution — provide a brief protocol:**

After reconnecting from offline work:

1. Check the SharePoint/OneDrive sync status icon. A red circle or conflict warning indicates conflicting copies.
2. Open the conflicting files. SharePoint names conflict copies with the device name and timestamp (e.g., `report_v02-TKLaptop.docx`).
3. Compare the two versions. For Word documents, use Review > Compare. For spreadsheets, compare cell-by-cell or use a diff tool.
4. Merge changes into a single authoritative version. Save it with the correct filename and version number. Delete the conflict copy.
5. If unsure which version is correct, keep both temporarily and consult the other editor before resolving.

For projects with frequent offline work, designate one person to check for and resolve sync conflicts daily during fieldwork phases.

**Source:** Microsoft 365 sync documentation; common practice.

---

## Summary of flags requiring human input

| # | Issue | What is needed |
|---|---|---|
| 2 | Large file storage options | Confirm NIRD/Sigma2 availability for CMI projects; confirm any institutional network storage options via CMI IT |
| 6 | SharePoint guest access for external partners | Document the CMI IT procedure for setting up guest access |
| 7 | Missing `gdpr-and-legal-compliance.md` page | Write the page or incorporate transfer mechanism guidance directly into STORE and/or CROSS-legal.md |

---

## Recommended next steps

1. **Revise `lifecycle-5-store.md`** using the resolutions above to replace "check/consider/discuss" language with direct answers.
2. **Confirm flagged items** (issues 2, 6, 7) with CMI IT and legal/data protection contacts.
3. **Prioritise writing `gdpr-and-legal-compliance.md`** (or expanding `CROSS-legal.md`) — it is referenced by STORE, PLAN, FUND, and FRAME pages and is currently a dead link.
4. **Remove the `notes` field** from the STORE page frontmatter once issues are resolved.
