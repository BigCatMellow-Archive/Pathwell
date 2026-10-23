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

## P38, 2026-10-05: Chapter 13, Shade at Camp

**Goal:** Plan row 13. Tighten the middle vignettes so each one changes something, keep the Hearts shift, vary the opening, and deal with Shade's procedural jokes (B7). The author's draft stops at the museum, so every line here is the August text. **This pass ran in two sittings.** An earlier run this morning wrote the decisions (K1–K5), ran a tenth seat on them (**YELLOW**) and made the first round of cuts, but was interrupted before it committed or reported. This afternoon's run picked up the working copy. It ran a second tenth seat on the triage's settled verdict, "Chapter 13 needs nothing" (trigger 2: **ORANGE**), and ran the reader with all three passes ([report](Reader-Reports/2026-10-05_Ch13_reader.md): no stoppers, five snags, 24 quibbles) and the fresh check ([report](Reader-Reports/2026-10-05_Ch13_fresh.md)). Both tenth seats are in [one file](Tenth-Seat/2026-10-05_Ch13-decisions.md). The change notes below are from the diff against the last commit (P37).

**What changed, from the diff** (2,520 → 2,195 words; short paragraphs 57% → 38%; checker commentary paragraphs 10 → 1):

- **The opening (K3).** It was the third personified opener in a row ("Camp Cunnan had decided Shade was neither an emergency nor an explanation."). Now it opens on people: Elizabeth by the fire, and Mama Baga pinching the museum glass out of Shade's sleeve. Ch12's blanket isn't repeated.
- **The middle (K2).** Each vignette now changes something:
  - The jacket: he gives up the coat.
  - The coffee: he learns the Space Between memory isn't his ("Then I don't remember it.").
  - Hearts: Milo's name, "I know the rules." / "I don't remember playing." / "Then today you play.", one queen-of-spades trap, and the shift from playing remembered rules to playing the people.
  - The queen and "Pockets": what he likes.
  - The onions: "You want to leave?" / "I want to stay here." / "Then stay." / "Asking."
  - The last hand.
  - **Cut:** the potato crate (one of nine "right hand opens" beats), the second trap, "They bounce." / "Good system.", the purple-foot set-up's extra lines, and the "chain of custody" queen return.
  - **Kept for later chapters:** "I know Hearts." (Ch17), the queen going back into the deck (Ch14), "by fewer points" (Ch17), "Corruption." (Ch15).
