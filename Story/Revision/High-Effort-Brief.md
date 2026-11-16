# High-effort session brief

## Status

**Active.** Written 2026-11-16 ([P119](Pass-Log.md#p119-2026-11-16-a-brief-for-a-high-effort-session)) for fresh sessions on a stronger model at high effort. The aim is to spend that effort on judgment, not on discovery. Run **one task per session**, and paste that task's prompt from the end of this page.

This page is a task router. It sits **under [AGENTS.md](../../AGENTS.md)**, which governs how agents work here: authority order, the reading budget, what needs the author, the loop, records, independence and reporting. It owns none of those. Where this page and AGENTS.md or a ruling disagree, they win.

## The decision only bt 7274 can make

**Which edition leads from here?** Every task below either serves all three answers or waits for one.

| Option | What it means |
| --- | --- |
| **A. The Wild Garden leads** | Develop Wild as the candidate edition and carry the older manuscript's moral pressure into it, not its catastrophes. This is the editorial lean in the [Carryover Review](Experiments/Wild/Carryover-Review-2026-11-03.md). The locks were made for the manuscript, so any lock Wild breaks (below) would need re-ruling. |
| **B. The manuscript stays canonical** | Harvest the Wild and Garden ideas that fit its locks, and keep Wild as a source. |
| **C. Decide after a blind read** | Readers who have never seen either edition read both, and he decides from that evidence. |

Tasks 1 and 2 serve every option, so they can run now. Task 3 runs after A or C, and Task 4 after B.

## What's true right now

Checked 2026-11-16 at commit `4fdeb01`. Don't re-verify it.

| Edition | Where | Words | State |
| --- | --- | --- | --- |
| **The manuscript** | `Story/Chapters/` | 47k | Canonical; every chapter is L3. The last chapter pass was P104. Each chapter's level and blockers are in [Revision-Status](../../Revision-Status.md). |
| **The Garden** | `Experiments/Garden/` | 55k | Sunday Morning trial (P113–P115). Growth record: `Growth-Log.md`. |
| **The Wild Garden** | `Experiments/Wild/` | 39k | Grown without opening either other edition, then tended twice (P116–P118). Its records are the [Growth Notes](Experiments/Wild/Growth-Notes.md) (each changed beat, with its reason) and the [Carryover Review](Experiments/Wild/Carryover-Review-2026-11-03.md). bt 7274 is test-reading the epub. |

- **The Carryover Review** (2026-11-03) is the most important record this brief points to. It sets five targets: C1 keep Elizabeth separate from his redemption; C2 respect Shade's first "no"; C3 leave Wren's debt unresolved; C4 put the duck pond through the same moral test as everything else (an author choice); C5 protect what Wild already does better. Its suggested order is **C2 → C1 → C3 → author on C4**. None of its suggestions have been adopted.
- **Overlap:** Wild shares 0.4% of its six-word phrases with the manuscript and 2.0% with the Garden. Transplanting has been checked; don't check it again.
- **Harada:** 22 errors, all pre-existing. A change that leaves it at 22 hasn't broken it.

### Known problems in Wild

These are diagnosed and not yet fixed. The Carryover Review's C1–C4 come on top of them.

1. **US/UK drift.** The manuscript is American: apartment, sidewalk, hood. Wild drifted British: flat, pavement, bonnet, fortnight, launderette, nan. A word count gives 43 US to 60 UK, against 49 to 27 in the manuscript.
2. **Ch3 runs 3.3k words,** long for Sunday Morning.
3. **The narrator's similes** ("the way you'd…", "as though") and a high rate of short paragraphs. Some of this is voice and some is tic.
4. **The back half is gentler.** The stakes are in what's lost, not in who.
5. **Ch15's Shade section,** in the present tense, may jar.
6. **Timeline,** from the Carryover Review's secondary checks: verify the work-at-nine remark, the story-hour Saturdays, the Sunday-to-Monday turn, and the bowling-to-launderette timing.

### Where Wild breaks a manuscript lock

These matter for Option B (a harvest) and for re-ruling under A. The locks themselves are in [Before you touch a chapter](Before-You-Touch-A-Chapter.md).

| Wild does | Lock it breaks |
| --- | --- |
| Elizabeth says "Ready?" and Pathwell says "No." (speakers reversed) | R9: the last three lines |
| No capture, no withheld call, no Milo; the rejoining is refused, and the dagger cuts the pull | R45, R46: the climax's shape |
| A Ch18 confession with anger and the landing scene, and no browsing hour | R47: Version C |
| Wren is named as the one who asked for help | lock 08-22 §4: stays open |
| Ch18 explains why he picked her | R48, R53: already answered by design |
| Gary, the rota, going back to work | R35(2), Q136: her work life stays open |
| Elizabeth uses the foam dagger to cut the pull | the no-magic lock. The foam weapons are in manuscript Ch5–Ch15 but not in the world bible; check how the manuscript lets her use them before calling this a breach |

Wild ideas that touch **no** lock:
- the "sorry" habit, with Mrs. Okafor as its mirror;
- ASK BEFORE USING, and "Can I?" / "No." / "Right.";
- Kevin's bear and BY PATHWELL;
- Pathwell not playing anything he might lose, and the dominoes;
- the healer's "Is there anything you want first?";
- the gray page rewritten in her own hand;
- the crossword answers;
- SUDS and the dryer;
- the insurance list;
- the recipe bookends;
- the object chapter titles.

### Open items waiting on bt 7274

These aren't for the model to decide.

- **Q-O**, Ch2's changed neighborhood: displacement or magic? ([Decisions](Decisions.md#open-for-the-author))
- **Ch5 "He lies, you know"** reads as mind-reading (asked in P104).
- **Nana's first name and Elizabeth's family name** stay off the page unless he says otherwise.
- **AGENTS.md §10** still says to call him "the author". His newer standing preference is **"bt 7274"**, which the Wild and Garden records already use. AGENTS.md needs his OK to update (§4: restructuring a record).
- **The full-book `PATHWELL_11.02.docx`** has the old em-dash quote bug. Rebuild it with `build_book.py` if he wants a fresh copy.

## Reading budget

Follow AGENTS.md §3. For these tasks, also skip:
- `Archive/`, `Council/`, `Currency-Audit*`, `Voice-Pass/` and the `Harada/` internals;
- the panel CSVs under `Reader-Reports/`;
- `Story/ideas`, `Story/insights` and `Story/Interview` (read the interview only when a lock's exact wording matters).

Grep `Pass-Log.md` (3,600 lines) for a P-number; don't read it through.

## Rules that aren't in AGENTS.md

- **His name.** Never write it anywhere in the repo. Call him **bt 7274**.
- **Commit trailers,** on every commit, then push to `main`. Pull first, because he commits from other sessions too:
  ```
  Co-Authored-By: <model> <noreply@anthropic.com>
  Claude-Session: <session url>
  ```
- **`Experiments/` can be committed freely.** It's scaffolding, not canon. `Story/Chapters/` changes are candidates only (AGENTS.md §4 and §7).
- **Reader notes are diagnoses, not prescriptions.** Fixes are offered as options.
- **No "Recommended" on a taste call.** Give a lean, labelled as a lean.
- **Chat replies stay brief.** The work goes in files.

## Tools

These are already built. See [Experiments/tools](Experiments/tools/README.md).

- `build_book.py`: docx and/or epub from any chapter folder.
- `overlap.py`: shared-phrase check, showing draft-side text only.
- The freshness checker, `assemble_manuscript.py` and the Harada check.

## Tasks

### Task 1. The Wild Garden's third tending: carryover first (serves A and C)

**Goal:** make Wild the strongest fair version of itself before anyone compares it with the manuscript.

**Read:**
- the Carryover Review;
- the Growth Notes;
- `Wild/` in full;
- for C1–C3, **only** the manuscript passages the Carryover Review links to (Ch14 and Ch16). The review has already done the comparison. Don't read the rest of the manuscript or the Garden.

**Method:**
1. **C2.** Elizabeth makes Pathwell hear Shade's *first* "no". Cut the second ask; keep the reasons he lines up, "All right.", and the empty hand.
2. **C1.** In Ch18, show a boundary she keeps living with, without turning her into his judge or the proof that he's reformed. Keep the anger, the landing, the recipe and her invitation.
3. **C3.** After the warmth, let Wren's debt still weigh, through a restrained action, not a speech or a new scene.
4. **C4.** Don't change it. Write candidate A (she pulls over and refuses to drive) and candidate B (the pond, with its consequences made credible) as an [EXP page](Emergence/experiments/) for bt 7274. Trace each candidate's downstream costs: the launderette, the wet books, Shade's ducks.
5. **Known problems 1, 2, 3 and 6.** Americanize the whole thing. Bring Ch3 to about 2.5k words, grepping each seed before you cut it. Thin the tics only, and list every cut you're unsure of. Walk the timeline.
6. Leave problems 4 and 5 alone unless C1–C3 change them. They're for a reader panel to judge.

**Output:**
- commits to `Wild/`;
- a "Third tending" section in the Growth Notes;
- a short Done/Pending addendum to the Carryover Review;
- the EXP page for C4;
- `build_book.py --docx --epub`, with the epub sent to him.

**Done when:**
- `overlap.py` against the manuscript stays under 1%, apart from deliberate C-carryover functions, which must not be transplanted lines;
- the freshness checker is clean, except for Shade's letters, which use full forms on purpose;
- every seed still has its payoff;
- a helper **that didn't write the changes** has run a fresh check (AGENTS.md §8).

### Task 2. Blind comparative panel (serves every option; best after Task 1)

**Goal:** the evidence for the lead-edition decision, plus the blind read the manuscript's L4 still needs.

**Read:** [Reader panel](../Sunday-Morning/Reader-Panel.md) and [Reader protocol](../Sunday-Morning/Reader-Protocol.md), for the method only. The reviser assembles the packets; the readers read only their packets.

**Method:**
1. Use four to six reader helpers with different reading conditions.
2. Split them so each edition gets fresh readers: half read the manuscript first, half read Wild first, and some read only one edition.
3. Keep them blind to the goals, the Growth Notes, the Carryover Review and each other.
4. Ask each reader where they lost interest, what confused them, what they'd quote, what they'd tell a friend, and which characters they'd follow into another book.
5. Merge by agreement, as diagnoses only.

**Output:** `Reader-Reports/<date>_Edition-Panel/` and an entry in the [Emergence index](Emergence/INDEX.md).

**Done when:**
- each finding has a reader count and a chapter location;
- there's a one-screen comparison (where each edition won, lost or tied);
- the report states plainly that it does not choose the edition.

### Task 3. After A (or C pointing to Wild): re-rule the locks

**Goal:** the rulings Wild would need in order to become the lead edition.

**Read:**
- the lock table above;
- each lock's own row in Decisions, and its interview answer where the wording matters;
- the Wild chapters involved.

**Method:** for each broken lock, write one question for bt 7274. Give two to four options: keep the lock and change Wild to fit (say how); retire the lock for this edition; or a middle option. Add a lean and the cost of each option. Don't decide any of them.

**Output:** an EXP-style ruling sheet, and his answers recorded as R-rows.

**Done when** every row in the lock table has a recorded ruling.

### Task 4. After B: the harvest map

**Goal:** which Wild and Garden ideas to graft into the manuscript, and how.

**Read:**
- all 18 manuscript chapters;
- the Growth Notes and Growth Log;
- then **only** the experiment passages they point to.

**Method:** for each idea:
- its source and its target spot in the manuscript;
- what it does for the [thesis](../../Thesis-and-Controlling-Ideas.md);
- what it displaces;
- the locks it touches;
- its size (a word, a line, a beat or a scene);
- a lean.

Group the ideas as free grafts, grafts that need a ruling, and structural alternatives. Americanize anything that comes from Wild. Then write the picks as EXP candidates (AGENTS.md §7) and apply them verbatim once he has picked.

**Output:** a review in `Emergence/`, indexed, plus the EXP pages.

**Done when** every idea has a row, or a one-line reason it was dropped, and every graft he picked has been applied and verified.

## Starting prompts

Paste one of these into a fresh session, as is.

**Task 1:**
> Read `AGENTS.md`, then `Story/Revision/High-Effort-Brief.md`, and do Task 1 exactly as the brief describes. Don't read files the brief says to skip, and don't open `Story/Chapters/` beyond the passages the Carryover Review links to. My notes from reading the Wild epub: [paste notes, or "none yet"].

**Task 2:**
> Read `AGENTS.md`, then `Story/Revision/High-Effort-Brief.md`, and do Task 2 (the blind comparative panel). Keep every reader blind, as the brief describes. Don't choose the edition.

**Task 3:**
> Read `AGENTS.md`, then `Story/Revision/High-Effort-Brief.md`. I'm choosing option A. Do Task 3 (the lock re-ruling sheet). Don't decide any of the rulings.

**Task 4:**
> Read `AGENTS.md`, then `Story/Revision/High-Effort-Brief.md`. I'm choosing option B. Do Task 4 (the harvest map).
