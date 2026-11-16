# High-effort session brief

## Status

**Active.** Written 2026-11-16 ([P119](Pass-Log.md#p119-2026-11-16-a-brief-for-a-high-effort-session)) for a fresh session on a stronger model at high effort. The point is to spend that effort on judgment, not on discovery. Everything a session would otherwise have to dig up is either here or one link away. Run **one task per session**, and paste that task's starting prompt from the end of this page.

Rulings and records still own their facts: [Before you touch a chapter](Before-You-Touch-A-Chapter.md), [Decisions](Decisions.md) and the [Pass Log](Pass-Log.md). This page only routes to them. If this page and an owner disagree, the owner wins; fix this page in the same change.

## What's true right now

Don't re-verify any of this. It was checked on 2026-11-16 at commit `cfe45e8`.

| Version | Where | Words | State |
| --- | --- | --- | --- |
| **The manuscript** | `Story/Chapters/Chapter_01–18.txt` | 47k | bt 7274's book under revision; the last pass was P104–P115. Every edit needs his approval first. |
| **The Garden** | `Story/Revision/Experiments/Garden/` | 55k | Sunday Morning trial, regrown from fresh soil (P113–P115). The growth record is `Growth-Log.md`. |
| **The Wild Garden** | `Story/Revision/Experiments/Wild/` | 39k | Grown without opening either other version, with beats free to change, then tended twice (P116–P118). bt 7274 is test-reading the epub. |

- **Wild's own records:** [Growth-Notes.md](Experiments/Wild/Growth-Notes.md) lists every changed beat with the reason, plus the candidate ideas and their costs. Read it instead of re-deriving what Wild did.
- **Overlap:** Wild shares 0.4% of its six-word phrases with the manuscript and 2.0% with the Garden. Transplanting has been checked; don't check it again.
- **Harada:** 22 errors, all pre-existing. A change that leaves it at 22 hasn't broken it.

### Known problems in Wild, already diagnosed

1. **US/UK drift.** The manuscript is American (apartment, sidewalk, hood). Wild drifted British: flat, pavement, bonnet, fortnight, launderette, nan, Biscuit. A word count gives 43 US to 60 UK, against 49 to 27 in the manuscript. Anything harvested into the manuscript must be Americanized.
2. **Ch3 is 3.3k words,** long for Sunday Morning.
3. **Narrator simile density** ("the way you'd…", "as though") and a high rate of short paragraphs. Some is voice and some is tic. Telling them apart is bt 7274's call.
4. **The back half is gentler.** There's no fire and no death, so the stakes sit in what's lost rather than in who.
5. **The Shade-POV section in Ch15** (present tense) may jar.

### Wild against the locks

These are the places where Wild **breaks a ruling or lock** in [Before you touch a chapter](Before-You-Touch-A-Chapter.md). None of them can be harvested without a new ruling from bt 7274.

| Wild does | Lock it breaks |
| --- | --- |
| Elizabeth says "Ready?" and Pathwell says "No." (speakers reversed) | R9: the last three lines |
| No capture, no withheld call, no Milo; the rejoining is refused, and the dagger cuts the pull | R45, R46: the climax's shape |
| A Ch18 confession with anger and the landing, and no browsing hour | R47: Version C |
| Names Wren as the one who asked for help | lock 08-22 §4: stays open |
| Ch18 explains why he picked her (he'd read four years of her carrying things) | R48, R53: already answered by design |
| Gary, the rota, going back to work | R35(2), Q136: her work life stays open |
| Elizabeth uses the foam dagger to cut the pull | Locks: "no magic for Elizabeth". The foam weapons are in manuscript Ch5–Ch15 but not in the world bible; check how the manuscript lets her use one before calling this a breach |

Wild ideas that touch **no** lock (from the Growth Notes):
- the "sorry" habit, with Mrs. Okafor as its mirror;
- ASK BEFORE USING and "Can I?" / "No." / "Right.";
- Kevin's bear and BY PATHWELL;
- Pathwell can't play anything he might lose, and dominoes;
- the healer's "Is there anything you want first?";
- the gray page rewritten in her own hand;
- the crossword answers;
- the duck pond;
- SUDS and the dryer;
- Wren's letter (the letter works only if the asker is named, so it falls under the 08-22 §4 row);
- the insurance list;
- the recipe bookends;
- the object chapter titles.

### Open items waiting on bt 7274

These are not for the model to decide.

- **Q-O**, Ch2's changed neighborhood: displacement or magic? ([Decisions, open](Decisions.md#open-for-the-author))
- **Ch5 "He lies, you know."** Stansbury's line, and its echo at line 291, read as mind-reading. It was asked in P104 and is still unanswered.
- **Nana's name and Elizabeth's family name** stay off the page unless he says otherwise (Pass Log, line 1258).
- **The full-book `PATHWELL_11.02.docx`** has the old em-dash quote bug. Rebuild it with `build_book.py` if he wants a fresh copy.

## Reading budget: what to read and what to skip

**Read:**
- this page;
- [Before you touch a chapter](Before-You-Touch-A-Chapter.md) (1 page);
- the task's named inputs.

**Search, don't read:**
- `Pass-Log.md` (3,600 lines). Grep for a P-number or a phrase.
- `Decisions.md`. Jump to the R-row you need.

**Skip unless the task names it:**
- `Archive/`, `Council/`, `Emergence/` and `Reader-Reports/` (the panel CSVs);
- `Currency-Audit*`, `Voice-Benchmark/`, `Voice-Pass/` and `Harada/` internals;
- `Story/ideas`, `Story/insights` and `Story/Interview`.

They're history, and the rulings have already been distilled into the R-rows.

## Standing rules

- **bt 7274's name.** Never write his name anywhere in the repo, in files, filenames or commits. He is "bt 7274".
- **Commit trailers**, on every commit:
  ```
  Co-Authored-By: <model> <noreply@anthropic.com>
  Claude-Session: <session url>
  ```
  Push to `main`.
- **`Story/Chapters/` is his.** Show every change to it as a diff and wait for his yes before you commit. `Experiments/` can be committed freely.
- **Reader notes are diagnoses, not prescriptions.** Report what's wrong and why. Offer fixes as options.
- **No "Recommended" on taste calls.** Give your lean, labelled as a lean.
- **He owns** jokes, emotional lines, character-defining dialogue, metaphors, narrator commentary and sentence rhythm. You may propose in those categories; mark each proposal and give an alternative.
- **Chapter file format:** the first line is the title. One blank line between paragraphs; 3+ newlines for a scene break. Straight quotes. No asterisks.
- **Chat replies stay brief.** The work goes in files.
- **Records:** add a Pass Log entry `P120+` for each task (AUTHORITY / DO / CHECKS) and an R-row in Decisions for each ruling he gives.

## Tools

These are already built. See [Experiments/tools](Experiments/tools/README.md).

- `build_book.py`: docx and/or epub from any chapter folder.
- `overlap.py`: shared-phrase check, showing draft-side text only.
- The freshness checker, `assemble_manuscript.py` and the Harada check.

## The tasks, in order

Task 0 is bt 7274's own: read the Wild epub and jot down what landed and what didn't. Task 1 runs better with those notes, but it doesn't need them.

### Task 1. The harvest map (highest value; this is what the effort is for)

**Goal:** a single decision document that says, chapter by chapter, which ideas from the Garden and the Wild Garden are worth grafting into the manuscript, what each graft would cost, and which need a new ruling.

**Read:**
- all 18 manuscript chapters, in full;
- `Wild/Growth-Notes.md`;
- `Garden/Growth-Log.md`;
- then **only** the experiment passages that the Growth Notes and Log point to.

Don't read either experiment cover to cover.

**Method:** for each candidate idea:
1. Name the source (Garden or Wild) and the chapter.
2. Name the manuscript spot it would graft into, by chapter and nearby line.
3. Name what it does for the book's goals: control is not competence; Elizabeth matters without power; Shade is a person; Sunday Morning, "You do not need to brace yourself."
4. Say what it would displace.
5. List the locks it touches, using the table above.
6. Give the graft size: a word, a line, a beat or a scene.
7. Give your lean, labelled as a lean.

Group the ideas into three sets:
- **free grafts**, which touch no lock and are small;
- **grafts that need a ruling**;
- **structural alternatives**, which are whole-shape choices such as the Wild climax. Present these as side-by-side options for bt 7274, not as edits.

**Output:** `Story/Revision/Harvest-Map-<date>.md`. It's an experiment record, so commit it. Don't touch any chapter.

**Done when:**
- every Growth-Notes and Growth-Log idea has a row or a one-line reason it was dropped;
- every lock conflict is named;
- the ruling questions can be answered quickly: a few options each, no "Recommended";
- the map is readable in 15 minutes.

**Stop and hand back** with a five-line summary in chat and the ruling questions.

### Task 2. Graft what he approved

Only run this after he has answered Task 1's questions.

**Goal:** apply the approved grafts to `Story/Chapters/`.

**Read:**
- the Harvest Map with his rulings;
- the target chapters;
- the R-rows those grafts touch.

**Method:**
- Write in his voice, using his pre-August Chapters 1–2 as the benchmark (W9, W14). Don't smooth his lines.
- Americanize anything that came from Wild.
- New text in the categories he owns gets marked, with an alternative.
- Run `assemble_manuscript.py` and the Harada check. It should stay at 22 errors, or the errors you add should be fixes to the chart's quotes.

**Output:** diffs shown in chat, or as a docx edit copy, **before** you commit. Then commit with an R-row and a Pass Log entry.

**Done when** he has approved the diffs and the records are written.

### Task 3. A second growth of the Wild Garden (experiment; can run any time)

**Goal:** fix known problems 1–5 inside Wild, so that it's a fair comparison read.

**Read:**
- `Wild/` in full;
- the Growth Notes.

Don't open the manuscript or the Garden. The fresh-soil rule still holds.

**Method:**
- Americanize it.
- Bring Ch3 under about 2.5k words without cutting any seed that later chapters use. Grep for each seed before you cut it.
- Thin the similes and fragments only where they're tics, and list every cut you're unsure of.
- Decide whether the back half needs one real reversal, so that it bends without breaking.
- Write a third tending section in the Growth Notes.

**Output:** commit to `Wild/`. Run `build_book.py --docx --epub` and send the epub.

**Done when:**
- `overlap.py` against the manuscript stays under 1%;
- the freshness checker is clean, except for Shade's letters, which use full forms on purpose;
- every seed still has its payoff.

### Task 4. A cold reader panel on Wild (optional, before or after Task 3)

**Goal:** diagnoses from readers who have no context, to set beside bt 7274's own read.

**Read:**
- `Story/Sunday-Morning/Reader-Panel.md` for the method;
- `Wild/` in full.

**Method:** use three to five independent reader agents, each with a different reading condition, and give them **no** Growth Notes. Collect where each reader lost interest, what confused them, what they'd quote, and what they'd tell a friend. Merge the results by agreement.

**Output:** `Story/Revision/Reader-Reports/<date>_Wild-Panel.md`, as diagnoses only.

**Done when** each finding has a count of readers who agreed and a chapter location.

## Starting prompts

Paste one of these into a fresh session, as is.

**Task 1:**
> Read `Story/Revision/High-Effort-Brief.md` and `Story/Revision/Before-You-Touch-A-Chapter.md`, then do Task 1 (the harvest map) exactly as the brief describes. Don't read files the brief says to skip. Don't edit `Story/Chapters/`. My notes from reading the Wild epub: [paste notes, or "none yet"].

**Task 2:**
> Read `Story/Revision/High-Effort-Brief.md` and do Task 2 using my rulings in `Story/Revision/Harvest-Map-<date>.md`. Show me every diff before you commit.

**Task 3:**
> Read `Story/Revision/High-Effort-Brief.md` and do Task 3 (the Wild Garden's second growth). Don't open `Story/Chapters/` or `Experiments/Garden/`.

**Task 4:**
> Read `Story/Revision/High-Effort-Brief.md` and do Task 4 (a cold reader panel on the Wild Garden).
