# 01-inputs: build the sizing input sheet

One job: list every component that loads the servers or network, with quantity, per-unit figures and a source for each.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Project record | `projects/<slug>/record.md` | Frontmatter, Scope | Products and versions |
| Profiles | `knowledge/sizing/size-profiles.md` | Rows for the project's components only | Sourced per-unit figures |
| Method | `knowledge/sizing/size-method.md` | "Per component row" | Column meaning |
| Input format | `references/input-format.md` | Full file | Starting file |
| Evidence | `projects/<slug>/evidence/` | Only files the PE names | Quantities, client retention requirement |

Do NOT load: `knowledge/network/`, other projects' work.

## Process

1. Copy `references/input-format.md` to `projects/<slug>/work/sizing-01-inputs.md` if absent.
2. Ask the PE for component types and quantities.
3. For each component, copy its profile row and keep its source. If no profile exists, ask the PE for the figure and its source, or write `[TBC: what, who]`.
4. Fill the Policy table. Headroom and retention come from the client requirement or company policy, with source; otherwise `[TBC]`.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 3 | Component table and list of unsourced cells | Supply figures, accept TBC, or stop |

## Audit

| Check | Pass Condition |
|-------|---------------|
| No invented figures | Every number has a source cell that is not blank |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Sizing inputs | `projects/<slug>/work/sizing-01-inputs.md` | `references/input-format.md` tables |
