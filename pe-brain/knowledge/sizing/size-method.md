---
id: size-method
title: Sizing arithmetic used by pe.py size
domain: sizing
type: guidance
authority: unverified
owner: "[TBC]"
reviewed: ""
sources:
  - "tools/pe.py, function size (the implementation this note describes)"
tags: [sizing, bandwidth, storage, method]
---

# Sizing arithmetic

Status: **unverified as company method.** The arithmetic is unit conversion and summation. Whether Stone Three sizes servers by summing per-component loads is `[TBC: Danie to confirm or replace with the company method]`. If `s3-agent-skills` holds a sizing calculator, that calculator becomes the authority and this note becomes a pointer.

## Units

KB = 1,000 bytes. Mbps = 10^6 bit/s. GB = 10^9 bytes. Stated so nobody mixes binary and decimal units silently.

## Per component row

| Quantity | Rule |
|---|---|
| Stream rate per unit | `net_mbps` if given, else `payload_kb x rate_hz x 0.008` |
| Stored per day per unit | `store_gb_day` if a number; if the cell says `stream`, `stream Mbps x 10.8` (Mbps to GB per day) |
| Row totals | per-unit value x `qty` for cpu, ram, network, fixed disk, daily store |

## Totals

- Storage = fixed disk + daily store x `retention_days`.
- Headroom: totals x (1 + `headroom_pct`/100), only if the policy row carries a source. Otherwise totals are reported raw and flagged.
- A blank or `[TBC]` cell in a row with `qty` above 0, or a row with no source, makes the result `INCOMPLETE` and lists the gap. Zero is a known value; blank is unknown.
- A source containing `SYNTHETIC` marks the result not for issue.

## What this does not do

No CPU-per-camera or RAM-per-analyser constants live here. Those are per-component facts and belong in `size-profiles.md` with their source.
