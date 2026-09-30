# Pass log: Pathwell revision

## Status

**Evidence, active. Book record, created 2026-09-29.** This page owns what happened in each pass of the revision: what ran, what changed (change notes written from the diff), and what each independent check found. It's the book's equivalent of the Sunday Morning [History](../Sunday-Morning/History.md): one entry per pass, newest last. A lesson that changes the method goes to the Sunday Morning notes (Pipeline, Craft or Rules) and gets a line here saying where it went.

## Before this revision

A short account of how the chapters got to where they are, so a later pass doesn't re-derive it. Details are in the linked records.

| When | What happened | Record |
| --- | --- | --- |
| to June 2026 | Discovery draft; Chapters 1–2 revised with James and adopted as the voice benchmark | [pathwell_editorial_operations.md](../Archive/Notes-2026-06-to-08/pathwell_editorial_operations.md), `chapter1_revision_journey.md`, `chapter2_revision_journey.md` |
| June–July 2026 | Multi-agent (MAP) review and prose passes; Chapters 1–2 locked (2026-07-01); the Coda made the only ending | [session_progress.md](../Archive/Notes-2026-06-to-08/session_progress.md), [INS-0001](../insights/INS-0001-unpaid-plot-debts-must-be-paid-on-page.md) |
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
7. **Promise ledger**, **Decisions** and **Plan** written. [Revision-Status.md](../../Revision-Status.md) rewritten to match the chapters; status lines added to [Open-Questions.md](../Archive/Wiki-2026-06/Open-Questions.md) and [Structural-Risks.md](../Archive/Wiki-2026-06/Structural-Risks.md); a pointer to this folder added to [Story/README.md](../README.md).

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

## P3, 2026-09-30: one current version of anything

**Why:** James: "Theres a lot of versions and notes, we should make sure that we are putting some things in like archive / legacy so that we dont keep running in to conflicting versions" (R16). The repository had three layers of rulings, a June wiki that contradicted the interview, a superseded ending still in `Chapters/`, and about 220 notes files mixed together, which is how P1 read summaries in place of James's own answers.

**What ran**

1. Classified every file outside the method folder as current, authority, or superseded, and checked the current pages for lines that contradict the interview's locks (diary buyback, lo mein as a rung, the cookbook healing Mama Baga, Elizabeth cutting herself out, eye contact stopping the draw, Papa Baga).
2. Moved 229 files with `git mv`, unchanged, and rewrote 77 links that pointed at them; converted the dead wiki links in the three root pages to plain text. Every link in the current pages resolves.
3. Corrected the stale lines in the pages that stay current (character_bible: 6; world_bible: 1; glossary: Papa Baga), each with a dated note.
4. Wrote an index for each folder: the [repository README](../../README.md), [Story/README](../README.md), the [archive](../Archive/README.md) (with what replaced each group and rules to keep it from piling up again), the [interview](../Interview/README.md), [Story_Files](../Story_Files/README.md), and the [voice benchmark](Voice-Benchmark/README.md).
5. Saved James's pre-August Chapters 1–2 as the voice benchmark, read-only, so the ear for the revision isn't only in git.

**The layout now**

- Current: the root (README, the three targets, Revision-Status, Reading-List); `Story/Chapters` (the eighteen chapters only); `Story/Interview`; `Story/Revision`; `Story/Story_Files` (eight files); `Story/Sunday-Morning`.
- Archive: `Story/Archive/` in seven labelled groups.

**Not changed:** every chapter file; the archived files' text; the Sunday Morning method, apart from Craft's two links to the archived Quick Diagnostic.

