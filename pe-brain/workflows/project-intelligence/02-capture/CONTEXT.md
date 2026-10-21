# 02-capture: record what the project taught

One job: update the project record and draft lessons other PEs can find.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Record | `projects/<slug>/record.md` | Full file | Current state |
| Work | `projects/<slug>/work/` | Validation and result files | What was decided and found |
| PE debrief | conversation | Faults, fixes, surprises, what to do differently | The lessons |
| Lesson template | `_templates/lesson.md` | Full file | Lesson shape |
| Existing lessons | `pe.py find <terms> --domain lessons` | Hits only | Avoid duplicates; add evidence to an existing lesson instead |

Do NOT load: other projects' records, raw evidence beyond what the PE names.

## Process

1. Ask the PE the debrief questions: what failed, what fixed it, what took longest, what would you tell the next PE.
2. Update `record.md`: status, products and versions installed, Lessons section with one line each.
3. For each lesson useful beyond this site: search for an existing lesson. If one exists, add this project to its `sources` and evidence list. If not, copy `_templates/lesson.md` to `knowledge/lessons/lesson-<slug>.md` with `authority: field-observed`.
4. Strip client identifiers from lessons. The lesson links to the project record; the record holds the specifics.
5. Run `python3 tools/pe.py index` then `python3 tools/pe.py check`.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 3 | Each lesson draft | Keep, edit or drop |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Updated record | `projects/<slug>/record.md` | Schema in `_system/schema.md` |
| Lessons | `knowledge/lessons/lesson-<slug>.md` | `_templates/lesson.md` |
