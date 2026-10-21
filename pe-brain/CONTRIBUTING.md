# Contributing to PE Brain

Corrections and new knowledge go into the one file that owns the fact. Git is the review queue.

## Three ways in

| You have | Do |
|---|---|
| A correction to an existing note | Open Claude Code here and run `/pe-contribute` with the correction and its source. Claude finds the canonical file, edits it, runs the checks and shows you the diff. |
| New knowledge (a fact, profile, product version) | Same, `/pe-contribute`. Claude copies `_templates/knowledge-note.md` only if no existing note owns the topic. |
| A lesson from a project | `/pe-history` close-out. Claude updates the project record and drafts the lesson. |

Not using git? Send the correction and its source to the note `owner` listed in `knowledge/INDEX.md`.

## Rules

1. **Source it.** Every fact carries a `sources:` entry: a URL, document reference, or `projects/<slug>/record.md`.
2. **Set authority honestly.** `field-observed` for one project's experience; only the note owner sets `s3-verified`, with a `reviewed:` date.
3. **No client evidence in `knowledge/`.** Lessons are abstracted; the project record holds specifics.
4. **One home.** If the fact lives in a company repo (`_system/sources.md`), link to it instead of copying.
5. **Checks pass.** `python3 tools/pe.py index` then `python3 tools/pe.py check` with zero errors.

## Review

Branch, commit, open a pull request in Azure DevOps. Reviewer: the note's `owner`; for `s3-verified` changes, the technical reviewer (`[TBC: Danie or delegate]`).
