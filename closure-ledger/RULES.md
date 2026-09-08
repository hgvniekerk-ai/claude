# RULES.md

Tests the weekly pass applies. Do not edit these to make the ledger look better.

- An item with no date in "Date proposed by me" fails the **date test**.
- An item where "Date last ask sent" is more than 14 days old fails the **age test**.
- An item failing both tests needs a **channel change**, not another message to the same person.
- An item whose owner is a team, a process or blank is **not owned**. Owner must be a named person.
- **CLOSED without a closure line is not closed.**
- **Closed by ABSORB** means you did the work yourself. Count these separately from ASK.

## Status values, and only these

| Status | Means |
|---|---|
| OPEN | Raised, nobody has been asked |
| ASKED | A dated ask has gone to the named owner |
| ROUTED | Handed to another owner, acknowledged |
| RULED | A decision exists, work may still follow |
| CLOSED | Done, with a closure line |
| DROPPED | Deliberately abandoned, with a one-line reason |

## Closure line format

`Closed DD Mon by <name>, source: <where>, closed by ASK or by ABSORB.`

## Two rules that are not tests

A verbal escalation is not a closure until one written line exists.

When somebody's verdict contradicts your own record, restate the open items in one factual sentence in the same reply. Do not accept the closure now and re-raise it later.
