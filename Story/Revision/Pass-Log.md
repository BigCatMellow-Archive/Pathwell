# Pass log: Pathwell revision

## Status

**Evidence, active. Book record, created 2026-09-29.** This page owns what happened in each pass of the revision: what ran, what changed (change notes written from the diff), and what each independent check found. It's the book's equivalent of the Sunday Morning [History](../Sunday-Morning/History.md): one entry per pass, newest last. A lesson that changes the method goes to the Sunday Morning notes (Pipeline, Craft or Rules) and gets a line here saying where it went.

## Before this revision

A short account of how the chapters got to where they are, so a later pass doesn't re-derive it. Details are in the linked records.

| When | What happened | Record |
| --- | --- | --- |
| to June 2026 | Discovery draft; Chapters 1–2 revised with James and adopted as the voice benchmark | [pathwell_editorial_operations.md](../Story_Files/pathwell_editorial_operations.md), `chapter1_revision_journey.md`, `chapter2_revision_journey.md` |
| June–July 2026 | Multi-agent (MAP) review and prose passes; Chapters 1–2 locked (2026-07-01); the Coda made the only ending | [session_progress.md](../Story_Files/session_progress.md), [INS-0001](../insights/INS-0001-unpaid-plot-debts-must-be-paid-on-page.md) |
| 2026-08-21 to 08-27 | The "Bible" interviews and decisions; the manuscript reconciliation audit | `BIBLE_DECISIONS_2026-08-2*.md`, `MANUSCRIPT_RECONCILIATION_AUDIT*` |
| 2026-08-28 | The reconciliation executed: all eighteen chapters rewritten to the [chapter contracts](../Story_Files/PATHWELL_MAPS_L_CHAPTER_CONTRACT_MATRIX_2026-08-28.md); Chapter 18 written as the new coda; Chapter 12b removed. `Coda.txt` wasn't touched and wasn't removed | `MANUSCRIPT_RECONCILIATION_EXECUTION_LOG*` |
| 2026-09-17 to 09-18 | Experimental Architecture V2–V5, recovered-decision audits and author-intent notes. Several author decisions recorded; nothing applied to the chapters | the 09-17/18 files in [Story_Files](../Story_Files/); indexed on [Decisions](Decisions.md#recorded-rulings-not-yet-in-the-manuscript) |
| 2026-09-27 to 09-29 | The Sunday Morning method built on a seven-story collection, with James's voice guide (09-27) | [Sunday-Morning/History](../Sunday-Morning/History.md) |

## P1, 2026-09-29: take stock (Step 1)

**Goal:** inventory, cold read, assessment, THINK and PLAN; no chapter edits ([R6](Decisions.md#jamess-rulings-for-this-revision)).

**What ran**

1. Read the Sunday Morning method (README, Decisions, Craft, Pipeline, Registry, History, Voice Guide, the checker) and the book's targets (Thesis, Non-Negotiable Scenes, Writing Principles, pathwell_prose_voice), then the recorded rulings and the chapter contract matrix.
2. **Cold read:** a fresh reader with no notes read Chapters 1–18 and the Coda in order, writing notes on each chapter before reading the next ([record](Cold-Read-2026-09-29.md)).
3. **Full read** of all nineteen files by the assessor.
4. **Checker adapted** in place ([W5](Decisions.md#working-decisions)): `--pattern`, `--status-block`, `--min-files`, a `registry:watch` block, a short-paragraph count, and filter verbs after named characters. Tested on a `.md` sample (status block skipped, dialogue excluded) and on the chapters. The Sunday Morning [Registry template](../Sunday-Morning/Registry.md#watch-patterns-optional) gained an empty watch block and its [README](../Sunday-Morning/README.md) a line on the new options.
5. **Registry** created for the book (names, chapter shapes, devices, watch patterns, exceptions), and the checker run on the chapters.
6. **Assessment** written ([record](Assessment-2026-09-29.md)): diagnostic per chapter, problems by level, shape check, checker results, watch-list, and the cold read's claims checked against the text.
7. **Promise ledger**, **Decisions** and **Plan** written. [Revision-Status.md](../../Revision-Status.md) rewritten to match the chapters; status lines added to [Open-Questions.md](../../Open-Questions.md) and [Structural-Risks.md](../../Structural-Risks.md); a pointer to this folder added to [Story/README.md](../README.md).

**What changed (from the diff)**

- New: `Story/Revision/` (README, Decisions, Plan, Promise-Ledger, Registry, Pass-Log, Cold-Read-2026-09-29, Assessment-2026-09-29).
- Changed: `Story/Sunday-Morning/tools/sunday_morning_check.py` (options above; no change to how `.md` drafts are chosen or split); `Story/Sunday-Morning/Registry.md` (an empty, optional watch block); `Story/Sunday-Morning/README.md` (the checker paragraph); `Revision-Status.md` (rewritten); `Open-Questions.md`, `Structural-Risks.md` (a status line each); `Story/README.md` (a pointer).
- Not changed: every chapter file, and every other record.

**Result:** every chapter at L2 ([levels](README.md#development-levels-for-a-chapter)); nine questions for James; plan awaiting approval. Stopped here.

### Check log

- **Cold read (P1).** Independent; opened only the chapter files. It found the premise gap (why Pathwell was in her apartment), the doubled ending and the Coda's contradictions, the dropped dagger, Shade's unclear reason at his death, the explanation-after-showing habit and its "Not X. Y." cadence, the one shared deadpan, and the back third's slowing. It confirmed the book's strengths. Its specific claims were checked against the text; nearly all held ([where the cold read was checked](Assessment-2026-09-29.md#where-the-cold-read-was-checked)).
- **Fresh check of the P1 records.** Not run: an independent fact-check of the assessment, ledger and decisions against the chapters and source records was started and declined in the session. The records were checked by their writer only (every link and anchor resolves; the checker numbers were regenerated from the script). Run the fact-check before Step 2 begins.
