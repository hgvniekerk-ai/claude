# PE Brain: task routing

Find the PE's task, open the named contract, load only what it lists.

## Task routing

| PE is asking for | Skill | Start at |
|---|---|---|
| Network requirements, IP plan, VLANs, segmentation, firewall flows, NTP | `/pe-network` | `workflows/network-requirements/CONTEXT.md` |
| Server or hardware sizing, storage, bandwidth | `/pe-sizing` | `workflows/hardware-sizing/CONTEXT.md` |
| "Have we seen this before?", past sites, lessons, product versions on a site | `/pe-history` | `workflows/project-intelligence/01-query/CONTEXT.md` |
| Close out a project or capture a lesson | `/pe-history` | `workflows/project-intelligence/02-capture/CONTEXT.md` |
| OPC connection, bridge, run signal troubleshooting | none | `knowledge/opc/CONTEXT.md`, then `/pe-history` for past cases |
| Product or tag version question | none | `knowledge/products/versions.md` |
| A correction or new knowledge | `/pe-contribute` | `CONTRIBUTING.md` |
| A formatted Word document from a finished markdown output | `docx` skill | the workflow's `03-document` output |

A question that fits no row: answer from `knowledge/CONTEXT.md` routing, cite paths, and say which workflow would have produced it properly.

## What to load

| Task | Load | Do NOT load |
|---|---|---|
| Any workflow stage | that stage's `CONTEXT.md`, then only its Inputs table | other workflows, other projects' `work/` |
| Knowledge question | `knowledge/CONTEXT.md`, then one domain router | `projects/*/evidence/` |
| History question | `projects/INDEX.md`, `knowledge/INDEX.md`, results of `pe.py find` | whole project folders; delegate wide searches to the `evidence-scout` subagent |

## Status

A project's status is what exists in `projects/<slug>/work/`. `python3 tools/pe.py status <slug>` renders it.
