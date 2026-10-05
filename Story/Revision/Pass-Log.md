# Pass log: Pathwell revision

## Status

**Evidence, active. Book record, created 2026-09-29.** This page owns what happened in each pass of the revision: what ran, what changed (change notes written from the diff), and what each independent check found. It's the book's equivalent of the Sunday Morning [History](../Sunday-Morning/History.md): one entry per pass, newest last. A lesson that changes the method goes to the Sunday Morning notes (Pipeline, Craft or Rules) and gets a line here saying where it went.

## Before this revision

A short account of how the chapters got to where they are, so a later pass doesn't re-derive it. Details are in the linked records.

| When | What happened | Record |
| --- | --- | --- |
| to June 2026 | Discovery draft; Chapters 1–2 revised with the author and adopted as the voice benchmark | [pathwell_editorial_operations.md](../Archive/Notes-2026-06-to-08/pathwell_editorial_operations.md), `chapter1_revision_journey.md`, `chapter2_revision_journey.md` |
| June–July 2026 | Multi-agent (MAP) review and prose passes; Chapters 1–2 locked (2026-07-01); the Coda made the only ending | [session_progress.md](../Archive/Notes-2026-06-to-08/session_progress.md), [INS-0001](../insights/INS-0001-unpaid-plot-debts-must-be-paid-on-page.md) |
| 2026-08-21 to 08-27 | The Bible interview: the author answered one question at a time (the Bible decisions, then audit questions Q1–Q149), and each answer was locked | `BIBLE_DECISIONS_2026-08-2*.md`, `MANUSCRIPT_RECONCILIATION_AUDIT*`; indexed on [Decisions](Decisions.md#the-bible-interview-locks-the-manuscript-follows) |
| 2026-08-28 | The reconciliation executed: all eighteen chapters rewritten to the [chapter contracts](../Story_Files/PATHWELL_MAPS_L_CHAPTER_CONTRACT_MATRIX_2026-08-28.md); Chapter 18 written as the new coda; Chapter 12b removed. `Coda.txt` wasn't touched and wasn't removed | `MANUSCRIPT_RECONCILIATION_EXECUTION_LOG*` |
| 2026-09-17 to 09-18 | Experimental Architecture V2–V5, recovered-decision audits and author-intent notes. Several author decisions recorded; nothing applied to the chapters | the 09-17/18 files in [Story_Files](../Story_Files/); indexed on [Decisions](Decisions.md#later-recorded-rulings-2026-09-1718) |
| 2026-09-27 to 09-29 | The Sunday Morning method built on a seven-story collection, with the author's voice guide (09-27) | [Sunday-Morning/History](../Sunday-Morning/History.md) |

## P1, 2026-09-29: take stock (Step 1)

**Goal:** inventory, cold read, assessment, THINK and PLAN; no chapter edits ([R6](Decisions.md#the-authors-rulings-for-this-revision)).

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

**Result:** every chapter at L2 ([levels](README.md#development-levels-for-a-chapter)); nine questions for the author; plan awaiting approval. Stopped here. (Nine became seven in P1b.)

### Check log

- **Cold read (P1).** Independent; opened only the chapter files. It found the premise gap (why Pathwell was in her apartment), the doubled ending and the Coda's contradictions, the dropped dagger, Shade's unclear reason at his death, the explanation-after-showing habit and its "Not X. Y." cadence, the one shared deadpan, and the back third's slowing. It confirmed the book's strengths. Its specific claims were checked against the text; nearly all held ([where the cold read was checked](Assessment-2026-09-29.md#where-the-cold-read-was-checked)).
- **Fresh check of the P1 records.** Not run: an independent fact-check of the assessment, ledger and decisions against the chapters and source records was started and declined in the session. The records were checked by their writer only (every link and anchor resolves; the checker numbers were regenerated from the script). Run the fact-check before Step 2 begins.

## P1b, 2026-09-29 to 30: the Bible interview checked

**Why:** The author pointed out that the repository holds the interview that "straightened everything out". P1 had indexed those files but read only the September audits that summarize them, so several of its questions were ones the author had already answered.

**What ran**

1. Read the interview's locks: the three `BIBLE_DECISIONS` pages (08-21 to 08-23) and the locked questions in the `MANUSCRIPT_RECONCILIATION_AUDIT` files (Q1–Q149, 08-23 to 08-27), with the handoffs' working rules. Every locked heading was listed; the ones bearing on P1's questions were read in full.
2. Compared each P1 question and finding with the locks, then with the September records.

**What the interview settled** (from P1's nine questions): the Coda is superseded (Q93–Q103 name its contents stale); Chapter 18's cookbook beat is a silent put-back, and Pathwell chooses not to find out whether he can still prune (Q96, Q99, Q103); "It was my fault" stands unexplained (Q95); Chapter 1 has him pass as a party guest, inferred from aftermath (08-22, Q112), which superseded the July lock on Chapters 1–2; the recognition happens at the diner and the narration withholds "Shade" until then (08-23, 08-24); the crash is deliberate; the prune's content stays open (08-22, Q141); Elizabeth is witness in the confrontation, with the child as her climax choice; Shade's last choice has a locked reason (Continued 30, Q132).

**What's still open:** seven questions, Q-A to Q-G, mostly where a September record differs from an interview lock ("Perfect." or "Good."; whose party; the midpoint echo; lo mein; the correction rule) plus the pillars pages and small calls.

**What changed (from the diff):** `Decisions.md` restructured into the interview locks the chapters don't yet follow, the ones they do, the later records checked against them, working decision W8, and the new open questions. The assessment, ledger, plan, README and Revision-Status were re-routed to match. The findings are unchanged; only who settles them changed. No chapter file was touched.

**Lesson, for the method:** read the author's primary decision record before any summary of it; a summary written for an experiment can misstate what's settled. This goes into the Sunday Morning [Pipeline](../Sunday-Morning/Pipeline.md#before-the-first-draft) as a line under "Check Decisions".

## P2, 2026-09-30: the author's answers; the voice benchmark; the pillar pages

**The author's answers** (recorded as [R9–R15](Decisions.md#the-authors-rulings-for-this-revision)): the book ends on "Perfect."; the party is Elizabeth's own welcome party, and "he knows her"; "It was the crash that woke her." repeats at the midpoint; she never orders the lo mein, she goes after her books; the climax is still open and he wants to see what the story needs; yes to bringing the pillar pages into line; the healer's name, the dagger and the test chapter don't matter to him.

**Finding: the benchmark chapters aren't his.** Checking the lo mein against git showed that the author's July Chapter 2 ends with "He still has it." and has no lo mein order, and that the 2026-08-28 reconciliation rewrote Chapters 1 and 2 along with the rest (Ch1: 729 → 1,680 words; Ch2: 1,141 → 1,807). Before the rewrite, the whole manuscript (Chapters 1–12b and the Coda, git `765b69b`) was about 16,600 words, with 2.8 uncontracted forms, 0.2 "Not…"/"No…" fragment paragraphs and 0.5 commentary paragraphs per 1,000 words of narration. It's now about 48,700 words at roughly 5 per 1,000 on each of those measures. The author's own Chapters 1–2 score zero, zero and one commentary paragraph between them. So the prose-layer faults are the rewrite's, not his; the revision keeps the rewrite's story (which follows his locks) and returns the prose to his voice. His July chapters become the voice benchmark ([W9](Decisions.md#working-decisions)); the assessment carries a correction note.

**What changed (from the diff)**

- `Decisions.md`: R9–R15; W9; the September records table updated; open questions reduced to Q-H ("he knows her": from the party, or from before?) and Q-E (the climax, exploring).
- `Plan.md`: new section, [the climax: what the story has already planted](Plan.md#the-climax-what-the-story-has-already-planted), with four options grown from the text; Step 2 set to Chapter 12 with the author's July chapters as the ear; chapter work lists for Ch1, 2, 8, 14, 15 and 18 updated; triggers updated.
- `Non-Negotiable-Scenes.md` rewritten to the interview's locks; two rows and one sentence of `Thesis-and-Controlling-Ideas.md`; beats 5, 9, 11 and 12 of `Story_Files/canon.md` (each page marked with a dated status line).
- `Promise-Ledger.md` (R1, R2, R5, P1, O4), `Assessment-2026-09-29.md` (correction note), `README.md`, `Revision-Status.md`.
- `Sunday-Morning/Pipeline.md`: one sentence under "Voice source first" (check that an author's sample chapters are still the author's text).
- No chapter file was touched.

## P3, 2026-09-30: one current version of anything

**Why:** The author: "Theres a lot of versions and notes, we should make sure that we are putting some things in like archive / legacy so that we dont keep running in to conflicting versions" (R16). The repository had three layers of rulings, a June wiki that contradicted the interview, a superseded ending still in `Chapters/`, and about 220 notes files mixed together, which is how P1 read summaries in place of the author's own answers.

**What ran**

1. Classified every file outside the method folder as current, authority, or superseded, and checked the current pages for lines that contradict the interview's locks (diary buyback, lo mein as a rung, the cookbook healing Mama Baga, Elizabeth cutting herself out, eye contact stopping the draw, Papa Baga).
2. Moved 229 files with `git mv`, unchanged, and rewrote 77 links that pointed at them; converted the dead wiki links in the three root pages to plain text. Every link in the current pages resolves.
3. Corrected the stale lines in the pages that stay current (character_bible: 6; world_bible: 1; glossary: Papa Baga), each with a dated note.
4. Wrote an index for each folder: the [repository README](../../README.md), [Story/README](../README.md), the [archive](../Archive/README.md) (with what replaced each group and rules to keep it from piling up again), the [interview](../Interview/README.md), [Story_Files](../Story_Files/README.md), and the [voice benchmark](Voice-Benchmark/README.md).
5. Saved the author's pre-August Chapters 1–2 as the voice benchmark, read-only, so the ear for the revision isn't only in git.

**The layout now**

- Current: the root (README, the three targets, Revision-Status, Reading-List); `Story/Chapters` (the eighteen chapters only); `Story/Interview`; `Story/Revision`; `Story/Story_Files` (eight files); `Story/Sunday-Morning`.
- Archive: `Story/Archive/` in seven labelled groups.

**Not changed:** every chapter file; the archived files' text; the Sunday Morning method, apart from Craft's two links to the archived Quick Diagnostic.

**Lesson, for the method:** the Sunday Morning notes already say not to leave a stale snapshot looking current (README, rule 7). Here the rule is now a folder: superseded material moves to the archive in the same change, with a line saying what replaced it ([archive rules](../Archive/README.md#rules-so-this-doesnt-pile-up-again)).


## P4, 2026-09-30: Step 2, Chapter 12

**Goal:** revise one chapter from the voice sources and check it, then stop for the author's verdict ([plan](Plan.md#step-2-the-test-chapter)). The author: "go ahead with chapter 12".

**Approach.** The story, the dialogue and every ledger fact stay as they were. The prose moves toward the author's pre-August Chapters 1–2 ([benchmark](Voice-Benchmark/README.md)). That means narration contracted the way people talk; ordinary movement written as sentences instead of stacks of one-line fragments; and narrator lines that only restate what the scene just showed cut. Lines in the cautious categories were left alone unless the change was plainly a cut of redundant explanation, and every one of them is listed below for the author ([plan](Plan.md#step-2-the-test-chapter), step 2).

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

- *Continuity.* The old text had "She had watched Pathwell say the scans still had the information. / She had understood immediately why that was not enough." But Elizabeth goes through the wall at Chapter 11 before Pathwell says the scans line, so she couldn't have watched him say it. It now reads: "The first night here, the archivist had told her a copy wouldn't be the same thing, and she'd said she knew." That is the Chapter 4 exchange ("The copy won't be the same thing." / "I know."). **This is new text in an emotional passage; it's for the author.**
- *Logic.* The old text had "Loan meant it remained hers in a different building. / Deposit meant she could tell herself…", but she had just said no to "Store". The two lines are now one, about the loan: "A loan meant it stayed hers in a different building, and she could tell herself she'd only moved the checking somewhere safer."
- *Time of day.* Chapter 11 ends in daylight; Camp is lit by lanterns and dawn comes at the end of Chapter 12. The line now reads "Then lantern light; here it was still dark." (the plan's C item for Chapter 12). **This is new text; it's for the author.**
- *Repetition with Chapter 11.* The old text had "No hand offered. / No argument. / He walked beside her instead." Chapter 11 says the same thing about ten minutes earlier in story time ("No argument. / No theatrical offer of his hand."). The line is cut to "He walked beside her."

**Cut:** narrator commentary that explains what the scene just showed. Each cut is listed below so the author can restore it.

**Kept on purpose:**

- *Continuity facts:* the diary "against her ribs", the intake rack "just inside the archive entrance", the cookbook's card, FIND NANA'S SPOON checked twice, "missing meetings", "DONOR PERMISSION REQUIRED. PATHWELL IS NOT DONOR." and "Ask me before anyone reads it".
- *Characters' tells:* Shade's right-hand tell and "Are you Pathwell?".
- *A family gesture:* Mama Baga's "mouth moved at one corner", which a book-wide check suggests is a family gesture ([ledger R17](Promise-Ledger.md#relationships-and-running-elements)).
- *Every line of dialogue.*

### For the author: lines to rule on

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
- **"Receiving weight rather than claiming it."** It echoes Chapter 4's "Receiving the weight rather than examining it." and is more aphoristic than the author writes. It could go now that the sentence before it names the cookbook.
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
  - one "and… and… and" chain (the diary's contents; the author's own "and" runs are similar);
  - no "didn't quite".

  Watch all of these in the next chapter.
- **Also reverted as change for its own sake:** "His eyes went to her sling" (back to "dropped briefly to"), "sat down" (back to "sat"), and "Shade stayed by the wagon door" (back to "remained", which also removes a doubled "Shade stayed").
- **Left for Chapter 13's pass:** the closing blanket "over the good shoulder" by the fire is repeated almost word for word in Chapter 13's second paragraph.
- **Still not run:** the independent fact-check of the P1 records (see P1's check log). It was declined in the session and hasn't been re-asked.

**Result:** Chapter 12 is at L3. It's waiting for the author's verdict; no other chapter has been touched.

## P4b, 2026-09-30: what the AI-detection read teaches

**Why:** The author ran the P4 Chapter 12 through GPTZero and shared the conversation about it. It classified the passage as AI-written, which it is. His ruling: "we dont need to over correct here, or even correct. For now its just somehting to learn from." ([R17](Decisions.md#the-authors-rulings-for-this-revision))

**What changed (from the diff):**

- New page, [AI detection notes](AI-Detection-Notes-2026-09-30.md). It holds the author's handoff unchanged, under a short account of what it teaches this revision.
- R17 in Decisions.
- A row in the README's table.
- One clause on the Plan's first reconsideration trigger, pointing to the notes.
- No chapter file was touched.
- The checker, the Registry and the plan's work are unchanged.

**Lessons,** held here as candidates. None goes into the Sunday Morning method unless the author acts on this.

- P4's measures (contractions, "Not…" fragments, commentary paragraphs) track the surface of the rewrite's habits, not the voice underneath. Against the author's Chapters 1–2 the larger differences are these:
  - where the humour lives: in his chapters, in Pathwell's dialogue, not the narrator's wit;
  - how clean Elizabeth's interior thought is: in his chapters, messy worry, not precise self-diagnosis;
  - how much the senses carry a scene.
- The new text P4 wrote was among the lines the detector flagged most strongly. That supports keeping new emotional text for the author.
- The fresh check should also look for repeated joke templates inside a chapter. P4's missed "as if mostly were a medically useful category" / "as though museums were a recognized injury category".

## P4c, 2026-09-30: the narrator has its own voice

**Why:** The author, on the AI-detection notes: "iirc there should be a note that the narrator has its own voice". There is one: [pathwell_narrator_register.md](../Story_Files/pathwell_narrator_register.md). P3 had filed it in the archive with the secondary voice notes, and P4b's notes had wrongly read the benchmark's quiet narration as the target.

**What changed (from the diff):**

- `pathwell_narrator_register.md` moved from `Archive/Voice-notes/` back to `Story_Files/`, with a status line. The guide's own text is unchanged.
- Decisions: W11.
- The revision README's order of authority (voice) and its inventory.
- The Story_Files and Archive indexes.
- The Plan's first reconsideration trigger.
- A sentence in the Sunday Morning Craft page's "Narration with an opinion".
- AI detection notes, points 2–3 and the closing paragraph, rewritten with a correction note.
- No chapter file was touched.

**What it means:**

- The narrator's attitude is wanted. The author names invisible narration as his own weakness.
- What reads as AI in Chapter 12 is a narrator voice that ignores its register. It's too frequent, all the same move, present in the places the guide keeps it out of (sensation, around Shade), and loud where the guide is quiet.
- P4's cuts match the guide's "does NOT do" list. P4's kept lines weren't checked against the guide. That happens in the next pass, if the author wants one.

**Lesson, for the method:** before archiving a note as secondary, check that a current page owns its concept. Here no current page owned the narrator's register; the Craft page had one paragraph on it. This joins the archive rules ([archive README](../Archive/README.md#rules-so-this-doesnt-pile-up-again)).

## P5, 2026-09-30: craft adjustments and AI tells

**Why:** The author asked how to take the lessons into the way the writing is crafted. Then: "just to pathwell for now, and then lets research AI giveaways like these and learn from them as well… The goal isnt to deceive but just provide the best product we can that matches the guide and stlye we have in place now." ([R18](Decisions.md#the-authors-rulings-for-this-revision))

**What ran**

1. Read the voice guide's "Humor", "Pathwell-Style Comic Character" and "What to Avoid", the prose voice, the narrator register, and the character bible's voice section. Almost everything the lessons ask for was already in them. The character bible's voice section set one register for the whole cast ("dry, precise, slightly absurdist"). That's part of how the shared deadpan crept in.
2. **Research:**
   - Wikipedia's *Signs of AI writing*, read through a summary, since the page itself couldn't be fetched.
   - Chakrabarty et al. (LAMP).
   - The Antislop paper and the Slop Score.
   - StoryScope, with its percentages checked by a second, verbatim fetch.
   - Gorrie, Vollmer, Record Crash, Symban and The Argument.
3. Counted the common tells across the eighteen chapters. The vocabulary tells are almost absent; the structural ones are everywhere.
4. **Fresh check** by a separate reader, who verified every quote and statistic against its source, the manuscript counts, the guides, and the tone of the ruling. It found 13 problems, all fixed:
   - four paraphrases presented as quotes (Gorrie, Vollmer twice, The Argument), replaced with the sources' actual words;
   - three manuscript counts overstated: the mouth-corner count was 8, not 7; "jaw clenched" appears 0 times; the Chapters 7–9 "cluster" is only about half the uses;
   - one contradiction with the guides: "let Elizabeth plainly know what she feels" conflicted with the register's "'She felt sad.' Cut." It's now "vary the vehicle, don't name the feeling";
   - five lines that read as rules, softened to guidance ("usually one polished closing line per scene"; "consider changing, moving or cutting").

   It also added notes that were taken up:
   - Antislop's biggest ratios come from one model's output;
   - one of The Argument's metaphors is its quote of Nostalgebraist;
   - the narrator register sanctions "as if it had personally…";
   - "character observations" belongs among the narrator-present stretches;
   - the character-humour lines are largely inference, for the author to confirm;
   - "One sock had surrendered halfway down his calf" is word for word in Chapters 4 and 12.

**What changed (from the diff)**

- New: [Writing against sameness](Writing-Against-Sameness.md), which covers:
  - before writing: the register map, whose joke it is, the situation funny first;
  - while writing: Elizabeth's interiority, polished closing lines, texture, varying the move, new emotional text left to the author, no degrading;
  - after writing: two benchmarks, joke shapes, the fresh check's six sameness questions, no detector.
- New: [AI-Tells](AI-Tells.md): the research, with each tell set against the book's guides and its present level in the manuscript. Awareness, not rules.
- `character_bible.md`: "Where each character's humour comes from", for the author to confirm.
- Registry:
  - "Joke shapes already used";
  - three watch patterns (the narrator's "as if / as though X were…", the "category" joke, stock gestures);
  - four more things to watch for by reading.
- The revision README:
  - a "Before and while writing" section;
  - after every pass: joke shapes in step 2, the two benchmarks in step 3 (replacing the stale "Chapters 1–3"), the sameness questions in step 5;
  - two index rows;
  - "where things stand".
- Decisions: R18 and W12.
- No chapter file was touched. The 10 Kings copy of the method is unchanged (R18).

**Checker, new watch patterns** (across the book):

- the narrator's "as if / as though X were…": 11;
- "category": 9, with 3 of them in Chapter 12;
- stock gestures: 19, the densest in Chapters 7–9.

**Lesson, for the method:** a voice note that sets one register for "all characters" invites a shared voice. Keep the register for the book, and give each character a source for their humour.

## P6, 2026-09-30: the lessons folded into the Sunday Morning notes

**Why:** The author asked: "lets make sure all these notes are part of the repo for pathwell sunday notes". The lessons of P1b to P5 lived in the revision's records. The method they change is this repository's copy of the Sunday Morning notes (W13).

**What changed (from the diff)**, all in `Story/Sunday-Morning/`:

- **Craft:**
  - a new section, "Writing against sameness": the general principles, the before/while/after steps and the fresh check's six questions;
  - "Narration with an opinion" now says the narrator has its own voice and a register;
  - "Who writes what" gains the rule that new text in the cautious categories stays plain and flagged;
  - the Status list is updated.
- **Pipeline:**
  - before the first draft: map the narrator's register and each character's humour;
  - after every pass: joke shapes in step 2; checker numbers as a floor in step 3; the sameness questions, and the check that new text stayed plain, in step 5.
- **Registry template:** a "Joke shapes already used" section, and example watch-pattern lines.
- **Sources/AI-Tells:** new. The researched general list with its sources, each tell set against the voice guide and Craft rather than against Pathwell.
- **Decisions:** D17 (a detector is not a target), D18 (awareness, not rules; for now only this copy changes), and W3 extended (the narrator has its own voice).
- **History:** seven lines, marked as Pathwell-revision lessons:
  - read the primary record;
  - check the voice sample's history;
  - checker numbers are a floor;
  - track joke shapes;
  - one register for the cast invites one voice;
  - keep new text plain and flagged;
  - the narrator has its own voice, and a concept's owner should be checked before archiving.
- **README:**
  - the index gains the AI tells row, and the Craft, Registry and History rows are updated;
  - four new "Find it fast" questions;
  - a new tidiness rule (check a concept has a current owner before archiving);
  - the Status names the Pathwell additions.

**In `Story/Revision/`:**

- `AI-Tells.md` is now "AI tells in Pathwell": what the manuscript shows, and each tell set against this book's guides. The general tables and sources moved to the Sunday Morning notes.
- `Writing-Against-Sameness.md` is marked as Pathwell's application of the Craft section.
- The README's index rows and Decisions W13 are updated.

No chapter file was touched. The 10 Kings copy of the method is unchanged (D18).

## P7, 2026-09-30: Chapter 1, from the author's July text

**Goal:** The author: "lets do Chapter 1, and see how it comes out". This is the first chapter revised with [Craft: writing against sameness](../Sunday-Morning/Craft.md#writing-against-sameness). Per the [plan](Plan.md#chapter-work-lists), it is rebuilt from the author's own July Chapter 1 ([benchmark](Voice-Benchmark/README.md)) wherever the locks allow, with her welcome party as aftermath (R10). [Q-H](Decisions.md#open-for-the-author) is still open, so the chapter takes its recommended default: he met her at the party.

**How:** The August rewrite (1,680 words) was set aside and the chapter rebuilt on the July text (729 words). It keeps **79 of the author's 102 sentences word for word**, including the whole sugar-cookie passage. It adds what the later locks and chapters need, in a few plain lines. It's now 884 words.

**The register map, before writing:**

| Stretch | Register | What that meant |
| --- | --- | --- |
| Waking; the living room | narrator present (arrival) | the party's aftermath, with one small wrong detail ("cheese cubes going shiny") |
| The cookbook demand, the door | action | clinical; the dialogue carries it |
| The working and the memory | sensation and magic | narrator quiet; July's sentences, word for word |
| The blob, the bathroom | action | clinical; July's sentences, plus two plain lines of mechanism |
| The wrecked room | narrator present (aftermath) | one detail ("The banner had come down into it."), "her last guest" |
| The talk, then shoes | dialogue | July's lines; one narrator line for what Elizabeth hasn't named (the bluff) |

**Whose joke:**

- Pathwell's humour stays his breezy, polite evasion: "That confusion is quite normal." "I did say please." "Yes, I did mention the marked thing, didn't I?"
- Elizabeth stays sincere and snapping: "Do you mind?" "I'm not going anywhere with you."
- The narrator makes almost no jokes. That's July's balance.

### What changed (from the diff, against the author's July text)

**New lines, each written to meet a lock or a later chapter:**

1. **The party:** "The party was still out here. Paper cups on every flat surface, a tray of cheese cubes going shiny. Somebody's WELCOME LIZZY banner hung by one corner over the kitchen doorway. The guests had gone home hours ago." (Q112 and R10; the banner plants "Lizzy", ledger P2.)
2. **Who he is:** "She knew him, a little. He'd been at the party, talking to everybody. She'd never caught his name." (R10 and the Q-H default; supports Ch2's "What is your name?".)
3. **The cookbook:** "Nana's cookbook, three rubber bands around the spine and the title in Nana's blue marker." (Ch4's rubber bands; ledger O1.)
4. **Where the book goes:** "The cookbook fell out of her hands." (Staging: the cookbook ends with him, W01.)
5. **The mechanism:** "The light under his palm had gone wrong. It spat and flickered, and loose threads of gold dropped onto the carpet." and "It rolled over the gold on the carpet, and the gold went out." (W01: the interruption leaves loose waste, and the blob is cleanup, not a predator.)
6. **The aftermath:** "The banner had come down into it."
7. **What he's holding:** "stood her last guest, holding Nana's cookbook and what looked like her diary". July had "a stranger, holding what looked like her diary".
8. **Before "marked":** "Then he went still. / When he turned back, he was sure of himself again." (The bluff, ledger P4; Ch4's "The same kind of still he had gone in her apartment hallway before declaring the place marked".) July's hall check ("He was already moving towards the door… checked up and down the hall") moved here from after "Why could I hear my Nana?", with "the door" made "the empty doorway".
9. **The torn page:** "She looked at the cookbook in his hand. A ragged edge stuck out where the page had been." (Ch2, Ch3, Ch4 and Ch18 all refer to the torn page.)

**Small edits to the author's sentences:**

- "a man tearing through boxes" became "…her boxes".
- "the stranger said" became "he said", since she knows him.
- "Another box hitting the ground," became "Another box hit the ground."
- "with book in hand" became "with the book in hand".
- "crisp, and stained" became "crisp and stained".
- Missing end punctuation added ("Now." "Reasonable, even." "Yes, but—").
- The comma removed from "until you tell me, what is going on".
- "She asked" became "she asked".
- "Tucking the diary under his arm, "We should…"" became "He tucked the diary under his arm."
- "His attention shifted to down the hall" became "…shifted down the hall".
- Straight quotes and em dashes, to match the manuscript.

**Kept from July on purpose (the author's call if he wants them changed):**

- the comma splice "He placed his hand flat on the page, the letters glowed a soft gold.";
- the fragment "Bringing a stench of low tide that churned her stomach.";
- "They're… they're in the kitchen?" (plural);
- "She watched for a moment" (a filter verb);
- the short breath before "Ready?".

**Gone with the August rewrite:** every line of it, apart from what July already had. Lines the author might want back:

- "Because it was hers." / "That's not an answer." / "No. It's the amount of answer we have time for.";
- the "tiers" exchange ("Second-tier question." "There are tiers?" "There are now.");
- "Don't overmix them, baby. You'll toughen them.";
- "Annoyance arriving one second before fear became necessary.";
- "That's new.";
- "Oh, don't be greedy.";
- "Her heart was loud enough to qualify as a second emergency.";
- "The living room looked as though a storm had developed strong opinions about personal property.";
- the burglary "being conducted by someone with very specific standards".

Most are narrator wit, of the kind the [AI detection notes](AI-Detection-Notes-2026-09-30.md#what-it-teaches-this-revision) and the sameness checks flag. A few (the first two above) are Pathwell's own dialogue.

### For the author: Chapter 1

1. **Does it sound like you?** It's mostly your July chapter.
2. **Q-H:** is "She knew him, a little. He'd been at the party… She'd never caught his name." right? That is, he met her at the party.
3. **The banner:** does "WELCOME LIZZY" suit you as where he gets "Lizzy"? The alternative is "WELCOME ELIZABETH", leaving "Lizzy" unexplained.
4. **The party details** (paper cups, cheese cubes, banner) and who threw the party. The interview left the logistics open, and the chapter doesn't say.
5. **The bluff line:** "When he turned back, he was sure of himself again." It's narrator interpretation, but the lock needs the bluff readable.
6. **The two lines of mechanism** (the light going wrong; the gold going out). Are they needed, or does "It darted for the light in the man's hand" carry it?
7. **The opening:** the lock says the blob's pounding woke her, and "the crash" now reads as the boxes. Leave it as July has it?
8. **Anything from the August list above** you want back.

### Check log

- **Shapes.** The opening line and the final exchange are unchanged. The engine is now "the guest who stayed", and the Registry is updated. Nothing is repeated from neighbouring chapters.
- **Checker** (Chapter 1: August version → now; the author's July chapter in brackets):
  - uncontracted narration: 2.8 → 0 per 1,000 words (0);
  - "Not…"/"No…" paragraphs: 4.2 → 0 (0);
  - commentary paragraphs: 2.1 → 2.8 (1.8). The new count is two short lines, "It was the crash that woke her." (his) and "She knew him, a little…" (new);
  - "for the first time" and "apparently": gone;
  - filter verbs: 0.6 → 2.2 (2.7);
  - very short paragraphs: 38% → 19% (35% in his formatting).
- **Scene diagnostic:**
  - *Want:* Elizabeth wants him out and her things safe; he wants a charged family record.
  - *Therefore / but:* the blob at the door, *therefore* the cookbook; *but* she grabs it, *therefore* the working breaks and the blob goes for the light.
  - *Changed:* home becomes unsafe; she leaves with him, pulled.
  - *Explaining after showing:* none.
  - *Deletion test:* the opening promise and the magic's calibration.
- **Fresh independent check.** A reader who didn't write it compared the new version with the August version, the July chapter, the locks, the contract and every later chapter's references to Chapter 1.
  - **Every lock passes:** first line; the party as evidence only; the guest who stayed; the blob before the working; she tells him where the book is and he fetches it; the page can't be saved; the loose light draws the blob; "marked" as invented certainty; both objects end with him; she leaves pulled.
  - **Nothing that worked in July was dropped.**
  - **Found and fixed:**
    - a duplicated hall check, which is now one;
    - "Most of them." spending the chapter's "mostly" joke early (cut);
    - two three-item lists in the new text (cut to one and a pair);
    - "Lizzy" and "What is your name?" not yet planted (the banner, and "She'd never caught his name.");
    - the torn page never confirmed (the ragged-edge line);
    - "the man from her party" (now "her last guest");
    - the front door's absence resting on one line ("the empty doorway").
  - **Re-check:** all the fixes landed, and no errors are left in Chapter 1.
- **Replacement tics.** None found. The new lines are plain; the one "Then… Then…" run is July's.
- **Knock-on for Chapter 2:** "You broke into my apartment." now contradicts "her last guest". The narration's "the stranger" is softer now that she never caught his name. Both are in the plan's Chapter 2 row.

**Result:** Chapter 1 is at L3, waiting for the author's verdict.

## P7b, 2026-09-30: Chapter 1, restaged to the lock

**Why:** The author: "this is an outdated version I can tell, cause he is supposed to be more casually going through the boxes and then the blob shows up and he thinks its there for her. Should be notes on that". There are notes: [Bible decisions 08-22 §3](../Interview/BIBLE_DECISIONS_2026-08-22.md#3-chapter-1-entry-and-false-importance-setup) says "The blob is what changes Pathwell's behavior toward Elizabeth… that assumption kicks him into the urgent 'I need a cookbook' defense". The character bible's entry behavior says he is "calm, unhurried, insultingly comfortable in spaces that aren't his".

**Why P7 missed it:**

- P7 rebuilt the chapter on the author's July text, which predates that lock. July has him "tearing through boxes" and demanding the cookbook before the blob arrives.
- The independent check then passed the chapter because its prompt carried a summary of the locks that left that line out.
- Lesson: the author's older text is the ear for the voice, not the source for what happens; the newest lock wins on story. Give the checker the primary records, not a summary. This went into [Pipeline](../Sunday-Morning/Pipeline.md#after-every-pass) and [History](../Sunday-Morning/History.md#what-went-wrong-and-where-the-lesson-lives-now).

**What changed (from the diff):**

- **The opening is restaged:**
  - "found a man going through her boxes" (it was "tearing through her boxes, hurling their contents across the floor");
  - "He sat on the floor with a box open beside him, reading her diary like a magazine in a waiting room.";
  - "Do you mind?" / "Not at all," he said, and turned a page.
- **The blob changes him:** "It came again. A thud against the front door. Wet. Heavy." (so the crash that woke her was its first hit) / "He looked up at the door. Then at her." / "Friend of yours?" / "What?" / "The door bowed in its frame and settled back." / "He was on his feet with the diary under his arm, tearing into the next box."
- **Then July's lines resume:** "Where's your cookbook?…" ("Another box" became "A box"), "We need it.", "Another thud, harder.", "Now."
- **Knock-on fixes:** "what looked like her diary" became "her diary", since she's watched him read it; "He tucked the diary under his arm" became "He shifted the diary under his arm".
- 949 words.

**For the author (new text):**

- "reading her diary like a magazine in a waiting room";
- "Not at all," he said, and turned a page;
- "Friend of yours?", which makes the misread legible;
- "It came again."

These are character-defining lines, so they're yours to judge. The checker noted one strain: the lock says he takes material "he believes will not be noticed missing", and reading her diary in front of her pushes on that.

**Check:** Re-checked against the full text of the 08-22 §3 lock, the character bible's entry behavior and misread blocks, W01, Q112 and Q113. Casual until the blob: yes. The blob changes him: yes. He thinks it's there for her: legible. The three continuity slips it found are fixed (what woke her; the stray "Another"; "what looked like"). The checker's numbers are unchanged in kind: 0 uncontracted forms and 0 "Not…" paragraphs.

## P8, 2026-09-30: currency audit

**Why:** The author: "this is why i worry about having had so many versions and drafts. I almost think we need to go over everything with a fine too comb tomake sure we have the current version." He chose "Everything": the decision timeline, all 18 chapters, and the reference notes. Report only, no edits.

**What ran:**

1. **The decision timeline.** Six readers extracted the decisions from the primary records into [Decision-Timeline.md](Decision-Timeline.md). That's 696 rows, each quoting its source, plus each reader's open items and conflict notes.
   - Two of the readers hit the session's usage limit and were rerun after it reset.
2. **The chapter audit.** Six readers audited three chapters each, against the timeline and the primary sections. Two groups finished before a second usage limit; the other four were rerun on 2026-10-01.
3. **The reference audit.** Two readers covered canon, the world and character bibles, the glossary, the contract matrix, the voice notes, the root pages, the ledger and the plan.
4. **Verification.** A separate reader checked the 18 most consequential findings against the primary record: 12 hold, 5 partly hold, none fails. Two had cited the wrong source; the corrections are in the verification file.

**What changed (from the diff):**

- New in the repository:
  - `Decision-Timeline.md`;
  - `Currency-Audit-2026-10-01.md`, the report;
  - its folder, holding the eight readers' files and the verification.
- Decisions: Q-I to Q-L, the four places where the author's decisions disagree (the Ch18 prune, the Ch18 errand, the source of "Lizzy", the Ch6 mirror).
- Plan: a line before the chapter work lists. "Voice is the ear; the story is the newest decision", and each chapter's pass reads its audit findings first.
- Revision-Status ("What's next") and the README index.
- No chapter or reference page was edited.

**Findings:**

- 113 across the chapters, about a third already in the plan.
- About 60 across the reference pages.
- The biggest single block is Chapters 8–9: the road and the diner, which together hold about 20 findings from one lock family.

**Lesson, for the method:** an AI rewrite that follows "the locks" can still drop the scene-level staging inside them (who's present, what's said aloud, which lines were to be kept). Before a chapter's pass, read the newest decisions for that chapter, not just the plan's summary of them. This is the same lesson as P1b and P7b at a larger scale. It's now on the [plan](Plan.md#chapter-work-lists).

## P9, 2026-10-01: the author's answers to the audit (R19–R23)

**Answers** (recorded in [Decisions](Decisions.md#the-authors-rulings-for-this-revision)):

- **R19, the Chapter 18 prune.** "He chooses not to find out if he can still prune." Q96 stands.
- **R20, the next errand.** "I dont think it makes a difference to the story." Chapter 18 keeps what it has.
- **R21, "Lizzy".** He hears the name through the echo of Nana's memory when he activates the sugar-cookie page. The echo is already canon: the activating practitioner carries the strongest echo ([world bible](../Story_Files/world_bible.md#the-echo)). The cookbook's own inscription is the fallback.
- **R22, the mirror.** "theres bound to be something that makes sense already."
- **R23, the general rule.** "evaluate what works for the story overall… Keeping the answers with what works best for what we have now, rather than inventing new things that we have to make fit." The audit's staging findings are judged on story merit, preferring existing text and canon.

**What changed (from the diff):**

- Chapter 1: "Somebody's WELCOME LIZZY banner" became "A WELCOME ELIZABETH banner".
- Registry: the "Lizzy" row.
- Ledger: P2 is paid by canon (R21).
- Glossary: Elizabeth's entry now gives the echo, with the marginalia as fallback.
- Decisions: R19–R23. Q-I to Q-L are marked as answered. The Q-H default stands unless the author objects.

**Next:** triage each audit finding under R23. Each one is marked FIX (a real story problem), KEEP (it differs only from a staging lock but works) or AUTHOR.

## P10, 2026-10-01: triage and continuity fixes

**Triage.** Under R23, three readers marked each audit finding FIX, KEEP or AUTHOR on story merit. The result was 27 FIX, 87 KEEP and 0 AUTHOR ([triage](Currency-Audit-2026-10-01/triage.md)). The reviser overrode two of the readers' calls:

- The Chapter 7 "mirror" speaker stays as it is ("A conversation happening before anyone spoke" covers it).
- The diary-placement slip is fixed with one change in Chapter 12, rather than two in Chapters 16–17, as one reader proposed.

**Continuity fixes, applied (from the diff):**

- **Ch5:** "the last few hours" became "last night".
- **Ch8:**
  - "Stansbury said 'the big prune.'" became "…'the prune that went wrong.'" (Ch7's words);
  - "There's a diner twenty minutes east." became "There's coffee somewhere along this road." (with a named destination, the brothers' tracking spell in Ch10 had no reason).
- **Ch9:**
  - cut "No lucky guess. / No dead grandmother's preferences appearing in the mouth of a stranger." (it referred to a beat that no longer exists);
  - "where Pathwell had been headed before she wrecked the car" became "where the night had started".
- **Ch12:** "still inside her coat. Its corner pressed against her ribs" became "still in her coat pocket. Its corner pressed against her hip" (matching Ch16–17).
- **Ch14:** "I don't remember the name." became "I've never been there." (matching Ch9's Prague).
- **Ch17:** "went into the drawer Pathwell had originally braced three inches too low. / It now opened cleanly." became "went into a box under the rack Pathwell had originally braced three inches too low. / It slid out cleanly now." (The three-inch error was the rack's.)
- **Ch18:** the stray `}` after "Perfect." is deleted.

**Left for chapter passes** (each is more than a word or a line, or new text in a cautious category):

- Ch2: R12.
- Ch8: R11's placement.
- Ch15: Shade seeing the cost, Q132. This is the author's emotional territory.
- Ch18: R19, the repeated cookbook and apology beats, and R9's attribution.

**Records:** ledger O3 and L6 fixed; Revision-Status updated.

## P11, 2026-10-01: Chapter 1 with and without the Sunday Morning tone

**Why:** The author: "I feel like the story could benefit from at least some of the Sunday Stories tones, it can still have weight doing that, but i feel like thats really the tone Ive been shooting for, maybe we try chapter 1 with it, and chapter 1 without, and see if it helps hurts or does nothing for the story." This tests R1, which kept the Sunday Morning tone out of Pathwell. It isn't a ruling yet.

**What ran:**

1. Re-read the Sunday Morning tone sources: the Framework's core promise ("You do not need to brace yourself"; "substantial enough to matter, but comfortable enough that the reader never feels emotionally punished") and the tone guardrails (one sad moment said once, then somewhere soft to land; people the reader enjoys; human-scale stakes; endings land warm).
2. Wrote a trial, [Chapter_01_sunday-tone.txt](Experiments/Chapter_01_sunday-tone.txt). It's the current Chapter 1 with four changes:
   - the party paragraph warmed: the half-eaten "ELIZ" cake, "It had been a good party", the hall light switch;
   - "He'd laughed at her joke about the landlord, which was more than anyone from work had managed.";
   - a soft landing after the danger: "The cake, somehow, was fine.";
   - a pause before his brush-off: "He stopped. For a second he wasn't in a hurry at all. / 'Because it was hers,' he said." (The second line is the August rewrite's own, restored.)

   The sugar-cookie passage, the fight and every lock are unchanged. The trial runs 1,037 words; the current chapter, 949.
3. A blind reader read both (current first), plus the Chapter 2 opening, without being told which was the trial. **It preferred the trial:**
   - It "made me like Elizabeth before anything goes wrong" and gives the reader a reason "to spend time with both of them".
   - The page's loss and the danger kept their weight, and "Because it was hers" adds weight: "someone who understands magic confirms that the page really held her grandmother's voice", and his carelessness becomes "a choice", "more troubling than ignorance".
   - It leads into Chapter 2's comedy more naturally, and the landlord joke now pays off Chapter 2's "My landlord is going to kill me".
   - The current version's "Again, understandable reaction" in answer to her grief "reads as plain dismissal".
   - The riskiest line is "The cake, somehow, was fine.": "whimsy right next to rot", which works as release.
4. Three of the reader's notes were applied to the trial:
   - cut "more gently than anything he'd said so far" (the pause already shows it);
   - removed "three weeks", which Chapter 2 reveals;
   - put WELCOME ELIZABETH back on the banner, so "The banner had come down into it" keeps its sting.

**For the author:** adopt the trial as Chapter 1, keep the current version, or take parts of it. If it's adopted, R1 would change: some of the Sunday Morning tone (warmth, people worth spending time with, a soft landing after the hard moment) would become part of Pathwell's voice, with the weight kept.

## P12, 2026-10-01: Chapter 1 in the Sunday tone, with the author's notes

**Why:** The author: "I love the sunday tone" (R24), with line notes (R25). The trial from P11 becomes Chapter 1, and his notes are applied.

**What changed (from the diff, against the trial):**

- **What woke her:** "It came again. A thud against the front door." became "A thud hit the front door." The first thud no longer reads as a second one; the crash that woke her is left to his rummaging.
- **He smells it:** after "Friend of yours?" / "What?": "He lifted his head and sniffed. Under the cheese and the cake there was something else, faint and wrong. Low tide, a long way from any sea. / His face changed." He smells the blob, then turns urgent. Elizabeth gets the full stench later, when the ooze comes through (the author's own line).
- **Her answer:** "My Nana always made the best sugar cookies?" now ends in a question.
- **The pages:** "crisp and stained pages" became "worn and stained pages".
- **"In years" twice:** "A voice she hadn't heard in years." became "…since the funeral." "Something she hadn't felt in years" stays.
- **The diary:** "Why are you holding my diary?" is cut, since she watched him read it. "What. What just happened?" stays.
- **The misread made legible:** "Then he looked at her more carefully. / 'You really don't know?' / 'Know what?' / 'Huh.'"
- **"Marked" (the author's idea):** "He nodded at the ooze drying on her walls." comes before "your house has now been marked". The exploded blob may be what marks it. His certainty that the danger is hers is still the misread ([ledger P4](Promise-Ledger.md#premise-and-mystery)).
- **Records:**
  - Decisions: R24 and R25.
  - Plan: each pass brings in some of the Sunday tone, with the weight kept.
  - The Experiments index.
  - Ledger P4.

Chapter 1 runs 1,082 words.

**For the author:** the new lines are "He lifted his head and sniffed…" / "His face changed.", "since the funeral", "You really don't know?" / "Know what?" / "Huh." and "He nodded at the ooze drying on her walls."

## P13, 2026-10-01: Chapter 1, after reviewing the author's notes

**Why:** The author asked for push-back on his notes (R26). The review kept five notes and questioned three. His answers are R27.

**What changed (from the diff):**

- **What woke her:** "Stepping out into the living room she found a man going through her boxes." gains "One stack had gone over, and her winter sweaters were all over the rug." The crash that woke her was the boxes. Otherwise Pathwell would be calmly reading through a blob slamming the door, as the author pointed out. This replaces the 08-22 lock's wording.
- **The voice:** "A voice she hadn't heard since the funeral." became "A voice she hadn't heard in a long time." The funeral line is gone, and "in years" now appears only once (line 69, the author's own).
- **"Marked":** no text change. The nod at the ooze stays as the prop that sells the bluff ([ledger P4](Promise-Ledger.md#premise-and-mystery)).
- **Records:** Decisions R27; ledger P4.
- **Follow-up, the same day.** "A voice she hadn't heard in a long time." became "A voice that couldn't be here." This is the author's idea ("a voice that couldnt be real"), made more concrete after push-back: "couldn't be real" is a stock phrase.

## P14, 2026-10-01: Chapter 2, from the author's July text

**Goal:** The author: "lets go on chapter 2". Rebuild it the way P7 rebuilt Chapter 1. His July Chapter 2 sets the voice and most of the text. The newest decisions set the story:

- R10: she knows him a little but never caught his name.
- R12: no lo mein order; she goes after her books.
- Q118: he walks off with them without noticing.
- R21: "Lizzy" came from Nana's echo.
- R23: prefer existing material.
- R24: some Sunday Morning tone, with the weight kept.

**How:** Most of the July text is kept word for word: the stairs, "Replaceable.", the run of worries, the pinch, "a really weird Tuesday" / "It's Thursday", the neighbourhood she doesn't recognize, "peckish", the dumplings, the ticket down the gutter, the crying, "Oh, fine, you can have a dumpling", the neon dragon, "Lizzy", "The choice is yours", the butter-and-sugar warmth and "He still has it."

### What changed against the July text (from the diff)

- **Narration:** "Pathwell" becomes "he" until he gives his name (R10). "Pathwell chuckled softly" comes after.
- **The name exchange, from the August version:** "What's your name?" / "You went through my boxes. I feel like that's information I should have." / "Pathwell." / "That's it?" / "That's generally been enough." / "First name?" / "Pathwell." / "Last name?" / "Also Pathwell, if the situation becomes formal." / "He speared another dumpling." It follows "She wiped her face with the heel of her hand." Ch1 has her never catching his name, so Ch2 needs it.
- **The books on the table:** "He sat down brimming with anticipation and dropped her books on the table beside the tray before noticing Elizabeth."
- **The books leaving:** "He stood up, brushing his hands off and gathering up his things." Her point of view doesn't tell his things from hers, so the reader finds out when she does (Q118).
- **The charred diary is cut:** "the diary caught the corner of her eye… charred edges… Thumper… six toed paw print…" goes. The later locks keep the diary intact and in his hands, which leaves the warmth without a trigger. It now has one: "Lizzy." on its own line, the word he just used, then "Then a warmth, the taste of butter and sugar…" (July had "Then another warmth"). R21 now shows on the page.
- **Punctuation:** "please", "Oh, these", "brushed up against", "but nothing came out" and "half-chewed" are tidied; the dialogue tags are made consistent.
- **Chapter 3:** "You said soon." / "This is soon." / "No. This is later." / "He considered that." / "Fair." are cut. They referred to a "Soon." that Ch2 no longer has.
- **Chapter 17:** "She unpacked Nana's mixing spoon." becomes "She picked Nana's mixing spoon up off the counter." Ch2 has it already unpacked.

### For the author

1. **Does it sound like you?** It's mostly your July chapter.
2. **"Lizzy." as the trigger:** the single word that sends her back to Nana's kitchen and then to the empty table. It's new placement of an existing word, and it's emotional, so it's your call.
3. **Thumper:** the cat and his six-toed paw print went with the charred diary. If you want him back, he could live in the diary for a later chapter (it's in Ch12's archive scene).
4. **The name exchange:** it's August's voice ("if the situation becomes formal") rather than your July Pathwell ("peckish", "I'm tellin' ya"). Keep it, or reword it in his folksier register.

### Check log

- **Fresh check:** a reader who didn't write it checked R10, R12, Q118 and R21, the continuity with Ch1 and Ch3–Ch18, the changed lines, the realization, "Lizzy" and the tone. The locks hold, and the tone is "the R24 shape exactly" (the hard moment, then "Oh, fine, you can have a dumpling").
- **Found and fixed:**
  - She watched him take the books, so "He still has it" wasn't a discovery. The line is now "gathering up his things".
  - The warmth had no trigger; it now has "Lizzy.".
  - Ch17 said she unpacked the spoon, which Ch2 has already unpacked.
  - Two stacked AI beats in the name exchange ("She waited. / He kept eating.", "She stared at him.") were cut.
- **Checker (Ch2):**
  - uncontracted narration: 0;
  - filter verbs: 0.9 per 1,000 words;
  - very short paragraphs: 34%;
  - 1,120 words (July: 1,141).
- **Follow-up, the same day.** The author agreed with all three suggestions:
  - "Lizzy." stays as the trigger.
  - The name exchange is reworded toward his July Pathwell: "That's it. Easy to remember." (it was "That's generally been enough.") and "Also Pathwell. Saves everybody time." (it was "…if the situation becomes formal."). These are new jokes in his register, for him to adjust.
  - Thumper comes back where the diary is described in Ch12, in mostly the author's own July words: "Thumper was in there too: his six-toed paw print pressed into the center of a page, the ink still holding after all these years." So the diary she gives away (and that later burns) holds the cat too.

## P15, 2026-10-01: Chapter 2, the author's notes

**Goal:** the author's line notes on Chapter 2 (R28). Under R26, each note was checked against the story, canon and the other rulings before it went in.

### Applied

- **"That's fair."** becomes **"Fair."**
- **The rant:** "How am I going to even get to the meeting?" becomes "I don't have my wallet." In Ch1 she leaves with only her shoes and a coat, so the new worry is true. No later chapter has her pay for anything.
- **Line breaks:** a paragraph break before "She looked back" and before "She hurried to catch him at the corner." "looked around one more time, looking back" becomes "looked back one more time".
- **A beat after "I don't share":** "Then why am I here?" / "Company?" This is new and the reviser's. Pathwell hasn't thought about her at all, and that is his blind spot later (Q118). A narration beat like "She stared at him." was avoided, because P14's check had already cut one.
- **The ticket:** "laundry ticket" becomes "dry-cleaning ticket" in Ch2 and Ch3. The rant already says "I have to get my dry cleaning before the meeting", and Ch17 calls it dry cleaning, so the reader knows what the ticket is for before it turns up. The order stays as it was: she finds the ticket, then empties her pockets.
- **The meeting matters (Ch1):** "The guests had left hours ago, and she'd gone straight to bed. She had a meeting at nine, her first big one since she'd started." It goes in the party paragraph rather than at the wake-up, so the opening ("It was the crash that woke her." / a man in her boxes) stays as fast as it is. "Her first big one since she'd started" is new, and the author's call. The records leave her job status open (C65), and this doesn't settle it.
- **The truck:** "a plastic table sat on the street" becomes "one of the plastic tables set out at the curb", and "a truck roared past close enough to rattle the table. The ticket skipped off the edge, caught the gutter, and was gone."
- **Cut:** "A funeral she still hadn't cried at." Ch3 ("Nana. The funeral.") and Ch12 still carry the funeral.
- **Cut:** "He drummed his fingers on the edge of the table, looking around aimlessly." "through half-chewed food" also comes off this line, so that the half-chewed mouthful happens once, on "Secondly".
- **"Who the hell are you?"** replaces "What's your name?" The stiff "You went through my boxes. I feel like that's information I should have." is cut, not reworded.
- **The name:** "That's it." (was "That's it. Easy to remember.") and "Don't need one. Saves everybody time." (was "Also Pathwell. Saves everybody time."). Two quips of the same shape in a row became one.
- **"You won't let me go home."** goes into her outburst. It is her reading of him. His answer ("I wouldn't go back there tonight. But that's just me.") corrects it without forbidding anything.
- **The dumplings:** "Secondly," he said through a half-chewed mouthful, "these things are perfect. Perfectly crappy. They aren't trying to be anything they're not. You have no idea how hard it is to find that kind of quality."
- **The ending:** "She heard her again." comes before "Lizzy." It is the first time the reader learns "Lizzy" was Nana's word. "her" stays ambiguous for one line; the butter and sugar resolve it.

### Held for discussion (not applied)

**Resolved the same day.** The author: "i agree with your push backs". Both stay as written. He also asked for the changes and the reasoning behind them to go into the Sunday notes: they are now in [Line notes](../Sunday-Morning/Line-Notes.md) (worked examples) and [Craft: lessons from the author's line notes](../Sunday-Morning/Craft.md#lessons-from-the-authors-line-notes) (the rules), under Sunday D19.


- **The spoon (line 15).** It is the author's own July choice. His June–August revision notes say: "The answer: Her grandmother's mixing spoon. The only thing she unpacked." It is also a paid thread (ledger O5): FIND NANA'S SPOON in Ch12 and Ch15, and the drawer and crock in Ch17 ("Because it was a spoon."). Changing it means changing four chapters.
- **"gathering up her things" (line 141).** Her point of view would see her books leave, and "He still has it." would stop being a discovery. P14's check found and fixed exactly that. "his things" is also Q118: to him they're just what he's carrying. The plant the reader gets is "dropped her books on the table beside the tray", while she's crying.

### Check log

- The checker (Ch1–2) found nothing new. "Lizzy" appears 4 times in Ch2 (there was no new use), and 33% of Ch2's paragraphs are very short.
- "laundry" no longer appears for the ticket. Ch2's "shuttered laundromat" and Ch18's "For laundry?" are unrelated.

## P16, 2026-10-01: Chapter 3, from the author's own drafts

**Goal:** The author asked to "do Chapter 3". The Plan had it as line work only, on the 2026-08-28 text. While looking for his voice, the pass found his own Chapter 3 drafts in `Story/Archive/Manuscript/Pathwell Working.docx`: "3 - Revised" (his latest) and "Chapter 3+4" (the barter at the counter). They're now saved unchanged in the [voice benchmark](Voice-Benchmark/README.md) ([W14](Decisions.md#working-decisions)). So the chapter was rebuilt the way P7 and P14 rebuilt Chapters 1 and 2: his text sets the voice and most of the lines, and the newest locks set the story.

**Locks kept:**

- She follows him because he still has her books (Q111, Q118b).
- She gets them back only after the payment ("His transaction first", "These were never his to spend") (Q111, Q120b).
- The Camp order sits at the counter, with no tome and no envelope (Q109, Q120).
- One payment covers the order and "past bills and all", and the debt's origin isn't invented (Q109).
- Nobody asks him to prune ("Did Camp Cunnan ask you…?", and he offers "potential" himself) (Q107, Q108).
- The custodian accepts ("Are you sure?") (08-22 §1).
- A clean prune with a proportionate cost: his right arm shakes (Q109, Q148b, Q149).
- Branch imagery without timelines ("They weren't pictures of anything.") (Q148, AUDIT Ch3).
- The terrible coffee is the anchor (C7 §4).
- "Scars are outside my wheelhouse" (Q117 cites it).
- No lore tour (SEP A6).
- The choice at the door, and her books on top of the Camp books (Q111, Q114).

### From the author's drafts

- **His opening:** the streetlight; "So then, where to?"; "Sounds good, Lizzy."; "Isn't that what your grandmother called you?" / "That's… that's not an answer."; the bookstore "first"; "The right kind."; the paper that doubles into a door; "listening ears"; "the most amazing coffee"; "How do I know this isn't some kind of trap?" / "You don't."
- **The shop:** the lavender page, the smell, "Not books — lives.", "would you mind closing the door?", the shush and his whole panic sequence.
- **Waking and the cat:** the chair and the ottoman; "Just in time."; "It tasted like late nights spent studying. Like the past."; the cat's tribute; "Her eyes darted back and forth, looking for the punchline."; the love note ("Cures most wounds."); "You finish that coffee there…"; Boots, "full-time guardian and part-time blood god"; "We pay him in mice."; "Glad you asked."
- **The barter (from 3+4):**
  - "You already owe quite a bit." / "I'm good for it." / "All bills come due eventually, Mr. Pathwell."
  - "They won't come cheap."
  - the Rai Stone and the thirty Lydian coins; "Okay, now you're just messing with me." / "Aren't you?"
  - "I've got potential to sell. Lots." / "You did."
  - "Can we do this before I change my mind?"
  - "Your bill has been paid in full. Will that be paper or plastic?"
- **Tidied:** punctuation and typos only; "the keeper" is now "the shopkeeper" throughout (as the June review asked).

### What was adapted from his drafts, and why

- **The lo mein** is cut (R12).
- **The leather tome, the "say the words" vow and the Latin are cut** (Q120 removes the tome). The prune happens on the ledger instead, using the pale branches from his shadow that Ch14 and Ch18 build on. His sick, half-dead tree is kept as "Some of them were already dark, stubs where something used to grow." (Q148b: "an old tree that has been aggressively pruned again and again"), which also explains "You did."
- **The fire through the branches and "screamed in a million voices" are cut.** Ch3 is the "early clean example of pruning working normally" (Q107), and the cost has to stay proportionate (Q109). Fire belongs to the climax.
- **"Pathwell Shade" becomes "Mr. Pathwell"** (the June review; his own drafts use "Mr. Pathwell" elsewhere).
- **The magic lecture and Dewey shelving (the start of his Chapter 4) are left out.** He had marked it for cutting ("I could just remove it from the story"), and JUN 24 and SEP A6 cut the lecture.
- **"a series of avoidable mistakes" (the fate line in 3+4) isn't used,** because his Revised draft dropped it. It's listed below in case he wants it back.
- **She wakes in his chair:** his Revised has her in a chair with her feet on an ottoman, where 3+4 left her on the carpet. Ch10's memory is changed to match.

### Kept from the 2026-08-28 text (needed for the locks, or used by later chapters)

- "You said I'd get them back at the counter." / "And look. A counter." / "It's alarmingly close."
- "His transaction first." / "Yours?" / "No." / "Good."
- "I dislike paperwork" (Ch18 echoes it: "I dislike novelty.")
- "Did Camp Cunnan ask you for all of this?" (Q108)
- "Familiar things are useful." (Ch10)
- the ledger, the two fingers, the knees and the shaking arm (Ch14 and Ch18)
- "Surprise me." (in the pre-August Ch3, and cited by [pathwell_prose_voice.md](../Story_Files/pathwell_prose_voice.md) as his kind of line)
- "These were never his to spend."
- the heavier cookbook
- "worse decisions with more confidence"
- the handcart gag (Ch4 needs the cart)
- the choice at the door and the ending

All the dialogue is now contracted ("That's not the same thing").

### Cut from the 2026-08-28 text

- The alley, and the paper put on sideways.
- "NEVER AGAIN", the horse incident, "eighty-three years" and "Debt is not cheese". The debt's origin isn't to be invented (Q109; audit 3.2).
- "particular about that distinction" (audit 3.3).
- "a father she had never buried" (Plan).
- The napkin, which the love note replaces.
- "He likes documentation."
- "Camp what?" / "it is a noun".
- The "Wouldn't dream of it" / "I know what you do" exchange, which referred back to nothing. The last "Wouldn't dream of it" stays.
- About half of the one-line paragraphs.

The chapter went from 2,416 to 2,108 words.

### Knock-ons

- **Ch9 and Ch10:** the coffee memory now matches. "Two in the morning. Highlighters…" becomes "Late nights spent studying."; *Drink.* becomes *Just in time.*; "on the floor" becomes "in a chair"; *That is terrible.* becomes *That's terrible.*
- **Ledger:** P7, R7, L1, L4 and L5.
- **Registry:** Ch3's opening, the coffee row and its watch pattern.
- **Plan:** a Ch4 note. Line 510 refers to an "archive" that Ch3 has never named. The gap is older than this pass.

### For the author

New lines, kept plain:

1. **"Don't call me that."** This is her first correction of "Lizzy", where the Registry expects it in Ch3. It also sets up your "listening ears, Lizzy" joke right after. If you'd rather she not push back yet, "How do you know that name?" does the same job.
2. **"You'll get them back at the counter." / "What counter?"** These carry the promise that "And look. A counter." pays off.
3. **"He still had her books."** before she steps through. This is her reason (Q111).
4. **"Some of them were already dark, stubs where something used to grow."** This is your tree, kept small.
5. **The barter order:** "Journals, bundles of letters, sheets of poetry, a few pages of music, blank archival paper, and a wooden crate tied with twine. Enough of it that the counter complained." Your list, made larger for Q109.

Your call:

- **The fate line from 3+4** ("I say fate because 'a series of avoidable mistakes' doesn't quite have the same ring to it"): restore it at the door?
- **"Surprise me."**: keep it, or let "paper or plastic" stand alone?
- **The handcart gag and her laugh:** these are August's lines, not yours.

### Check log

- **Fresh check (a reader who didn't write it):** the locks hold, Ch2 hands off cleanly, Ch4's opening agrees, and the coffee recalls match. It found eight problems, all fixed:
  - "one more time" came before the first time;
  - "So then, where to?" had no speaker;
  - "get it" didn't match "get them";
  - the prune imagery had lost "They weren't pictures of anything.", which Ch14 needs;
  - "cut off a long time ago" was something she couldn't know;
  - "over his glasses" and "out from behind the counter" were each used twice;
  - a "narrow" door was too narrow for a loaded cart.
- **Checker (Ch3):**
  - uncontracted narration: 0;
  - filter verbs: 0.6 per 1,000 words;
  - very short paragraphs: 24% (it was about 45%; the author's Ch1 is 23%);
  - 2,108 words.
- **Follow-up the same day (R29).** The author asked: "why did we cut the leath tome, the vow, the fire, and million voices? i thought all that was good?" P16 had been wrong to treat all four as locked out. Only the tome was, by his Q120. Q120 was answered against the pre-August text, where the tome looked like the thing being bought and had no job. In his draft it is the instrument of the prune. His prune is restored from "Chapter 3+4" almost word for word:
  - the safe in the paneling, and the tome with its branded dot and rings;
  - "say the words": "I understand the cost of my needs." / "I give what may be, to protect what will." / "Perdat quod esse poterat.";
  - the roots up his forearm and the sick tree;
  - "You don't have much left to give" / "Take what you will, and spare me the lesson.";
  - the fire, and the million voices "burning out to become memories never made".

  Q120's purpose still holds: the Camp order on the counter is the purchase, and there is no envelope.

  Adaptations, all small:
  - **Naming:** "Pathwell Shade" becomes "Mr. Pathwell".
  - **The shopkeeper's question** ("are you sure this cost is worth what you must?") is untangled to "are you sure this is worth what it will cost?".
  - **His hands are swapped:** the right hand on the cover and the left across his chest, so the roots take the right arm whose tremor carries into Ch5 (Q149).
  - **A point-of-view slip:** "The pain was alive now, front and center in his mind" was in Pathwell's head, so it becomes "Whatever the pain was, it had all of him now." (new, flagged).
  - **"Then the roots let go, and he caught the counter with one hand."** is added so he can let go of the book (new, plain).
  - **Cut:** the ledger-and-shadow version. Ch14's memory of it now reads "something like it" and "the tree had grown to his chest before it ever began to branch".

  Ch18 needs nothing: its plan already removes the visible prune (R19, Q96).
  - **The author answered (R30):** "They dont leave marks." The answer is in the world bible, and Ch3 shows it in one plain line: "His right arm was shaking, but there wasn't a mark on it."

## P17, 2026-10-02: Chapter 3 with the Sunday tone

**Why:** The author asked: "theres no sunday morning version?" He was right to ask. P16 rebuilt Chapter 3 from his draft and the locks, but it never added the Sunday Morning tone that R24 asks each pass to bring in. Chapter 1 had been tried both ways, so Chapter 3 now gets a trial too: [Experiments/Chapter_03_sunday-tone.txt](Experiments/Chapter_03_sunday-tone.txt). The chapter itself is unchanged until he chooses.

**What the trial adds.** His draft already does a lot of this: "Hey, it's okay. You're fine.", the coffee "just in time" after the panic, the love note. So there are only three additions, each a soft landing after the hardest moment (the million voices) or warmth from someone the reader should like:

1. **Her:** "Elizabeth was halfway around it before she knew she'd moved." She goes to him when he falls, before anyone tells her to. It's a small first step out of compliance.
2. **The shopkeeper:** "The shopkeeper set a glass of water by his hand, then slid Nana's cookbook…" He shows care under the grumbling, with no comment on it.
3. **The parting:** "'Mind the cart on the hill,' the shopkeeper called after them. 'It pulls left.' / Then he closed the door behind them." The chapter ends warm, and the joke is his: he knows the cart he never lent.

All three are new lines in the cautious categories (an emotional beat, a joke), kept plain for him to judge. The prune, the cost and every lock are unchanged.

## P18, 2026-10-02: Chapter 2 with the Sunday tone

**Why:** The author asked: "what happened to Chapter 2 sunday tone?" Like Chapter 3, Chapter 2 never got its own Sunday trial. P14's fresh check judged that his July text already had the shape R24 asks for: the hard moment (the ticket, the tears), then "Oh, fine, you can have a dumpling." That's true, but it's no substitute for showing him a version. The trial is [Experiments/Chapter_02_sunday-tone.txt](Experiments/Chapter_02_sunday-tone.txt). The chapter itself is unchanged until he chooses.

**What the trial adds:**

1. **A stranger's kindness after the tears:** "Whoever was working the counter had sent a thick stack of napkins out with the tray." Later, "She wiped her face with one of the napkins." (it was "with the heel of her hand"). Someone noticed her crying, and nobody makes a speech about it.
2. **A soft beat before the sting:** "He left the last dumpling on her side of the tray." This pays off his "I don't share", so the man walking off with her books has just been decent to her without making a thing of it. It doesn't spoil "He still has it.": when her eyes sweep the table, they find the dumpling and not the books.

Both are new lines (a small kindness and a callback joke), kept plain for him to judge. Nothing else changes, and the locks (Q118, R12, R21) are untouched.

- **Follow-up to P17 and P18 (2026-10-02).** The author: "I dont think the strangers kindness passes the rule about if you remove it, does it change anything." Agreed. The napkins are cut from the Ch2 trial. The same test, applied to every trial addition, cuts the shopkeeper's glass of water from the Ch3 trial. What stays:
  - **Ch2:** "He left the last dumpling on her side of the tray." It pays off "I don't share", and it changes how we read him as he leaves with her books.
  - **Ch3:** "Elizabeth was halfway around it before she knew she'd moved." It changes her: she acts unprompted.
  - **Ch3:** "It pulls left." It changes how the chapter ends. It's the borderline one, and his call.

  The lesson is in the Sunday notes ([Craft rule 4](../Sunday-Morning/Craft.md#lessons-from-the-authors-line-notes); [Line notes §4](../Sunday-Morning/Line-Notes.md#4-if-cutting-it-changes-nothing-cut-it-and-dont-replace-it)): warmth has to pass the cut test too.

## P19, 2026-10-02: Chapter 3 ends on "Don't make anything of that."

**Why:** The author: "Chapter 3 should end on \"Don't make anything of that.\", and then pick up in chapter 4, the rest after that isnt needed in the chapter" (R31).

**What changed:**

- **Ch3 and its Sunday-tone trial** now end on her laugh and "Don't make anything of that." Cut: the loading of the cart, the door to the pine forest, "If you want the sidewalk…", her weighing of home against Camp, the books placed on the cart, "Don't lose those." / "Wouldn't dream of it.", the closing "Camp Cunnan" exchange, and (in the trial) "It pulls left."
- **Checked against the locks (R26).** Her free choice to continue once her books are back is locked (Q111, Q114, Q120b). Ch4's opening already shows the result: the books ride on the Camp books, and "She had put them there herself." What was missing was that she could have gone home. One line restores it: "The shopkeeper had offered to send her back to the sidewalk. She had put them there herself instead." It's plain and new, and it passes the cut test, because without it the choice looks forced. The threshold to Camp's edge (Q114) is now skipped over: Ch4 opens on "the last stretch of dirt road".
- **Records:**
  - Registry: Ch3's final line.
  - Ledger: R15 (the choice is now told in Ch4); L1 and L3 (Ch3 no longer mentions the meeting or the police).

## P20, 2026-10-02: Chapter 4, the author's Camp arrival

**Goal:** The author said: "Go for chapter 4." Per W14, the pass checked his docx first. His latest "Chapter 4" was written for an older version of the story: a fortune-teller errand, Papa Baga, a morning arrival, and a second half at a school with Stansbury. The second half belongs to the current Ch5 and is kept for that pass. Papa Baga is cut from canon. What still fits is his Camp arrival, and it replaces the August one. The healing, the archive and the Stansbury ending are locked beats the assessment called strong. They stay as August wrote them, lightly trimmed. His draft is saved to the [voice benchmark](Voice-Benchmark/README.md).

### From his draft

- **The arrival on foot:**
  - She falls behind and calls "Pathwell!", then "Darn it, where are you?"
  - She trips on a root: "followed by another greeting with the ground. The taste of dirt kissed her lips."
  - The old woman helps her up: "Now, you really do have to be careful, young lady. These trees are very spiteful." / "Where are you off to in such a hurry?" / "I was looking for my friend" ("between a confession and a complaint").
  - "He said you would say that." / "He said you would say that too."
  - "This way, if you please."
  - She hops over trunks as tall as Elizabeth.
- **The camp, seen a piece at a time through the wagons:**
  - smoke, roasting, wood being chopped;
  - the man in an old blazer with no shirt underneath, now playing a fiddle missing a string (the fiddle is the Camp's instrument in later chapters);
  - the boar on the spit and the boy at the crank;
  - children playing tag;
  - the table of people laughing.
- **Mama Baga's strength:** "There was no effort in it, no sound of strain. She simply picked it up and was on her way." It's now the crate Pathwell loaded with both hands.
- **The bear and the welcome:**
  - "You just left me in the woods." / "I did no such thing… I sent someone to get you… figuratively, and quite literally, lost without you. She's just a little nervous after the bear." / "There was a bear!?" / "Not if you didn't see her."
  - The whole welcome speech, from "home of the Cunning Folk" to "Runemasters!". The world bible's own Camp entry agrees with it.
  - "And the occasional no-good thief." / "I was only ever no good at being a thief."
  - "Home is such a permanent term. I prefer… layover." / "Humph."

### Adapted, and why

- **Night, not morning.** Chapters 2–4 are one night (AUDIT §6). "Then lantern light through the trees." is restored, and Mama Baga carries a lantern.
- **The handcart stays** (Ch3, Q114). Pathwell goes ahead with it, which is why she falls behind.
- **Mama Baga is "the old woman" until Pathwell names her.** The narration follows Elizabeth, and she doesn't know the name yet.
- **His guitar becomes a fiddle;** Ch11, 13, 14 and 16 use the Camp fiddle.
- **Left out of his draft:**
  - Papa Baga (cut from canon).
  - "Mishka", the clothes, and the grandmothers' circle. They belong to the old fortune-teller errand, and the healing takes their place.
  - "the whole bookkeeper thing or the life sucking amoeba thing" (here Pathwell discusses the blob openly with Mama Baga).

### Fixes to the August text

- "Less than yesterday" becomes "Less than I was." (it's the same night).
- "Used tonight?" / "Before tonight?" becomes "Pages used?" / "One tonight." / "Before that?" / "One. Also tonight." Both pages went tonight.
- The archive is "one of the nearest wagons on the ring" (Q75; audit #2).
- "Camp had continued having an evening" becomes "Camp was still up."
- Cut: "The word felt different in her mouth than it had in the Space Between." Ch3 never says "archive".
- **Cut narrator verdicts:** "That was fine. / For the first time in several hours, fine was enough.", "An absurdly small kindness.", "This felt rude and was probably healthy.", "The moment was over because apparently archives also had opinions about sentimentality.", "For once, he didn't decide what the moment needed." (a repeat of "He didn't." in the wagon), and "Not a vault. Not a shrine."
- **The closing list** loses "She wanted to know why Pathwell had gone still". Mama Baga "watching it too" at the edge of Camp now carries that, and Ch5 refers back to it.
- "The corner of his mouth moved" for the archivist becomes "He almost smiled." Mama Baga keeps the gesture.
- Narration is contracted. Mama Baga's dialogue stays uncontracted (her marker in the character bible). Fragment paragraphs are merged where they were only rhythm.
- **Ch5:** "behind a door in a forest that had been behind a bookstore" becomes "down a dirt road from a bookstore inside a wall" (R31 cut that door).

### No Sunday-tone trial this time

His own arrival already carries the tone: the spiteful trees, a stranger helping her up, the bear joke, the welcome and "layover". The pass looked for anything more to add, and nothing passed his cut test, so there is no separate trial. If he wants one anyway, it's quick to make.

### For the author

New lines, kept plain:

1. **The gap:** "Where the road gave out, a path went on into the trees… she could only hear the cart somewhere ahead of her." It explains why she's alone in the woods.
2. **The crate:** "the crate tied with twine, the one Pathwell had loaded with both hands and a great deal of complaining". This is your strength beat, tied to Ch3.
3. **"Less than I was."**
4. **"Pages used?" … "One. Also tonight."**
5. **"Word had gotten there before her."** This is how Pathwell knows about the healing.

Your call:

- "That was the choice. / Everything afterward was consequence." It's kept for the Ch15 rhyme ("That was the choice. Everything else burned afterward.").
- The beetle children ("It's practicing." / "Being dead.") are August's.
- Mama Baga's dry lines ("You look terrible." / "You look worse than that.") are August's too, next to your warmer Mama Baga.

### Check log

- **Fresh check:** the locks hold. It found 13 problems, all fixed:
  - **Plants and names:** the crate had no plant; the narration named Mama Baga early; "the largest wagon" clashed with the larger archive.
  - **Light and staging:** there was no light in the woods; her entry into the ring wasn't staged; she was "lifted up" and then "got to her feet".
  - **Knowledge:** Pathwell knew about the healing with no source; Mama Baga's "first look" at him came after she'd already talked to him.
  - **Prose:** "the same kind of still he'd gone" was garbled; the archivist copied Mama Baga's mouth gesture; there were too many stacked closers.
  - **Ch5:** two callbacks referred to things that were cut.
- **Not new, noted for Ch12 and Ch15:** the archive cards say "ONE PAGE USED — CHICKEN & DUMPLINGS". The cookbook has lost two pages, but only one was used at Camp, so the card can stand. Mama Baga's bracelets (Ch12–14) aren't planted in Ch4.
- **Checker (Ch4):**
  - uncontracted narration: 0 (one hit is Mama Baga's dialogue);
  - filter verbs: 0.5 per 1,000 words;
  - very short paragraphs: about 26%;
  - about 3,950 words (it was 3,536). The new arrival accounts for the difference.

## P21, 2026-10-03: the reader protocol, and Chapter 4 fixes

**Why:** The author asked: "How did Elizabeth lose track of Pathwell so easily? I think we need an independent reader asking questions as they read to find stuff like that. Might be worth the time to set up a reader protocol and do some research on how to properly analyze a story…" The P20 fresh check had passed the staging. It was right about the locks and wrong as a reader: a loaded handcart on a root-crossed path is slow, and she had a hand on it.

**What was built (Sunday D20):** [Reader-Protocol.md](../Sunday-Morning/Reader-Protocol.md), in the general Sunday notes. It rests on:

- the event-indexing model: readers track time, space, cause, goals and who is present, and stop when one of them breaks without a reason;
- Iser's gaps versus holes;
- the plot-hole types and beta-reader question sets;
- the idiot plot and Pixar's rule 19;
- suspension of disbelief;
- think-aloud reading;
- Lerman's order of feedback.

It is wired into the [Pipeline](../Sunday-Morning/Pipeline.md#after-every-pass) (the new step 6), [Craft](../Sunday-Morning/Craft.md#writing-against-sameness) and the README, and the author's question is now a worked example in [Line notes §1](../Sunday-Morning/Line-Notes.md#1-walk-the-scene-physically).

**First run, as calibration** ([report](Reader-Reports/2026-10-03_Ch01-04.md)). A cold reader read Ch1–4 in order, with Ch4 as P20 left it. **It caught the known miss** (stopper 2; questions 4.4 and 4.5): she lets the cart carrying her books go ahead, and nothing explains how a cart outpaces her. It found about 50 other questions, most of them gaps the ledger already covers.

### Fixed in Chapter 4 (holes and clear snags)

- **Losing him:**
  - She stops to shake something out of her office shoe ("Her shoes had been bought for an office."), which Ch10 already echoes.
  - "Pathwell didn't look back."
  - The cart's rattle goes on ahead, and the lantern light drops behind the slope.
  - The path splits around a tree. "She picked a side. Her books were on that cart."
  - The fallen-trunk sentence is gone.
- **"there":** "She had put them there herself, after the shopkeeper had offered to send her back to the sidewalk." The R31 line had separated "them" from the books.
- **"Did I say runemasters?" / "You did not."** The first list had already said runemasters, so "and the runemasters" is dropped. The joke now works as written: he forgot them, then remembers.
- **"He has the rest of the cart."** becomes "The archivist has the rest of the cart.", because "he" was ambiguous.
- **The cot is planted:** "a curtain was half drawn across the back" / "Behind the curtain was a cot she hadn't noticed."
- **"You keep the original"** becomes "We keep the original".
- **"Older," she said.** The line is now tagged.
- **Cut:** "Not because something was chasing her. Nothing was." The narration was claiming something she can't know, against the "marked" bluff she still believes.
- **The meeting is back, once,** where she chooses: "Back in the city, her meeting was still at nine. She noticed she hadn't thought about it in an hour." It's new, plain and flagged (ledger L1).
- **The diary:** "Elizabeth followed him, the diary still under her arm." (O3).
- **Cut:** "She couldn't decide whether that made the loss smaller or worse." The loss was being told about six times.
- The archivist's "posture" becomes "stoop" ("posture" appeared three times).
- **Chapter 3, and its trial:** "A cup of coffee swung into view, with Pathwell behind it." In the coffee exchange he was otherwise unplaced.

### Left for the author (neutral questions from the report)

- **Ch3:** nothing from Elizabeth during the tree-fire payment. The Sunday trial's "Elizabeth was halfway around it before she knew she'd moved" is one answer, and it waits on his choice of trial.
- **Ch4:**
  - Why this page, when the archive is full of recipe notebooks?
  - Does Mama Baga bring her to that wagon on purpose?
  - Which of the three handoffs (wagon, cart, archive) should carry the loss?
  - Should the Camp's minor characters share the dry register, or be plainer?
  - The narrator's remaining closers (the cookbook "heavier", "For the first time since the apartment…", the last line).
- **Ch12:** "JONES FAMILY COOKBOOK" is printed there, against the Registry's rule about the family name.

## P22, 2026-10-03: the tenth seat adopted; first report

**Why:** The author asked: "would it also help to use MAPSL 10th seat review for this stuff as well? Not just the reviewing but the writing." He linked MAPS_L's [TENTH_SEAT_REVIEW.md](https://github.com/BigCatMellow/MAPS_Lean/blob/main/playbook/TENTH_SEAT_REVIEW.md).

**Assessed before adopting (R26; MAPS_L invariant 14).** It fits one failure the reader protocol doesn't cover: a decision or verdict nobody argued against, which later passes then treat as settled. Every costly mistake in this revision was one of those:

- Ch1 rebuilt on superseded staging;
- the tome, vow and fire cut as if locked;
- "no Sunday trial for Ch2";
- the woods staging passed with no findings.

The protocol's own warning is that it turns into ceremony if it fires on everything. So it's adopted narrowly (Sunday D21; [Pipeline: the tenth seat](../Sunday-Morning/Pipeline.md#the-tenth-seat-narrow-d21)), with three triggers:

1. overriding the author's text because the record seems to require it;
2. an unchallenged verdict that later passes will treat as settled;
3. a clean pass after passes that found things.

For the writing, it tests a rebuild's riskiest decision before the prose is drafted. It never tests the author's rulings and never writes prose. MAPS_L owns the method, and the Sunday notes link to it rather than copy it.

**First report** ([Tenth-Seat/2026-10-03_Ch4-cuts.md](Tenth-Seat/2026-10-03_Ch4-cuts.md)). It fired on trigger 1: P20 left most of his drafted Chapter 4 out. **Verdict: ORANGE.** Four cuts hold: the morning, Papa Baga, the fortune errand and the grandparents' circle. The blanket claim that the rest "had to be left out" doesn't hold:

- **Mishka.** His JUN 16 ruling ("keep it the existing girl") and the August lock C2 §4 both make the Camp child a girl. The book has Milo, and the triage settled that without asking him. Now Q-M.
- **The clothes.** They pay off his own Ch2 line "Nothing to wear to it". Now Q-N.
- **The "bookkeeper / amoeba" hush** could come back. It would show when Pathwell tells Mama Baga about the blob. It's low value and isn't raised with him.
- **A caution:** "one night" (audit §6) was cited as if it bound, but it's an audit's likely sequence, not a lock. The morning cut still holds on Ch12's own lines.

Nothing in the chapters changes until he answers Q-M and Q-N.

## P23, 2026-10-03: Chapter 4, new clothes (R32)

**Why:** The author answered the tenth seat's questions. "Idk" on the girl or Milo, so Milo stays. On the clothes: "Yeah I think she should get some new clothes since it would be kinda symbolic of her entering their world."

**What changed:**

- **The clothes beat in Ch4,** after "Archive," she said. It's mostly his draft's material, given to Mama Baga (Q126: her motherhood shows through ordinary care; the tenth seat recommended her too):
  - she looks at the pajama legs under Elizabeth's coat;
  - his line: "Try these. Take what you like.";
  - she hangs a quilt from a hook to make a corner;
  - his outfit: "a mix of pastel linen, a short blazer and a thin gold chain, with a bandana holding her hair back";
  - "clapped her hands together once";
  - his draft's dropped clothes become "She left the pajamas folded on the onion crate."

  She puts her own coat back on over the top, which keeps every later "coat" true (Ch5–18).
- **New lines, plain and flagged:**
  - "the pajama legs showing beneath it, which Elizabeth had been trying not to think about since the lobby of her building";
  - "Better." (in place of his "Belíssimo!", which was another character's word);
  - "Nothing matched. It was the most comfortable she'd been all night." "Nothing matched" deliberately echoes the Camp description, where nothing matched either.
  - "The healer tucked Nana's cookbook under her arm and went out to find someone to take it." This stages the book leaving the wagon.
- **Ch12:** "moved Elizabeth's coat aside" becomes "moved Elizabeth's coat and the borrowed blazer aside".

**Reader check (D20, scaled to the change):** no stoppers; it passes the cut test. The reader asked where the healer and the cookbook were during the change, now staged. Ch13's clean clothes for Shade ("Take something that fits") and Ch16's "CAMP ISSUE" now read as rhymes with this beat.

**For the author:**

- Should anyone notice the outfit? With the coat on, only she knows.
- Her shoes stay hers. Ch10's sore heel pays that off.

## P24, 2026-10-03: the open questions from Ch2–4, answered (R33)

**Why:** The author asked to readdress the questions he'd glossed over, and answered all thirteen: "Go with your leans."

**What changed:**

- **Ch2 and Ch3** are now their Sunday-tone trials. Each adds one line ("He left the last dumpling on her side of the tray."; "Elizabeth was halfway around it before she knew she'd moved."). The Ch3 line also answers the reader's complaint that she does nothing during the fire.
- **Ch4:**
  - The healer: "What we had that would help, I've already used." This answers "why Nana's page, when the archive is full of recipe notebooks?"
  - The healer is plainer: "Then she gets to be annoyed about being alive for a while." becomes "Then she wakes up sore and hungry."
  - The muslin handoff is cut from eleven lines to two ("Archive," he said. / "I'm going that way," Elizabeth said.), so the loss is carried in the wagon and the shelf's "Available" carries the rest.
- **Unchanged by choice:** "Don't call me that.", "Surprise me.", the choice/consequence rhyme, the beetle children, Mama Baga's two sides, her unsaid motive, and the outfit kept private. The fate line isn't restored.

## P25, 2026-10-03: Chapter 5, the author's school and Cadillac

**Goal:** The author said: "Go for it." This is the first pass to run the full method, start to finish:

- **Check his docx first (W14).** The second half of his "Chapter 4" has the portal, the closet, the school, Ken and Stansbury. His "Chapter 5" has the Cadillac and the drive to the bar.
- **Write the big decisions down before drafting**, and let the **tenth seat** argue against the riskiest of them (D21). [Report](Tenth-Seat/2026-10-03_Ch5-decisions.md): YELLOW, with conditions.
- **Draft.**
- **Run the reader protocol** (D20; [report](Reader-Reports/2026-10-03_Ch05.md)) and **a fresh check against the locks**, both cold.
- **Fix, record, push.**

### What the chapter is now

- **The bridge (new, plain):** they walk out of Camp until dawn. Pathwell sleeps off the Space Between until past noon, and Elizabeth sits awake with her hand on the diary in her coat pocket.
- **His portal:**
  - the crumpled pages of light, the spinning circle, the wind;
  - the bandana from Mama Baga (R32) singed in half: "You mean that would have done this to my fingers?" / "Oh, most certainly.";
  - "The pages in his hand were gone." (new: the portal costs paper; the tenth seat's condition);
  - then "That was a portal." / "To where?" / "Here." / "Where is here!?" / "I don't know. Let's find out."
- **His school:**
  - the mop closet, "Air's fine.", "You brought us to a school!?", "Surely you've been to school before.";
  - "We went where we needed to go… Sometimes where you want to go and where you need to go aren't the same place.";
  - "It's Saturday." Then the bell and the "tidal wave of waist-high backpacks", and "Small child. What is today?";
  - "I'm going to run out of ways to say 'I don't know'";
  - Ken, "No, not at this time.", and Elizabeth's "I'm the missus… Mrs. Pathwell… Don't be rude, honey.";
  - "They're here to see me, Ken." / "Stansbury. It's been too long."
- **The adaptations, per the tenth seat:**
  - **The goal is set, the place isn't.** "Looking for my brother." (Q121: he already meant to go to Stansbury; Mama Baga sent word ahead.)
  - **"Friday."** It was "Monday" in his draft; Ch2 fixed the night as a Thursday. One line on the meeting: "her nine o'clock meeting had come and gone while she sat in a field."
  - **The scene stops at "Give me twenty minutes."**
- **His Cadillac:**
  - "Is this what waiting is like?" / "If I have, it certainly wasn't this boring.";
  - "friends become enemies… blah blah blah";
  - the interrupted Bakhtak story;
  - "He lies, you know… half-truths". This plants "I don't lie" at the bar door.
- **His swords:**
  - "Those are his weapons" / "That you need";
  - the smacked hand and "They don't need to be pointy";
  - the tree that soaks both of them, and "put your noodle away" / "Always so crass";
  - "Shotgun!", which knocks her into the hood.
- **Stansbury's work (his):** "He steals children's energy." / "That feels a bit reductive… It would never be used otherwise." / "That feels… harmless… I guess?" Plus a new clause tying it to the prune: "Spending something nobody was going to use."
- **His town and bar lot:**
  - "You would be forgiven for not stopping in the town…";
  - Pathwell getting out through the window;
  - the beer sign "they no longer sold and she doubted anyone still made";
  - "you're gonna be fine… just bring one of Stansbury's little swords" / *He lies, you know.* / "I don't lie.";
  - she takes the dagger herself (Q106: Stansbury made it, she chose to use it);
  - corn across the road.
- **Kept from August, because later chapters need them:**
  - "You pruned" and the tremor (R30);
  - the order of events and "Was it?" (Ledger P3; compressed, since Ch4 already runs most of it);
  - the dagger line "Cuts separation into things that don't separate easily…", said at the school (Ch7:95 quotes it);
  - the safety and wear lines (Q124, Q125);
  - "How thin?" (now "He said I didn't have much left to give." to match Ch3's tome);
  - "I brought myself to a bar. You happen to be in my car." (Ch6:44 rhymes with it).
- **Left out, per the tenth seat (D4):**
  - "kill him in the future" and the fortune errand;
  - the office interrogation, in which Pathwell admits "marked" was a lie (R27: Ch7–9 pay the bluff off);
  - "take me home", along with "the portal would have taken you home" and the "lost" speech (she already chose in Ch4; R31);
  - Papa Baga;
  - Stansbury calling her "Lizzy" (only Pathwell does).
- **Records:**
  - **world bible:** Stansbury's source, with the tenth seat's limits;
  - **ledger:** new row O6b; R4, R8 and L1 updated;
  - **Registry:** Ch5 row;
  - **Plan:** the Ch5 row (and a stray edit from P20 on the stages table, removed);
  - **voice benchmark:** his Ch5 draft.

### Check log

- **Tenth seat (before drafting):** YELLOW. Conditions met: the clock line, the portal as a one-off that costs paper, the scene stopping at "wait at his car", one line for the meeting, the author's own words on Stansbury's source with no narrated verdict, "He lies" planted, no mocking "Lizzy", and the dagger line at the school.
- **Reader (cold, Ch1–5):** no stoppers. Fixed:
  - the dagger "under her coat" (not under the linen);
  - the diary in her coat pocket;
  - the meeting line, which no longer reads as news;
  - "Fine compared to what?";
  - "That settled it.";
  - the bookstore parallel made clear;
  - the order-of-events replay compressed.
- **Fresh check:** YELLOW. Fixed:
  - the doubled "We went where we needed to go." (now "What do you mean, apparently?");
  - the portal's cost;
  - the Ch6 rhyme restored;
  - "this week's stock" (Q122b);
  - a narrated verdict on "harmless" cut;
  - "It had been twenty minutes." twice;
  - the hall seen before she'd looked, and an untagged line;
  - "late afternoon" / "evening sun" (now "low sun");
  - "It didn't reach the rest of his face." (a stock gesture) cut;
  - "grey" made "gray".
- **Checker (Ch5):**
  - uncontracted narration: 0;
  - very short paragraphs: 20%;
  - 3,198 words (it was 2,155).

### For the author

New lines, kept plain:

1. The dawn bridge: "slept until well past noon, the way she imagined people slept after giving blood."
2. "The pages in his hand were gone."
3. "Looking for my brother." / "Apparently." / "What do you mean, apparently?"
4. The meeting line.
5. "Give me twenty minutes."
6. "Spending something nobody was going to use."

Your call:

- Stansbury smacking her hand. It's from your draft, and it's sharper than his August self.
- The one second-person line, "You would be forgiven…". It's yours, and the only one in the chapter.
- Stansbury's source now partly settles what Q106 left open. Keep it?

## P26, 2026-10-03: reader protocol on Chapters 1–5

**Why:** The author said: "Use the independent reader protocol." A fresh reader read Ch1–5 cold, in order, as they stood after R34, and saw no earlier report ([report](Reader-Reports/2026-10-03_Ch01-05.md)). It found no plot holes. There were three small holes, three stoppers that each cost a reread, and a list of snags, most of them already tracked as deliberate.

**Fixed:**

- **Ch1, the doors.** "She opened the door all the way" becomes "She opened the bathroom door all the way". It was unclear which door she was behind.
- **Ch1, the spoon and the cookbook.** "They're… they're in the kitchen?" becomes "They're… in a box in the kitchen?" Ch2 says the spoon was the only thing she'd unpacked.
- **Ch5, Elizabeth's line.** "Spending something nobody was going to use." becomes "Selling off potential nobody was going to use." The reader couldn't tell what she meant. It now points back to Ch3's "I've got potential to sell".
- **Ch5, why walk all night.** "Pathwell wouldn't open anything near the wagons, so they walked…" The reader asked why they didn't portal from Camp.
- **Ch5, a repeated question.** The Cadillac's "How much?" / "Enough." / "That's not an amount." is cut. The car's "How thin?" asks it again, and better.
- **Ch5, a typo:** "burst in to" becomes "burst into".
- **Ch4, fragment paragraphs.** The "Not X. / Y." count drops from five to three. "Not gratitude. Not consolation. Just contact." becomes "Mama Baga put a hand on Elizabeth's shoulder and left it there a moment."; "Nothing glowed. Nothing announced itself as important." becomes "Nothing in it glowed."; the aphorism "That was the problem with important things. They almost always were." is cut. "Not burned. Spent.", "Not hidden. Not displayed. Available." and "Not because he had her things. He didn't." stay.
- **Ledger:**
  - P1's stale set-up cell now matches the current Ch1–2.
  - O5's spoon location is fixed.
  - New open-deliberate rows: L12 (the shadow in her window, the second thing from Ch1's hall), L13 (Pathwell and streetlights, a habit), L14 (the "no-good thief" line).

**Left as they are (gaps already covered, or by design):**

- why he's in her flat, and the diary (Q112, R10, R25, P1);
- "Lizzy" (R21);
- her choice told at the top of Ch4 (R31);
- the cot behind the curtain (R33);
- "Was it?" going unanswered (P3);
- the meeting's quiet passing (L1);
- "You would be forgiven" (R34).

**For the author (the reader's neutral questions worth his time):**

1. In Ch3, does Pathwell know the stacks will floor her, and is leaving her alone his choice? It's his own drafted scene.
2. In Ch5, is her flat "You're unbelievable." the reaction he wants to losing the meeting, after Ch2's "a meeting that I cannot miss"?
3. In Ch5, should Elizabeth react when Stansbury asks "Was it?" about her own door?
4. Should the reader ever learn her family name, or Nana's first name? Ch4 keeps both off the page.

## P27, 2026-10-04: the reader's questions, answered (R35)

- **Ch3 (and its trial):** "She pulled her hand back. None of that had been hers, and she held on to that. / Then something was. The next turn hit her like a door slamming." The books' feelings start it, and her own panic finishes it. That keeps the lock on ambient charge (08-21 §4.15), keeps Ch10's "a room full of other people's feelings", and takes up the author's instinct that it's a panic attack.
- **Ch5:** after "nobody had answered": "Elizabeth almost asked whose door it was, if it wasn't hers. She didn't." It's new and plain. It answers the reader's question and leaves Ch9 to say it.
- **Unchanged:** the meeting reaction; the names kept off the page.

## P28, 2026-10-04: Chapter 6, the author's bar

**Goal:** The author said: "Go for it." This was the same full process as P25: his drafts first (W14), the decisions written down and tested by the tenth seat ([report](Tenth-Seat/2026-10-04_Ch6-decisions.md), YELLOW), then the draft, then the reader ([report](Reader-Reports/2026-10-04_Ch06.md)) and a fresh check (GREEN with small fixes). His bar drafts come from an older architecture (the bar outside time, the brothers drunk, the blob attacking her in a void inside the bar). August had already followed his skeleton: the neat bar, the appletini, darts, the red sky and the keys.

**From his drafts:**

- **The bar:** "The bar wasn't nearly as dingy as she'd imagined. It sat as a point of pride for the owner and the patrons, neater than it should have been… The plastic on the seats was worn from years of supporting customers too inebriated to do it for themselves."
- **The order:** "Good afternoon, ma'am. What will it be?" / "I'm not too sure." / "Well, what do you normally have?" / "She didn't have an answer for that either." Then his "Appletini for her, and a pair of something domestic for my friend here and I".
- **His toast across her and Stansbury's shoulder turn:** "No idea what's up with him."
- **His mint thud, adapted** (the tenth seat's conditions):
  - It's a physical sound she happens to notice. There's no smell, Pathwell's head doesn't come up, and it comes before "Mine.".
  - "She could have sworn one of them came a hair before his hand did. / She decided she was tired." This is the one line that leans on the world bible's "no special perception". It's his call.
- **The red sky:** "Red sky at night, sailors' delight… My mom used to always tell me that. It means tomorrow's going to be nice." / "We have to get there first, Mrs. Elizabeth… We still have the night." (skipping down the steps).

**The ending:**

- **The chapter now ends on "Then, from the far side of the Cadillac, a thud. / Wet. Heavy."** It echoes Ch1's first thud, and Ch7 still opens on the smell. Before, the chapter ended "Then the smell reached them. Low tide. Wet rot.", which Ch7 then repeated.
- Pathwell's closing stillness is cut, because Ch7 opens with it. Stansbury still sees where he's looking before handing over the keys.

**Kept from August:**

- the mirror scene in Pathwell's point of view (R22; now logged as W15 against 08-23 §6–§7);
- "Mine." / "Not here.";
- Stansbury's quiet check that she chose to come;
- the dart that misses the board;
- the fish argument;
- "He disappears constantly. Quiet is newer.";
- the tab argument;
- the keys.

**Left out of his drafts:** the bar outside time, the drinking, the void attack, "How do I know this is real?", her outburst, and Stansbury's cruel speech. The tenth seat confirmed this cut on 08-23 §8 ("Do not make the brothers cartoonishly cruel") and Q128b, not on the stale bible line about "keeping people small". Also left out: "She's in."

**Trimmed (Plan's line items):**

- **Narrator verdicts:** "That turned out to be good."; the "Nobody… Nobody… Nobody…" run; "It was the kind of familiarity built out of repetition rather than affection…"; "The room warmed around them. Not magically…"; "That felt irresponsible."; "The fun had not vanished… They couldn't."
- **Fragment paragraphs** merged.

**Fixed after the reader and the fresh check:**

- "You said you came here because something didn't fit" becomes "Your brother said something didn't fit" (Stansbury said it, in Ch5).
- A plant for Ch7's "The mirror": "Stansbury looked toward the back hall, then back at him."
- **Staging:**
  - he sits back down "on her other side";
  - the thud comes from "down the bar";
  - "Pathwell stopped mid-turn".
- **Time:** "all evening" becomes "all day".
- **Repetition:** "a few minutes" twice; "apparently" twice; "She saw that too."
- **The sky sentence.**
- **Drinks:** two beers on the tab, and his beer is no longer "untouched".

**Records:**

- Decisions W15;
- Registry Ch6 row;
- Plan (Ch7 still needs the triage fix for "The mirror" at 321 and 431, and "You said that inside" at 331);
- ledger P4's stale quote;
- voice benchmark: his Ch6–7 draft.
- **Noted for the reference pass:** the character bible's Stansbury entry still carries "keeps others small", which Q127/Q128 superseded.

**For the author:**

1. The mint thud's "a hair before his hand did". Keep it, or make the thud plainly innocent?
2. The bartender remembers Pathwell from seventeen years ago, but in Ch5 Pathwell asks "What are we doing here?" Fine as Pathwell not knowing where Stansbury was taking them?

## P29, 2026-10-04: Chapter 7, line pass

**Goal:** This is a line pass, not a rebuild. Chapter 7 is the locked blob fight (R0 §7: the blob goes for Pathwell, Elizabeth cuts him out with the dagger, Stansbury burns it), and the triage found nothing to fix in it. The author's own drafts of this fight come from the older architecture, where the blob takes Elizabeth. One exchange from them still fits. Because it's line work and not a rebuild, there was no tenth seat (D21's triggers didn't fire). The reader ([report](Reader-Reports/2026-10-04_Ch07.md)) and a fresh check did run. Per R36, the reviser's leans are applied and listed below, without stopping to ask.

**What changed:**

- **From his draft:** Pathwell "went for his coat, patted it, and came up with nothing." / "You mean to tell me you brought zero books with you!?" / "Yes! It slipped my mind! Would you please focus!?" Now there's a cause for his helplessness: Ch5's portal used his pages, and the books went to Camp.
- **"The mirror" (the triage gap):** Stansbury, who had seen him go to the back hall (Ch6's new plant), says "The back hall"; Pathwell says "The mirror." "Not here." is Pathwell's again, so "You said that inside." is true.
- **Fight staging, after the reader's stopper:**
  - Pathwell stops "halfway across the lot".
  - The blob rises at the far side of the Cadillac (Ch6's thud) and "crossed the lot toward him".
  - Stansbury yanks open the back door for the box.
  - Elizabeth plants her feet rather than a foot on the tire.
  - Stansbury is "a few yards off".
  - The light is "the last of the red light" and the ground is dirt (Ch5: "kicked-dust"), with no "pavement", "asphalt" or "parking-lot light".
  - "Let's get off the road first" becomes "Let's get away from here first".
- **Trimmed:**
  - "Elizabeth accepted that because lately she had developed an appreciation for people who knew where their answers ended." (the Plan's third telling)
  - "Not burned away. / Unmade, at least here."
  - "There it was."
  - "Not resolution. Not victory. Just the first time…"
  - "That should have helped. It didn't."
  - "years passed between them in about half a second"
  - two of three "worse"es
  - "Pathwell swallowed" (next to the blob "swallowing" him)
  - "Not reassurance. Correction." became "like a correction"
- **Her speech:** "Important enough to carry your books" became "Important enough to follow your cart through the woods" (she never carried them).
- **Prose:** narration contracted, and fragment paragraphs merged where they were only rhythm. The fight keeps its short beats.
- **Ch4:** its closing "For the first time since the apartment, Elizabeth walked away from it on purpose." became "…stayed on the shelf, and Elizabeth didn't go back for it." Ch7's last line is now the only "For the first time since the apartment".
- **Ledger:** L7 marked fixed (Ch8 quotes "the prune that went wrong" exactly). L8 (Ch9's "where Pathwell had been headed") goes to the Ch8–9 pass.

**The reviser's leans (R36), for the author to overrule:**

1. **"Whose decision was that?"** and **the last line**, "For the first time since the apartment, nobody was telling Elizabeth where to go.", both stay. They're the chapter's turn, and they set up Ch8's crash.
2. **The "Important enough…" speech stays.** The reader found it more built than her usual snapping voice, but it's her one speech and the book's turn into her agency.
3. **"Not me." / "No."** stays (the triage kept it). The reader noted it spends some of Ch9's "theory dying"; that's for the Ch9 pass.
4. **Ch8's "Lizzy—"**, five lines after Ch7's correction, goes to the Ch8 pass.

- **Follow-up to P28 (2026-10-04).** The author: "I noticed in the bar scene that stansbury smiled into his beer before he got it." Fixed: "Stansbury smiled down at the bar." The reader and the fresh check both missed it. The reader protocol's staging questions now ask "Is anything used before it arrives?", and the author's note is in Line notes §1.

## P30, 2026-10-04: Causality pass, Chapters 1–7 (calibration and fixes)

**Goal:** The author suggested turning the "used before it arrives" question into a fuller causality check. D22 added the causality pass to the reader protocol (commit 31c0d7b). This run tests it on Ch1–7, using Ch6 as it stood before the beer fix. **It caught the beer** as a snag, along with other gaps the earlier passes had missed. [Report](Reader-Reports/2026-10-04_Ch01-07_causality.md).

**Fixed (smallest fix each):**

- **Ch1:**
  - "She'd thought he'd left with the rest." (why a man is still in her living room after the party)
  - "she heard tape rip in the kitchen before he came back with the book in hand" (how he found the cookbook in a box)
- **Ch4:** The turnip boy says "Pathwell said bring these to you," to Mama Baga. That's why he has the books.
- **Ch5:**
  - Stansbury arrives "a walkie-talkie still in one hand". He answered Ken's radio call, which explains how he knew where they were.
  - "Her sleeves were still damp from the tree." The sword soaked them, and the soaking now carries over.
- **Ch6:** "for my brother here and I". The second beer is now plainly Stansbury's.
- **Ch7:**
  - "She shoved the keys into her coat pocket" before the dagger.
  - Pins and needles return to her numb fingers before she has to drive.
  - Stansbury collects "the foam sword and the baton".
  - She pulls out "the way the car was already facing", since nobody tells her where to go.

**Left alone, as by design or locked:**

- Ch2: the books leaving under her nose (Q118/R28).
- Ch2: the spoon as "the only thing she'd bothered to unpack" (O5).
- Ch2: the coins left on the table.
- Ch4: no transit from the Space Between to the road (R31 cut it there).
- Ch4: Mama Baga knowing the order of events. Pathwell told her off the page, and "Word had gotten there" covers it.

**The reviser's leans (R36), for the author to overrule:**

1. The Ch5 soaking stays, now carried over by one line, and isn't cut. It's the swords' first demonstration, and it's funny.
2. Stansbury's walkie-talkie explains his arrival without a new line of dialogue.
3. "Brother" rather than "friend" in Pathwell's order. It's the cheapest fix, and Pathwell knows exactly who he's ordering for.
4. Ch7's direction is "the way the car was already facing", not a turn someone gives her. That keeps the last line true: nobody tells her where to go.

## P31, 2026-10-04: Chapter 8, line pass and the echo

**Goal:** a line pass on the midpoint crash and Shade's arrival, plus R11's echo. The author's own draft of this material (his "Chapter 7" in the docx) was written for the older story: a "meeting with himself in the future", a flash spell, and "Mr. Shade" blowing her flat and carrying her off. It's the voice source here, as W14 asks, but not the story. Decisions were written down before drafting, and the tenth seat tested them ([report](Tenth-Seat/2026-10-04_Ch8-decisions.md): **YELLOW**). Then came the reader with the causality pass ([report](Reader-Reports/2026-10-04_Ch08.md): no stoppers, four snags, twelve quibbles), and a check against the tenth seat's conditions.

**What changed:**

- **The echo (R11):** "It was the crash that woke her." is its own paragraph. It comes after the engine dies, the dust settles and the hubcap rolls away, and after "Her heart was beating hard enough to make the steering column feel alive under her palms." Placed there, "woke" reads as what it means, not as her being knocked out. Nothing near it points at the echo.
- **The name:** the opening no longer repeats Ch7's correction beat for beat. Pathwell says "Elizabeth, keep driving." / "He'd gotten her name right. It didn't improve the sentence."
- **From his draft:**
  - Pathwell's "Okay. I understand that you might be upset," merged into the existing "extraordinary overreaction", so it stays one joke.
  - The fence post the car clips, and "how upset the farmer was going to be when he saw it".
  - Not used: the side mirror torn off by a pole (mirrors already carry weight in Ch6–7).
- **Stansbury's beat of cost** (Plan row 8): he stands by the wreck with his hand on his ribs and doesn't tell her what to do. She holds out his dagger and he says "Keep it." The narration no longer says how she feels about it.
- **Staging, from walking the scene and from the reader:**
  - The farm driveway crosses the ditch on a concrete culvert. That's what the wheel hits, and why Stansbury's axle is "in a drainage culvert" (Ch10).
  - Stansbury is already belted (Ch7). He checks her seatbelt and tells Pathwell to put his on. The box of foam swords goes over on Pathwell, who comes up with a hand at the back of his neck.
  - Shade gets out under the dome light at the edge of his headlights. At fifty yards she sees only his height and the face; the coat and hair come once he has walked up to a car's length away.
  - He no longer looks at a dagger he couldn't see; the dagger is on her, against the seat, as she gets in.
  - Pathwell asks to come ("Then I'm coming with you."), and Shade refuses ("Not in my car. … Not you."). That answers why nobody takes the empty front seat.
  - Pathwell, lit by the headlights, steps aside to let the car by. The sedan was facing the wreck, so she sees him through the windshield first.
- **Line work:** short paragraphs went from 52% to 34%, and the checker's commentary paragraphs from 16 to 4. Cut: "Not finished. / Quiet. / There was a difference.", "That mattered.", "That was worse in a more satisfying way.", "That helped. A little.", "appreciated that against her will", "She appreciated him for it. / She resented that she noticed.", "That should have been satisfying. / It wasn't.", "That almost made the choice feel safer than it was." and the triage's optional "objected to the substitution". "somebody had finally said there were pieces…" was stale (Pathwell had said so in Ch7) and became "the man in the sedan had pieces Pathwell wouldn't give her". Kept because later pages or locks rely on them: "Not compulsion. Awareness.", "late to the decision", "No recognition.", "Wrong.", the hand, "Same ingredients. / Different recipe.", Shade's explanation (Ch9:394 quotes it), "Drive.", "following another man who sounded certain", "Too late to call it an accident."
- **Records:**
  - Ledger R2 is paid.
  - Ledger L8 is marked fixed (Ch9's "where the night had started" was fixed in P10).
  - W16 logged; Plan row 8 and the status table updated.

**The reviser's leans (R36), for the author to overrule:**

1. **The road reveal stays (W16).** This is the big one. In August he locked a different version. She takes the man for Pathwell after the crash, the brothers don't see her go, and she only recognizes him at the diner when he talks about Pathwell as someone else. The October triage kept the road version under R23. His own draft also has the reveal at the roadside, and it's what Ch9 is built on. Restoring the lock means rebuilding this chapter's second half and Ch9's first half. Under W8 a difference from a lock is his call, so it's put to him.
2. **The echo goes after her heartbeat on the wheel,** not straight after "Stopped." The tenth seat allowed either; this one reads less like she was knocked out.
3. **Stansbury lets her keep the dagger.** It's a new gesture, and it's plain: his one beat of cost, and the reason she still has the dagger in Ch9.
4. **Shade refuses Pathwell a seat: "Not in my car. … Not you."** It's new, and a reader would otherwise ask why Pathwell just doesn't get in. It also fits the draw (his hand keeps opening toward Pathwell).
5. **Kept despite the reader's quibbles:** the opening line gives away that she crashes (it's the lock's cited line, and the chapter's hook); "The thought made her unexpectedly angry."; Elizabeth's sarcastic "Perfect," (the word passes from Pathwell in Ch1 to her here, then to the ending).

**Next:** Chapter 9. If W16 stands, its front half needs de-duplicating against the road (the tenth seat's note).

## P32, 2026-10-04: Chapter 9, the diner

**Goal:** a line pass on the drive and the diner. The author said "Go for it" after P31 without overruling W16. So the road reveal stands, and this pass takes the tenth seat's note: the front half of Ch9 shouldn't re-tell the road. His own draft of the diner chapter is in the older story: Shade calls her "Lizzy" and orders her breakfast, reads her mind, explains the salt and pepper shakers and the "observer", and wolves come out of the dark. It was used for voice and small things, not story (W14). No tenth seat: as in P29, none of D21's triggers fired. The reader ran with the causality pass ([report](Reader-Reports/2026-10-04_Ch09.md)): no stoppers, six snags and fourteen quibbles. Its fixes are applied.

**What changed:**

- **No longer re-told from the road (Ch8):**
  - Shade's "it only tells me which way" exchange.
  - The resemblance paragraph (habits, head tilt, empty space; Ch8 already did this).
  - "You know pieces. / Of Pathwell. / But not now." (the diner now opens with "You don't know me." / "I met you on the road twenty-five minutes ago.").
  - The "old versions of his excuses" back-and-forth. The draw beat now comes in through "You drove toward him because your hand told you to." / "I drove because it wouldn't stop."
  - Kept: the hand opening and the quiet "No" (C4 §1b), "He used to," and the list of nouns.
- **From his draft:**
  - The old song on the radio, her humming giving her away, Shade tapping the wheel and singing under his breath until he loses the words.
  - "You don't have to sit back there."
  - The waitress (blue-and-white uniform, wild hair under a little white cap) looking at her Camp clothes and deciding not to ask.
  - The coffee: grounds "used once already", her face not hiding it, the waitress unsurprised.
  - Her order: cheesy grits with extra pepper, two eggs sunny side up. She still orders it herself (C4 §3).
  - The bacon she chews and chews, and that's exactly how she'd have made it.
  - "I assume you're paying for this." / "All I have to my name right now is my diary and a foam dagger."
- **Causality:**
  - **Money.** She has had no wallet since Ch2, so she can't pay at the register. Shade pays for both, and the pay-phone beat goes with it (no coins). "She did know where the night had started." (ledger L8) moves outside under the sign.
  - **The receipt.** The waitress writes the directions on the back in blocky capitals and underlines the second left after the water tower twice, which is what Ch10 says. Before, Elizabeth wrote them herself.
  - **The coffee.** Ch9 no longer recalls the Space Between coffee. Ch10 makes that recall on the road, where the tracking spell catches it, so it isn't spent twice.
  - **"Never the point."** Shade can only conclude this because she now tells him the blob came "while he was standing in my living room".
  - **The clock.** The crash was after dark and the diner less than an hour later, so outside it's "still full night". Ch10 opens with one clause: "She had been walking for most of the night."
  - **Mirrors.** "the way Pathwell did" is cut: she has never seen him drive.
- **Line work:**
  - Commentary paragraphs went from 19 to 3, and short paragraphs from 47% to 36%.
  - Cut: "Agency, apparently, was not a staircase…" (Plan), "That saved it. / Barely.", "There it was." (twice), "Of course.", "Good." as narration, "Ordinary information. / Again.", "almost enough to make him sympathetic", "Not because Shade had sent her. / Not because Pathwell had called her back."
  - The end is now "Nobody had sent her, and nobody had called her back. She had a question now, and this time she intended to make him answer it."

**The reviser's leans (R36), for the author to overrule:**

1. **W16 stands** on his "Go for it", so Ch9 is built on the road reveal. If he wants the August version after all, Ch8's second half and this chapter's first half are the rebuild.
2. **Shade pays for both breakfasts.** She has no money, and it's his own line ("I assume you're paying for this"). No thank-you exchange; the cut test took "I'll pay you back."
3. **The Space Between coffee recall is left to Ch10.** In Ch9 the coffee is just terrible and still settles her shoulders.
4. **Kept despite the reader's quibbles:** "twenty-five minutes" twice (it's Shade's running joke, and she calls it); the "Good." / "Fair." rhythm in Shade's dialogue (it's his voice).

**For the Ch10 pass:** after a night of walking, "Her mouth still tasted like coffee." and "another hundred yards" need checking against the new clock.

## P33, 2026-10-05: Chapter 10, the brothers from his draft, and the Ask

**Goal:** rebuild the brothers' half of Chapter 10 from the author's own draft (W14). His draft runs from after his diner chapter (peas, the walk to Stansbury's house, the library, the letter and lists, "A crappy cup of coffee") into his "Chapter 10?" (the catch). It was written for the older story: the brothers drunk at the bar, Pathwell hearing "the voice", and a vision of the diner. The pass also trims the Ask (Plan row 10). The decisions were written down first, and the tenth seat ran on them ([report](Tenth-Seat/2026-10-05_Ch10-decisions.md): **YELLOW**, with G3 **ORANGE** as written). Then came the reader with the causality pass ([report](Reader-Reports/2026-10-05_Ch10.md): no stoppers, seven snags, fifteen quibbles). Its snags are fixed.

**A correction to P32.** The tenth seat found that P32 broke a lock. Continued 7 (LOCKED A) has the tracking catch *while Elizabeth is at the diner*: the diner's terrible coffee makes her think of the Space Between's at the moment Pathwell reaches for the same memory. P32 had moved her memory to the road. It's back in Ch9, in one sentence: "it was the Space Between's coffee all over again: a plain white mug, an orange cat, *Just in time.* Late nights spent studying." That also fixes the clock. The brothers no longer sit idle for seven hours. They walk two miles home, the working catches while she's still at the diner, and the lists find her on the road an hour or so later. So Ch10 is night, not "early morning". "She'd been walking for a little over an hour" replaces P32's "most of the night", and "The dark waited outside the windows" replaces "the gray morning". Ch11's museum is still before sunrise.

**What changed:**

- **The walk home, in his lines:**
  - "She is our responsibility, Leo." / "She's your problem, Pathwell. I'm just here for you."
  - "I do my best work on the fly." / "I've seen you work. I didn't know that was your best."
  - The letter of longing and the grocery lists as Stansbury's idea; "Leo, the next time I call you an idiot, you smack me right in the face."
  - Two slaps, "Bank it."; "Let's roll, big cat." / "Please don't start calling me that again." / "Too late, grande gatto."
  - Stansbury carries the box of foam swords home and takes it in the van (his own bracketed note asked for this). "Can you find her?" / "No." / "Good." (the draw finds Shade, not her) moves onto the walk.
- **The house, in his lines:**
  - Unlocked, in a small town where "most everyone knew better".
  - The library half a floor down, in "skyscraper piles" (Continued 10 says downstairs).
  - "Children's stories? Leo, you mustn't be so desperate." / "Copies. Not all of us are willing to mortgage our potential to that shopkeeper of yours." His draft says "bookkeeper"; it's the shopkeeper.
- **The working:**
  - Stansbury's instructions are his: "A shared experience works best." / "You just have to get lucky." / the tracker line / "You are better at this than me", re-seated on the lists.
  - Stansbury goes upstairs to dig out the lists, which is why Pathwell has to shout "Stansbury!".
  - The catch is his: "Really?" / "What do you mean, really?" / "I just didn't expect it to work so soon. Or at all." / "Why do you keep sounding so surprised?" / "A crappy cup of coffee."
  - Pathwell still cycles through shared memories before the coffee catches (Continued 7). It stays passive ("Can she feel this?" / "No.").
- **The letter:** the Ellison estate letter and its cost beat stay ("If I use this, it's gone." / "Not the thing." / "It makes the cost mine to approve."). His draft's letter "confiscated off some lovesick kid" was the decision's first choice. The tenth seat held it ORANGE: Stansbury's "copy before I buy" (ledger R9) pays off in Ch11 and Ch17, and a confiscated note wasn't bought. So the kid's letter goes, and his "Children's stories?" exchange carries the school instead.
- **Fixes from the reader:**
  - The brothers' section opens "While Elizabeth was still at the diner…", so the reader knows it's a rewind.
  - Stansbury connects "He did say coffee. On the road." / "It's a long road."
  - She walks toward the bar "because it was where the night had started, and the wreck was somewhere on the way".
  - "Let's roll, big cat," is tagged to Stansbury.
  - The list only gives turns, so Pathwell says "Left. Soon." and Stansbury supplies the water tower.
  - The box goes in the van. The peas are "mostly thawed" when Pathwell gets out.
- **The Ask (Plan row 10):**
  - The second pass is cut to its landing: "So you paid the cost yourself." → "…the method was yours to choose." → "No. You know enough. Whatever happened after that became Shade. But you still chose it." / "Yes."
  - Cut: the thesis lines ("No magic. / No philosophy…", "That was the answer…", "The question was answered. / The problem was not…"), "That part mattered…", "That mattered too.", "felt the words arrive without any magic helping them", the "advisory committee" simile, and the third coffee recital.
  - Kept intact: "Because I thought I knew the cleanest way through it.", "Quickest." / "And cleanest, I thought." (Ch11 quotes them), "My choice produced the failure he came from", and "I heard him." / "That's not the same as listening." (Ch14 echoes it).
- **Line work:** commentary paragraphs went from 16 to 2, and short paragraphs from 52% to 36%. The brothers' half is about 1,800 words, against the tenth seat's ceiling of about 1,470. The overage is the author's own walk and house, kept by lean 3 below.
- **Records:** W17; Registry (Leo; the Ch9 and Ch10 shapes); glossary (Stansbury: Leo, "big cat"); ledger L15 (both names unpaid after Ch10); Plan row 10; status table.

**The reviser's leans (R36), for the author to overrule:**

1. **"Leo" and "big cat" / "grande gatto" are in.** They're his; his June note already says "Leo Stansbury is the brother of Pathwell". Only Pathwell says "Leo". They appear only in this chapter, so ledger L15 asks whether he wants one more use later.
2. **The estate letter stays, not the lovesick kid's.** The kid's letter would break Stansbury's "copy before I buy", which Ch11 and Ch17 pay off. His school still shows up, in the children's stories.
3. **His walk-home banter is kept nearly whole,** even though it runs past the tenth seat's length. Dropped from it: the gate that knocks Stansbury over, the fridge raid (chicken thigh, pasta salad), the kicking match in the booth and the drunk line.
4. **The slaps stay.** They're his, and they show two very old brothers being children with each other.

## P34, 2026-10-05: the after-pass routine, caught up for Chapters 8–10

**Why:** The author asked: "Just to be sure, you're following all the protocols that have been built including the Sunday stories". Not all of them were being followed. P31–P33 ran the decisions, the tenth seat, the reader with the causality pass, the checker, and the records. They skipped steps 1 (Sunday Morning tone guardrails), 4 (scene diagnostic), 5 (fresh check), 7 (replacement tic) and 9 (change notes from the diff), and the light Sunday touch R24 asks for. A pass that didn't write the text ran those steps on all three chapters, against the primary records ([report](Reader-Reports/2026-10-05_Ch08-10_fresh-check.md)). It found real problems in each. New standing rule: Sunday D23 / Pipeline step 10, under which every pass reports the routine step by step.

**What the fresh check found:**

- **Replacement habits.** The "Not X. / Y." fragments were gone, but other habits had grown in their place:
  - people pointedly *not* doing things (17 uses);
  - jaw, stomach and "went still" gestures (24);
  - objects acting like people (11);
  - a spoken "Good." shared by four characters (8).
- **Closing lines.** Chapters 8 and 9 had about one polished closing line every hundred words.
- **Chapter 8's ending.** It was the only one with weight and nothing warm after it.
- **Told twice.** The diner told "never the point" twice: the narrator's "a theory dying…" came first and did Shade's line's job. The Ask said its central point about four times.

**Changes, from the diff** (Ch8 +10/−12 lines, Ch9 +16/−18, Ch10 +5/−21):

- **Chapter 8:**
  - **The ending.** "Her stomach tightened." is cut. Light Sunday touch, flagged: "Beside the Cadillac, Stansbury, one hand still on his ribs, raised the other. Elizabeth raised hers." It's the warm beat before the hard close, and it sets up Ch10's lifted hand from the wheel.
  - **Narrator conceits cut:**
    - "The rest of the Cadillac objected."
    - "His hair had finally achieved something he couldn't defend."
    - "where his hubcap had died" (now "where the hubcap lay")
    - "as if it had answered a question he hadn't wanted asked out loud" (Ch9's wrist line keeps that image)
    - "as if it had personally chosen to become relevant"
    - "Pathwell's coat moved like punctuation…"
  - **Smaller fixes:**
    - "That's fair." → "Fair." (as R28 ruled for the same line in Ch2)
    - "That is a terrible start." → "That's…"
    - Elizabeth's "Good." after "I'm getting coffee." cut
    - "gotten behind her" → "gotten down the road" (Pathwell was standing next to her)
- **Chapter 9:**
  - **The reveal.** "Something small and embarrassing came loose… a flattering explanation." is cut, so "You were never the point." is the first time the verdict is said. The concrete line the lock wants back (refinements §13) is restored: "pulling her into the hallway because he'd already decided the danger belonged to her".
  - **Shade's script.** "And if he says he doesn't?" / "Then ask what he decided he was allowed to do." is cut. It scripted Elizabeth's own step in the Ask (§15). "Ask him what he chose." stays (ledger P5).
  - **Repeated "pieces".** The second telling ("I know what he knew in places. I remember what he remembered in pieces.") is cut.
  - **Narrator glosses cut:**
    - "The gesture was Pathwell's. The restraint around it wasn't."
    - "Not Pathwell done badly, or Pathwell in another coat."
    - "and Elizabeth believed that too"
    - "That was what made it hard."
    - "That one she understood more than she wanted to."
    - "Nobody had sent her, and nobody had called her back."
  - **Hand beats.** Two of six are cut. The peak at the table and the closing image stay.
  - **Coffee props.** The mug, cat and "Just in time" are cut here; Ch10 gives them from Pathwell's side.
  - **Smaller fixes:** Elizabeth's "Good. Keep remembering that." loses the "Good."; the dagger lies "beside her", since the coat is on her.
  - **Light Sunday touch, flagged:** after Shade pays, "Elizabeth took the last triangle of toast off his plate. Shade let her." It shows the thaw without a sentence about it.
- **Chapter 10:**
  - **The Ask.**
    - Cut: "For them." / "Without asking them." (466 had already said it, and the run of "Yes." was using up the final one); the narrator's "He had spent himself, and somehow he'd turned that into permission."; the third telling of "Shade remembers pieces of you. / Old pieces."
    - **Pushed back on one cut.** The fresh check also wanted "a thing in his hand" and "The blobs keep confusing the two of you" gone. They stay: C4 §1a puts the draw in the Ask, and the triage kept Elizabeth's restatement as the version of it the chapter has.
  - **Camp.** Her abstract motive ("I want somewhere this isn't just…") becomes a remembered one, which is what Continued 10 asks for. New and flagged: "Mama Baga didn't ask me anything I didn't want to tell her." (from Ch4, where Mama Baga didn't ask about the coat or the apartment).
  - **Smaller fixes:** the shoe "started to rub" (it was personified twice); the peas are on his neck in the van; "That is not what I asked." → "That's…".
- **Ledger:** L2's note about the diner phone is updated (the phone has been gone since P32).

**The routine for P31–P34, step by step (D23):**

| Step | P31 (Ch8) | P32 (Ch9) | P33 (Ch10) | Now (P34) |
| --- | --- | --- | --- | --- |
| 1 Sunday tone guardrails | skipped | skipped | skipped | done (all three) |
| 2 Shapes in the Registry | partly (Ch8 row not updated) | done | done | Ch8 row checked: its opening and ending lines still hold |
| 3 Checker | done | done | done | done |
| 4 Scene diagnostic | skipped | skipped | skipped | done (fresh check §§8.2, 9.2, 10.2) |
| 5 Fresh check | skipped | skipped | skipped | done |
| 6 Reader protocol (causality) | done | done | done | n/a (P34 is cuts plus three plain lines) |
| 7 Replacement tic | skipped | skipped | skipped | done; fixed in part (see below) |
| 8 Deliberate ambiguity left alone | done | done | done | done |
| 9 Change notes from the diff | from intention | from intention | from intention | from the diff (above) |
| Tenth seat | done (YELLOW) | not triggered | done (YELLOW) | not triggered (cuts) |
| Light Sunday touch (R24) | skipped | skipped | skipped | done: Ch8 the raised hands, Ch9 the toast; Ch10 needed none |

**Still open:**

- The shared "That is…" / "Do not…" deadpan, used by Elizabeth, Pathwell and Stansbury alike, is only partly fixed.
- The "Elizabeth looked at X" rate is 5–9 per 1,000 words, against about 2 in the author's own pages.
- Both are book-wide habits. They belong to the reference-pages pass and the remaining chapter passes, not a patch here.

**For the author:**

1. **The diner's sign.** His draft says "DINNER 24/7", and the narrator-register page quotes it. The manuscript says DINER. Was the misspelling deliberate?
2. **Who says "Camp" first.** In Ch10, Pathwell says "Camp" first (his deferral) before she chooses it. The lock says Elizabeth says it first. That's the text from before this pass, and the triage kept it.
3. **The three plain new lines are leans:** the raised hands, the toast, and Mama Baga not asking.

## P35, 2026-10-05: the reader checks tone and rules across Chapters 1–10

**Why:** The author said: "Okay so have the reader make sure he goes through all that and make sure we are sticking to the tone and the rules." The reader protocol now has a third pass, the [tone and rules check](../Sunday-Morning/Reader-Protocol.md#the-tone-and-rules-check) (Sunday D24). The reader goes through all eight items for every chapter:

1. the tone guardrails and R24
2. the scene diagnostic
3. the line-note lessons
4. writing against sameness
5. the replacement tic
6. who wrote what
7. the records
8. the routine itself

Each item is marked holds, breaks or n/a. Two independent readers ran it across everything revised so far, each reading from Chapter 1: [Ch1–5](Reader-Reports/2026-10-05_Ch01-05_tone-and-rules.md) and [Ch6–10](Reader-Reports/2026-10-05_Ch06-10_tone-and-rules.md).

**Verdicts:**

| Chapter | Tone and rules |
| --- | --- |
| Ch1 | holds |
| Ch2 | holds (one question for the author) |
| Ch3 | holds |
| Ch4 | breaks, mildly but widely |
| Ch5 | mostly holds (a staging hole at the tree) |
| Ch6–10 | hold, with tics to trim |

No stoppers. No missing light-touch moments: every chapter already has its soft landing, and adding more would be the density the AI-tells list warns against.

**Fixes, from the diff** (Ch4 −35/+17 lines, Ch5 3, Ch6 2, Ch7 4, Ch8 6, Ch9 9, Ch10 11):

- **Ch4 (cuts only, no new text).** It was the worst chapter for sameness: 41 look beats, 9.8 per 1,000 words against about 2 in the author's pages, and ten "Not X." fragments, after P26 thought it had cut them to three.
  - **Look beats:** eight cut. "Mama Baga looked at her." twice; "Elizabeth looked at the pile, then at her."; "Elizabeth looked at it."; the archivist's look; "Elizabeth looked at the boy, who was losing interest rapidly."; "He looked up."; "Mama Baga watched him for a moment."
  - **Personifications:** four cut. The onions "accepted her without comment"; she "resented the blanket for trying"; the camp smelling "like a better decision than bark tea"; the horse drawn "from rumor".
  - **"As though":** two cut ("saved lives before"; "the only task she had agreed to perform"). The collar line stays, because ledger R17 cites it as Mama Baga's care.
  - **Fragments:** "Not quickly.", "Not theatrically." and the two "Nothing…" sentences cut.
  - **Glosses:**
    - "That mattered to Elizabeth more than it should have."
    - the three "Because…" sentences at the archive
    - "The unease under his joking didn't leave."
    - "The offer surprised both of them."
    - "and Nana's cookbook was inside" (the fourth telling of the loss; the guardrail is one sad thing, said once)
    - "because it was there and didn't require either of them to say anything useful"
  - **One name for one thing:** the blue notebook is "the notebook" throughout.
  - **Smaller:** "That sounds as bad as she looks." (read twice by two readers). The closing "You were about to." is cut, so the shape isn't used a third time with Ch6.
- **Ch5:**
  - **The tree (a staging hole).** The Cadillac is "parked under the one tree in the lot", and Stansbury "stepped out from under the branches" before he strikes the trunk. That's why the other two get wet and he stays dry.
  - **A gloss cut:** "Nobody said anything else about it, and nobody had answered."
- **Ch6:** two glosses cut ("Elizabeth had started noticing that very little could be enough."; "and that was what made her believe it").
- **Ch7:**
  - Three glosses cut ("and that ended the joke"; "and that was answer enough from him"; "Now they were quiet together, holding whatever came next between them.").
  - "Important enough to give up mine" → "…give up Nana's cookbook" (two readers found "mine" ambiguous).
- **Ch8:**
  - **New, plain, flagged:** "Or pull over and let me drive," Pathwell said. "I am an excellent driver." The reader asked why she couldn't just stop on an empty road. Stopping would only hand Pathwell the wheel and end the question; the ditch doesn't. It calls back his Ch6 line.
  - **Restraint notes:** four cut ("Pathwell didn't answer.", "Pathwell said nothing.", "The man who always had an answer close at hand didn't have one.", "and didn't argue").
  - **Hands on the wheel:** one of the four beats cut.
- **Ch9:**
  - **Contractions:** Elizabeth's three uncontracted lines that sounded like Shade are now contracted ("That's not the normal response.", "Don't start doing that.", "That's an extremely low bar.").
  - **"Good.":** her "Good." becomes "Okay.", so "Good." is Shade's again.
  - **Cut:** "He left it there."; "A person sorting his grammar around memories that didn't belong to his life."; "He didn't add anything to make it easier to hear."; "It wasn't for Elizabeth, and it wasn't exactly for Pathwell either."; "Pathwell in the car saying Drive." (the list keeps two).
- **Ch10:**
  - **The Ask.** "So you paid the cost yourself." / "Yes." / "And that made you feel…" merged into Elizabeth's one step: "And paying for it yourself made you feel like the method was yours to choose."
  - **The letter.** The gloss before the longing is cut ("The page wasn't about finding anyone…"), because the images that follow carry it.
  - **The heel.** It hurt at the start and then "started to rub" a mile later. Now the shoes are only uncomfortable at the start.
  - **Cut:** "which was the worst injury by a considerable margin" (the opening had four jokes in fifteen lines); "because fast certainty had become its own problem"; Stansbury's second "Of course."
  - **The van.** It comes up on the far side of the road and stops on the far shoulder.
- **Records (stale quotes the readers found):**
  - Ledger O6b and R34 note the newer Ch5 wording.
  - Ledger R15 now quotes Ch4's opening as it stands.
  - Registry: the Ch2 Pathwell row (the "if the situation becomes formal" line is gone from Ch2), and the "without asking permission" row (Ch2 dropped).
  - Ledger L1 ("three times"; Ch5 now has the line it wanted).

**Kept against a reader, as leans (R36):**

1. **"It was a decent time. She let it be one."** (Ch6): it's her choosing to enjoy the evening, not a gloss.
2. **"late to the decision"** (Ch8): the tenth seat and the triage keep it.
3. **"Too late to call it an accident."** (Ch8's last line): the Registry and ledger R3 use it. The second reader found its "it" unclear and would end on her realizing. That one's for the author.
4. **The slaps, "Bank it." and "big cat" run** (Ch10) are his own lines.
5. **"The draw finds him."** stays: "draw" is the book's word.

**Lines that aren't the author's and were never flagged one by one (item 6).** These are for him to confirm or cut. Each is plain unless noted:

- **Ch3:** "the counter complained"; "as though posture had become the problem"; "which was stupid. Missing a page should have made it lighter."
- **Ch4:** about twenty jokes and narrator lines kept from the August text. Among them:
  - the sock that "surrendered"
  - the tea "after a long argument with bark"
  - the turnip boy who "forgot the interaction"
  - the archivist's dry run at the door and the shelves
  - "twelve and badly assembled"
  - "soup was an argument you could win" (the reader would keep it)
  - Elizabeth explaining why she gives the whole book
  - her reasons for going, spelled out at the end
- **Ch5:**
  - "like a man measuring a room"
  - "You pruned." / "Hello to you too."
  - "That is a more compelling version." / "It's also a worse description."
  - "That fixes it."
- **Ch6:** "She let it be one."; "Not now. Not here. Not necessarily not her."
- **Ch7:** "She had become very aware of how much machine she was responsible for."; "Elizabeth laughed once. Both men stopped. Nothing was funny."
- **Ch8:** "Or pull over and let me drive… I am an excellent driver." (new in P35)
- **Ch9:**
  - "She believed him, mostly because he'd bothered to make the distinction."
  - "Pathwell would have done that. Probably."
  - "For the first time Shade smiled without looking like Pathwell. It was smaller, and meaner around the edges, and his own." (the reader would keep it)
- **Ch10:** "less defense in it and more of something Elizabeth didn't trust herself to name"; "And paying for it yourself made you feel like the method was yours to choose." (new in P35)

**The routine for P35 (D23):**

| Step | P35 |
| --- | --- |
| 1 Sunday tone guardrails | done (reader, item 1, all ten chapters) |
| 2 Shapes in the Registry | done (the stale Registry rows are fixed; no opening or ending changed) |
| 3 Checker | done |
| 4 Scene diagnostic | done (reader, item 2) |
| 5 Fresh check | done for Ch8–10 in P34. For Ch1–7 the last fresh checks are P7–P29. Not re-run: P35 is the readers' own fixes |
| 6 Reader protocol | done (this pass); not re-run on its own fixes, which are cuts plus two plain lines |
| 7 Replacement tic | done (reader, item 5, with counts) |
| 8 Deliberate ambiguity | left alone |
| 9 Change notes from the diff | done (above) |
| Tenth seat | not triggered (cuts, and readers' findings are not an unopposed verdict) |
| Light Sunday touch | checked: none missing in Ch1–10 |

**The routine for earlier chapters.** The readers rebuilt it from the log. Ch1–5 never recorded step 4 (scene diagnostic) or step 7 (replacement-tic count) before this pass, and Ch5 never recorded step 1. Those passes came before D23, so it's a missing record rather than a broken rule. This pass has now run all three for Ch1–10.

## P36, 2026-10-05: Chapter 11, the museum

**Goal:** a line pass on the museum, in the author's voice where his draft gives one. His museum draft was written for the older story: Shade hearing "the narrator", a lock-picking entrance and a jump scare, a fight with exploding sheets, and Stansbury healing Pathwell with a soldier's poem. The decisions were written down first, and the tenth seat ran on them ([report](Tenth-Seat/2026-10-05_Ch11-decisions.md): **ORANGE**). Its trigger was the triage's "Chapter 11 needs nothing", accepted with no findings and sending nothing to the author. Then the reader ran with all three passes, including the tone and rules check ([report](Reader-Reports/2026-10-05_Ch11_reader.md): one stopper, eight snags, sixteen quibbles), and the fresh check ran against the previous version ([report](Reader-Reports/2026-10-05_Ch11_fresh.md)). Their fixes are applied.

**What changed, from the diff** (Ch11 rewritten in place, from 3,831 words to about 3,750; Ch10 −8 lines):

- **The road accusation, restored** (C3 §3, LOCKED B; W18), in the lot: "You left the crash with her." / "Yes." / "You took her from me." / "She wasn't yours to take from." The 08-28 rewrite had dropped it. The triage kept it out because "no later chapter uses them", but three later locks cite this scene.
- **The author's lines:**
  - **Parking.** Stansbury drives past the disabled spaces: "Well, I don't want to get towed for parking in a blue spot. What if someone comes along and needs it?" / "Are you serious?" / "Look, just because we're trying to find a bad guy doesn't mean we need to be one." This replaces "I have suffered one vehicular loss tonight", the car-loss joke's fourth use.
  - **The lobby.** "The museum was dim, the sparse glow of… lights cutting corners off the shadows… a cannon, flanked by two soldiers, one in dark blue and the other in gray: two brothers split by land and by ideology… photographs of still-framed ghosts, letters home."
  - **The graffiti house, given to Pathwell:** "Civil War soldiers would come through and leave graffiti. Draw something silly. They were messages home, or attempts to be remembered as something beyond literal cannon fodder. These were men and boys looking for a chance not to be lost to time."
  - **His soldier's poem, inverted.** It's planted on the tour: a man wondering if he'll ever again know the smell of lilac on his wife. In the aftermath, Stansbury looks at it and goes for the first-aid box instead. Spending a fourth record after three were destroyed would undercut "That is not the same as fixing it."
- **The stopper (reader).** The Vale letters, the household notebook and the medical ledger were shown in the front rooms, but the blast that destroys them is in the far gallery. They're now its side cases ("the museum's best things kept close to its oldest one"). The tour through the rooms keeps the poem and the floorboard.
- **Causality:**
  - **The clock.** "The drive took most of what was left of the night." Ch10 ends around one in the morning; the museum is pre-dawn gray; that's unconfirmed, a reading of the text.
  - **The letter.** Pathwell had no pages after Ch7. Now Stansbury: "That's from my library. You took that while I was upstairs."
  - **Her hand.** "her good hand" → "her hand" (she isn't hurt by the case yet).
  - **Staging.** Elizabeth is "a step from the plane's edge", and "the nearest case" hits her.
  - **His ribs.** Pathwell has "one arm across his ribs", and the cold pack goes to his ribs, because Ch14 relies on his rib pain.
  - **The dagger.** It's seen at the back of her waistband in the lot (ledger O4).
  - **The healer.** Stansbury: "Find the healer before you do anything else." She goes through hurt and alone, and Ch12 has the healer.
- **Plan row 11:**
  - Cut: "good hand", the "Three adults" exchange, the narrator's "because she had chosen Camp and the route belonged to that choice", and "The sentence changed the room. / Not magically. / More effectively."
  - Kept: her three spoken "Camp"s.
- **Ch10.** "Pathwell likes museums." / "Museums like me." / "They do not." is cut. It's the same shape as Ch11's "I support the arts." exchange, which is the better one.
- **Line work (tone and rules):**
  - **Glosses and flourishes cut:**
    - "left it behind with excellent signage", "three fonts", "calling the ocean damp", "the proportions of an unsuccessful dog"
    - "That was irritatingly good."
    - the narrator's verdicts on Pathwell ("as though seeing the difference between a plan and its consequences…"; "among the consequences of protecting her after she told him not to")
    - "Possibly because Stansbury's tone had finally discovered a frequency…"
    - "Which was worse."
    - "No softening. / No correction."
    - the "Not X. / Y." runs in the blast, which become one contrast: "a quartermaster's rather than a battlefield's"
  - **Repetition cut:** about twelve look beats and two draw-hand beats; the second "Three times."; "I support this policy." (the same shape as "I support the arts."); "Shade kept walking."; "I'm standing right here" (her speech has "I'm standing here"); the second "Yes." after "The information."
  - "A porch in summer" (Ch10's letter) becomes "A kitchen door in summer".
  - The last line is plain: "Outside the high windows, it was daylight."
  - The checker counts no commentary paragraphs (11 before); short paragraphs are down from 48% to about 32%.
- **Records:** W18; ledger O4; Registry row 11; Plan row 11; the status table.

**The routine (D23):**

| Step | P36 |
| --- | --- |
| 1 Sunday tone guardrails | done (reader, item 1: holds; no light touch needed) |
| 2 Shapes in the Registry | done (row 11 updated) |
| 3 Checker | done |
| 4 Scene diagnostic | done (reader, item 2) |
| 5 Fresh check | done |
| 6 Reader protocol, with the tone and rules check | done |
| 7 Replacement tic | done (reader and fresh check: ", and" joins and colon lists rose. The worst joins in the blast are split; the rest go to the next fresh check) |
| 8 Deliberate ambiguity | left alone |
| 9 Change notes from the diff | done (above) |
| Tenth seat | done (ORANGE; answered by W18 and the author questions below) |
| Light Sunday touch | checked; none needed (the tour is the chapter's quiet stretch) |

**Not re-run:** the reader and the fresh check on the fixes themselves. The fixes are the readers' own suggestions, plus the gallery move.

**Carried to later passes:**

- Ch14 says "I can hold it" where Ch11 says "I can contain this".
- Ch12 has Shade say "All right.", the word Pathwell broke here.
- The shared deadpan across Pathwell, Stansbury and Shade is still flagged book-wide.

**The reviser's leans (R36), for the author to overrule:**

1. **The museum staging stays as written (W18).** Shade waits by his car, he slips and grabs her arm, and "I don't need to be rescued" answers an argument. His August refinements had Shade wandering inside, a small open-handed step, and Pathwell's body-block.
2. **The road accusation is back.**
3. **The graffiti-house speech is Pathwell's.** In his draft it's Shade's, but here Shade isn't the one pitching her.
4. **The cannon points at the gift shop** (six places use the joke), not the front door as in his draft.
5. **The poem is planted and then left on the wall.**
6. **"For the record, I hate you both." is not used.** "Both" would blame Shade for a blast that's Pathwell's.

**New lines that aren't his (plain, flagged):**

- "That's from my library. You took that while I was upstairs."
- "Find the healer before you do anything else."
- "Side cases stood around the gallery, the museum's best things kept close to its oldest one."
- Stansbury looking at the poem.
- "a quartermaster's rather than a battlefield's".

## P37, 2026-10-05: Chapter 12, Camp and the diary

**Goal:** a line pass. The author's working draft stops at the museum, so nothing in this chapter is his. Every line is the August text as P4 revised it, and that makes item 6 (who wrote what) the whole chapter. The reader ran with all three passes ([report](Reader-Reports/2026-10-05_Ch12_reader.md): no stoppers, seven snags, seventeen quibbles). The fresh check ran against the previous version ([report](Reader-Reports/2026-10-05_Ch12_fresh.md)) and found no misattribution in the merged beats; one slip was caught by me first. Their fixes are applied.

**What changed, from the diff** (Ch12 2,440 → about 2,250 words):

- **Tone (R24, Craft rule 4).**
  - Cut: a stranger "put a piece of bread beside Elizabeth without breaking off her conversation", the kind of offstage kindness the author cut in Ch2.
  - Shown instead, from a person the story follows: "Mama Baga came out with a blanket and left it folded beside Elizabeth without a word." The last line now says "Mama Baga's blanket" rather than reporting it. That also pays ledger R17 (her care, shown in ordinary things).
  - Kept: Mama Baga's "mouth moved at one corner" before "Drink.". Ledger R17 and the Registry hold it as a possible family tell for the author, and P4 restored it for that reason.
- **Knowledge.** Shade's "Stansbury has infected you" answered "I have standards", a line from Ch10 that neither he nor Elizabeth heard. Cut, with the two lines that led to it ("You have one functioning arm and are becoming reckless with it.").
- **Staging.** After the sling, the healer "eased Elizabeth's coat back over it" (the diary rides in that coat pocket later).
- **The diary (one sad thing, said once):**
  - Cut: the museum retelling ("At the museum she'd watched letters survive a war…"); "The diary felt heavier because she knew where she was taking it."; "That still hurt." on the cookbook card; "That question was harder."; "The diary belonged to Camp now. The life in its pages was still hers."; and the closing list of "two pieces of her life".
  - Kept: the lock's reason, "something larger than herself" (08-21 §2), carried by "The diary wasn't important the way Daniel Vale's letters were important…" / "That wasn't the same as saying it was nothing."; and the rhyme with Ch4, "with both hands, the way Mama Baga had taken the cookbook".
- **Cut (commentary and narrator jokes):**
  - "This seemed to require active effort."
  - "It was terrible. / That, at least, felt normal." (Plan row 12)
  - "Shade obeyed. The simplicity of it seemed to annoy him. Elizabeth approved."
  - "For a second Elizabeth thought he might smile. He didn't."
  - "because somebody had apparently explained physics to him"
  - "He nodded as if mostly were a medically useful category."
  - "Instead: what do you need?"
  - "Elizabeth understood."
  - "For the first time since the museum, nothing required an immediate answer." (a fifth "for the first time" closer)
  - "No glowing paper, no borrowed memory, no page disappearing." became "There was no paper in it anywhere".
- **"Good." and "All right".**
  - The healer's closing "Good." became a nod.
  - Shade's first "All right." is cut. His second, when she goes to the archive, stays as the real one, after the chapter where Pathwell broke the word.
- **Rhythm:** 49 one-line action beats merged into the dialogue they introduce; short paragraphs went from 48% to about 33%. One merge put the healer's "That?" after Elizabeth's beat; it's separated and tagged. "Hand," is tagged to Shade.
- **Records:** Registry rows 75, 94, 97 and 116; Plan row 12; the status table.

**Kept, as leans (R36):**

1. **"ONE PAGE USED — CHICKEN & DUMPLINGS" on the card** stays. The reader noted that Ch4 counts two missing places; P23 weighed this and kept the card, and Ch15 repeats it.
2. **The dagger** isn't mentioned (ledger O4 tracks it as unpaid). Adding a beat here would only be bookkeeping.
3. **The archive's dry run** ("museums were a recognized injury category", "Is that also a category?", "He respects paperwork more consistently than people.") stays, as the archivist's register (R33: "the archivist stays the one dry wit"). "That's bleak." is contracted.

**New lines, plain, flagged:**

- "There was no paper in it anywhere"
- "She eased Elizabeth's coat back over it."
- "Mama Baga came out with a blanket and left it folded beside Elizabeth without a word."
- "The healer nodded."
- "Shade washed it."

**For the author:** this chapter has no line of his. The emotional lines around the diary are listed here for his eye:

- "There was still time to choose that. A loan meant it stayed hers in a different building…"
- "That wasn't the same as saying it was nothing."
- "The book belonged here now, and it no longer felt like a disappearance."
- "Don't let Pathwell decide the restriction expired."

**The routine (D23):**

| Step | P37 |
| --- | --- |
| 1 Sunday tone guardrails | done (reader item 1; the offstage kindness replaced by Mama Baga's) |
| 2 Shapes in the Registry | done (rows 75, 94, 97, 116) |
| 3 Checker | done |
| 4 Scene diagnostic | done (reader item 2: holds) |
| 5 Fresh check | done |
| 6 Reader protocol, with the tone and rules check | done |
| 7 Replacement tic | done (fresh check: the merges created a "[Name] considered / understood / thought about it." shape six times; three are cut) |
| 8 Deliberate ambiguity | left alone |
| 9 Change notes from the diff | done (above) |
| Tenth seat | not triggered (line edits; the triage's "needs one word" had a finding and was fixed in P10) |
| Light Sunday touch | done: Mama Baga's blanket, shown |

**Not re-run:** the reader and the fresh check on their own fixes.
