---
id: net-windows-ports
title: Windows RPC and DCOM ports through firewalls
domain: network
type: reference
authority: external
owner: "[TBC]"
reviewed: ""
sources:
  - "https://learn.microsoft.com/troubleshoot/windows-server/networking/service-overview-and-network-port-requirements"
  - "https://learn.microsoft.com/troubleshoot/windows-server/networking/default-dynamic-port-range-tcpip-chang"
  - "https://learn.microsoft.com/troubleshoot/windows-client/networking/rpc-errors-troubleshooting"
tags: [rpc, dcom, firewall, ports, windows]
---

# Windows RPC and DCOM ports

| Protocol | Port | Note |
|---|---|---|
| RPC endpoint mapper | TCP 135 | First contact for any RPC or DCOM call |
| RPC and DCOM dynamic | TCP 49152 to 65535 | Default since Windows Vista and Server 2008. Older Windows used 1025 to 5000 |
| SMB | TCP 445 | File shares |
| LDAP | TCP 389 | Domain lookups |

## Narrowing the dynamic range

Opening 49152 to 65535 across a conduit is usually unacceptable to an OT firewall owner. Two documented options:

1. Change the server's dynamic range: `netsh int ipv4 set dynamicport tcp start=<n> num=<range>` (minimum 255 ports, start at 1025 or above).
2. Restrict RPC allocation with the `HKLM\SOFTWARE\Microsoft\Rpc\Internet` key (Ports, PortsInternetAvailable, UseInternetPorts). Registry change; back up first.

Either change applies to every RPC server on that host. Agree it with the client's Windows owner before writing it into a requirement.
