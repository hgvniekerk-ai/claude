# Project intelligence workflow

Two independent stages over the project record library: ask it, and feed it.

| Stage | Job | Input | Output | Human check |
|---|---|---|---|---|
| `01-query` | Answer "have we seen this before" with citations | indexes, `pe.py find` | Answer in chat; saved to `projects/<slug>/work/history-01-<topic>.md` if the PE asks | PE opens the cited files before relying on the answer |
| `02-capture` | Turn a project's experience into record entries and lessons | project `work/`, PE debrief | `record.md` updates, `knowledge/lessons/lesson-*.md` drafts | PE approves each lesson before commit |

Factory: `projects/INDEX.md`, `knowledge/INDEX.md` (both generated).
Product: the records and lessons themselves.
