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
| H1 | 12 | `Elizabeth looked at her. The healer looked back. "I ask because people point at the wrong thing surprisingly often."` | cut; "Which shoulder?" goes straight to "Left." | keep the current text: it explains her question rather than correcting anyone. Take H1 only if she should be strictly plain *(lean changed after the fresh check)* | [H1](EXP-0021-H1-Ch12-Which-Shoulder.patch) |
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
| S1a | 6 | `"Good."` / `"Really?"` / `"No. I ordered it because I enjoy disappointment."` | `Stansbury closed his eyes over the next bite. "Don't talk to me for a minute."` | take: the author's own Stansbury says "So good" to himself over this fish (benchmark Ch5), and the napkin slap now catches Pathwell with his eyes shut *(lean changed after the fresh check)* | [S1a](EXP-0021-S1a-Ch06-Fish-Dont-Talk.patch) |
| S1b | 6 | (same) | `"Exceptional. I have exceptional taste in fish."` | |  [S1b](EXP-0021-S1b-Ch06-Fish-Exceptional-Taste.patch) |
| S1c | 6 | (same) | `"Everyone has principles until the fish arrives."`, a jab at Pathwell's "objected to the batter on philosophical grounds", adapted from the quote bank's "Everyone has principles until lunch is delayed." | lean against: S1a comes from his own draft, and his voice guide says "not every line should be quotable" (see below) | [S1c](EXP-0021-S1c-Ch06-Fish-Principles.patch) |
| S2 | 7 | `Stansbury set the baton down carefully. "That one is gone."` | `…carefully and brushed something off his vest that wasn't there. "That one is gone."` | take, with S1a: the author's own beat at this moment ("Stansbury dusted himself off", benchmark Ch5); the vest is set up in Ch5. S1a is appetite and S2 is vanity, so together they're the one trace EXP-0020 Q2 asked for | [S2](EXP-0021-S2-Ch07-Vest.patch) |
| E1 | 8 | `"No. It's one of them."` | `"One of them."` | take: same joke, without the house shape | [E1](EXP-0021-E1-Ch08-One-Of-Them.patch) |
| T1a | 15 | `There were advantages to children who had spent the morning taking instructions from people carrying turnips.` | `There were advantages to a boy half of Camp sent on errands.` | | [T1a](EXP-0021-T1a-Ch15-Turnips-Errands.patch) |
| T1b | 15 | (same) | `There were advantages to a boy who had been carrying things for other people since he was big enough to carry turnips.` | take: keeps the turnip, Milo's running tag, and the small absurdity R24 wants here. Two flaws for the author to write over: "carrying… carry", and "since he was big enough" is a small new claim *(lean changed after the fresh check)* | [T1b](EXP-0021-T1b-Ch15-Turnips-Kept.patch) |

Every patch passes `git apply --check` on its own. The lean set (H2a, H3, H4, H5b, H6–H9, S1a, S2, E1, T1b) applies together, across Ch6, 7, 8, 12, 15 and 16.

**Kept on purpose:** the archivist's "No." in Ch4 (he's the sanctioned dry wit, R33) and Shade's "No. I'm getting coffee." in Ch8 (his literalness). In Ch12 the healer's "Because it's your shoulder." and in Ch16 "Can I check it?" stay: they're plain, and they carry the asking theme.

## The quote bank

[quote_and_character_voice_reference.md](../../../Story_Files/quote_and_character_voice_reference.md) was read for this page on the author's prompt, after the first draft of it. It is about 340 lines of tone he approved: the seed line is his ("These moments will someday be memories we wish had lasted longer."); the rest were written in an earlier chat. Most of it is reflective or irreverent aphorism, a "bad guy, not the villain" set and a portrait of a weary, careful man.
- **It has no notes on the healer, Stansbury or Elizabeth,** so it doesn't change H1–H9, E1 or T1. The healer is meant to be plain, and the bank's register is the opposite of plain.
- **Its "barroom wise" set suits Stansbury at the bar.** S1c is adapted from it.
- **None of its lines is in the book.** A five-word overlap search found only stock phrases ("the look of a man").
- Kept for the author, not drafted: the portrait line "He was not cynical by temperament. He had simply kept the receipts." sits close to Stansbury's Ch10 "You keep receipts until they become archaeological sites." about Pathwell, one of the deadpan lines the fresh check found.

## Checked against the author's voice guide

Read after the author asked whether the repository's resources were being used ([resource audit](../RESOURCE-AUDIT-2026-10-22.md)). His [voice guide](../../../Sunday-Morning/Sources/Voice-Guide.md) names this problem itself: "everyone sharing the same sense of humor" and "constant quipping" are on its avoid list, and "Characters should not feel like stand-up comedians. Not every line should be quotable. Not every scene needs a joke."
- **It explains the shape.** The "No. [correction]." line is someone answering the literal question exactly and winning the exchange. The guide wants the opposite: "People do not always answer the question they were asked. They may deflect, misunderstand, change subjects, answer the emotional question instead of the literal one." That's a way in for any of these lines he rewrites.
- **It backs S1a over S1c.** Humour "from character… appetites… petty concerns", and "the funniest moments should often occur because a character is completely sincere about something ridiculous": Stansbury shutting his eyes over fried fish. S1c is a quotable line, which the guide warns against. **S1c: lean against.**
- **It backs the healer cuts.** "Not every scene needs a joke"; "capable of kindness without announcing themselves as kind" is the plain healer who says "Sorry." and "I know."
- **One caution.** H5b's "Milo considered that insufficient." is narrator cleverness ("Do not turn every observation into a clever observation"). H5b stays the lean, because it keeps Milo's soft landing, but that word is the one to write over.

## Fresh check

An independent helper read every option in its scene against the author's Ch4–5 drafts, without the reviser's leans: [report](../../Reader-Reports/Fresh-Check-EXP-0021-2026-10-22.md). It agreed on H2a, H3, H4, H5b, H6–H9 and E1, and changed three leans (H1, S1, T1, marked above). Also from the report:
- **H4 removes an unflagged echo:** Ch12's "I wasn't." / "You were going to." copies Ch6's "I was not." / "You were about to."
- **The healer's warmth in Ch16 then rests on "Sorry." (H5) and "I know." (H7).** Take the cuts without those two and she reads curt, not plain.
- **H9 leaves Stansbury silent in that stretch;** his tight jaw carries it.

**Found, not drafted** (for a later pass or the author):
- Mama Baga's "That was not the question." (Ch12:187) is the third of its kind after Ch7's "That wasn't the question." and Ch8's "Was that a question?".
- The healer's "before the swelling makes us all regret waiting" (Ch12:108) would be her one remaining flourish. Tolerable.
- Two more house-deadpan "No." lines: "No. You keep receipts until they become archaeological sites." (Ch10:133) and "No. I can see gravy on the cover." (Ch18:233). The helper listed five more "No." lines in Ch10 and Ch13; the reviser read them, and they are plain answers, not the corrective shape (Ch10:522, "No. I would not try.", was kept on purpose in P77).
- EXP-0019's B1 row still says "A low standard." / "It has been a morning." stay; R59 superseded that. Noted there.
