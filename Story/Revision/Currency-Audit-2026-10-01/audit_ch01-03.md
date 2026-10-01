# Currency audit: Chapters 1-3 (contracts W01-W03)

Audited 2026-09-30 against the repo at commit 77fc40c (Chapter 1 as restaged in P7b). Each chapter was read in full. Each decision below was checked in the primary file named in its row, not only in the Decision-Timeline. Line numbers are from `cat -n` of `Story/Chapters/Chapter_0N.txt`.

Primary files opened:
- `Story/Revision/Decisions.md`
- Interview: `BIBLE_DECISIONS_2026-08-21.md` and `-08-22.md` (§1 Space Between, §2 blobs, §3 Chapter 1 entry, §4 Shade creation)
- `MANUSCRIPT_RECONCILIATION_AUDIT_2026-08-23.md` (Ch1-3 sections)
- `..._REFINEMENTS_2026-08-23.md` (§1, §4, §5, §12)
- Continued 19, 25, 39, 44, 46, 47, 48, 49, 50, 51, 52, 55, 56, 57, 58, 59, 65, 67
- `Story/Story_Files/PATHWELL_MAPS_L_CHAPTER_CONTRACT_MATRIX_2026-08-28.md` (W01-W03)
- `character_bible.md`, `world_bible.md`, `Story/Revision/Plan.md`, `Pass-Log.md` (P7, P7b), `Promise-Ledger.md`
- The author's July Chapter 2 (git `765b69b`), for the shape R12 restores

Short version: Chapter 1 is current on everything I could check, with four small flags. Chapter 2 has real outdated material: the lo mein order and its knock-ons, plus one motive line and a Q118 tension that the Plan does not name. Chapter 3 follows its locks, with four low-confidence items.

---

## Chapter 1 (W01; old Ch1)

| # | Line(s) | Text (quote <=25 words) | Current decision (quote <=40 words) | Decision source | Kind | Level | Already listed in Decisions.md or Plan.md? | Confidence |
|---|---|---|---|---|---|---|---|---|
| 1.1 | 9 | "She knew him, a little. He'd been at the party, talking to everybody. She'd never caught his name." | R10: "I think its a welcome party for Elizabeth, and he knows her." Q-H is open: "he knows her" from the party, or from before? | Decisions.md R10 and "Open for the author" Q-H; Timeline `R10`, `Q-H he-knows-her (OPEN)`, `SEP RNA1 party-stranger` | inconsistency (unconfirmed default). R10 says *he* knows *her*. The page shows the reverse (she recognises him) and never shows him knowing her before Ch2's "Lizzy". | line | yes (Q-H; P7 flag 2) | medium |
| 1.2 | 7 | "Somebody's WELCOME LIZZY banner hung by one corner over the kitchen doorway. The guests had gone home hours ago." | Q112: the party is shown "only by brief cues after she wakes: hallway music/voices, people or cups, door traffic". R10 and SEP A2: her own welcome party; "he stays after the guests leave". | Continued 49 §Q112 LOCK; Decisions.md R10; Timeline `Q112`, `SEP A2 welcome-party`, `R10` | conflict between decisions: Q112's "nearby party" (08-26) against R10's her own party (09-30). R10 is newer and the text follows it. Q112's no-prelude and brief-evidence limits are also respected. Recorded so no pass reverts it; no change needed. | line | yes (Decisions.md lock-table row 1; Q-H) | high |
| 1.3 | 11-15 | "reading her diary like a magazine in a waiting room." / "Not at all," he said, and turned a page. | 08-22 §3: he "passes as a party guest" and takes useful material "he believes will not be noticed missing". Character bible: "calm, unhurried, insultingly comfortable in spaces that aren't his." | Bible 08-22 §3 Intended setup; Timeline `08-22 §3 ch1-entry`, `JUN 11 calm-entry`; `character_bible.md` line 47 | inconsistency (weak). The casual-until-the-blob restaging is correct. The only strain is that he reads her diary openly and unbothered once she's in the room, against "not noticed missing". P7b already noted this. | line | no (Pass-Log P7b only) | low |
| 1.4 | 107-161 | "stood her last guest, holding Nana's cookbook and her diary" ... "With a smile he grabbed her by the hand." | AUDIT G1 [audit-directive]: "By the time they leave, Pathwell must clearly have possession of the cookbook and diary so Chapter 3's reclaim works." | `MANUSCRIPT_RECONCILIATION_AUDIT_2026-08-23.md` Global 1 and Ch1 "Required fixes"; Timeline `AUDIT G1 ledger-ch1`, `AUDIT Ch1 leaves-with-both` | missing (weak). He holds both at 107, 115 and 133, but the departure (147-161) never shows the books leaving with him. Ch2 line 7 supplies it. | line | no | low |

