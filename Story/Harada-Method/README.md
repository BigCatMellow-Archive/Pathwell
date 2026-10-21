# Harada method

**Status: active, 2026-10-21. A method, like [Sunday-Morning](../Sunday-Morning/README.md): how to build a Harada chart, not a chart itself.** Pathwell's chart, which this method was learned from, is in [Story/Revision/Harada](../Revision/Harada/README.md).

A Harada chart puts one goal in the middle, the eight things that get you there around it, and lets any of those open into eight of its own, as deep as needed. Every claim about the source is checked against the source.

## For an agent

Start at **[SKILL.md](SKILL.md)**. It's self-contained: the procedure, the twenty rules, the eight facets for an actor, the file format, the script, and what went wrong before. Open the other files only when SKILL.md points you to them.

The folder is portable. Copy it whole into another project or another agent's skills folder; nothing in it depends on Pathwell except the example.

| File | What it is |
| --- | --- |
| [SKILL.md](SKILL.md) | The method. Read first. |
| [reference/wording.md](reference/wording.md) | How to word boxes, with real before-and-after pairs |
| [reference/chart-schema.json](reference/chart-schema.json) | The chart file's format (JSON Schema) |
| [examples/pathwell-excerpt.json](examples/pathwell-excerpt.json) | A finished example: the center, one actor through its eight facets, one engine with a problem broken into options |
| [scripts/harada_chart.py](scripts/harada_chart.py) | Checks a chart against its sources and builds its page. Python 3, standard library only. |
| [assets/chart-template.html](assets/chart-template.html) | The page the script builds: sheets, outline, open any box, edit and save |

## Try it

From the Pathwell repository root:

```text
python3 Story/Harada-Method/scripts/harada_chart.py Story/Harada-Method/examples/pathwell-excerpt.json --sources "Story/Chapters/Chapter_*.txt"
```

That checks the example's quotes against the chapters and builds `examples/pathwell-excerpt.html`.
