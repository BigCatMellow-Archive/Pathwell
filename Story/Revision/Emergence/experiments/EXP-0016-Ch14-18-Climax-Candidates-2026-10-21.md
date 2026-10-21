# EXP-0016 — Chapters 14–18: who he could have called, Shade's position, theme-stating closers

**Date:** 2026-10-21  
**Status:** **AUTHOR-SELECTED 2026-10-21 ([R54](../../Decisions.md#the-authors-rulings-for-this-revision), [P69](../../Pass-Log.md#p69-2026-10-21-author-selected-climax-cuts-from-exp-0016)): B2, B3a and B3b applied; Candidate 1 kept as A (“someone”), so B1 and C1 are not taken.**  
**From:** [P68 review](../CLIMAX-P68-CH14-18-REVIEW-2026-10-21.md), F1–F3  
**Control (A):** the chapter text on `main` after P67. Each candidate is a patch in this folder; adopt one with `git apply <patch>` from the repository root.

---

## Candidate 1 — Ch18: name who he could have called (F1)

**A — now:** “I could have called someone. I didn't.”

**B1 — lean:** `"I could have called Mama Baga. I didn't."` · [patch](EXP-0016-B1-Ch18-Called-Mama-Baga.patch)

**C1:** `"I could have called my brother. I didn't."` · [patch](EXP-0016-C1-Ch18-Called-My-Brother.patch)

| | A “someone” | B1 “Mama Baga” | C1 “my brother” |
| --- | --- | --- | --- |
| What the reader can picture | Leaves them to work out who | Someone in earshot (Ch15), who lifted the crate Pathwell struggled with: “There was no effort in it, no sound of strain.” (Ch4) | Stansbury, on the far side of the wagon, who has fought one before (Ch7) |
| What it says about Pathwell | General guilt | He wouldn't ask the one person who told him to stop. His flaw (deciding alone) in one word | His brother was choosing records at that moment; adds weight between the brothers |
| Risk | Underdefined (P55-01) | Could be read as "she'd have saved him." The line doesn't say so | Same, and Stansbury's Ch7 sword didn't hold the blob, which weakens the case |
| Voice | Author's line | One-word change to the author's line | One-word change to the author's line |

This is the climax confession's key line, so the author owns the wording. B1 and C1 only offer a name.

## Candidate 2 — Ch14: cut “Shade was one breath behind her.” (F2)

**A — now:** “Her shoulder screamed inside the sling. Shade was one breath behind her. Stansbury ran toward the archive from the other side, and Mama Baga shouted for the bucket line.”

**B2:** `Her shoulder screamed inside the sling. Stansbury ran toward the archive from the other side, and Mama Baga shouted for the bucket line.` · [patch](EXP-0016-B2-Ch14-Shade-Not-Behind-Her.patch)

Ch15 opens with Shade “coming toward the fire from the far side of the ruined brass frame”. With the cut, Ch14 doesn't place him until “Shade was still alive.” Cut only; no new words.

## Candidate 3 — end two aftermath chapters before the thesis line (F3)

**B3a — Ch16's last line:** end at `…because morning was going to require things from all of them.` (cuts “and for once Pathwell would not be the person deciding what those things were.”) · [patch](EXP-0016-B3a-Ch16-End-Without-Thesis.patch)

**B3b — Ch17's ending:** end at “Elizabeth smiled.” (cuts “Not because she knew where she wanted to go yet.” / “Because she wanted to go.”) · [patch](EXP-0016-B3b-Ch17-End-On-Her-Smile.patch)

Both are cuts only. The point each line states is already made a paragraph earlier: Camp's “Defined by whom?” / “Not me” in Ch16, and “The thought of going somewhere strange didn't arrive attached to somebody else's hand on the map.” in Ch17.

## Not proposed

- **No new line for Elizabeth after the confession** (F4). Test first; any line there is the author's.
- **No change to “I kept thinking resemblance was enough,”** (F5). Test first.
- **Nothing about who at Camp learns** (F6). That's Q-P, a question, not a patch.
- **“Elizabeth didn't call that redemption. She called it evidence.” stays.**

## Verification

Every patch passes `git apply --check` against `main` after P67. B1 and C1 are alternatives; B2, B3a and B3b apply alongside either.
