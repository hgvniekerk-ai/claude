# Sizing inputs: <project slug>

Edit surface for the sizing workflow. `python3 tools/pe.py size <this file>` computes the result. Keep headers exactly. Blank or `[TBC]` means unknown; `0` means known to be zero. Column rules: `knowledge/sizing/size-method.md`.

## Policy

| key | value | source |
|---|---|---|
| headroom_pct | | |
| retention_days | | |

## Components

`net_mbps` or (`payload_kb` and `rate_hz`) per unit. `store_gb_day` is a number or `stream`.

| component | qty | cpu_cores | ram_gb | net_mbps | payload_kb | rate_hz | store_gb_day | disk_gb_fixed | source |
|---|---|---|---|---|---|---|---|---|---|
