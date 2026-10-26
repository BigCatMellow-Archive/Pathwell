# EXP-0019 — The Sunday Morning lens: four cuts and five questions

**Date:** 2026-10-22  
**Status:** **AUTHOR-SELECTED 2026-10-22 ([R59](../../Decisions.md#the-authors-rulings-for-this-revision), [P81](../../Pass-Log.md#p81-2026-10-22-exp-0019-leans-applied)): "I trust your leans".** B1–B4 applied. Q1: the healer goes back to plain; her lines are marked below for the author to rewrite. Q3, Q4 and Q5 are kept as they are. **Q2 stays open**, because it had no lean.  
**From:** two independent reads of the book after P79, both requested by the author ("would it be worth reading the story again with these new notes in mind"):
- the [lens read](../../Reader-Reports/Sunday-Lens-2026-10-22/LENS-Ch01-18.md): informed, all 18 chapters, against his [Sunday Morning Movies](../../../Sunday-Morning/Sources/Sunday-Morning-Movies.md) definition and R24;
- the [drop-in read](../../Reader-Reports/Sunday-Lens-2026-10-22/DROP-IN-Ch09-18.md): blind, given only Chapters 9–18, as his cable test turned into reading.

**Control (A):** the chapter text on `p77-exp0018-leans-and-status` after P79. Each candidate is a patch in this folder; adopt one with `git apply <patch>` from the repository root.

---

## The headline

**The book passes the author's test.** Opened cold at Chapter 9, the blind reader would have kept reading at every checkpoint ("yes, and firmly" at Ch15) and closed the book smiling. The lens reader found the R24 balance working. Camp and the side cast carry the Sunday part. The weight in Ch3, 11 and 14–16 is intact. Ch16 draws the line itself: "You don't get to use being funny to decide when this becomes easier."

Both readers agree that **a Sunday pass should mostly protect what's there.** The lens report lists what not to touch: section 6, which a later pass should read as a rule.

**The convergent finding is the voice, not the warmth.** Both readers, independently, heard too many people speaking in the same dry, clipped rhythm:
- the lens reader: "Apparently." seven times from several speakers; the healer drifting into a second dry wit against R33;
- the drop-in reader: "a lot of characters started to sound alike… especially Stansbury, the archivist and the healer".

The definition asks for "several excellent character actors", which means different performances. Cuts can thin the repetition (B1, B2). Giving someone a different register is new character-defining dialogue, so that's Q1.

## Cuts (B)

| # | Ch | Change | Why | Lean | Patch |
| --- | --- | --- | --- | --- | --- |
| B1 | 16 | `"Apparently. Can I check it?"` → `"Can I check it?"` | the seventh "Apparently."; makes the healer plainer, as R33 set her in Ch4. "A low standard." / "It has been a morning." stay *(superseded by R59: both are on the healer's list below; candidates in [EXP-0021](EXP-0021-House-Deadpan-Candidate-Lines-2026-10-22.md))* | take (cuts a joke, so it's flagged) | [B1](EXP-0019-B1-Ch16-Healer-Apparently.patch) |
| B2 | 18 | cut the shopkeeper's `"Occupationally."` after "I hate when you know things about your own shop." | the same word is Stansbury's in Ch14; Pathwell's line becomes the button | take | [B2](EXP-0019-B2-Ch18-Occupationally.patch) |
| B3 | 14 | `…spreading from Pathwell's shadow, possibility given a shape only because the eye needed something to fail at understanding.` → `…spreading from Pathwell's shadow.` | **both readers stopped here**; the narrator explaining at the moment of greatest stress (W11). The Ch3 tree callback in the next two sentences stays (R29 covers Ch3) | take (cuts a metaphor, so it's flagged) | [B3](EXP-0019-B3-Ch14-Pale-Light.patch) |
| B4 | 15 | "cut Pathwell out of one of these things at the bar" → "outside the bar" | the blind reader read Ch9's "parking lot" and Ch15's "at the bar" as two places; it happened in the bar's lot (Ch7) | take | [B4](EXP-0019-B4-Ch15-Outside-The-Bar.patch) |

Every patch passes `git apply --check`, alone and all four together. After B1, "Apparently." is down to six.

## Questions for the author (Q)

No lean on these where they're taste. Each would need new text in your categories.

**Q1. The house deadpan.** Should two or three people speak in a different way from everyone else? Both readers suggest it. The lens reader names Milo and the woman in the knitted cap as the model: funny, but not dry. The healer is the clearest case (Ch12's "Briefly? Very." / "Afterward, less."; Ch16's "Shelves are famous for respecting medical instructions."). R33 made her plain in Ch4 so that "the archivist stays the one dry wit". *Lean:* yes for the healer, back to plain. That means rewriting a few of her lines, which is yours to do. I can mark every one of them in her chapters if that helps.

**Q2. Ch15: "There were advantages to children who had spent the morning taking instructions from people carrying turnips."** Milo was the one carrying turnips (Ch4), so the joke's referent is off. The 10-06 Ch15 reader stopped here too. It's a small absurdity inside the hard moment, which R24 wants, so it shouldn't be cut. It needs a new line from you, or "keep".

**Q3. The foam dagger's resting place.** It's last seen in Ch15. The lens reader notes that this mode usually gives a setup a final touch, for example Stansbury taking it back, which would rhyme with his Ch8 "Keep it." R15 ("no idea yet, and doesnt matter to me") and R37 cover its role at the climax, not its end. *Lean:* leave it, unless you want the beat.

**Q4. The Merritt cookbook in Ch18.** The blind reader wasn't sure what Pathwell decided ("about 70% sure"), and called it a key moment. Its guess was the intended reading. The scene is locked silent: Q99 and Q103 say no offering and no explaining. *Lean:* keep it silent. The reader got it, and that's what a silent beat asks for. The ledger glance is the one clue, and it's doing its job.

**Q5. Theme said aloud.** The blind reader "liked each of these on its own" but felt "a little guided" by the three together: "People keep doing that." / "Asking." (Ch13), Elizabeth's Ch16 speech, and "She called it evidence." (Ch17). The lens reader protects the Ch16 speech. *Lean:* keep all three. Ch17's line survived R54's cut of the chapter's thesis closer. Raised only because it's the one place two readers' opinions touch on R26.

## Considered, not proposed

| Finding | Why not |
| --- | --- |
| The Ch9 recap ("At the school… marked") was the blind reader's densest stretch | R39: the Oct 12 diner revision has Elizabeth connect the clues herself; a reader who started at Ch9 was always going to lack them |
| The Ch10 Ask is abstract lore at an emotional peak | Non-Negotiable 6; the human line carries it, and P77 just edited this scene |
| Ch14's "At the time, it looked like fidgeting." (the narrator looking back) | Q147: he builds the frame while talking; the flash-forward is how the reader learns it was the frame |
| Ch15 has no soft landing | correct (R45, R46); Ch16 opens with it |
| Never explained to the drop-in reader: "marked", who asked for help, why the blob spared Pathwell | each is deliberately open or set up before Ch9, and the reader marked each "fine not knowing" |
| The gold chain's resting place | already EXP-0018 C3 |
| Elizabeth almost always right in the back half | already EXP-0018 C1 |

## The healer's lines, for the author (Q1)

The author's call (R59) is that the healer goes back to plain, as R33 set her in Ch4. These are the lines where she's the dry wit. Rewriting them is his (who writes what). The lines around them that are hers and plain ("Which shoulder?", "Because it's your shoulder.", "Fingers?", "Still in.") already do the job.

| Ch | Line (as on the branch after P81) | Note |
| --- | --- | --- |
| 12 | "I ask because people point at the wrong thing surprisingly often." | wry, but explains her question; may stay |
| 12 | "Briefly? Very." / "Afterward, less." | a two-part quip; Elizabeth's "Excellent." / "Strong sales pitch." answer it |
| 12 | "If you are about to ask whether carrying something counts, yes." / "You were going to." | banter in the house rhythm |
| 16 | "Useful." / "Me." (to Milo, after "Ow." / "For who?") | Milo's "deeply unfair" depends on it |
| 16 | "A low standard." | answers Elizabeth's "Still attached." |
| 16 | "Shelves are famous for respecting medical instructions." | Elizabeth's "This one was especially difficult." depends on it |
| 16 | "You use this arm again today and I will tie you to the wagon." / "Fine. I will ask you very firmly not to." / "It is what we have." | a running exchange with Mama Baga's "No." in the middle |

If any of these become plain, check the reply that answers it. Several of Elizabeth's jokes only work as answers to the healer's.
