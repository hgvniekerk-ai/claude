# 03-document: write the network requirements document

One job: turn a validated register into a requirements document for the client's IT and OT owners.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Register | `projects/<slug>/work/network-01-register.md` | Full file | All values in the document come from here |
| Validation | `projects/<slug>/work/network-02-validation.md` | Result line, Conduit summary | Must show zero errors; conduit list becomes firewall requests |
| Record | `projects/<slug>/record.md` | Frontmatter | Site, products, versions |
| Structure | `references/document-structure.md` | Full file | Section order |
| NTP | `knowledge/network/net-ntp.md` | "What to specify" | Time section wording |
| Segmentation | `knowledge/network/net-segmentation.md` | "What to specify" | Zone section wording |

Do NOT load: evidence files, `knowledge/sizing/`, other projects.

## Process

1. Stop if the validation result is not PASS or PASS WITH WARNINGS. Send the PE back to stage 01.
2. Draft the outline from `references/document-structure.md` with the section headings and the open items list.
3. Write the document. Tables come straight from the register. Every requirement cites its register row or knowledge note.
4. Add a Mermaid diagram of zones and conduits.
5. Carry every `[TBC]` into the Open items section with its owner.
6. If the PE wants Word, render with the `docx` skill after the PE approves the markdown.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 2 | Outline and open items | Sections to drop or add for this client |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Traceable | Every IP, VLAN, port and subnet appears in the register |
| Open items | Count of `[TBC]` in the document equals the count carried from the register |
| No client evidence quoted | No text pasted from `evidence/` beyond values in the register |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Requirements document | `projects/<slug>/work/network-03-requirements.md` | Markdown, structure per reference |
