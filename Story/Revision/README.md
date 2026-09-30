# Pathwell revision

## Status

**Index. Active.** This folder holds the records for revising the Pathwell manuscript with the method in [Story/Sunday-Morning/](../Sunday-Morning/README.md): its pipeline, craft, voice guide, Registry, checker, promise ledger and independent checks, but not its tone, stakes, setting palette, larger-story machinery or collection calendar ([R1](Decisions.md#jamess-rulings-for-this-revision)). Pathwell is a longer, darker literary urban fantasy.

It follows MAPS_L: **one concept, one owner**, linked rather than repeated. It holds only what didn't already exist; everything else is linked from the [inventory](#inventory-of-existing-process-records).

**Where things stand:** pass P1 (Step 1: take stock) is done and stopped for James's review. P1b checked the findings against the Bible interview's locked answers, which settle most of what P1 first asked. P2 (2026-09-30) recorded James's answers, brought the pillar pages into line, laid out the climax options, and found that the voice benchmark is his pre-August prose. P3 archived everything superseded. **P4 (Step 2) revised Chapter 12 and stopped for James's verdict**: the [pass log](Pass-Log.md#p4-2026-09-30-step-2-chapter-12) has the change notes and the lines for him to rule on. No other chapter has been touched.

## Order of authority

When two notes pull in different directions, each decides its own ground in this order ([R2](Decisions.md#jamess-rulings-for-this-revision)):

1. **[Decisions](Decisions.md):** James's rulings, including his answers in the Bible interview (2026-08-21 to 08-27, Q1–Q149), which are indexed there.
2. **The book's own targets:** [Thesis and Controlling Ideas](../../Thesis-and-Controlling-Ideas.md), [Non-Negotiable Scenes](../../Non-Negotiable-Scenes.md) and [Writing Principles](../../Writing-Principles.md). Non-Negotiable Scenes and two rows of the Thesis page were brought into line with the interview on 2026-09-30 ([R14](Decisions.md#jamess-rulings-for-this-revision)). On facts about the world (how pruning, records and blobs work; who is who), [canon.md](../Story_Files/canon.md) and the interview's locks are the owner pages, as the Sunday Morning notes' [canon discipline](../Sunday-Morning/Rules.md#canon-discipline) would have it.
3. **Craft:** the Sunday Morning [Craft](../Sunday-Morning/Craft.md) page (the 17 telling principles, write how people talk, who writes what, the watch-list, the one-line test), read with the book's changes below. Its telling principles are adapted *from* Writing Principles; where the two differ, Writing Principles wins.
4. **Voice:** James's [voice guide](../Sunday-Morning/Sources/Voice-Guide.md), then [pathwell_prose_voice.md](../Story_Files/pathwell_prose_voice.md). The ear to check against is James's own Chapters 1–2 **as they stood before the 2026-08-28 rewrite** (`git show 765b69b:Story/Chapters/Chapter_01.txt`, and `Chapter_02.txt`), not the current files ([W9](Decisions.md#working-decisions)).
5. **[Registry](Registry.md):** keeps the book from repeating itself.

## What's here

| Note | Owns | MAPS_L class | State |
| --- | --- | --- | --- |
| [Decisions](Decisions.md) | James's rulings for this revision; earlier rulings recorded elsewhere, and whether the manuscript reflects them; working decisions; open questions for James | authority | active |
| [Plan](Plan.md) | the book-level THINK pass, the prioritized plan routed by level, reconsideration triggers, the Step 2 test | procedure | active, awaiting approval |
| [Promise ledger](Promise-Ledger.md) | every setup and payoff across the chapters, with its status | working record | active |
| [Registry](Registry.md) | names, chapter shapes, devices, stock phrases, watch patterns and checker exceptions | template copy, read by the checker | active |
| [Pass log](Pass-Log.md) | one entry per pass: what ran, what changed (change notes from the diff), the check log | evidence | active |
| [Cold read, 2026-09-29](Cold-Read-2026-09-29.md) | the independent cold read of the whole manuscript | evidence | closed |
| [Assessment, 2026-09-29](Assessment-2026-09-29.md) | chapter-by-chapter assessment, shape check, checker results, watch-list | evidence | closed (describes the manuscript at pass P1) |

Chapter status lives where it always has, in [Revision-Status.md](../../Revision-Status.md). Each chapter's plan is its contract in the [chapter contract matrix](../Story_Files/PATHWELL_MAPS_L_CHAPTER_CONTRACT_MATRIX_2026-08-28.md) ([W3](Decisions.md#working-decisions)).

## Development levels for a chapter

The Pipeline's [levels](../Sunday-Morning/Pipeline.md#development-levels-what-done-means), read per chapter ([W1](Decisions.md#working-decisions)). Every chapter's target is **L4**.

| Level | DONE when |
| --- | --- |
| **L0 Contract** | the chapter's job in the book is stated: its contract in the matrix |
| **L1 Hardened** | the book-level THINK pass is recorded and any open question touching the chapter is listed for James |
| **L2 Planned** | the chapter's work list, its ledger rows and the reconsideration triggers are recorded ([plan](Plan.md#chapter-work-lists)) |
| **L3 Revised** | the chapter has been revised from the voice sources, run through [after every pass](#after-every-pass), and checked independently against its plan and its previous version |
| **L4 Reviewed** | an independent JUDGE pass (a cold read of the book in order, then the checks) is done and reconciled, and James has read it |

## Scene diagnostic for Pathwell

The Sunday Morning [scene diagnostic](../Sunday-Morning/Craft.md#sunday-morning-scene-diagnostic), with its fifth question replaced ([W2](Decisions.md#working-decisions)), since "Would a reader brace here? Add warmth" enforces Sunday Morning tone:

1. **What does the viewpoint character want in this scene?** "Nothing" or "to understand what's happening" means passive, unless the scene's job is breathing room ([Writing Principles 11](../../Writing-Principles.md#11-breathe-when-the-story-needs-possession)).
2. **Therefore, but, or and then?** Fix "and then".
3. **What changed from top to bottom?**
4. **Did anyone, including the narrator, explain what the scene already showed?** Cut it.
5. **Deletion test:** "If this scene is removed, ______ becomes materially weaker." And before anything is lost: what has the reader been allowed to *have*? ([necessity test](../../Writing-Principles.md#universal-chapter-necessity-test))

## After every pass

Every revision pass ends with this, in order. It's the Pipeline's [routine](../Sunday-Morning/Pipeline.md#after-every-pass) with the first step replaced.

1. **The book's targets first.** Check the pass against [Decisions](Decisions.md), the Thesis page's test ("If a character says the theme out loud, it's failed", which here includes the narrator) and the world's rules ([canon.md](../Story_Files/canon.md), [Writing Principles 17](../../Writing-Principles.md#17-rules-are-sacred-once-established)).
2. **Shapes before sentences.** If the pass changed an opening, engine, resolution or ending, update the [Registry's shapes](Registry.md#chapter-shapes) and check the neighbouring chapters for sameness.
3. **Run the checker** from the repository root, and compare the chapter's numbers with the benchmark (Chapters 1–3):

   ```text
   python3 Story/Sunday-Morning/tools/sunday_morning_check.py --registry Story/Revision/Registry.md --drafts Story/Chapters --pattern "Chapter_*.txt" --min-files 3
   ```

4. **Run the [scene diagnostic](#scene-diagnostic-for-pathwell)** on every scene the pass touched. Prefer cuts.
5. **Get a fresh check** from a pass that didn't write the text, comparing the new version with the old one (drift, lost setups, new continuity errors) and with its neighbours (repetition).
6. **Look for the replacement tic.** After removing a repeated move, check that another hasn't taken its place.
7. **Leave deliberate ambiguity alone.** Some gaps are rulings (the prune's content, open by lock; whether Pathwell can still prune, which he chooses not to find out).
8. **Write change notes from the diff,** not from intention, in the [pass log](Pass-Log.md); update the [ledger](Promise-Ledger.md) and [Revision-Status.md](../../Revision-Status.md).

## Inventory of existing process records

Reorganized on 2026-09-30 so that there's one current version of anything ([R16](Decisions.md#jamess-rulings-for-this-revision), [W10](Decisions.md#working-decisions)). The [repository README](../../README.md) is the front door; this table says how the revision uses each part.

| Concept | Owner | State | Use in this revision |
| --- | --- | --- | --- |
| The manuscript | [Story/Chapters/](../Chapters/) `Chapter_01–18.txt`; `assemble_manuscript.py` | current; chapters last changed 2026-08-28 | the text under revision |
| James's rulings | the [Bible interview](../Interview/README.md) (2026-08-21 to 08-27, Q1–Q149), and [Decisions](Decisions.md) for everything since | authority | order of authority, 1 |
| The book's targets | [Thesis](../../Thesis-and-Controlling-Ideas.md), [Non-Negotiable Scenes](../../Non-Negotiable-Scenes.md), [Writing Principles](../../Writing-Principles.md) | authority; the first two brought into line with the interview on 2026-09-30 | order of authority, 2 |
| World, characters, chapter plans, voice | [Story_Files](../Story_Files/README.md): canon, world and character bibles, glossary, chapter contract matrix, pathwell_prose_voice, forbidden_patterns, the quote bank | current; stale bible lines corrected 2026-09-30 | owner pages for world facts; each chapter's contract is its plan |
| Voice | [voice guide](../Sunday-Morning/Sources/Voice-Guide.md), [pathwell_prose_voice.md](../Story_Files/pathwell_prose_voice.md), and James's own pre-August Chapters 1–2 in the [voice benchmark](Voice-Benchmark/README.md) | authority | order of authority, 4 |
| Chapter status | [Revision-Status.md](../../Revision-Status.md) | current | updated after every pass |
| The method | [Story/Sunday-Morning/](../Sunday-Morning/README.md) and its [checker](../Sunday-Morning/tools/sunday_morning_check.py) | current | this revision's method |
| Everything superseded | [Story/Archive/](../Archive/README.md): the old Coda and manuscript files, the June wiki, the interview handoffs, the August reconciliation logs and roadmaps, the September experiments, session notes, secondary voice guides | history | never cited as authority; read for why things changed |
