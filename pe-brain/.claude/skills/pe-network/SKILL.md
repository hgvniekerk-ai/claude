---
name: pe-network
description: Network requirements for a Stone Three project. Use when a PE asks for an IP plan, VLANs, subnets, segmentation, firewall rules or flows, NTP or time sync design, or a network requirements document for a site. Not for OPC fault-finding on its own (use knowledge/opc).
---

Run the network requirements workflow.

1. Read `workflows/network-requirements/CONTEXT.md`.
2. Identify the project slug. If none exists, offer `python3 tools/pe.py new-project <slug>`.
3. Run `python3 tools/pe.py status <slug>` and start at the first PENDING network stage, unless the PE names a stage.
4. Open that stage's `CONTEXT.md` and load only its Inputs table. Follow its Process, stop at its Checkpoint, and end at its Human check.
