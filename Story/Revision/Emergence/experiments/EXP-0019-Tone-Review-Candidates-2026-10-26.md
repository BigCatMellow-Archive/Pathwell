# EXP-0019 — Tone review: candidates, and what was withdrawn

**Date:** 2026-10-26
**Status:** **CLOSED 2026-10-27** ([P89](../../Pass-Log.md#p89-2026-10-27-whole-book-tone-pass-and-scrubs-beats), [P90](../../Pass-Log.md#p90-2026-10-27-exp-0019-closed-b2-and-b5-kept), R61, R62). Applied: B1a and B3a. B4 was replaced by a rewrite that keeps the ditch joke. B1b and B3b are moot. **B2 and B5 were declined; both lines stay.** The reasons are under [Decided 2026-10-27](#decided-2026-10-27-b2-and-b5-kept).
**From:** the [tone review](../TONE-REVIEW-2026-10-26.md). It read all the tone and voice notes and checked whether canon hits them. It was revised under the author's [Do-Not-Overliteralize rule](../../Author-Notes/2026-10-26_Do-Not-Overliteralize.md). Asked about it, the author said **"Go for it."**
**Applied in [P88](../../Pass-Log.md#p88-2026-10-26-tone-review-two-cuts-and-exp-0019):** only the two cuts that held up when read in context. Everything else that held up is a candidate here. Recommendations that didn't hold up are listed as withdrawn, with the reason.
**Control (A):** the chapter text on `main` after P88. Each candidate is a patch in this folder; adopt one with `git apply <patch>` from the repository root.

Each candidate carries the rule's diagnosis:

- **A:** actual problem.
- **B:** preference.
- **C:** meaning-altering.
- **D:** genuine improvement.

The **lean** is the reviser's under R36. "No lean" means it's taste or it changes meaning, so it's the author's call.

---

## Applied in P88 (on "Go for it")

| Ch | Cut | Diagnosis | Note |
| --- | --- | --- | --- |
| 16 | "For the fact that choosing Milo had been right and had still cost her things she wanted back." (last item of the crying list) | A: the thesis, stated at the emotional peak | It was a reviser lean "kept against the checks" in the P54 Ch16 pass, not an author pick. The list now ends on "…still managed to owe Milo a card game." |
| 18 | "She had asked him to bring her here. That didn't make the next step his." | A: narrator states what "Do you want to come?" shows | **This line arrived with the Version C prose test ([EXP-0004C](EXP-0004C-Ch18-Confession-Then-Existing-Hour-Prose-Test-2026-10-15.md)) the author picked (R47).** His pick was about structure, not this sentence, but revert if he wants it back. The Harada box p1-8-6 now quotes the remaining line. |

## Candidates

| # | Ch | Change | Diagnosis | Lean | Patch |
| --- | --- | --- | --- | --- | --- |
| B1a | 1 | "He nodded at the ooze drying on her walls." + the line → `"Your house has now been marked. Magically speaking," he said, nodding his head to the side. "So we should probably be anywhere but here."` | Reverses a C: the nod at the ooze changed his "so to speak" into pointing ([P83](../../Pass-Log.md#p83-2026-10-26-author-clarifies-qualifying-nod)) | **take**: it's the author's own wording from P83 | [B1a](EXP-0019-B1a-Ch01-Half-Nod-Authors-Words.patch) |
| B1b | 1 | Same, using Line Notes §12's minimal illustration: `"…Magically speaking." He gave a small, sideways half-nod at the last two words. "So we…"` | same | alternative to B1a; apply one | [B1b](EXP-0019-B1b-Ch01-Half-Nod-Minimal.patch) |
| B2 | 14 | Mama Baga: cut "The working knows what you mean, not what you wish you meant." and keep "You are giving it two incompatible answers." | A (stated rule) vs C (it's her voice, and it names the mechanism the next paragraph shows) | **no lean** | [B2](EXP-0019-B2-Ch14-Working-Knows-Cut.patch) |
| B3a | 17 | Cut "Elizabeth didn't call that redemption. She called it evidence." | A by the thesis test; C because it is her verdict on him | **no lean** | [B3a](EXP-0019-B3a-Ch17-Evidence-Line-Cut.patch) |
| B3b | 17 | Cut it and the line before ("Pathwell had kept showing up…"). The "still ash" list then leads straight to the road | same | **no lean**; apply B3a or B3b, not both | [B3b](EXP-0019-B3b-Ch17-Evidence-Pair-Cut.patch) |
| B4 | 17 | Cut the "Adventure had been difficult to separate…" paragraph | First sentence A (summary); the rest is pleasure (the ditch joke). Cutting the whole paragraph is C | **no lean**; there's no clean partial cut without new wording | [B4](EXP-0019-B4-Ch17-Adventure-Paragraph-Cut.patch) |
| B5 | 4 | Cut the scene closer "Behind her, Nana's cookbook stayed on the shelf, and Elizabeth didn't go back for it." | The Oct 5 report: the gift is told four times (A). In context it's the one indirect beat of her leaving it (C) | **no lean** | [B5](EXP-0019-B5-Ch04-Cookbook-Closer-Cut.patch) |

B1, B2, B3, B4 and B5 are independent of one another. B3 and B4 both touch Ch17, but at different paragraphs.

## Questions, no patch

- **Q10 (from the Oct 5 report), the rate of glances.** In group scenes, "X looked at Y. 'line'" usually marks who is being *addressed*. That is purposeful blocking, not clutter. Do you want any of it changed, and if so where? No candidate until you say. Per the rule, the review won't cut toward a number.
- **The minor cast's shared dry voice** (healer, curator, notebook woman). Each line is a pleasure on its own; only the sameness is the issue. Does it bother you on the page? If yes, name one or two characters and write their lines yourself, or ask for plain candidates.

## Withdrawn after reading in context

| Earlier recommendation | Why withdrawn |
| --- | --- |
| Ch10: cut "And paying for it yourself made you feel like the method was yours to choose." | Pathwell's next line, "At the time, I would have called *that* responsibility," depends on it. It's also Elizabeth's accusation, an action that pulls his admission out of him. |
| Ch10: cut "That's not the same as listening." | Her rebuttal, an action. He answers "No." |
| Ch10: cut the Shade recall (*For him to stop deciding what I am…*) | It's Elizabeth thinking before she speaks ("He thinks you'll decide for him."). That's the "let Elizabeth think like a person" rule. Cutting it is C. |
| Ch14: cut Stansbury's "How many times are you going to call that responsibility…" | In character (precision: two facts, then the question) and it's the confrontation's action; "Move." / "No." follow. |
| Ch14: shorten Mama Baga's "Your intent is split" exchange to orders | It's diagnosis that drives the plot: the split intent is why the frame loosens and Pathwell gets his exit. Only B2's single sentence is offered. |
| Ch16: shorten Elizabeth's "I am not going to make your guilt useful…" | It's a refusal, which is an action, and her boundary. Cutting it is C. |
| Ch9: trim the glosses beside Shade | Already done in earlier passes: "It was for the pull itself." stands alone, as the Oct 5 report asked. |
| Ch15: cut the turnips line | A callback that explains the boy's instant "Okay."; the action resumes in the next sentence. B at most. |
| Ch4: thin the attitude personification | The flagged lines are mostly gone; "One sock had surrendered" is figurative truth and stays. |
| Ch5: "Selling off potential nobody was going to use." | The author already kept it (R34). Not re-raised. |


## Decided 2026-10-27: B2 and B5 kept

The author said "do whats best, but make notes on why in the repo" (R62). Both lines stay, for the reasons below.

**B2 — Ch14, Mama Baga: "The working knows what you mean, not what you wish you meant." Kept.**

- **It's a rule of the world, not the book's theme.** The thesis test bans stating the theme: who gets to decide for whom. This line states how workings behave. Rules are stated once by the person entitled to state them (Writing Principles 17), and at Camp that's Mama Baga.
- **The scene needs the rule at that moment.** "Your intent is split" names the problem. This line says why a split intent matters. The next paragraph proves it: the brass loop dips, and the structure loosens. Without the rule, the loosening reads as luck rather than consequence.
- **It's her voice.** It's dry, flat and certain, care given as an instruction. The overliteralization rule asks whether a cut would change a character's manner. This one would, so it's C rather than A.
- **The redundancy is mild.** It's one sentence next to "You are giving it two incompatible answers." The two do different jobs: one is the principle, the other is the diagnosis.

**B5 — Ch4 closer: "Behind her, Nana's cookbook stayed on the shelf, and Elizabeth didn't go back for it." Kept.**

- **It's the indirect version of the feeling.** The grief is shown through an object and an action she doesn't take, which is what the Voice Guide asks for. Nothing is named.
- **It plants a later scene, which is the Scrubs method of retrospective revaluation** ([notes](../../Author-Notes/2026-10-27_Irreverence-With-Heart-Scrubs.md)). In Ch15 she runs past the same cookbook on the same shelf to reach Milo: "Elizabeth ran past the cookbook too." Ch4's "didn't go back for it" is what gives "too" its weight. Cutting it weakens the Ch15 choice.
- **The Oct 5 count of four tellings still has a remedy, just not this cut.** The giving scene (the raised hand, "Archive") is the moment. This closer is its aftermath, in the narrator's aftermath register, and it's the only one of the four that points forward.
