---
icon: lucide/archive-restore
title: "Project closure"
description: "Close your project systematically: finalise the data inventory, decide what to keep and what to delete, update compliance records, and leave a clear trail for the future."
tags:
  - Closure
  - Archiving
  - Deletion
  - Compliance
  - Data inventory
  - DMP
notes: ""
date_updated: 2026-07-02
---

# Project closure

*Project closure is when data management decisions become permanent. Data is either preserved or deleted; documentation is finalised; access is revoked. A structured process ensures nothing drifts into ambiguity: no datasets lingering in uncertain states, no documentation left incomplete, no former collaborators retaining access they no longer need. Start planning at least three months before the project ends.*

## Why closure matters

During the project, many data management decisions are provisional. You store data in a working location, grant access to collaborators, and maintain documentation that is 'good enough for now'. Closure is when you settle these open questions. If you skip it, the consequences tend to surface later:

- A funder audit requests documentation of how data was handled.
- A data subject exercises their rights and the project cannot locate the relevant records.
- A team member leaves and nobody knows where project data is stored or what agreements govern it.
- Years later, datasets sit on shared drives with no clear owner, no retention decision, and no record of what consent was given.

The time to address these questions is while the project team is still together and the details are fresh.

## When to start

Begin closure planning approximately **three months before the anticipated project end**. This allows time for:

- Confirming the project timeline and any outstanding tasks
- Identifying funder deliverables and deadlines
- Planning data disposition for each dataset
- Completing documentation without rushing

If your project receives an extension, adjust the closure timeline accordingly.

## Finalise the data inventory

The [data inventory](data-inventory.md) is the backbone of closure. Review it against reality and update it to reflect the final state of the project.

| Field | What to check |
|-------|---------------|
| **Status** | Update each dataset to its final status: Complete, Archived, Deleted, or Deposited |
| **Storage location** | Confirm where each dataset currently lives; update if it has been moved |
| **Retention plan** | Confirm the decision: delete, archive internally, deposit externally, or transfer |
| **Retention period** | Specify end dates where applicable (e.g. "Delete by 31 December 2030") |
| **Documentation links** | Verify all links are functional; attach final versions of information letters, consent forms, and agreements |

Ask yourself:

- Are all datasets from the original inventory accounted for?
- Were any additional datasets created that were not in the original plan?
- Does the final state match what was described in consent forms and participant information sheets?
- Are retention decisions consistent with the legal basis for processing and with funder requirements?

!!! tip "Close the gap between plan and reality"
    Most projects diverge from their original DMP in some way: an unexpected dataset, a changed storage arrangement, a partner who dropped out. Closure is the moment to reconcile the plan with what actually happened. The final documentation should describe the project as it was, not as it was intended to be.

## Decide the fate of each dataset

Every dataset needs a clear disposition decision. There are four options. The retention obligations and destruction procedures behind them are covered at the [PRESERVE](lifecycle-9-preserve.md) stage.

### Delete

Delete data when retention is no longer justified: personal data where consent was limited to the project period, identifiable data that has served its purpose, or working files with no ongoing value.

When you delete:

- Confirm that deletion is consistent with consent and your legal basis for processing.
- Delete from **all** locations: primary storage, backups, and local copies.
- Document what was deleted, when, by whom, and the method used.
- Retain the documentation of deletion (not the data itself).

!!! warning "Deletion means all copies"
    Deleting a file from the project folder while a copy remains on someone's laptop or in an old backup does not constitute deletion under the GDPR. Account for all copies when executing a deletion decision.

### Archive internally

Retain data at CMI for a specified period when there is ongoing research value, a funder retention requirement, or a legal obligation. Set a clear retention end date and restrict access to those who need it.

- Move data to a designated archive location with appropriate access controls.
- Set a calendar reminder for the retention review date.
- Document the archive location, who has access, and the retention end date.

### Deposit externally

Publish data to a repository when you have an open data commitment, a funder requires deposit, or the data has reuse value. See the [PUBLISH](lifecycle-8-publish.md) stage for guidance on choosing a repository and preparing data for deposit.

