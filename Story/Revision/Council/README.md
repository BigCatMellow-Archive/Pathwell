# The Council

## Status

**Standing roster, active (R64, 2026-10-28).** This folder holds a large, permanent cast of reader personalities for Pathwell. bt 7274's request:

> "Can we maybe have a council of personalities made on the repo in their own folder, as many as we can really think to have, and then we will pull from those as needed and sometimes randomly to evaluate the book fairly"

The council owns **who** reads. The Sunday Morning [Reader Panel](../../Sunday-Morning/Reader-Panel.md) still owns **how** a group of readers is run, kept blind and combined: the research, the levers, the noise and diversity checks, and the finding records. Read that page before running a large panel. This README is the short version for everyday draws.

**Why it exists.** Over Reads 1–7, readers were often told bt 7274's goals, and they found them. [Read 8](../Reader-Reports/2026-10-27_Read-08_Honest-Editor.md), a cold reader with no goals who was calibrated against published books, scored the book 6/10 and found the problems the earlier reads had softened. The council makes that kind of honest, blind read routine, from many different kinds of reader, so no single personality decides what the book needs.

## What's here

| File | What it is |
| --- | --- |
| [ROSTER.md](ROSTER.md) | All 44 members by family, with each one's stance, default model, reading condition, what they're built to find, and their known lean |
| `members/NN-slug.md` | One card per member: the table above, plus a **paste-ready brief** |
| [LEDGER.md](LEDGER.md) | Every council run: date, who sat, which text, and where the reports went |
| `tools/draw.py` | Draws members (by hand, at random, or both), spreads them across families, skips recent members, and writes filled briefs |
| `tools/roster_source.py` | The source for every card. Edit this file to add or change a member |
| `tools/build.py` | Regenerates the cards, `roster.json` and ROSTER.md from the source |
| `roster.json` | Machine-readable roster, used by `draw.py` |
| `addons/best-version.md` | Optional brief add-on asking for a protect list, prioritized changes and the shape of the best version (round 1) |
| `tools/save_handback.py` | Saves a reader's report from its agent transcript when the reader couldn't write its own file |

## The families

| Family | Count | Reads for | Members |
| --- | --- | --- | --- |
| **Experience** | 15 | how it feels to read | 01–13, 15, 16 |
| **Craft** | 9 | how it's made | 17–25 |
| **Market** | 6 | whether and how it would sell | 27–32 |
| **Audit** | 4 | whether it holds together | 33–36 |
| **Specialist** | 5 | whether a real-world subject rings true | 38–42 |
| **Adversarial** | 5 | the case against | 14, 26, 37, 43, 44 |

A finding counts as strong when members from **different families** reach it independently. Agreement within one family is one kind of reader agreeing with itself.

## Choosing who sits

**1. By question.** Seat the members built for what you need to know, then add at least one random member from a family you didn't pick.

| Question | Start with |
| --- | --- |
| Is it ready? How far off is it? | 17 developmental editor, 27 literary agent, 28 acquisitions editor, 43 hostile reviewer |
| Is it funny? Is the humor its own? | 01 Discworld devotee, 19 sitcom writer, 14 whimsy-allergic, 10 three-star reviewer |
| Does the heart land? | 38 former caregiver, 05 literary-fantasy reader, 02 cozy regular, 44 ending skeptic |
| Is it clear? | 06 reluctant reader, 08 audiobook listener, 36 translator, 29 look-inside browser |
| Does the middle drag? | 25 beat-sheet mapper, 24 middle-starter, 07 commuter skimmer (chained), 11 BookTok reader |
| Do the characters sound alike? | 21 playwright's ear, 18 line editor, 26 machine-prose detector |
| Does the logic hold? | 34 rules lawyer, 37 plot-hole hunter, 33 continuity auditor, 35 logistics clerk |
| Is the ending earned? | 44 ending skeptic, 42 moral philosopher, 04 quiet-ethics reader, 23 rereader (chained) |
| Who is it for, and how long should it be? | 27, 28, 30 indie marketer, 31 novella editor, 32 expansion editor |
| Does the real-world detail ring true? | 38 caregiver, 39 archivist, 40 museum curator, 41 ER nurse |
| Is it fresh or derivative? | 13 long-memory reader, 15 companion-story fan, 03 hidden-world fan |

