# Closure Ledger

This folder holds items only, never analysis.

## Files

- `LEDGER.md` — one table, one row per open item, across all projects.
- `RULES.md` — the tests the weekly pass applies.
- `WEEKLY.md` — append-only log, one dated block per week.
- `README.md` — this file.

## The two commands

Run from Claude Code in this repository.

`/weekly-pass`
Reads `LEDGER.md` and `RULES.md` and prints, in order: items failing both tests worst first with days elapsed; a drafted message under 60 words for each; items whose owner is not a named person; items marked CLOSED with no closure line; the Friday three. It prints to the screen. Paste the output plus your three answers into a new dated block in `WEEKLY.md`.

`/log-close <ID>`
Asks two questions — what closed it and on whose word, and whether it was ASK or ABSORB — then writes the closure line into that row, sets the status to CLOSED, and stops.

## Status values

- `OPEN` — raised, no ask sent yet.
- `ASKED` — an ask has gone to the named owner.
- `ROUTED` — handed to a different named owner or a different channel.
- `RULED` — a decision was given, whatever the answer.
- `CLOSED` — done, and carrying a closure line. Without the closure line it is not closed.
- `DROPPED` — abandoned on purpose. No longer chased.

## Closure line

`Closed DD Mon by <name>, source: <where>, closed by ASK or by ABSORB.`

ASK means someone else did it after you asked. ABSORB means you did the work yourself.