- **Shade's procedural jokes (B7).** Cut: "Laughing seems medically irresponsible.", "This camp communicates like a hostage situation.", "That seems deliberately dangerous.", "Chain of custody has already been compromised.", "That is inconvenient.". The kept ones are listed below for the author.
- **Q82, placed** (ledger L16). Shade's "holding onto" reading, in the lock's own example wording: "He keeps acting like you're something he can hold onto." / Elizabeth, remembering the museum lot ("You took her from me."): "I know." It's plain and flagged. It's his own inference from what he saw in Ch11, with no telepathy.
- **Staging (reader):**
  - The grinder goes into Shade's hands, not his lap (he's standing).
  - He works it with his bandaged left hand (Ch11–12 never said which palm; this pass picks the left).
  - The cards don't slide from a hand that's already over.
  - In the last hand his left jerks with the right, so the cards he's holding scatter.
  - "Are you one?" replaces "I thought you weren't a guest." (nobody had said he wasn't).
  - The archivist's "He's just better than you" is tagged.
  - "Shade stood with the grinder" replaces an ambiguous "He".
- **Narrator commentary and restraint notes cut:**
  - "Elizabeth was getting better at that distinction."
  - "That, apparently, settled it."
  - "No philosophy followed."
  - "This seemed to make him happier than winning might have."
  - "No hesitation."
  - "No follow-up inspection…"
  - "That was becoming one of the easiest ways to tell them apart."
  - "Not certainty. / Not distance. / An inference from pressure."
  - "He was losing the fight with the draw by inches."
  - "it wasn't Pathwell's smile" (Ch9 owns his first own smile)
  - "Elizabeth let him have it."
  - "The phrase came automatically."
  - "and he didn't fill the silence"
  - "His face had gone tight."
  - "That's unfortunate."
  - "He swallowed."
  - a third blanket-adjust
  - the pre-announcing "while his right hand opened and closed against his knee"
  - the fiddle clause (its fourth use across Ch12–14, now "a dog asleep under the cooking wagon")
- **Fragment runs merged** throughout. "That's a terrible answer." is contracted (Elizabeth contracts; Shade doesn't). "For the first time, Elizabeth had a name for him." → "Elizabeth finally had a name for him."
- **Records:** W19; ledger L16 and L17; Registry rows 76 and 96; Plan row 13; the status table.

**The tenth seat on the triage (ORANGE) and how it was answered:**

- **13.1, no tree-line conversation.** The locks keep one: Q79, LOCKED C+A hybrid, which rejects "no advance discussion"; C15; C2 §11. The triage's test ("nothing later cites an earlier talk") tested the wrong thing. **Answered by W19:** kept out for now and put to the author, with Q82 placed here and C1 §6 left open as ledger L17.
  - The seat also offered one marked prediction line as a trial. Not taken: Ch14's reveal reads as the reveal, and a prediction here would spend part of it. That's a lean, listed below.
- **13.2, Milo a boy.** GREEN. Q-M stays open (R32: "idk"). The record's reason is corrected: the "girl" was the author's own Ch4 draft, not "a discarded draft", and a swap would be a rename plus pronouns.
- **The contract's exit clause** (Shade "does not consent to reintegration"): "I want to stay here." carries it implicitly. Listed for the author.

**Kept against the checks, as leans (R36):**

1. **No tree-line conversation** (W19).
2. **"He got the onion anyway."** It's his will against the draw, not a button.
3. **Shade's two "Good."s on his own coffee.** One deliberate rhyme.
4. **The older woman stays unnamed.** She's silent, and she's the one who wins.
5. **"since before any of them were a logistical concern"** stays.

**For the author:**

- **W19,** and three questions the tenth seat says only he can settle:
  - Should Shade predict Pathwell's attempt before the fire?
  - Is the "holding onto" line wanted?
  - Should Elizabeth say "I'm going to be there when he decides"?
- **Milo or the girl** (Q-M).
- **Which palm** is Shade's bandaged one (this pass says left).
- **Shade's kept jokes:** "This child is cheating.", "Evidence." / "Corruption." / "Exactly. No one suspects him.", "This place is hostile.", "I can choose badly.", "My face is adjusting.", "You have already suffered enough.", "I've been told worse.", "That hand was promising.".
- **Mama Baga's** "That one belonged to a man with unfortunate arms."

**New lines, plain, flagged:**

- "He worked the grinder with his bandaged left hand, because the right one couldn't be trusted to stay on the handle."
- "He keeps acting like you're something he can hold onto." / "Elizabeth thought of the parking lot at the museum. 'I know.'"
- "Are you one?"
- "a dog asleep under the cooking wagon"
- "His left jerked with it"

**Carried to later passes:** Ch15:1118 says "Milo saying he was cheating", but in Ch13 it's Shade who says it (the Ch15 pass).

**The routine (D23):**

| Step | P38 |
| --- | --- |
| 1 Sunday tone guardrails | done (reader item 1: holds; every brace lands within a few lines) |
| 2 Shapes in the Registry | done (rows 76, 96) |
| 3 Checker | done |
| 4 Scene diagnostic | done (reader item 2: holds) |
| 5 Fresh check | done |
| 6 Reader protocol, with the tone and rules check | done |
| 7 Replacement tic | done (gaze is still about 17 per 1,000 here; about a dozen looks cut over both sittings; carried book-wide) |
| 8 Deliberate ambiguity | left alone |
| 9 Change notes from the diff | done (above, against P37) |
| Tenth seat | done twice (YELLOW on the decisions; ORANGE on the triage, answered by W19) |
| Light Sunday touch | checked; none needed (the book's warmest chapter) |

**Not re-run:** the reader and the fresh check on their own fixes.

## P39, 2026-10-05: Chapter 14, the confrontation

**Goal:** Plan row 14 and the climax (Q-E), under **R37** ("You decide and then go on to 14."). The author's draft stops at the museum, so every line here is the August text. The decisions were written before drafting (M1–M5) and the tenth seat ran on them ([file](Tenth-Seat/2026-10-05_Ch14-decisions.md): **ORANGE** overall; M1 ORANGE, M2, M3 and M5 YELLOW, M4 GREEN). The reader ran all three passes, including the tone and rules check ([report](Reader-Reports/2026-10-05_Ch14_reader.md): no stoppers, 12 snags, 24 quibbles; Pass 3 two holds, six mild breaks, two of them records only). The fresh check ran against the pre-pass text ([report](Reader-Reports/2026-10-05_Ch14_fresh.md)). The change notes below are from the diff against the last commit (P38).

**What changed, from the diff** (3,463 → 3,247 words; paragraphs 618 → 308; short paragraphs 50% → 32%; checker commentary paragraphs 17 → 2; filter verbs 10 → 4):

- **The climax decision (Q-E).** Decided as **option 2 with 3b**. Option 1 (her "Let it fail" makes him take his hands off) was the first choice and was **dropped after the tenth seat**: on the page Shade is already not folded in (the frame collapses toward Pathwell with his hands on the loop), so the beat could change nothing without inventing a rule at the climax, and his letting go would soften Ch16 ("chose not to stop") and Ch18's lift. Her line stays unheeded; "He does it anyway" stands. Option 2 is the Ch15 pass. R37, Q-E and the Plan's climax section are corrected to say so.
- **3b, the dagger** (ledger O4, paid by refusal). Planted after "Your occupation is causing paperwork." ("Elizabeth felt the foam dagger at the back of her waistband and didn't mention it."). When the draw goes rigid, her hand goes to it and stays, with the reason on the page: she doesn't know what it would cut, "or whose it was to cut." The tenth seat's caution is kept: Shade doesn't shake his head at her; the choice to leave it is hers.
- **C1 §6, placed** (ledger L17). After "I am the person living with it," Shade looks at her: "You don't have to stay for this." / "I'm going to be there when he decides." Only the lock's second sentence is used; the first ("I'm not going to tell him what to do") would be false a page later.
- **Continuity.** "I can hold it." → "I can contain it.", so "That's what you said at the museum." is true (Ch11: "I can contain this."). The fiddle stopping is cut. *Correction to M4 and P38:* this was not the fiddle's "fourth use across Ch12–14"; P38 had already cut Ch13's, so Ch14's was the second remaining, and only Ch12:132 is left in Ch12–14. Ch16 keeps the fiddle as Camp's pulse.
- **The "Not X. / Y." runs and commentary.** Every run in the M5 list is merged or cut. Gone, among others: "Not louder. / Less casual.", "Not permission. / Not surrender.", "Not fear. / Recognition.", "Not toward Shade. / Not toward Elizabeth." (kept as one clause: "not toward Shade or Elizabeth, but toward the practitioner…"), "That was the problem with Pathwell…", "The answer unsettled her more than one would have.", "That helped him. Elizabeth understood that only later.", "It was not an apology…", "Elizabeth had never heard the word sound so merciful.", "There it was.", "It wasn't permission.". About 87 short beats were merged into the lines they belong to; every merge was checked for its speaker.
- **Speakers (the merge script misattributed three; all fixed):** "Am I wrong?" is separated again; "You are not paying for this." is Stansbury's, in one paragraph with his "No."; "Lift it. Let the frame fall. Nothing has released yet." is Mama Baga's. Also tagged: "Do not release payment," Mama Baga said.
- **The reader's snags:**
  - "a little finger" (it landed on Mama Baga).
  - The dagger plant moved after "So do I." / "Your occupation…", so "So do I." is Pathwell's.
  - "That helped him…" cut (it gave the reveal away; Q147 wants recognition after, not a signpost).
  - The cards change hands once: "The archivist turned to him." / "Milo took the deck".
  - Mama Baga's diagnosis: "But you are also trying to keep him separate."; "And you no longer believe you have the right…" and "Pathwell's face went very still." are cut (she reads behaviour, not his conscience, Q126b).
  - "Nothing is acceptable," cut; "Nothing changing is acceptable to me." stays.
  - The archive look is now Elizabeth's knowledge: he looks past Mama Baga at the open door, and "Elizabeth knew what was on those shelves…". He wasn't at Camp when the diary was given.
  - The lantern: "still lit from the night".
  - The queen: the archivist lays it on the card table, where Ch15 finds it.
  - "might be both" → "might be a binding, and might be him."
  - "the older woman in the knitted cap", as in Ch13 ("the old woman" is Mama Baga in Ch4).
  - "Nobody at the table moved".
- **Tics trimmed:** "Pathwell did not move.", "Mama Baga didn't move.", "He wasn't resisting;", "Shade clenched his jaw.", "Pathwell's jaw tightened.", a bare "Pathwell looked at him.", and Pathwell's "mouth moved at one corner" (the stock gesture). Shade's second "Apparently." is now "It seems so."
- **Ch16, one fix carried here:** "the empty place at her hip" → "the empty coat pocket" (the diary was in her coat pocket, Ch12).
- **Records:** R37 and Q-E corrected; Plan row 14 and the climax section; ledger O4 and L17; Registry row 14; the status table.

**The tenth seat and how it was answered:**

- **M1, ORANGE:** dropped (above).
- **M2, YELLOW:** kept, with its reason on the page and no headshake from Shade.
- **M3, YELLOW:** kept. The seat's two conditions: pace (Q145) — the exchange is two lines; and the stance being broken three times ("Then put it away", "Don't.", "Let it fail"). Answered as a lean: it's a stance she keeps failing at, which is human, and the lock allows her to challenge a dodge.
- **M4, GREEN:** done, with the fiddle count corrected.
- **M5, YELLOW:** done. The seat's warning about "Not toward Shade." is kept by folding it into one clause, not cutting it.

**Kept against the checks, as leans (R36):**

1. **No soft landing inside Ch14** after the fall (reader Pass 3 item 1). It's a cliffhanger; the landing is in Ch15–16. The reader's bucket-line beat is not added.
2. **The archivist's "Milo?"** stays (reader snag 11). He goes white because he sent the boy in himself; "Milo?" is him calling into the smoke.
3. **Elizabeth's stance and her "Don't." / "Let it fail"** (above, M3).
4. **The narration's in-sentence negations** (reader item 5: the "Not X." fragments were replaced by "didn't / did not" inside sentences). Some cut here; the rest carried to the book-wide tic pass.
5. **The threshold opening onto the card table** (Ch13 put the seam between two trees). A mouth opens where he is; not changed.

**For the author:**

- **R37 as read:** option 2 with 3b, option 1 dropped. If you wanted her words to stop him, that needs a new rule at the climax (holding the loop would endanger Shade), and the tenth seat advises against it.
- **C1 §6:** only the second sentence of the lock is used. The first ("I'm not going to tell him what to do") would be broken a page later.
- **The dagger reason:** "She didn't know what it would cut, or whose it was to cut." Plain, flagged.

**New lines, plain, flagged:**

- "Elizabeth felt the foam dagger at the back of her waistband and didn't mention it."
- The dagger paragraph: "Elizabeth's hand went to the foam dagger at the back of her waistband. Stansbury had made it to cut things that don't separate easily, and had said it was designed not to cut people. Whatever held Shade's arm out now might be a binding, and might be him. She didn't know what it would cut, or whose it was to cut. She left it where it was."
- "You don't have to stay for this." / "I'm going to be there when he decides." (the second is the lock's)
- "But you are also trying to keep him separate."
- "Elizabeth knew what was on those shelves:"
- "still lit from the night"
- "He laid it on the card table."
- "It seems so."

**Carried to later passes:** Ch15: option 2 (Shade's locked reason set off by what she carries out of the fire); Ch15:1118 "Milo saying he was cheating" (it was Shade); Ch15's leftover "Not X." fragments; "the failed brass frame" (Ch15:543; one name for the frame). Book-wide: in-sentence negations and restraint notes, gaze rate, "the back of her waistband" (six chapters).

**The routine (D23):**

| Step | P39 |
| --- | --- |
| 1 Sunday tone guardrails | done (reader item 1: mild break, no soft landing after the fall; lean 1) |
| 2 Shapes in the Registry | done (row 14) |
| 3 Checker | done (numbers above) |
| 4 Scene diagnostic | done (reader item 2: holds) |
| 5 Fresh check | done |
| 6 Reader protocol, with the tone and rules check | done (2 holds, 6 mild breaks; answered above) |
| 7 Replacement tic | done (in-sentence negations and restraint notes rose as the fragments went; some cut, the rest carried book-wide) |
| 8 Deliberate ambiguity | left alone (whether Shade could have been folded in stays unasked) |
| 9 Change notes from the diff | done (above, against P38) |
| Tenth seat | done (ORANGE; M1 dropped) |
| Light Sunday touch | checked; none inside the cliffhanger (lean 1) |

**Not re-run:** the reader and the fresh check on their own fixes.

## P40, 2026-10-06: Chapter 15, the fire

**Goal:** Plan row 15 and option 2 of the climax (R37): show Shade's locked reason before he walks, cut the explanatory close, and cut the "Not…" cadence. The author's draft stops at the museum, so every line here is the August text. **This pass ran in two sittings.** A run last night wrote the decisions (N1–N6), ran a tenth seat on them ([file](Tenth-Seat/2026-10-05_Ch15-decisions.md): **ORANGE**; N1 ORANGE, N2–N5 YELLOW, N6 GREEN) and drafted most of the chapter to its conditions, but was interrupted before it ran the checks or committed. This morning's run picked up the working copy, ran the reader with all three passes ([report](Reader-Reports/2026-10-06_Ch15_reader.md): 2 stoppers, 16 snags, 17 quibbles; Pass 3 one hold, six mild breaks, one unconfirmable until this entry) and the fresh check ([report](Reader-Reports/2026-10-06_Ch15_fresh.md)), and ran a second tenth seat on two changes made after the reader ([file](Tenth-Seat/2026-10-06_Ch15-after-reader.md): **YELLOW**). The change notes below are from the diff against the last commit (P39).

**What changed, from the diff** (3,328 → 3,271 words; paragraphs 569 → 294; short paragraphs 49% → 35%; "Not…/No…" paragraph openers 28 → 4; checker commentary paragraphs 24 → 7):

- **Shade's reason (option 2; ledger R14, now paid).** As the blob advances, the hurt people move back past him: Stansbury with his hand in the healer's wet cloth, the archivist drawing Milo back "one bare foot dragging in the dirt". "Shade watched them go. Then he looked at Elizabeth's left arm, hanging out of what was left of the sling." / "I told Pathwell to leave it unresolved," he said. "I thought I'd be the one carrying it." Then the informed risk, as before: "I'd like to find out which problem it thinks is biggest." (Q132; it was "A way to learn…"). It's one line in his own register, with no "person", "fault" or "mistake" (C30), and nothing that cues Pathwell's "Will you stay?". Shade's whereabouts during the rescue are given ("about as far toward the archive as the draw had let him come").
- **What option 2 does not do (tenth seat N1).** Take her rescue away and the fire, the burned Stansbury, the hurt child and the blob are all still in front of him; only the images change. So it is **not** recorded as meeting the 2026-09-18 rule, and nor is 3b. R37, Q-E, the Plan and ledger R14 now say so, and the rule is put to the author.
- **The explanatory close is cut** ("Shade had taken a risk because… Like everyone else."). The memory list ends on "That hand was promising.", then the roof, the empty ground and the last three lines, unchanged. The blob's departure no longer reads as clearing waste that included Shade: "The ambiguous signal… was gone with Shade. The blob found nothing else it recognized as unclaimed waste" → "found nothing left that it had come for".
- **The death, reordered to lock C29** (eye contact → draw quiet → relief → absorption; the second tenth seat, D1, YELLOW). Now: "Shade looked at Pathwell, and Pathwell was looking back." / "Then the blob took his chest, and the draw went quiet." / Pathwell falls sideways / "Shade's right hand was still open toward him. Shade closed it himself." / the surface passes over him. Before, the draw vanished only after he was gone. This overrides triage 15.6, which kept the old order without checking C29; nothing in Ch16–18 depends on the order. "Not because Pathwell made it." is gone, because it is now false.
- **The dagger in Ch15** (reader stopper S1; ledger O4). When the blob turns after Shade: "Her hand had found the foam dagger at her back. She had used it on one of these before. This one was coming for him because he had let it, and it wasn't hers to cut. She kept her hand where it was and said nothing." The first version sat inside the death sequence and said he had "walked into" it; the second tenth seat moved it out and asked for the verb to carry his informed choice and for no claim that it would have freed him.
- **The books (N3).** The diary pause stays, at one beat ("Elizabeth stopped, for less than a second."), with the checking motion; "That decided it." and the cookbook weighing ("She could take it. / Right hand, one motion.") are cut; "The fire had not reached it yet. The shelf was close enough to touch." and "She didn't stop." on the way out stay. **The pause departs from C2 §7a and §8** ("does not stop", "does not slow down"); kept as a lean (R23) and put to the author.
- **Continuity:**
  - "Milo saying he was cheating" → "Shade calling Milo a cheat" (Ch13; Ch16's "Did you actually catch him cheating?" still works).
  - The queen lies "on the card table where the archivist had left it" (Ch14); the onion placement is gone.
  - Stansbury's rescued letters are "a packet of family letters", no longer "that had sat beside the cookbook" (the cookbook burns on that shelf; C2 §10b).
  - The boxes: he lets go of both when the canvas falls, brings away "the box that hadn't stuck", and "One archive box" sits by the notebook (Ch16: "One flat box").
  - "Stansbury came back out through the side window" (it had already been smashed; it no longer "exploded outward").
  - "the brass frame" / "the frame" for the failed working.
- **The reader's snags:** "Can you stand?" he asked (Milo's); the strut staging ("under the strut as a fulcrum and braced her shoulder against the shelf"); "Think." / "Yes." → "You think." / "It's the best I have."; "That is new. I'm not." → "That is new. Whatever it's been following all night isn't." (it could have read as "my existence is the mistake"); Elizabeth's "Different category." → "Worse. Mine." (it doubled Stansbury's "Different problem."); "She didn't regret the order." keeps its first sentence only; "Her right hand found the edge. She pulled. Nothing moved."; Shade's last look: "He wasn't asking for anything, or forgiving anything. He just looked." (keeps the not-absolution content).
- **Narrator commentary and "Not…" runs cut.** The old text of every cut narrator line is listed for the author in the [fresh check](Reader-Reports/2026-10-06_Ch15_fresh.md), section 2, N4 item 8. Among them: "That was not bravery. / It was distance." (now "She had already been moving when Milo shouted the second time."), the three "That mattered.", "That was also a choice.", "That distinction was the entire world…" (kept as "for the next several seconds that difference was the entire world"), "Not fast. / Decisively.", "No glow. / No magical consumption.", "No coat. / No card. / No useful relic.", "The correction landed even here.", "There was almost humor in it.", "The answer seemed to satisfy him more than certainty would have.", "It was getting easier to say.", "She ignored that.", "Elizabeth hated that too." / "The silence inside him was visible.", and "Different mess. Different consequence.". The stock gesture "Shade's mouth moved at one corner." is gone.
- **Records:** R37 and Q-E corrected; Plan row 15, the option 2 row and the climax section; ledger P8, O4, R12, R14; triage 15.1, 15.3–15.6; Registry row 15; the status table.

**The tenth seats and how they were answered:**

- **N1 (ORANGE):** narrowed to the look and one line; recorded as showing the motive, not meeting the rule. All seven conditions (a–g) met; the fresh check confirms.
- **N2 (YELLOW):** close cut; one line of reason is on the page; no meaning-sentence added back; the blob-eye line fixed; triage 15.4 and ledger R14 updated.
- **N3 (YELLOW):** the pause kept at one beat and recorded as a departure; "The fire had not reached it yet." and "She didn't stop." kept; the checking motion unchanged.
- **N4 (YELLOW):** the content of items 1–6 kept in sentences (the effort "too small for the moment, and still real"; not asking, not forgiving; his own hand; the blob not punishing Pathwell; pinned without crushing; the blob's assessing and turn); the opener corrected; the old text listed.
- **N5 (YELLOW):** done, with the queen at the Ch14 placement. The frame name across Ch16 is for the Ch16 pass.
- **N6 (GREEN):** "You can ask." and "Will you stay?" untouched. *Correction:* N6 cited a lock for "Shade closed it himself"; there is none (the locks are Q131 and C30), and 15.6's order was not GREEN against C29.
- **Second seat D1 (YELLOW):** done (the hand still open when the draw quiets; both men looking; the blob the cause). **D2 (YELLOW):** done (moved, verb fixed, no counterfactual, kept silent), flagged.

**Kept against the checks, as leans (R36):**

1. **The diary pause** (one beat) against C2 §7a/§8.
2. **"The answer came out in Shade's voice and Pathwell's voice and her own."** (reader snag 7). It notices the book's shared "I know." on purpose, once.
3. **"A person could accumulate a surprising amount of life in a morning."** and **"Shade had never been particularly interested in deserving scenes."** (reader snags 8 and 9). Both were on the decisions' keep list; they are the narrator's grief, said once each.
4. **"For once, the world didn't reorder itself around the fact that Pathwell had fallen down."** and **"Not everything. Something."** stay. The first is mid-chapter, not a closing turn.
5. **"No spell. / No sacrifice. / No last message. / Just fire."** stays: the cold reader's line, and the one place the climax keeps the fragment cadence.
6. **No soft beat after the death** (reader Pass 3 item 1; the biscuit for Milo not added). Ch16 opens on Camp carrying on.
7. **Stansbury's letters may still read as the Ch12 packet** beside the cookbook; only the explicit claim is cut.

**For the author:**

- **The 2026-09-18 rule** ("her final choice materially alters the central conflict"): not met by option 2 or 3b. If you want it met, the only option that changes the outcome is 3 (the dagger used), which the Plan says risks making her the solver. Default: not met; the book goes on.
- **The diary pause** against C2 §8.
- **C29:** both men now look when the quiet comes; the draw goes quiet before he's gone. If you preferred the old order (the draw vanishing after), say so.
- **The dagger in Ch15**, or leave it silent with Ch14 carrying it.
- **Shade's line:** "I told Pathwell to leave it unresolved. I thought I'd be the one carrying it."

**New lines, plain, flagged:**

- "about as far toward the archive as the draw had let him come"
- "Shade watched them go. Then he looked at Elizabeth's left arm, hanging out of what was left of the sling."
- "I told Pathwell to leave it unresolved," he said. "I thought I'd be the one carrying it."
- "It's the best I have."
- "That is new. Whatever it's been following all night isn't."
- "Your theories have had a bad morning."
- "Worse. Mine."
- The dagger paragraph (above).
- "Shade looked at Pathwell, and Pathwell was looking back." / "Then the blob took his chest, and the draw went quiet." / "Shade's right hand was still open toward him."
- "found nothing left that it had come for"
- "Shade calling Milo a cheat"

**Carried to later passes:** Ch16: the frame name ("failed brass frame", Ch16:454), the 19 "Not/No" openers (the rhythm will change at the chapter boundary), where the dagger goes. Book-wide: in-sentence negations and restraint notes ("didn't <verb>" rose as the fragments went), ", and" joins and colon-lists (the fresh check's replacement-tic count), look-beat openers, the shared "I know.".

**The routine (D23):**

| Step | P40 |
| --- | --- |
| 1 Sunday tone guardrails | done (reader item 1: mild break, no soft place after the death; lean 6) |
| 2 Shapes in the Registry | done (row 15) |
| 3 Checker | done (numbers above) |
| 4 Scene diagnostic | done (reader item 2: holds) |
| 5 Fresh check | done |
| 6 Reader protocol, with the tone and rules check | done (1 hold, 6 mild breaks, 1 unconfirmable before this entry; answered above) |
| 7 Replacement tic | done (fragments replaced by in-sentence negations, ", and" joins and colon-lists; some cut, the rest carried book-wide) |
| 8 Deliberate ambiguity | left alone (whether Shade expected to die; whether the quiet felt like being seen, C29) |
| 9 Change notes from the diff | done (above, against P39) |
| Tenth seat | done twice (ORANGE on the decisions; YELLOW on the two post-reader changes) |
| Light Sunday touch | checked; none added after the death (lean 6); Milo's "You still owe me a hand" and "I was winning" carry it |

**Not re-run:** the reader and the fresh check on their own fixes.

## P41, 2026-10-06: Chapter 16, aftermath

**Goal:** Plan row 16: the hearing's numbered rules, the narration grading Pathwell (the cold reader: "I felt managed"), the thesis opener, and the line items (body-deciding, "That ended the conversation for now. Nothing more."). The author's draft stops at the museum, so every line here is the August text. The decisions were written before drafting (M1–M6) and the tenth seat ran on them ([file](Tenth-Seat/2026-10-06_Ch16-decisions.md): **YELLOW** overall; M1–M5 YELLOW, M6 GREEN). The reader ran all three passes ([report](Reader-Reports/2026-10-06_Ch16_reader.md): no stoppers, 11 snags, 12 quibbles; "the chapter now reads as people, not a ruling") and the fresh check ran against the pre-pass text ([report](Reader-Reports/2026-10-06_Ch16_fresh.md): every lock and callback intact, one seat condition not met, since fixed). The change notes below are from the diff against the last commit (P40).

**What changed, from the diff** (3,639 → 3,333 words; paragraphs 582 → 362; short paragraphs 49% → 35%; "Not…/No…" narration openers 19 → 1; uncontracted narration forms 33 → 3, all kept for weight; checker commentary paragraphs 30 → 4):

- **The hearing (M1).** Mama Baga's "First rule… / Second rule… / Third rule…" are gone as a list. The schedule line is her own sentence, right after "Then it isn't." (it keeps the debt open): "The person who broke the thing does not get to set the schedule because waiting makes him uncomfortable." "Second rule: no pruning shortcuts." is cut; the archivist's "You will not prune to buy any of it." (with Pathwell's eyes flicking up) carries it, and "Pruning?" / "No." in the scar scene. The hobby line stays solemn and standalone, tagged ("Mama Baga wasn't finished."), so Stansbury's "Cards." and Milo's shout still land and Ch17's Hearts still pays it. Kept: "Then stop naming impossible payment…", "Defined by whom?" / "Not me," the archivist's terms, "Don't become decorative.", and Elizabeth's "My shoulder is not a Camp expense." exchange.
- **The narration stops grading Pathwell (M2).** Cut: "That helped less than he probably hoped.", "That ended the conversation for now. Nothing more.", "That seemed to bother him more than anger would have.", "Elizabeth watched the hesitation.", "The silence did the work.", the narrator's "Good." (twice), "Nothing more." (the bandages), "The words were quiet. / No challenge in them. / No punishment either. / A boundary.", "That was all. / Elizabeth watched him stop. / It was not enough to repair anything. / It was still different.", "That, too, was visible.", "That answer hurt too. / It was supposed to.", "For once, empty did not look temporary.", and the "He did not explain… / Did not offer… / Did not reach for his coat." run. "Pathwell didn't add a because." stays (triage 16.1). Q134b's observer stays on the page ("Elizabeth noticed how strange that looked on him. Pathwell noticed her noticing, and looked away first."), and the three "reflex shown, then stopped" beats are untouched. The old text of every cut narrator line is in the [fresh check](Reader-Reports/2026-10-06_Ch16_fresh.md), section 7.
- **The opener (M3).** It was "The archive roof came down and Camp Cunnan kept moving. / That was the first thing Elizabeth understood about aftermath. / Nothing waited for meaning.", which retold the collapse Ch15 ends on. It now opens on Elizabeth: "Elizabeth was sitting in the dirt and didn't remember sitting down." (this also removes "her legs had stopped participating"), then Camp working around her. Stansbury's hand is unwrapped at "Stansbury was next" (Ch15 had the healer already wrapping it).
- **Stansbury's reasoning (M4; lock Q140c).** "The burn had happened because he chose to enter the archive. / The archive had burned because Pathwell chose not to stop. / Both things were true." entered Stansbury's head. It is now Elizabeth's: "Elizabeth thought of the side window. The burn had happened because Stansbury chose to go back in. The archive had burned because Pathwell chose not to stop. Both things were true." This overrides triage 16.3's KEEP in part (it kept the narrator report; the lock says Stansbury gets no interior), and keeps one balancing signal in the scene now that "No punishment either." is gone.
- **Line pass (M5):**
  - The healer's "Not broken, she thought." was in the healer's head; now "Not broken, she had said".
  - Body-deciding cut ("her body had decided it had been patient long enough").
  - "Not X. / Y." runs merged ("Not holding him down. / Just there.", "Not performatively.", "Not because it was funny.", "There it was. / Want. / Not owed… / Not required testimony.", the archive-at-night list, the fiddle, "Not elegantly. / No gradual cinematic tear.").
  - Watch patterns: Stansbury's "Fair." → "Noted." (Mama Baga's stays); "without asking permission" cut; three narrator "apparently"s gone; "the older woman in the knitted cap" here and in Ch17:583 (as Ch13–14).
  - The close: the "Tomorrow there would be more lists" run is one sentence, and the three "Nothing would make…" one sentence (Ch17 echoes "original" and "ash"); "The work would not become forgiveness… / Elizabeth understood that…" cut; the last line kept, uncontracted.
  - About 80 short beats merged into the dialogue they belong to. The script's list was checked line by line; six merges were refused because they would have given a line to the wrong speaker ("Two people moved." and "Someone answered." before Mama Baga's orders; "Slowly." before the healer's question; "Elizabeth waited." before Mama Baga's "He chose to stay here…"; and two others), and Mama Baga's repeated "Shade." is tagged to her.
- **After the reader and the fresh check:** "Not me," Pathwell said (re-tagged; it carries Q133c); "Rare morning for those," he said; "for approval" restored; "Mama Baga had said his name because someone had died" (it said "once", but she says it three times); three nod beats became tags; "The motion was part of the loss, not proof she had chosen wrong." and "For the fact that none of those losses balanced each other." cut.
- **Ch15, one line:** "For once, the world didn't reorder itself around the fact that Pathwell had fallen down." is cut. Ch16's last line says the same thing with more weight, and two "for once"s about Pathwell in two pages was one too many.
- **Records:** Plan row 16 and the dagger row; ledger O4 (left open on purpose after Ch15); triage 16.2 and 16.3; Registry row 16; the status table.

**The tenth seat and how it was answered:**

- **M1 (YELLOW):** done; the claim narrowed to "removes Mama Baga's three rules" (the archivist's terms and Pathwell's acceptances stay); the hobby line standalone; triage 16.2 noted.
- **M2 (YELLOW):** done; Q134b's observer kept; the reflex beats kept; one balancing signal kept (see M4); "Better." is said twice (the healer, Mama Baga), both kept.
- **M3 (YELLOW):** done; Elizabeth seated in the first line; the Stansbury join fixed.
- **M4 (YELLOW):** answered differently from the decision: "Both things were true." is kept and the reasoning moved into Elizabeth, which meets Q140c and the seat's balancing condition. The question of who holds that thought is put to the author.
- **M5 (YELLOW):** done; the lines the seat named ("He did not say Lizzy.", "yellow archive light", "Those circumstances were not available.", the museum/"original"/"ash") are kept.
- **M6 (GREEN):** the dagger left open; ledger and Plan updated.

**Kept against the checks, as leans (R36):**

1. **The bare apology on day one** (reader snag 1: C27, Q93, Q134c). It is short, he asks for nothing, and she refuses to say she forgives; the coda's offhand admission is a different act (triage 16.1).
2. **"Both things were true."** (reader snag 4: it echoes Milo's "Both can be true."). The echo is the point: the same arithmetic applied to a burn.
3. **"None of it would bring Shade back, or make the diary original again, or make Nana's cookbook anything but ash."** (reader snag 7). Ch17 calls back "original" and "ash".
4. **"The word kept arriving as if somebody had to keep delivering it."** (reader snag 9). It is the grief's voice, once.
5. **The last line** (reader snag 6) stays: "…for once Pathwell would not be the person deciding what those things were." It is the chapter's turn (Q133c); Ch15's "for once" is cut instead.
6. **"Mama Baga had said his name because someone had died, and names were one of the few things the fire hadn't managed to take."** It explains, but it is Camp's funeral in one sentence.
7. **"For the fact that choosing Milo had been right and had still cost her things she wanted back."** stays in the crying list.

**For the author:**

- **The apology on day one** (lean 1): keep it bare and refused, or move all of it later?
- **Stansbury's reasoning as Elizabeth's thought** (Q140c), or the narrator's as before?
- **The dagger:** left open after Ch15. Does it need a line in Ch17?
- **Does Pathwell hear Shade named and written down?** He is twenty feet away and the page doesn't say.

**New lines, plain, flagged:**

- "Elizabeth was sitting in the dirt and didn't remember sitting down." / "Around her, Camp worked."
- "The wrapping from the fire was off,"
- "Not broken, she had said:"
- "He walked slowly; his ribs wouldn't permit anything else."
- "Elizabeth thought of the side window."
- "Mama Baga wasn't finished."
- "Noted."
- "and a few people near her joined in"
- "There was no accusation in it, which made it easier and harder."

**Carried to later passes:** book-wide: look and nod beats at the front of dialogue paragraphs (the merge moved them there; Ch16 is "look*" 21.9 per 1,000 words against Ch15's 10.0), "didn't <verb>" lists, "looked away first" (twice in Ch16). Ch17: the dagger, if anywhere.

**The routine (D23):**

| Step | P41 |
| --- | --- |
| 1 Sunday tone guardrails | done (reader item 1: holds, with explaining sentences cut after) |
| 2 Shapes in the Registry | done (row 16, the new opener) |
| 3 Checker | done (numbers above) |
| 4 Scene diagnostic | done (reader item 2: holds; the tail trimmed) |
| 5 Fresh check | done |
| 6 Reader protocol, with the tone and rules check | done (no stoppers; Pass 3 answered above) |
| 7 Replacement tic | done (verdicts had moved into "didn't" lists, and look/nod beats moved to the front of dialogue; two lists and three nods cut, the rest carried book-wide) |
| 8 Deliberate ambiguity | left alone (whether Pathwell hears Shade named; what Mama Baga's "Person" settles) |
| 9 Change notes from the diff | done (above, against P40) |
| Tenth seat | done (YELLOW) |
| Light Sunday touch | checked; the chapter has it already (Milo's boot, "new hobby", the terrible coffee); none added |

**Not re-run:** the reader and the fresh check on their own fixes.

## P42, 2026-10-06: Chapter 17, three weeks

**Goal:** Plan row 17: compress the correction montage around the Henry Vale refusal, fix the museum section's viewpoint, add a line on how Elizabeth reaches Camp, and cut the closing summation. The author's draft stops at the museum, so every line here is the August text. **This pass ran in two sittings.** A run this morning wrote the decisions (K1–K6), ran a tenth seat on them ([file](Tenth-Seat/2026-10-06_Ch17-decisions.md): **YELLOW** overall; K3 **RED** as written), drafted the chapter to its conditions and ran the fresh check ([report](Reader-Reports/2026-10-06_Ch17_fresh.md)), but stopped before the reader ran or anything was committed. This afternoon's run applied the fresh check's fixes, ran the reader with all three passes ([report](Reader-Reports/2026-10-06_Ch17_reader.md): no stoppers, 7 snags, 16 quibbles), and applied most of those. The change notes below are from the diff against the last commit (P41).

**What changed, from the diff** (2,762 → 2,549 words; paragraphs 420 → 202; short paragraphs 45% → 29%; "Not…/No…" narration openers 16 → 2; checker commentary paragraphs 18 → 2; uncontracted narration forms 17 → 3):

- **The museum section in Elizabeth's view (K1; lock Q140; overrides triage 17.1).** It was told from inside the room with Pathwell ("The old answer was already assembled behind his teeth."), with Elizabeth arriving at the end. Now it opens on why she is there ("The current curator emailed Elizabeth directly. Pathwell hadn't asked her to come. The museum wanted a witness statement from someone who had been in the room and wasn't Pathwell."), and she sits at a side table writing it while the curator works through his stacks. The copies he has been supplying are in the curator's dialogue ("You've sent us scans, photographs and old catalog entries since." / "Every copy I could find." / "Useful," the curator said. "Not returned."). The temptation is shown, not narrated from inside: he says the old answer aloud ("Same family. Same period. Genuine originals. It is better than an empty—"), stops, looks at the empty case, says "No," and puts the packet back; "At the side table, Elizabeth's pen had stopped." Stansbury's "I have standing." now gets Elizabeth's "You were burned at a different incident." / "It's a series," Stansbury said. The narrow-socks memory is now "a man who had kept every pair of socks".
- **The montage compressed (K2).** Cut as repeats of the rack and the cabinets: the lavender boxes, the wrong wagon ("Other one."), the knot. The cabinets are one paragraph. Cut as the narrator grading: "No one applauded. / That was also useful.", "This surprised nobody but Pathwell.", "That helped.", "That was when Elizabeth began trusting it more.", "That mattered more than if he had said yes." ("She believed him." stays), "Not once. / Elizabeth noticed because she expected him to. / Then she noticed herself expecting him to. / That was information too." ("Pathwell never mentioned changing it again." stays), "Pathwell accepted both facts without trying to combine them. / Elizabeth saw that too.", "By the second week, Pathwell had been corrected often enough that correction stopped looking like a dramatic event." Kept: the rack, the cabinets, "Copy the smudge.", the board ("That hurt." / "Want me to say you're doing well?" / "No."), the Lemon with his asking (Ch18 calls back "Diseased lemon." and "I asked first."), Hearts, the reopening, the last placing. The old text of every cut narrator line is in the [fresh check](Reader-Reports/2026-10-06_Ch17_fresh.md), section 6.
- **One shared task (K2 condition c; Q134).** "Elizabeth stayed for lunch. Afterward the archivist put a stack of finished copies in front of her and the blue notebook beside it, and she checked them one-handed at the next table, line against line. In the third copy she found a place where Pathwell had quietly fixed somebody's spelling of Susquehanna." / He copies the page again, "mistake included." Whether this meets Q134's "working alongside" is put to the author; the record does not claim it.
- **How she reaches Camp (K3).** The decision's line ("through the Space Between and down the dirt road; the shopkeeper had stopped asking her business…") was **RED**: Ch18 has the shop greet her as new, and Q137 forbids an Elizabeth-only route. The line now says she is brought and names no route: "Getting there meant asking Pathwell to open the way." (Q137b allows him to open the threshold.) The fresh check's version cut "still" and "he did it without asking what she wanted there", which pre-echoed a Ch18 beat.
- **The close (K4).** Cut: "Three weeks had not fixed any of those sentences. / Three weeks had only made another sentence possible beside them:", "Evidence was enough for a next choice. / Not an obligation. / A choice.", and "For the first time since the crash," (Ch7 has the same turn). Kept: the list of what stays broken, "Pathwell had kept showing up when other people told him what needed doing.", "Elizabeth didn't call that redemption. She called it evidence.", and the motive-list ending, now the only one of its kind in the book's last chapters.
- **Continuity and line items (K5):**
  - Triage 17.5's "hip" is stale (Ch12 has the diary in her coat pocket "against her hip"); kept.
  - The route-copy box slides under the rack (17.6); "Pathwell looked at the box under the rack."; the label joke is on that box.
  - "2026" cut from the museum card ("ORIGINAL DESTROYED IN COLLECTION INCIDENT."); for the author.
  - "the original letters" restored; "The current curator" (Margaret Bell was the first).
  - The packet goes back into his coat, where it came from.
  - "Not X. / Y." runs merged; the narrator's "apparently" cut; one "Elizabeth could see" left (the Lemon); "while he felt bad" restored to the list of things nobody asked of her.
  - Speakers tagged where Elizabeth's presence made them ambiguous: the curator's "No." (with her unchanged face restored), "The curator waited.", "It's a series," "Continue writing," Stansbury said; "Pathwell looked at Stansbury. 'I regret bringing you.'"; "He was bad," Milo said.
  - A few look beats became tags. The reopening now has Elizabeth in it ("Elizabeth went to see the museum reopen…"), and its closer "Nothing pretended to be what it was not." is cut. The adventure paragraph loses "She was beginning to suspect that was because nobody had asked her what counted as adventure before."
- **Records:** Plan row 17; ledger R9 (the quote) and O4 (not used in Ch17); triage 17.1, 17.2, 17.5, 17.6; Registry row 17 and the "For the first time" device row; the status table.

**The tenth seat and how it was answered:**

- **K1 (YELLOW):** all six conditions met (one "could see" left, not at Henry Vale; the four reasons spoken and cut off, not narrated; the copies on the page; the "sit beside Pathwell" line reworded to the room; Stansbury's standing answered). Q140 is the reason; the alternative (a clean Pathwell section) is the author's.
- **K2 (YELLOW):** done; the Lemon intact; the smudge exchange as written; one shared task added, and Q134 put to the author rather than claimed.
- **K3 (RED as written):** replaced with the seat's option 2.
- **K4 (GREEN):** done, with the fresh check's trim ("Pathwell had kept showing up…" without "And for three weeks").
- **K5 (YELLOW):** done; 17.5's premise was stale, as the seat said; the dagger not used (ledger O4).
- **K6 (GREEN):** every named line kept.

**Kept against the checks, as leans (R36):**

1. **"Pathwell had kept showing up…" / "She called it evidence."** (reader snag 2). Ch18 depends on her having a reason to call him; this is where she names it, once.
2. **The list of what stays broken, all seven "still"s** (reader snag 5). Three of them repeat Ch15–16, but the list is what stops three weeks of good behaviour reading as a repair.
3. **The new relapse beat (Susquehanna)** (fresh check: it repeats the smudge's shape). It is the one task Elizabeth does with her own hands, and the relapse is caught by her, not by Camp.
4. **Pathwell saying the old answer aloud before he stops** (fresh check: a visible relapse, where before it was silent). It's the only way to show the temptation without his interior.
5. **The museum section has no Pathwell interior at all**, though the cold reader may miss the inside of the temptation.

**For the author:**

- **Q134 ("working alongside each other"):** one shared task is on the page (she checks his copies). Enough, or do you want more?
- **The museum section:** in Elizabeth's view now (Q140). If you want it back in Pathwell's head, that's a third POV exception.
- **The year on the museum card ("2026"):** cut, so the book isn't dated. Put it back?
- **The dagger:** still not used; Ch18 is the last place.

**New lines, plain, flagged:**

- "Getting there meant asking Pathwell to open the way."
- The shared task paragraph (above) and "copied the page again, mistake included."
- "The current curator emailed Elizabeth directly. Pathwell hadn't asked her to come. The museum wanted a witness statement from someone who had been in the room and wasn't Pathwell."
- "So she sat at a side table in the damaged gallery with a pen and a lined pad, writing it one-handed, while the museum made Pathwell write everything down."
- "Elizabeth didn't look up from her pad. 'You were burned at a different incident.'" / "'It's a series,' Stansbury said."
- "You've sent us scans, photographs and old catalog entries since." / "Every copy I could find." / "Useful," the curator said. "Not returned."
- "Same family," Pathwell said. "Same period. Genuine originals. It is better than an empty—"
- "At the side table, Elizabeth's pen had stopped."
- "or to sit any nearer to Pathwell than the side table she'd been given while he felt bad."
- "remembered a man who had kept every pair of socks"
- "Elizabeth went to see the museum reopen the damaged gallery"

**Carried to later passes:** book-wide: look beats at the front of dialogue (18 "Pathwell looked/stared" openers here), the shared flat deadpan across Pathwell, the curator, the archivist, Stansbury and Mama Baga, and the "comply button" shape. Ch18: the dagger, if at all.

**The routine (D23):**

| Step | P42 |
| --- | --- |
| 1 Sunday tone guardrails | done (reader item 1: holds with marks; the narrator's summaries cut) |
| 2 Shapes in the Registry | done (row 17; the device row) |
| 3 Checker | done (numbers above) |
| 4 Scene diagnostic | done (reader item 2: holds for the rack, Henry Vale, Hearts and the label; the and-then stretches trimmed) |
| 5 Fresh check | done (in the morning sitting; its fixes applied) |
| 6 Reader protocol, with the tone and rules check | done (no stoppers; answered above) |
| 7 Replacement tic | done (look beats and the comply button; a few cut, the rest carried book-wide) |
| 8 Deliberate ambiguity | left alone (what she wants to go and do) |
| 9 Change notes from the diff | done (above, against P41) |
| Tenth seat | done (YELLOW; K3 RED, replaced) |
| Light Sunday touch | checked; the chapter has it (the Lemon, Milo's boots, "Copy the smudge.", "lose worse"); none added |

**Not re-run:** the reader and the fresh check on their own fixes.

## P43, 2026-10-06: Chapter 18, the ending

**Goal:** Plan row 18: make the cookbook the silent put-back the interview locked (no price, no branches, no dialogue about it; Q96, Q99, Q103), let "It was my fault" stand without naming Shade or a reply (Q95), make the last exchange plainly Elizabeth's (R9, Q102), and cut the "Not…" cadence (27 paragraphs, the densest in the book). The author said "finish it". The author's draft stops at the museum, so every line here is the August text. The decisions were written before drafting (N1–N5) and the tenth seat ran on them ([file](Tenth-Seat/2026-10-06_Ch18-decisions.md): **ORANGE** overall; N1 and N2 ORANGE, N3 YELLOW, N5 GREEN). The reader ran all three passes ([report](Reader-Reports/2026-10-06_Ch18_reader.md): no stoppers, 8 snags, 17 quibbles; "the book ends on a small, warm, funny errand, with the Ch1 triplet turned the right way round") and the fresh check ran against the pre-pass text ([report](Reader-Reports/2026-10-06_Ch18_fresh.md): no lock broken; the last three lines byte-identical). The change notes below are from the diff against the last commit (P42).

**What changed, from the diff** (2,720 → 2,182 words; paragraphs 477 → about 215; short paragraphs 55% → about 45%, nearly all of them dialogue and the cookbook's own text; "Not…/No…" narration openers 28 → 3; commentary 13 → 1; uncontracted narration forms 20 → 2):

- **The cookbook, silent (N1).** The tenth seat found the decision kept a transaction begun (the ledger turned, his hand flat on it, the shopkeeper's fingers, "Nothing had released."), which Q96 allows but Q103, Plan row 18 and the author's own 2026-09-18 note (§13: he "does **not** ask what it costs", "does **not** start a transaction", "does **not** explicitly test or discuss whether pruning still works") do not. **This pass follows §13 and R19:** never starts. He asks "May I?", picks it up, reads the margins with her (RUTH LIED ABOUT THE LARD. / SHE DID NOT. YOU USED THE WRONG CUP.; the tomato soup; "They seem healthy." / "By family standards,"), the smile fades, "His eyes went to the ledger under the shopkeeper's arm and stayed there.", he looks down at the open book a long moment, closes it, puts it back on the shelf square to the edge, and takes his hand off the cover. After a silence, the shopkeeper takes off his glasses: "I may need to sit down." / "You are sitting spiritually," Pathwell said. / "Do not ruin this." (protected; the seat says it doesn't break Q103's letter). Cut: "How much?", the price and the pockets, "Future." / "Yours?" / "Mine.", the branches ("Alive. / Still capable of division. / Still his."), the shopkeeper's raised fingers, "Nothing had released.", the lift, "Nothing had been spent.", "Camp lost a family cookbook." / "Camp lost Nana's cookbook.", "No what?" / "It isn't Nana's." / "And Camp didn't ask for it." / "Then it stays itself.", the listing lines and "Disturbing.". The narrator's "the need, the available thing, the method, the price" was drafted and then cut after the reader (it explained what the glance shows).
- **"It was my fault" (N2).** Cut: "Shade." (Q95: he doesn't name Shade), "Elizabeth knew they were no longer talking about cookbooks.", the list (first prune, museum, frame, fire) and the Shade sentence, "Elizabeth did not soften it." / "Yes.", and "Life, apparently, remained aggressively uninterested in timing.". The seat's condition was a Shade carrier that isn't Pathwell naming him, and distance from the cookbook. So the admission moved after the coffee: "It was. Shade would have liked it." (Elizabeth's thought; Ch16's "He liked terrible coffee."), the coffee banter, then "He turned the refused cup a quarter turn on the counter and left it there." / "I kept thinking resemblance was enough," he said. / He looked at his empty hand. / "It was my fault." / No speech followed. / The shopkeeper put his glasses back on, opened his ledger again, and went on adding numbers. The reader, asked cold what it referred to: "Shade comes to mind first… The page never says which, and I take that as the design."
- **The ending (N3).** "Already chosen to follow. / Not leading. / Not being dragged. / Coming." is cut, and "Pathwell stopped beside her." no longer comes right before the question. Now: "She looked back. He had already stepped away from the counter, and he came to stand beside her." / "Elizabeth kept her hand on the handle." / "Are you ready?" / "No." / "Perfect." The handle isn't turned before his "No." (Q102: his "No." is unreadiness, not a boundary she overrides). The last three lines are unchanged, with nothing after them. "Freely. / No debt. / No Camp order. / No blob. / No one waiting… / At least as far as either of them knew." is one sentence ("He said it freely: …").
- **Line pass (N4).** Merged or cut: the phone pause; "No mission. / No instructions. / No suggestion…" (one sentence; the dumpling kept); "This was not strategy. / That was also new."; "No sling."; "That was all. / She let the silence continue. / It did not need saving."; the smell list; "He did not make anything of it. / That helped too."; "That was pleasant."; "None of it meant she was special. / That made the room better." (Ch9 says it); "Not guarding her. / Not following."; "Not published cookbooks. / The other kind."; "Not checking for the diary this time. / Just somewhere to put it."; "Not offended. / Not amused. / Surprised."; "The shop was enough. / Being there because she had asked to be there was enough."; the narrator's "apparently" (the postcards). Elizabeth's "Fair." → "Fair enough." Contractions in narration.
- **After the reader and the fresh check:** "Pathwell hadn't asked why she wanted to go back, though they had gone three blocks." (it said "until", and he never asks); "The entrance wasn't the concrete wall she remembered." (there is no alley in Ch3); "The first time, she had been offered the sidewalk, and had chosen a forest without knowing what it was." (Ch4); "I contain multitudes," Elizabeth said; Pathwell's "The fifth is seasonal." joined to his look (it read as the shopkeeper's); "At some point Elizabeth realized she had stopped waiting…" moved before the coffee (after the admission it read as her answer to it); "Pathwell nodded. The silence didn't need saving." (it repeated Ch17 word for word); "She said nothing." cut.
- **Records:** Decisions (the Q94–Q103 lock rows' manuscript column; Q-I); Plan row 18 and the ending notes; ledger P7, O1, O11, R1, R3, R7, R16; triage 18.1–18.8; Registry row 18; the status table.

**The tenth seat and how it was answered:**

- **N1 (ORANGE):** answered by choosing the never-starts reading, on the author's own §13 and R19, and recording it (Decisions Q-I, triage 18.2). The shopkeeper's banter kept after a silence, with his glasses off and back on; "You are sitting spiritually" tagged to Pathwell. The listing line cut (overrides triage 18.1's KEEP).
- **N2 (ORANGE):** a Shade carrier put before the line (Elizabeth's thought), the cookbook anchor broken by distance (the admission is now an hour and a cup of coffee later), and the no-locks cold read run (Shade first). "Yes." cut as the lower-regret reading of Continued 32, and put to the author. "Elizabeth let it stand." not used.
- **N3 (YELLOW):** done; the last paragraph before the question has Elizabeth as its only subject; the handle not turned.
- **N5 (GREEN):** the dagger stays open at the end of the book (ledger O4: open-deliberate).

**Kept against the checks, as leans (R36):**

1. **"I may need to sit down." / "You are sitting spiritually." / "Do not ruin this."** It's the shopkeeper's surprise that he didn't buy, not an explanation, and it's one of the book's best exchanges (Assessment).
2. **"What routes can you actually get us back from?"** (reader snag 6). It is the responsible version of the question; the shopkeeper's routes answer it.
3. **The pause's explanation** ("the kind where a man with too many habitual answers was checking…") stays, merged into one sentence.
4. **"You've changed."** (fresh check: the one place Elizabeth names his change). It is a joke, and he deflects it.
5. **"Nothing has released yet."** (Ch14) is now unpaid. No lock or later chapter needs it; Ch18 no longer stages a prune for it to rhyme with.

**For the author:**

- **The cookbook** follows your 2026-09-18 note exactly: he doesn't ask the price or begin anything. If you wanted him to begin and stop (Q96's "could push the attempt far enough"), that is the old version, minus the branches.
- **Elizabeth's "Yes."** after "It was my fault" is cut (your lock: no response just to show she understands). If you read "Yes." as her holding him to it, it can come back.
- **"Shade would have liked it."** is the new line that points the admission at Shade without Pathwell naming him.
- **The dagger** is never mentioned again after Ch15.

**New lines, plain, flagged:**

- "He looked at her left shoulder, out of the sling now, and looked away again without asking for a report."
- "The entrance wasn't the concrete wall she remembered."
- "His eyes went to the ledger under the shopkeeper's arm and stayed there."
- "Pathwell looked down at the open book for a long moment." / "Then he closed it, carefully, and put it back on the end of the shelf where it had been, square to the edge." / "He took his hand off the cover." / "For a while nobody said anything."
- "It was. Shade would have liked it."
- "He turned the refused cup a quarter turn on the counter and left it there."
- "The shopkeeper put his glasses back on, opened his ledger again, and went on adding numbers."
- "The first time, she had been offered the sidewalk, and had chosen a forest without knowing what it was."
- "He said it freely:"
- "She looked back. He had already stepped away from the counter, and he came to stand beside her." / "Elizabeth kept her hand on the handle."

**Carried to later passes:** the reference pages still say Ch18 "begins" a prune (world bible line 55; contract matrix lines 779 and 881; Decision-Timeline Q138b, Q140b) and the Ch14 tenth seat says Ch18 "completes" the lift; book-wide: "Name looked" openers, "-ly" one-word replies, absence-lists.

**The routine (D23):**

| Step | P43 |
| --- | --- |
| 1 Sunday tone guardrails | done (reader item 1: holds; the one brace, the formula sentence, cut) |
| 2 Shapes in the Registry | done (row 18) |
| 3 Checker | done (numbers above; no stock phrases book-wide) |
| 4 Scene diagnostic | done (reader item 2: holds; explained-after-shown lines cut) |
| 5 Fresh check | done |
| 6 Reader protocol, with the tone and rules check | done (no stoppers; answered above) |
| 7 Replacement tic | done (look openers, "-ly" replies, absence-lists noted; two cut, the rest carried book-wide) |
| 8 Deliberate ambiguity | left alone on purpose: what "resemblance" and "my fault" point to (Q95), and whether he can still prune (Q96) |
| 9 Change notes from the diff | done (above, against P42) |
| Tenth seat | done (ORANGE; answered by the author's §13) |
| Light Sunday touch | checked; the chapter is the book's lightest (the cat, "Diseased lemon.", the margins, the geese); none added |

**Not re-run:** the reader and the fresh check on their own fixes.

## Q1, 2026-10-06: the whole book, read with the questionnaire

**Not a revision pass; nothing in the chapters changed.** At the author's request ("create a questionnaire for a reader to keep in mind as it reads… ask questions based on what my goals of the story were… dont just ask yes or no… lets see if we get the answers that align with our goals"), the reviser wrote the [Reader questionnaire](Reader-Questionnaire.md) (a running log after every chapter, then 54 open questions) and kept a separate [goals key](Reader-Questionnaire-Goals.md) out of the reader's reach until the answers were in. A fresh reader read Chapters 1–18 in order, as of P43 ([log](Reader-Reports/2026-10-06_Whole-Book_reader_log.md), [answers](Reader-Reports/2026-10-06_Whole-Book_answers.md)). The comparison is [here](Reader-Reports/2026-10-06_Whole-Book_alignment.md). The reader used about 233,000 tokens.

**Result, in short:** aligned on Elizabeth's change and who leads at the end, Pathwell's flaw and his late, behavioural turn, Shade as a person, "It was my fault" pointing at Shade, the losses staying lost, the tone, and the last exchange. Its favourite moments are all protected beats. Diverges on: (1) the opening premise (why Pathwell was in her apartment, "Lizzy", the cookie page), which it calls "the book's first question" and never answered; (2) the climax rule, confirming P40 (it's Shade's climax; her rescue doesn't change the outcome); (3) the narrator lines the passes kept as leans, which it names as telling it what to think ("Trust your scenes."); (4) rungs 1–2 reading as passive and the diary gift's want; (5) the Ch18 cookbook motive, read as spending or paying rather than replacing Nana's. The tuning list is at the end of the comparison. The author asked to hold the open questions, so nothing is applied.

## Method, 2026-10-06: the reader panel (D25)

**Not a revision pass.** The author asked for "a protocol and research… about how to have a good reader / reviewer for the story", worried about "having just 1 run of a reader" and that a dozen agents would be "the same agent a dozen times". Researched and written as the [reader panel](../Sunday-Morning/Reader-Panel.md) in the Sunday notes (D25): readers differ by job, reading condition, model and a short reader's life; each gets a sandbox copy of only the text it should read; the shared questions arrive after the reading; at least one lens runs twice to measure noise; findings are extracted per report, merged twice and sorted into convergent, lens-specific, minority and noise; an informed pass then runs the record checks; and every panel reports a noise check and a diversity check. A fresh reviewer checked the page and its sources twice ([review](Reader-Reports/2026-10-06_Reader-Panel_review.md)) (13 of 14 sources fetched; three misquotes and several overstatements fixed). Pipeline Stage 4, the reader protocol, the README and History link to it. No panel has run yet.

## Q2, 2026-10-08: the first reader panel, whole book

**Not a revision pass; nothing in the chapters changed.** The author asked, "can we run this on the story?", and then, to control cost, chose a lean finish. Files: [Panel-2026-10-08](Reader-Reports/Panel-2026-10-08/README.md); results in [synthesis.md](Reader-Reports/Panel-2026-10-08/synthesis.md). Text read: 281524a.

**Panel:** nine runs by eight lenses in four families, on Sonnet and Haiku (no Opus was available). 883 finding records, two merges (A on Sonnet, B on Haiku) that agree on 77% of grouped pairs, and 43 convergent clusters in each.

**Result, in short:**
- **The opening premise is the top gap.** Why he was in her flat, whose door it was, "He still has it", and "Lizzy" are now convergent across three families, which confirms Q1's first finding.
- **Other convergent problems:**
  - the Ch3 currency (a stopper);
  - restitution lists (a stopper in B);
  - Hearts running long (a split; trim, don't cut);
  - the diary donation repeating the cookbook's;
  - "That was the choice." and the narrator explaining;
  - Elizabeth's own want;
  - "Leo";
  - who asked for the prune;
  - the day-of-week slips.
- **Locks that readers faulted:** R11's Ch8 echo and R32's sock. Both are kept; the Ch8 echo is noted for the author (R26).
- **Strengths:** the protected beats.
- **Checks:**
  - Noise check: 31–36%, under the band.
  - Diversity check: passed (lens-to-lens overlap 0.03–0.04 against 0.22 for the repeat pair), with one flag, prose/target-1 at 0.20.

**Leans (R36):**
1. Merge B on Haiku rather than Sonnet, to keep the protocol's "different models".
2. A "short of convergent" list for findings from two or more lenses below the bar. Step 8 has no place for them; proposed as a protocol fix.
3. The character reader's Shade findings stay "prompted", per the extraction rule, so they don't count toward convergence.
4. The lists show only findings at snag or above; quibbles stay in the CSVs.
5. Lean finish: the orchestrating session did the sort, informed check and goals comparison itself, and the D24 check was not run on the findings. This was the author's choice, recorded as a deviation.
6. The Ch8 echo stays (R11), with the readers' reaction reported.
7. The sock: suggest dropping one middle use, not the gag.

**Nothing applied.** The author is holding the open questions.


## P44, 2026-10-12: Chapter 9 diner — character-knowledge repair

**Scope:** Chapter 9 only. The author directed implementation after reviewing the causal gap in Shade's knowledge of why Elizabeth was traveling with Pathwell. R39 clarifies that the Bible cannot substitute for evidence on the page.

**Change (from diff):** Replaced the leap from Shade's “I did not know you existed” to his categorical “You were never the point.” Elizabeth now tells him explicitly that Pathwell brought her along because he thought the apartment creature was after her; Shade limits his testimony to his own pull toward Pathwell and acknowledges he does not know what drew the creature to the door. Elizabeth recalls Stansbury's “Was it?” at the school and Pathwell's “No” after the second creature pursued him. She asks whether the first creature might also have been after someone else; Shade's conclusion is conditional. The original qualifying line “Of whatever followed him. Don't make that sentence larger than it is” remains.

**Continuity check:** Checked the exchanged facts against Chapters 5, 7, and 8; Chapter 10's next question (“What did Pathwell choose?”) remains supported. No magical mechanism, hidden memory, off-page conversation, or separate explanation was added. The remainder of Chapter 9 is unchanged. No automated checker or independent reader pass was run for this narrow amendment; a broader L4 review remains separate.


## P45, 2026-10-12: Chapter 9 diner — remove Shade's explanatory aside

**Scope:** Narrow author-directed line edit to Chapter 9. Removed Shade's “Of whatever followed him. Don't make that sentence larger than it is.” after “Then you were never the point.” Elizabeth's look and physical reaction remain, with the second mention of her name reduced to “She” for flow. The following questions about what drew the creatures remain unchanged. No new character knowledge or lore was introduced. The earlier evidence-based exchange from P44 remains intact. **Review:** Exact passage checked for continuity; no full independent reread or automated suite run for this two-sentence edit.

## P46, 2026-10-13: Chapter 4 — Mama Baga names Elizabeth's welcome

**Scope:** Narrow author-directed addition to the existing clothing exchange, not a replacement or new ritual. After Elizabeth tries on Camp clothes and feels unexpectedly comfortable, Mama Baga says, “You'll fit in here.” The following sentence now names Elizabeth explicitly to avoid a pronoun pointing back to Mama Baga. This puts the author's established understanding — Elizabeth is already welcome at Camp independently of Pathwell (R41) — on the page with one simple line.

**Continuity / boundary:** The clothes, cookbook donation, and Pathwell's separate “You can stay here” were already present in Chapter 4. The new line changes no magical access rule, Shade motivation, or later scene. The hypothetical diner manipulation and Camp-entry mechanics remain open. The exact Chapter 4 passage was checked; no full independent manuscript review or checker run for this two-sentence patch.

## P47, 2026-10-13: Chapter 4 — warmth in Mama Baga's welcome

**Scope:** At the author's request, adjusted the newly added Chapter 4 “You'll fit in here” line so that Mama Baga's behavior feels quietly grandparent-like. After Elizabeth looks at the clothes, Mama Baga tucks a loose strand of her hair beneath her bandana and says, “There you are. You'll fit in here.” The gesture replaces the former speech-only welcome, adding no new ritual, formal admission, or explanation.

**Continuity / boundary:** The outfit, cookbook donation and Elizabeth's independent welcome remain as before (R41, P46). Only the local passage changed. No further diner, Camp-entry, or character-arc scenes were altered. Passage comparison performed; no full independent checker run for this narrow line edit.

## P48, 2026-10-13: Diner discovery archived; portable lessons added to Sunday Morning notes

**Scope:** Documentation and working-method reconciliation only; no chapter prose changed in this pass. Added the author's latest **unresolved** diner reaction to [Chapter 9 development notes](Chapter-09-Character-Dynamics-and-Camp-Access-2026-10-13.md): upon learning she may never have been the blob's target, Elizabeth might feel anger and frustration or even briefly want her old life back, without instantly planning to reach Camp or confront Pathwell. The author has **not settled** her first emotion or next action. The current Ch9–10 decision sequence remains the draft and may need a later scene-level review; it has not been rewritten.

**Method learning:** In the Pathwell repository's [Sunday Morning Craft](../Sunday-Morning/Craft.md#character-discovery-before-explanation), distinguished immediate response, conflicting wishes, and later decisions; updated its scene diagnostic so confused upset doesn't automatically count as passivity. [Pipeline](../Sunday-Morning/Pipeline.md#emotional-and-knowledge-handoff-in-think) adds an optional evidence/emotion/motive/knowledge check in THINK. [Decisions W8–W9](../Sunday-Morning/Decisions.md#working-decisions) mark both rules provisional until author review, not standing D-rulings. [History](../Sunday-Morning/History.md#what-went-wrong-and-where-the-lesson-lives-now) records the examples and failure causes; [README](../Sunday-Morning/README.md) indexes them. No setting-specific facts were added to the setting-free method.

**Continuity and restraint:** Kept Shade's proposed Camp piggyback and psychological leverage separate from canon; Ch11 currently lets Shade use the threshold and remains an open contradiction for a future PLAN pass. Existing author rulings R39–R41 remain. This pass did not implement a diner speech, rewrite Chapter 11, add magical entry rules, run the checker, or run an independent cold read (no manuscript prose was edited).

## P49, 2026-10-13: author-directed operational line-editing system for Sunday Morning / Pathwell

**Request:** The author clarified that prior lessons were still too general: he wants “structure and rules for how to write things not just guidelines,” applicable when editing individual words and reviewing the whole story.

**Documentation changes:** Added [Sunday Morning Line-Editing Protocol](../Sunday-Morning/Line-Editing-Protocol.md) as the single owner for exact copyediting procedures. It defines non-negotiable gates, an order of passes (story contract → causality → paragraph/dialogue → sentence/word → regression), exact word/sentence/dialogue/paragraph/scene/chapter tests, a composition sequence for writing new lines, evidence-based issue classification, a compact edit trace, coverage for full and surgical reviews, and a known Chapter 9 before/after calibration. Recorded [D26](../Sunday-Morning/Decisions.md#standing-rulings) as the author's request, marked the protocol an initial implementation to calibrate, and linked it into [Craft](../Sunday-Morning/Craft.md), [Pipeline](../Sunday-Morning/Pipeline.md), [Reader Protocol](../Sunday-Morning/Reader-Protocol.md), [History](../Sunday-Morning/History.md), [index](../Sunday-Morning/README.md) and the [Pathwell revision index](README.md). The independent reader now checks whether actual line changes have a defensible purpose and pass regression, **after** its blind read.

**Boundary and verification:** **No manuscript words changed in P49.** This does not alter Pathwell's character facts, Shade's proposed diner manipulation, or the open Camp-door contradiction. Documentation paths and required sections inspected; no automated checker or independent manuscript review claimed. The first real editing pass should calibrate the procedure and record KEEP/CUT/REPLACE/OPEN decisions with line evidence, rather than treating these rules as an excuse for blanket prose rewriting.

## P50, 2026-10-14: Chapter 4 — Mama Baga finishes Elizabeth's outfit with her own chain

**Scope:** Narrow author-directed change to Chapter 4's existing clothing/welcome exchange, following Rung interview question 11. The author proposed that Mama Baga look Elizabeth over more than once, decide something is missing, take off her own necklace or bracelet, and declare the outfit complete. To preserve established continuity, the edit reuses the **thin gold chain** Elizabeth already wore in Chapters 4 and 9, rather than introducing a second piece. The earlier clothing sentence no longer treats it as part of the clothes selected from the chest. Mama Baga looks her over twice, says “Something's missing,” removes the chain from her own neck, fastens it around Elizabeth's and says “There. Now it's complete.” Elizabeth's comfortable reaction and Mama Baga's bandana hair-tuck and “You'll fit in here” remain. The former “Better” / “There you are” wording is superseded, not repeated beside the new completion beat. Her coat is now put back on **after** Mama Baga inspects and finishes the visible outfit, rather than before the inspection.

**Evidence/continuity:** Chapter 9 already identifies a gold chain at Elizabeth's throat during the diner entrance. The edit makes that existing object Mama Baga's personal gift without granting the chain magic, creating a new Camp access rule, or establishing that Shade remembers/recognizes it. Shade's potential recognition remains open in [Chapter 9 Rung development notes](Chapter-09-Character-Dynamics-and-Camp-Access-2026-10-13.md#7-interview-mode-session-rung-2026-10-13). [R41](Decisions.md#the-authors-rulings-for-this-revision) was reconciled in the same pass. **Verification:** compared the exact edited passage with its previous form and checked the Chapter 9 diner entrance where the chain appears; no independent full-chapter cold read, checker, or broad chapter audit claimed for this small edit.

## P51, 2026-10-14: Chapter 4 — Elizabeth refuses Mama Baga's chain; affectionate insistence

**Scope:** Small author-directed expansion of the existing necklace-giving beat. When Mama Baga unclasps her chain, Elizabeth now says, “Oh, I can't take that. It's yours.” Mama Baga answers in her brisk, grandmotherly register: “I know it is,” pats Elizabeth's arm, then insists, “Hush now. You're taking it, and I won't hear another word about it.” She fastens the same chain around Elizabeth's neck and calls the outfit complete. The existing hair tuck and “You'll fit in here” remain after Elizabeth sees herself dressed. The added pat is the author's requested soft gesture, not a replacement for the gesture already present.

**Before/after and continuity:** Before P51, Mama Baga put the chain on Elizabeth without objection or conversation. After P51, Elizabeth can object **before** it is fastened; the clasping and response follow in physical order. This preserves her ability to respond rather than denying her a voice. The gold chain remains the one worn in Chapter 9, and no new jewelry, magical rule, or Shade knowledge has been introduced. [R41](Decisions.md#the-authors-rulings-for-this-revision) and [Rung interview Q12](Chapter-09-Character-Dynamics-and-Camp-Access-2026-10-13.md#7-interview-mode-session-rung-2026-10-13) record the clarification.

**Verification:** Exact local before/after passage was compared; chain ownership, objection, fastening order and Chapter 9 object reference checked. This was a surgical edit, not a full chapter review; full cold-reader and checker passes were not run.

## P52, 2026-10-14: Chapter 4 — Mama Baga notices what Elizabeth hides

**Author request:** Add a conversation between Elizabeth and Mama Baga in which Mama Baga can see that Elizabeth carries hurt beneath a practiced composure. The author has not yet specified the full cause of that hurt.

**Smallest placement:** Directly after Mama Baga adjusts Elizabeth's blanket and Elizabeth almost cries, before the turnip boy enters with Nana's cookbook. This keeps the new exchange grounded in an existing involuntary reaction, without explaining the subsequent decision to donate the cookbook or replacing the established necklace-giving exchange.

**New beat:** Elizabeth attempts a polite smile and says she's made quite an entrance. Mama Baga recognizes her tendency to stay polite while struggling. Elizabeth minimizes her distress as a long night; Mama Baga gently suggests there's more to it than tonight. Elizabeth protests that Mama Baga doesn't know her; she answers that she can get to know her. Elizabeth pulls the blanket higher rather than delivering an explanatory speech. These lines are **provisional, subject to author review**, not authority to invent Elizabeth's specific history.

**Continuity checked:** The moment comes after tea, blanket and initial “I'm fine” / “That is not a posture,” and before the boy enters. No change to the cookbook donation, Chapter 4 necklace gift (P50–P51), Chapter 9 recognition question, or world mechanics. Local dialogue turn order, stool placement and blanket pronoun checked; no external independent reader review or full chapter pass completed.

## P53, 2026-10-14: document Chapter 3 party flashback proposal; no chapter edit

**Author's direction:** Preserve Chapter 1's opening crash hook while exploring a chance to see Elizabeth *at* her welcome party. The author specifically asked whether the party could appear as a flashback when she passes out in the Space Between (Chapter 3), then directed us to update the repository.

**READ / evidence:** Compared the Chapter 1 opening (the party's aftermath, Pathwell as a guest, 9 a.m. meeting), Chapter 2's existing emotional breakdown, Chapter 3's other people's emotions → own panic → carpet → waking in the chair, and Chapter 4's Mama Baga/Camp counterpoint. Checked existing R10/R21, R42 and the earlier Bible-interview constraint against replacing the crash with a prologue. The candidate insertion seam is between Chapter 3's carpet blackout and chair waking, not before Chapter 1.

**Documentation changes:** Created [Chapter 3 party flashback THINK → PLAN](Chapter-03-Party-Flashback-THINK-PLAN-2026-10-14.md) with the scene purpose, evidence, a bounded flashback-versus-no-flashback test, continuity constraints, and open choices. Indexed it in [Revision README](README.md) and recorded [R44](Decisions.md#the-authors-rulings-for-this-revision) as a **test proposal**, not an adopted page change. The Rung thread on Elizabeth's private pain and spontaneous happiness remains owned by the [character-development note](Chapter-09-Character-Dynamics-and-Camp-Access-2026-10-13.md#7-interview-mode-session-rung-2026-10-13).

**DO/JUDGE:** No changes to Chapters 1, 2, 3 or 4. No party flashback drafted, no magical memory capability added, no independent cold-reader test or checker run; those belong to a later implementation pass if author-approved. R42's no-length-target rule remains in force.


## P54, 2026-10-15: coordinated Chapter 14–18 climax and ending rewrite (author-authorized)

**AUTHOR DIRECTION:** Following Rung Q43–68, the author selected a restrained, nonmagical Elizabeth climax and the revised Shade ending: Shade is caught unexpectedly by a blob drawn to failed-prune spillage, struggles and calls for help, shares Milo's cry from the archive with Elizabeth, and she rescues the child. Pathwell recognizes Shade's removal as a convenient resolution and deliberately withholds a request for aid. The author then selected **Version C** for Chapter 18 and said “go for it” to the coordinated manuscript revision. Decision sources: [revised climax ruling](Author-Ruling-Ch14-Ch15-Climax-2026-10-15.md), [Version C](Author-Ruling-Ch18-Version-C-2026-10-15.md) and [implementation plan](Climax-C18-Coordinated-Implementation-2026-10-15.md).

**THINK / PLAN:** Read Chapters 14–18 and the existing Ch14–15 rescue availability audits, the author Q51–68 handoff, current canon, character and world bibles, Writing Principles and the voice register. Protected: Pathwell solely caused the failed merge and ordinary archive ignition; Milo's lever/shoulder rescue; Stansbury's separate physical archive salvage and burn; diary/cookbook destruction by fire; active Camp bucket response; Elizabeth uses no magic; final geese destination and exact three-line “Perfect.” ending.

**DO — verified chapter changes:**
- **Chapter 14:** After the working's failure and the fire starts, added a child's short, mostly missed warning pointing toward the woods. The failed-prune causal mechanism remains the same.
- **Chapter 15:** Replaced the later long deliberate-approach/blob dialogue with simultaneous danger at the archive threshold. Shade tries to help with the fire, notices an advancing creature at his shin, struggles and calls for help. A Camp man physically tries and cannot pull him free; Milo also calls from inside the archive and both hear him; Shade and Elizabeth make eye contact. Elizabeth recalls the dagger requires multiple cuts and substantial extraction, then enters the fire to save Milo, passing her irreplaceable diary and cookbook. On exit she sees Shade is gone while the blob clears fresh spill; the witness confirms he could not pull him free. Pathwell is visible and close enough to hear, but his intentional motive is **not** narrated from Elizabeth's viewpoint. Stansbury's salvage and burned hand remain afterward; fire consumes the diary and cookbook ordinarily; the last “Shade did not either” remains.
- **Chapter 16:** Added one line to Elizabeth's grief about the sound of Shade asking for help. Camp's restitution and the conversation refusing easy moral absolution remain.
- **Chapter 17:** Reread for consequences, **no production prose changes**. Its ongoing restitution remains incomplete evidence of change, not absolution of what Pathwell has withheld.
- **Chapter 18:** Applied Version C: quiet cookbook put-back intact; later specific, shame-driven admission that Pathwell heard Shade struggle and deliberately did not call; Elizabeth tries to relate the competing pleas, he gently rejects the moral equivalence; the already existing hour of browsing comes **after** this disclosure. No new length-target scene. Elizabeth still freely picks the route and invites Pathwell; final words unchanged. Cut an earlier explanatory sentence about Pathwell's “Yes” that would have falsely signaled a clean absolution.

**RECONCILE:** Updated [canon](../Story_Files/canon.md), [character bible](../Story_Files/character_bible.md), [world bible](../Story_Files/world_bible.md) and [Non-Negotiable Scenes](../../Non-Negotiable-Scenes.md). The author-directed **voluntary Shade death Q132 is superseded** for the new manuscript; so is the unexplained “It was my fault” Q94–Q95 for Version C. Their historical records remain for provenance. Updated [Revision Status](../../Revision-Status.md); recorded current author choices in the dated ruling files.

**JUDGE — state of review:** Source, staging and limited-viewpoint checks were performed during the edits. **No true independent external cold reader or full manuscript checker result claimed yet.** Critical remaining questions: whether a reader believes Pathwell had a genuine opportunity to call without saving Shade being guaranteed; whether the blob's approach and timing remain physically credible; whether the one-hour gap earns the invitation after confession; and whether the new factual admission is too explicit in the book's dry voice. These are actual revision risks, **not permission to revert the author's choices unilaterally**. All five chapters are kept under L4 pending further fresh review.

**COMPLETION:** Ch14, Ch15, Ch16 and Ch18 committed directly; Ch17 reviewed without changes. The active bibles and pillars updated. No old experiment files were deleted.

## P55, 2026-10-15: informed reader and voice follow-up (not independent L4)

**SOURCE:** Consulted the current main-series chapters and author voice benchmarks (pre-August Ch1–2 at `765b69b`), current [Decisions R45–R47](Decisions.md#the-authors-rulings-for-this-revision), the author-selected Version C, Writing Principles and the Reader/Line-Editing Protocol. Because this review received the previous audit/handoff before reading, it is an **informed** editorial pass, not a blind reader or independent author approval. [Full P55 report](QA-2026-10-15-Informed-Reader-Voice-Followup.md).

**DO:** In [Chapter 18](../Chapters/Chapter_18.txt), cut the duplicate `RUTH LIED ABOUT THE LARD. SHE DID NOT. YOU USED THE WRONG CUP.` following Pathwell's turn to another cookbook page. The earlier inscription remains, and his hesitation, ledger glance, quiet book return, confession, browsing hour, invitation and exact last three lines remain unchanged. No other production chapter was changed.

**JUDGE:** A fresh 12-item live-source assertion pass checked sequence and presence of the revised Ch14–16/18 events, including fire cause, two cries, dagger limitation, ordinary losses, Stansbury injury, grief, confession-to-hour-to-invitation order, and the locked ending: **12/12 pass**. The separate Python voice checker and genuinely cold author-independent reader panel **were not run**. This same pass did not independently approve its own small edit.

**OPEN, evidence-led:** (1) A Camp man is already pulling Shade free when Pathwell declines to call; the specific **additional** help he could summon is vague, although his moral refusal is not. (2) Elizabeth's return to playful banter after the later confession may read as forgiveness despite the chosen no-absolution ending. Also watch creature travel/capture pacing and the repeated Ch4/Ch15 “That was the choice” shape. Keep the author-selected climax and final exchange; test P55-01/02 blind before changing major emotional or causal material. **L4 remains pending** author read and independent panel.

## P56, 2026-10-16: adopt Chapter 1 scavenging clue (author R48)

**SOURCE AND AUTHORITY:** The author said **“I like it”** about the [two-sentence EXP-0008 B Chapter 1 candidate](Emergence/experiments/EXP-0008-Ch01-Entry-Motive-Cue-Controlled-Comparison-2026-10-16.md), then asked what's next. Under R48, this selects **that exact candidate**, not the independently open R38 Chapter 1 revision requests. This specifically addresses the author's confirmed concern that readers could not infer why Pathwell was looking through Elizabeth's things without conflating his book-scavenging motive with the blob's following Pathwell/Shade.

**DO (exact prose delta):** Insert after “He'd been at the party, talking to everybody.”: “She'd assumed someone from work had brought him. She'd seen him peering into an open box of old notebooks once, before somebody asked for more cake.” No other words/paragraph order changed in Chapter 1. The entire approved B trial was used directly from the stored noncanonical experiment file. It does not establish new magical sensing mechanics or a prior relationship with Elizabeth.

**JUDGE (live GitHub fetch):** The committed [Chapter 1](../Chapters/Chapter_01.txt) content exactly matches the author-reviewed [B candidate](Emergence/experiments/EXP-0008B-Ch01-Party-Notebook-Cue-Noncanonical-2026-10-16.txt), and deleting that one 149-character insertion yields the previous Chapter 1 exactly. First line “It was the crash that woke her.” and last “Ready?” / “No.” / “Perfect.” are preserved. Production blob SHA `ee5e5ad6db1dc3a02f2401227e42225523b36f45`; chapter commit `c7da0da8f4f55d00416f59af7251cbe52d71ba90`.

**RECONCILE:** [Decisions R48](Decisions.md#the-authors-rulings-for-this-revision) and [Promise Ledger P1](Promise-Ledger.md) now distinguish **early evidence** of an emotionally charged-material scavenger from later explanation of the creature's unrelated pursuit. [EXP-0008](Emergence/experiments/EXP-0008-Ch01-Entry-Motive-Cue-Controlled-Comparison-2026-10-16.md) and [Emergence index](Emergence/INDEX.md) mark B as selected and implemented; the stored B file remains a historical review artifact.

**OPEN:** Unprimed reader recall at Chapters 3/9 is not run; **not L4**. Existing R38 notes cover further physical blocking, first spell, Nana cookbook panic, low tide and line cuts, all of which **remain unchanged** by this pass. The R44 proposed Chapter 3 party flashback also remains unapproved. Chapter 1 remains L3 pending author/fresh-reader gate. No other chapter changed.

## P57, 2026-10-16: Chapter 1 cookbook action and early door test

**AUTHORITY:** Following the [EXP-0009](Emergence/experiments/EXP-0009-Ch01-First-Magic-and-Cookbook-Panic-2026-10-16.md) A/B comparison and recommendation to retain a more physical book grab, treat extra first-magic exposition cautiously and examine the author's R38 door-glimpse idea separately, the author said **“go for it”**. [R49](Decisions.md#the-authors-rulings-for-this-revision) records the bounded interpretation: implement **book action only**, leave original first-magic phrasing unchanged, and prepare a **noncanonical** door trial.

**DO — production:** [Chapter 1](../Chapters/Chapter_01.txt) one exact replacement:
- Before: `Elizabeth snatched the book, leaving the page behind. "What are you doing!?"`
- After: `Elizabeth grabbed the cookbook by the spine and pulled it from his hands. The sugar-cookie page stayed under his palm.` then its own paragraph `"What are you doing!?"`.
- The interrupted sugar-cookie working, Nana's memory, creature already at the door, Pathwell's marked bluff, opening, party-notebook cue and exact ending did **not** change. [Production commit](https://github.com/BigCatMellow-Archive/Pathwell/commit/c5f671d4345727ff481dc9dd83f6873a19b4dd29), blob `5faf36143e072265f477bc3e9acf9cc024176036`.

**THINK / PLAN / TEST — research only:** [EXP-0010](Emergence/experiments/EXP-0010-Ch01-Door-Glimpse-Blocking-and-Reader-Controls-2026-10-16.md) compares the existing “Friend of yours? / What?” → sniff → door bow scene with [a full noncanonical Chapter 1](Emergence/experiments/EXP-0010B-Ch01-Door-Glance-Chain-Candidate-2026-10-16.txt) where Elizabeth opens the locked front door only to the length of its chain, glimpses a dark/wet substance, and Pathwell closes and bolts it, with two later prose/blocking adjustments so the action remains stageable. It is **not authorized as live prose**. The old locked early door-opening scenario is a suggestion, not a complete current blocking lock.

**JUDGE — informed checks:** The production change is reversible as one exact string replacement and is the only production prose update in this pass. The noncanonical door candidate is constructed from the new live text with exactly three isolated replacements; the exact first-magic sentence and final Ready/No/Perfect exchange remain unchanged. No unaffiliated reader or L4 claim. Door trial has material risks (why she opens after the wet thud, chain/bolt logistics, softened monster reveal) that need independent reading and author preference before being adopted.

**RECONCILE:** [EXP-0009](Emergence/experiments/EXP-0009-Ch01-First-Magic-and-Cookbook-Panic-2026-10-16.md) marks change 2 adopted and change 1 unadopted; the [Emergence Index](Emergence/INDEX.md) points to EXP-0010. [O1](Promise-Ledger.md) and [Revision Status](../../Revision-Status.md) updated to reflect physical page loss and Chapter 1 L3 gate. R38's other author notes remain open.

## P58, 2026-10-16: author-approved Chapter 1 door glimpse

**AUTHORITY:** The author responded **“go for it”** to the specific choice of whether to put Elizabeth's early door-opening into [Chapter 1](../Chapters/Chapter_01.txt). The immediate proposal linked the complete B passage and [EXP-0010 blocking assessment](Emergence/experiments/EXP-0010-Ch01-Door-Glimpse-Blocking-and-Reader-Controls-2026-10-16.md), so the authorization selects **that full candidate**, not EXP-0009's separate first-magic expansion or any other outstanding R38 notes. New ruling [R50](Decisions.md#the-authors-rulings-for-this-revision).

**DO — live Chapter 1:** The previously reviewed B candidate was committed verbatim. The change has exactly three coordinated spans:
1. Following “Friend of yours?” / “What?”, Elizabeth checks the wet thud from inside, opens her apartment door only against its chain, sees an indistinct wet/dark substance, and Pathwell closes and bolts the door with the diary under his arm. He can smell low tide and the door bows under pressure **before** reaching for her cookbook.
2. The subsequent “He was on his feet with the diary …” stage direction becomes **“He went straight back to the boxes, the diary still under his arm.”** This prevents him from inexplicably getting up a second time when the front door sequence already showed him crossing the room.
3. At the later breach, the “It was some sort of blob” reveal becomes **“Now she could see the whole thing: some sort of blob…”**. The opening glimpse of matter is distinguished from the first view of the complete creature.

**VERIFIED:** GitHub fetch of production [Chapter 1](../Chapters/Chapter_01.txt) exactly matched the stored [EXP-0010 B full chapter](Emergence/experiments/EXP-0010B-Ch01-Door-Glance-Chain-Candidate-2026-10-16.txt), and a reconstruction by applying only these three replacements to prepass Chapter 1 matched the same file. Source blob before pass `5faf36143e072265f477bc3e9acf9cc024176036`; after pass `4545631a3441514e6d337fb628c45742ceef933d`; [production commit](https://github.com/BigCatMellow-Archive/Pathwell/commit/157caf3c0ed59d41628e36db9668347060316b58).

**REGRESSION CONTROLS:** The first line “It was the crash that woke her.” still refers to the fallen stack of boxes. The welcome party remains hers, Pathwell's notebook/diary scavenging cue remains, the blob is at the door **before** any cookbook magic, Elizabeth still physically grabs Nana's cookbook, the original short first-magic/sugar-cookie memory remains, the “marked” diagnosis is still Pathwell's unjustified claim and the final exchange remains “Ready?” / “No.” / “Perfect.” Chapter 2's escape starting on the stairs, and Ch4/5/7/9's later cleanup/false-target resolution are undisturbed. No other chapter edited.

**UNRESOLVED / JUDGE LIMIT:** This was an **informed editorial and live-text continuity assertion check**, not a blind read. The new “Someone might have fallen in the hall” rationale, plausibility of opening a chained door after a strange wet thud, Pathwell's return to rummaging, and whether the earlier partial glimpse reduces the full breach's fright need unprimed reading and author whole-chapter judgment. Other R38 suggestions (more magical first experience, heavier cookbook feelings, smell, duplicated impact note, rogue falling box, and post-fight bathroom blocking) remain separately open. Chapter 1 remains **L3, not L4**.

**RECONCILE:** [Decisions R50](Decisions.md#the-authors-rulings-for-this-revision), [Emergence EXP-0010](Emergence/experiments/EXP-0010-Ch01-Door-Glimpse-Blocking-and-Reader-Controls-2026-10-16.md), the [Emergence index](Emergence/INDEX.md), [Promise Ledger P3 / R15](Promise-Ledger.md), and [Revision Status](../../Revision-Status.md) record the selected scene's changed setup and agency.

## P59, 2026-10-16: author selects C for first magic

**AUTHORITY:** The author replied **“Go C and continue”** immediately after viewing the complete [EXP-0011 A/B/C first-magic trial](Emergence/experiments/EXP-0011-Ch01-First-Magic-Controlled-Comparison-2026-10-16.md), with [C's full novel context](Emergence/experiments/EXP-0011C-Ch01-First-Magic-Ink-and-Perception-2026-10-16.txt). Under R51, this approves C's specific prose rather than a generic expansion of every R38 stylistic idea.

**DO:** In [Chapter 1](../Chapters/Chapter_01.txt), changed exactly **one unique source paragraph**, the old “He placed his hand flat on the page, the letters glowed a soft gold.” into three short paragraphs: his hand on page; gold running along Nana's uneven ink, where her pen hesitated; Elizabeth leaning close enough to see the ink beneath it. Production commit [ed1df00](https://github.com/BigCatMellow-Archive/Pathwell/commit/ed1df00de3252a283675f22bc96655da1260efe4).

**CHECK:** Fetch confirmed a literal match with the reviewed EXP-0011C full alternative; undoing the single replacement reconstructed the previous canonical Chapter 1 exactly. The notebook clue, chained-door glimpse, cookbook grab, Nana's intact cookie memory, disrupted working and gold spill, creature already outside the door, later “marked” misread, and the closing “Ready?” / “No.” / “Perfect.” are untouched. New gold-ink perception does **not** add an Elizabeth-specific magical ability.

**STATUS:** Author chose the exact paragraph. The larger chapter still awaits unprimed reading and full-chapter verdict (L3, not L4). Earlier EXP-0009B includes a noncurrent pre-R50 door sequence and is not the current control.

## P60, 2026-10-16: Chapter 1 mechanical line clarity

**AUTHORITY:** The author's **continued work instruction**, the original October 8 [R38 line notes](Author-Notes/2026-10-08_Chapter-01_line-notes.md), and the [post-R50 triage](Emergence/CHAPTER-01-R38-CURRENT-DISPOSITION-2026-10-16.md). This pass uses reviser judgment for tiny, reversible physical clarity rather than misrepresenting each line as independently author-selected. R52 records scope.

**DO — four isolated production edits, each verified against its immediate prior source by single-block reversal:**
1. The free-floating “A box hit the ground.” after Pathwell's cookbook demand became **“He shoved a box aside.”** He is the visible actor, without an uncaused fall. In the same commit, remove the repeated **“A clear bright note that rang through the room.”** after “The impact sang.” [commit 8b2855a](https://github.com/BigCatMellow-Archive/Pathwell/commit/8b2855aeab7b4f2ac29dba58a403bbff32ae9d85).
2. A later duplicate first-opening of the bathroom door became **“She stepped out of the bathroom.”** She had already opened it slowly earlier; the revised line clarifies the exit rather than pretending the door was closed anew. [commit fb14213](https://github.com/BigCatMellow-Archive/Pathwell/commit/fb14213ece5c63e6a4d03af90a0a8bb2460447b8).
3. The doubled “It rolled over the gold on the carpet, and the gold went out.” became **“The blob rolled over the fallen threads of gold. Their light went out.”** This connects the same loose gold threads spilled by the interrupted working to the creature's consumption of cleanup waste without adding a magical mechanism. [commit f2ec685](https://github.com/BigCatMellow-Archive/Pathwell/commit/f2ec68513496a82391aad18b7e11688df2f41877).

**JUDGE:** These are local grammar/action refinements; the underlying interrupted-casting and blob-response rules were checked against [the current world bible](../Story_Files/world_bible.md), which expressly identifies the *Chapter 1* gold mess as unclaimed casting waste. No new weapons, spell effects, emotional reactions or dialogue added. No other chapter edited. The first C magic paragraph and previous R48–R50 locks were preserved.

**HELD FOR SEPARATE CHOICE:** The strike line is still the passive “met sharply by a blinding strike,” which raises real uncertainty over action/spell mechanics. The early Pathwell **“Perfect.”** repetition is a signature voice choice that may intentionally echo the locked last word. [EXP-0012](Emergence/experiments/EXP-0012-Ch01-Strike-Actor-and-First-Perfect-2026-10-16.md) presents separate noncanonical **active strike / unattributed flash / ‘Good… that's good’** full-chapter controls; none is promoted. Second low-tide detail, cookbook emotional depth, the post-“Huh” blocking and Elizabeth's repeated refusal remain open to a proper scene read rather than automatic expansion.

**LEVEL:** L3; a truly independent uninformed read and author's whole-chapter verdict remain open. [Revision Status](../../Revision-Status.md) and [Emergence Index](Emergence/INDEX.md) track the active source.

## P61, 2026-10-16: page-contact staging and dialogue comparison

**SCOPE AND AUTHORITY:** The author said **“continue”** after the previous pass recommended resolving Chapter 1's unclear strike, then settling dialogue choices before an unprimed read. The active source was fetched afresh at blob `03eafcab77d35805839468755abaf9b55f921a85`; the active [world bible](../Story_Files/world_bible.md), the [August interview](../Interview/BIBLE_DECISIONS_2026-08-22.md), [R38 author line notes](Author-Notes/2026-10-08_Chapter-01_line-notes.md), and [EXP-0012](Emergence/experiments/EXP-0012-Ch01-Strike-Actor-and-First-Perfect-2026-10-16.md) were reviewed. **This is a reviser implementation under the ongoing task, not a newly signed-off author R53.** The first “Perfect” and paired dialogue cuts remain author-facing alternatives.

**DO — canonical Chapter 1 (two isolated changes, separate commits):**

1. Replace the passive “It darted for the light in the man's hand, where it was met sharply by a blinding strike.” with “It darted for the light in the man's hand. He raised the glowing page between them. The blob struck it, and white light burst out.” The original “The impact sang.” stays. The action is **contact with the already-active protective cookbook page**, not a new offensive blast or spell. Single replacement verified against [EXP-0013B full-chapter control](Emergence/experiments/EXP-0013B-Ch01-Strike-Page-Barrier-2026-10-16.txt). [Production commit](https://github.com/BigCatMellow-Archive/Pathwell/commit/672dfcbdbc7a7f32768a4b486b33d97a17b1985d), post-fetch blob `7a664b5da41d98fcaaa3f9dccb0b52807a861d6e`.
2. Repair the mixed comma splice and stranded fragment after Elizabeth watches the ink: “The door began to crack and splinter. Ooze searched through the gaps, and the stench of low tide turned her stomach.” This preserves existing threat and smell without inventing a new monster signal or smell note. [Production commit](https://github.com/BigCatMellow-Archive/Pathwell/commit/31597d6f0c2ffd4bcbe0702958e96d3362f8dc04), post-fetch blob `40bbe6aab026db2095e77ed84b213ac52cea4175`.

**THINK / PLAN — dialogue kept noncanonical:** [EXP-0014](Emergence/experiments/EXP-0014-Ch01-Dialogue-Cuts-and-Bookend-Test-2026-10-16.md) compares the current first “Perfect”, first “I'm not going anywhere with you”, and “Understandable. But” with [B: paired cuts](Emergence/experiments/EXP-0014B-Ch01-Refusal-and-Preamble-Cuts-2026-10-16.txt) and [C: paired cuts plus “Good… that's good”](Emergence/experiments/EXP-0014C-Ch01-Author-Dialogue-Trio-2026-10-16.txt). Those full candidate files were captured **before** the second scent-fragment grammar edit; copy only explicitly selected snippets into the *latest* chapter, not an entire old trial. They were not committed to `Story/Chapters`.

**READER/MECHANICS JUDGE:** Page still remains in Pathwell's hand after Elizabeth removes the cookbook; the blob first consumes loose threads of interrupted casting waste, then lunges for the still-active page. A shielding/contact flash is a coherent physical reading of the already-described defensive cookbook working, **not a universal rule for other texts**. The creature's arrival precedes the spell; the misdiagnosed “marked” apartment remains Pathwell's belief/bluff, not canon fact. Introductory crash, party notebook cue, the author's original Nana kitchen memory, bodily retreat, and final Ready/No/Perfect survive unchanged. No chapter other than Chapter 1 edited. No genuinely unaffiliated cold reader participated in this pass; keep **L3**.

**NEXT GATE:** The author can pick keeping the dialogue unchanged (**A**), paired cuts (**B**), or paired cuts plus the author's original “Good… that's good” (**C**). Before L4, test the revised full Chapter 1 without giving readers the project annotations, then get a whole-chapter author verdict. An informed editor rereading known problems does not meet that requirement.

## P62, 2026-10-16: shorten Chapter 1 departure and attribute Chapter 2 speaker

**SOURCE/REVIEW:** The author said **“continue”** after the previous pass compared the paired dialogue cut Version B against keeping the original (“Perfect” choice held). This allowed the reviser to finish the comparison and work forward, but was **not** an explicit author vote “Go B”. The source is the [author's R38 October 8 markup](Author-Notes/2026-10-08_Chapter-01_line-notes.md) ¶131 / ¶139 requesting these exact cuts, and ¶185 requesting Chapter 2 opening speech attribution. The informed in-context analysis is [P62 Chapter 1–2 dialogue review](Emergence/CH01-CH02-P62-DIALOGUE-DECISION-AND-TRANSITION-2026-10-16.md).

**THINK / PLAN / DO:**
1. In [Chapter 1](../Chapters/Chapter_01.txt), **delete** the first “I'm not going anywhere with you.”, and **cut only** the dependent “Understandable. But” lead-in to Pathwell's subsequent “Your house has now been marked…” statement. These two changes are an interdependent unit. Keep the stronger “I'm not going anywhere until you tell me what is going on”, his talking past it (“That confusion is quite normal. Do you have shoes?”), the later “I already told you I'm not—”, and the final “No.” **Both first and final “Perfect.” remain exactly as before.** [Commit](https://github.com/BigCatMellow-Archive/Pathwell/commit/84475de4be117a6663b431190045ce9148f55506).
2. In [Chapter 2](../Chapters/Chapter_02.txt), remove **only the blank line** after “Will you slow down!?” so that Elizabeth's action follows in the same paragraph: `"Will you slow down!?" Elizabeth struggled to keep up with him as he charged down the stairs. "What about all my stuff?"`. The author's specific ¶185 comprehension request is satisfied without adding content. [Commit](https://github.com/BigCatMellow-Archive/Pathwell/commit/7ae7d3ed4802bd332d17d19fb9d499d2ca2c33a8).

**JUDGE (verified against GitHub):**
- Chapter 1 live fetch exactly reversed to the immediate prior blob `40bbe6aab026db2095e77ed84b213ac52cea4175` after reinstating **those two and only those two** changes; new blob `a105bc1cff92664e0d0faaf31bca58426f0cb06a`.
- Chapter 2 live fetch exactly reversed to blob `4e505c3c72c4e87bd6a644ddccf9c811bb5c027d` when the sole removed line break was restored; new blob `6f2b9e7ff157242ebd6fe610847404911577bb66`.
- [Chapter 3](../Chapters/Chapter_03.txt) still begins with Elizabeth refusing to go further without questions, and challenges Pathwell over retaining both Nana's cookbook and her diary. The character-control thread is not severed by one earlier dialogue cut.
- The creature's **pre-spell** arrival, gold spillage **after** interrupted cookbook work, protective-page contact, original sugar-cookie memory, author-selected first-magic C, and final “Ready?” / “No.” / “Perfect.” all survive unchanged.

**EDITORIAL COST / HOLD:** The deleted lines originally made Pathwell ignore a directly stated “No” before his bluff. Revised B instead puts her refusal **after** the false “marked” diagnosis, where Pathwell immediately sidesteps it. The revised line should be judged in a fresh read, not pronounced objectively superior. The author's “Good… that's good” marked-up alternate remains **noncanonical**. [EXP-0014](Emergence/experiments/EXP-0014-Ch01-Dialogue-Cuts-and-Bookend-Test-2026-10-16.md) and the [P62 detailed review](Emergence/CH01-CH02-P62-DIALOGUE-DECISION-AND-TRANSITION-2026-10-16.md) preserve the tradeoffs. Earlier whole-chapter candidate files predate P61's low-tide grammar repair and must not be blindly copied over current canon.

**NEXT GATE:** A genuinely uninformed first-act read, ideally Chapters 1–3, should test the motive clue, consent pressure, and why Elizabeth continues; the previously held Ch3 party-flashback candidate remains **unapproved**. Do not pretend informed editing is an independent read. **Chapter 1 and Chapter 2 remain L3** pending author whole-chapter verdict and valid reader check.

## P63, 2026-10-16: manuscript-only Chapters 1–3 reader audit

**AUTHORITY / EVIDENCE LIMIT:** The author said **“go for it”** after P62 recommended a fresh, unprimed reading of Chapters 1–3 to test Pathwell's initial motive, the creature's timing and Elizabeth's reasons for following. This session could directly re-read the current [Chapter 1](../Chapters/Chapter_01.txt), [Chapter 2](../Chapters/Chapter_02.txt) and [Chapter 3](../Chapters/Chapter_03.txt), and it could prepare a clean reader packet. **It did not have a genuinely independent uninformed reader or isolated fresh reading agent.** A prior-context-aware reviewer, even when using only chapter text as evidentiary basis, must report an **informed manuscript-only audit**, not falsely certify an unprimed reader panel.

**DO — research deliverables, no chapter edits:**
1. [P63 manuscript-only comprehension audit](Emergence/FIRST-ACT-P63-MANUSCRIPT-ONLY-READER-AUDIT-2026-10-16.md) reads all three latest source chapters in order and records at each chapter boundary what is shown, what is inferable and what is still deliberately unknown, then ranks falsifiable risks F1–F8.
2. [Neutral first-act reader packet](Reader-Reports/First-Act-2026-10-16/READER-PACKET.md) gives direct current-Ch1/2/3 links and generic running-log/end-of-Ch3 questions. **Only the packet and chapter files** should be given to an actually new reader; the audit, author goals, bible, prior panel and experiment reports must not be provided until after that reader responds. Existing [whole-book reader questionnaire](Reader-Questionnaire.md) inspired the log discipline, but its spoilers/answer key remain separate.

**HIGHEST SPECIFIC NEW CANDIDATE:** The Ch2 diner scene puts Elizabeth's two books **on the table**. Later Pathwell “gather[s] up his things” and leaves; the final “He still has it” requires him to have brought her books. Ch3 confirms the objects are beneath his arms, but the **pickup itself is not explicitly depicted**. This may be effective delayed realization rather than a mistake. Ask cold readers where the books were when he walked away **before** supplying an alternate explicit-pickup line. No prose change authorized from this audit alone.

**ADDITIONAL RISKS:** Ch1's “marked” statement is only Pathwell's assertion; readers can legitimately believe it until the story's later correction (Ch5–9). His party attention to old notebooks plus the Ch3 trade supports the *kind* of material he wants but does not fully prove why he picked that apartment. Ch3's Rai Stone/Lydian coins/potential sequence may overload readers before the cost is bodily felt; the Oct 8 simulated panel had independently complained in **the older version**, but is **not a reader test of this version**. Pathwell calling Elizabeth “Lizzy” may read as prior knowledge; test guesses rather than retconning magic rules. Elizabeth's constrained choice remains visible as property custody, not free consent, and Ch3 explicitly returns both books to her after the settlement.

**VERIFY:** Primary file SHA captured in the audit: Chapter 1 `a105bc1cff92664e0d0faaf31bca58426f0cb06a`, Chapter 2 `6f2b9e7ff157242ebd6fe610847404911577bb66`, Chapter 3 `7ac8171b172c20de1449c4901c4e58a44b3c83d5`. **Zero source edits in P63.** None of the scoring rubric dimensions is populated with invented reader answers. No “new reader” success claim, no L4 elevation. Chapter 1–3 follow-up now waits on genuinely isolated outside text response or author discussion. Current L3 development status remains unchanged.

## P64, 2026-10-16: launch recruitment handoff for authentic first-act blind reader

**SOURCE:** After P63's informed manuscript-only audit, the author replied **“go for it”** to the next goal: obtain a truly unprimed first-act response for current Chapters 1–3, not another informed reenactment. P63 explicitly separated editorial hypotheses from real reader data and already provided a neutral questionnaire. **No new independent reader result is available in this tool session.**

**REVIEW OF AVAILABLE EXECUTION:** The linked repository contains extensive older model-simulated reader-panel records, but no `.github/workflows` workflow configured to execute a new isolated reader. The current chat has no tool to summon a new clean-context reading model or an unfamiliar human. A plugin capability search likewise did not supply a connected fresh-reading service. These constraints cannot be repaired by pretending a re-prompt of the same editorial reviewer is blind.

**DO — concrete recruitment/test assets:**
1. Created [the standalone first-act reader edition](Reader-Reports/First-Act-2026-10-16/READER-EDITION.md) with full Chapters 1–3 in order and neutral, non-spoiler running-log instructions. Each prose body was programmatically compared character-for-character against the current live GitHub chapter at build time, excluding presentation headings; **all three matched exactly**. Snapshot blobs: Ch1 `a105bc1cff92664e0d0faaf31bca58426f0cb06a`, Ch2 `6f2b9e7ff157242ebd6fe610847404911577bb66`, Ch3 `7ac8171b172c20de1449c4901c4e58a44b3c83d5`. Creation commit `ae482b9c8bb4f3b5c35be41d3ee0b0bc891d5929`.
2. Opened [GitHub issue #3](https://github.com/BigCatMellow-Archive/Pathwell/issues/3) as the public reader invitation and response-tracking task. The issue directs readers to see **only** the reader edition and [neutral packet](Reader-Reports/First-Act-2026-10-16/READER-PACKET.md), to save comments after each chapter *before* advancing, to avoid other reader responses and editorial files, and to return answers privately where possible to prevent contamination.
3. Preserved the separate **editor-only** [P63 audit](Emergence/FIRST-ACT-P63-MANUSCRIPT-ONLY-READER-AUDIT-2026-10-16.md) as a scoring key to be used **after** actual reader answers, not as briefing material. The public issue marks every response/score condition unchecked and records **zero independent reader submissions** upon creation.

**JUDGE:** These are usable logistics and an open recruitment endpoint, **not** a completed blind read. Recruiting real participants, collecting their notes, comparing to P63, and the author's whole-chapter approval remain outstanding. No result count, reader quote, comprehension finding, or L4 upgrade has been fabricated. **Zero canonical chapter edits in P64.** If chapter prose changes, preserve this dated edition as the frozen stimulus and create a separately versioned edition rather than modifying it in place.

**NEXT GATE:** A person who has not read Pathwell must actually read the self-contained edition and return chapter-by-chapter impressions; submit responses without exposure to notes or prior panel results. Then record the responses verbatim with permission, analyze without leading reinterpretation, and escalate only confirmed recurring problems. L3 remains.

## P65, 2026-10-16: evaluate supplied informed Chapters 1–3 reader report

**RECEIVED:** The author uploaded `Pasted text(20261016-172846).txt`, **838 lines**, containing a review organized by Chapter 1, Chapter 2, Chapter 3, an after-Ch3 comprehension section and an overall evaluation. The reviewer begins with an explicit **prior-familiarity disclosure** (knowledge of later chapters, characters, plot, prior revision discussions), though says they read Chapters 1–3 in order and did not consult other materials while preparing this review. Treat as **ONE INFORMED reader response**, not an independent blind first-time reader. **Do not** close [GitHub issue #3](https://github.com/BigCatMellow-Archive/Pathwell/issues/3) as if a genuinely unfamiliar reader completed the test.

**DO — evaluated and archived the findings:** [Informed-review evaluation](Reader-Reports/First-Act-2026-10-16/INFORMED-REVIEW-EVALUATION-2026-10-16.md) records provenance, what the report actually claims, a point-by-point comparison with P63's **F1–F8** predicted risks, fresh observations, and the smallest safe next checks. The full 838-line uploaded text remains the conversation source; this repository document is **an editorial analytical extract**, not falsely presented as a raw transcript or newly generated independent reader log.

**OUTCOME — reader-positive signals:** Reader reports willingness to continue after all three chapters, more firmly at Ch3. The emotional magic, Nana's cookbook memory, Elizabeth's mixing spoon and breakdown, horrible-but-restorative coffee, love-note healing, costly future-potential ritual, shopkeeper's property-ownership rebuke and the handcart joke are especially effective. Reader understands Elizabeth's pressured rather than carefree decision to follow Pathwell, and keeps the initial creature target uncertain. This is **direct evidence of one informed review**, not a tested general audience conclusion.

**OUTCOME — risks supported in the actual report:**
1. **Strongest recurring issue:** Why Pathwell searched **this apartment** before the attack and what he is trying to accomplish with Elizabeth remain unclear by Ch3. The R48/P56 party-notebook clue helps the reader infer he is looking for written materials, but does not answer the exact motive. Reader also doubts why Pathwell repeatedly declines basic explanations and worries the story may excuse his disregard for Elizabeth by making him charming.
2. **New physical/circumstantial issues:** Ch3's bulk *order* appears at the shop counter without a clear preparation/selection stage, while the price is spectacular but immediate benefit vague; the Ch1 old sugar-cookie page remaining under his palm is somewhat hard to visualize; the Ch2 truck neatly blowing away the dry-cleaning ticket feels contrived despite that emotional beat working.
3. **P63 checks NOT confirmed:** This reviewer **did not** get confused about who has Nana's cookbook at the end of the diner scene; did not insist Pathwell's “marked” claim was fact; did not object to Elizabeth opening the chained door; and did not cite Rai/Lydian **vocabulary** as a reason to stop. Avoid turning P63 hypotheses or 2026-10-08 panel complaints into claims about this report.
4. **Ch2 exchange strain:** Dumpling banter and nonanswers became repetitive, and the changing neighborhood received less attention than the reviewer wanted. Elizabeth's fuller emotional life nevertheless begins to land in Ch2, and her Chapter 3 reflex to help Pathwell after the costly ritual is understood as involuntary human compassion rather than forgiveness.

**CH4 CONTROL — read canon before prescribing changes:** [Chapter 4](../Chapters/Chapter_04.txt) already shows Camp workers needing supplies (“We were down to six sheets”) and Mama Baga saying **“We did not ask for this” / “You needed it” / “We did.”** It reframes the Ch3 purchase as a self-appointed attempt to help that addresses the reviewer’s next-step demand for a beneficiary *without providing an early magic lecture or excusing Pathwell*. Ask an unfamiliar reader to continue to Ch4 and evaluate whether that payoff comes quickly enough before rewriting Ch3.

**AUTHOR-HELD GATES / NO CHAPTER CHANGE:** Do **not** respond by revealing the blob's ultimate target, making Elizabeth magical, dissolving consent pressure, cutting the mixer/ticket emotional detail, softening the shopkeeper's property rebuke, or inventing how all pages become barriers. The review contains suggestions and doubts, **not author approval** of any particular prose. No canonical chapters changed under P65. Preserve L3 and [issue #3](https://github.com/BigCatMellow-Archive/Pathwell/issues/3) for a truly unfamiliar reader. Use this informed review as a diagnostic baseline to compare against a later genuinely unprimed report, not a substitute.


## P66, 2026-10-20: independent first-act editorial assessment, Chapters 1–4

**SOURCE / AUTHORITY:** The author's editorial-agent handoff of 2026-10-20 (assignment: narrative clarity, motivation, pacing and continuity of Chapters 1–4; deliverables A–E; branch and pull request; no unapproved manuscript changes). Source read: `main` at `63dd268`; chapter blobs Ch1 `a105bc1c`, Ch2 `6f2b9e7f`, Ch3 `7ac8171b`, Ch4 `ce180867`. **Informed review by a new agent**, independent of the passes that wrote the current text, **not** an unprimed reader; [issue #3](https://github.com/BigCatMellow-Archive/Pathwell/issues/3) remains open with zero submissions.

**DO — research only, no chapter edits:**
1. [P66 assessment](Emergence/FIRST-ACT-P66-INDEPENDENT-EDITORIAL-ASSESSMENT-2026-10-20.md): per-concern analysis (location, observation, reader evidence, interpretation, counterargument, payoff, severity, recommendation, confidence) for handoff concerns A–E plus three new findings; a chapter-by-chapter information map (fact / inference / mistaken claim / unresolved); a Ch3–4 continuity audit separating staging from motive.
2. [EXP-0015](Emergence/experiments/EXP-0015-First-Act-Motive-Hinge-Order-Staging-Page-Tear-2026-10-20.md): controlled A/B/C candidates as `git apply` patches against `63dd268`: **B1** one line of Elizabeth's inference at the Ch3 counter linking her diary to the shop's ledger; **B2/C2** where the Ch3 order came from; **B3/C3** the Ch1 page tearing; **R1** the orphaned “Again” left by P62.
3. [Decisions Q-O](Decisions.md#open-for-the-author): is Chapter 2's changed neighborhood displacement or magic?

**FINDINGS (ranked):** (1) **Motive** — nobody in the book ever asks Pathwell what he was doing in her apartment, and the party is never mentioned after Ch1 ¶9; the creature question is handed from Pathwell to Mama Baga to Elizabeth by the end of Ch4, the motive question never is. The material for the answer is on the page (notebooks, diary, ledger, debt, “outside property”, “never his to spend”, “no-good thief”) and lacks one hinge. HIGH. (2) **Ch3 order** appears on the counter with no source: staging defect, MEDIUM; the price's proportion is already explained as clearing the whole account (“past bills and all”), LOW. (3) **Ch1 page** — the tear is never shown though Ch1/3/4 depend on it, MEDIUM-LOW; ordinary physics, no new rule. (4) **P62 regression** — cutting “Understandable. But” orphaned “Again, understandable reaction.”, LOW. (5) **Ch4 latent gap** — the healer is out of usable material an hour after a cart of records arrives; canon (records work “with the grain”) resolves it and the archivist states the fit rule after the healing; TEST only. (6) **Ch2** — keep the dumplings (they carry the perfect/crappy/familiar thread to the coffee and the last word), keep the author's truck (R28); the altered neighborhood is an unledgered promise for the author to rule on. (7) **Accountability** — consistently handled through other characters and paid by Pathwell's own conduct in Ch18 (“I asked first.”); KEEP.

**DISAGREEMENTS WITH PRIOR RECORDS:** P63 F3 / EXP-0007 / P65 frame the motive gap as *why this flat*; P66 argues the missing half is *what for*, after which opportunity answers *why this flat*. P65 treats the Ch3 price's necessity as unexplained; proportion is stated four times. P62's cut was not neutral (orphaned “Again”). The repetition risk is cumulative across Ch2→Ch3 evasions, which is why EXP-0015 rejects an asked-aloud motive question (C1).

**VERIFY:** All curly-quoted manuscript strings in both new files machine-checked against the chapters at `63dd268` (173 quotes, 0 missing). Every patch passes `git apply --check`; B1+B2+B3+R1 apply together. Book-wide checker on `63dd268` vs `63dd268`+B1+B2+B3+R1: only Ch3's paragraph count (139→140) and one Ch3 rate (0.5→0.4 per 1,000) differ; no new hits. **Zero changes to `Story/Chapters/`, canon, Registry or Promise Ledger.**

**OPEN / NEXT GATE:** Author decision on R1, B3 (or C3), B2 (or C2), B1 (new interiority; author's ear) and Q-O. If any are applied, follow P64's rule: keep the 2026-10-16 reader edition frozen and version a new one for issue #3. All chapters stay **L3**.

**P66 ADDENDUM (2026-10-20, author response):** On the central finding, the author proposed Elizabeth's opening line become "What are you still doing here?" in place of "Do you mind?" (his own July line). Reviewed under R26: the change works and is the better place to raise the question (Ch1, interrupted by the thud) than the Ch3 asked-aloud option P66 had rejected; its only knock-on is that the reply "Not at all," (a later revision's addition) no longer answers anything. [EXP-0015 Candidate 0](Emergence/experiments/EXP-0015-First-Act-Motive-Hinge-Order-Staging-Page-Tear-2026-10-20.md#candidate-0--elizabeth-asks-the-question-ch1--author-proposed-2026-10-20): **B0** silent "He turned a page." (recommended: her question doesn't get his attention; the thud does) or **C0** "Reading," he said, and turned a page. B0 pairs with B1 (asked in Ch1, worked out by her at the Ch3 counter). Both patches pass `git apply --check`; B0+B1+B2+B3+R1 apply together. **Still no chapter edits:** the reply is the author's pick.

## P67, 2026-10-21: author-selected first-act edits from EXP-0015

**AUTHORITY:** [R53](Decisions.md#the-authors-rulings-for-this-revision). Asked directly which of the P66 candidates to apply, the author chose the reply C0 for his own Chapter 1 question, and all four of B1, B3, B2 and R1. The P66 review records (PR #4) were merged into `main` first, since the selections come from them.

**DO (exact, from the EXP-0015 patches, applied with `git apply`):**
1. Ch1: “She watched for a moment before interrupting. "Do you mind?"” / “"Not at all," he said, and turned a page.” → “…"What are you still doing here?"” / “"Reading," he said, and turned a page.” (author's question; reply C0)
2. Ch1: “The sugar-cookie page stayed under his palm.” → “The sugar-cookie page tore free and stayed under his palm.” (B3)
3. Ch1: “Then, "Again, understandable reaction.” → “Then, "Understandable reaction.” (R1)
4. Ch3: new paragraph after “He went back to his ledger, making ticks and carrying ones.”: “Elizabeth thought of Pathwell on her living-room floor, turning the pages of her diary like he was pricing it.” (B1)
5. Ch3: “The shopkeeper set the order on the counter and looked it over.” → “The shopkeeper turned to the pile at the far end of the counter, the one Pathwell must have built while she was out, and looked it over.” (B2)

Blobs: Ch1 `a105bc1c` → `6b063462`; Ch3 `7ac8171b` → `75296137`. No other chapter changed.

**CHECK:** The word diff against the previous blobs shows these five changes and nothing else. “Do you mind” and “Not at all,” no longer appear anywhere in the chapters. Book-wide checker before and after: only Ch3's paragraph count (139 → 140) and one Ch3 rate (0.5 → 0.4 per 1,000 words) move; no new hits. Regression controls: first line, party and notebook clue, chained-door glimpse, cookbook grab, Nana's memory, first-magic C, the marked bluff, “Ready?” / “No.” / “Perfect.”, Ch3's shopkeeper rebuke, prune and handcart all unchanged.

**READER TEST:** Per P64, the [2026-10-16 reader edition](Reader-Reports/First-Act-2026-10-16/READER-EDITION.md) stays frozen as the old stimulus. A [2026-10-21 edition](Reader-Reports/First-Act-2026-10-21/READER-EDITION.md) carries the changed text, built from the chapter files and checked against them. [Issue #3](https://github.com/BigCatMellow-Archive/Pathwell/issues/3) still points at the old edition and has no responses; whether to repoint it is the author's call.

**RECONCILE:** [Decisions R53](Decisions.md#the-authors-rulings-for-this-revision); [EXP-0015](Emergence/experiments/EXP-0015-First-Act-Motive-Hinge-Order-Staging-Page-Tear-2026-10-20.md) status; [Promise Ledger](Promise-Ledger.md) P1 and O1; [Revision Status](../../Revision-Status.md). Chapters 1 and 3 stay **L3**. Next, per the author: a fresh review of the 2026-10-15 climax and ending, Chapters 14–18.

## P68, 2026-10-21: review of the Chapter 14–18 climax and ending

**SOURCE / AUTHORITY:** The author chose this as the next work after P67: "Review the new ending, Ch14–18". `main` after P67; Chapters 14–18 read in full, with Ch4, Ch7 and Ch13 checked where a setup mattered. Built on [P54](#p54-2026-10-15-coordinated-chapter-1418-climax-and-ending-rewrite-author-authorized) and [P55](#p55-2026-10-15-informed-reader-and-voice-follow-up-not-independent-l4) rather than repeating them. An informed review by an agent that didn't write the text; not a blind read, not the author's verdict.

**DO — research only, no chapter edits:**
1. [P68 review](Emergence/CLIMAX-P68-CH14-18-REVIEW-2026-10-21.md): seven findings with counterarguments, what to protect, and the disagreements with P55.
2. [EXP-0016](Emergence/experiments/EXP-0016-Ch14-18-Climax-Candidates-2026-10-21.md): verified patches. Ch18 B1 "Mama Baga" / C1 "my brother" for "someone"; Ch14 B2 cut "Shade was one breath behind her."; Ch16 B3a and Ch17 B3b cut the closing thesis lines.
3. [Decisions Q-P](Decisions.md#open-for-the-author): does anyone at Camp learn what he confessed?

**FINDINGS:** (F1, high) P55-01's open question has an answer on the page: Mama Baga is in earshot in Ch15, and Ch4 shows her lifting the crate with "no effort in it"; naming her is a one-word change to the confession. (F2, medium, new) Shade is "one breath behind" Elizabeth at the end of Ch14 but "on the far side of the ruined brass frame" at the start of Ch15, a leftover from the pre-P54 staging. (F3, medium, new) Ch16 and Ch17 end almost every scene on a polished line, and two state the thesis in the narrator's voice. (F4, medium) The pardon risk is smaller than P55 thought, because Ch16 already has "I don't know if I forgive you." / "I'm not asking you to."; it's a reader test. (F5, low) "I kept thinking resemblance was enough," may not parse on a first read; test. (F6, low-medium, new) Nobody at Camp learns the confessed fact; Q-P. (F7) The Ch4/Ch15 "That was the choice" echo earns its repeat; keep.

**VERIFY:** Every curly-quoted manuscript line in both new files checked against the chapters (61 + EXP quotes, 0 missing). Every EXP-0016 patch passes `git apply --check`. No chapter, canon, Registry or ledger text changed.

**OPEN:** Author choices on F1 (A/B/C), F2, F3a, F3b, and Q-P. Chapters 14–18 stay **L3**.

## P69, 2026-10-21: author-selected climax cuts from EXP-0016

**AUTHORITY:** [R54](Decisions.md#the-authors-rulings-for-this-revision). Asked about the P68 findings, the author kept “someone” in the Ch18 confession, took all three cuts, and answered Q-P: the confession stays with Elizabeth.

**DO (exact, from the EXP-0016 patches, applied with `git apply`):**
1. Ch14: “Her shoulder screamed inside the sling. Shade was one breath behind her. Stansbury ran toward the archive from the other side…” → “Her shoulder screamed inside the sling. Stansbury ran toward the archive from the other side…” (B2)
2. Ch16: last line ends at “…because morning was going to require things from all of them.” Cut: “and for once Pathwell would not be the person deciding what those things were.” (B3a)
3. Ch17: ends at “Elizabeth smiled.” Cut: “Not because she knew where she wanted to go yet.” / “Because she wanted to go.” (B3b)

Blobs: Ch14 `9b1be3f7` → `da48b224`; Ch16 `f61a3870` → `b752f794`; Ch17 `1ac7d078` → `c9c6a6c6`. Ch18 unchanged (“someone” kept).

**CHECK:** The word diff shows these three cuts and nothing else. Book-wide checker before and after: Ch16 loses one uncontracted form and one "for once"; Ch17 loses one "Not…" fragment paragraph and two paragraphs; nothing new. Ch15 still opens with Shade “coming toward the fire from the far side of the ruined brass frame”, which now has no contradiction in Ch14. Ch16's restitution scene and Ch17's “The thought of going somewhere strange didn't arrive attached to somebody else's hand on the map.” still carry what the cut lines said.

**RECONCILE:** [Decisions R54](Decisions.md#the-authors-rulings-for-this-revision) and Q-P marked answered; [EXP-0016](Emergence/experiments/EXP-0016-Ch14-18-Climax-Candidates-2026-10-21.md) status; [Promise Ledger](Promise-Ledger.md) new row L18 (who learns the confession: open-deliberate); [Revision Status](../../Revision-Status.md). P68's F4 (pardon risk) and F5 (“resemblance”) remain reader-test items. Chapters 14–18 stay **L3**.

## P70, 2026-10-21: W16, W18, W19 put to the author

**AUTHORITY:** The author said "go for it" to settling the three working decisions that had waited on him since early October (W8), then answered each. Recorded as [R55](Decisions.md#the-authors-rulings-for-this-revision).

**OUTCOME:** **W18 confirmed** (Ch11 museum staging, with "You took her from me." / "She wasn't yours to take from."). **W19 confirmed** (no Ch13 tree-line talk; Ch14 carries the prediction and refusal; the two lines that talk was meant to hold are placed as ledger L16 and L17). **W16: "I dont know".** Under R36 the reviser's lean stands: keep the roadside reveal. It's the author's own draft, R39's diner revision is built on it, and reverting costs the end of Ch8 and the front half of Ch9. W16 is marked as the reviser's call, still overrulable.

**RECONCILE:** W16, W18 and W19 rows in [Decisions](Decisions.md#working-decisions) annotated; [Revision Status](../../Revision-Status.md) rows for Chapters 8, 11 and 13 updated. No chapter changed. Next: the Chapters 5–13 review.


## P71, 2026-10-21: review of Chapters 5–13

**AUTHORITY:** The author said "go for it" to settling W16, W18 and W19 and then reviewing Chapters 5–13 the same way as the ending: find what's wrong and offer small candidate fixes to pick from. No manuscript change without his pick.

**DO:** Read Chapters 5–13 in full on `main` after P70, with Ch1, Ch3 and Ch14–18 checked wherever a setup or payoff depended on them. Checked against the September assessment's chapter verdicts, the October 8 panel and P34's open "For the author" items so settled points weren't re-raised. Wrote the [P71 review](Emergence/MIDDLE-P71-CH05-13-REVIEW-2026-10-21.md) and [EXP-0017](Emergence/experiments/EXP-0017-Ch05-13-Middle-Candidates-2026-10-21.md): three cuts (B1 Ch7's closing line; B2 Ch12's "For most of the night,"; B3 a doubled "cooking wagon" in Ch13) and one question (Q1, the Ch9 diner sign, DINER or the author's draft DINNER, open since P34).

**CHECK:** All 43 manuscript quotations in the review match the chapter files. All four patches pass `git apply --check`, alone and together. The setup-to-payoff table (dagger, "Drive", "You took her from me.", Shade's hand, pockets and the queen, the coffee, "He lies") was checked in both directions.

**OUTCOME:** No structural problem found, and nothing argues for reversing an author decision. Kept with reasons: the Ch5 "I don't lie" beat (the panel read it as intended), W16, the Ch10 "Camp" order (the choice is still hers), Shade's escalating hand in Ch13, the Ch6–7 fragment stacks, the Ch5 second-person aside. "Fair." and L15 stay on watch.

**RECONCILE:** [Revision Status](../../Revision-Status.md) manuscript note added and its "What's next" list rewritten (the old list dated from October 1 and is in git history). [Emergence index](Emergence/INDEX.md) entry added for P68 and P71. No chapter changed; all still L3.

## P72, 2026-10-21: author-selected middle cuts from EXP-0017

**AUTHORITY:** The author picked from the P71 candidates: all three cuts, and "Keep DINER" on the diner sign. Recorded as [R56](Decisions.md#the-authors-rulings-for-this-revision).

**DO:** Applied [EXP-0017](Emergence/experiments/EXP-0017-Ch05-13-Middle-Candidates-2026-10-21.md) B1, B2 and B3 with `git apply`, unchanged. Ch7 now ends "…then a long empty stretch of road with nothing coming the other way." Ch12 reads "The diary had been one of the few things that was unequivocally hers." Ch13's list reads "a woman shaking flour from a cloth, a dog asleep under the cooking wagon." Ch9 not touched.

**CHECK:** The diff is three lines across three chapters, cuts only. No other text moved.

**RECONCILE:** EXP-0017 status, the P71 review header, [Revision Status](../../Revision-Status.md) (manuscript note; "What's next" item 1 marked done) and Decisions R56. P34's diner-sign question is closed by R56. Chapters 7, 12 and 13 still L3.

## P73, 2026-10-22: the external checklist, reconciled with the records

**AUTHORITY:** The author asked for the revisions from an external three-read review and its chapter-by-chapter checklist (made outside this repository), chose scope "Everything", "Keep the scar" and "Card says two", then asked that this repository's rules be followed. Recorded as [R57](Decisions.md#the-authors-rulings-for-this-revision).

**THINK:** A first draft of this pass applied about forty changes to an exported copy of the manuscript, without the records. Checked against them, many broke rulings: R21, R29, R31, R35, R39, R47, R48/R53, Q136 and the glossary's "Leo" rule. That draft is discarded and never reached the chapters. The corrected work separates what the author decided directly (applied) from what needs his pick (candidates) and what the records rule out (withdrawn).

**DO:** Ch12's card reads `TWO PAGES USED — SUGAR COOKIES, CHICKEN & DUMPLINGS`, and Ch15's echo reads "Two pages used." (author pick; overrides P23/P38, with push-back noted in EXP-0018). Ch18's "The old scratch was long gone." becomes "Elizabeth looked at the thin scar between her thumb and wrist." (author pick; matches Ch3). Ch18's "the Shopkeeper" is lowercased. Everything else is in [EXP-0018](Emergence/experiments/EXP-0018-Whole-Book-Checklist-Candidates-2026-10-22.md): eleven B candidates (cuts and continuity), four flagged C candidates (new text), and fifteen withdrawn items with the ruling that rules each out.

**CHECK:** The diff is four lines in three chapters. Small-edit path ([Line-Editing Protocol §7](../Sunday-Morning/Line-Editing-Protocol.md)): each line was read in its paragraph; the scar matches Ch3's placement and wording; ledger L4 is still paid ("He remembers winning."); the card now agrees with the archivist's two marks in Ch4. The routine (D23):

1. Tone guardrails: done. No tonal change; the pass adds nothing a reader would brace for.
2. Shapes before sentences: not applicable. No opening, engine, resolution or ending changed.
3. Checker: done. Output identical before and after.
4. Scene diagnostic: not applicable. No scene's movement changed.
5. Fresh check: skipped. Four mechanical lines, all on the author's direct answers, no new cautious-category text in the chapters. EXP-0018's C candidates need one if he adopts any.
6. Reader protocol: skipped, for the same reason. A cold reader is due if B or C candidates are adopted.
7. Replacement tic: done for the candidates. Every B is a cut, not a substitute move.
8. Deliberate ambiguity: done. The withdrawn list keeps R54/Q-P, Q136 and the open "who asked for help" (08-22 §4) as they are.
9. Change notes from the diff: done (above).
10. Tenth seat: not applicable. It doesn't fire on line edits or the author's rulings.

The light Sunday touch: not applicable.

**RECONCILE:** Decisions R57; EXP-0018 opened; [Revision Status](../../Revision-Status.md) (manuscript note; "What's next"); [Emergence index](Emergence/INDEX.md). Chapters 12, 15 and 18 still L3. **Found, not fixed:** `Story/Pathwell.txt` doesn't match an assembly of the current chapters (about 300 lines differ), so it predates at least one earlier pass. Left alone here; re-run `Story/assemble_manuscript.py` in its own commit.

## P74, 2026-10-22: a one-page brief in front of the method

**AUTHORITY:** The author, on the suggestion of a one-page brief to load before any chapter edit: "go for it".

**DO:** New [Before you touch a chapter](Before-You-Touch-A-Chapter.md): seventeen rulings a pass is most likely to undo, each with its owner; who writes what; how a change gets in. It owns nothing new (MAPS_L: link, don't restate). Linked first in this folder's README table and in the repository README.

**CHECK:** Every line was checked against its owner row (R9, R11, R17, R21, R26, R27, R29–R31, R35, R36, R42, R45–R48, R53, R54; the lock tables; the glossary). No chapter changed. Routine (D23): steps 1–9 not applicable (no prose changed); tenth seat not applicable.

**RECONCILE:** README tables. Chapters unchanged.

## P75, 2026-10-22: agent instructions point to the Sunday notes

**AUTHORITY:** The author: "Can we make sure the Agent instructions point to the sunday notes".

**DO:** The repository had no agent instructions. New `AGENTS.md` at the root: read first, every session ([Before you touch a chapter](Before-You-Touch-A-Chapter.md), the [Sunday Morning notes](../Sunday-Morning/README.md), this folder's [README](README.md)); which Sunday note to open for which job; the working rules and the checker command. New `CLAUDE.md` imports it, so Claude Code and other tools read one file. Linked from the repository README.

**CHECK:** Every relative link in both pages resolves. No chapter changed. Routine (D23): not applicable.

## P76, 2026-10-22: AGENTS.md rebuilt as the operating contract

**AUTHORITY:** The author: "we need to build the agent instructions more, since theres a lot more going on than just Sunday notes, make sure to use https://github.com/BigCatMellow/MAPS_Lean/wiki as a guide as needed".

**DO:** `AGENTS.md` rewritten on the MAPS_L wiki's pattern at method-only depth, and on the shape of MAPS_Lean's own AGENTS.md. It covers:
- authority (this file governs agent conduct; the revision README's order governs the story; what is never authority);
- who owns what (the author, the reviser, bounded helpers; delegation hands off the work, never the ownership);
- the reading budget;
- what needs the author (the boundary crossings) and what doesn't;
- the loop and its stop conditions;
- which method page for which job;
- where records go (EXP candidates, reviews, IDEA/INS, one owner, one current version, UNKNOWN kept open);
- independence;
- the report format;
- house rules.

It adds no story rules; every line links to its owner. `CLAUDE.md` still imports it.

**CHECK:** Every relative link and anchor resolves. No chapter changed. Routine (D23): not applicable.

## P77, 2026-10-22: EXP-0018 leans applied after a fresh check

**AUTHORITY:** [R58](Decisions.md#the-authors-rulings-for-this-revision): "i authorize you to this time do what you need to do push the PR". Delivered as a pull request, not a push to main.

**DO:**
- **Prose (as finally applied):**
  - Ch5 adds "Thumper's paw print was in there somewhere." (C2).
  - Ch7 drops "Elizabeth waited." (B3).
  - Ch10 drops "Pathwell went still." before "No." (B1, first cut only), and "That wasn't the question." becomes "Would you try?" (B2, his "No. I would not try." kept).
  - Ch11 and Ch16 each drop "Pathwell went still." (B4, B6).
  - Ch13 drops "Shade went completely still." (B5), and the pocketed-card slip becomes `"He keeps acting like you're something he can hold onto," Shade said.` (B11).
  - Ch15 drops "Rain on canvas." and "Bread." (B8).
  - Ch17 drops "Elizabeth waited." after the Hearts game (B7).
  - Ch18 names Boots twice and "It allowed this" becomes "He allowed this" (B10).
- **Not applied:** B9 (cabinets) and C1, C3, C4.
- **Records:**
  - The revision README's "Where things stand" now points to Revision Status and the Pass Log instead of a 10-15 snapshot.
  - Its inventory no longer says the chapters last changed 08-28.
  - Plan.md's status says the plan has been overtaken by the chapter passes.
  - `Story/Pathwell.txt` regenerated; it had lagged the chapters.
  - Ledger L11 records the Ch5 Thumper plant.
  - The Registry's "goes still" row is updated.
  - EXP-0018's status is updated, and its count is corrected (12 → 8 on the checker's pattern, not "10 to 6").

**CHECK:** Routine (D23):

1. **Targets first: done.** No ruling or lock keeps any cut text. The fresh check searched Decisions, the ledger, the glossary, the Registry and Non-Negotiable Scenes. Ch13's "holding onto" line stays (R37, Q82); Ch11's "I don't need to be rescued" stays.
2. **Shapes: not applicable.** No opening, engine or ending changed.
3. **Checker: done.** The "goes still" watch pattern drops from 12 to 8; nothing else moved but paragraph counts.
4. **Scene diagnostic: done, by the fresh check's reading.** No scene's movement changed.
5. **Fresh check: done,** by a helper that didn't write the patches. Ten hunks KEEP. Three REVISE (Ch10 ×2, Ch13), all applied: the first Ch10 cut was restored rather than merged, because a merge would have had Pathwell correct himself unprompted, and Non-Negotiable 6 has Elizabeth make him say it. One REVERT (the Ch17 cabinets setup), applied. Outside the hunks it found the Ch18 pronoun (fixed), the stale Registry row (fixed), the missing authorization record (R58), and two older repeats it didn't cause (Ch11 "He waited."; Ch10's two remaining "Elizabeth waited."), left as they are.
6. **Reader protocol: skipped.** Every change is a cut or a one-line plain edit, and the fresh check read each in context. A cold reader is still owed for L4.
7. **Replacement tic: done.** The fresh check caught two (a fifth bare "No." in Ch10; "After a while he said" four lines under "After a moment Shade added" in Ch13), and both are fixed.
8. **Deliberate ambiguity: done.** Untouched.
9. **Change notes from the diff: done** (above).
10. **Tenth seat: not applicable.** These are line edits.

**RECONCILE:** R58, EXP-0018, the Registry, the ledger, [Revision Status](../../Revision-Status.md) and the [Emergence index](Emergence/INDEX.md). Chapters still L3.

## P78, 2026-10-22: the Sunday Morning tone written into the notes

**AUTHORITY:** The author, on what the Sunday stories were for: "the goal of the sunday stories was a more fun tone … Based off my experience / enjoyment with what I called 'Sunday Morning Movies'". Then: "Can we add the tone to the sunday morning stuff too?" Recorded as Sunday Morning [D27](../Sunday-Morning/Decisions.md#standing-rulings).

**DO:**
- The Sunday Morning README opens with a new "What it's for": the stories are meant to be fun; the name comes from his "Sunday Morning Movies"; the method protects the feeling, and the feeling wins over a check (D9); a soft landing isn't a repeated beat to trim. It also gets a router row.
- The tone guardrails link back to it.
- `AGENTS.md` names R24 (Pathwell keeps some of the tone) beside the Sunday notes.
- The brief adds "don't cut a soft landing as a repeated beat".

These edits are in this repository's copy only (D18); the 10 Kings copy doesn't have them yet.

**CHECK:** Links and anchors resolve. No chapter changed. Routine (D23): not applicable. The README quotes only his words for "Sunday Morning Movies" and adds no description he didn't give.

## P79, 2026-10-22: the author's "Sunday Morning Movies" definition added as a source

**AUTHORITY:** The author supplied two files "I had worked on to define the concept": his own definition of Sunday Morning Movies, and the earlier conversation it grew out of. Both are recorded under Sunday Morning [D27](../Sunday-Morning/Decisions.md#standing-rulings).

**DO:**
- New source [Sunday Morning Movies](../Sunday-Morning/Sources/Sunday-Morning-Movies.md): his definition, word for word. Headings and bullets were added for reading; a script confirmed the words and their order are unchanged.
- New evidence page [the first conversation](../Sunday-Morning/Sources/Sunday-Morning-Movies-Conversation.md): kept verbatim, marked not authority (it's another assistant's reply; its figures and links aren't checked here).
- The Sunday Morning README's "What it's for" now quotes his short definition and his test ("Would I happily leave this on if I discovered it halfway through on cable?"), with a row in the notes table and the router.
- D27 links the sources.

**CHECK:** Links and anchors resolve. No chapter changed. Routine (D23): not applicable.

## P80, 2026-10-22: two reads through the Sunday Morning lens

**AUTHORITY:** The author: "would it be worth reading the story again with these new notes in mind and seeing what revisions need to be made?", then "yes" to running two independent reads and putting the results in a candidate page.

**DO:** Two helpers that didn't write the text read the book on this branch, after P79.
- The [lens read](Reader-Reports/Sunday-Lens-2026-10-22/LENS-Ch01-18.md) was informed: all 18 chapters, against the author's Sunday Morning Movies definition, R24, the Thesis and the brief.
- The [drop-in read](Reader-Reports/Sunday-Lens-2026-10-22/DROP-IN-Ch09-18.md) was blind: given only Chapters 9–18, copied out of the repository.

Both reports are saved verbatim. The reviser checked every finding against the chapters and the rulings, and built [EXP-0019](Emergence/experiments/EXP-0019-Sunday-Lens-Candidates-2026-10-22.md): four cuts (B1–B4, each leaned "take") and five questions (Q1–Q5). **No chapter changed.**

**CHECK:** Every cited line was checked against the chapter text, and three counts were corrected. Every patch passes `git apply --check`, alone and all four together. Routine (D23):
- Steps 1–9 are not applicable to the chapters, since no prose changed.
- The two reads are the independent check, steps 5 and 6. The drop-in read is the first blind read of the back half since 10-06. It isn't the whole-book blind read L4 needs.
- Tenth seat: not applicable (no verdict that later passes will treat as settled).

**FINDINGS:**
- **The book passes the author's test.** The blind reader would have kept reading from Ch9 at every checkpoint.
- **The R24 balance holds.**
- **The voice:** both readers, independently, found one shared deadpan spoken by too many characters. B1 and B2 thin it; Q1 asks whether the healer goes back to plain (R33).

**RECONCILE:** [Revision Status](../../Revision-Status.md), the [Emergence index](Emergence/INDEX.md). Chapters still L3.

## P81, 2026-10-22: EXP-0019 leans applied

**AUTHORITY:** The author: "I trust your leans". Recorded as [R59](Decisions.md#the-authors-rulings-for-this-revision).

**DO:** Applied EXP-0019 B1–B4 with `git apply`, unchanged:
- Ch16: "Can I check it?"
- Ch18: the shopkeeper's "Occupationally." cut.
- Ch14: "…spreading from Pathwell's shadow."
- Ch15: "outside the bar".

`Story/Pathwell.txt` regenerated. EXP-0019 now lists the healer's dry lines for the author to rewrite (Q1). No new text was written.

**CHECK:** Small-edit path; all four are cuts or a one-word change, and both readers in P80 read them in context. The checker moved only paragraph counts. Routine (D23):
- Steps 1, 3 and 9: done.
- Steps 2, 4 and 8: not applicable.
- Step 5 (fresh check): covered by P80's two readers, who proposed these exact changes.
- Step 6 (reader): skipped. The first-half read starts next, on this text.
- Step 7 (replacement tic): done; no substitute moves.
- Tenth seat: not applicable.

**RECONCILE:** R59, EXP-0019, [Revision Status](../../Revision-Status.md).

## P82, 2026-10-22: the first half through the Sunday Morning lens

**AUTHORITY:** The author: "read the first half of the story now with the sunday tone in mind".

**DO:** Two helpers that didn't write the text read Chapters 1–9 after P81.
- The [blind cold read](Reader-Reports/Sunday-Lens-First-Half-2026-10-22/BLIND-Ch01-09.md) got only the nine chapters, copied out of the repository.
- The [lens read](Reader-Reports/Sunday-Lens-First-Half-2026-10-22/LENS-Ch01-09.md) went scene by scene with the rulings. It disclosed seeing a few one-line snippets of the earlier lens reports, which it didn't open; this is recorded in its report.

Both reports are saved verbatim. The reviser checked every cited line against the chapters and checked authorship against the voice benchmark, then built [EXP-0020](Emergence/experiments/EXP-0020-First-Half-Sunday-Lens-Candidates-2026-10-22.md): four cuts (B1–B4, none in the author's own lines) and two questions. **No chapter changed.**

**CHECK:** Every patch passes `git apply --check`, alone and together. Routine (D23):
- Steps 1–9 are not applicable to the chapters (no prose changed).
- The two reads are steps 5 and 6.
- The blind read is the first blind read of Ch1–9 since the October edits. It isn't the whole-book blind read L4 needs.
- Tenth seat: not applicable.

**FINDINGS:**
- The first half passes the author's test: the blind reader said "keep reading" after every chapter.
- Camp (Ch4) and the bar (Ch6) are the half's Sunday heart.
- As in the back half, both readers found one corrective deadpan shared by too many speakers. Stansbury after Ch5 is the clearest case, and Elizabeth picks it up in Ch7–9.

**RECONCILE:** [Revision Status](../../Revision-Status.md), the [Emergence index](Emergence/INDEX.md). Chapters still L3.

## P83, 2026-10-22: EXP-0020 leans applied

**AUTHORITY:** The author: "go for it". Recorded as [R60](Decisions.md#the-authors-rulings-for-this-revision).

**DO:** Applied EXP-0020 B1–B3 unchanged:
- Ch4: "He nodded. "This wheel is new." "Newer," he amended. "Relatively."" is now one paragraph.
- Ch9: Shade's first "Fair." cut.
- Ch8: "That wasn't my question." cut.

B4 was corrected after the reviser read it in context: the plain cut left "this one passed too" with nothing to refer to, so Ch5 now reads "The pint-sized siege of chaos raged around them, then passed." The B4 patch and the EXP page are updated to match. `Story/Pathwell.txt` regenerated.

**CHECK:** Each line read in its paragraph. The checker moved one watch count (5 → 4) and paragraph counts. Routine (D23):
- Steps 1, 3, 7 and 9: done.
- Steps 2, 4 and 8: not applicable.
- Steps 5 and 6: covered by P82's two readers, who proposed these changes. The B4 correction is a reviser line edit, recorded here so a later fresh check can test it.
- Tenth seat: not applicable.

**RECONCILE:** R60, EXP-0020, [Revision Status](../../Revision-Status.md). Q1 and Q2 stay with the author.

## P84, 2026-10-22: the house deadpan, candidate lines (EXP-0021)

**AUTHORITY:** The author: "lets get back to the actual work of improving the story". The reviser took the open voice items from R59 and R60 (the healer back to plain, the Ch15 turnips line, Stansbury's Ch6 and Elizabeth's Ch8 "No. [correction]." lines, one trace of Stansbury's Ch5 vanity), because they are the convergent finding of both Sunday-lens passes.

**DO:** [EXP-0021](Emergence/experiments/EXP-0021-House-Deadpan-Candidate-Lines-2026-10-22.md): 17 patches over 12 spots, as plain scaffolds for the author to pick, rewrite or refuse (who writes what). **No chapter changed.** The healer options take her back to her Ch4 register and keep Elizabeth's jokes wherever they can answer a plain line. The Stansbury options come from the author's own drafts (the fish, dusting himself off).

**CHECK:** Every patch passes `git apply --check` alone, and the lean set applies together. An independent helper read each option in its scene against the author's Ch4–5 drafts, without the leans ([report](Reader-Reports/Fresh-Check-EXP-0021-2026-10-22.md)). It agreed on nine spots and changed three leans (H1 keep, S1a with S2, T1b). It also found two more deadpan "No." lines (Ch10:133, Ch18:233) and a third "the question" line (Ch12:187), all listed and not drafted. Routine (D23):
- Steps 1, 3, 7 and 9: done.
- Steps 2, 4 and 8: not applicable (no chapter text changed).
- Step 5: done, as the fresh check above.
- Step 6 (a cold read): not applicable until the author picks.
- Tenth seat: not applicable.

**Addendum:** the author asked whether the [quote and character voice reference](../Story_Files/quote_and_character_voice_reference.md) was being used. It wasn't: the reviser had searched it for the characters' names, found none, and not read it. Read in full and recorded on the EXP page; one option added from it (S1c). [AGENTS.md](../../AGENTS.md) §6 now sends any joke, emotional line or narrator comment to the voice benchmark first and then to this bank.

**RECONCILE:** EXP-0021; EXP-0019's B1 row marked superseded by R59; [Emergence index](Emergence/INDEX.md); [Revision Status](../../Revision-Status.md).

## P85, 2026-10-22: resource audit

**AUTHORITY:** The author: "are we pulling inspiration from that? If we arent, are we using all the resources in the repo properly?"

**DO:** [Resource audit](Emergence/RESOURCE-AUDIT-2026-10-22.md). Every tracked resource was checked for whether the entry pages reach it and whether passes cite it. Then the under-used pages were read. Finding: the records are linked, but passes have used them for constraints far more than for aim. The author's [voice guide](../Sunday-Morning/Sources/Voice-Guide.md) has never been cited by a pass, and the [reading list](../../Reading-List.md) (Pratchett first) wasn't reachable from AGENTS.md. Fixed where agents look:
- AGENTS.md §6: the drafting row now starts with the voice guide and his line notes. The joke and narrator row now goes aim (voice guide, reading list), then his drafts, then the quote bank.
- Two stale notes marked: the Ch1 line-notes page ("nothing applied") and the narrator register (pointed at archived guides).
- A committed `.pyc` removed, and `.gitignore` added.

EXP-0021 rechecked against the voice guide. S1c is now leaned against ("not every line should be quotable"), and the guide's dialogue section is recorded as the way into any "No. [correction]." rewrite.

**CHECK:** Every link on the changed pages resolves. No chapter text changed, so the checker and readers aren't needed (D23 steps 2, 4, 5, 6 and 8 not applicable; 1, 3, 7 and 9 done).

**OPEN, for the author:** some of his own Ch1 line notes from 2026-10-08 (R38) are still waiting: the first "Perfect." → "Good… that's good.", the second "low tide" cue, the felt cookbook panic, the party/light-switch deletion, the stammer and the "Huh" blocking. They're listed in the audit.

**RECONCILE:** [Emergence index](Emergence/INDEX.md); [Revision Status](../../Revision-Status.md).

## P86, 2026-10-22: the author's own Ch1 line notes

**AUTHORITY:** The author: "go for it", on the lean to apply his open 2026-10-08 Ch1 notes as he wrote them unless a later ruling blocks one. Recorded as [R61](Decisions.md#the-authors-rulings-for-this-revision).

**DO:**
- Ch1: nine of his notes applied in his own words (listed in R61). The bookend lock keeps the final "Perfect.". ¶15 no longer has a line to apply to.
- The four notes that ask for new writing (¶65 low tide, ¶69 panic, ¶73 "more poetic", ¶125 blocking) are candidates in [EXP-0022](Emergence/experiments/EXP-0022-Ch01-Author-Note-Requests-2026-10-22.md), with leans, aimed by his voice guide.
- The [R38 disposition](Emergence/CHAPTER-01-R38-CURRENT-DISPOSITION-2026-10-16.md) marked ¶71 "intent preserved", but his note changes "here" to "there", and that hadn't been applied. It is now.
- `Story/Pathwell.txt` regenerated.

**CHECK:** The checker runs clean (exit 0). A fresh check read the applied wording against his verbatim notes and found every change faithful. It also found a third mechanic ("He waved it off." as its own sentence), now named in R61, and two notes nobody had tracked (¶39 more detail, ¶167 "his attention"), now EXP-0022 C5 and C6. Its opinions, for the author: the ¶73 memory line is now a verbless fragment; "she thought that he had left" leaves the paragraph's past perfect; the final "Perfect." now rests on the bookend rather than an echo inside the chapter. Routine (D23): steps 1, 3, 7 and 9 done; 2 and 4 done (checker, ledger: "Perfect." R1 bookend intact); 5 done (fresh check); 6 (cold read) waits for the whole-book review (P87); 8 not applicable; tenth seat not applicable.

**RECONCILE:** R61; EXP-0022; [Revision Status](../../Revision-Status.md).

## P87, 2026-10-22/23: the web, and the whole book against the repository's resources

**AUTHORITY:** The author: "we need to then review the entire story using the resources in the repo, and mkae the agent notes make note of it all, that should have been part of the spiderweb from MAPSL".

**SOURCES:** *Rulings:* Decisions, Before you touch a chapter, Author-Notes. *Targets:* Thesis, Non-Negotiable Scenes, Writing Principles, the contract matrix, INS-0001/IDEA-0001. *Aim:* the voice guide (whole), the Sunday Morning Movies definition, the reading list, pathwell_prose_voice, the narrator register, the voice benchmark (Ch1–7), the quote bank, forbidden_patterns, Writing against sameness, AI tells. *World:* canon, the world and character bibles, glossary, Registry, Promise Ledger. *Evidence:* the 2026-10-22 Sunday lens reports and blind reads, the cold read, the panel. *Method:* MAPS_L's Spiderweb playbook and scanner.

**DO:**
- **The web** ([AGENTS.md §8](../../AGENTS.md#8-the-web)): MAPS_L's Spiderweb rule, "nothing durable is an island". Resources are opened by role, and Aim is required for any writing pass. Every Pass Log entry now carries a SOURCES line. His own words come first. Stale statuses get dated current dispositions. The [inventory](README.md#inventory-of-existing-process-records) is now the full map, with when to open each resource. The scanner is ported to [`tools/check_spiderweb.py`](tools/check_spiderweb.py), where links to folders and folder READMEs count as edges: 349 files, no findings. Three stale EXP statuses (0008, 0012, 0014) got current dispositions.
- **The review:** three independent reviewers each read all 18 chapters through one role (aim, targets, world): [reports](Reader-Reports/Whole-Book-Resources-2026-10-22/). They're reconciled in [EXP-0023](Emergence/experiments/EXP-0023-Whole-Book-Resource-Review-Candidates-2026-10-23.md):
  - 19 cuts where the book explains itself;
  - 5 lines where reviewers disagree with earlier readers;
  - 4 continuity fixes;
  - 8 items for his pen;
  - partial options A3b, A8b and A17b.
  **No chapter changed.**
- **Records pass**, from the world and targets reviewers. Dated current-disposition notes on stale lines in canon, the world and character bibles (including Stansbury's turn), the glossary, the contract matrix, Writing Principles and three Decisions lock rows. The ledger's P2, O6, R3, R7, R12, R17, L1 and L11 corrected, and L19 (the healed young woman), L20 (the gold chain) and L21 (Q-O) added. The Registry gains Ken, and its open letters and three final lines are corrected.

**CHECK:**
- An independent [fresh check](Reader-Reports/Whole-Book-Resources-2026-10-22/FRESH-CHECK-EXP-0023.md) applied the leans and read each in context. Four leans changed: A8 → A8b, A14 keep, A15 keep, A17 → A17b.
- Every patch applies, and the lean set applies together. The checker runs clean on it. The spiderweb finds nothing.
- Routine (D23): steps 1, 2, 4, 5, 6 and 9 done; 3 done (checker); 7 done (open-on-purpose items left alone: marked, the prune, the blob sparing Pathwell); 8 done (this entry, ledger, status). Tenth seat: not applicable.

**RECONCILE:** EXP-0023; [Emergence index](Emergence/INDEX.md); [Revision Status](../../Revision-Status.md).
