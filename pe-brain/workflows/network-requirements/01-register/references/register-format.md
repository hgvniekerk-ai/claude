# Network register: <project slug>

Edit surface for the network workflow. `python3 tools/pe.py netcheck <this file>` validates it. Keep the table headers exactly as written. Unknown values: `[TBC: what, who]`.

## Zones

One row per network zone (VLAN or subnet). `subnet` in CIDR form.

| zone | vlan | subnet | gateway | purdue_level | firewall_owner | source |
|---|---|---|---|---|---|---|

## Hosts

One row per device with an IP. `zone` must match a zone name. `ntp_source` is a hostname from this table or `external:<name>`.

| hostname | role | zone | ip | ntp_source | os | source |
|---|---|---|---|---|---|---|

## Flows

One row per required connection. `from` and `to` are hostnames, zone names, or `external:<name>`. `port` may be a number, a range `49152-65535`, or a list `135,445`. `protocol`: TCP, UDP, ICMP or ANY.

| from | to | protocol | port | purpose | source |
|---|---|---|---|---|---|
