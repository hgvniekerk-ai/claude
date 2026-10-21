---
type: project
slug: example-synthetic-plant
site_alias: Demo Plant
client: "SYNTHETIC, not a real client"
region: demo
year: 2026
status: active
pe: "Peter (walkthrough)"
products: [demo-analyser@1.0]
tags: [synthetic, demo, opc-ua, ntp]
---

# example-synthetic-plant

Synthetic project used by `QUICKSTART.md` and `_system/findings.md`. All values are invented for demonstration and use RFC 5737 documentation address ranges. Do not cite this record as evidence.

## Scope
Two camera-based analysers, one site server, OPC UA link to the client's plant historian.

## Network
Register: `work/network-01-register.md`. Validation: `work/network-02-validation.md`.

## Sizing
Inputs: `work/sizing-01-inputs.md`. Result: `work/sizing-02-result.md`.

## OPC and integration
Demo fault for search testing: OPC UA session failed with BadCertificateTimeInvalid; server clock was 9 minutes fast because it had no NTP source. Fixed by pointing it at the plant domain controller.

## Lessons
- Check NTP on the OPC server before exchanging certificates (synthetic).
