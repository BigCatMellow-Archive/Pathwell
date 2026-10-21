# EXP-0017 — Chapters 5–13: three cuts and one spelling question

**Date:** 2026-10-21  
**Status:** **AUTHOR-SELECTED 2026-10-21 ([R56](../../Decisions.md#the-authors-rulings-for-this-revision), [P72](../../Pass-Log.md#p72-2026-10-21-author-selected-middle-cuts-from-exp-0017)): B1, B2 and B3 applied; the diner sign stays DINER, so Q1 is not taken.**  
**From:** [P71 review](../MIDDLE-P71-CH05-13-REVIEW-2026-10-21.md), F1–F4  
**Control (A):** the chapter text on `main` after P70. Each candidate is a patch in this folder; adopt one with `git apply <patch>` from the repository root.

---

## Candidate 1 — Ch7: end on the road (F1)

**A — now:** the chapter ends on “For the first time since the apartment, nobody was telling Elizabeth where to go.”

**B1 — lean:** end at `…then a long empty stretch of road with nothing coming the other way.` · [patch](EXP-0017-B1-Ch07-End-On-The-Road.patch)

Cut only. Same kind of closer as the Ch16 and Ch17 lines cut in R54.

## Candidate 2 — Ch12: drop “For most of the night,” (F2)

**A — now:** “For most of the night, the diary had been one of the few things that was unequivocally hers.”

**B2 — lean:** `The diary had been one of the few things that was unequivocally hers.` · [patch](EXP-0017-B2-Ch12-Diary-Without-The-Night.patch)

Cut only. The diary was taken and returned on Thursday night; this scene is Saturday dawn.

## Candidate 3 — Ch13: one “cooking wagon” (F4)

**A — now:** “a woman shaking flour from a cloth near the cooking wagon, a dog asleep under the cooking wagon.”

**B3 — lean:** `a woman shaking flour from a cloth, a dog asleep under the cooking wagon.` · [patch](EXP-0017-B3-Ch13-One-Cooking-Wagon.patch)

Cut only.

## Question 1 — Ch9: the diner sign (F3)

**A — now:** “a yellow sign that said DINER 24/7.”

**Q1:** `a yellow sign that said DINNER 24/7.` · [patch](EXP-0017-Q1-Ch09-DINNER-Sign.patch)

The author's draft spelling. No lean: it's his call, open since P34.

## Not proposed

- **Ch5 “I don't lie.”** Kept; the panel read it as intended (review, "Considered and kept").
- **No new line anywhere.** Every candidate is a cut, or a one-word restoration of the author's own spelling.

## Verification

Every patch passes `git apply --check` against `main` after P70, alone and all four together. They touch different chapters and don't depend on each other.
