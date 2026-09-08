---
description: Close one ledger item and write its closure line
argument-hint: <ID>
---

Close item `$1` in `closure-ledger/LEDGER.md`.

Find the row with that ID. If there is no such row, say so and stop.

Ask two questions, one at a time, and wait for the answer to each:
1. What closed it, and on whose word? (the name, and where it came from — meeting, email, call, site)
2. Was it ASK or ABSORB?

Then write into that row:
- Status: `CLOSED`
- Closure line: `Closed DD Mon by <name>, source: <where>, closed by ASK.` or `... closed by ABSORB.` using today's date.

Change nothing else in the file. Confirm the line you wrote, then stop.
