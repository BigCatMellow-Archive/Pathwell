# Pass log: Pathwell revision

## Status

**Evidence, active. Book record, created 2026-09-29.** This page owns what happened in each pass of the revision: what ran, what changed (change notes written from the diff), and what each independent check found. It's the book's equivalent of the Sunday Morning [History](../Sunday-Morning/History.md): one entry per pass, newest last. A lesson that changes the method goes to the Sunday Morning notes (Pipeline, Craft or Rules) and gets a line here saying where it went.

## Before this revision

A short account of how the chapters got to where they are, so a later pass doesn't re-derive it. Details are in the linked records.

| When | What happened | Record |
| --- | --- | --- |
| to June 2026 | Discovery draft; Chapters 1–2 revised with James and adopted as the voice benchmark | [pathwell_editorial_operations.md](../Story_Files/pathwell_editorial_operations.md), `chapter1_revision_journey.md`, `chapter2_revision_journey.md` |
| June–July 2026 | Multi-agent (MAP) review and prose passes; Chapters 1–2 locked (2026-07-01); the Coda made the only ending | [session_progress.md](../Story_Files/session_progress.md), [INS-0001](../insights/INS-0001-unpaid-plot-debts-must-be-paid-on-page.md) |
| 2026-08-21 to 08-27 | The Bible interview: James answered one question at a time (the Bible decisions, then audit questions Q1–Q149), and each answer was locked | `BIBLE_DECISIONS_2026-08-2*.md`, `MANUSCRIPT_RECONCILIATION_AUDIT*`; indexed on [Decisions](Decisions.md#the-bible-interview-locks-the-manuscript-follows) |
| 2026-08-28 | The reconciliation executed: all eighteen chapters rewritten to the [chapter contracts](../Story_Files/PATHWELL_MAPS_L_CHAPTER_CONTRACT_MATRIX_2026-08-28.md); Chapter 18 written as the new coda; Chapter 12b removed. `Coda.txt` wasn't touched and wasn't removed | `MANUSCRIPT_RECONCILIATION_EXECUTION_LOG*` |
| 2026-09-17 to 09-18 | Experimental Architecture V2–V5, recovered-decision audits and author-intent notes. Several author decisions recorded; nothing applied to the chapters | the 09-17/18 files in [Story_Files](../Story_Files/); indexed on [Decisions](Decisions.md#later-recorded-rulings-2026-09-1718) |
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

**Result:** every chapter at L2 ([levels](README.md#development-levels-for-a-chapter)); nine questions for James; plan awaiting approval. Stopped here. (Nine became seven in P1b.)

### Check log

- **Cold read (P1).** Independent; opened only the chapter files. It found the premise gap (why Pathwell was in her apartment), the doubled ending and the Coda's contradictions, the dropped dagger, Shade's unclear reason at his death, the explanation-after-showing habit and its "Not X. Y." cadence, the one shared deadpan, and the back third's slowing. It confirmed the book's strengths. Its specific claims were checked against the text; nearly all held ([where the cold read was checked](Assessment-2026-09-29.md#where-the-cold-read-was-checked)).
- **Fresh check of the P1 records.** Not run: an independent fact-check of the assessment, ledger and decisions against the chapters and source records was started and declined in the session. The records were checked by their writer only (every link and anchor resolves; the checker numbers were regenerated from the script). Run the fact-check before Step 2 begins.

## P1b, 2026-09-29 to 30: the Bible interview checked

**Why:** James pointed out that the repository holds the interview that "straightened everything out". P1 had indexed those files but read only the September audits that summarize them, so several of its questions were ones James had already answered.

**What ran**

1. Read the interview's locks: the three `BIBLE_DECISIONS` pages (08-21 to 08-23) and the locked questions in the `MANUSCRIPT_RECONCILIATION_AUDIT` files (Q1–Q149, 08-23 to 08-27), with the handoffs' working rules. Every locked heading was listed; the ones bearing on P1's questions were read in full.
2. Compared each P1 question and finding with the locks, then with the September records.

**What the interview settled** (from P1's nine questions): the Coda is superseded (Q93–Q103 name its contents stale); Chapter 18's cookbook beat is a silent put-back, and Pathwell chooses not to find out whether he can still prune (Q96, Q99, Q103); "It was my fault" stands unexplained (Q95); Chapter 1 has him pass as a party guest, inferred from aftermath (08-22, Q112), which superseded the July lock on Chapters 1–2; the recognition happens at the diner and the narration withholds "Shade" until then (08-23, 08-24); the crash is deliberate; the prune's content stays open (08-22, Q141); Elizabeth is witness in the confrontation, with the child as her climax choice; Shade's last choice has a locked reason (Continued 30, Q132).

**What's still open:** seven questions, Q-A to Q-G, mostly where a September record differs from an interview lock ("Perfect." or "Good."; whose party; the midpoint echo; lo mein; the correction rule) plus the pillars pages and small calls.

**What changed (from the diff):** `Decisions.md` restructured into the interview locks the chapters don't yet follow, the ones they do, the later records checked against them, working decision W8, and the new open questions. The assessment, ledger, plan, README and Revision-Status were re-routed to match. The findings are unchanged; only who settles them changed. No chapter file was touched.

**Lesson, for the method:** read the author's primary decision record before any summary of it; a summary written for an experiment can misstate what's settled. This goes into the Sunday Morning [Pipeline](../Sunday-Morning/Pipeline.md#before-the-first-draft) as a line under "Check Decisions".

## P2, 2026-09-30: James's answers; the voice benchmark; the pillar pages

**James's answers** (recorded as [R9–R15](Decisions.md#jamess-rulings-for-this-revision)): the book ends on "Perfect."; the party is Elizabeth's own welcome party, and "he knows her"; "It was the crash that woke her." repeats at the midpoint; she never orders the lo mein, she goes after her books; the climax is still open and he wants to see what the story needs; yes to bringing the pillar pages into line; the healer's name, the dagger and the test chapter don't matter to him.

**Finding: the benchmark chapters aren't his.** Checking the lo mein against git showed that James's July Chapter 2 ends with "He still has it." and has no lo mein order, and that the 2026-08-28 reconciliation rewrote Chapters 1 and 2 along with the rest (Ch1: 729 → 1,680 words; Ch2: 1,141 → 1,807). Before the rewrite, the whole manuscript (Chapters 1–12b and the Coda, git `765b69b`) was about 16,600 words, with 2.8 uncontracted forms, 0.2 "Not…"/"No…" fragment paragraphs and 0.5 commentary paragraphs per 1,000 words of narration. It's now about 48,700 words at roughly 5 per 1,000 on each of those measures. James's own Chapters 1–2 score zero, zero and one commentary paragraph between them. So the prose-layer faults are the rewrite's, not his; the revision keeps the rewrite's story (which follows his locks) and returns the prose to his voice. His July chapters become the voice benchmark ([W9](Decisions.md#working-decisions)); the assessment carries a correction note.

**What changed (from the diff)**

- `Decisions.md`: R9–R15; W9; the September records table updated; open questions reduced to Q-H ("he knows her": from the party, or from before?) and Q-E (the climax, exploring).
- `Plan.md`: new section, [the climax: what the story has already planted](Plan.md#the-climax-what-the-story-has-already-planted), with four options grown from the text; Step 2 set to Chapter 12 with James's July chapters as the ear; chapter work lists for Ch1, 2, 8, 14, 15 and 18 updated; triggers updated.
- `Non-Negotiable-Scenes.md` rewritten to the interview's locks; two rows and one sentence of `Thesis-and-Controlling-Ideas.md`; beats 5, 9, 11 and 12 of `Story_Files/canon.md` (each page marked with a dated status line).
- `Promise-Ledger.md` (R1, R2, R5, P1, O4), `Assessment-2026-09-29.md` (correction note), `README.md`, `Revision-Status.md`.
- `Sunday-Morning/Pipeline.md`: one sentence under "Voice source first" (check that an author's sample chapters are still the author's text).
- No chapter file was touched.

