# Closure ledger

One file that matters: `LEDGER.md`. It holds items only, never analysis.

## Files

| File | What it is |
|---|---|
| `LEDGER.md` | Every open item, one row each, with a source you can check |
| `RULES.md` | The tests the weekly pass applies |
| `WEEKLY.md` | Append-only. One dated block per week |
| `README.md` | This |

## Commands

`/weekly-pass` reads `LEDGER.md` and `RULES.md` and outputs, in order: items failing both tests worst first; a drafted message under 60 words for the top twelve; items with no named owner; items marked CLOSED with no closure line; and the Friday three. It then stops. It does not propose improvements to the ledger.

`/log-close <ID>` asks two questions, what closed it and on whose word, and whether it was ASK or ABSORB, writes the closure line, sets status CLOSED, and stops.

Commands live in `.claude/commands/`, not in this folder.

## How to use it

Run `/weekly-pass` on a Friday. It takes about ten minutes. Send or delete every drafted message. Do not keep them.

The number that matters is not how many items close. It is the ratio of ASK to ABSORB in the closure lines. Absorbing an item closes the row and hides the gap.

## Seeding note

The 88 rows in `LEDGER.md` were extracted from seven evidence packs dated 6 and 7 September 2026. Every row carries its source. Delete any row you know closed after the pack cut-off rather than marking it CLOSED, because you have no closure line for it and a false CLOSED is worse than a deleted row.
