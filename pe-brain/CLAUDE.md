# PE Brain

Shared engineering workspace for Stone Three Project Engineers. A PE asks an engineering question; PE Brain routes to the right knowledge and workflow and produces source-grounded work in the project's folder.

Built on ICM: folders carry sequencing, hierarchy carries context scope, files carry state. Read `CONTEXT.md` next for task routing. Do not crawl the workspace.

## Where things live

| Folder | Holds | Layer |
|---|---|---|
| `knowledge/` | Shared, canonical engineering knowledge. One home per fact. | Factory (L3) |
| `projects/<slug>/` | One record per project: `record.md` (shared), `evidence/` (raw, local only), `work/` (inputs and generated outputs) | Product (L4) |
| `workflows/` | Pipelines with numbered stages. Each stage has a `CONTEXT.md` contract. | Contracts (L2) |
| `_system/` | Schema, source registry, decisions, findings | About the workspace |
| `_templates/` | Stamps. A new project or note is a copy, not a blank page. | About the workspace |
| `tools/pe.py` | Checks, indexes, search, IP plan validator, sizing arithmetic | Tooling |

## Rules that never bend

1. **Source every engineering claim.** Cite the file path (and section) or the external source. If no source exists, write `[TBC: what is missing, who can supply it]`. Never fill a gap with a plausible number.
2. **Check `authority:` before relying on a note.** `s3-verified` is company practice. `external` is a public standard or vendor document. `field-observed` is one project's experience. `unverified` must be flagged to the PE in the answer.
3. **Raw client evidence never leaves `projects/<slug>/evidence/`.** Do not quote it into `knowledge/`. Promote only abstracted lessons.
4. **One home per fact.** Link to the canonical note; do not copy it.
5. **Stop at each stage's human check.** Nothing moves to the next stage until the PE has read the output.
6. **Generated files are never hand-edited.** `knowledge/INDEX.md` and `projects/INDEX.md` come from `python3 tools/pe.py index`.

## Triggers

| PE says | Do |
|---|---|
| `status <slug>` | `python3 tools/pe.py status <slug>` and report |
| `check` | `python3 tools/pe.py check` and report failures |
| `new project <slug>` | `python3 tools/pe.py new-project <slug>`, then fill `record.md` with the PE |
| a correction or new knowledge | `/pe-contribute` |

Company skills from `s3-agent-skills` appear under `.claude/skills/s3-*` once linked (see `_system/sources.md`). Prefer them over writing new guidance.
