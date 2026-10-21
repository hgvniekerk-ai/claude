---
id: net-ntp
title: Time synchronisation (NTP and Windows Time)
domain: network
type: guidance
authority: external
owner: "[TBC]"
reviewed: ""
sources:
  - "https://learn.microsoft.com/troubleshoot/windows-server/active-directory/support-boundary-high-accuracy-time"
  - "https://learn.microsoft.com/windows-server/networking/windows-time-service/windows-server-2016-improvements"
  - "https://learn.microsoft.com/windows-server/networking/windows-time-service/configuring-systems-for-high-accuracy"
  - "RFC 5905 (NTPv4), UDP 123"
tags: [ntp, w32time, time, accuracy]
---

# Time synchronisation

## What to specify in a network requirement

1. The time source for every host (column `ntp_source` in the IP register). `pe.py netcheck` flags hosts without one.
2. The upstream reference: plant domain controller, plant NTP appliance, or GPS clock. State who owns it.
3. The firewall flow: UDP 123 from each client zone to the time source.
4. The accuracy target, if the product needs one. Stone Three product target: `[TBC: s3-agent-knowledge-base or product team]`.

## How Windows picks a source

- Domain members sync from the domain hierarchy by default. The PDC emulator in the forest root is the default clock source for all domains.
- Machines not joined to a domain default to `time.windows.com`. On an isolated plant network that source is unreachable, so the machine free-runs.
- Windows Time does not support broadcast or multicast NTP peers.

## Accuracy tiers (Microsoft support boundary, Windows 10 / Server 2016 and later)

| Target | Key conditions |
|---|---|
| 1 s | Hierarchy ends at an accurate source; cumulative one-way latency to source at most 100 ms |
| 50 ms | Under 5 ms latency to its source; stratum 5 or better; six or fewer hops; one-day average CPU under 90% (host too, if virtual) |
| 1 ms | Under 0.1 ms latency to its source; stratum 5 or better; four or fewer hops; CPU under 80% |

Default configuration only aims at Kerberos-level accuracy (loose). Anything tighter requires the high-accuracy configuration on every Windows node in the chain, including Hyper-V hosts. Windows Server 2012 R2 and earlier are not supported for high accuracy.

## Field checks

- `w32tm /query /status` shows source and stratum.
- `w32tm /stripchart /computer:<source> /samples:5` shows live offset.
