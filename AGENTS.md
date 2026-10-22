# AGENTS.md — Pathwell

The operating contract for any AI agent working in this repository. It follows [MAPS_L](https://github.com/BigCatMellow/MAPS_Lean/wiki) at **method-only depth**: one owner, a small number of bounded jobs, written evidence, independent checks. It adds no rules about the story. Those live in the records it points to.

Pathwell is the author's novel. Your job is to help him become more himself, not to supply a substitute voice.

## 1. Authority

**This file governs how agents work.** The story is governed by the author's rulings and the book's targets, in the order the revision README sets ([order of authority](Story/Revision/README.md#order-of-authority)):

1. **The author's rulings.** The R-rows and locks in [Decisions](Story/Revision/Decisions.md), which index his [Bible interview](Story/Interview/README.md) answers (Q1–Q149).
2. **The book's targets.** [Thesis](Thesis-and-Controlling-Ideas.md), [Non-Negotiable Scenes](Non-Negotiable-Scenes.md), [Writing Principles](Writing-Principles.md); for world facts, [canon.md](Story/Story_Files/canon.md).
3. **Craft, procedure and some of the tone.** The [Sunday Morning notes](Story/Sunday-Morning/README.md), as this book adapts them. They exist to protect a feeling first ([what it's for](Story/Sunday-Morning/README.md#what-its-for)). Pathwell keeps some of that tone ([R24](Story/Revision/Decisions.md#the-authors-rulings-for-this-revision)): warmth, people the reader enjoys spending time with, a soft landing after the hard moments, without losing the book's weight.
4. **Voice.** The [voice guide](Story/Sunday-Morning/Sources/Voice-Guide.md), [pathwell_prose_voice.md](Story/Story_Files/pathwell_prose_voice.md), the [narrator register](Story/Story_Files/pathwell_narrator_register.md), and the author's own text in the [voice benchmark](Story/Revision/Voice-Benchmark/README.md).
5. **[Registry](Story/Revision/Registry.md).**

On a conflict, follow the higher source; don't blend them. A lower page that disagrees is stale: fix it in scope, or report it. A reference is authoritative but fallible. Check the chapters before "fixing" them to suit a bible ([R39](Story/Revision/Decisions.md#the-authors-rulings-for-this-revision)).

**Not authority:** anything in [Story/Archive](Story/Archive/README.md); exports, summaries and assembled copies; candidates the author hasn't picked; reader reports and reviews (evidence only); your own memory of an earlier session.

## 2. Who owns what

| Role | Owns | Doesn't |
| --- | --- | --- |
| **The author** | the objective, every ruling, taste, and the final read (L4) | approve routine steps inside work he's already asked for |
| **The reviser** (the agent he's working with) | the pass from start to finish: recovering state, shaping candidates, applying his picks, checks, records, the report | change his rulings, settle taste, or review its own text |
| **Helpers** (fresh check, cold reader, reader panel, tenth seat) | one bounded job, returning evidence | write prose, widen scope, or rule on anything |

Delegation hands off the work, never the ownership. A helper's verdict is evidence for the reviser to reconcile, not a decision.

## 3. Reading budget

Don't read the whole repository; it's far larger than the book. For a normal task, read:

```text
this file
+ Before you touch a chapter      (always)
+ Revision-Status.md and the latest Pass Log entry   (where things stand)
+ the chapter(s) in scope, and the Decisions rows that touch them
+ one method page for the job     (section 6)
```

Add other sources only when the work needs them: the interview when a lock's exact wording matters; the Promise Ledger before changing anything planted or paid; the Decision Timeline only to trace when a ruling arrived.

## 4. What needs the author

Ask first, or put it in a candidate for him to pick, when a change would:

- alter chapter prose he hasn't picked, beyond the small edits he asked for;
- add or change a joke, emotional line, character-defining line, metaphor or narrator comment ([who writes what](Story/Sunday-Morning/Craft.md#ai-and-the-author-who-writes-what));
- override or reinterpret any ruling or lock, including through a broad request ("everything" means propose everything, not override earlier rulings);
- settle anything the records leave open on purpose, or add new lore, mechanics or backstory ([R23](Story/Revision/Decisions.md#the-authors-rulings-for-this-revision): use what the book already has);
- archive, delete or restructure a record.

Inside that boundary, don't ask permission for routine steps. On your own questions, take your lean, apply it and list it for him to overrule ([R36](Story/Revision/Decisions.md#the-authors-rulings-for-this-revision)). Push back when a request or note has a cost, with the reason and an alternative ([R26](Story/Revision/Decisions.md#the-authors-rulings-for-this-revision)). Don't agree just to agree.

## 5. The loop

1. **Recover the current state.** Read [Revision-Status](Revision-Status.md), the last [Pass Log](Story/Revision/Pass-Log.md) entry, and the open questions in [Decisions](Story/Revision/Decisions.md#open-for-the-author). Some status pages lag behind; the Pass Log and the chapters are the evidence.
2. **State what done looks like** for this pass, in one line.
3. **Check it against the records:** [Before you touch a chapter](Story/Revision/Before-You-Touch-A-Chapter.md), the ruling rows, the [Promise Ledger](Story/Revision/Promise-Ledger.md).
4. **Do the smallest change that meets it.** If the author hasn't picked it, write it as a candidate (section 7).
5. **Verify.** Run the [after-every-pass routine](Story/Revision/README.md#after-every-pass), including the checker. Independent checks go to helpers that didn't write the text.
6. **Reconcile the records:** Pass Log entry, R-row for any new ruling, [Revision-Status](Revision-Status.md), the ledger, the [Emergence index](Story/Revision/Emergence/INDEX.md).
7. **Commit** after each step ([R8](Story/Revision/Decisions.md#the-authors-rulings-for-this-revision)), then **report** (section 9).

Stop when the pass is done, when you reach something only the author can decide, or when you're waiting on him. Don't stop early while asked-for work remains, and don't invent new work after it's done.

## 6. Which method page, for which job

| Job | Open |
| --- | --- |
| Any change to a chapter | [Before you touch a chapter](Story/Revision/Before-You-Touch-A-Chapter.md) |
| Drafting or revising prose | the author's [voice guide](Story/Sunday-Morning/Sources/Voice-Guide.md) (his own analysis of how he writes: read it whole before a pass that writes), [Craft](Story/Sunday-Morning/Craft.md), then [Writing against sameness in Pathwell](Story/Revision/Writing-Against-Sameness.md); his [line notes](Story/Sunday-Morning/Line-Notes.md) are the worked examples |
| Exact words, a sentence or a paragraph | [Line-editing protocol](Story/Sunday-Morning/Line-Editing-Protocol.md) (§7 for small edits) |
| A scene's job | the [scene diagnostic for Pathwell](Story/Revision/README.md#scene-diagnostic-for-pathwell) |
| A character's reaction or motive that isn't landing | [Craft: character discovery](Story/Sunday-Morning/Craft.md#character-discovery-before-explanation) |
| Finishing a pass | [after every pass](Story/Revision/README.md#after-every-pass), reported step by step (D23) |
| An independent read | [Reader protocol](Story/Sunday-Morning/Reader-Protocol.md); several readers: [reader panel](Story/Sunday-Morning/Reader-Panel.md) |
| Testing a consequential decision nobody has argued against | [the tenth seat](Story/Sunday-Morning/Pipeline.md#the-tenth-seat-narrow-d21); reports go in [Tenth-Seat](Story/Revision/Tenth-Seat/) |
| Sameness or AI tells | [AI tells in Pathwell](Story/Revision/AI-Tells.md) (awareness, not rules; detector scores aren't targets, [R17](Story/Revision/Decisions.md#the-authors-rulings-for-this-revision)) |
| Setups and payoffs | [Promise Ledger](Story/Revision/Promise-Ledger.md) |
| A joke, an emotional line or a narrator comment, before drafting one | for what to aim at: the voice guide's *Humor*, *Dialogue* and *What to Avoid* sections, and the [reading list](Reading-List.md) (Pratchett first: "ideas smuggled inside jokes"). For how he does it: his own drafts in the [voice benchmark](Story/Revision/Voice-Benchmark/README.md). For tone to borrow: the [quote and character voice reference](Story/Story_Files/quote_and_character_voice_reference.md), a bank of lines and tones he approved (a resource, not a rule; only its seed line is his own words, none of it is in the book yet, and the voice guide outranks it: "not every line should be quotable") |
| World facts, names, characters | [Story_Files](Story/Story_Files/README.md): canon, world and character bibles, [glossary](Story/Story_Files/glossary.md) |
| What a chapter must accomplish | its contract in the [chapter contract matrix](Story/Story_Files/PATHWELL_MAPS_L_CHAPTER_CONTRACT_MATRIX_2026-08-28.md); later rulings win |

## 7. Records, and where things go

- **The manuscript** is `Story/Chapters/Chapter_01–18.txt` ([R3](Story/Revision/Decisions.md#the-authors-rulings-for-this-revision)). `Story/assemble_manuscript.py` writes `Story/Pathwell.txt` from them; that file is derived, and may lag.
- **Candidates** go in `Story/Revision/Emergence/experiments/`: an `EXP-NNNN` page with a control (the current text), one patch per candidate, a lean or "no lean" on each, and a check that every patch applies. Copy the newest EXP page for the shape. The author picks; picks are applied verbatim.
- **Reviews and findings** go in `Story/Revision/Emergence/`, and helpers' reports in `Reader-Reports/` and `Tenth-Seat/`. Each is indexed in the [Emergence index](Story/Revision/Emergence/INDEX.md).
- **Ideas and lessons** are `IDEA-NNNN` and `INS-NNNN` pages. A lesson that changes how the work is done is folded into the method page that owns it, not left as a note.
- **One concept, one owner.** Before creating a page, find the page that already owns the concept and add to it. Link, don't restate.
- **One current version of anything** ([R16](Story/Revision/Decisions.md#the-authors-rulings-for-this-revision)). Superseded material moves to [Story/Archive](Story/Archive/README.md) in the same change, with a line in its index saying what replaced it.
- **Keep UNKNOWN unknown.** Don't fill a gap in the records with a guess. Mark it open and ask, or take a lean and list it.

## 8. Independence

The agent that wrote a text can't be the one that passes it. Fresh checks, cold readers and tenth seats are separate helpers. Give each one the chapters, the task and the primary records it needs (the ruling's own row, the lock's own paragraph), not your summary of them. Readers stay blind to the goals and to each other ([reader panel](Story/Sunday-Morning/Reader-Panel.md)). An informed read, including the reviser's own, never counts as the blind read L4 needs.

## 9. Reporting to the author

Lead with the result, the decision he needs to make, or what's blocked. Then:

- **Done / Changed / Verified / Blockers**, leaving out any that are empty;
- the after-every-pass steps, each marked done, skipped (with the reason) or not applicable (D23);
- every lean you took, so he can overrule it;
- questions one at a time, each with your lean.

Don't narrate routine steps, and don't turn status into requests for permission.

## 10. House rules

- Refer to him as **"the author"** in files, filenames and commit messages. Never by name.
- Revise from his own drafts where they exist ([W14](Story/Revision/Decisions.md#working-decisions)). Don't smooth his lines toward "better writing".
- The book's length is whatever it naturally is ([R42](Story/Revision/Decisions.md#the-authors-rulings-for-this-revision)).
- The method in `Story/Sunday-Morning/` stays setting-free. Pathwell-specific application goes in `Story/Revision/`.
