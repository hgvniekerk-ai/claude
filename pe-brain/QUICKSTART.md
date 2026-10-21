# PE Brain quick start

For Project Engineers. Ten minutes to first useful output.

## Set up once

1. Clone PE Brain from Azure DevOps and open it: `cd pe-brain && claude`. Accept the folder trust prompt once, so the workspace permissions load.
2. Optional, for company skills: clone `s3-agent-skills` into `~/s3-reference/` and run `tools/link-s3-skills.sh`.
3. Check it works: type `check`. Expect `0 errors`.

Requires Claude Code and Python 3. No other installs.

## Your project

Type `new project <your-site-slug>`. Put client files (drawings, IP lists, emails) in `projects/<slug>/evidence/`. They stay on your machine.

Everything a workflow produces lands in `projects/<slug>/work/` as markdown you can edit. Each step stops and asks you to read its output before the next one runs. Type `status <slug>` to see where you are.

## Five prompts

Try them first on the demo project `example-synthetic-plant`, then on your own.

**1. Network requirements**
```
/pe-network Validate the network register for example-synthetic-plant and tell me what I must fix before it goes to the client.
```
Expect: `work/network-02-validation.md` with PASS, PASS WITH WARNINGS or FAIL, each finding explained, and the firewall conduit list.

**2. Server sizing**
```
/pe-sizing Run the sizing for example-synthetic-plant. Which figures dominate the totals, and which are unsourced?
```
Expect: `work/sizing-02-result.md` with CPU, RAM, network and storage totals, headroom, and a gap list. Synthetic inputs are flagged NOT FOR ISSUE.

**3. Has this happened before**
```
/pe-history Have we seen OPC UA certificate errors on any site? What fixed them?
```
Expect: an answer citing project records and lessons by path, with how many projects support it.

**4. Troubleshooting**
```
Our OPC DA link to the plant historian fails with 0x80070005 since the last Windows updates. What do I check, in order? Cite the notes.
```
Expect: the DCOM hardening checks from `knowledge/opc/opc-da-dcom.md`, event IDs to look for, fix options, and the company gaps marked TBC.

**5. Correct the brain**
```
/pe-contribute The NTP note should state our product's time accuracy target. The target is <value>, source <document or person>. Update the right file.
```
Expect: one edited file, a source added, checks passing, and a diff with a commit message for you to approve.

## When Claude says TBC

`[TBC: what, who]` means no authoritative source exists in PE Brain yet. That is deliberate. Supply the source with prompt 5 and every PE benefits.
