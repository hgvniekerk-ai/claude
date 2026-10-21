---
id: net-segmentation
title: Segmentation with zones and conduits
domain: network
type: guidance
authority: external
owner: "[TBC]"
reviewed: ""
sources:
  - "IEC 62443-3-2, Security risk assessment for system design (zones and conduits)"
  - "ISA-95 / Purdue reference model, functional levels 0 to 5"
tags: [segmentation, vlan, firewall, iec-62443, purdue]
---

# Segmentation

## Model

- **Zone:** a group of assets with common security requirements. In the IP register each zone has one row: name, VLAN, subnet, gateway.
- **Conduit:** the controlled path between two zones. Every flow in the register whose endpoints sit in different zones crosses a conduit and needs a firewall rule owned by someone.
- **Purdue levels** give a shared language with the client's OT team: 0 to 2 process and control, 3 site operations, 3.5 the industrial DMZ, 4 to 5 enterprise.

## What to specify

1. Every host is in exactly one zone. `pe.py netcheck` checks the host IP sits inside its zone's subnet.
2. Every cross-zone flow lists protocol, port, direction and purpose. `pe.py netcheck` lists these as the conduit summary for the firewall owner.
3. Where Stone Three equipment sits in the client's levels: `[TBC: company standard placement per product, Danie]`.
4. Who owns each firewall: client IT, client OT, or Stone Three. Never leave it as a team; name a person.
