# 01-register: build the IP and flow register

One job: turn what is known about the site network into one structured register.

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Project record | `projects/<slug>/record.md` | Frontmatter, Scope | Products, versions, site |
| Evidence | `projects/<slug>/evidence/` | Only files the PE names | Client network drawings, IP lists, emails |
| Register format | `references/register-format.md` | Full file | Column definitions; copy as the starting file |
| Segmentation | `knowledge/network/net-segmentation.md` | "What to specify" | Zone and conduit rules |
| NTP | `knowledge/network/net-ntp.md` | "What to specify" | Time source column |

Do NOT load: other projects' work, `knowledge/sizing/`, the whole evidence folder.

## Process

1. Copy `references/register-format.md` to `projects/<slug>/work/network-01-register.md` if it does not exist. Never overwrite an existing register without asking.
2. Ask the PE which evidence files hold network data. Read only those.
3. Fill Zones, Hosts and Flows. Every row gets a `source` (evidence filename, PE statement with date, or knowledge note path).
4. Where a value is unknown, write `[TBC: what, who]`. Do not guess IPs, VLANs or ports.
5. Add the flows the products need. Product port list: `[TBC]` until `knowledge/network/CONTEXT.md` lists a source; ask the PE and source their answer.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 3 | Count of zones, hosts, flows, and the TBC list | Whether anything is missing before validation |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Sourced | Every row has a non-empty `source` |
| No invention | Every value traces to an input or is `[TBC]` |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| IP and flow register | `projects/<slug>/work/network-01-register.md` | `references/register-format.md` tables |
