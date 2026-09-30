# Pathwell revision

## Status

**Index. Active.** This folder holds the records for revising the Pathwell manuscript with the method in [Story/Sunday-Morning/](../Sunday-Morning/README.md): its pipeline, craft, voice guide, Registry, checker, promise ledger and independent checks, but not its tone, stakes, setting palette, larger-story machinery or collection calendar ([R1](Decisions.md#jamess-rulings-for-this-revision)). Pathwell is a longer, darker literary urban fantasy.

It follows MAPS_L: **one concept, one owner**, linked rather than repeated. It holds only what didn't already exist; everything else is linked from the [inventory](#inventory-of-existing-process-records).

**Where things stand:** pass P1 (Step 1: take stock) is done and stopped for James's review. P1b checked the findings against the Bible interview's locked answers, which settle most of what P1 first asked. Read [Decisions](Decisions.md) first (the interview locks the chapters don't yet follow, then the few open questions), then the [plan](Plan.md). The manuscript itself hasn't been touched.

## Order of authority

When two notes pull in different directions, each decides its own ground in this order ([R2](Decisions.md#jamess-rulings-for-this-revision)):

1. **[Decisions](Decisions.md):** James's rulings, including his answers in the Bible interview (2026-08-21 to 08-27, Q1–Q149), which are indexed there.
2. **The book's own targets:** [Thesis and Controlling Ideas](../../Thesis-and-Controlling-Ideas.md), [Non-Negotiable Scenes](../../Non-Negotiable-Scenes.md) and [Writing Principles](../../Writing-Principles.md). Two of them partly predate the interview; bringing them into line is [Q-F](Decisions.md#open-for-james). On facts about the world (how pruning, records and blobs work; who is who), [canon.md](../Story_Files/canon.md) and the interview's locks are the owner pages, as the Sunday Morning notes' [canon discipline](../Sunday-Morning/Rules.md#canon-discipline) would have it.
3. **Craft:** the Sunday Morning [Craft](../Sunday-Morning/Craft.md) page (the 17 telling principles, write how people talk, who writes what, the watch-list, the one-line test), read with the book's changes below. Its telling principles are adapted *from* Writing Principles; where the two differ, Writing Principles wins.
4. **Voice:** James's [voice guide](../Sunday-Morning/Sources/Voice-Guide.md), then [pathwell_prose_voice.md](../Story_Files/pathwell_prose_voice.md). Chapters 1–2, which James revised himself, are the ear to check against.
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

What already existed on 2026-09-29, who owns each concept, and how this revision treats it. Nothing here was moved or deleted; stale pages are marked, not rewritten, except Revision-Status ([W7](Decisions.md#working-decisions)).

| Concept | Owner | State | Use in this revision |
| --- | --- | --- | --- |
| The manuscript | [Story/Chapters/](../Chapters/) `Chapter_01–18.txt`, and `Coda.txt` (superseded by the interview's locks; to be retired, see [Decisions](Decisions.md#the-bible-interview-locks-the-manuscript-doesnt-yet-follow)); [Story/README.md](../README.md); `assemble_manuscript.py` (Chapters 1–18) | canonical; chapters last changed 2026-08-28 | the text under revision |
| Legacy manuscript files | `Pathwell Working.docx`; `Chapters/editorial/` (June chapter reviews) | archive | not used |
| Chapter status | [Revision-Status.md](../../Revision-Status.md) | was stale (around June); rewritten in P1 | kept current after every pass |
| Controlling idea and thesis | [Thesis-and-Controlling-Ideas.md](../../Thesis-and-Controlling-Ideas.md) | authority; two rows predate later rulings | order of authority, 2 |
| Structural pillars | [Non-Negotiable-Scenes.md](../../Non-Negotiable-Scenes.md); the later "Non-negotiable story beats" in [canon.md](../Story_Files/canon.md#non-negotiable-story-beats) | authority, but six of ten scenes predate the interview | [Q-F](Decisions.md#open-for-james) |
| Craft principles | [Writing-Principles.md](../../Writing-Principles.md); [Quick-Diagnostic.md](../../Quick-Diagnostic.md) (its "one unexplained thing" quota is overruled by Writing Principles 18) | authority | order of authority, 2; the scene diagnostic |
| Voice | [Voice-Guide.md](../Sunday-Morning/Sources/Voice-Guide.md); [pathwell_prose_voice.md](../Story_Files/pathwell_prose_voice.md). Secondary: `pathwell_narrator_register.md`, `pathwell_tone_register.md`, `pathwell_narration_mode_guide.md`, `oral_vs_precise_register.md`, `pathwell_oral_vs_clinical_guide.md`, `natural-oral-storytelling-prose-ai-guide.md`, `cadence-rhythm-euphony-ai-review-guide.md`, `quote_and_character_voice_reference.md`, `PATHWELL_TONE_NORTH_STAR_2026-09-17.md` | authority (the first two); the rest support and give way to them | order of authority, 4 |
| James's habits | [forbidden_patterns.md](../Story_Files/forbidden_patterns.md) | authority for the watch-list | via [Craft's watch-list](../Sunday-Morning/Craft.md#jamess-watch-list) |
| World facts | [canon.md](../Story_Files/canon.md), `world_bible.md`, `character_bible.md`, `glossary.md`; wiki pages Magic-System, Pruning, Blobs, Locations, Elizabeth, Pathwell-(Character), Shade, Stansbury, Supporting-Characters | canon.md locked; the rest support, partly pre-reconciliation | owner pages for world facts |
| Earlier rulings | the Bible interview: `BIBLE_DECISIONS_2026-08-21/22/23.md`, then Q1–Q149 in the `MANUSCRIPT_RECONCILIATION_AUDIT` files, with the 64 `BIBLE_INTERVIEW_CONTINUATION` handoffs that carried it between sessions; [recovered decisions](../Story_Files/PATHWELL_RECOVERED_DECISIONS_AUDIT_2026-09-17.md) and [newer decisions](../Story_Files/PATHWELL_RECOVERED_NEWER_DECISIONS_AUDIT_2026-09-17.md) (09-17); [disagreement register](../Story_Files/PATHWELL_AUTHOR_EDITORIAL_DISAGREEMENT_REGISTER_2026-09-18.md) and [author intent](../Story_Files/PATHWELL_CURRENT_AUTHOR_INTENT_SHADE_CONSEQUENCE_NOTES_2026-09-18.md) (09-18) | the interview binds; the September records are checked against it | indexed on [Decisions](Decisions.md), not copied |
| Chapter plans | [chapter contract matrix](../Story_Files/PATHWELL_MAPS_L_CHAPTER_CONTRACT_MATRIX_2026-08-28.md); the reconciliation roadmap, backward proof and expansion roadmap (08-27/28) | the matrix is each chapter's plan; the rest background | L0–L2 |
| How the current chapters were made | `MANUSCRIPT_RECONCILIATION_AUDIT` (with 67 continuation files, 08-23 to 08-27) and `MANUSCRIPT_RECONCILIATION_EXECUTION_LOG` (with 13 continuations, 08-28) | archive; these files are also the Bible interview (Q1–Q149), with the `BIBLE_DECISIONS` pages and the `BIBLE_INTERVIEW_CONTINUATION` handoffs | **James's locked answers**: indexed on [Decisions](Decisions.md) |
| Earlier audits and evaluations | `WHOLE_MANUSCRIPT_CONTINUITY_COMPRESSION_PROSE_AUDIT_2026-08-28.md`, `PATHWELL_MANUSCRIPT_EVALUATION_2026-09-17.md`, `PATHWELL_LENGTH_AND_EARNEDNESS_AUDIT_2026-09-17.md`, `PATHWELL_WRITING_BIBLE_APPLICATION_AUDIT_2026-09-18.md`, `PATHWELL_ORIGINAL_VISION_REANCHOR_AUDIT_2026-09-18.md`, `PATHWELL_ANALYSIS_LOG.md`, `Story_logic_test.md`, `Pathwell_convenience_paradox.md`, `Story/Review_Notes*.txt`, `chapter1_revision_journey.md`, `chapter2_revision_journey.md` | evidence | superseded as the current assessment by [this pass's](Assessment-2026-09-29.md) |
| Experimental architecture, never applied | V2–V5 architecture and story files, the integrated, radical and foundational options, the revised outline and revision direction, the dwell-time map and proof, the V5 matrices, ledger and correction plan, the experimental writing contract, principle-selection rule, story-identity reference and terminology correction (all 09-17/18) | parked proposals | not authority ([W4](Decisions.md#working-decisions)); their author decisions are on [Decisions](Decisions.md) |
| Open questions and risks | [Open-Questions.md](../../Open-Questions.md), [Structural-Risks.md](../../Structural-Risks.md) | June; most items settled by the manuscript; marked in P1 | current questions: [Decisions](Decisions.md#open-for-james) |
| Insights and ideas | [INS-0001](../insights/INS-0001-unpaid-plot-debts-must-be-paid-on-page.md), [IDEA-0001](../ideas/IDEA-0001-debt-payment-pass-for-pathwell-expansion.md), `debt_payment_checklist.md` | promoted | now [Craft principle 15](../Sunday-Morning/Craft.md#15-pay-your-debts-on-the-page-carries-over) |
| Earlier revision method | [pathwell_editorial_operations.md](../Story_Files/pathwell_editorial_operations.md) (how Chapters 1–2 were revised); `session_progress.md` (July) | evidence | the operations inform line work |
| Other wiki pages | Home, Plot-Structure, Agency-Ladder, Key-Discoveries, Mirrors-and-Echoes, Reading-List, `_Sidebar`, `index.html` | support, mostly pre-reconciliation | not used as authority |
| MAP_System | named in [Story/README.md](../README.md) and INS-0001, but not in this repository (it lives in the MultiAgentProject repository) | absent here | not needed |
| The method | [Story/Sunday-Morning/](../Sunday-Morning/README.md), its [checker](../Sunday-Morning/tools/sunday_morning_check.py) (extended in P1, [W5](Decisions.md#working-decisions)) | active | this revision's method |
