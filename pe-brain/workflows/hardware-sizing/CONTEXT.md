# Hardware sizing workflow

From the project's component list to a server, storage and bandwidth specification with every figure sourced.

| Stage | Job | Input | Output (in `projects/<slug>/work/`) | Human check |
|---|---|---|---|---|
| `01-inputs` | Build the sizing input sheet | record, profiles, PE quantities | `sizing-01-inputs.md` | PE confirms quantities and each source |
| `02-calculate` | Run the arithmetic | `sizing-01-inputs.md` | `sizing-02-result.md` | PE checks the result is COMPLETE and plausible |
| `03-document` | Write the specification | result + inputs | `sizing-03-specification.md` | PE reads it as the client's server team would |

Factory (every run): `knowledge/sizing/size-method.md`, `knowledge/sizing/size-profiles.md`.
Product (this run): `projects/<slug>/work/sizing-*`.

The calculator holds no engineering constants. An INCOMPLETE result is a correct result when sources are missing; it lists what to obtain.