**2. At random.** bt 7274 asked for random draws too, so no favorite reader becomes the only voice. `draw.py` seats one member per family before it doubles up, and `--avoid-recent` keeps the same members from sitting run after run:

```text
python3 Story/Revision/Council/tools/draw.py --n 5 --avoid-recent 2
```

**3. Mixed** (the usual): pick two or three by question, and let the draw fill the rest.

```text
python3 Story/Revision/Council/tools/draw.py --include 17 --include 19 --n 5 --avoid-recent 2
```

**Sizes.** A quick check uses 3–4 members. A normal round uses 5–6 across at least four families. A big round uses 8–12, with one member run twice on the same model so you can see run-to-run noise (Reader Panel: [the noise check](../../Sunday-Morning/Reader-Panel.md#the-noise-check)).

## Running a draw

1. **Freeze the text.** Assemble `Story/Pathwell.txt`, then copy it into a fresh folder per reader, outside the repo. A reader must not be able to reach the repo, the notes or another reader's report.
2. **Write the briefs.** `draw.py … --text <frozen copy> --briefs <folder>` fills each member's brief with the text path and its own report path.
3. **Launch the readers in parallel and in the background, one agent per member,** on the member's default model unless you're deliberately rotating. Send the brief exactly as written. **Never add** bt 7274's goals, the tone notes, earlier reports, or what you hope they'll find. That's the lesson of Reads 1–8.
4. **Chained members** (07 commuter skimmer, 23 rereader) need several agents. Follow the Reader Panel's [chain procedure](../../Sunday-Morning/Reader-Panel.md#lenses-that-need-more-than-one-agent).
5. **The shared core, second.** When a reader has filed its report, send it the Reader Panel's six [shared-core questions](../../Sunday-Morning/Reader-Panel.md#the-shared-core) by message, so different members can be compared on the same questions.
6. **File it.** Reader agents are usually blocked from writing their own report file, so the report arrives as the agent's final hand-back. `tools/save_handback.py <transcript> <report.md>` saves it without retyping. If an Opus reader stops on an API safety false positive, relaunch the same brief on Sonnet and record the swap. Copy each report to `Story/Revision/Reader-Reports/Council/<date>/<NN-slug>.md` with a provenance line saying which text (commit) it read and which model ran it. Add a row to [LEDGER.md](LEDGER.md).
7. **Triage**, as with the earlier reads:
   - Clear problems are fixed and logged in the [Pass Log](../Pass-Log.md).
   - Anything that changes meaning, adds a beat, or touches bt 7274's own chapters or his rulings goes to him with a lean.
   - Use each member's **known lean** to weigh what it says. One adversarial member alone is a minority report.

## Keeping the council honest

- **Lives come from reading history**, not demographics and not this book's goals. Two members should differ on at least three of these: reading history, patience, what they're carrying, and what they distrust.
- **A brief never names the persona.** Card names like "The Hostile Reviewer" are for bookkeeping only.
- **Every brief carries the same honesty calibration** that made Read 8 useful: published books as the benchmark, short earned praise, opinions committed to.
- **Caveat: these cards were written by the same session that revised the book.** The Reader Panel recommends briefs drafted blind and checked by a separate reviewer agent ([step 3](../../Sunday-Morning/Reader-Panel.md#step-3-write-and-check-the-briefs)). That check hasn't been run on the council yet. Run it before relying on the council for a big decision.
- **All members are Claude.** Many readers from one model converge, and they may be kinder to Claude-revised prose than strangers would be (see the Reader Panel's research section). Rotate models, and treat a real human reader as worth more than any council seat.

## Adding or changing a member

Edit `tools/roster_source.py` and run `python3 Story/Revision/Council/tools/build.py`. Give the new member:

- a reading life of five to eight lines;
- a distinct job, with its own output;
- a reading condition;
- a default model;
- an honest "known lean".

Don't delete a member who has sat in a run. Mark them retired in their lean instead, so the ledger still resolves.
