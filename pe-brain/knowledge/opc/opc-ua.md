---
id: opc-ua
title: OPC UA connections
domain: opc
type: guidance
authority: external
owner: "[TBC]"
reviewed: ""
sources:
  - "https://www.iana.org/assignments/service-names-port-numbers (opcua-tcp 4840, opcua-tls 4843)"
  - "https://reference.opcfoundation.org/Core/Part4/ (GetEndpoints, status codes)"
  - "https://reference.opcfoundation.org/Core/Part6/ (opc.tcp mapping)"
tags: [opc-ua, certificates, endpoint, troubleshooting]
---

# OPC UA connections

## What to specify

1. Server endpoint URL, for example `opc.tcp://<host>:4840`. 4840/TCP is the IANA registration (`opcua-tcp`); vendors often use another port, so take it from the server's configuration, not from this note.
2. Security mode (None, Sign, SignAndEncrypt) and security policy agreed with the client. The client must request one the server offers.
3. Certificate exchange: who places the Stone Three client certificate in the server's trusted list, and the server certificate in ours. Name the person.
4. User authentication: anonymous, username, or certificate.
5. The firewall flow from our client zone to the server port.

## Troubleshooting order

| Step | Check | Typical symptom |
|---|---|---|
| 1 | TCP reachability to the endpoint port from the client host | Timeout, `BadNotConnected` |
| 2 | Endpoint URL returned by discovery uses a hostname the client can resolve | Discovery works, session fails; server advertises an internal hostname |
| 3 | Security mode and policy match an endpoint the server offers | `BadSecurityPolicyRejected` |
| 4 | Each side trusts the other's application certificate | `BadCertificateUntrusted`, `BadSecurityChecksFailed` |
| 5 | Clocks on both hosts are correct (see `../network/net-ntp.md`) | `BadCertificateTimeInvalid` |
| 6 | Certificate hostname or URI matches | `BadCertificateHostNameInvalid`, `BadCertificateUriInvalid` |
| 7 | User identity is accepted | `BadIdentityTokenRejected`, `BadUserAccessDenied` |

Record the fault and the fix in the project record so `/pe-history` can find it next time.
