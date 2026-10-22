# EXP-0018 — Whole-book checklist: candidates, and what was withdrawn

**Date:** 2026-10-22  
**Status:** **Leans applied 2026-10-22 ([R58](../../Decisions.md#the-authors-rulings-for-this-revision), [P77](../../Pass-Log.md#p77-2026-10-22-exp-0018-leans-applied-after-a-fresh-check)), as adjusted by the fresh check:** B1 (first cut only), B2 (keeping "No. I would not try."), B3–B8, B10, B11 (attributed as "…hold onto," Shade said.") and C2. **B9 reverted:** the cabinets paragraph sets up "It fits the cabinets." later in Ch17. **C1, C3 and C4 stay open** (no lean). Three items were applied earlier as P73.  
**From:** an external three-read review of the P72 manuscript and its revision checklist (outside this repository). On 2026-10-22 the author asked for the checklist's revisions, scope "Everything", and then asked that this repository's rules be followed. A first, unrecorded draft applied about forty changes directly to an exported copy. Checked against the records, many of them broke rulings. That draft is **discarded**; nothing from it reached the chapters. This page is the corrected version of that work.  
**Control (A):** the chapter text on `main` after P73. Each candidate is a patch in this folder; adopt one with `git apply <patch>` from the repository root.

---

## Applied in P73 (the author's direct answers, 2026-10-22)

| Ch | Change | Note |
| --- | --- | --- |
| 12, 15 | The archive card reads `TWO PAGES USED — SUGAR COOKIES, CHICKEN & DUMPLINGS`; Ch15's echo reads "Two pages used." | **Overrides P23 and P38**, which weighed the card twice and kept "ONE" because only one page was used at Camp. Push-back under R26: the archivist in Ch4 asks "Pages used?" and marks two, so the card now agrees with his own count. If the author meant to keep P23's reading, revert. |
| 18 | "The old scratch was long gone." → "Elizabeth looked at the thin scar between her thumb and wrist." | Matches Ch3 ("the thin line it had left behind"; "scars are outside my wheelhouse") and its placement ("between her thumb and wrist"). Ledger L4 is still paid by "He remembers winning." New narration, kept plain. |
| 18 | "the Shopkeeper" → "the shopkeeper" | Mechanical; lowercase everywhere else. |

## Candidates: repeated beats and continuity (B)

All are cuts or one-line changes. The **lean** is the reviser's under R36.

| # | Ch | Change | Lean | Patch |
| --- | --- | --- | --- | --- |
| B1 | 10 | Cut "Pathwell went still." before "No." and cut "That's not what I asked." Pathwell's "No." then corrects himself unprompted | take | [B1](EXP-0018-B1-Ch10-Ask-Cuts.patch) |
| B2 | 10 | "That wasn't the question." / "No. I would not try." → "Would you try?" / "No." | take, flagged (Elizabeth's line) | [B2](EXP-0018-B2-Ch10-Would-You-Try.patch) |
| B3 | 7 | "Pathwell looked at him. Elizabeth waited. Stansbury looked back at Pathwell." → drop "Elizabeth waited." | take | [B3](EXP-0018-B3-Ch07-Mirror-Line.patch) |
| B4 | 11 | Cut "Pathwell went still." after "I don't need to be rescued." | take | [B4](EXP-0018-B4-Ch11-Still-Cut.patch) |
| B5 | 13 | Cut "Shade went completely still." The next lines carry it ("Shade stared at the seam of light.") | take | [B5](EXP-0018-B5-Ch13-Still-Cut.patch) |
| B6 | 16 | Cut "Pathwell went still." before "Elizabeth continued before he could answer." | take | [B6](EXP-0018-B6-Ch16-Still-Cut.patch) |
| B7 | 17 | "Pathwell looked at him. Elizabeth waited." → drop "Elizabeth waited." | take | [B7](EXP-0018-B7-Ch17-Hearts-Waited.patch) |
| B8 | 15 | Cut "Rain on canvas." and "Bread." from the fire. Both images already ran in Ch14's list (and "rain against canvas" in Ch11); the relief and grief lines stay | take | [B8](EXP-0018-B8-Ch15-Fire-Records.patch) |
| B9 | 17 | Cut the cabinets paragraph from the restitution montage. The same propose/no/comply beat runs six more times; this is the one with no turn in it | take | [B9](EXP-0018-B9-Ch17-Cabinets-Cut.patch) |
| B10 | 18 | "The orange cat" → "Boots", twice. Ties the Ch18 cat to Ch3 by name; the glossary flags Boots as underused | take, low stakes | [B10](EXP-0018-B10-Ch18-Boots.patch) |
| B11 | 13 | **Staging slip.** Shade pockets the queen ("Shade put the queen into one of the green jacket's many pockets."), then "He turned the card over once more." and later takes it out of the jacket again. → "After a while he said, …" | take | [B11](EXP-0018-B11-Ch13-Pocketed-Card.patch) |

After B1–B7, the checker's "goes still" watch pattern drops from 12 to 8, and "Elizabeth waited" from 16 to 14. *(Corrected in P77; the first version gave "10 to 6" from a hand count.)* No replacement move was added: every one is a cut, which is the rule's fix for the replacement tic (Pipeline step 7). B1–B11 apply together.

## Candidates: new text (C), flagged

New lines in the cautious categories, kept plain under [Craft: who writes what](../../../Sunday-Morning/Craft.md#ai-and-the-author-who-writes-what). They are scaffolding for the author to write over. **No lean on C1, C3 or C4:** they're taste.

**C1 — Ch13: Elizabeth plans Shade's life for him, and he stops her.** [patch](EXP-0018-C1-Ch13-Elizabeth-Plans-For-Shade.patch) *(includes B11's fix; apply one or the other.)*

> "You could stay here," Elizabeth said. "Mama Baga wouldn't mind. Milo needs someone to beat at cards. When Pathwell comes, you don't have to talk to him. I could—"  
> "Elizabeth."  
> She stopped.  
> "That's your plan," Shade said. "Let me find mine."

*Why:* the review found Elizabeth is almost never wrong in the back half. This gives her one wrong move, of the same kind as Pathwell's, before her Ch18 "I didn't help him either." Minutes later Shade chooses to stay on his own ("I want to stay here."), so the scene pays it off. *Cost:* it adds dialogue inside an existing scene (R42 allows that; it's not the S1 scene he declined). It also edges Elizabeth toward advocate, which the Ch14 lock forbids **in the confrontation**; here it's before it, and she backs off. *Alternative:* cut to Elizabeth's first sentence and Shade's "I might." *Or* leave Ch13 as it is.

**C2 — Ch5: Thumper planted before the diary is lost.** [patch](EXP-0018-C2-Ch05-Thumper.patch) · lean **take**, flagged

> She sat with one hand on the diary in her coat pocket and didn't sleep at all. Thumper's paw print was in there somewhere.

*Why:* the paw print is the diary's most personal object and appears only in Ch12, one scene before it's given away (Craft 14: memory before loss). *Alternative:* plant it later, in the Ch9 diner where the diary is beside her.

**C3 — Ch17: the gold chain returns.** [patch](EXP-0018-C3-Ch17-Gold-Chain.patch)

> …though not never. Some days her hand went to the gold chain at her throat instead.

*Why:* R41's chain is never seen again after Ch9. *Cost:* an emotional line in Ch17's quiet stretch, which R54 just trimmed of thesis lines. *Alternative:* leave the chain where it is.

**C4 — Ch7: "Leo" before Ch10.** [patch](EXP-0018-C4-Ch07-Leo.patch)

> "Yes! It slipped my mind! Leo, would you please focus!?"

*Why:* "Leo" first appears in Ch10 with no setup. The glossary says only Pathwell uses the name, so the plant has to be his. *Cost:* it edits the author's own line. *Alternative:* leave Ch10 as the first use; the brothers' scene makes it clear enough.

## Withdrawn: checklist items the records rule out

Each of these was in the discarded draft, and a ruling or lock rules it out.

| Checklist item | Why it's out |
| --- | --- |
| Put the sidewalk choice on the page at the end of Ch3 | **R31:** Ch3 ends on "Don't make anything of that."; the choice was cut by the author and lives in Ch4's line, which stays |
| Plainer prune scream in Ch3 ("a million voices") | **R29:** the author restored the million voices ("i thought all that was good?") |
| Three "earlier-draft" lines in Ch1 (the glow, "Recoiling, the blob", "behemoth") | His own prose (voice benchmark); Ch1 changes go through his line review (R38–R52) |
| Compress the Ch5 portal; "Gathering her wits" | From his draft (W14); taste, not continuity |
| Ken calls Stansbury "Leo" in Ch5 | **Glossary:** only Pathwell uses "Leo". See C4 for the version that fits |
| Answer the meeting (a manager's email) in Ch17 | **Q136:** her ordinary-life logistics stay unresolved; **R35(2)** keeps the flat reaction |
| Stansbury explains in Ch17 why the first blob was at her door and that the apartment was never marked | **R35(3)** sets this up for Ch9's "You were never the point", which already pays it; **R27(2)** "marked" is a bluff; the docent pattern |
| Ch18: why he was at the party and reading her diary | Already answered by design: **R48** (the notebook cue in Ch1) and **R53** (her "pricing it" inference in Ch3: "she asks in Ch1, and works out her own answer in Ch3") |
| Ch18: "Lizzy" came from a birthday card in the diary | **R21:** he heard it through Nana's echo; the fallback is the cookbook's inscription, not the diary |
| Ch18: a paragraph weighing the confession before the invitation | **R47** (Version C): the hour of browsing follows the admission and the invitation speaks "without a pardon speech" |
| Ch9: compress the recap of the clues | **R39:** the Oct 12 revision has Elizabeth connect the on-page clues herself; that paragraph is her doing it |
| Ch10: "Who?" / Pathwell won't name who asked for help | Lock 08-22 §4 already keeps it open; the drafted reply spoke the theme (forbidden_patterns §13) |
| Ch14: cut Mama Baga's third "Stop" | **Q145:** she tells him to stop; P68 reviewed Ch14 and proposed no change there |
| Ch17: dry-cleaning ticket "days ago" | Accurate as written |
| Ch3: em dashes in narration | His draft's punctuation; voice, not continuity |

## Verification

- Every patch passes `git apply --check` against `main` after P73. B1–B11 and C2–C4 apply together. C1 and B11 edit the same line, so take one.
- The checker (`--pattern "Chapter_*.txt" --min-files 3`) gives identical output before and after P73.
