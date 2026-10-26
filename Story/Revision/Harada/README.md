# Pathwell Harada chart

**Status: active chart, v4 thematic candidate, 2026-10-21. A planning view of the book, not part of the manuscript and not an authority over it.** The [order of authority](../README.md#order-of-authority) still decides: the author's rulings, then the book's targets, then canon. Where the chart and the chapters disagree, the chapters win and the chart gets fixed.

The chart currently proposes **“Control is not competence; others pay when you decide for them.”** as its central *working* message, derived from the author's existing controlling-idea page and direct chapter evidence, **not yet approved final theme wording**. Around it are four individual character arguments (Elizabeth, Pathwell, Shade, Stansbury), a Camp/Mama Baga collective counterexample, and three story engines (the false target, the price of magical spending, the changed meaning of the first and last pages). Any significant box opens recursively as deep as the story warrants, without padding to eight. All 407 manuscript quotations remain source-checked, but quotation matching alone does not prove that an unprimed reader experiences the theme. See the [full 18-chapter thematic audit](THEMATIC_AUDIT_2026-10-21.md).

**How to make a good one:** the general method, [Story/Harada-Method](../../Harada-Method/SKILL.md). **How this one got better:** [Chart-Method.md](Chart-Method.md).

## What's here

| File | What it is |
| --- | --- |
| [pathwell-harada.md](pathwell-harada.md) | **The chart for an agent to read.** The whole chart as a Markdown outline: how to read it, the shape at a glance, the open decisions with their options, then every box in order with its note, quote and status. Generated; don't edit it. **Hand this file to another agent.** |
| [pathwell-harada.json](pathwell-harada.json) | **The chart's source.** Every box: title, chapter, quote, status, note, proposed wording, boxes inside. Edit this, or edit on the page and sync. |
| [Chart-Method.md](Chart-Method.md) | The author's rulings (H1–H4), the before-and-after of each version, how this chart applies the method's rules, the change log |
| [THEMATIC_AUDIT_2026-10-21.md](THEMATIC_AUDIT_2026-10-21.md) | Full Chapter 1–18 evidence map, why the earlier center was insufficient, counterexamples, checks across 464 nodes / 407 quotes, and what remains author- or reader-dependent |
| [build_chart.py](build_chart.py) | Runs the method's [checker and builder](../../Harada-Method/scripts/harada_chart.py) with Pathwell's paths: quotes against chapters, at most eight boxes inside any box, ids, statuses, wording warnings; then builds the page |
| [pathwell-harada.html](pathwell-harada.html) | The chart page for people: sheets, outline, open any box, edit. Generated. |
| [versions/](versions/) | Each version as it stood, so the improvements can be compared |

The published copy of the chart is a private page in the author's Claude artifacts (*Pathwell Harada Chart*). It can be edited there: **Edit**, change or add boxes, **Save to page**.

## Updating it

From the repository root:

```text
python3 Story/Revision/Harada/build_chart.py          # check, then build pathwell-harada.html and pathwell-harada.md
python3 Story/Revision/Harada/build_chart.py --check  # check only
```

If the chart was edited on the published page, save that page's HTML (Claude can read it back from the artifact) and pull the edits in before changing anything else:

```text
python3 Story/Revision/Harada/build_chart.py --from-page saved-page.html
```

Then commit the JSON and the rebuilt page and outline together, add a line to the [change log](Chart-Method.md#change-log), and republish the page if the change was made here rather than there.

**When the manuscript changes,** run the check. A quote that no longer matches its chapter fails the build and names the box, so the chart can't quietly drift from the book.
