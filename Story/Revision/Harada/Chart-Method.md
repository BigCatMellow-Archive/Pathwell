# How to make a good Harada chart

**Status: active, 2026-10-21.** This page owns the method for the Pathwell Harada chart: what the author asked for, what each version got wrong, and the rules that came out of it. The chart itself is [pathwell-harada.json](pathwell-harada.json); the [README](README.md) says how to open, edit and rebuild it.

The general method (rules, procedure, checker, viewer) is [Story/Harada-Method](../../Harada-Method/SKILL.md). This page keeps what's specific to Pathwell: the author's rulings, how the chart got better, and its change log.

---

## What the chart is

A Harada chart (the Open Window 64) puts one goal in the middle of a 9×9 sheet. The eight boxes around it are what has to happen to reach the goal. Each of those eight sits at the center of its own 3×3 block, with eight boxes of its own around it.

The Pathwell chart takes one step further: **any box can be opened as the center of its own sheet.** So a box can break down as far as it needs to, and different boxes go to different depths.

---

## What the author asked for

His words, in order. These are the method's rulings; the rules below are how they're carried out.

| # | Date | The author | What it decided |
| --- | --- | --- | --- |
| H1 | 2026-10-20 | "I want to see if that would help organize the story we have here, starting with lets say the ending of the story or the goal of the story in the center and expanding out as needed" | Start from the ending. Expand only where needed. |
| H2 | 2026-10-20 | "the key here is that each box can have its own breakdown as far as needed, so dont just stick to the first breakdown" | Every box can open into its own sheet, as deep as it needs. |
| H3 | 2026-10-20 | "Most of the text in the boxes is pretty nondescript, and just not great to be honest. We need to work on how we word things and what we are putting in those boxes. The end goal of the story should be the ending message of what the story is trying to tell, that boxes around that are how we get to that point, those boxes have boxes around how you get to those points. Some boxes will have characters and those will blneed boxes about who they are, what they stand for, their arches etc" | The center is the story's message, not its last event. Every box is how you get to the box it sits around. Characters get their own breakdown. The wording has to say something. |
| H4 | 2026-10-21 | "lets make sure we are updating this to the repo along with the process of improvement so that we can understand how to make the best charts going forward" | This page, the chart source and its version history live in the repo. |

---

## How the chart improved

Three versions in one day. Each is saved in [versions/](versions/) so the difference can be seen, not just described.

| Version | Boxes | Levels | Center | What was wrong with it |
| --- | --- | --- | --- | --- |
| [v1: pillars](versions/v1-2026-10-20-pillars.json) | 73 | 2 | "The last page earns it" | A fixed 9×9: eight pillars of eight beats, and nothing below that. Every beat was a scene with a quote. (H2) |
| [v2: recursive](versions/v2-2026-10-20-recursive.json) | 379 | 4 | "The last page earns it" | Any box could open, and it went deep where the story did. But the center was an event, the boxes were scene tags, and characters were spread across pillars instead of having their own sheets. (H3) |
| [v3: message first](versions/v3-2026-10-20-message-first.json) | 464 | 5 | "Choose your own life, ready or not, and let other people choose theirs" | The current shape. Center is the message; around it, five characters and three story engines; every box says what it does for the box above. Its first check found six boxes with no note (v3.1 fixed them; see rule 5). |

### The same boxes, three times

The clearest way to see what changed is to follow a few boxes through the versions.

| What the box is about | v1 | v2 | v3 |
| --- | --- | --- | --- |
| The center | "The last page earns it" | "The last page earns it" | "Choose your own life, ready or not, and let other people choose theirs" |
| Elizabeth | "Elizabeth chooses her way here" (a pillar of eight scenes) | same | "Elizabeth: the one who learns to choose", which opens into start, wants, needs, stands for, in her way, arc, voice and end |
| The blob at the door in Ch1 | "At the door before any magic" | "Seen first" | "Something was at her door before any magic" |
| Pathwell's first reaction | (not there) | "Assumes she knows" | "He thought she'd know" |
| His "Huh." | (not there) | "Recalculates" | dropped: it had no job of its own |
| The Ch3 counter order | (not there) | "The pile" | "Where the pile came from isn't shown" |
| Shade caught in the fire | "Fights to live" | "Help!" | "He yells for help", inside "He fights to live", inside Shade's arc |
| The page-tear fix | "The page tears" | "Ch1 depends on it" | "Chapters 1, 3 and 4 depend on the tear" |

v1's problem was depth. v2's problem was words: "The pile", "Help!" and "Recalculates" are labels. They tell you where you are in the book, not what the box is doing for the box above it.

---

## The rules

The rules that came out of these corrections now live in the general method, [Story/Harada-Method/SKILL.md](../../Harada-Method/SKILL.md), so any chart (Pathwell or not) uses one copy. They keep the same numbers: rules 1–3 for the center, 4–9 for every box, 10–13 for actors, 14–16 for depth, 17–20 for evidence. Bad-to-good title pairs from this chart are in its [wording reference](../../Harada-Method/reference/wording.md).

How this chart applies them:

- **Center (rules 1–3):** drafted from the [Thesis page](../../../Thesis-and-Controlling-Ideas.md); still waiting on the author's words.
- **Actors (rule 10):** Elizabeth uses the eight standard facets. Pathwell swaps Needs for **Flaw** and **Blind spot**. Shade swaps Needs and End for **A person in small things** and **His death has to cost something**. Stansbury and Camp use facets that fit their smaller roles. Mama Baga and Camp share one box (rule 13).
- **Engines:** she was never the point; the magic spends real lives; the last page answers the first.
- **Problems (rule 16):** the motive gap sits under "She was never the point", the page tear under "The magic spends real lives", the Chapter 3 order on Pathwell's arc. The options come from EXP-0015 in the P66 review ([PR #4](https://github.com/BigCatMellow-Archive/Pathwell/pull/4); it moves into `Story/Revision/Emergence/experiments/` when that merges).
- **Statuses (rule 20)** follow the [Promise Ledger](../Promise-Ledger.md).

## Change log

| Date | Version | Change |
| --- | --- | --- |
| 2026-10-20 | v1 | First chart: ending at the center, eight pillars, 64 verified beats. |
| 2026-10-20 | v2 | Recursive: any box opens; 379 boxes; editing and saving on the page. (H2) |
| 2026-10-20 | v3 | Rebuilt around the message; characters with eight facets each; every box reworded as a statement of what it does; 464 boxes. (H3) |
| 2026-10-21 | v3.1 | Moved into the repo with the build script and this page. The script's first run caught six boxes with boxes inside and no note; notes added. (H4) |
| 2026-10-21 | v3.2 | The method split out as a skill other agents can use ([Story/Harada-Method](../../Harada-Method/SKILL.md)): procedure, rules, wording reference, schema, a general checker and viewer, and an excerpt of this chart as the worked example. This chart now builds with it; the chart's content didn't change. |

## Still open

- **The center sentence** is a draft from the Thesis page. It needs the author's words (rule 3).
- **The Chapter 1 boxes still show "Do you mind?"**, because the author's "What are you still doing here?" isn't in the manuscript yet. When it lands, update those boxes and rebuild; the quote check will fail until they match.
- **Wording pass.** v3's titles are a first pass at the new standard. The author's corrections to individual boxes are the best guide for the next version; record what he changes and why in this log.
