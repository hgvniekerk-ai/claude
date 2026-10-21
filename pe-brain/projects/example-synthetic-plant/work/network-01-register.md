# Network register: example-synthetic-plant

SYNTHETIC demo data. RFC 5737 documentation ranges. Edit surface for the network workflow; validated by `python3 tools/pe.py netcheck`.

## Zones

| zone | vlan | subnet | gateway | purdue_level | firewall_owner | source |
|---|---|---|---|---|---|---|
| s3-analysers | 110 | 192.0.2.0/25 | 192.0.2.1 | 2 | [TBC: client OT lead name] | SYNTHETIC |
| plant-ops | 120 | 198.51.100.0/24 | 198.51.100.1 | 3 | Demo OT Engineer | SYNTHETIC |

## Hosts

| hostname | role | zone | ip | ntp_source | os | source |
|---|---|---|---|---|---|---|
| s3-srv01 | Stone Three site server | s3-analysers | 192.0.2.10 | plant-dc01 | Windows Server 2022 | SYNTHETIC |
| s3-cam01 | analyser camera 1 | s3-analysers | 192.0.2.21 | s3-srv01 | embedded | SYNTHETIC |
| s3-cam02 | analyser camera 2 | s3-analysers | 192.0.2.22 | s3-srv01 | embedded | SYNTHETIC |
| plant-dc01 | plant domain controller | plant-ops | 198.51.100.5 | external:gps-clock | Windows Server 2019 | SYNTHETIC |
| plant-hist01 | plant historian, OPC UA server | plant-ops | 198.51.100.20 | plant-dc01 | Windows Server 2019 | SYNTHETIC |

## Flows

| from | to | protocol | port | purpose | source |
|---|---|---|---|---|---|
| s3-srv01 | plant-hist01 | TCP | 4840 | OPC UA read of process tags and run signal | SYNTHETIC |
| s3-srv01 | plant-dc01 | UDP | 123 | time sync | SYNTHETIC |
| s3-cam01 | s3-srv01 | TCP | [TBC: product image port, product team] | image stream | SYNTHETIC |
| s3-cam02 | s3-srv01 | TCP | [TBC: product image port, product team] | image stream | SYNTHETIC |