Locks checked that the chapter follows: about 20. These are:
- First line unchanged, and no prelude (Q112).
- She wakes to the blob's pounding; the blob is already at the door before activation (08-22 §2, §3).
- He is casual, then "Friend of yours?" (the misread); the urgent cookbook demand follows from it (08-22 §3; JUN 11 calm-entry).
- "Marked" is an invented certainty; the wet thud reinforces it (08-22 §3; Q149b "went still").
- She tells him where the cookbook is and he fetches it (Q113).
- Handwritten cookbook, contact needed, page committed, the page can't be saved (08-21 §4, 08-23 §1).
- Elizabeth's interruption leaves loose waste; the blob lunges at the light only after entry (08-22 §2).
- The echo reaches a non-consenting recipient (08-21 §4.11).
- The blob is cleanup, not prey.
- The diary is intact, with no charring (08-23 §4).
- She leaves pulled (W01 exit state).
- "Ready?" / "No." / "Perfect." in Pathwell's original direction (Q102, Continued 39).

---

## Chapter 2 (W02; old Ch2) and the dumplings / first-choice night

| # | Line(s) | Text (quote <=25 words) | Current decision (quote <=40 words) | Decision source | Kind | Level | Already listed in Decisions.md or Plan.md? | Confidence |
|---|---|---|---|---|---|---|---|---|
| 2.1 | 277-307 | "Lo mein." / "I want lo mein." ... "It was an absurdly small decision. / It was still hers." | R12: "she didnt get the order cause she realized that he had her books still and she went after him." No lo mein order. | Decisions.md R12; Timeline `R12`, `SEP A5 no-lomein-rung`, `JUN ch2-ending` | outdated (the 2026-08-28 rewrite's beat, which R12 retires) | scene | yes (R12; Plan Ch2 row; Promise-Ledger R5) | high |
| 2.2 | 309-335, 433, 455 | "She took one bite. It was fine." / "Her lo mein was half gone." / "the ridiculousness of the lo mein" | Same as 2.1: no order, so no carton, no tasting banter, no later references. | Decisions.md R12; Timeline `R12` | outdated (follow-on references to 2.1) | scene | yes (same Plan row: "no lo mein order") | high |
| 2.3 | 293 | "You said the choice was—" She stopped. "You didn't say anything. I want lo mein." | "The choice is yours" is Pathwell's last line at 423, so this refers to a choice not yet offered. It is a seam from the rewrite. | Plan.md chapter work list, Ch2 "L" item; Timeline `Q118` | outdated (dead reference; goes with 2.1) | line | yes (Plan Ch2 L item) | high |
| 2.4 | 443-457 | "Not because he had told her to. Not because she trusted him. Because he still had her things. And because ... she wanted to know what the hell had happened" | R12 (the restored July shape is one motive, "He still has it"). Q118b: she "follows him because she still has a practical reason to do so"; only after the Space Between transaction "does the story give her a genuinely optional choice". | Decisions.md R12; Continued 55 §Q118 LOCK; Timeline `Q118b`, `R12`, `JUN ch2-ending` | contradiction. The curiosity motive at 455 and the "She could go back / call the police / sit here" list at 435-441 stage a free, deliberated choice here. Q118b reserves that for Ch3. The closing "ate it in two bites, and followed him" (457) is also rewrite-era, not the July ending. | scene | partly (Plan Ch2 row covers R12 and "new route to 'He still has it.'"; it does not name the curiosity motive or the deliberation list) | high for R12; medium for the curiosity line against Q118b |
| 2.5 | 7, 119-123, 369-375 | "because he still had her grandmother's cookbook under one arm" / "Give those back." "Soon." / "Fine. Pathwell. Give me my books." | R12's shape: she "realized that he had her books still" as the turn. July: she sits, the realization lands, then "He still has it." | Decisions.md R12; Timeline `R12`, `SEP RNA4 follow-for-books`, `JUN ch2-ending` | missing (the realization beat). Here she knows from the first paragraph and demands the books back three times, so the realization has no moment. | scene | yes (Plan Ch2 row: "the moment needs a new route to the same line") | high |
| 2.6 | 119-127, 391-399 | "That is not yours to decide." / "No," he said ... "It isn't." He kept walking anyway. / Instead he tucked them under his arm. "Somewhere safer." | Q118: he "does **not** consciously retain her diary/cookbook as leverage"; he "fails to recognize that walking away with her property still materially constrains her decision." Option C (knowing leverage) was rejected. | Continued 55 §Q118 LOCK (restated 56); Timeline `Q118`, `Q118b` | contradiction (partial). He twice refuses a direct request and concedes the books aren't his to decide about. That reads as knowing retention, near the rejected option C. It can be defended as "safekeeping", but it is hard to square with "does not consciously retain". Ch3 lines 25-29 and 79 carry the same pattern. Restoring the July shape (she notices only after he leaves) would fix it. | scene | no (Decisions.md lists Q118 under "locks the manuscript follows", Ch2/Ch3) | medium |
| 2.7 | 345 | "You broke into my apartment. I feel like this is information I should have." | R10: a welcome party for Elizabeth. Ch1 has him as "her last guest" she "knew ... a little". | Decisions.md R10 and Q-H "Blocks"; Timeline `R10`; Pass-Log P7 "Knock-on for Chapter 2" | contradiction (with the restaged Ch1). "What is your name?" (341) now fits, since she "never caught his name". | line | yes (Q-H; Plan Ch2 row; Revision-Status) | high |
| 2.8 | 5, 135, 231, 321, 371 | "The stranger did not." / "The stranger stepped up to the counter." (narration calls him "the stranger", then "Pathwell" after 347) | Ch1 line 9: "She knew him, a little." He is a guest she's seen, not a stranger. | Decisions.md Q-H; Pass-Log P7 ("the narration's 'the stranger' is softer now") | inconsistency (soft, since she never caught his name) | line | yes (Revision-Status Ch2 row; Plan) | low |
| 2.9 | 307 (and 433, 455) against Ch17 line 205 | "It was still hers." | Ch17: "The choice was ridiculous. / It was still hers." R12 removes the Ch2 source. | Decisions.md R12 ("Ch17's rhyme loses its source"); Plan Ch2 flags | inconsistency (cross-chapter; Ch17's callback has no source once 2.1 goes) | line | yes (Decisions R12; Plan Ch2 flag; Promise-Ledger R5) | high |
| 2.10 | whole scene (none present) | Text has no noticing-the-neighbourhood beat; the July coffee shop / laundromat / park passage was dropped in the rewrite. | "Chapter 2's changed-neighborhood feeling is primarily about Elizabeth finally noticing the ordinary world around her after living on autopilot." If retained, stage it so "there is a mundane explanation available". "Do not over-explain." | Refinements 08-23 §5 (LOCKED); Timeline `R0§5a-ch2-autopilot`, `R0§5b-ch2-mundane-staging`, `SEP RNA7 ch2-wrongness` | missing (conditional). The lock says the detail is optional ("if retained"), but it locks the feeling, and nothing in the chapter now carries "she has been on autopilot". The rebuild from the July chapter would bring the passage back and needs the §5 staging. | scene | no (Plan Ch2 row doesn't mention it) | low-medium |
| 2.11 | 91-107 (none present) | "This is a dream." / He pinched her arm. ... "Useful distinction." (the July Tuesday/Thursday exchange is gone) | AUDIT Ch2, "Strong material to preserve": "Tuesday/Thursday exchange." Also Ch1 = Thursday night (AUDIT Global 6). | `MANUSCRIPT_RECONCILIATION_AUDIT_2026-08-23.md` Chapter 2 "Strong material to preserve" and Global 6 | missing (preserve-note, [audit-directive], not a lock) | line | no | low |
| 2.12 | whole chapter | W02 contract: "Value turn: Elizabeth moves from pure reaction toward the first small act of self-direction"; the lo mein order was that act. | R12 removes the order. The character bible's rung 1 already reads "She follows because Pathwell still has the cookbook." | Contract W02 (`..._CONTRACT_MATRIX_2026-08-28.md`) against Decisions.md R12; Timeline `R12`, `JUN 24 agency-ladder` | conflict between decisions: the 08-28 contract (AI-written) against R12 (the author's, newer). R12 wins. After 2.1 goes, the only small assertive act left is defending the dumpling (267-275, "Boundary recognized"). The contract's value-turn line needs updating when Ch2 is rebuilt. | scene | no | medium |

Locks checked that the chapter follows: about 12. These are:
- Pathwell still holds both books (W02; AUDIT Global 1).
- The diary is intact, with no charring (08-23 §4; contract W02 stale list).
- The apartment-shadow detail is not staged as a magical mark (AUDIT Ch2).
- The laundry ticket blows away as the small final break.
- Grief arrives (AUDIT Ch2).
- "The choice is yours, Lizzy" is kept, and the narration calls it sincere (Q118).
- "Lizzy" comes from the banner (Q-H default).
- The first line and midpoint echo are not borrowed here (R11).
- The dumpling scene is kept (audit preserve).
- No city rewrites itself (SEP RNA7; Ch2 has no threshold geography).
- The spoon, door and landlord objects are planted (Promise-Ledger O5-O7).
- The meeting line is planted (Q136 leaves it unresolved, so fine).

---

## Chapter 3 (W03; old Ch3) and the Space Between

| # | Line(s) | Text (quote <=25 words) | Current decision (quote <=40 words) | Decision source | Kind | Level | Already listed in Decisions.md or Plan.md? | Confidence |
|---|---|---|---|---|---|---|---|---|
| 3.1 | 654-662, 698-728 | "Elizabeth held her books against her chest while Pathwell moved the Camp order." / "He pulled the cart through the doorway. Elizabeth went with him." | Q111: "She is given/takes up a stack of the newly purchased Camp books to carry onward. She places her recovered diary/cookbook on top of that Camp-book stack." Q114: "Pathwell takes his share ... through first"; Elizabeth, "with her recovered diary/cookbook atop the Camp-book stack she is carrying, independently chooses to follow." | Continued 48 §Q111 LOCK; Continued 51/52 §Q114; Timeline `Q111-stack`, `Q114-follow`, `Q120b` | inconsistency (minor). The recovered/choice order is right. But she carries no Camp stack: a shopkeeper's handcart, which Pathwell hauls, replaces it. She puts her books on the cart and goes "with him", not after him. Q109/Q47 say "exact transport scale is secondary", and Ch4 (lines 11-13) repeats the cart, so this may be a deliberate allowed variation. | scene | no | low |
| 3.2 | 400-420, 564 | "One had NEVER AGAIN written in the margin." / "It was written during the horse incident." / "It has been reasonable for eighty-three years." | Q109: "The exact origin and contents of the older balance are **not yet defined** ... and should not be invented without a separate decision if the manuscript needs them." | Continued 46 §Q109 user correction; Timeline `Q109-old-debt` | inconsistency (invented detail). The 08-28 rewrite supplies a number of years and the "horse incident". The scene itself never says what the debt was for. Promise-Ledger L5 treats it as an open-deliberate "world exceeds the scene" detail. | line | no (Promise-Ledger L5 only) | low |
| 3.3 | 484-492 | "Yours?" / "I have become very particular about that distinction." / "Yours?" / "Yes." | "A practitioner spends their own future possibility to pay for something else." Shade's prune: "The payment came entirely from Pathwell's own future possibility." | Bible 08-21 §3 Core law; Continued 19 §Shade origin; Timeline `96 pruning-currency` (08-21 §3), `C19 shade-origin-causal` | inconsistency (possible). "Particular about that distinction" implies he once spent a future that wasn't his. No lock says so, and Shade's origin lock says the opposite. Probably a wry nod to the shopkeeper's rule, but nothing on the page settles it. | line | no | low |
| 3.4 | 520-540 | "Pale lines opened from his shadow. They spread over the floor and split ... each division becoming two, then four" / "Branches folded inward." | AUDIT Ch3 [audit-directive, 08-23]: "Avoid imagery that reads as literal branching timelines. Abstract roots/branches may be retained only if they do not imply timeline selection." Q148 (08-27): future possibility is "a living branching structure" and "Pruning permanently removes branches." | AUDIT Ch3 "Required fixes"; Continued 67 §Q148; Timeline `AUDIT Ch3 sb-language`, `Q148`, `Q148b` | conflict between decisions. The 08-23 audit line was written before Q148, and Q148 is the author's own and newer. The text says "They were not pictures of anything", so it isn't timeline selection. Ch14 (lines 849-859) and Ch18 (lines 575-621) already build on it. No change needed unless the author wants the audit line to govern. | line | no | low |

Locks checked that the chapter follows: about 22. These are:
- She follows into the Space Between because he still has her books (Q111, Q118b; lines 182-186).
- Recovery comes only after "Settled" (Q111; lines 572-576), and the reclaim is hers.
- Her continuing is a free choice after the books are back (Q111, Q118b; lines 684-728).
- Camp is self-appointed: "Did Camp Cunnan ask you for all of this?" / "They need it." / "That was not what I asked." (Q108, Q107 moral function).
- Nobody authorises the prune; the coins and the note are refused and he offers "Future." himself (Q108-pruning-his-choice).
- A large book order staged in stacks at the counter, with no tome or envelope (Q109, Q120).
- One settlement covers the order and the old balance: "The order and the old balance together" (Q109-old-debt, Q120b).
- Proportionate physical cost: the arm shakes, and "You're thin." gets "Still standing." (Q109-shaking, Q148b; C25: Ch3 is the clean baseline).
- The custodian accepts and the ledger registers, with no second approval (08-22 §1).
- The shopkeeper is a distinct being, not the place (08-22 §1).
- The archive comes first and commerce second; no aisle tour (SEP A6).
- Ambient overwhelm that doesn't make her special (08-21 §4.15).
- The terrible coffee and "Familiar things are useful" (C7 §4; Ch9/Ch10 recall it word for word).
- The orange cat, "He likes documentation" and the mug are planted (Ch10, Ch18).
- Possession is not a magical lock; the shopkeeper uses house rules (08-21 §4.20).
- The exit is near Camp's edge: trees and a dirt path, then "the last stretch of dirt road" in Ch4 (Q114).
- Right-hand tremor carries into Ch5 (Q149).
- Nana's cookbook is the same handwritten book, with no Joy of Cooking (08-23 §1).
- The diary is intact (08-23 §4).
- The torn page is carried over from Ch1.
- Laundry ticket, meeting and front door carry over.

---

## Count of findings

| Chapter | Findings | High | Medium | Low | Not already in Decisions.md/Plan.md |
|---|---|---|---|---|---|
| Ch1 | 4 | 1 (1.2, no change needed) | 1 | 2 | 2 (1.3, 1.4) |
| Ch2 | 12 | 7 | 2 | 3 | 4 (2.6, 2.10, 2.11, 2.12), plus the curiosity-motive part of 2.4 |
| Ch3 | 4 | 0 | 0 | 4 | 4 |

Notes for the reader:
- Findings 2.1-2.5, 2.7, 2.8 and 2.9 are already in the Plan's Ch2 row. The audit adds two things to that row: the curiosity motive at line 455 and the "She could..." list at 435-441, which both fall under 2.4.
- The most consequential item the Plan does not name is 2.6. Pathwell knowingly refusing the books contradicts Q118, and restoring the July shape would fix it as a side effect.
- Ch1 shows no July-residue beyond what P7b already fixed. Ch1 is otherwise current.
- Not reported because they are prose rather than story-fact issues: Ch3 line 220 ("a father she had never buried"), the Ch3 "give them back" loop, and Ch1 line 39 ("They're… they're in the kitchen?" plural). The Plan and P7 already cover them.
