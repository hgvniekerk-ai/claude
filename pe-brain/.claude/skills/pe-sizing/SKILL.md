---
name: pe-sizing
description: Hardware and server sizing for a Stone Three project. Use when a PE asks how big a server must be, CPU, RAM, storage, retention, or network bandwidth for cameras, analysers or other components on a site.
---

Run the hardware sizing workflow.

1. Read `workflows/hardware-sizing/CONTEXT.md`.
2. Identify the project slug. If none exists, offer `python3 tools/pe.py new-project <slug>`.
3. Run `python3 tools/pe.py status <slug>` and start at the first PENDING sizing stage, unless the PE names a stage.
4. Open that stage's `CONTEXT.md`, load only its Inputs table, and follow it. Never supply a per-unit figure without a source; write `[TBC]` instead.
