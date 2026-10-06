# Sunday Morning Notes

## Status

**Index. Writing reference: a general guideline for Sunday Morning stories in any setting.** A Sunday Morning story is a low-pressure, character-forward story: a clear premise, a memorable little world, manageable stakes, and people the reader enjoys spending time with. Its promise to the reader: "You do not need to brace yourself."

This folder holds everything needed to make one, or a whole collection: the framework, the author's voice guide, the rules and craft, the step-by-step pipeline, templates for a collection, and the lessons from the first collection (seven stories, 2026-09-27 to 29) and from the Pathwell revision (2026-09-30: writing against sameness, the narrator's voice, AI tells). This copy lives in the Pathwell repository; the 2026-09-30 additions haven't been carried to other copies yet ([D18](Decisions.md#standing-rulings)). It's organized with MAPS_L: **one concept, one owner**, each note labeled by the kind of information it holds and its lifecycle state, and linked rather than repeated. Start here.

Nothing here belongs to any one world. When a collection is set in a particular setting, the setting's own owner pages (its bible or wiki) outrank everything in this folder on setting facts ([Rules: canon discipline](Rules.md#canon-discipline)).

## Order of authority

When two notes pull in different directions, each decides its own ground, in this order. The Framework's place is the author's ruling ([D9](Decisions.md#standing-rulings)); the rest of the order is a working decision ([W7](Decisions.md#working-decisions)).

1. **[Decisions](Decisions.md):** The author's rulings (the D-rows). Nothing below reopens them.
2. **[Framework](Sources/Framework.md):** what a Sunday Morning story is for, and its tone and stakes. "You do not need to brace yourself."
3. **[Rules](Rules.md):** what a story must and mustn't do: tone guardrails, the tie to a larger story, canon discipline, and how to fit a setting.
4. **[Craft](Craft.md):** how the story is told (the Pathwell principles), then how its sentences sound (the [voice guide](Sources/Voice-Guide.md)).
5. **[Registry](Registry.md):** keeps a collection from repeating itself.

[Pipeline](Pipeline.md) is the procedure that applies all five; [Collection](Collection.md) is the guide to making stories work as a set; [History](History.md) is the record of what the first collection taught.

## The notes

| Note | Owns | MAPS_L class | State | Read it when |
| --- | --- | --- | --- | --- |
| [Decisions](Decisions.md) | The author's standing rulings, working decisions waiting for him, the shape of a collection's own decisions list | authority | active | before changing anything a ruling might cover |
| [Framework](Sources/Framework.md) | the Sunday Morning framework, verbatim | authority (imported source) | active, never edited | shaping a premise; the checklist (§20) and template (§23) |
| [Voice Guide](Sources/Voice-Guide.md) | The author's analysis of his own style, verbatim | authority (imported source) | active, never edited | drafting or revising prose |
| [AI tells](Sources/AI-Tells.md) | what research and editors report as common features of AI-generated fiction, each set against the voice guide, with sources; awareness, not rules ([D18](Decisions.md#standing-rulings)) | reference | active | checking a draft for sameness; before a fresh check |
| [Rules](Rules.md) | tone guardrails; connecting to a larger story ("connected, not driven"); canon discipline and promotion; using the saga's main characters; setting rules that still apply; the checklist addendum; building a setting palette | authority / invariant | active | planning a story; checking any pass |
| [Craft](Craft.md) | the 17 storytelling principles, how to use the voice guide, writing how people talk, writing against sameness, lessons from the author's line notes, who writes what (AI or the author), the author's watch-list, the one-line test, the scene diagnostic | skill | active | drafting; reviewing scenes |
| [Pipeline](Pipeline.md) | levels L0–L4, Stage 0 to RECONCILE, routing, the after-every-pass routine, restraint rules | procedure | active | starting, advancing or reviewing any story |
| [Collection](Collection.md) | how a set of stories works together: reading order and expected reader state, cross-story links and the promise ledger, the larger web, collection-level THINK and PLAN; with fill-in templates | procedure + template | active | planning a collection; touching anything another story depends on |
| [Registry](Registry.md) | template: names, name rules, story shapes, devices, joke shapes, stock phrases, watch patterns, checker exceptions | template, read by the checker | copy into each collection; update on every new name or shape change | inventing a name; choosing an opening, device or ending |
| [Reader protocol](Reader-Protocol.md) | how an independent reader reads a story (cold, in order, logging questions as they come), the question bank (space, time, cause, goals, knowledge, who, world rules, reaction, promise, engagement), how to sort open questions, the report format; with research sources | procedure | active (D20) | after every pass, before the author sees it; at L4 |
| [Reader panel](Reader-Panel.md) | how to run several readers so they read differently (by job, reading condition, a short reader's life and model), keep them blind and independent, measure noise with repeat runs, synthesise convergent, lens-specific and minority findings, and check the panel isn't one reader many times; a twelve-lens starting roster; with research sources | procedure | active (D25) | after a full pass on a book; at L4 |
| [Line notes](Line-Notes.md) | worked examples of the author's line notes: each note, the change and the reasoning, grouped by lesson; where push-back adjusted a note and why | evidence | open; add each new set of notes | when a Craft line-notes rule seems arbitrary; before applying new notes |
| [History](History.md) | lessons from the first collection (and, marked, from the Pathwell revision): timeline, check log, what worked, what went wrong and where each lesson lives now | evidence | archive | asking why something is the way it is |

**The checker:** [`tools/sunday_morning_check.py`](tools/sunday_morning_check.py). It reports name clashes, five-word phrases shared across stories, stock phrases, filter verbs, uncontracted narration, very short paragraphs and any watch patterns the Registry lists. It reads a collection's copy of the Registry and its drafts; it never edits. Run it from the repository root:

```text
python3 Story/Sunday-Morning/tools/sunday_morning_check.py --registry <Collection>/Registry.md --drafts <Collection>/Drafts
```

For a single long work kept as plain files (a novel's chapters, say), add `--pattern "Chapter_*.txt"` to read those files in place, and `--min-files 3` so that a callback shared by two chapters isn't reported as repetition.

## Find it fast

| Question | Go to |
| --- | --- |
| What makes a story a Sunday Morning story? | [Framework](Sources/Framework.md) §1; the checklist, [§20](Sources/Framework.md#20-the-sunday-morning-story-checklist) |
| How sad or tense can it get? | [Rules: tone guardrails](Rules.md#tone-guardrails) |
| The stories belong to a bigger saga. How do they tie in? | [Rules: connecting to a larger story](Rules.md#connecting-to-a-larger-story), then [Pipeline: larger-story check](Pipeline.md#larger-story-check) |
| Can a story add a town, name or custom to the setting? | [Rules: canon discipline](Rules.md#canon-discipline) and the [promotion rule](Rules.md#promotion-rule) |
| Can the saga's hero star in one? | [Rules: the saga's main characters](Rules.md#the-sagas-main-characters) |
| Which place, festival or habit should I build from? | [Rules: setting palette](Rules.md#setting-palette) |
| How do I start a new story? | [Pipeline: Stage 0](Pipeline.md#stage-0--add-a-story) |
| How do I start a new collection? | [Starting a new collection](#starting-a-new-collection) |
| What must be true before drafting? | [Pipeline: before the first draft](Pipeline.md#before-the-first-draft) |
| What do I run after a pass? | [Pipeline: after every pass](Pipeline.md#after-every-pass) |
| Something broke while drafting. Where does it go? | [Pipeline: routing table](Pipeline.md#stage-3--do-draft) |
| What does L4 need, and how is the review run? | [Pipeline: Stage 4](Pipeline.md#stage-4--judge-review-independently) |
| How do I get an independent reader's questions on a story? | [Reader protocol](Reader-Protocol.md) |
| How do I run several readers on a book without getting one reader many times? | [Reader panel](Reader-Panel.md) |
| How should the prose sound? | [Craft: voice](Craft.md#voice), then the [Voice Guide](Sources/Voice-Guide.md) |
| Does this sound like a person talking, in narration too? | [Craft: write how people talk](Craft.md#write-how-people-talk) |
| How do I check a scene? | [Craft: scene diagnostic](Craft.md#sunday-morning-scene-diagnostic) |
| Which of the author's habits should I watch for? | [Craft: watch-list](Craft.md#the-authors-watch-list) |
| What should AI write, and what is the author's? | [Craft: who writes what](Craft.md#ai-and-the-author-who-writes-what) |
| Does this read as generated? Is everyone funny the same way? | [Craft: writing against sameness](Craft.md#writing-against-sameness) |
| What's common in AI-written fiction? | [AI tells](Sources/AI-Tells.md) (awareness, not rules) |
| Should the narrator have a voice? | [Craft: voice](Craft.md#voice) (yes, with a register) |
| What order should a collection be read in, and what does the reader know by each story? | [Collection: reading order](Collection.md#reading-order) |
| Which details must match across stories? | [Collection: promise ledger](Collection.md#cross-story-promise-ledger) |
| Is this name taken, or too close to another? | the collection's copy of the [Registry](Registry.md#names), then run the checker |
| Has this opening, ending or device been used? | [Registry: shapes](Registry.md#story-shapes) and [devices](Registry.md#devices-already-used) |
| Did the author already decide this? | [Decisions](Decisions.md) |
| Why is it like this? What went wrong before? | [History](History.md) |

## Starting a new collection

The method and templates live here; each collection's own stories and records live in its own folder. Suggested layout:

```text
Story/
  Sunday-Morning/            this folder: the method, sources, templates, checker
  <Collection>/
    README.md                the collection's index: its one-sentence frame, reading order, and a
                             "Read the stories" list with each story's level (L0–L4)
    Collection.md            its reading order, links, promise ledger and (if any) web, from the Collection guide
    Decisions.md             its own rulings, working decisions and open questions for the author
    Registry.md              a copy of the Registry template, filled in
    History.md               its pass log: one timeline row per collection-wide pass, plus a check log
    Stories/                 one page per story, plus a seeds list for undeveloped premises
    Drafts/                  one prose draft per story
```

Each story page uses this section order: Status, Premise, Protagonist, Place, Cast, Problem, Complications, Running elements, Emotional core, Climax, Soft landing, World anchors, Larger-world thread (if the collection belongs to a saga), Development record.

- **Protagonist through Soft landing** are the Framework's [writing template](Sources/Framework.md#23-writing-prompt-template) (§23), filled in.
- **World anchors** lists the setting's owner pages the story relies on (places, customs, institutions), so canon can be checked.
- **Larger-world thread** holds the answers to the [larger-story check](Pipeline.md#larger-story-check).
- **Development record** holds the Stage 1–5 notes: the THINK pass and PLAN handoff, the scene plan and promise ledger, each pass's change notes (Stage 3 — DO) and the review (Stage 4).

Then follow [Pipeline: Stage 0](Pipeline.md#stage-0--add-a-story).

If the collection is set in a particular world, build its [setting palette](Rules.md#setting-palette) first, and note where the setting's owner pages live.

## Keeping the notes tidy

How this folder grows without becoming a pile:

1. **Find the owner first.** A new fact, rule or lesson goes to the note whose "Owns" column covers it. If none does, add a section to the nearest owner. Create a page only for a genuinely separate concept, and give it a row in the table above and in [Find it fast](#find-it-fast).
2. **Link, don't restate.** Elsewhere, write the local implication in one line and link to the owner.
3. **Rulings go to [Decisions](Decisions.md) first,** then into the page where they apply. A ruling about one collection's stories goes to that collection's own decisions list.
4. **Lessons become method.** Fold a lesson into Pipeline, Craft or Rules. History records only what happened and where the lesson now lives.
5. **Check a concept has a current owner before archiving a note.** A note isn't secondary just because it's one of several on a topic. If no current page owns what it says, fold it into an owner or keep it current. (Pathwell revision: the narrator-register note was archived by mistake.)
6. **Per-story notes stay on the story page** (its Stage 3 — DO section). A collection-wide pass adds one row to that collection's own pass log. A lesson that changes the method is folded into Pipeline, Craft or Rules, and noted in [History](History.md#what-went-wrong-and-where-the-lesson-lives-now).
6. **Keep this folder setting-free.** Anything that names a particular world's places, people or events belongs in that collection's folder or the setting's own pages.
7. **Don't leave a stale snapshot looking current.** Move it to History, marked superseded, or update it.
8. **Sources stay verbatim.** Notes about a source go on the page that uses it, never inside the source.
9. **After any reorganization,** check that every link resolves and run the checker.
