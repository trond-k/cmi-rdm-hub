# Research Data Management at CMI: Approach Overview

## Context

CMI is a research institute of approximately 70–80 researchers, initiating a handful of new projects each year (typically 5–15). The project portfolio is diverse: qualitative and quantitative methods, single-researcher studies and large consortia, domestic and international fieldwork, varied funders with different requirements.

This context shapes the RDM approach:
- **Scale allows individual attention:** Each new project can be assessed individually; automation is neither necessary nor desirable for most tasks
- **Complexity resists templates:** No single workflow fits all projects; flexibility and judgment are essential
- **Researcher autonomy matters:** CMI researchers are experts in their fields; RDM should support their work, not constrain it

## The Challenge

Research data management exists in tension:

| Pressure Toward More Structure | Pressure Toward Less Structure |
|-------------------------------|-------------------------------|
| Funder requirements (DMPs, open data) | Researcher time is scarce |
| GDPR and Sikt compliance | Administrative burden is resented |
| Institutional risk management | Complexity varies; one-size-fits-all doesn't work |
| Knowledge preservation when staff leave | "It's worked fine so far" |

The traditional responses—either heavy compliance frameworks or benign neglect—both fail. Heavy frameworks create burden without proportionate benefit. Neglect works until it doesn't: an audit, a data subject request, a departing PI, a funder question.

## The CMI Approach: Machine-in-the-Loop

This RDM framework takes a middle path: **structured visibility with minimal researcher burden**, enabled by machine assistance.

### Core Principles

**1. Low effort, high return**

Researchers invest modest time (primarily verification and confirmation); rdm@cmi and LLM tools do the drafting and preparation. The system produces tangible outputs: ready-to-use information letters, pre-filled Sikt notifications, customised DMPs.

**2. Machine-in-the-loop, not human-in-the-loop**

LLMs and automated tools assist rdm@cmi by:
- Parsing proposals to identify data entities
- Suggesting classifications and flagging sensitivities
- Drafting document bundles based on project parameters
- Pre-filling templates with project-specific details

Humans (rdm@cmi, researchers, DPO) validate, adjust, and approve. The machine accelerates; the human decides.

**3. Make the implicit explicit**

Projects involve data, but proposals rarely articulate data entities, flows, responsibilities, and pipelines clearly. The RDM process surfaces these assumptions early—when they can be addressed—rather than late, when they become problems.

**4. Proportionate response**

Low-risk projects get light-touch treatment. High-risk projects get more attention. The framework scales to project needs, not institutional anxiety.

**5. Support, not surveillance**

The data inventory and tracking mechanisms exist to help projects, not monitor researchers. They provide structure when structure is useful and stay out of the way otherwise.

## The Value Proposition

**For researchers:**

| You Invest | You Receive |
|------------|-------------|
| ~30 min at project start (review inventory and assumptions) | Pre-filled, customised information letters |
| ~15 min at milestones (update status, confirm details) | Pre-filled Sikt notification (ready to submit) |
| Brief responses to rdm@cmi queries | Project-specific DMP (Light-DMP always; funder format where needed) |
| | Ethics summary and storage recommendations |
| | Clear documentation trail if questions arise later |
| | Support at project closure |

**For the institution:**

- Reduced risk of compliance failures
- Knowledge preservation when staff transition
- Ability to respond to audits and data subject requests
- Institutional overview without micromanagement
- Consistent baseline across projects

**The bargain:**

> A modest, structured investment in visibility—mostly handled by rdm@cmi with researcher verification—reduces reactive burden later and provides ready-to-use, project-specific documentation.

## What This Approach Is Not

- **Not a compliance checkbox exercise:** Documentation exists to be useful, not to satisfy bureaucrats
- **Not surveillance:** We track data entities and project status, not researcher activity
- **Not one-size-fits-all:** Recommendations are tailored to project scale, sensitivity, and risk
- **Not an autonomy grab:** Researchers make research decisions; rdm@cmi provides data management support
- **Not an attempt to automate judgment:** Machines draft and suggest; humans decide

## How the Recommendations Fit Together

```
┌─────────────────────────────────────────────────────────────────┐
│  Recommendation #1: Teams-based Project Structure               │
│  → Every project has a dedicated Team with standard channels    │
│  → Foundation for access control, collaboration, RDM integration│
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Recommendation #2: Initial Assessment & Classification         │
│  → rdm@cmi assesses new projects at intake                      │
│  → Identifies data entities, sensitivity, risk, compliance needs│
│  → LLM-assisted; human-verified                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Recommendation #3: Data Inventory                              │
│  → Structured list of data entities in each project             │
│  → Makes implicit data flows and responsibilities explicit      │
│  → Links to documentation; tracks status at milestones          │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Recommendation #4: Embedded RDM & Document Bundle              │
│  → RDM channel in each Team with tailored documentation         │
│  → Pre-filled templates: info letters, consent, DMP, Sikt, etc. │
│  → Light-touch presence; available for questions                │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  Recommendation #5: Project Closure                             │
│  → Final documentation generated                                │
│  → Retention/deletion/archival confirmed                        │
│  → Funder deliverables bundled                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Key Roles

| Role | Responsibilities |
|------|------------------|
| **rdm@cmi** | Intake assessment, classification, document generation, milestone check-ins, guidance, project closure support |
| **PI / Project Coordinator** | Verify assumptions, approve classifications, update inventory at milestones, ensure team compliance |
| **Project Team** | Follow storage/security recommendations, use provided templates, flag changes or issues |
| **DPO / Compliance** | Consulted on complex cases: DPIA, controller/processor questions, high-risk situations |
| **IT** | Team creation, template management, security configurations, technical support |

## Implementation Philosophy

**Start simple, iterate:**
- Begin with new projects; don't attempt to retrofit everything at once
- Refine templates and processes based on experience
- Add complexity (e.g., central dashboards) only when value is demonstrated

**Embrace imperfection:**
- Preliminary classifications are expected to be adjusted
- Documentation is "good enough," not perfect
- The goal is useful structure, not comprehensive bureaucracy

**Measure success by researcher experience:**
- Do researchers find the document bundle useful?
- Is the burden perceived as proportionate to the benefit?
- Are compliance tasks easier than before?

If the answer is no, adjust the approach.