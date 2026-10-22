# EXP-0021: the house deadpan, candidate lines

**Date:** 2026-10-22  
**Status:** **CANDIDATES. Nothing applied.** Every line here is a joke, an emotional line, a character-defining line or narrator commentary, so each one is the author's to pick, rewrite or refuse ([who writes what](../../../Sunday-Morning/Craft.md#ai-and-the-author-who-writes-what)). The new lines are scaffolds: plain on purpose, for him to write over.  
**From:** the convergent finding of both Sunday-lens passes: too many people speak in one dry, corrective deadpan. Each spot comes from a question already put to the author:
- [EXP-0019](EXP-0019-Sunday-Lens-Candidates-2026-10-22.md) Q1, answered by [R59](../../Decisions.md#the-authors-rulings-for-this-revision): the healer goes back to plain, as R33 set her in Ch4; her lines are listed there for him to rewrite;
- EXP-0019 Q2: the Ch15 turnips line, whose referent is off (Milo *is* the turnip boy);
- [EXP-0020](EXP-0020-First-Half-Sunday-Lens-Candidates-2026-10-22.md) Q1: Stansbury's Ch6 and Elizabeth's Ch8 "No. [correction]." lines;
- EXP-0020 Q2: one trace of Stansbury's Ch5 vanity in Ch6–7.

**Control (A):** the chapter text on `p77-exp0018-leans-and-status` at `05f1b6b` (after P83). Each candidate is a patch in this folder; adopt one with `git apply <patch>` from the repository root.

---

## What the options are trying to do

**The healer.** Her baseline is the author's Ch4: practical, kind, asks before she touches, says what's true ("Then she wakes up sore and hungry."). In Ch12 and Ch16 she trades quips with Elizabeth in the archivist's rhythm. The options make her plain **and keep Elizabeth's jokes where they can answer a plain line**: Elizabeth gets the laugh, the healer stays the straight one. That is the "several character actors" the definition asks for.

**Stansbury.** In the author's own drafts he is theatrical and self-indulgent: he circles and sniffs Pathwell ("That stench of desperation"), wants to hug him, loves his fried fish and malt vinegar, finishes Pathwell's drink, and punches his arm "for making me wait". From Ch6 on the revision has him only correcting people. One line of vanity or appetite is enough to bring him back. S1b and S2 are alternatives for that one line.

## Candidates

| # | Ch | Current | Candidate | Lean | Patch |
| --- | --- | --- | --- | --- | --- |
| H1 | 12 | `Elizabeth looked at her. The healer looked back. "I ask because people point at the wrong thing surprisingly often."` | cut; "Which shoulder?" goes straight to "Left." | take | [H1](EXP-0021-H1-Ch12-Which-Shoulder.patch) |
| H2a | 12 | `"Briefly? Very."` / `"Excellent."` / `"Afterward, less."` / `"Strong sales pitch."` | `"It'll hurt a lot, and then it'll hurt less."` / `"Strong sales pitch."` | take | [H2a](EXP-0021-H2a-Ch12-Briefly-Very-Plain.patch) |
| H2b | 12 | (same) | `"Badly, for a moment."` / `"Strong sales pitch."` | | [H2b](EXP-0021-H2b-Ch12-Briefly-Very-Short.patch) |
| H3 | 12 | `"Still mine."` / `"Keep them that way."` | cut her reply; "Still mine." is the button | take | [H3](EXP-0021-H3-Ch12-Keep-Them.patch) |
| H4 | 12 | `"Define using."` / `"If you are about to ask whether carrying something counts, yes."` / `"I wasn't."` / `"You were going to."` / `"Probably."` | `"Define using."` / `"Lifting. Carrying. Pulling. Any of it."` | take: a concrete rule that Ch15 then breaks (she braces the shelf on that arm and lifts) | [H4](EXP-0021-H4-Ch12-Define-Using.patch) |
| H5a | 16 | `"Ow."` / `"Useful."` / `"For who?"` / `"Me."` / `Milo considered that deeply unfair.` | `"Ow."` / `"Sorry. That's the one."` | | [H5a](EXP-0021-H5a-Ch16-Useful-Sorry.patch) |
| H5b | 16 | (same) | `"Ow."` / `"Sorry."` / `Milo considered that insufficient.` | take: keeps Milo's beat, the healer apologises | [H5b](EXP-0021-H5b-Ch16-Useful-Insufficient.patch) |
| H6 | 16 | `"Still attached."` / `"A low standard."` / `"It has been a morning."` | cut both; her look toward the archive answers Elizabeth's joke | take | [H6](EXP-0021-H6-Ch16-Low-Standard.patch) |
| H7 | 16 | `"There was a shelf."` / `"Shelves are famous for respecting medical instructions."` / `"This one was especially difficult."` | `"There was a shelf."` / `"I know."` | take: she was at the fire | [H7](EXP-0021-H7-Ch16-Shelves-Famous.patch) |
| H8 | 16 | the threat, Mama Baga's "No.", then `"Fine. I will ask you very firmly not to."` / `"That seems less effective."` / `"It is what we have."` | keep the threat and Mama Baga's "No."; cut the three lines after. "I'll try," follows the "No." | take: the threat is heat, not deadpan | [H8](EXP-0021-H8-Ch16-Tie-To-Wagon.patch) |
| H9 | 16 | `"Good. This is going to take a while."` / `"Define a while."` / `"Longer than you want."` / `"Everything does."` | cut the three lines after hers | take: "Define a while." repeats Ch12's "Define using." | [H9](EXP-0021-H9-Ch16-Define-A-While.patch) |
| S1a | 6 | `"Good."` / `"Really?"` / `"No. I ordered it because I enjoy disappointment."` | `Stansbury closed his eyes over the next bite. "Don't talk to me for a minute."` | | [S1a](EXP-0021-S1a-Ch06-Fish-Dont-Talk.patch) |
| S1b | 6 | (same) | `"Exceptional. I have exceptional taste in fish."` | take: answers EXP-0020 Q1 and Q2 in one line | [S1b](EXP-0021-S1b-Ch06-Fish-Exceptional-Taste.patch) |
| S2 | 7 | `Stansbury set the baton down carefully. "That one is gone."` | `…carefully and brushed something off his vest that wasn't there. "That one is gone."` | alternative to S1b; not both | [S2](EXP-0021-S2-Ch07-Vest.patch) |
| E1 | 8 | `"No. It's one of them."` | `"One of them."` | take: same joke, without the house shape | [E1](EXP-0021-E1-Ch08-One-Of-Them.patch) |
| T1a | 15 | `There were advantages to children who had spent the morning taking instructions from people carrying turnips.` | `There were advantages to a boy half of Camp sent on errands.` | take: he's sent somewhere in Ch12 and Ch14 | [T1a](EXP-0021-T1a-Ch15-Turnips-Errands.patch) |
| T1b | 15 | (same) | `There were advantages to a boy who had been carrying things for other people since he was big enough to carry turnips.` | | [T1b](EXP-0021-T1b-Ch15-Turnips-Kept.patch) |

Every patch passes `git apply --check` on its own. The lean set (H1, H2a, H3, H4, H5b, H6–H9, S1b, E1, T1a) applies together: 8 lines in, 44 out, across Ch6, 8, 12, 15 and 16.

**Kept on purpose:** the archivist's "No." in Ch4 (he's the sanctioned dry wit, R33) and Shade's "No. I'm getting coffee." in Ch8 (his literalness). In Ch12 the healer's "Because it's your shoulder." and in Ch16 "Can I check it?" stay: they're plain, and they carry the asking theme.

## Fresh check

*(Pending: an independent helper is reading every option in its scene against the author's drafts.)*
