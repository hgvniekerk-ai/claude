---
id: opc-da-dcom
title: OPC DA (Classic) over DCOM
domain: opc
type: guidance
authority: external
owner: "[TBC]"
reviewed: ""
sources:
  - "https://learn.microsoft.com/troubleshoot/mem/configmgr/console-management/dcom-hardening-change-effect"
  - "KB5004442: Manage changes for Windows DCOM Server Security Feature Bypass (CVE-2021-26414)"
  - "https://learn.microsoft.com/troubleshoot/windows-server/networking/service-overview-and-network-port-requirements"
tags: [opc-da, dcom, kb5004442, firewall, troubleshooting]
---

# OPC DA over DCOM

OPC DA uses DCOM between client and server hosts. Ports and firewall narrowing: see `../network/net-windows-ports.md`.

## DCOM hardening (KB5004442)

| Windows update | Behaviour |
|---|---|
| 8 June 2021 | Hardening available, off by default |
| 14 June 2022 | Hardening on by default, registry opt-out available |
| 14 March 2023 | Hardening enforced, no opt-out |

Effect: a DCOM client must activate the server at authentication level `RPC_C_AUTHN_LEVEL_PKT_INTEGRITY` or higher. Older OPC DA clients and servers that request a lower level fail after patching. The registry key `RequireIntegrityActivationAuthenticationLevel` is ignored after March 2023, so it is not a fix.

## Diagnose

| Event ID (System log) | Side | Meaning |
|---|---|---|
| 10036 | Server | Activation rejected, client authentication level too low |
| 10037 | Client | Application explicitly set a level below the minimum |
| 10038 | Client | Application used a default level below the minimum |

Common errors at the application: `0x80070005` access denied, `0x800706BA` RPC server unavailable.

## Fix options

1. Update the OPC client and server to versions that meet the hardened level. Vendor responsibility.
2. Avoid cross-host DCOM: run the DA client on the server host and carry data across the network with OPC UA or a tunnelling product. Stone Three approved approach: `[TBC: Danie, or s3-agent-skills once cloned]`.
