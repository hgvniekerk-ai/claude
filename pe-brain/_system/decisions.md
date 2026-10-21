# Architecture decisions

REUSE what exists, ADAPT what nearly fits, BUILD only what is missing, AVOID what adds weight without value. Dated, newest last. Change a decision by appending, not editing.

## D1 2026-10-21 Form: umbrella over a knowledge bundle and a record library

- **Decision:** Three workflow pipelines (network, sizing, project intelligence) share one `knowledge/` layer. Projects are records that accumulate, not runs. ICM forms 2, 3 and 4 composed, as `forms.md` permits.
- **Why:** The repeating unit for a PE is the project. Workflows recur across projects; knowledge is shared across workflows.

## D2 REUSE: ICM five-layer routing and stage contracts unchanged

`CLAUDE.md` (L0) routes, `CONTEXT.md` (L1) routes by task, stage `CONTEXT.md` (L2) holds Inputs / Process / Checkpoints / Audit / Outputs tables in upstream shape, `knowledge/` is L3, `projects/<slug>/work/` is L4. Upstream guardrails kept: CONTEXT under 80 lines, references under 200, no em dashes, one-way references, docs over outputs.

## D3 ADAPT: stage outputs land in the project record, not in `stages/NN/output/`

- **Upstream:** each stage writes to its own `output/` folder.
- **PE Brain:** each stage writes to `projects/<slug>/work/<workflow>-NN-<artifact>.md`.
- **Why:** Several PEs run the same workflow for different projects in parallel. Per-stage output folders would mix projects. The ICM "pipeline emits into a record library" composition keeps one project's state in one folder, and `pe.py status <slug>` still derives status by scanning files.

## D4 ADAPT: skills by link, not bundle (ICM pattern 9)

- **Upstream:** copy skills into the workspace `skills/` folder.
- **PE Brain:** `tools/link-s3-skills.sh` symlinks skills from a sibling `s3-agent-skills` clone into `.claude/skills/s3-*` (git-ignored).
- **Why:** Bundling would fork company skills and break one-home-per-fact. The shared repo stays the authority and is never modified from here.

## D5 BUILD: four thin native skills plus one subagent

- `/pe-network`, `/pe-sizing`, `/pe-history`, `/pe-contribute`: trigger descriptions plus a pointer to the contract. No content inside, so they cannot drift from the contracts.
- `evidence-scout` subagent: read-only wide search across projects and knowledge, returns cited paths. Keeps the main session's context in the 2k to 8k token range on history questions.

## D6 BUILD: `tools/pe.py`, standard-library Python, no dependencies

Replaces hand-maintained indexes (ICM invariant 9) and gives PEs two deterministic checks that models do badly: IP plan validation and sizing arithmetic. Neither contains engineering constants. Every figure comes from an input row with a `source` column; missing sources make the result `INCOMPLETE`.

## D7 BUILD: authority ladder in frontmatter

`s3-verified`, `external`, `field-observed`, `unverified`. Gives Danie a review lever and lets Claude tell Peter how far to trust an answer.

## D8 AVOID

| Avoided | Reason |
|---|---|
| Vector store, database, web front end, orchestration service | Corpus is small markdown; `pe.py find` plus `grep` and the subagent cover retrieval. Revisit if `projects/` passes roughly 300 records. |
| Claude Projects as the delivery vehicle | The brief: no manual context assembly. Files in git replace project knowledge uploads. |
| Company sizing rules, product port lists, run-signal logic written from memory | No authoritative source was reachable. Marked `[TBC]` with the source that should supply them. |
| Committing raw client evidence | `projects/*/evidence/` and `projects/*/work/` are git-ignored by default. Ed decides whether `work/` is tracked in the Azure DevOps repo. |
| `setup` questionnaire (ICM pattern 8) | Nothing per-user to configure beyond cloning sources. `QUICKSTART.md` covers it. |
