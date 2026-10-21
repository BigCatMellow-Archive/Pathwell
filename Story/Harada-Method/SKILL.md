---
name: harada-chart
description: Build, extend or review a recursive Harada (Open Window 64) chart that breaks one goal, such as a story's message, into the boxes that achieve it, with every claim checked against source text.
---

# Harada chart

A Harada chart puts one goal in the middle. Around it are the eight things that have to be true to reach it. Each of those can become the middle of its own sheet with eight of its own, as deep as it needs to go.

**Every box answers one question: how does this get us to the box it sits around?** If a box doesn't answer that, it's in the wrong place or it shouldn't exist. Everything below follows from that.

This skill came out of three versions of a chart for a novel (Pathwell), each corrected by its author. The rules are the corrections. The worked example is in `examples/`; the full history is in `Story/Revision/Harada/Chart-Method.md` in the Pathwell repository.

## Files

| File | Open it when |
| --- | --- |
| `SKILL.md` (this file) | Always. It's enough to build a chart. |
| `reference/wording.md` | You're writing or reviewing box titles. Bad-to-good pairs from real charts. |
| `reference/chart-schema.json` | You're writing the JSON by hand or validating someone else's. |
| `examples/pathwell-excerpt.json` | You want to see a finished center, a story-engine box and a character opened to three levels. |
| `scripts/harada_chart.py` | Checking or building. Standard-library Python 3. |
| `assets/chart-template.html` | Only if you're changing how the page looks. The script uses it automatically. |

## Procedure

Work in this order. Don't skip ahead to the boxes; the center decides everything.

1. **Read the sources first.** Read the actual material the chart is about (chapters, specs, code docs) and the owner's own statements of intent (thesis, goals, decisions). The chart claims things about the source, so you need to know it, not summarise it from notes.
2. **Write the center as a message, not an event.** One sentence that the whole work argues and its ending proves. *"The last page earns it"* is a mechanism. *"Choose your own life, ready or not, and let other people choose theirs"* is a message. Its note names where the work proves it. **Mark it as a draft and ask the owner for their words.** Every other box hangs off it.
3. **Pick the eight around the center.** What has to be true for the center to land? Mix two kinds:
   - **Actors** (characters, teams, components) named by what they stand for: *"Pathwell: the one who chooses for everyone"*, not *"Pathwell"*.
   - **Engines**: the mechanisms that carry the message (a misdirection, a rule of the world, a structural echo).

   Test: read the center and the eight aloud as one paragraph. If it doesn't argue the center, change the eight.
4. **Open every actor into the same eight facets** (table below). Use the same facets for every actor so they can be compared at a glance.
5. **Go deeper only where it's needed.** Open a box when the answer to "how does this get to the box above?" has more than one part. Arcs open into steps; steps open into the moments that make them land. Load-bearing and broken places go four or five levels deep. Simple beats stay as one box.
6. **Attach evidence.** Where a box claims something about the source, give the exact words and say which source file. The script checks every one.
7. **Put problems where they hurt.** An open question goes under the box it threatens, with its options as children: A (as it is now), B (smallest fix), C (another approach). Mark them `author`.
8. **Do a wording pass on titles alone.** Read only the titles on one sheet. Could a stranger tell what each box does? Fix the ones that are labels (see `reference/wording.md`).
9. **Check, build, record.** Run the script. Fix every error. Fix each warning or decide it's deliberate. Add a line to the chart's change log saying what changed and why.

## Rules

**The center**
1. It's what the work is saying, not what happens last.
2. Its note shows how the ending delivers it.
3. The owner writes or approves the sentence.

**Every box**

4. It answers: how does this get us to the box it sits around?
5. If it has boxes inside, it has a note saying how it gets to the box above. The page shows this as "How it gets us there".
6. Its title is a statement with a subject and a verb, under about ten words. *"Where the pile came from isn't shown"*, not *"The pile"*.
7. The title says what the box does, not where it is. *"Chapters 1, 3 and 4 depend on the tear"*, not *"Ch1 depends on it"*.
8. Use plain words, the way people talk in a planning meeting. No mannered asides, no "not X, but Y" for effect, no stock phrases.
9. Boxes with no job get cut. Fewer than eight is fine; never pad to eight.

**Actors**

10. Every actor opens into the same eight facets.
11. An actor is named by what they stand for in relation to the center.
12. An arc opens into steps, and each step into the moments that make it land.
13. A group can be one actor if it does one job for the center.

**Depth**

14. Open a box when its "how" has more than one part; otherwise it's a leaf.
15. Go deep where the work is load-bearing or broken.
16. A problem goes under the box it threatens, with A/B/C options as children.

