# Sizing inputs: example-synthetic-plant

SYNTHETIC demo data. Every figure below is invented to exercise the calculator. Not for issue.

## Policy

| key | value | source |
|---|---|---|
| headroom_pct | 30 | SYNTHETIC |
| retention_days | 90 | SYNTHETIC |

## Components

| component | qty | cpu_cores | ram_gb | net_mbps | payload_kb | rate_hz | store_gb_day | disk_gb_fixed | source |
|---|---|---|---|---|---|---|---|---|---|
| analyser camera stream | 2 | 2 | 4 | | 500 | 5 | 2.5 | 0 | SYNTHETIC |
| site server base (OS, application) | 1 | 4 | 16 | 0 | | | 0 | 200 | SYNTHETIC |
| OPC UA client | 1 | 0.5 | 1 | 0.1 | | | stream | 0 | SYNTHETIC |
