# EXP-0015 — First act: motive hinge, counter-order staging, page tear

**Date:** 2026-10-20  
**Status:** CANDIDATES PREPARED AND VERIFIED; **NONE APPLIED TO `Story/Chapters/`; awaiting author**  
**From:** [P66 assessment](../FIRST-ACT-P66-INDEPENDENT-EDITORIAL-ASSESSMENT-2026-10-20.md), A1–A7  
**Control (A) for every candidate:** the chapter text at `63dd26893a66eb58f194f66bee937eab6eb04477` (Ch1 blob `a105bc1c…`, Ch3 blob `7ac8171b…`).  
**Method:** A = current; B = smallest change that addresses the problem; C = a meaningfully different approach, or the rejected option with the reason. Each candidate is a unified diff in this folder; adopt one with `git apply <patch>` from the repository root. Patches, not whole-chapter copies, so nothing stale can be pasted over later canon (the P61/P62 warning about EXP-0014's whole files).

The wording of every new line is offered for the author's ear, not as settled voice. B1 in particular is new interiority and belongs to him under [Writing against sameness](../../Writing-Against-Sameness.md).

---

## Candidate 0 — Elizabeth asks the question (Ch1) — author-proposed, 2026-10-20

**Source.** The author's response to P66's central finding: "rather than her asking 'do you mind' its 'what are you still doing here?'" Her line is his own wording. "Do you mind?" is also his own July line (`765b69b`); the reply "Not at all," was added in a later revision pass.

**Knock-on reviewed under R26.** The current reply only works as an answer to "Do you mind?" (literal reply to a politeness idiom). With the new question it answers nothing, so the reply has to change with it.

**A — current:** “She watched for a moment before interrupting. "Do you mind?"” / “"Not at all," he said, and turned a page.”

**B0 — recommended:** `"What are you still doing here?"` / `He turned a page.`  
Patch: [EXP-0015-B0-Ch01-Still-Doing-Here-Silent.patch](EXP-0015-B0-Ch01-Still-Doing-Here-Silent.patch)

**C0 — alternative:** `"What are you still doing here?"` / `"Reading," he said, and turned a page.`  
Patch: [EXP-0015-C0-Ch01-Still-Doing-Here-Reading.patch](EXP-0015-C0-Ch01-Still-Doing-Here-Reading.patch)

Why B0: the very next lines are “A thud hit the front door. Wet. Heavy.” / “He looked up at the door. Then at her.” With a silent page-turn, her question doesn't get his attention and the thud does, which shows his priorities without a new joke. C0 keeps a spoken dodge in the author's register for Pathwell, but it's a new joke line, which is the author's to write; and every added nonanswer counts against the P65 complaint.

**What it fixes.** The question is now on the page from the first exchange, unanswered and interrupted, so the reader knows the story knows it's open. "Still" also confirms what ¶9 implies: he should have left with the other guests. **It pairs with B1:** she asks in Ch1 and works out her own answer at the Ch3 counter. Without B1 the question is asked but never returned to; without Candidate 0, B1 answers a question nobody asked. Together they are the full fix for P66 A1–A2.

**Cost.** "Do you mind?" was Elizabeth's accommodating politeness even toward an intruder, a trait Ch4 picks up ("You're being awfully polite about it."). The new line is more direct. She is still mild, and Ch4's politeness has plenty of other support, so the cost is small.

---

## Candidate 1 — the motive hinge (Ch3)

**Problem.** Ch1 shows him reading her diary; Ch3 shows a shop that trades in personal writing, his debt to it, and her books treated as property he had no right to spend. Nobody connects the two, and nobody in the book ever asks what he was doing in her apartment. ([P66 A1–A2](../FIRST-ACT-P66-INDEPENDENT-EDITORIAL-ASSESSMENT-2026-10-20.md#a1-pathwells-immediate-motivation-handoff-concern-a))

**A — current** (Ch3):

> “He went back to his ledger, making ticks and carrying ones.”
>
> “"So what do we owe?" Pathwell said.”

**B1 — recommended.** Insert one paragraph between them:

> He went back to his ledger, making ticks and carrying ones.
>
> **Elizabeth thought of Pathwell on her living-room floor, turning the pages of her diary like he was pricing it.**
>
> "So what do we owe?" Pathwell said.

Patch: [EXP-0015-B1-Ch03-Elizabeth-Prices-the-Diary.patch](EXP-0015-B1-Ch03-Elizabeth-Prices-the-Diary.patch)

Why here: it follows the shopkeeper's “He brought outside property into an open transaction”, sits under the image of the ledger, and comes just before Pathwell's “You already owe quite a bit.” exchange, so the reader meets debt, ledger and her diary in one breath. It's a callback to Ch1's “reading her diary like a magazine in a waiting room” and is paid by the shopkeeper's “These were never his to spend.” a page later. The name “Pathwell” is used because the previous sentence's “He” is the shopkeeper.

**C1 — considered and rejected.** Elizabeth asks aloud, e.g. "Is that what you were doing in my boxes?", and Pathwell deflects. This makes the question public, but it adds a fourth nonanswer to a chapter that already has “Pathwell didn't answer.”, “Neither of them answered her.” and “Neither here nor there.”, which is the exact pattern the P65 reader found repetitive. It would also require a new Pathwell line, which is his most author-sensitive register.

| Dimension | A (current) | B1 | C1 (rejected) |
| --- | --- | --- | --- |
| Comprehension | Motive assembled only by the reader, from five scattered clues | Ch1→Ch3 link made, as a suspicion | Link made, then withheld again |
| Characterization | Elizabeth observes the transaction | Elizabeth reads the room and him; footing in a scene the reader said she drifts out of | Elizabeth confronts; Pathwell evades again |
| Voice | — | One plain sentence, contracted register, physical image; flagged for the author's ear | Needs new Pathwell dialogue |
| Pacing | — | +1 line in a slow-build scene | +2–4 lines, another stop |
| Physical continuity | — | Unaffected | Unaffected |
| Emotional impact | Shopkeeper's rebuke lands as moral judgment | Rebuke lands as confirmation of her suspicion; sharper | Rebuke partly pre-empted |
| World rules | — | None stated; consistent with the [character bible](../../../Story_Files/character_bible.md) ("He takes things because his ledger balances") | Same |
| Later plot | Motive never paid | Paid enough: Ch4's “no-good thief”, Ch9's “books nobody had asked him to buy” | Same, with a dangling evasion |

**Risk.** It could read as the narrator explaining. It's in Elizabeth's head and could be wrong (the shopkeeper, not Pathwell, returns the books), which is what keeps it on the right side of that line. If the author's ear says it's too pointed, the fallback is to keep A and rely on the reader test.

---

## Candidate 2 — where the order came from (Ch3)

**Problem.** “The shopkeeper set the order on the counter and looked it over.” The pile has no source. ([P66 A3 and Deliverable C](../FIRST-ACT-P66-INDEPENDENT-EDITORIAL-ASSESSMENT-2026-10-20.md#deliverable-c--chapter-34-continuity-assessment))

**A — current:** “The shopkeeper set the order on the counter and looked it over.”

**B2 — recommended:**

> The shopkeeper turned to the pile at the far end of the counter, the one Pathwell must have built while she was out, and looked it over.

Patch: [EXP-0015-B2-Ch03-Order-Pathwell-Built.patch](EXP-0015-B2-Ch03-Order-Pathwell-Built.patch)

"Must have" keeps it as Elizabeth's inference; it ties his disappearance into the aisles (“moving like he knew the place by feel”) to a result, and makes the shopkeeper's “Did Camp Cunnan ask you for all of this?” land on choices Pathwell made himself. The next two sentences (“Journals, bundles of letters”…, “Enough of it that the counter complained.”) are unchanged and still work.

**C2 — alternative (show, two edits):** when she wakes, "A cup of coffee swung into view, with Pathwell behind it, dust to the elbows."; at the counter, "The shopkeeper dragged the pile at the far end of the counter toward himself and looked it over."

Patch: [EXP-0015-C2-Ch03-Dusty-Sleeves-and-Pile.patch](EXP-0015-C2-Ch03-Dusty-Sleeves-and-Pile.patch)

| Dimension | A | B2 | C2 |
| --- | --- | --- | --- |
| Comprehension | Pile appears | Source and selector stated | Source shown, selector inferable |
| Characterization | — | Reinforces self-appointed buyer | Same, plus a funny image of him |
| Voice | — | Slightly explanatory ("must have") | Shows rather than tells; "dust to the elbows" is a new image |
| Pacing | — | Same length ±1 clause | Two touches, both tiny |
| Physical continuity | Gap | Closed | Closed |
| Emotional impact | — | Neutral | Neutral |
| World rules | — | None | None |
| Later plot | Ch4 crate loading unaffected | Same | Same |

**Lean:** B2 for certainty; C2 if the author prefers showing. Either is better than A.

---

## Candidate 3 — the page tears (Ch1)

**Problem.** The page stays under his palm when the book is pulled away, but the text never says it tore, so a reader can't picture what's holding it. ([P66 A5](../FIRST-ACT-P66-INDEPENDENT-EDITORIAL-ASSESSMENT-2026-10-20.md#a5-chapter-1s-physical-magic-handoff-concern-d))

**A — current:** “Elizabeth grabbed the cookbook by the spine and pulled it from his hands. The sugar-cookie page stayed under his palm.”

**B3 — recommended:** "…The sugar-cookie page **tore free and** stayed under his palm."  
Patch: [EXP-0015-B3-Ch01-Page-Tears-Free.patch](EXP-0015-B3-Ch01-Page-Tears-Free.patch)

**C3 — alternative:** "…pulled it from his hands. **Paper tore.** The sugar-cookie page stayed under his palm."  
Patch: [EXP-0015-C3-Ch01-Paper-Tore.patch](EXP-0015-C3-Ch01-Paper-Tore.patch)

| Dimension | A | B3 | C3 |
| --- | --- | --- | --- |
| Comprehension | Page detaches unexplained | Ordinary tear | Ordinary tear, heard |
| Characterization | — | — | Her grab audibly rips Nana's page; sets up her Ch5 “I broke it.” |
| Voice | — | Invisible | Clinical two-word sentence, in register for action ([narrator register](../../../Story_Files/pathwell_narrator_register.md)) |
| Pacing | — | +3 words | +1 beat in the fastest sequence |
| Physical continuity | Later “ragged edge” has no moment | Moment shown | Moment shown |
| Emotional impact | — | Slight | Stronger: guilt at the instant of grief |
| World rules | — | No new rule | No new rule |
| Later plot | Ch1/3/4 ragged edge, Ch5 confession | Same, now grounded | Same, now grounded |

**Lean:** B3. C3 is the stronger beat if the author is willing to spend the stop.

---

## R1 — orphaned “Again” (Ch1, regression from P62)

**A — current:** “"Because it was hers," he said. Then, "Again, understandable reaction. Reasonable, even.”  
**R1:** `Then, "Understandable reaction. Reasonable, even.`  
Patch: [EXP-0015-R1-Ch01-Orphaned-Again.patch](EXP-0015-R1-Ch01-Orphaned-Again.patch)

P62 cut the earlier `Understandable. But` that this “Again” pointed back to. Dropping the word restores the line's sense and keeps one `Understandable` in the scene, which is what the author's October 8 markup cut from the other line. Mechanical; no voice risk.

---

## Not proposed (and why)

- **No Chapter 3 explanation of Camp's need.** Chapter 4 pays it on arrival.
- **No Chapter 2 cuts.** See [P66 A4](../FIRST-ACT-P66-INDEPENDENT-EDITORIAL-ASSESSMENT-2026-10-20.md#a4-chapter-2s-pacing-and-emotional-logic-handoff-concern-c).
- **No neighborhood line** until the author rules on [Q-O](../../Decisions.md#open-for-the-author).
- **No Chapter 4 healer line** unless a reader raises the cart (A8).
- **Nothing about Pathwell's sensing, the creature's target, or Elizabeth being special.**

## Verification

- Every patch: `git apply --check` passes against `63dd268`. B0+B1+B2+B3+R1 also apply together. C0 conflicts with B0 by design. C2 conflicts with B2 by design (same sentence); C3 with B3.
- Book-wide checker (`sunday_morning_check.py`, Registry, all 18 chapters) run on `63dd268` and on `63dd268` + B1+B2+B3+R1: identical except Chapter 3's paragraph count (139 → 140) and one existing Chapter 3 rate diluted (0.5 → 0.4 per 1,000 words). No new hits.
- Curly-quoted current-text strings in this file were checked against the chapter files; historical text is shown in code formatting.

## Outcome

Open. Recommended set for the author: **R1, B3, B2, B0 + B1** (B0 and B1 are a pair: she asks in Ch1, she works it out in Ch3). The author has chosen Candidate 0's question; the reply (B0 silent or C0 "Reading,") is his pick. If adopted, apply as separate commits, record a pass, and version a new reader edition per P64.
