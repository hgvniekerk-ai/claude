# 01-query: answer from project history

One job: find what past projects and lessons say about the PE's question, and answer with file citations.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Project index | `projects/INDEX.md` | Full file | Which projects exist, products, status, tags |
| Knowledge index | `knowledge/INDEX.md` | Rows in domain `lessons` and the question's domain | Promoted lessons and guidance |
| Search | `python3 tools/pe.py find <terms>` | Command; add `--domain`, `--tag` to narrow | Ranked hits with path and line |
| Wide search | `evidence-scout` subagent | When more than about five files need reading | Keeps this session's context small |

Do NOT load: whole project folders, `evidence/` unless the PE asks and the project is theirs.

## Process

1. Restate the question as search terms: symptom, product, version, protocol, site alias.
2. Run `pe.py find` with two or three term sets. Read the top hits only.
3. If hits span many projects, delegate to `evidence-scout` with the question and the hit list.
4. Answer: what was seen, on which project, what fixed it, how strong the evidence is (authority, number of projects).
5. Say plainly when history holds nothing. Then route to the relevant knowledge note.

## Audit

| Check | Pass Condition |
|-------|---------------|
| Cited | Every claim names a file path |
| Strength stated | Answer says how many independent projects support it |
| No overreach | One project's fix is not presented as company practice |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Answer | chat; optional `projects/<slug>/work/history-01-<topic>.md` | Finding, evidence table (path, authority), next step |
