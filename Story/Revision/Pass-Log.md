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
