---
name: pe-contribute
description: Correct or add shared PE Brain knowledge. Use when a PE says a note is wrong or out of date, wants to add a new fact, profile, product version or lesson, or wants to know how to contribute.
---

Follow `CONTRIBUTING.md`.

1. Find the one canonical file for the fact with `python3 tools/pe.py find <terms>`. Edit it there; never create a second home.
2. Every changed fact gets a source in `sources:` and the right `authority:` (ladder in `_system/schema.md`).
3. Strip client identifiers from anything in `knowledge/`.
4. Run `python3 tools/pe.py index` and `python3 tools/pe.py check`. Fix errors.
5. Show the PE the diff and a one-line commit message. Commit only when the PE says so. Never push.
