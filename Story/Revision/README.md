# Pathwell revision

## Status

**Index. Active.** This folder holds the records for revising the Pathwell manuscript with the method in [Story/Sunday-Morning/](../Sunday-Morning/README.md): its pipeline, craft, voice guide, Registry, checker, promise ledger and independent checks, but not its tone, stakes, setting palette, larger-story machinery or collection calendar ([R1](Decisions.md#the-authors-rulings-for-this-revision)). Pathwell is a longer, darker literary urban fantasy.

It follows MAPS_L: **one concept, one owner**, linked rather than repeated. It holds only what didn't already exist; everything else is linked from the [inventory](#inventory-of-existing-process-records).

**Where things stand:** pass P1 (Step 1: take stock) is done and stopped for the author's review. P1b checked the findings against the Bible interview's locked answers, which settle most of what P1 first asked. P2 (2026-09-30) recorded the author's answers, brought the pillar pages into line, laid out the climax options, and found that the voice benchmark is his pre-August prose. P3 archived everything superseded. **P4 (Step 2) revised Chapter 12 and stopped for the author's verdict**: the [pass log](Pass-Log.md#p4-2026-09-30-step-2-chapter-12) has the change notes and the lines for him to rule on. No other chapter has been touched. P4b–P5 (2026-09-30) took the lessons of the author's AI-detection read into Pathwell's craft, without correcting the chapter: the narrator's own voice ([register guide](../Story_Files/pathwell_narrator_register.md)), [Writing against sameness](Writing-Against-Sameness.md) and the researched [AI-Tells](AI-Tells.md) reference.

## Order of authority

When two notes pull in different directions, each decides its own ground in this order ([R2](Decisions.md#the-authors-rulings-for-this-revision)):

1. **[Decisions](Decisions.md):** The author's rulings, including his answers in the Bible interview (2026-08-21 to 08-27, Q1–Q149), which are indexed there.
2. **The book's own targets:** [Thesis and Controlling Ideas](../../Thesis-and-Controlling-Ideas.md), [Non-Negotiable Scenes](../../Non-Negotiable-Scenes.md) and [Writing Principles](../../Writing-Principles.md). Non-Negotiable Scenes and two rows of the Thesis page were brought into line with the interview on 2026-09-30 ([R14](Decisions.md#the-authors-rulings-for-this-revision)). On facts about the world (how pruning, records and blobs work; who is who), [canon.md](../Story_Files/canon.md) and the interview's locks are the owner pages, as the Sunday Morning notes' [canon discipline](../Sunday-Morning/Rules.md#canon-discipline) would have it.
3. **Craft:** the Sunday Morning [Craft](../Sunday-Morning/Craft.md) page (the 17 telling principles, write how people talk, who writes what, the watch-list, the one-line test), read with the book's changes below. Its telling principles are adapted *from* Writing Principles; where the two differ, Writing Principles wins.
4. **Voice:** The author's [voice guide](../Sunday-Morning/Sources/Voice-Guide.md), then [pathwell_prose_voice.md](../Story_Files/pathwell_prose_voice.md) and, for the narrator, [pathwell_narrator_register.md](../Story_Files/pathwell_narrator_register.md): the narrator has its own voice ([W11](Decisions.md#working-decisions)). The ear to check against is the author's own Chapters 1–2 **as they stood before the 2026-08-28 rewrite** (`git show 765b69b:Story/Chapters/Chapter_01.txt`, and `Chapter_02.txt`), not the current files ([W9](Decisions.md#working-decisions)).
5. **[Registry](Registry.md):** keeps the book from repeating itself.

## What's here

| Note | Owns | MAPS_L class | State |
| --- | --- | --- | --- |
| [Decisions](Decisions.md) | The author's rulings for this revision; earlier rulings recorded elsewhere, and whether the manuscript reflects them; working decisions; open questions for the author | authority | active |
| [Chapter 1 author markup and editorial feedback (2026-10-08/09)](Author-Notes/2026-10-08_Chapter-01_line-notes.md) | verbatim red-and-bold author notes from *Pathwell 10.7*, initial R26 response, and separately labeled independent feedback on those edits; no manuscript change | evidence / editorial review | received; not applied |
| [Plan](Plan.md) | the book-level THINK pass, the prioritized plan routed by level, reconsideration triggers, the Step 2 test | procedure | active, awaiting approval |
| [Writing against sameness](Writing-Against-Sameness.md) | Pathwell's application of [Craft: writing against sameness](../Sunday-Morning/Craft.md#writing-against-sameness): the register map, whose joke it is, Elizabeth's interiority, usually one polished closing line per scene, new emotional lines left to the author, the two benchmarks, the fresh check's sameness questions | procedure | active |
| [AI tells in Pathwell](AI-Tells.md) | what the manuscript shows, and each common AI tell set against this book's guides; the researched general list is in the Sunday Morning notes' [AI tells](../Sunday-Morning/Sources/AI-Tells.md). Awareness, not a rulebook | reference | active |
| [Promise ledger](Promise-Ledger.md) | every setup and payoff across the chapters, with its status | working record | active |
| [Registry](Registry.md) | names, chapter shapes, devices, stock phrases, watch patterns and checker exceptions | template copy, read by the checker | active |
| [Pass log](Pass-Log.md) | one entry per pass: what ran, what changed (change notes from the diff), the check log | evidence | active |
| [Decision timeline](Decision-Timeline.md) | every decision the author has made, oldest to newest (about 700 rows, each quoting its source), with the old-to-new chapter mapping | index | active |
| [Currency audit, 2026-10-01](Currency-Audit-2026-10-01.md) | where the chapters and reference pages follow outdated versions of the decisions, with the full findings and a verification in its folder | evidence | closed |
| [Cold read, 2026-09-29](Cold-Read-2026-09-29.md) | the independent cold read of the whole manuscript | evidence | closed |
| [AI detection notes, 2026-09-30](AI-Detection-Notes-2026-09-30.md) | what the author's GPTZero read of the revised Chapter 12 teaches; not a work item ([R17](Decisions.md#the-authors-rulings-for-this-revision)) | evidence | closed |
| [Assessment, 2026-09-29](Assessment-2026-09-29.md) | chapter-by-chapter assessment, shape check, checker results, watch-list | evidence | closed (describes the manuscript at pass P1) |

Chapter status lives where it always has, in [Revision-Status.md](../../Revision-Status.md). Each chapter's plan is its contract in the [chapter contract matrix](../Story_Files/PATHWELL_MAPS_L_CHAPTER_CONTRACT_MATRIX_2026-08-28.md) ([W3](Decisions.md#working-decisions)).

## Development levels for a chapter

The Pipeline's [levels](../Sunday-Morning/Pipeline.md#development-levels-what-done-means), read per chapter ([W1](Decisions.md#working-decisions)). Every chapter's target is **L4**.

| Level | DONE when |
| --- | --- |
| **L0 Contract** | the chapter's job in the book is stated: its contract in the matrix |
| **L1 Hardened** | the book-level THINK pass is recorded and any open question touching the chapter is listed for the author |
| **L2 Planned** | the chapter's work list, its ledger rows and the reconsideration triggers are recorded ([plan](Plan.md#chapter-work-lists)) |
| **L3 Revised** | the chapter has been revised from the voice sources, run through [after every pass](#after-every-pass), and checked independently against its plan and its previous version |
| **L4 Reviewed** | an independent JUDGE pass (a cold read of the book in order, then the checks) is done and reconciled, and the author has read it |

## Scene diagnostic for Pathwell

The Sunday Morning [scene diagnostic](../Sunday-Morning/Craft.md#sunday-morning-scene-diagnostic), with its fifth question replaced ([W2](Decisions.md#working-decisions)), since "Would a reader brace here? Add warmth" enforces Sunday Morning tone:

1. **What does the viewpoint character want in this scene?** "Nothing" or "to understand what's happening" means passive, unless the scene's job is breathing room ([Writing Principles 11](../../Writing-Principles.md#11-breathe-when-the-story-needs-possession)).
2. **Therefore, but, or and then?** Fix "and then".
3. **What changed from top to bottom?**
4. **Did anyone, including the narrator, explain what the scene already showed?** Cut it.
5. **Deletion test:** "If this scene is removed, ______ becomes materially weaker." And before anything is lost: what has the reader been allowed to *have*? ([necessity test](../../Writing-Principles.md#universal-chapter-necessity-test))

## Before and while writing

Follow [Writing against sameness](Writing-Against-Sameness.md): map the scene's register before touching it, know whose joke each joke is, let Elizabeth think like a person, keep polished closing lines to usually one per scene, and leave new emotional lines and jokes to the author. The [AI-Tells](AI-Tells.md) reference lists what to be aware of.

## After every pass

Every revision pass ends with this, in order. It's the Pipeline's [routine](../Sunday-Morning/Pipeline.md#after-every-pass) with the first step replaced.

1. **The book's targets first.** Check the pass against [Decisions](Decisions.md), the Thesis page's test ("If a character says the theme out loud, it's failed", which here includes the narrator) and the world's rules ([canon.md](../Story_Files/canon.md), [Writing Principles 17](../../Writing-Principles.md#17-rules-are-sacred-once-established)).
2. **Shapes before sentences.** If the pass changed an opening, engine, resolution or ending, update the [Registry's shapes](Registry.md#chapter-shapes) and check the neighbouring chapters for sameness. Do the same for [joke shapes](Registry.md#joke-shapes-already-used).
3. **Run the checker** from the repository root, and compare the chapter's numbers with the author's own [pre-August Chapters 1–2](Voice-Benchmark/README.md). The numbers are a floor. The voice is judged by reading, against those chapters and the [narrator register guide](../Story_Files/pathwell_narrator_register.md)'s calibration lines ([two benchmarks](Writing-Against-Sameness.md#after-writing)):

   ```text
   python3 Story/Sunday-Morning/tools/sunday_morning_check.py --registry Story/Revision/Registry.md --drafts Story/Chapters --pattern "Chapter_*.txt" --min-files 3
   ```

4. **Run the [scene diagnostic](#scene-diagnostic-for-pathwell)** on every scene the pass touched. Prefer cuts.
5. **Get a fresh check** from a pass that didn't write the text, comparing the new version with the old one (drift, lost setups, new continuity errors) and with its neighbours (repetition). It also answers the [sameness questions](Writing-Against-Sameness.md#after-writing): repeated joke shapes, whose joke each is, the narrator's register, how Elizabeth thinks, polished closing lines, and clusters from the [AI-Tells](AI-Tells.md) list.
6. **Look for the replacement tic.** After removing a repeated move, check that another hasn't taken its place.
7. **Leave deliberate ambiguity alone.** Some gaps are rulings (the prune's content, open by lock; whether Pathwell can still prune, which he chooses not to find out).
8. **Write change notes from the diff,** not from intention, in the [pass log](Pass-Log.md); update the [ledger](Promise-Ledger.md) and [Revision-Status.md](../../Revision-Status.md).

## Inventory of existing process records

Reorganized on 2026-09-30 so that there's one current version of anything ([R16](Decisions.md#the-authors-rulings-for-this-revision), [W10](Decisions.md#working-decisions)). The [repository README](../../README.md) is the front door; this table says how the revision uses each part.

| Concept | Owner | State | Use in this revision |
| --- | --- | --- | --- |
| The manuscript | [Story/Chapters/](../Chapters/) `Chapter_01–18.txt`; `assemble_manuscript.py` | current; chapters last changed 2026-08-28 | the text under revision |
| The author's rulings | the [Bible interview](../Interview/README.md) (2026-08-21 to 08-27, Q1–Q149), and [Decisions](Decisions.md) for everything since | authority | order of authority, 1 |
| The book's targets | [Thesis](../../Thesis-and-Controlling-Ideas.md), [Non-Negotiable Scenes](../../Non-Negotiable-Scenes.md), [Writing Principles](../../Writing-Principles.md) | authority; the first two brought into line with the interview on 2026-09-30 | order of authority, 2 |
| World, characters, chapter plans, voice | [Story_Files](../Story_Files/README.md): canon, world and character bibles, glossary, chapter contract matrix, pathwell_prose_voice, forbidden_patterns, the quote bank | current; stale bible lines corrected 2026-09-30 | owner pages for world facts; each chapter's contract is its plan |
| Voice | [voice guide](../Sunday-Morning/Sources/Voice-Guide.md), [pathwell_prose_voice.md](../Story_Files/pathwell_prose_voice.md), the [narrator register guide](../Story_Files/pathwell_narrator_register.md), and the author's own pre-August Chapters 1–2 in the [voice benchmark](Voice-Benchmark/README.md) | authority | order of authority, 4 |
| Chapter status | [Revision-Status.md](../../Revision-Status.md) | current | updated after every pass |
| The method | [Story/Sunday-Morning/](../Sunday-Morning/README.md) and its [checker](../Sunday-Morning/tools/sunday_morning_check.py) | current | this revision's method |
| Everything superseded | [Story/Archive/](../Archive/README.md): the old Coda and manuscript files, the June wiki, the interview handoffs, the August reconciliation logs and roadmaps, the September experiments, session notes, secondary voice guides | history | never cited as authority; read for why things changed |
