# PR #6 conflict reconciliation — 2026-10-26

**Status: Git conflict resolution only. No author signoff or merge of PR #6 into main.**

The author requested help resolving PR #6, which diverged after commit `dbb2c81156d9d8e6259e3acd625553919c082ed4`. The current main was `e9006afde6cbb34b5ded8e107b7d7e88bb1cfa9f`, while the PR branch was `ba97dba31e869d9ad7f6cd0b947b9926b5ca1860`.

## Disposition

- **Main is authoritative in files changed on both branches (19 paths).** Later author-approved P77–P84 changes, including canonical Chapter 1, must not be reverted by applying earlier versions from this branch.
- **PR-only changes preserved (113 paths):** 112 additions/modifications at paths untouched on main, including Chapter_04, Chapter_08, Chapter_09, and Chapter_14, plus deletion of a tracked Python `__pycache__` binary.
- **Three manual resolutions:** (1) Sunday Morning README carries the author D27 *Sunday Morning Movies* origin/purpose from the PR while preserving main's more recent voice recovery links; (2) `.gitignore` includes `*.pyc` and `__pycache__/`; (3) `Story/Pathwell.txt` is regenerated to reflect the four retained PR-only chapters without replacing main's newer approved text in other chapters.
- The old PR branch has a competing `P77`–`P88` narrative in `Story/Revision/Pass-Log.md` and overlapping R-rows. **These historical entries were not copied to main's active records**, which would collide with main's own P77–P84. They remain inspectable in the PR branch's original parent commit `ba97dba31e869d9ad7f6cd0b947b9926b5ca1860`. Their substance requires separate author-led reconciliation before any merger.
- All unresolved semantic conflicts in older Pass Log, Decisions, Promise Ledger and status records were resolved **in favor of current main**; PR-only reports and experiments remain available as proposals and evidence, not automatic story law.

## Overlapping paths

- `.gitignore` — combined
- `Revision-Status.md`
- `Story/Chapters/Chapter_01.txt`
- `Story/Chapters/Chapter_05.txt`
- `Story/Chapters/Chapter_07.txt`
- `Story/Chapters/Chapter_10.txt`
- `Story/Chapters/Chapter_13.txt`
- `Story/Chapters/Chapter_15.txt`
- `Story/Chapters/Chapter_16.txt`
- `Story/Chapters/Chapter_17.txt`
- `Story/Chapters/Chapter_18.txt`
- `Story/Pathwell.txt` — regenerated
- `Story/Revision/Decisions.md`
- `Story/Revision/Emergence/INDEX.md`
- `Story/Revision/Emergence/experiments/EXP-0018-Whole-Book-Checklist-Candidates-2026-10-22.md`
- `Story/Revision/Pass-Log.md`
- `Story/Revision/Promise-Ledger.md`
- `Story/Revision/README.md`
- `Story/Sunday-Morning/README.md` — D27 origin preserved

## Review gates before merging PR #6

1. **Inspect the four PR-only chapter diffs** (Ch04, Ch08, Ch09, Ch14) and their authorization. This reconciliation retains them as **proposed PR content**, not approved canon.
2. **Audit new experiment files** and reader reports (EXP-0019 through EXP-0024 and related reviews) for stale descriptions of decisions before importing their authority.
3. **Run the story's tests, check the assembled manuscript, and check book continuity**. None was run as part of this Git ancestry repair.
4. **Do not press Merge solely because GitHub reports mergeable**. This PR still changes many files, and the absence of textual conflicts is not literary approval.

The current branch commit records both the old PR parent and the new main parent. `main` is unchanged by the reconciliation.
