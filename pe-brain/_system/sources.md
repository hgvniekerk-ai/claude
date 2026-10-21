# Source registry

Every external body of knowledge PE Brain depends on, where it is expected on disk, and its verified state. `python3 tools/pe.py sources` checks the local paths.

PE Brain references these sources in place. It does not copy them. Clone them read-only into `~/s3-reference/`, outside the workspace, and never commit from there.

## Stone Three repositories (Azure DevOps)

| Name | Expected local path | Role in PE Brain | Status (2026-10-21) |
|---|---|---|---|
| s3-agent-skills | `~/s3-reference/s3-agent-skills` | Company Claude skills. Linked into `.claude/skills/s3-*` by `tools/link-s3-skills.sh`; no copies. | BLOCKED: not reachable from the build session. Contents not inspected. |
| s3-agent-notes | `~/s3-reference/s3-agent-notes` | Engineer notes. Candidate canonical home for field observations; PE Brain notes link to it with `sources:`. | BLOCKED: not inspected. |
| s3-agent-knowledge-base | `~/s3-reference/s3-agent-knowledge-base` | Candidate canonical home for product, network and sizing facts. Where a fact exists there, the PE Brain note becomes a pointer. | BLOCKED: not inspected. |

Clone command (run on a machine with Azure DevOps access; the org and project path are `[TBC: confirm with Ed]`):

```
mkdir -p ~/s3-reference && cd ~/s3-reference && git clone https://dev.azure.com/<org>/<project>/_git/s3-agent-skills
```

After cloning, run the discovery contract in `_system/local-integration.md`: Claude walks each repo, lists facts that duplicate PE Brain notes, and proposes which file becomes the pointer. Do not let both stay authoritative.

## Method

| Name | Location | Role |
|---|---|---|
| ICM (Interpretable Context Methodology) | https://github.com/RinDig/Interpretable-Context-Methodology, `_core/CONVENTIONS.md` | Workspace conventions. PE Brain deltas are in `decisions.md`. |
| icm-architect skill | personal Claude skill | Used to build and audit this workspace. Not required by PE users. |

## Company capabilities reused by route, not copy

| Capability | How PE Brain uses it |
|---|---|
| `docx`, `xlsx`, `pdf` Claude skills | Render finished markdown outputs to Word or Excel; read PDFs from `evidence/` |
| Mermaid | Network diagrams in `03-document` outputs |
| Existing calculators and document generators in `s3-agent-skills` | `[TBC: inspect once cloned]`. If a sizing calculator exists there, it replaces `pe.py size` as the authority and the workflow contract points to it. |
