---
description: Run the weekly closure pass over the ledger
---

Read `closure-ledger/LEDGER.md` and `closure-ledger/RULES.md`. Apply the tests in RULES.md to every row. Use today's real date to calculate elapsed days.

Output these five sections, in this order, and nothing else.

**a) Failing both tests**

Items that fail the date test and the age test. Worst first, ordered by days since "Date last ask sent". For each: ID, project, item, owner, days elapsed since the last ask.

**b) Drafted messages**

For each item in (a), one message under 60 words. Address the named owner. State the fact, make the ask, propose a date for them to correct. One question. One date. No preamble, no apology, no explanation of why you are asking. No sign-off.

**c) Owner is not a named person**

Items whose owner is a team, a process, or blank.

**d) CLOSED with no closure line**

Items with status CLOSED and an empty or malformed closure line.

**e) The Friday three**

Ask these three questions, do not answer them:
1. What closed this week, and was it by ASK or by ABSORB?
2. Which dependency has been open longest, and what is the next channel for it?
3. What did you build this week that nobody requested?

Then stop. Do not propose improvements to the ledger, do not score or rank beyond the ordering asked for, do not suggest new columns, statuses or files. Do not edit any file.