**Lesson, for the method:** the Sunday Morning notes already say not to leave a stale snapshot looking current (README, rule 7). Here the rule is now a folder: superseded material moves to the archive in the same change, with a line saying what replaced it ([archive rules](../Archive/README.md#rules-so-this-doesnt-pile-up-again)).


## P4, 2026-09-30: Step 2, Chapter 12

**Goal:** revise one chapter from the voice sources and check it, then stop for James's verdict ([plan](Plan.md#step-2-the-test-chapter)). James: "go ahead with chapter 12".

**Approach.** The story, the dialogue and every ledger fact stay as they were. The prose moves toward James's pre-August Chapters 1–2 ([benchmark](Voice-Benchmark/README.md)). That means narration contracted the way people talk; ordinary movement written as sentences instead of stacks of one-line fragments; and narrator lines that only restate what the scene just showed cut. Lines in the cautious categories were left alone unless the change was plainly a cut of redundant explanation, and every one of them is listed below for James ([plan](Plan.md#step-2-the-test-chapter), step 2).

### What changed (from the diff)

The chapter goes from 2,497 to 2,411 words and from 408 to 282 paragraphs.

**Contractions in narration.** There were nineteen: "did not" to "didn't", "had not" to "hadn't", "she had" to "she'd", "was not" to "wasn't" and so on. Dialogue is untouched, including Mama Baga's and the healer's uncontracted speech ("You are not using this arm today.", "That was not the question.").

**Fragment stacks merged into sentences.** Nothing was added or lost in these:

- the boy seeing her;
- Shade's stopped hand;
- the wagon's contents;
- the healer's examination;
- the no-glowing-paper line;
- the setting of the joint;
- the diary's contents;
- the archivist's expected questions;
- the intake rack;
- Elizabeth looking from the cookbook to the diary;
- Shade looking at her empty hand.

**Plain words for stiff ones:**

- "attempted" became "tried";
- "discussed" became "talked about";
- "Camp continued outside" became "Outside, Camp went on";
- "Then continued with the bucket" became "Then he carried on with the bucket";
- "newly received items" became "new arrivals";
- "The Space Between had returned it" became "had given it back";
- "the checking behavior" became "the checking".

**Fixes:**

- *Continuity.* The old text had "She had watched Pathwell say the scans still had the information. / She had understood immediately why that was not enough." But Elizabeth goes through the wall at Chapter 11 before Pathwell says the scans line, so she couldn't have watched him say it. It now reads: "The first night here, the archivist had told her a copy wouldn't be the same thing, and she'd said she knew." That is the Chapter 4 exchange ("The copy won't be the same thing." / "I know."). **This is new text in an emotional passage; it's for James.**
- *Logic.* The old text had "Loan meant it remained hers in a different building. / Deposit meant she could tell herself…", but she had just said no to "Store". The two lines are now one, about the loan: "A loan meant it stayed hers in a different building, and she could tell herself she'd only moved the checking somewhere safer."
- *Time of day.* Chapter 11 ends in daylight; Camp is lit by lanterns and dawn comes at the end of Chapter 12. The line now reads "Then lantern light; here it was still dark." (the plan's C item for Chapter 12). **This is new text; it's for James.**
- *Repetition with Chapter 11.* The old text had "No hand offered. / No argument. / He walked beside her instead." Chapter 11 says the same thing about ten minutes earlier in story time ("No argument. / No theatrical offer of his hand."). The line is cut to "He walked beside her."

**Cut:** narrator commentary that explains what the scene just showed. Each cut is listed below so James can restore it.

**Kept on purpose:**

- *Continuity facts:* the diary "against her ribs", the intake rack "just inside the archive entrance", the cookbook's card, FIND NANA'S SPOON checked twice, "missing meetings", "DONOR PERMISSION REQUIRED. PATHWELL IS NOT DONOR." and "Ask me before anyone reads it".
- *Characters' tells:* Shade's right-hand tell and "Are you Pathwell?".
- *A family gesture:* Mama Baga's "mouth moved at one corner", which a book-wide check suggests is a family gesture ([ledger R17](Promise-Ledger.md#relationships-and-running-elements)).
- *Every line of dialogue.*

### For James: lines to rule on

**Cuts you may want back.** Every one is narrator commentary.

1. "That was probably why it mattered." (after "Elizabeth hadn't expected the question.")
2. "Nobody was moving the world around her while she decided." (after the fiddle)
3. "Elizabeth found the ordinariness unexpectedly comforting." (after the sling)
4. "Camp had absorbed their crisis by refusing to become only their crisis. / Elizabeth had not known she needed that." (after the stew). The fresh check called the first sentence one of the chapter's better lines, and it is the cut I'm least sure of.
5. "Not pressure. / Room." (after "He waited one more beat."). The fresh check would restore it: without it the beat could read as pressure, in a chapter whose contract is about consent.
6. "Those facts could coexist without canceling each other." (after "The life in its pages was still hers.")
7. "Not because the objects were destined for anything. / … / That was enough." The middle line, "because someone had decided they were worth keeping", is kept and folded into the sentence before it.
8. "Nobody was asking her to decide what happened when he arrived." (the second-to-last paragraph)
9. "Not dramatically." (from "Camp was moving toward morning. / Not dramatically. / One person at a time."). This also removes an echo of Chapter 15's "Not dramatically."

**Kept, but in a cautious category.** Suggestions only.

- **The opening,** "Camp Cunnan was awake enough to notice trouble and asleep enough to resent it." It's the second of three personified openings in a row (11, 12, 13). The plan varies Chapter 13's opening instead, so this one can stay.
- **"It was terrible. / That, at least, felt normal."** This is the drink gag's fifth use (3, 4, 9, 12, 13, 18). Keep it here, or cut "That, at least, felt normal."
- **"Receiving weight rather than claiming it."** It echoes Chapter 4's "Receiving the weight rather than examining it." and is more aphoristic than James writes. It could go now that the sentence before it names the cookbook.
- **"Still being used. Still itself."** (the blue road notebook). This fragment pair is fine as it is.
- **"The book belonged here now. That still hurt. It also no longer felt like disappearance."** The emotional turn is unchanged; only the paragraphing changed.
- **"Elizabeth understood."** (before "Do it."). It can be cut, since "The healer waited." already carries it.
- **"Elizabeth's hand stayed suspended after the diary left it. Empty. She lowered it."** Kept as it was, now in one paragraph.
- **The closing,** "For the first time since the museum, nothing required an immediate answer." "For the first time since…" closes Chapters 4, 7, 12, 16 and 17 (Registry). Keep it, or end on the last line alone: "Elizabeth pulled the blanket Mama Baga had left over the good shoulder and watched Camp wake up."

### Check log

- **Shapes.** No opening, engine, resolution or ending changed. The one Registry change is to the motive-list device: its "Not because X… Because Z." instance in Chapter 12 is gone.
- **Checker** (Chapter 12, before → after, per 1,000 words):
  - uncontracted narration: 9.0 → 0.5 (the benchmark is 0);
  - "Not…"/"No…" paragraphs: 5.2 → 0 (benchmark 0);
  - commentary paragraphs: 5.2 → 2.4 (benchmark 0–1.8);
  - evaluative follow-ups: 0.5 → 0;
  - filter verbs: 3.2 → 3.2;
  - very short paragraphs: 49% → 47% (benchmark 12–35%).

  The filter verbs are "Shade watched it.", "Elizabeth saw the inside of her own skull", "Shade watched him go." and the like. They're comic timing and action, not filtering, so they stay. The short-paragraph share is still high because most of what's left is one-line dialogue exchanges, and those were left alone.
- **Scene diagnostic** (every scene touched):
  - *arrival:* she wants to get to help without being carried; it works as a "therefore"; she ends inside the wagon.
  - *the shoulder:* she wants it over with; "but" it's her shoulder, so she has to say when; the joint is set.
  - *Shade's hand:* they get fed.
  - *the stew:* "therefore" she goes to the archive.
  - *the archive:* she wants to keep the diary and not keep checking it; she gives it.
  - *dawn:* nothing needs an answer.

  All six pass. The explained-after-showing lines are cut (listed above). **Deletion test:** without the chapter, the diary's gift, which Chapter 15's fire depends on, and a scene of care done with hands and cloth, not pages, would both be lost.
- **Fresh independent check** (a pass that didn't write the text read the old and new versions, the neighbours, the benchmark, the contract and the ledger). *No lost setups*; Chapter 14's and 15's placements of the cookbook and diary are intact. *It confirmed the scans fix and the time-of-day fix, and found one new continuity error:* "no page going blank" contradicts the canon, where the page disappears. That was fixed back to "no page disappearing". *It flagged these other problems, all of which were fixed:*
  - the "Deposit/Storing" logic;
  - four cuts that were doing work (Mama Baga's mouth, Shade's "old Pathwell knowledge" line, the cookbook callback, "worth keeping"), all restored or folded in;
  - editor-sounding new lines ("She knew it better now." cut; "didn't feel like disappearing anymore" reverted);
  - the repeat of Chapter 11's hand-and-argument line.

  *Re-check after the fixes:* all fixes landed, no continuity errors remain, and what's left is judgment calls, all in the list above.
- **Replacement tics.** The check found the main new tic: ", then" chains (9 against 1 before, four of them "looked at X, then at Y"). They're now down to 4. Other counts:
  - ", and he/she" joins: 5;
  - colon lists: 4 (against 2 before);
  - one "and… and… and" chain (the diary's contents; James's own "and" runs are similar);
  - no "didn't quite".

  Watch all of these in the next chapter.
- **Also reverted as change for its own sake:** "His eyes went to her sling" (back to "dropped briefly to"), "sat down" (back to "sat"), and "Shade stayed by the wagon door" (back to "remained", which also removes a doubled "Shade stayed").
- **Left for Chapter 13's pass:** the closing blanket "over the good shoulder" by the fire is repeated almost word for word in Chapter 13's second paragraph.
- **Still not run:** the independent fact-check of the P1 records (see P1's check log). It was declined in the session and hasn't been re-asked.

**Result:** Chapter 12 is at L3. It's waiting for James's verdict; no other chapter has been touched.
