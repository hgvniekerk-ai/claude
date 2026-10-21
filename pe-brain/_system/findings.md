# Build findings, 2026-10-21

Detailed record of the cloud build. The handover in chat is the summary; this file is the evidence.

## Status of this build

**Candidate, not canonical.** Your local `~/pe-brain` is canonical. This build is folded into it on your machine with `local-integration.md`. It does not replace it.

## Discovery

| Source | Result | Evidence |
|---|---|---|
| Local `~/pe-brain` | Not reachable. The build ran in a cloud container; the workspace is on the PE's machine. | `ls ~/pe-brain`: no such directory |
| Azure DevOps `s3-agent-skills`, `s3-agent-notes`, `s3-agent-knowledge-base` | Not reachable. No credentials in the container; the proxy refuses the tunnel to the org URL. | `git ls-remote`: auth prompt refused; curl: 403 on CONNECT |
| Google Drive, SharePoint | No PE Brain or s3-agent files found (metadata search only, no content read) | Searches returned empty |
| Local Claude session for hand-off | None running | `ListAgents`: no reachable sessions |
| ICM upstream | Cloned read-only and read: `_core/CONVENTIONS.md`, `workspaces/workspace-builder` (5 stages), `script-to-animation` routing | RinDig/Interpretable-Context-Methodology, depth 1 |
| icm-architect skill | Read: invariants, accuracy floor, forms, templates | personal skill |

Consequence: every Stone Three-specific fact (product ports, run-signal logic, bridge products, sizing profiles, headroom policy, version register, document templates) is `[TBC]` with the source that should fill it. Nothing was invented. The `pe.py check` count of open markers is the backlog.

## ICM conformance (upstream validation checks applied)

| Check | Result |
|---|---|
| L0 entry file under 60 lines, routing only | `CLAUDE.md` 36 lines |
| CONTEXT.md under 80 lines | Longest 45 lines |
| Stage contracts: Inputs, Process, Outputs tables; checkpoints in creative stages; audits in build stages | All 8 stages |
| One-way references | `knowledge/` never points into `workflows/`; workflows point to knowledge |
| Generated indexes not hand-edited | `pe.py check` fails on a stale index |
| No em dashes | Enforced by `pe.py check` |
| Token budget per step | L0 + L1 + workflow + stage + one note + register: about 1,500 words, roughly 2,000 tokens |

Deviations are recorded in `decisions.md` (D3 outputs in the project record, D4 skills by link).

## Tool verification

| Test | Input | Result |
|---|---|---|
| `netcheck` clean register | demo register | PASS WITH WARNINGS, 4 warnings, conduit summary correct |
| `netcheck` seeded faults | duplicate IP, host outside subnet, VLAN clash, unknown endpoint, port 99999 | FAIL, all 5 caught, exit code 1 |
| `size` complete | demo inputs | Camera 500 KB x 5 Hz x 0.008 = 20 Mbps each; storage 200 + 6.08 x 90 = 747.2 GB; matches hand calculation |
| `size` with gaps | CPU `[TBC]`, headroom unsourced | INCOMPLETE, both gaps listed, headroom withheld |
| `check` | whole workspace | 0 errors; warning on `demo-analyser@1.0` shows version awareness working |

## Cold-session walk test

Fresh `claude -p` runs inside `pe-brain/`, no prior context, tools limited to Read, Grep, Glob and `pe.py`.

| Prompt (QUICKSTART) | Behaviour observed |
|---|---|
| 3 history | Routed to `01-query`, ran `pe.py find`, found the demo record, refused to treat it as evidence (0 real projects), pointed to `knowledge/opc/opc-ua.md` by section, offered capture |
| 1 network | Ran `netcheck`, explained each warning against the register row, named the firewall conduit, did not edit the register, stopped at the human check |
| 4 OPC DA | Answered from `opc-da-dcom.md` and `net-windows-ports.md` with section citations, flagged authority `external`, listed company gaps |
| 2 sizing | Reported dominant drivers with shares, flagged every input as synthetic, caught that 2.5 GB/day per camera conflicts with 216 GB/day implied by payload and rate |

Prompt 5 (contribute) was not run headless because it edits files; the skill and checks it relies on were exercised directly.

Known friction: Claude Code ignores `.claude/settings.json` permissions until the folder is trusted once interactively. QUICKSTART step 1 covers it.

## Open items for the local session

1. Run `local-integration.md` steps 1 to 4 to inventory `~/pe-brain` and the three company repos.
2. For each `[TBC]` in `knowledge/`, look for the fact in `s3-agent-knowledge-base` and replace the note body with a pointer where found.
3. If `s3-agent-skills` holds a sizing calculator or document generator, it replaces `pe.py size` or the `03-document` structures (decision D6 and D8).
4. Ed: whether `projects/*/work/` is tracked in Azure DevOps, and the org and project path for cloning.
5. Danie: owner for each knowledge domain; confirm or replace `size-method.md`.
