---
id: size-profiles
title: Component sizing profiles
domain: sizing
type: register
authority: unverified
owner: "[TBC]"
reviewed: ""
sources:
  - "[TBC: product team, s3-agent-knowledge-base, or measured on a reference site]"
tags: [sizing, profiles, register]
---

# Component sizing profiles

One row per component type and version. Copy a row into a project's sizing input; keep the `source` cell. A row without a source is not usable.

| component | version | cpu_cores | ram_gb | net_mbps | payload_kb | rate_hz | store_gb_day | disk_gb_fixed | source |
|---|---|---|---|---|---|---|---|---|---|
| [TBC: first component] | | | | | | | | | [TBC] |

To add a profile: measure on a running site or take it from a product specification, then follow `../../CONTRIBUTING.md`. Name the measurement method in `source`.
