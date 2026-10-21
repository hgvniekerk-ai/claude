# 03-document: write the server and network specification

One job: turn a COMPLETE sizing result into a specification the client's server team can procure against.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Result | `projects/<slug>/work/sizing-02-result.md` | Full file | Totals and per-row breakdown |
| Inputs | `projects/<slug>/work/sizing-01-inputs.md` | Policy table | Headroom and retention basis |
| Record | `projects/<slug>/record.md` | Frontmatter | Site, products, versions |
| Structure | `references/document-structure.md` | Full file | Section order |

Do NOT load: evidence, `knowledge/network/`, other projects.

## Process

1. Stop if the result status is INCOMPLETE, unless the PE asks for a draft marked DRAFT with open items.
2. Write the specification. Every figure quotes the result file. Round up only, and state the rounding.
3. Carry every gap and source into the Basis section.
4. If the PE wants Word or Excel, use the `docx` or `xlsx` skill after the PE approves the markdown.

## Audit

| Check | Pass Condition |
|-------|---------------|
| Traceable | Every figure appears in the result file or is a stated round-up of one |
| Not synthetic | No SYNTHETIC warning in the result, or the document is marked NOT FOR ISSUE |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Specification | `projects/<slug>/work/sizing-03-specification.md` | Markdown, structure per reference |
