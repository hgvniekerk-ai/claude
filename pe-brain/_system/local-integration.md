# Local integration: discover Stone Three sources, fold this candidate into ~/pe-brain

One job: on the PE's own machine, discover the company repositories and improve the canonical `~/pe-brain` with whatever parts of this candidate earn their place. The local workspace wins every conflict.

## Kickoff prompt (paste into Claude Code opened in ~/pe-brain)

```
Run the contract at ~/pe-brain-candidate/_system/local-integration.md.
~/pe-brain is canonical: do not overwrite or recreate it. Do not push or
modify company repositories. Stop at each checkpoint for my approval.
```

## Inputs

| Source | File/Location | Section/Scope | Why |
|--------|--------------|---------------|-----|
| Canonical workspace | `~/pe-brain` | Inventory first, then file by file | What already works |
| Candidate | `~/pe-brain-candidate` (from `tools/install.sh`) | `_system/decisions.md`, then pieces as needed | Parts to adopt |
| Company repos | `~/s3-reference/<repo>` | Inventory, then SKILL.md and READMEs | Capabilities to reuse |
| Registry | candidate `_system/sources.md` | Full file | Repo names and roles |

Do NOT load: client evidence beyond names and folder counts during inventory.

## Process

1. `git -C ~/pe-brain status` and `git log --oneline -15`. Inventory its tree, instructions, index, sources and workflows. Change nothing.
2. Find Azure DevOps access already on the machine: `git config --get-all credential.helper`, `az account show`, `az devops configure --list`, existing remotes in other clones (`git -C <clone> remote -v`). Use what exists. Ask the PE only if none works.
3. Clone `s3-agent-skills`, `s3-agent-notes`, `s3-agent-knowledge-base` into `~/s3-reference/`. Read-only: no commits, no branch changes beyond checkout.
4. Inspect each: tree, every `SKILL.md`, README and conventions files, calculators and document generators (run their own tests or `--help` where safe). Record capabilities by evidence, not filename.
5. **[Checkpoint]** Present a capability table: capability, where it lives (local, company repo, candidate), verified how.
6. Decide per capability: REUSE (link to company or local asset), ADAPT (small change in `~/pe-brain` only), BUILD (missing everywhere, authoritative input exists), AVOID (duplicate or speculative). Company skills: `tools/link-s3-skills.sh`, never copies.
7. **[Checkpoint]** Present the decision table and the list of files to add or change in `~/pe-brain`.
8. On approval, apply in a branch of `~/pe-brain`. Merge entry files into one `CLAUDE.md` under 60 lines. Replace candidate `[TBC]` markers with company sources where found; turn duplicated facts into pointers to the company repo.
9. Run `python3 tools/pe.py index` and `python3 tools/pe.py check` if `pe.py` was adopted, then walk-test: a fresh `claude -p` in `~/pe-brain` answers one prompt from `QUICKSTART.md` citing paths.

## Checkpoints

| After Step | Agent Presents | Human Decides |
|------------|---------------|---------------|
| 5 | Capability table | Missing capabilities, wrong readings |
| 7 | REUSE/ADAPT/BUILD/AVOID table and file plan | Approve per row |

## Audit

| Check | Pass Condition |
|-------|---------------|
| Canonical preserved | `git diff` on `~/pe-brain` shows additions and agreed edits only; no deleted working assets |
| Company repos untouched | `git -C ~/s3-reference/<repo> status` clean for all three |
| No duplication | No fact copied from a company repo into `~/pe-brain`; links instead |
| Data handling | Nothing from company repos sent to any cloud or personal workspace |

## Outputs

| Artifact | Location | Format |
|----------|----------|--------|
| Findings | `~/pe-brain/_system/findings-local.md` (or the local equivalent) | Capability table, decisions, blockers |
| Updated workspace | `~/pe-brain` branch `integrate-s3-sources` | Commits, not pushed |
