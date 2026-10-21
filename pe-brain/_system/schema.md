# Schema

The closed set of file types, the frontmatter they carry, and naming. `tools/pe.py check` enforces this file. When practice and this file disagree, reconcile the same day.

## Knowledge notes (`knowledge/**`)

```yaml
---
id: net-ntp              # unique, kebab-case, domain prefix: net-, opc-, size-, prod-, lesson-
title: Time synchronisation (NTP)
domain: network          # network | opc | sizing | products | lessons
type: guidance           # guidance | reference | register | profile | lesson
authority: external      # s3-verified | external | field-observed | unverified
owner: "[TBC]"           # a named person, never a team
reviewed: ""             # YYYY-MM-DD of last technical review, blank if never
sources:                 # where the content comes from; at least one
  - "https://..."
tags: [ntp, w32time]
---
```

### Authority ladder

| Value | Meaning | Who can set it |
|---|---|---|
| `s3-verified` | Stone Three practice, reviewed by the note owner | Note owner after review (Danie or delegate) |
| `external` | Public standard or vendor documentation, cited | Any contributor, with a URL |
| `field-observed` | Seen on one or more projects; not yet company practice | Any PE, linking the project record |
| `unverified` | Draft or recollection; must be flagged when used | Any contributor |

A `field-observed` lesson seen on three independent projects is a candidate for `s3-verified` guidance (ICM pattern rule).

## Project records (`projects/<slug>/record.md`)

```yaml
---
type: project
slug: example-synthetic-plant   # kebab-case; matches the folder name
site_alias: ""                  # how PEs refer to the site
client: ""                      # optional; omit if the repo policy says so
region: ""
year: 2026
status: active                  # proposal | active | commissioned | supported | closed
pe: ""                          # lead PE, a named person
products: []                    # "product@version", must match knowledge/products/versions.md
tags: []
---
```

## Placeholders

`[TBC: what is missing, who can supply it]`. `pe.py check` counts them per file. A `[TBC]` is correct output; an invented value is a defect.

## Naming

- Folders and files: lowercase-with-hyphens. Stage folders `NN-name`.
- Project work files: `NN-<artifact>.md` matching the workflow stage that wrote them, for example `work/network-01-register.md`.
- Generated files carry a `GENERATED` banner on line 1.
- No em dashes anywhere (ICM quality guardrail).
