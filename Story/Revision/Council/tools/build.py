#!/usr/bin/env python3
"""Regenerate the council's member cards, roster.json and ROSTER.md from tools/roster_source.py.

Edit roster_source.py (add, change or retire a member), then run from the repository root:

    python3 Story/Revision/Council/tools/build.py
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from roster_source import M

ROOT = os.path.dirname(HERE)  # Story/Revision/Council
os.makedirs(f"{ROOT}/members", exist_ok=True)

GROUND = """**Ground rules**

- Read ONLY the manuscript file named below, and only the parts your reading instructions name, in order, in chunks of about 400 lines. Don't skip, skim or search ahead of where you are. Don't open any other file, folder, note or website; if you do by accident, say so in your report.
- Write only to the output file named below.
- Keep a running log as you read, and don't revise it afterwards. Your first reactions are the data.
- Quote the text exactly and give chapter numbers.
- "I don't know" and "I didn't care" are real answers. Don't guess what the author intended.
- Name what you'd cut before what you'd praise.
- Don't fault an image just because it's physically impossible; fault it if it confuses, repeats or falls flat.
- Don't rewrite the book or write new lines for it. Describe the problem and the direction of a fix."""

CAL = """**How honest to be**

The author has asked for honest, direct, calibrated feedback: no hype, no cruelty. Write as you would to a talented friend whose book you want to get better.

- Measure against published books you know, not against drafts. Don't use "good for a draft" as a compliment.
- Keep praise short, specific and earned. Spend most of your words on what would make the book better.
- If you got bored, confused or unmoved, say where and why.
- Commit to your opinions. Mark your confidence where it matters."""

def brief(x):
    life = x["life"].strip()
    return f"""{GROUND}

{CAL}

**Who you are as a reader**

{life}

**How you read**

Reading condition: {x['condition']}.

{x['job']}

**What you produce**

Write your report to `{{OUT}}`:

{x['produces'].strip()}

Finish with your ranked top ten: the ten things you'd most want the author to hear, most important first.

**The manuscript:** `{{TEXT}}`
"""

roster = []
for i, x in enumerate(M, 1):
    xid = f"{i:02d}"
    fn = f"{xid}-{x['slug']}.md"
    roster.append({"id": xid, "slug": x["slug"], "name": x["name"], "family": x["family"],
                   "stance": x["stance"], "model": x["model"], "condition": x["condition"],
                   "finds": x["finds"], "lean": x["lean"], "file": f"members/{fn}",
                   "chained": x["condition"].startswith("CHAINED")})
    body = f"""---
id: "{xid}"
slug: {x['slug']}
name: {x['name']}
family: {x['family']}
stance: {x['stance']}
default_model: {x['model']}
---

# {xid} · {x['name']}

| | |
| --- | --- |
| **Family** | {x['family']} |
| **Stance** | {x['stance']} (reads for what {'works' if x['stance']=='works' else "doesn't work" if x['stance']=='wrong' else "works and what doesn't"}) |
| **Default model** | {x['model']} |
| **Reading condition** | {x['condition']} |
| **Built to find** | {x['finds']} |
| **Known lean** | {x['lean']} |

The persona name is for the council's bookkeeping only. **Never put it in the brief**: a reader told what kind of reader it is performs the label instead of reading ([Reader Panel: writing a reader's brief](../../../Sunday-Morning/Reader-Panel.md#writing-a-readers-brief)).

## Brief (paste-ready)

Replace `{{TEXT}}` with the path to a frozen copy of the manuscript in the reader's own folder, and `{{OUT}}` with its report path. Send nothing else about the book.

````text
{brief(x)}````
"""
    open(f"{ROOT}/members/{fn}", "w").write(body)

json.dump(roster, open(f"{ROOT}/roster.json", "w"), indent=1)

fams = {}
for r in roster: fams.setdefault(r["family"], []).append(r)
order = ["experience", "craft", "market", "audit", "specialist", "adversarial"]
lines = ["# Council roster", "", f"{len(roster)} members across {len(fams)} families. Generated from `roster.json`; each member's full card and paste-ready brief is in `members/`.", ""]
for f in order:
    lines += [f"## {f.capitalize()} ({len(fams[f])})", "", "| ID | Member | Stance | Model | Reads | Built to find | Known lean |", "| --- | --- | --- | --- | --- | --- | --- |"]
    for r in fams[f]:
        lines.append(f"| {r['id']} | [{r['name']}]({r['file']}) | {r['stance']} | {r['model']} | {r['condition']} | {r['finds']} | {r['lean']} |")
    lines.append("")
open(f"{ROOT}/ROSTER.md", "w").write("\n".join(lines))
print(len(roster), {k: len(v) for k, v in fams.items()})