**Evidence**

17. Every quote matches its source exactly. The script fails the build if it doesn't.
18. Proposed wording is never a quote. It goes in `proposed`, shows as "Proposed wording · not in the source yet", and has status `author`.
19. Don't write the owner's creative lines. The chart can say where a line could go, not what it says.
20. Statuses mark only what needs attention: `paid` (it's there), `thin` (there but light), `open` (left open on purpose), `author` (needs the owner).

## The eight facets of an actor

| Facet | Title starts with | It answers |
| --- | --- | --- |
| Start | `Start:` | Who they are when we meet them |
| Wants | `Wants:` | What they're after, and how it changes |
| Needs | `Needs:` | What they actually need and don't know yet |
| Stands for | `Stands for:` | Their part in the argument the center makes |
| In the way | `In the way:` / `Flaw:` / `Blind spot:` | What stops them, inside or outside |
| Arc | `Arc:` | Steps from start to end; each step opens into moments |
| Voice | `Voice:` | How they sound, proved with their lines |
| End | `End:` | Who they are when we leave them |

A facet can be swapped when an actor needs something else (a doomed character might get "His death has to cost something" instead of End). Keep the prefix so the facet's type shows in a small cell.

## The chart file

One JSON file. The full format is in `reference/chart-schema.json`.

```json
{
 "title": "Pathwell Harada Chart",
 "lede": "One or two sentences on how to read it.",
 "footer": "Where it was built from.",
 "labels": {"center": "The message", "centerNote": "What the story is saying", "source": "Ch", "sourceName": "Chapter"},
 "root": {
  "id": "g", "title": "The center sentence", "note": "How the ending proves it.",
  "kids": [
   {"id": "p1", "title": "Elizabeth: the one who learns to choose", "kind": "character", "note": "…", "kids": [
     {"id": "p1-1", "title": "Start: she hands things over before she's decided to", "note": "…", "kids": [
       {"id": "p1-1-1", "title": "Three weeks in, nothing unpacked", "ch": 2,
        "quote": "Three weeks. Twenty-one days of unpacked boxes…", "status": "paid", "note": "…", "kids": []}
     ]}
   ]}
  ]
 },
 "loose": [{"id": "Q-O", "text": "Things not on the chart yet", "status": "author"}]
}
```

- `id`: the root is `g`; its kids are `p1`…`p8`; below that, the parent's id plus `-1`…`-8`.
- `ch`: the source key. For a file named `Chapter_07.txt` it's `7`; for a file with no number in its name, it's the name without the extension.
- Each box needs `title` and `kids`; everything else is optional.

## The script

```text
python3 scripts/harada_chart.py CHART.json --sources "path/to/sources/*.txt"           # check, then build CHART.html
python3 scripts/harada_chart.py CHART.json --sources "…" --check                        # check only
python3 scripts/harada_chart.py CHART.json --sources "…" --from-page saved-page.html    # pull edits made on the page first
```

The built page is one HTML file. It opens in a browser, shows the chart as sheets or as an outline, lets anyone open any box as the center, and lets an editor add or change boxes. Published as a Claude artifact with the `artifact` capability, it saves edits to itself.

**If the owner may have edited the published page, sync before you change anything.** Read the page back, save it, and run `--from-page`. Otherwise you overwrite their work.

## What went wrong before (don't repeat it)

- **One level only.** v1 was a fixed 9×9: eight pillars of eight scenes, and nothing below. The owner: "each box can have its own breakdown as far as needed, so dont just stick to the first breakdown."
- **Labels, not statements.** v2 opened any box, but its titles were scene tags: "The pile", "Help!", "Recalculates", "Seen first". The owner: "Most of the text in the boxes is pretty nondescript."
- **An event at the center.** v1 and v2 put "The last page earns it" in the middle. The owner: "The end goal of the story should be the ending message of what the story is trying to tell."
- **Characters scattered.** v2 spread each character's moments across theme pillars. The owner: characters "need boxes about who they are, what they stand for, their arches."

## Done when

- [ ] The center is a message, its note shows where the ending proves it, and the owner has approved the words (or it's marked as a draft).
- [ ] The center and its eight, read aloud as a paragraph, argue the center.
- [ ] Every actor has the eight facets.
- [ ] Every box with boxes inside has a note.
- [ ] Reading only the titles on any sheet, a stranger could say what each box does.
- [ ] The script passes with no errors, and each warning is fixed or deliberate.
- [ ] Proposed wording is marked `author`; no creative lines were written for the owner.
- [ ] The change log says what changed and why.
