# Resource audit: are the passes using what the repository has? (2026-10-22)

**Asked by the author:** "are we pulling inspiration from that? If we arent, are we using all the resources in the repo properly?" (about the [quote and character voice reference](../../Story_Files/quote_and_character_voice_reference.md)).  
**Method:** every tracked file outside the archive, the interview transcripts and the generated reports was checked two ways: is it reachable from [AGENTS.md](../../../AGENTS.md), [Before you touch a chapter](../Before-You-Touch-A-Chapter.md) or the two READMEs; and do the [Pass Log](../Pass-Log.md) entries cite it, before P73 and in P73–P84. Then the pages that looked under-used were read.  
**Status:** findings. The fixes that only change where agents look were made in [P85](../Pass-Log.md#p85-2026-10-22-resource-audit); the rest are for the author.

## The answer

**No, not properly.** The records are well linked (nothing outside the archive is orphaned), but the passes have used them for **constraints** (rulings, locks, what not to break) far more than for **aim** (what the writing should sound like). The pages that say what to aim at were the ones skipped:

| Resource | What it is | How it was used | Fix |
| --- | --- | --- | --- |
| [Voice guide](../../Sunday-Morning/Sources/Voice-Guide.md) | **The author's own analysis of how he writes** (Humor, Dialogue, Characters, What to Avoid) | In AGENTS.md's authority list since P76, but **no pass has ever cited it**, and P84 drafted voice lines without reading it | AGENTS.md §6 now sends every drafting pass to it first; EXP-0021 rechecked against it (one lean changed: S1c) |
| [Reading list](../../../Reading-List.md) | His model authors: **Pratchett first** ("Irreverent voice with philosophical weight. Ideas smuggled inside jokes. The tone Pathwell wants."), then Gladstone and Miéville, plus Le Guin, Gardner and three philosophy books | Not reachable from AGENTS.md; cited once, before P73 | AGENTS.md §6, the joke/narrator row |
| [Quote and character voice reference](../../Story_Files/quote_and_character_voice_reference.md) | About 340 lines of tone he approved; only the seed line is his own words | Never read until P84; none of its lines is in the book | AGENTS.md §6, ranked below the voice guide and his drafts |
| [Line notes](../../Sunday-Morning/Line-Notes.md) | His line notes as worked examples (before, after, why) | Reached only through Craft | AGENTS.md §6, the drafting row |
| [forbidden_patterns.md](../../Story_Files/forbidden_patterns.md) | "YOUR documented habits" | Folded into Craft's watch-list; never cited directly | none needed: Craft owns it |

## Found on the way

1. **Some of the author's own Chapter 1 line notes (2026-10-08, R38) are still open.** The [disposition page](CHAPTER-01-R38-CURRENT-DISPOSITION-2026-10-16.md) marks these as waiting on him:
   - the first "Perfect." → his "Good… that's good." ([EXP-0014](experiments/EXP-0014-Ch01-Dialogue-Cuts-and-Bookend-Test-2026-10-16.md));
   - a distinct second unpleasant cue in place of the second "low tide";
   - whether Elizabeth's panic over Nana's cookbook is *felt*;
   - his deletion around "It had been a good party" and the light-switch joke;
   - the "I—" stammer, and blocking around "Huh".
   They're his own notes, so they rank above everything a reader has said since; the reviser's lean is to take his words as written unless one breaks a later ruling.
2. **Stale:** the line-notes page still said "Nothing is applied to the chapters yet." Most of it was applied in P57–P62. Marked.
3. **Stale:** the [narrator register](../../Story_Files/pathwell_narrator_register.md) told agents to read two voice guides first that have since been archived. Marked as background, not authority.
4. **Housekeeping:** a compiled Python cache file was committed. Removed, with a `.gitignore`.

## Not under-used

The rulings ([Decisions](../Decisions.md)), the [Promise Ledger](../Promise-Ledger.md), the [Registry](../Registry.md), the [voice benchmark](../Voice-Benchmark/README.md), [Before you touch a chapter](../Before-You-Touch-A-Chapter.md), the checker and the Sunday Morning definition are cited in nearly every recent pass. The [character](../../Story_Files/character_bible.md) and [world](../../Story_Files/world_bible.md) bibles, [canon](../../Story_Files/canon.md), the [Thesis](../../../Thesis-and-Controlling-Ideas.md) and [Non-Negotiable Scenes](../../../Non-Negotiable-Scenes.md) haven't been cited recently. That's correct for passes that changed single lines, but any pass that touches a scene's job should open them.
