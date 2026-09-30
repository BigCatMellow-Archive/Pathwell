# Archive

## Status

**Archive. Nothing in this folder is authority, and nothing here is the manuscript.** It holds earlier versions, superseded plans, session plumbing and experiments, kept as history so a later pass can see why something is the way it is. It was gathered on 2026-09-30 at the author's request, so that earlier versions stop being mistaken for current ones ([revision Decisions, R16](../Revision/Decisions.md#the-authors-rulings-for-this-revision)). Files were moved with `git mv`, unchanged, so `git log --follow` shows each one's history.

**If something here disagrees with a current page, the current page wins.** Current pages are listed in the [repository README](../../README.md). Don't cite anything in this folder as a ruling; the author's rulings are in the [Bible interview](../Interview/README.md) and the revision's [Decisions](../Revision/Decisions.md).

## What's here, and what replaced it

| Folder | What it was | Replaced by |
| --- | --- | --- |
| [Manuscript/](Manuscript/) | `Coda.txt` (the pre-reconciliation ending), `Pathwell Working.docx` (the legacy working file), `editorial-2026-06/` (June chapter reviews and story context), `Review_Notes*.txt` | [Chapter 18](../Chapters/Chapter_18.txt) is the ending; [the chapters](../Chapters/) are the manuscript. Coda.txt contradicts the book and the interview's Q93–Q103 name its contents stale |
| [Wiki-2026-06/](Wiki-2026-06/) | The June story wiki: Home, Plot-Structure, Agency-Ladder, Key-Discoveries, Mirrors-and-Echoes, the character pages, Magic-System, Pruning, Blobs, Locations, Open-Questions, Structural-Risks, Quick-Diagnostic, the sidebar, and `index.html` (a rendered copy of the wiki) | The [Bible interview](../Interview/README.md) and [canon, world and character bibles](../Story_Files/README.md). These pages predate the interview: they have the diary as a weapon, the cookbook healing Mama Baga, lo mein as a rung, Elizabeth cutting herself out of the blob, and the private retry |
| [Interview-handoffs/](Interview-handoffs/) | The 64 `BIBLE_INTERVIEW_CONTINUATION` files that carried the interview from one chat session to the next | The interview itself, in [Story/Interview](../Interview/README.md) |
| [Reconciliation-2026-08/](Reconciliation-2026-08/) | How the chapters were rewritten on 2026-08-28: the execution logs, the reconciliation roadmap, the backward proof, the expansion roadmap, the whole-manuscript audit | The [chapters](../Chapters/) as written, and the [chapter contract matrix](../Story_Files/PATHWELL_MAPS_L_CHAPTER_CONTRACT_MATRIX_2026-08-28.md), which stays active as each chapter's plan |
| [Experiments-2026-09/](Experiments-2026-09/) | The 17–18 September Experimental Architecture V2–V5 and everything around it (options, evaluations, matrices, the recovered-decision audits, the disagreement register, the author-intent notes). None of it was applied to the chapters | The author decisions it recorded are indexed, and checked against the interview, on the revision's [Decisions](../Revision/Decisions.md#later-recorded-rulings-2026-09-1718); the author answered the differences on 2026-09-30 (R9–R15) |
| [Notes-2026-06-to-08/](Notes-2026-06-to-08/) | Session notes and analysis: the analysis log, the story logic test, the convenience paradox, session progress (July), the Chapter 1–2 revision journeys, the editorial operations guide, the debt-payment checklist | The [revision records](../Revision/README.md). The revision journeys and editorial operations remain good evidence of how the author revised Chapters 1–2 |
| [Voice-notes/](Voice-notes/) | Secondary voice and register guides (tone register, narration mode, oral vs precise, oral vs clinical, the oral-storytelling and cadence guides) | The author's [voice guide](../Sunday-Morning/Sources/Voice-Guide.md), [pathwell_prose_voice.md](../Story_Files/pathwell_prose_voice.md), and his own [pre-August chapters](../Revision/Voice-Benchmark/README.md); the narrator register guide, which returned to [Story_Files](../Story_Files/pathwell_narrator_register.md) on 2026-09-30 |

## Rules, so this doesn't pile up again

1. **One current version of anything.** When a page, plan or draft is superseded, move it here in the same commit, and add a row above saying what replaced it.
2. **Archive whole, don't edit.** Files here keep their original text; the row above carries the status.
3. **Nothing here is cited as a ruling.** If an archived file holds a decision that's still live, the decision is copied to its owner page (the interview index or Decisions) with a link back, and the owner page is what's cited.
4. **Look here for history, not for answers.** A pass that needs to know why the story changed can read here; a pass that needs to know what's true reads the current pages.
5. **Check the concept has a current owner before archiving.** A note isn't secondary just because it's one of several on a topic. If no current page owns what it says, it stays current. The narrator register guide was archived by mistake on 2026-09-30 and returned the same day ([W11](../Revision/Decisions.md#working-decisions)).
