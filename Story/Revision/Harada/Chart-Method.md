# How to make a good Harada chart

**Status: active, 2026-10-21.** This page owns the method for the Pathwell Harada chart: what the author asked for, what each version got wrong, and the rules that came out of it. The chart itself is [pathwell-harada.json](pathwell-harada.json); the [README](README.md) says how to open, edit and rebuild it.

The rules are written for Pathwell but most of them are general. A chart for another story, or for a project in MAPS_L, can use the same rules and the same [build script](build_chart.py) with a different source file.

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

## Rules for the center

1. **The center is what the story is saying, not what happens last.** Write it as a sentence the whole book argues and the ending proves. Test: could someone who finished the book say it back to you? v1 and v2 used "The last page earns it", which describes a mechanism, not a message.
2. **Show how the ending says it.** The center's note names the scene that delivers the message. For Pathwell, the last page uses the first page's words with the roles swapped; same words, different person choosing.
3. **The author owns the center sentence.** Draft it from the book's own targets ([Thesis](../../../Thesis-and-Controlling-Ideas.md)), then put it to him. Every other box hangs off it, so it's the one worth getting exactly right.

## Rules for the boxes

4. **Every box answers one question: how does this get us to the box it sits around?** If it doesn't, it's in the wrong place or it shouldn't exist.
5. **Every box that has boxes inside it gets a note saying how it gets to the box above.** That's the "How it gets us there" line on the page. The build script warns when one is missing.
6. **Titles are statements, not labels.** Give them a subject and a verb, and make them say what's true or what happens. "The pile" becomes "Where the pile came from isn't shown." "Help!" becomes "He yells for help." Under about ten words; the script warns past 70 characters.
7. **Say what the box does, not where it is.** "Ch1 depends on it" points at a location. "Chapters 1, 3 and 4 depend on the tear" says why it matters.
8. **Plain words, in the book's register.** Write how people talk ([Writing Principles](../../../Writing-Principles.md); [AI tells](../AI-Tells.md)). No mannered asides, no "not X, but Y" for effect, no stock phrases. A box is a sentence someone would say out loud in a planning meeting.
9. **Cut boxes with no job.** If a beat only restates its quote ("Recalculates" for "Huh."), drop it. Fewer than eight is fine; empty slots are honest. Never pad to eight.

## Rules for characters

10. **A character is a box, and it opens into the same eight facets every time.** That makes characters comparable at a glance:

    | Facet | What it answers |
    | --- | --- |
    | Start | Who they are when we meet them |
    | Wants | What they're after, and how it changes |
    | Needs | What they actually need, which they don't know yet |
    | Stands for | Their part in the story's argument (from the Thesis table) |
    | In the way | Their flaw, blind spot, or the people blocking them |
    | Arc | The steps from start to end; each step opens into the moments that build it |
    | Voice | How they sound, with lines that prove it ([character bible](../../Story_Files/character_bible.md), "Where each character's humour comes from") |
    | End | Who they are on the last page they're in |

    A facet can be swapped when the character needs something else (Pathwell has "Flaw" and "Blind spot"; Shade has "A person in small things" and "His death has to cost something"). Keep the facet name as a prefix ("Wants: …") so the type is clear in a small cell.
11. **Name the character by what they stand for.** "Elizabeth: the one who learns to choose", not "Elizabeth". The title should already connect them to the center.
12. **Arcs go down to scenes, and scenes go down to moments.** Arc → step (one per chapter or turn) → the moments that make the step land, each with its quote.
13. **Groups can be characters.** Mama Baga and Camp share one box because they do one job for the message: help that asks first.

## Rules for depth

14. **Open a box when its "how" has more than one part.** If the answer to "how does this get to the box above?" is a single quote, it's a leaf. If it takes several moments, it opens.
15. **Go deep where the story is load-bearing or broken.** The climax, the confession and the open problems go to four or five levels. Simple beats stay as one box.
16. **Put each problem under the box it threatens.** The motive gap sits under "She was never the point"; the page tear under "The magic spends real lives". Its children are the options: A (now), B (smallest fix), C (another approach).

## Rules for evidence

17. **Every manuscript quote is checked against its chapter** by the build script. A quote that drifts from the text fails the build.
18. **Proposed wording is never a quote.** It goes in its own field, shows on the page as "Proposed wording · not in the manuscript", and is marked as needing the author.
19. **New emotional lines belong to the author** ([Writing against sameness](../Writing-Against-Sameness.md)). The chart can say where a line could go; it doesn't write the line.
20. **Status marks only what needs attention:** on the page, thin, open on purpose, needs the author. They follow the [Promise Ledger](../Promise-Ledger.md).

---

## Check before publishing

- [ ] Read the center and the eight around it aloud as one paragraph. Does it argue the message?
- [ ] Open three boxes at random. Do the boxes inside add up to the box?
- [ ] Read only the titles on one sheet. Could a stranger tell what each box does?
- [ ] `python3 Story/Revision/Harada/build_chart.py` passes with no errors, and the warnings are either fixed or deliberate.
- [ ] Anything new that's proposed wording is marked as needing the author.

---

## Change log

| Date | Version | Change |
| --- | --- | --- |
| 2026-10-20 | v1 | First chart: ending at the center, eight pillars, 64 verified beats. |
| 2026-10-20 | v2 | Recursive: any box opens; 379 boxes; editing and saving on the page. (H2) |
| 2026-10-20 | v3 | Rebuilt around the message; characters with eight facets each; every box reworded as a statement of what it does; 464 boxes. (H3) |
| 2026-10-21 | v3.1 | Moved into the repo with the build script and this page. The script's first run caught six boxes with boxes inside and no note; notes added. (H4) |

## Still open

- **The center sentence** is a draft from the Thesis page. It needs the author's words (rule 3).
- **The Chapter 1 boxes still show "Do you mind?"**, because the author's "What are you still doing here?" isn't in the manuscript yet. When it lands, update those boxes and rebuild; the quote check will fail until they match.
- **Wording pass.** v3's titles are a first pass at the new standard. The author's corrections to individual boxes are the best guide for the next version; record what he changes and why in this log.