- Select the appropriate repository for the data type.
- Prepare data for deposit: anonymisation if needed, documentation, metadata.
- Complete the deposit and obtain a persistent identifier (DOI).
- Record the repository, identifier, access conditions, and any embargo in the data inventory.

### Transfer

Transfer data to a partner institution or successor when a collaborator continues the work, or when the terms of a commissioned research agreement require it.

- Document the transfer: what was transferred, to whom, when, and under what terms.
- Ensure a data sharing or transfer agreement is in place.

## Update the DMP

Update your Data Management Plan to reflect what **actually happened**, not just what was planned. The final DMP should cover:

| Section | What to update |
|---------|----------------|
| **Data description** | Confirm the data actually collected; note any deviations from the original plan |
| **Storage** | Document where data was stored during the project |
| **Access** | Record who had access and any issues encountered |
| **Preservation** | Final disposition of each dataset |
| **Sharing** | What was or will be shared; repository details and identifiers |

If your funder requires a final DMP (as Horizon Europe and the Research Council of Norway do), the updated internal version feeds directly into the funder submission.

## Close compliance records

### Sikt notification

If you registered a [Sikt](https://sikt.no/en) notification for the project, update it to reflect the project's completion.

| Scenario | Action |
|----------|--------|
| Project complete, data deleted | Close the notification; confirm the end date |
| Project complete, data archived | Update the notification with the new end date reflecting the retention period |
| Data deposited in a repository | Update the notification to reflect new storage; close if data is fully anonymised |

### Other compliance obligations

- **REK:** Notify if required by your approval conditions.
- **Data processing agreements:** Confirm that processor obligations have been fulfilled; retain agreements for your records.
- **Data sharing agreements:** Confirm terms have been met; note any ongoing obligations.

## Review and revoke access

Review who currently has access to project data and storage. The default at closure is to **revoke access unless there is an explicit reason to retain it**.

For external collaborators and guests:

- List everyone with access to the project workspace.
- For each person, determine whether continued access is needed and for how long.
- Remove access for anyone no longer involved.
- Document who retained access and the justification.

!!! tip "Do not leave access open by default"
    It is easier to restore access for someone who needs it later than to discover, months after project close, that a former collaborator still has unrestricted access to sensitive data. Review access proactively.

## Bundle funder deliverables

If the project has external funding, check the grant agreement for end-of-project requirements and assemble the necessary documentation.

| Funder | Typical requirements |
|--------|---------------------|
| **Research Council of Norway** | Final DMP; data deposit confirmation; publication list |
| **Horizon Europe** | Updated DMP; FAIR data documentation; open access confirmation |
| **ERC** | Data management summary; repository deposit confirmation |
| **Other funders** | As specified in the grant agreement |

## Closure checklist

Use this checklist to confirm that all closure tasks are complete.

**Data inventory**

- [ ] All datasets accounted for
- [ ] Final status confirmed for each dataset
- [ ] Disposition decision documented for each dataset
- [ ] Documentation links verified and up to date

**Data disposition**

- [ ] Deletions executed and documented
- [ ] Internal archives established with access controls and retention dates
- [ ] Repository deposits completed with metadata and persistent identifiers (where applicable)
- [ ] Transfers completed with agreements in place (where applicable)

**Documentation**

- [ ] DMP updated to reflect actual practice
- [ ] Funder deliverables assembled (where applicable)

**Compliance**

- [ ] Sikt notification updated or closed
- [ ] REC notified (where applicable)
- [ ] Data processing agreement obligations confirmed fulfilled

**Access**

- [ ] External collaborator access reviewed
- [ ] Unnecessary access revoked
- [ ] Remaining access documented with justification

## After closure

Once the project is formally closed:

- Archived project materials remain accessible (read-only) to the core project team.
- If a data subject exercises their rights, use the archived records to respond.
- If a funder requests documentation during an audit, the archived project workspace and final DMP provide the evidence.
- When the retention period expires for archived data, review and delete if retention is no longer justified.

A well-closed project requires no further effort. A poorly closed project generates reactive work for years.
