# Network requirements workflow

From project evidence to a network requirements document the client's IT and OT owners can act on.

| Stage | Job | Input | Output (in `projects/<slug>/work/`) | Human check |
|---|---|---|---|---|
| `01-register` | Build the IP and flow register | `evidence/`, PE answers | `network-01-register.md` | PE confirms hosts, zones and flows match the design |
| `02-validate` | Validate the register | `network-01-register.md` | `network-02-validation.md` | PE clears every error, accepts or fixes each warning |
| `03-document` | Write the requirements document | register + validation | `network-03-requirements.md` | PE reads it as the client's IT lead would |

Factory (every run): `knowledge/network/`, `knowledge/opc/` where OPC flows exist.
Product (this run): `projects/<slug>/work/network-*`.

Run stages in order. A stage starts only when the previous output exists and the PE has read it. Re-running a stage overwrites its output; the register is the edit surface, so fix data there, not in later outputs.

Need a project first? `python3 tools/pe.py new-project <slug>`.
