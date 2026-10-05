# Tenth seats: Chapter 13, 2026-10-05

**Evidence, closed; preserved whatever the verdict (Sunday D21).** Two reports. The first tested the pass's decisions (K1–K5), written before drafting: **YELLOW**. The second tested the triage's settled verdict "Chapter 13 needs nothing" (trigger 2): **ORANGE**. How both were answered is in [pass P38](../Pass-Log.md#p38-2026-10-05-chapter-13-shade-at-camp).

---

## 1. On the decisions (K1–K5)

# Tenth seat: the Chapter 13 decisions, 2026-10-05

tenth_seat: fresh agent (not the reviser)
against: ch13_decisions.md (K1-K5, written before drafting)
head_sha: ed46d6c (P37, /home/claude/pathwell; evidence read from the working tree and, where stated, git history; no repo file edited)
independent: true
verdict: YELLOW overall. K1 YELLOW as the lean is written (the triage's row 13.1 and "Chapter 13 needs nothing" as recorded: ORANGE). K2 YELLOW (it collides with K4 and protects the wrong section). K3 GREEN. K4 GREEN with conditions. K5 GREEN with two conditions.
summary: The plan can go ahead, but K1's reasons, K2 and K4 need correcting first. K1's lean (no explaining conversation in Ch13, log it, put it to the author) holds, and holds better than the triage argued: Ch14 already says the refusal three times (Ch14:609-635, :663, :967) and the cold reader called the "rejoining frame" a great reveal (Cold-Read:539). Three things in K1 are wrong or untested. (1) The triage's reason ("nothing later cites an earlier talk") tests the wrong object again: nothing in Ch14-18 cites a talk, but seven locks are homed in that scene. (2) K1 describes the lock as "predict, then explain". The lock set also wants Elizabeth warned (Q86), Elizabeth's stance (C1 §6, "I'm going to be there when he decides") and Shade's "holding onto" reading (Q82); none of those is in Ch14 or anywhere else, and Q82's evidence was just planted in Ch11 by W18. (3) "Restoring it would pre-spend Ch14" is true of an explanation and untested for one marked line of prediction, whose price is two Ch14 lines (:257, :513). K2 and K4 contradict each other: the lines K4 keeps ("This child is cheating." / "He's just better than you.") sit inside the queen-of-spades trap K2 says to cut. K2 also describes "Hearts 1" by lines that live in a different section (the recruitment), so the section it actually cuts (the "bad at Hearts" run) is the one whose only unique content is the second trap and "I don't know what I am here." Four later-chapter dependencies are not on the keep lists: "I know Hearts." (Ch17:625-629), the queen going back into the deck (Ch14:75; Hearts needs 52 cards), "By fewer points." (Ch17:683-687) and "Corruption." (Ch15:881).

Paths are under /home/claude/pathwell/Story unless given in full. Ch = Chapters/Chapter_NN.txt as it is today (Ch13 line numbers are the file's). C2, C15, C20, C21, C26, C56 = Interview/MANUSCRIPT_RECONCILIATION_AUDIT_REFINEMENTS_CONTINUED_N_*.md; "C1" = ..._CONTINUED_2026-08-23.md. Cold-Read = Revision/Cold-Read-2026-09-29.md. "Old Ch12" = git 765b69b:Story/Chapters/Chapter_12.txt (2026-08-26, before the 08-28 rewrite). I did not draft prose (Pipeline, "tenth seat": it never drafts prose); where a fix needs a line I say what the line must do.

**On the trigger.** This is Pipeline D21 trigger 2 (a lock-level KEEP in a triage that sent nothing to the author: 87 KEEP, 0 AUTHOR, triage.md:11) and, for the deviation itself, close to trigger 1 (a lock overridden because the reviser judges the text works). It also has a base rate: this is the fifth chapter where a triage KEEP over a lock was later put to the author after a tenth seat (Ch4 Q-M, Ch6 W15, Ch8 W16, Ch11 W18). The cause is structural and unchanged: the triage's KEEP means "differs only from an interview staging or line lock, and the text works" and its other category is a taste call (triage.md:7-9), so a lock deviation the reviser wants to keep has no route to the author. K1's lean (a W-row under W8) is the right repair and is not in dispute.

---

# Minority report: Chapter 13 decisions

## K1. No tree-line conversation in Ch13

**Claim, stated so it can be proven wrong.** Chapter 13 does not need a conversation, before Pathwell arrives, in which Shade predicts that Pathwell will try to put him back and explains why losing his independent self is unacceptable (Q79, C15/C16, C2 §11). Ch13's vignettes show a self worth keeping, and Ch14's "What happens to me?" / "Do I remain myself?" / "Can." / "Not will." / "Then no." gives the prediction and the reason when they matter. Restoring the conversation would pre-spend Ch14. Lean: keep the triage, log it as a W-row put to the author.

**Assumptions.**
1. The conversation is one thing: a prediction plus an explanation (K1's description).
2. What it does is done by Ch13 plus Ch14. (Triage 13.1: "Nothing later cites an earlier talk.")
3. A short version would be an explanation and so would pre-spend Ch14.
4. Ch13 is the chapter the lock names.
5. Keeping the departure from a lock as a logged working decision (W8) is enough; nothing else is lost.
6. Ch14 can lose the conversation without losing what the locks wanted from it.

**Weakest: 1 and 3 together, with 2 behind them.**

On 2: the same wrong test the Ch11 report found. The triage asks whether a later *chapter* cites the talk (none does; I grepped Ch14-18 for "told me", "he said he'd", "you said" and for the lock phrases: no hit). The dependents are *locks*, and there are seven, all homed in this scene:
- Q79 (C20:47-55; C21:9-14): Shade's advance prediction, marked as prediction ("I think", "he'll probably"); "preserves the tree-line conversation as the place where Shade can explain why loss of independent self is existentially unacceptable".
- C20:39 rejects the option K1 now chooses. Option D is "Remove all advance discussion... Shade says only that Pathwell is coming. The actual absorption proposal and Shade's explanation... happen for the first time at the central fire." The author's answer was the hybrid with A, and the audit's reason against D ("moves necessary stakes explanation into the climax", C20:43) is the triage's reason *for* the omission. The triage's "Ch14 gives the reason when it matters" is the rejected option's own rationale. (R23 lets a reviser overrule staging by what works; it does not make the rejected option cost-free.)
- C15:24 and C16: "He's coming." (no ETA).
- Q86 (C26:13): Shade tells Elizabeth because he does not know whether Pathwell will tell her before he acts.
- C1 §6 (C1:73): "I'm not going to tell him what to do. But I'm going to be there when he decides." Decisions.md:94 lists this as a lock the manuscript *follows* ("Let it fail"); the line itself is in no chapter (grep Ch11-14: none; triage 14.5 notes "the lock's 'I'll be there when he decides' is absent").
- Q82 (C2 §12; C21:75-): Shade's inference that Pathwell treats Elizabeth as something he can hold onto. W18 has just restored its evidence in Ch11 ("You took her from me." / "She wasn't yours to take from.", Ch11:47-49). Its payoff is in no chapter (grep Ch11-18: no "hold onto"/"holding onto") and in no ledger row.
- C2 §11 (C2:130-140): technical uncertainty plus existential certainty, "whatever it is, it isn't me".
- Q119c (C56:32): "Shade's important relationship material with Elizabeth remains in the diner, museum aftermath, tree-line conversation, resistance to the draw, refusal of reintegration, and climax." This is the newest of them (08-26), so the conversation survived the 08-26 pass.

The conversation is also *existing text*: old Ch12 (765b69b) lines 46-102, about 350 words at a tree line in the dark ("He'll be here by morning." / "He's going to try to cut me loose." / "It kills me." / "I'm telling you because he won't tell you." / "I'm not going to tell him what to do. But I'm going to be there when he decides." / "you're not what he described"). The 08-28 rewrite dropped it without a record; it is on no list in Decisions.md (neither "locks the manuscript doesn't yet follow", :62, nor "follows", :78). R23 prefers existing text to new material, and this is existing text with a lock-shaped repair for every stale line.

On 1: the lock set wants three jobs from the scene, and K1 names one and a half. (a) Say the threat before it arrives (Q79, C15). (b) Say why it cannot be accepted (C2 §11). (c) Give Elizabeth a place beside Shade in it: the warning (Q86), her stance (C1 §6), the reading of Pathwell's "holding onto" (Q82), and a serious register between the two of them (Q119c). The lock fixes the *order* too: C24 has the diary donation come "before Elizabeth seeks Shade out for the tree-line conversation" (Decision-Timeline.md:470), so the home is the end of Ch12, not Ch13. Ch12 ends "Elizabeth sat beside the fire. Her shoulder hurt. Pathwell still wasn't there." (Ch12:440): the slot is open. K1 asks the wrong chapter. (Currency-Audit verification.md:19 row 11 said "place it at the end of Ch12 or in Ch13".)

On 3: the pre-spend claim is about (b). Job (a) is a separate, small thing. A single marked line of prediction ("I think he'll try to put me back.") says *what*, not *why*, and spends none of Ch14's "Do I remain myself?"

**Strongest alternative.** Not "restore the tree-line scene". A capable person would defend this: Ch13 carries no explanation and no existential talk, and the lock chain is logged and put to the author; *and* the reviser offers him the narrower option, which is one marked prediction inside the beat that is already there (Ch13:746-752, "Stronger." / "Closer?" / "Probably." with Mama Baga watching at :766-776), with Elizabeth's answer being her C1 §6 stance (she will not tell him what to do; she will be there). Its price is Ch14:257 ("Elizabeth understood that only later.") and Ch14:513 ("Tell me he's wrong."), and the reveal at :485 becomes confirmation. Its gains are the dread the contract asks for (W14 exit state: "Pathwell's arrival becomes threatening because the reader now knows what could be erased", Story_Files/PATHWELL_MAPS_L_CHAPTER_CONTRACT_MATRIX_2026-08-28.md:591) and a Q86/C1 §6 beat. The full tree-line scene, or the end-of-Ch12 placement, is the author's call.

**Evidence that should exist if the alternative is true, and whether it does.**
- The contract's exit-state sentence is unmet by Ch13 as it stands. Partly. Ch13 never says what Pathwell will do; the threat is the draw only (Ch13:41, :506, :716-724, :746). Ch14 opens on banter ("I'm standing beautifully", Ch14:91; "medically outnumbered", :211) and the cold reader says "attention dipped until Shade said 'That's not diagnostic'" (Cold-Read:536). A named threat would turn that stretch from banter into suspense. This is the best evidence for the alternative.
- The Ch13 sag is partly dread-starved. Weakly. The reader calls the hand "a metronome, not an escalation until the very end" (Cold-Read:494). But the drag items the reader names are repetition (coffee, "the second and third Hearts sections", :495), and a prediction line would not cut those.
- The audit's own directive, "Shade's objection should prepare his later explicit refusal", is unmet (audit_ch13-15.md:15). It is. Ch14:609 is the first time the reader hears the basis, "with nothing prepared".
- A relationship beat is missing. Elizabeth and Shade are "an easy, wry friendship" at the end of Ch13 (Cold-Read:513), which is the register of the lock's *other* Shade/Elizabeth scenes, not the serious one Q119c names.

**Evidence against the alternative (what holds the omission up).**
- Ch14 already says the existential certainty three times, so a Ch13 version is a fourth: "Do I remain myself?" / "Can." / "Not will." / "Then no." (Ch14:609-635), "I am the person living with it," ... "No." (:663), "Nothing changing is acceptable to me." (:967). The cold reader called the first "the strongest dialogue in the book" (Cold-Read:540). Rules.md, tone guardrails: "One sad moment, said once." Mama Baga's Ch16:1120-1124 is a fifth telling ("He said no when somebody tried to decide what happened to him.").
- Ch14 meets the *purposes* of Q86 and C26 better than a warning would. Q86 exists because Shade does not know whether Pathwell will disclose; Ch14 stages exactly that (he builds under fidgeting, then answers truthfully when asked: "Tell me he's wrong." / "He isn't.", Ch14:513-517), which is C26's rule ("when Elizabeth directly demands the truth, Pathwell does answer her", Decision-Timeline.md:476).
- The Ch14 first third is a lock too: Q147 (he builds the frame while talking), and the contract says "Shade recognizes emerging purpose first; Mama Baga shortly after" (matrix W15). The cold reader praised the misdirection ("structurally clever", Cold-Read:536) and "Two anchors. One return." / "You're building a rejoining frame." as a "Great reveal" (:539). Ch14:257 ("Elizabeth understood that only later.") and :601 ("The whole ordinary morning behind them seemed to contract around the sentence.") both lean on Ch13 being plain.
- The reader already predicts the right conflict with no line of warning: "Shade's newly won choice ('I want to stay here') will be tested against Pathwell's instinct to fix or contain him" (Cold-Read:507) and braced for the archive and Milo (:511). So the dread is present.
- The contract's own stale list and tone job: "Shade explaining full metaphysics" is stale; "This is not a funeral rehearsal"; "If every beat foreshadows death, the chapter fails" (matrix W14:575-625). The loss-memory job ("let reader remember him simply being alive") is why Ch16:1124 can list "He chose to stay here. He played cards. He made bad coffee." as a person's evidence. A conversation in Ch13 about what Pathwell will do to him colours every vignette after it.
- Craft 13: "Theme through action, not speeches"; the AI-cautious category list names "philosophical statements" and "character-defining dialogue" (Craft.md:79, :192). The conversation is exactly those, to be written by the author or flagged.
- R23 ("rather than inventing new things that we have to make fit", Decisions.md:47) cuts both ways, but a new scene that forces edits in Ch14 is the thing R23 warns against.
- The reversal is cheap either way. Ch14 has not had its pass (Plan row 14 waits on the climax option, Plan.md:129), so adding the line later costs a new scene plus two Ch14 lines; removing a line added now costs the same.

**What would disprove the alternative.** The author reading Ch14's first third and saying it works as misdirection; or a reader who gets to Ch14:485 having been told and says the reveal is flat.

**Cost if wrong.**
- If the omission is recorded as settled ("needs nothing", triage.md:221) and is wrong: seven locks lose their home, Q82's plant (W18) has no payoff, and the audit's "prepare the refusal" is unmet; the loss shows only when someone writes the scene after Ch14 has been polished around its absence. The record also tells later sessions the locks were followed (Decisions.md:94 says C1 §6 is followed).
- If it is logged and put to the author and he says "keep it out": a W-row.
- If he says "put it back": a scene of about 300 words (the old text is in git) plus Ch14:257 and :513. The Ch12 end is the cheapest place.

**Verdict: YELLOW for K1's lean; ORANGE for the triage's row 13.1 as recorded** ("KEEP... Nothing later cites an earlier talk", "the tree-line talk is not missed", triage.md:184 and :221). Proceed with no tree-line talk in the draft if all of these hold:
- (a) **Log it as W19** (W16/W18's shape): "Chapter 13 keeps no tree-line conversation, over Q79, Q82, Q86, C15/C16, C1 §6, C2 §11 and Q119c; put to the author under W8; the lock rows stand." List the dependents that make the omission work (Ch14:257, :513, :601, :609-635, :663, :967) so a reversal has a known price. Reword triage.md:221 from "needs nothing"/"not missed".
- (b) **Say in the log what the lock wanted that Ch14 does not supply**: Elizabeth's warning (Q86), her stance (C1 §6), the "holding onto" reading (Q82), and a serious Shade/Elizabeth scene (Q119c). Add a Promise-Ledger row for Q82 ("planted in Ch11 by W18; payoff absent from Ch12-14") and one for C1 §6.
- (c) **Put the narrower alternative to the author with its price** (one marked prediction in the :746-752 beat, no why; Ch14:257 and :513 change), and the placement question (end of Ch12, per C24, or Ch13). Do not word this as a choice between "the full scene" and nothing.
- (d) **Change the reason K1 gives.** "Would pre-spend Ch14" holds for the explanation and is untested for a prediction; say so.
- (e) **Nothing in the Ch13 draft states what Pathwell will do or why Shade refuses.** Keep the "Stronger." / "Closer?" / "Probably." exchange (Ch13:746-752) as the surviving trace of Q79's draw half and C15/C16; K5's cut of the "Not certainty. / Not distance. / An inference from pressure." gloss is fine so long as "Probably." and "Closer?" stay.
- (f) If any trace is wanted without the author's answer, it is the one line above; nothing longer.

**Reopening indicators.** The author says Elizabeth should be warned, or wants the scene; someone writes Q82's "holding onto" line and finds no anchor; Ch14 is line-passed and Ch14:257 or :513 is revised; a reader asks why Ch14's first third has no dread; the cold reader of the next run says Ch13 "waits for Pathwell" again.

---

## K2. Tighten the middle so each vignette changes something

**Claim, stated so it can be proven wrong.** Every vignette in the middle of Ch13 (jacket, coffee, Hearts 1, Hearts 2, the queen and "Pockets", the onions, the last hand) changes something, so each stays and the work is cutting its repetition. The named cuts (the second queen-of-spades trap; the procedural-joke run around "Pockets"; "They bounce." / "Good system."; the purple-foot joke; the "chain of custody" queen return, "or make it plain") remove nothing a vignette needs or a later chapter uses.

**Assumptions.**
1. Each vignette changes what K2 says it changes.
2. The cuts are repetition, not load.
3. The lines K2 credits to "Hearts 1" live in the section K2 trims.
4. K2's cuts are compatible with K4's keep list.
5. Keeping all seven answers the Assessment (B8, Assessment:37) and the cold reader's drag (Cold-Read:494-495).
6. The queen return can go.

**Weakest: 3, 4 and 6** (execution, not direction). The direction (keep every vignette) is the part the later chapters most clearly support.

**What holds the direction up (for K2).** Every vignette is spent later, separately. Ch16:1124 ("He chose to stay here. He played cards. He made bad coffee. He died.") lists the onion choice, Hearts and the coffee; Ch16:546-554 and :1104 spend the jacket ("LIKED POCKETS."); Ch15:1114-1120 lists the coffee, the jacket, the cheating and "I did not know yet what else he liked"; Ch17:621-687 spends Hearts ("I know Hearts." / "Shade said that." / "He was bad." / "Shade was better."). The contract's test is "If W14 can be removed without making Shade's death hurt less, W14 has failed" (matrix:857); Promise-Ledger R13 lists the same set as the setup. A harder alternative ("merge the coffee into the jacket scene", or cut a vignette whole) would break one of those payments. The Assessment's protect list names Hearts, "Pockets." and "I want to stay here." (Assessment:42).

**Where K2 goes wrong, in the text.** Section map (words): jacket 438 (:9-131), grinder 170 (:134-200), coffee 272 (:203-303), recruitment 242 (:306-398), "bad at Hearts" 219 (:401-473), fifth game 212 (:476-540), queen and "Pockets" 263 (:543-643), onions 445 (:646-826), last hand 259 (:829-909).

1. **K2 credits "Hearts 1" with lines from the recruitment and cuts a trap from the next section.** "Milo's name", "I know the rules." / "I don't remember playing." / "Then today you play." are at :364-390, in the recruitment. The "second queen-of-spades trap" is at :433-445, in the "bad at Hearts" section. The section that actually changes nothing on its own is the second one: its unique content is the two traps, "I don't know what I am here." (:459) and Milo's "You're losing." / "Apparently that." (:461-467). It is also the "before" the Hearts shift needs ("Shade was bad at Hearts... because he knew exactly why each bad decision had been bad about three seconds after making it", :401-405: that is the remembered-rules failure the fifth game answers), and Ch17:641 and :687 spend it. So: compress that section hard, but keep the "bad" and the "again", and keep it as one section.
2. **K2 and K4 contradict each other.** K4 keeps "This child is cheating." / "He's just better than you." (:439-445), which are inside the trap K2 says to cut. They cannot both be executed. The second trap also carries what no other section does: Milo "had been setting [it] for six rounds" (:433) is Milo playing the people before Shade learns to, which is the plant for the fifth game (:476) and for Milo reading Shade's thumb (:851); and the hinge "You see how they treat guests." / "I thought you weren't a guest." / "I don't know what I am here." (:451-459). The first trap's unique content is "I dislike the game." / "You have nineteen points." / "I dislike you." (:417-421), which gives Elizabeth's "You liked that." / "Playing." / "Yes." (:579-589) its reversal. My reading: keep the second trap (it holds K4's keeps, the hinge and the plant) and let the first shrink to the line that introduces the queen and the score; "again" at :435 then has to change. This is the reviser's call; what is not acceptable is cutting the second and keeping K4's lines.
3. **"I don't know what I am here." is character-defining dialogue** (Craft.md:192, the AI-cautious list) and is Shade's closest thing in Ch13 to the identity talk K1 keeps out. If the trap it hangs on goes, it goes, so it belongs on the author's list.
4. **The queen return has to stay (K2's "cut it, or make it plain": the second half).** Shade pockets the card at :627. Hearts is four players and thirteen cards each (:839), so the deck is a card short from :627 until Milo "put the queen into the deck" at :712. Ch14:75 has the archivist pick the queen of spades off the dirt; Ch14:25 has Milo say "He had the queen"; Ch15:717 and :855 and Ch17:659 all assume one queen in a whole deck. If the return goes, the last hand has two queens or none. Make it plain: the card goes back to Milo, the deck is whole, nothing witty. (It is also Shade giving up the first thing he said he liked, to a child; it is the "Cards later?" / "Yes." at :688-694 that pays as "You still owe me a hand", Ch15:859 and Ch16:506.)
5. **"The procedural-joke run around Pockets" is, in the text, "Evidence." / "Corruption."** (:549-553) plus "Milo is a child." / "Exactly. No one suspects him." (:555-557). K4 keeps the first pair, correctly: "Corruption." plants "Corrupt institution." (Ch15:881), which the Assessment protects (Assessment:42), and the archivist's "Evidence is inconclusive." (Ch14:79) and Ch17's "evidentiary standards" (:655) and "She called it evidence." (:835) are the same register. The two follow-on lines are the cut.
6. **The potato set-up** (:648-662): "They bounce." is the plant for the onion drop that rolls (:716-724), and "Good system." echoes Shade's own "Efficient system." in Ch12:19. Cutting both is fine; "Why is that better?" must go with them. Keep the escape thread: the three escaped onions (:722), the second onion (:818-826) and "an onion that had somehow escaped again" (:905), because Ch15:855 ("the escaped onion") needs it.
7. **The purple-foot joke** (:674-686) is a prank, not a procedural quip: Shade's only deception-for-fun, with "Shade's mouth twitched" (:682). It is the one beat where he teases Milo, and Ch14:145-151's easy "Are they always like this?" / "You would know." / "Sorry." leans on a bond built here and at the table. It is also the third "the child out-reads Shade" shape in the chapter. Either call can be defended. Keep the cloth on the calf and "That's going to cut off your circulation." / "Fixed it," (:664-672): that is the sock set-up Ch15:104, :857, Ch16:37 and ledger R11 pay. If the joke goes, "You are a bad person." / "I've been told worse." goes with it; "I've been told worse" sits near C15's rule against implying a long personal history for a man created days ago.
8. **Hearts 2 "trim the list"** (:480-486): keep the archivist scratching his nose "when holding the queen" (:482): it is the parallel for Milo's "You scratch your thumb when you have it" (:851), the reversal that pays the shift. The narrator's flourishes about the older woman and Milo's bluffing are the cut.
9. **The coffee.** Keep, for the reason K2 gives: the audit counts "Then I don't remember it" as a lock the chapter follows (audit_ch13-15.md:18, G4: creation-time fragments only), and Ch16:1060-1068 and Ch15:1114 spend the liking and the badness. Do not trim :209-213 as "commentary": "The knowledge came easily enough that Elizabeth could see him distrust it. / He would start a motion, pause, then continue only after looking at what his hands were actually doing." is the first showing of inherited know-how against his own doing, the idea the Hearts shift then states. The cold reader's coffee drag is the *fifth Space Between* (Cold-Read:495); K2 keeps that exchange (:267-289) and it is the only one with new content (Shade learns it is not his), so the fix is the commentary around it, as K2 says.

**Lines used later that K2's keep list leaves out** (add them): "I know Hearts." (:350) and "You said that," (:384) for Ch17:625-629; "Shade was bad at Hearts" (:401) and "By fewer points." (:490) for Ch17:641, :683-687; "Too many." (:119) and "half an inch short" (:75) for Ch15:713-715, :932; "I changed my mind." (:629) for Ch14:47-49, :603-605; "You have the queen." and the thumb (:845-855) for Ch14:25; "Cards later?" / "Yes." (:688-694); the sock cloth (:664-672).

**A dangling reference this pass should log.** Ch15:1118 ("Milo saying he was cheating") has no source in Ch13: there Shade says the child is cheating (:439) and Milo only reads his tell. Ch16:488-496 has Milo say Shade cheated, with a joke that works alone. Either Ch15:1118 changes (it is the cheaper edit; Ch15 has not had its pass) or Ch13 gets a Milo accusation; do not cut :439-445 without deciding.

**Evidence that should exist if the alternative ("cut deeper, or merge a vignette") is true, and whether it does.** The cold reader's drag is in the Hearts and coffee sections (Cold-Read:495): yes. The Assessment says the point lands at the jacket and the rest "makes it again" (Assessment:37, :136): yes. But the readers' own best lines are in the sections K2 keeps (Cold-Read:501-503), and every vignette is spent later (above). So the alternative wins on length, loses on the later payments, and K2 is the right trade.

**Cost if wrong.** Lines, in git, if caught in this pass. If the queen return or "I know Hearts." is cut and found after Ch17 is polished: a continuity fix in Ch14 and Ch17 and the loss of Ch17's best echo ("Hearts with Pathwell... the best moment in the chapter", Cold-Read:669). If the second trap is cut and K4's lines are kept anyway: orphaned replies.

**Verdict: YELLOW.** Direction holds (keep every vignette); execution needs these conditions:
- (a) Resolve K2 against K4 before drafting: decide which trap stays; if the second goes, say where "This child is cheating." / "He's just better than you." and "I don't know what I am here." go, or drop them from K4's keep list.
- (b) Aim the Hearts cut at the "bad at Hearts" section (:401-473), not the recruitment.
- (c) The queen goes back into the deck, plainly.
- (d) Add the used-later lines above to the keep list.
- (e) Decide the purple-foot joke knowingly (it is Shade's own mischief) and keep the sock cloth either way.
- (f) Log the Ch15:1118 mismatch.
- (g) Flag "I don't know what I am here." for the author.

**Reopening indicators.** Ch14 or Ch17 is revised and the queen or "I know Hearts." has gone; a reader counts the deck; the cold reader still drags in Hearts after the trims; the author says one of the cut jokes was his favourite.

---

## K4. B7, the shared deadpan

**Claim, stated so it can be proven wrong.** Cutting six of Shade's procedural jokes ("Laughing seems medically irresponsible.", "This camp communicates like a hostage situation.", "That seems deliberately dangerous.", "Chain of custody has already been compromised.", "That is inconvenient.", "Good system.") answers B7 in Ch13 and leaves a Shade who is himself: "Evidence." / "Corruption.", "I can choose badly.", "Pockets.", "This child is cheating." / "He's just better than you.", "This place is hostile." / "You're still here." Milo (blunt), the archivist (dry about records) and the older woman (silent) keep their own registers.

**Assumptions.**
1. The six are the lines B7 means (Assessment:36; Cold-Read:521: Shade's humour is "procedural-legal, much like the narrator's... I could swap many lines between characters").
2. Each can go without orphaning the lines around it.
3. No later chapter uses them.
4. What is left is Shade's and not the narrator's or Pathwell's.
5. Subtraction is an adequate remedy for B7.
6. The registers K4 gives the others are the ones the text gives them.

**Weakest: 2 (mechanical) and 4 (a taste call, and the author's).**

**Evidence for.**
- Assumption 3 holds. None of the six, and none of their wording, is in Ch10-18 (grep: "hostage", "chain of custody", "medically", "good system", "deliberately dangerous", "inconvenient", "irresponsible": only Ch14:211, Pathwell's own "I am being medically outnumbered.", and Ch12:19's "Efficient system."). Cutting Shade's "medically" line leaves Pathwell's as the only one. P37 already cut a "medically useful category" line in Ch12 (Pass-Log P37).
- The shared register is not only Shade's: Ch10:343 ("Do not anthropomorphize the evidence."), Ch14:79 (the archivist's "Evidence is inconclusive."), Ch17:655 and :835 all use the evidence/procedure joke. B7 is real and book-wide, and the cold reader's complaint is exactly that the narrator and Shade converge (Cold-Read:521).
- The kept "Evidence." / "Corruption." is the right one to keep: it plants "Corrupt institution." (Ch15:881), which the Assessment protects (Assessment:42), and Ch17's "evidentiary standards".

**Evidence against (what K4 under-counts).**
- **Orphans.** Each cut joke has a reply left standing: "I'll risk it." (:184) answers the medical joke, and Elizabeth's laugh runs :178 → :469 ("Elizabeth laughed again."), so the first laugh must stay; "That was considerably better." (:332) answers the hostage joke and is on neither list; "The boy considered this." (:166) follows the pepper joke; "Mama Baga nodded." (:776) answers "That is inconvenient."; Milo's "That's not evidence." (:704) loses its answer when "Chain of custody..." goes, and "Milo stared at him. / Shade stared back." (:708-710) were the reaction to that joke. These are mechanical, but they are exactly the kind that survive a trim by fragment-merging.
- **The Plan's own remedy for B7 is not subtraction.** Plan.md:93 says "Perspective shift, speaker by speaker, with the lived-specificity lens... Shade through inheritance... It proposes lines; the author writes them", and the Assessment's owner for B7 is "The author (character-defining dialogue); AI marks candidates only" (Assessment:36). K4's cuts are candidates, which is within bounds if they are listed for him (K4 says they are). But "what's left is his" is not established: the six kept lines are mostly the same understatement shape ("I can choose badly.", "This place is hostile."), and "Evidence." / "Corruption." is the same legal-domain move as the cut "Chain of custody", kept once for a plant. The honest claim is "fewer, and one plants Ch15".
- **"Shade through inheritance" is the Plan's key for him, and K4 gives him none.** Ch13 is about what he inherited and what is his ("I have inherited worse problems.", :81; "Not Pathwell's smile.", :129; the coffee; the Hearts shift). His best line of that kind is in the jacket scene, which K2 leaves alone. Fine; but cutting his procedural jokes should not leave Shade with no joke that comes from what he is. The one place the chapter has it is the purple-foot prank (:674-686), which K2 also cuts (K2 item 7).
- **The replacement tic** (Pipeline step 7). After the cuts, the rhythm of "Shade says something dry / the other person looks at him" will want a new filler. The cut list should not be answered with new Shade quips; Craft lesson 4 ("If cutting it changes nothing, cut it, and don't replace it").
- **The registers list is partly off.** The older woman is "silent" in Ch13 except "Absolutely not." (:889), and she speaks in Ch14:63-71 ("I was winning."); Milo's "That's not evidence." (:704) and "Do those count as played?" (:885) are rules-lawyering, which is his fairness-and-games register (Plan:93), not "blunt"; "Then today you play." (:390), given to the archivist, is a warm line and not dry about records. None of this changes the cuts; it changes what the author is told.
- **The tag at :441-445.** "No," the archivist said. / "Thank you." / "He's just better than you." has no tag on "Thank you." (Milo, presumably); fragment-merging can make the order of speakers worse.

**Cost if wrong.** A few lines, all in git. The wider cost is that B7 "Ch13 onward" (Plan:93) is a book-wide problem and the Ch13 trims will read as complete when they are one chapter of it: Ch14-17 carry the same shapes ("That's a nautical term.", "evidentiary standards", "Inherited badly.").

**Verdict: GREEN with conditions** (the cuts are safe; the conditions are mechanical).
- (a) Cut the orphaned replies with their jokes: :184, :332, :166, :776, :708-710, and decide :704.
- (b) Keep :178 and :469 (the laugh) and "Cards later?" (:688-694); keep "Evidence." / "Corruption." for Ch15:881.
- (c) No replacement quips; run step 7 on the result.
- (d) List the cuts for the author as B7 *candidates*, say plainly that "what's left is his" is the author's to confirm, and correct the registers note (above).
- (e) Add the cut shapes to the Registry's watch patterns so Ch14-17 are checked against them.
- (f) Resolve K2/K4 over :439-445 before drafting (see K2).

**Reopening indicators.** The author says one of the cut lines was his, or that Shade now has no humour; the next cold read still says "I could swap many lines between characters" in Ch13; the replacement tic appears.

---

## K3. A varied opening (brief; GREEN)

**Claim.** Ch13 should not open on a personified Camp ("By full morning, Camp Cunnan had decided Shade was neither an emergency nor an explanation. / It found work for him instead. / This happened without a meeting.", Ch13:3-7), since Ch12 does ("Camp Cunnan was awake enough to notice trouble and asleep enough to resent it.", Ch12:3). It opens instead on the existing sentence at :9: Elizabeth by the fire, Mama Baga pinching Shade's sleeve.

**Evidence for.** The pattern is the Assessment's (Assessment:183: Ch6, 11, 12, 13, and Ch17; "Three of them (11, 12, 13) are consecutive. Fix: vary Ch12 or Ch13"); the cold reader noticed it (Cold-Read:522); Plan.md:169 already chose Ch13 so that Ch12 can stand; and Ch11 no longer opens that way ("The drive took most of what was left of the night.", Ch11:3), so after the change the run is Ch12 alone. The replacement is existing text, not new.

**What the opener carries, and the conditions.**
- A time bridge: Ch12 ends at dawn at the fire (Ch12:434-440) and Ch13 begins "By full morning". Mama Baga's "You have been planning to for forty minutes." (:19) carries elapsed time; keep a morning marker in the first lines anyway.
- The chapter's spine: Camp *asks* Shade for things (the sleeve, the grinder, a fourth player, two hands) and the chapter ends the thread on "Asking." (:810). The vignettes show it; the opener only names it, and the cold reader read the point without it (Cold-Read:494).
- Do not put the tree-line or a prediction in the opening to vary it: the contract (matrix W14) says "not a funeral rehearsal", and the first line is where that tone is set.
- A small echo to watch: the section opener "Camp kept moving." (:646) is the same move at smaller scale, and Ch16:3 uses it again ("Camp Cunnan kept moving."). Fix the opener first; leave the rest.

**Cost if wrong.** Nil. **Verdict: GREEN.**

---

## K5. Line pass (brief; GREEN with two conditions)

**Claim.** The narrator commentary listed ("Elizabeth was getting better at that distinction.", "That, apparently, settled it.", "No philosophy followed.", "This seemed to make him happier than winning might have.", "No hesitation.", "No follow-up inspection. / No suggestion that his judgment outranked hers.", "That was becoming one of the easiest ways to tell them apart.", "Not certainty. / Not distance. / An inference from pressure.", "He was losing the fight with the draw by inches. / He was winning the hand.") can go, fragments merge, and the kept list (the last hand, the queen face-up beside an onion, "That hand was promising.", "Then the threshold opened.") covers what Ch14 opens on.

**Evidence for.** Every item is narration, not a line anyone says; the cold reader named most of them ("the machine", Cold-Read:517; the fourth statement of the fills-silence distinction, :516; "Elizabeth laughed again. Her shoulder objected.", :519). Nothing in Ch14-18 quotes any of them (grep). The keep list is right: Ch14:3, :25 and :75 and Ch15:855 depend on it.

**Two conditions.**
1. **"He was winning the hand." (:843) is the plant for Ch14:69-71 and Ch15:873-875** ("I was winning." / "You were not."), and for "That hand was promising." (:907) meaning anything. It is the only line that says the hand was going well; the visible beats (Milo reads the thumb, :845-855; "This place is hostile.") read as Shade being caught. Cut "He was losing the fight with the draw by inches." (the strain is already in the cards sliding and the hand against his knee) and keep or re-seat the half that says the hand was good. Also: "This seemed to make him happier than winning might have." (:492) is on the cold reader's *Gripped* list (Cold-Read:501), quoted whole. It can go only if "By fewer points." (:490, which Ch17:683-687 spends) and "Again?" / "Yes." (:496-500) carry it; they do, and "Yes." answered by surprise is the stronger version. Keep "By fewer points.".
2. **Keep "Closer?" / "Probably." (:748-752) and "Not Pathwell's smile." (:129)**; only the gloss lines go. After merges, check speaker tags (":441-445" has an untagged "Thank you.").

**Verdict: GREEN.** Cost if wrong: lines, reversible.

---

# Overall verdict: YELLOW

| Decision | Verdict | One-line reason |
| --- | --- | --- |
| K1 no tree-line talk | YELLOW (triage row 13.1 as recorded: ORANGE) | The lean holds; the reasons need correcting and the lock chain must be logged and put to the author. |
| K2 tighten the middle | YELLOW | Direction holds; collides with K4, aims at the wrong Hearts section, and drops four later-chapter dependencies. |
| K3 varied opening | GREEN | Existing text, nil cost. |
| K4 B7 cuts | GREEN with conditions | Safe against later chapters; orphans and the "what's left is his" claim need handling. |
| K5 line pass | GREEN with two conditions | Plant and gripped-line care. |

Proceed with the draft on these conditions, in this order:
1. Log K1 as W19 (W18's shape): the seven locks, the dependents that make the omission work, the Q82 and C1 §6 rows, and the one-line alternative with its price (Ch14:257, :513). Reword triage.md:221 and row 13.1; say that "would pre-spend Ch14" applies to the explanation.
2. Resolve K2 against K4 (which queen trap stays; where "This child is cheating." / "He's just better than you." and "I don't know what I am here." live) before any prose.
3. The queen goes back into the deck, plainly (Hearts needs 52; Ch14:75; Ch15:717, :855; Ch17:659).
4. Add to the keep list: "I know Hearts." (:350), "You said that," (:384), "Shade was bad at Hearts" (:401), "By fewer points." (:490), "Too many." (:119), "half an inch short" (:75), "I changed my mind." (:629), "Cards later?" / "Yes." (:688-694), the sock cloth (:664-672), "You have the queen." and the thumb (:845-855), the escaped onions (:722, :818-826, :905).
5. Cut the orphaned replies with their jokes (:184, :332, :166, :776, :708-710); no replacement quips.
6. Log the Ch15:1118 / Ch13:439 mismatch ("Milo saying he was cheating") for the Ch15 pass.
7. List for the author: the six B7 cuts, "I don't know what I am here.", the registers note (corrected), the purple-foot call.

**What this report did not find.** No lock requires any Ch13 vignette to be cut or kept as a scene. No later chapter quotes any of the six cut jokes or the K5 narrator lines. No lock is touched by K3. Ch14's existential refusal (:609-635, :663, :967) covers C2 §11's content in full. The "needs nothing" paragraph's claim that the child is Milo all the way through holds (Ch4 through Ch17).

**What I could not verify.**
- Whether the old tree-line text (git 765b69b, 2026-08-26) was the author's own writing or an earlier AI draft. His working draft stops at the museum and has no "tree line" talk or "cut me loose" (grep of working.txt), so the scene may be AI text that the locks then repaired; the locks are his either way.
- Whether the "C+A HYBRID" label in Q79 was his phrase or the AI's. The lock set is his rulings (Interview/README.md).
- Whether one marked line of prediction in the :746-752 beat would read as prediction and not as plan-telepathy (Q79's boundary). That is prose, and I did not draft it.
- How a reader reacts to Ch14's first third and the "rejoining frame" reveal with a warning in Ch13. The only evidence is the one cold reader, who read the unwarned version.
- The "fifth Space Between" drag: whether the reader means Elizabeth's telling at :267-289 or the recitals in earlier chapters (I read it as the former plus the count).

**Questions only the author can settle, in the order they are likely to change the chapter.**
1. **Q1. Is Elizabeth warned before Pathwell arrives?** The locks (Q79, Q86) have Shade tell her, before he arrives, that he thinks Pathwell will try to put him back; the manuscript has her and the reader learn it with the pins in Ch14 ("Elizabeth understood that only later."). Options: no warning (the manuscript; default, because the Ch14 reveal and the "ordinary morning" depend on it); one marked line in Ch13's "Closer?" / "Probably." beat (prediction only, no why; Ch14:257 and :513 change); or the old tree-line scene at the end of Ch12 where the locks put it.
2. **Q2. "I'm not going to tell him what to do. But I'm going to be there when he decides."** (C1 §6) is in no chapter, and Ch14 has Elizabeth say "You heard him." / "Then put it away." (:647-653). Is the line still wanted, and where?
3. **Q3. Shade's "holding onto" reading of Pathwell** (Q82) has no home now that Ch11 plants "She wasn't yours to take from." Do you want Shade to say something like it to Elizabeth before Ch14, or is the Ch11 exchange enough?
4. **Q4. Shade's humour.** Is his deadpan meant to be the one he inherited from Pathwell (Plan: "Shade through inheritance"), and which of "Evidence." / "Corruption.", "I can choose badly.", "This place is hostile." are plainly his? Do you want the purple-foot prank (the one beat where he teases Milo) kept?
5. **Q5. "I don't know what I am here."** Keep as spoken (it hangs on the second queen trap), or let him show it?
6. **Q6. Who says "cheating"?** Ch13 has Shade accuse Milo; Ch15:1118 and Ch16:488 have Milo accuse Shade. Which way round?

**Reopening indicators (all).** The author wants Elizabeth warned or the tree-line scene; someone writes Q82's line or C1 §6's and finds no anchor; Ch14 is line-passed and :257 or :513 changes; Ch14 or Ch17 is revised and the queen or "I know Hearts." has gone; a reader counts the deck; the next cold read still drags in Ch13's Hearts or still says "I could swap many lines between characters"; the replacement tic appears; the cut jokes turn up again in Ch14-17.

---

## Appendix: the decisions as written

(K1-K5 as in /tmp/claude-0/-home-claude/c14102f3-1f35-5356-85de-0367ac67de1f/scratchpad/ch13/ch13_decisions.md, written before drafting, 2026-10-05; not reproduced here.)

---

## 2. On the triage verdict

# Tenth seat: the Chapter 13 verdict ("needs nothing"), 2026-10-05

**Evidence, closed; preserved whatever the verdict (Sunday D21).** Tests the 2026-10-01 triage's verdict on Chapter 13 (rows 13.1 and 13.2 and the "**Chapter 13.**" paragraph) against the locks, the author's rulings and the manuscript as it stands after today's line pass.

tenth_seat: fresh agent (not the reviser; not the checker)
against: Currency-Audit-2026-10-01/triage.md:184-185 and :221 ("Chapter 13. It needs nothing.")
head_sha: ed46d6c (P37) plus the uncommitted Chapter_13.txt line pass (working tree). Old chapters read from git (765b69b, 4a1d69c).
independent: true
verdict: ORANGE overall, as the verdict is recorded. 13.1 ORANGE (the structure holds, YELLOW; the record "needs nothing" does not; two locked contents have no home anywhere in the book). 13.2 GREEN, with two corrections to the record. W14's other duties YELLOW (one clause of the exit state is only loosely met).
summary: Chapter 13 can stand as the chapter it is. It is not the weak point of the book, the later chapters lean on it hard (Ch15:1114-1122, Ch16:546-554 and :1116-1128), and a blind reader found Ch14's refusal "direct and earned" without a prior talk. What cannot be recorded is "needs nothing". The triage tested "does a later chapter cite an earlier talk" (none does), which is the same wrong object it tested for Chapter 11 (W18). The right object is the locks, and the Interview records name the tree-line talk (seven files) as the home of content the author chose between options. For Q79 (Shade predicts, marked as prediction, before Pathwell arrives) and Q82 (Shade's "holding onto" reading of Pathwell and Elizabeth) the author picked an option that rejected exactly what the book now does (D: "no advance discussion"; D: "cut the assessment"). Elizabeth's "I'm going to be there when he decides" (C1 §6, "Preserve the existing Chapter 12 principle") is in no chapter, and triage row 14.5 saw its absence and closed it too. None of this was put to the author, against W8. The chapter structure should stay; the decision should be logged as W19 and listed for him; and the two orphaned contents need either a home or a recorded cut. The child is Milo, a boy: GREEN, because the author has been asked (R32, "idk") and the cost of a swap is lower than the record says; but the triage's reason is wrong and should be replaced.

Paths are under /home/claude/pathwell/Story unless given in full. Ch = Chapters/Chapter_NN.txt as it is today (Ch13 = working tree). Interview files by short name: AUD = MANUSCRIPT_RECONCILIATION_AUDIT_2026-08-23.md; C1 = ..._REFINEMENTS_CONTINUED_2026-08-23.md (the unnumbered file); C2 = ..._CONTINUED_2_2026-08-23.md; C15, C20-C26, C56 = the numbered CONTINUED files; B823 = BIBLE_DECISIONS_2026-08-23.md. Matrix = Story_Files/PATHWELL_MAPS_L_CHAPTER_CONTRACT_MATRIX_2026-08-28.md. Timeline = Revision/Decision-Timeline.md. "Old Ch12" = `git show 765b69b:Story/Chapters/Chapter_12.txt` (2026-08-26, before the 08-28 rebuild). I edited no repo file and drafted no prose (Pipeline, "tenth seat": it never drafts prose); where a fix needs a line, I say what the line must do.

On the trigger. This is Pipeline D21 trigger 2 ("nothing to fix" in a triage). The strict MAPS reading does not fire, because the audit did argue the other side: audit_ch13-15.md row 13.1 ("missing", medium confidence) and verification.md row 11 ("holds": "place it at the end of Ch12 or in Ch13"). What was missing was anyone arguing for the audit's side after the triage disagreed with it, and any route to the author (triage.md:11: "27 FIX, 87 KEEP, 0 AUTHOR"; KEEP is defined as "differs only from an interview staging or line lock, and the text works", triage.md:8, so a lock deviation the reviser wants to keep has no AUTHOR route). Base rate: four earlier KEEPs over locks have each been put to the author after a tenth seat: Ch4 (R32/Q-M), Ch6 (W15), Ch8 (W16), Ch11 (W18).

---

# Minority report: the Chapter 13 verdict

## The consensus, stated so it could be proven wrong

Chapter 13 owes nothing to the locks. Specifically: (1) it may have no scene before Ch14 in which Shade explains his refusal, because Ch14's "Do I remain myself?" gives the reason when it matters and "nothing later cites an earlier talk" (triage.md:184); (2) the Camp child may be a boy, Milo, against the older lock's "girl" (triage.md:185); (3) so the chapter "needs nothing" and no AUTHOR item arises (triage.md:221).

## Assumptions the verdict rests on

1. **A1.** "Does a later chapter cite an earlier talk?" is the right test of whether a talk is owed.
2. **A2.** The tree-line talk is staging, so R23 ("the interview's scene-level staging is guidance, not law", Decisions.md:47) releases all of it.
3. **A3.** Ch14 carries what the talk was locked to carry.
4. **A4.** The locks attached to the talk are one thing, a scene, and are released together.
5. **A5.** Ch13 works without the talk, for readers.
6. **A6.** W14's own warnings (Shade not "explaining full metaphysics", matrix:603; Shade's want "unrelated to explaining himself", matrix:581) exclude it.
7. **A7 (13.2).** Only a gender word differs from the lock, and R32 settled the author's side.

**Weakest: A1, with A4 behind it.** A1 is a test of later chapters. The Chapter 11 seat found that the dependents of a dropped beat are locks, not chapters (Tenth-Seat/2026-10-05_Ch11-decisions.md, H1 assumption 2), and it is the same here. The talk's content is cited by the Interview records in the table below and by no chapter. A chapter cannot cite a scene that the same 08-28 rebuild removed (Archive/Reconciliation-2026-08/..._LOG_CONTINUED_07:17: "The stale tree-line/confrontation material formerly attached to the chapter has been removed from current manuscript continuity"). The check could not have come out any other way. A4 fails on inspection: the records are four different kinds of thing (an option the author rejected, a line to preserve, a conditional on wording, a rationale for a different lock).

## Item 13.1: no talk where Shade explains his refusal before Ch14

### What the old scene was and what happened to it

Old Ch12 (765b69b), lines 46-102, is one scene at the tree line. Shade says "He'll be here by morning" (:48), "He's going to try to cut me loose" (:54), "It kills me" (:58), "I'm telling you because he won't tell you" (:64). Elizabeth: "I'm not going to tell him what to do. But I'm going to be there when he decides." (:82) and "Then I'll stand there until he has to notice." (:90). Shade, last: "You're not what he described" / "Something he was holding onto." (:94-98). Commit 4a1d69c (2026-08-28, "Rebuild Chapter 12 for W13") replaced all of it. Nothing in the repository records the author agreeing to that. The log's own wording is a deferral: "any useful ideas can be mined later only if they do not turn W14 into a funeral rehearsal" (LOG_CONTINUED_08:19). It was never mined. The matrix, written the same day, mentions the tree line only as a timing marker (matrix:553, "before the tree-line/confrontation material"). The tree-line scene is not in W14's contract at all. That is where the locks and the plan came apart, and no record notes it.

The old text was AI text, not the author's (his docx stops at Ch10, Decisions.md W14; the scene is in session_progress.md as added "tree-line friction"). Its content, though, was repeatedly reviewed by the author and locked in pieces.

### What the locks and rulings actually say

| Record | What it says | Who chose | In the book now |
| --- | --- | --- | --- |
| Q79, C20:47-56 (Timeline:454-457) | LOCKED C+A HYBRID. The draw gives "bodily pressure and the supported certainty that Pathwell is coming"; Shade predicts reintegration, marked as prediction ("I think", "he'll probably"). "This preserves the tree-line conversation as the place where Shade can explain why loss of independent self is existentially unacceptable." Option D, "Remove all advance discussion", was rejected (Timeline:454; C20:39 gives D's own flaw: "slowing the climax with exposition that the tree-line scene can carry more naturally"). | The author picked a hybrid of the audit's options; he did not accept the audit's lean (A). | **Option D is what the book does.** Ch13:434-438 has only "Stronger." / "Closer?" / "Probably." Nobody says Pathwell will try to put Shade back until Shade names the frame in Ch14:485. The lock's constraint (no telepathy, no plan from the draw) is met, more strictly than before. Its content is not. |
| C1, "Shade predicts Pathwell's pattern" (C1:30-43) | "Pathwell will come, and Pathwell will try to fix him/control the problem." "Shade can nevertheless make a strong prediction." | Locked | Permissive ("can"). Not in Ch13. |
| C2 §11 (C2:130-140) | LOCKED D: "technical uncertainty and existential certainty"; "whatever it is, it isn't me". "Exact wording is not yet a manuscript lock." | The author | **Met, compressed, in Ch14:595-635** ("I don't know exactly." / "Do I remain myself?" / "Can." / "Not will." / "I am the person living with it. No." at :663). |
| Q82, C22:9-17 (C21:71-75; C2:142-153; Timeline:462-463) | LOCKED A: "Preserve Shade's underlying judgment that Pathwell behaves as though Elizabeth is someone he can hold onto, manage, or determine for," grounded in the museum slip "you took her from me". Rejected D ("cut the entire `holding onto` assessment"). | The author chose A over D | **Cut: option D again.** `grep -i "hold onto\|holding onto"` over Chapters finds nothing about it in Ch1-18. Ch11:47-49 (restored in P36) plants the evidence, and no scene collects it. The Ledger has no row for it (the Ch11 seat asked for one: Ch11-decisions H1 condition b). |
| C1 §6, witness (C1:71-80; Timeline:347) | "**Preserve the existing Chapter 12 principle:** `I'm not going to tell him what to do. But I'm going to be there when he decides.`" | Locked | **Absent from Ch1-18** (grep: no hit; audit_ch13-15 row 14.5 says the same). Triage 14.5 saw it ("The lock's 'I'll be there when he decides' is absent, so no payoff is broken", triage.md:190). That is the same wrong test again, and 13.1 closed the only earlier place it could go. Decisions.md:94 meanwhile lists this lock under "locks the manuscript follows" ("Ch14 ('Let it fail.')"), so the record says it is met. |
| Q86, C26:9-18 | "Replace the categorical `I'm telling you because he won't tell you.`" Shade is uncertain whether Pathwell will tell her before he acts. | Locked | Conditional on Shade warning her. If no warning scene, nothing to word. Moot with 13.1a. |
| Q119, C56:20-32 | Author chose D (Shade has no treatment role). The lock text: "Shade's important relationship material with Elizabeth remains in the diner, museum aftermath, **tree-line conversation**, resistance to the draw, refusal of reintegration, and climax." | The author | The relationship material is in Ch13 (coffee, Hearts, "Pockets", the easy Elizabeth/Shade register). The tree-line conversation is not. So the author traded the shoulder scene on a stated rationale that includes a scene that no longer exists. Partly met. |
| AUD:375, :385 | "Shade's objection should prepare his later explicit refusal." Keep "Tree-line atmosphere"; keep "Elizabeth refusing to become the person who decides Shade's fate for him." | The AI audit (08-23); lower weight | Elizabeth never decides for him (Ch13:444-462, Mama Baga asks). The "prepare" part is in Ch14 in the moment, not before. The atmosphere survives only as the phrase "not toward the tree line" at Ch13:361, which has no antecedent on the page. |
| C23:35 | The letter-echo "may become subtext for the tree-line conversation" | Locked | Dead: the letter treatment was superseded by Q119 (C57). |
| C24:31, C25:12 | The donation comes "before Elizabeth seeks Shade out for the tree-line conversation." | Locked | Order constraint, met (Ch12:330-425 then Ch13). |
| C15:24 | Shade "may state simply, in the spirit of `He's coming.`" | Locked B | Optional. Ch13 never has him say it. |
| Matrix:591 (W14 exit state) | "Shade has explicitly or implicitly clarified he does not consent to reintegration; ... Pathwell's arrival becomes threatening because the reader now knows what could be erased." | The AI contract (08-28, derived) | See Item 3. |

So the verdict "the tree-line talk is not missed" is true as a reader-experience claim, and not true as a record claim. What the locks left in that scene was (a) an advance prediction the author chose to keep over cutting it, (b) a judgment of Elizabeth's place with Pathwell that the author chose to keep over cutting it, (c) a line of Elizabeth's that the author asked to be preserved, (d) a place that the author's choice on a different question was explained by. R23 releases staging. It does not obviously release (b) and (c), which are content with a "Preserve" directive, and which the 08-28 rebuild dropped without a record, which is the Chapter 11 pattern.

### The strongest alternative

Not "restore the tree-line scene". A capable reader of the record would defend this: **Chapter 13 stands as a chapter, and no scene is added to it. What changes is the record and two orphans.** (i) The triage's "needs nothing" is replaced by a working decision, W19, in the W16/W18 shape: Chapter 13 keeps the August 28 staging (no advance talk) over Q79, the placement of C2 §11, Q82, C1 §6 and the AUD directive; the lock rows stand until the author answers; it is listed for him under R36. (ii) The Q82 judgment and the witness line are each given a home or a recorded cut, because they are "existing text, preferred over new material" by R23's own rule, and both are lines the author asked to be kept. (iii) If a minimum is wanted in Ch13 itself, it is the smallest unit that meets Q79 and the W14 exit clause: one prediction by Shade, marked as prediction and without method, at the beat where Mama Baga asks "You want to leave?" (Ch13:444-462) or just before it. That is a few lines, not a scene.

### Evidence that should exist if the alternative is true, and whether it does

| Prediction | Found? |
| --- | --- |
| The content was in the manuscript and was removed by the 08-28 rebuild. | Yes. Old Ch12:46-102; 4a1d69c; LOG_07:17. |
| No record shows the author agreeing to the removal. | Yes. Searched Decisions.md R1-R36 and W1-W18, Pass-Log, Plan; "tree line" appears in no ruling. |
| The author rejected, in a lock, the option the book now embodies. | Yes, twice: Q79 D and Q82 D (Timeline:454, :463). |
| Locks cite the scene as the home of content. | Yes (table above). |
| Something downstream in the book is left unpaid. | Yes, partly: Ch11:47-49 (the plant for Q82) has no collection; "I'll be there when he decides" has no source; Ch14:485's "rejoining frame" is the first time any character names the plan (Cold-Read:539 calls it a "great reveal"; the lock set wanted Shade to have said, earlier, that he expected to be put back). |
| Ch14's refusal reads as unprepared to a blind reader. | **No.** See below. |
| A later chapter refers back to a talk. | **No.** |
| Ch14's first third shows the lack of a named threat. | Partly. Ch14:91-263 is banter while Pathwell lays out the pins, and the blind reader's attention "dipped until Shade said 'That's not diagnostic'" (Cold-Read:536). The same reader calls the misdirection "structurally clever", so this is a cost of the surprise structure, not a plain defect. |

### Evidence against the alternative (what holds the verdict up)

- **The blind reader found the refusal strong without the talk.** Cold-Read:540-541: "Do I remain myself?" ... "Then no." "This is the strongest dialogue in the book. Shade refuses without any struggle, which is exactly his character." And "I am the person living with it. Direct and earned." That is the reader's report on the very point the audit said was "the first time the reader hears the basis for his refusal, with nothing prepared" (audit_ch13-15.md row 13.1). The audit's "medium" confidence was right to be medium.
- **The reader predicted the conflict from what Ch13 gives.** Cold-Read:507: "Shade's newly won choice ('I want to stay here') will be tested against Pathwell's instinct to fix or contain him." The reader did not feel a gap, and had also learned in Ch11 that Pathwell tries to "separate" the problem (Ch11:347 "I am separating the problem").
- **Ch13 is where the book sags, and an added conversation adds weight to the sag.** Cold-Read:494: "the third calm Camp chapter out of the last two ... the point landed early ... I was waiting for Pathwell to arrive"; the drags it names are the coffee section and the second and third Hearts sections (Assessment-2026-09-29.md:136; Plan row 13).
- **The later book is built on the lived-life version, and nothing depends on a talk.** Elizabeth's last look at the empty ground is a list of Ch13: "the coffee. The green jacket. Milo saying he was cheating. Shade saying he did not know yet what else he liked. That hand was promising." (Ch15:1114-1122). Ch16:546-554 ("GREEN JACKET, CAMP ISSUE", "LIKED POCKETS."), Ch16:1060-1068 (the coffee) and Ch16:1116-1128 ("He chose to stay here. He played cards. He made bad coffee. He died." / "Person is the word I have for that.") all rest on Ch13. Mama Baga's answer to "Was he a person?" starts "He said no when somebody tried to decide what happened to him" (Ch16:1120), which is Ch14.
- **The author's own pillar list puts Shade's no at the fire.** Non-Negotiable-Scenes.md pillar 7 ("Shade says no"); the tree-line talk is not a pillar. The matrix puts the "explicit refusal" at W15 (matrix:853), not W14. The author-intent note lists "refusal of reintegration" as its own required protection beside "ordinary preferences", "Camp relationships", "humor", "a future expectation" (Archive/Experiments-2026-09/PATHWELL_CURRENT_AUTHOR_INTENT_SHADE_CONSEQUENCE_NOTES_2026-09-18.md:138-160). Ch13 supplies "a future expectation" ("Cards later?" / "Yes.", Ch13:408-410; "Again?" / "Yes.", :282-284).
- **W14's own warning is real.** The contract and the log both say the chapter fails "if every beat foreshadows death" (matrix:601) and that the old tree-line talk "primarily discussed Shade's expected death" (LOG_08:19). A talk that makes the reader brace is a risk to the chapter's single purpose. (The lock does not ask for a death talk. Q79 asks for the reason a loss of self is unacceptable, and C2 §11 forbids certainty about what happens. That is a smaller thing than what the 08-28 log was avoiding. The log may have judged the old scene, not the lock.)
- **The reveal.** Ch14's structure (Pathwell builds under cover of fidgeting, Elizabeth "understood that only later", Ch14:255-263; Shade names the frame from the brass, :477-485) depends on the reader not yet having heard "he'll try to put me back". An advance prediction pre-spends some of that. It would not pre-spend the method (the lock bars Shade from knowing the working: C20:54), so what is lost is surprise about the *intent* and what is gained is dread about it. That is a real trade and not mine to settle.
- **R23, R33, R34, R36.** The author told the revision to judge staging on "what works for the story" (R23) and to "go with your leans" (R33, R34, R36, Decisions.md:47, :57-60). R36 changes the cost of the conditions below: a lean needs no stop, only a listing for him.
- **JUN 16, "A+B feels right"** (Timeline:48; Archive/Notes-2026-06-to-08/Story_logic_test.md:2206): Elizabeth is "with the child" when Pathwell walks into Camp. Ch13 and Ch14:17-19 do exactly that. The author's own wish is met by the very text the triage kept.

### What the weighing comes to

The structure is probably right. Reasons to keep it are the blind read, the dependents and the reveal, and they are better than the triage gave. The record is wrong in three ways: it names the wrong test, it says "needs nothing" over two locked items the author chose to keep, and it sends nothing to the author. Two items have no home: Q82's judgment and the witness line. Q79's prediction is a real choice with a real cost on both sides, and only the author can say which he wants.

### Cost if wrong

- **If "needs nothing" stays recorded and the author wanted the content:** the Ch14 and Ch15 passes each treat Q79, Q82 and C1 §6 as satisfied. Ch11's plant for Q82 stays unpaid with no ledger row. The witness line is lost with both of its homes closed (13.1 and 14.5). Putting it back later means reopening Ch13 after Ch14 has been revised around the absence. The lines that lean on Ch13 being plain are Ch14:257 ("Elizabeth understood that only later."), :513 ("Tell me he's wrong."), :601 and the reveal at :485; they would need rechecking. That is the Chapter 11 shape.
- **If it is logged and he says "keep the book as written":** a W-row and a ledger note. Nothing else.
- **If the minimum is added and he did not want it:** a few lines (Ch13 is 2,209 words; the drags the readers named, the coffee and the Hearts middle, are about 260 and 350 words); the old text is in git.
- **If the minimum is added and it spoils the reveal at Ch14:485:** the fresh check on the revised pair would show it before it ships (see below).

### What would disprove the alternative

- The author says the refusal first heard at the fire is what he wants, and drops Q79's advance prediction, Q82 and the witness line, or moves them to Ch14. Then 13.1 closes as a keep with his name on it.
- A fresh cold reader reads Ch13 then Ch14 with a candidate prediction added and reports the reveal at Ch14:485 as pre-spent, or reads it without and reports a gap at "Do I remain myself?". The first kills the "add the minimum" option; the second kills the "keep as written" option. This test is cheap, and nobody has run it, because the reader has only seen the version without the line.
- Someone finds an author statement, not in the Interview files I searched, that rejects the tree-line material. I did not find one. The material searched: Interview/ (all 73 files, by grep for tree line, treeline and tree-line: nine hit; seven are about the scene, two about geography), Decisions.md, Decision-Timeline.md, Plan.md, Pass-Log.md, Promise-Ledger.md, the Story_logic_test.md turns on Ch12, the 08-28 logs, Non-Negotiable-Scenes.md.

### Verdict on 13.1: ORANGE, as recorded

The evidence cannot tell whether the author still wants the talk's content in Ch13, and the record says it can. Narrow the claim to what is proven ("Ch13 as a chapter works; three locked contents have no home") and move to YELLOW when these hold:

- **(a) Log it.** A working-decision row (W19), same shape as W16 and W18: "Chapter 13 keeps no advance talk before the fire, over Q79 (C20), Q82 (C22), C1 §6 (witness), the AUD directive (:375) and Q119's rationale; put to the author under W8; the lock rows stand until he answers." It names what it costs to reverse (below). Rewrite triage.md:184's reason ("Nothing later cites an earlier talk") and :221, which tested later chapters, not the locks. Replace "It needs nothing" with "It needs no change to its scenes; three locked contents are unplaced (W19)."
- **(b) Give Q82 and the witness line each an owner.** Either a home (a line in Ch13, or the Ch14 pass, and say which) or an explicit cut that is listed for him. Add Promise-Ledger rows: "Shade's reading of how Pathwell holds Elizabeth (Q82): planted Ch11:47-49; unpaid" and "Elizabeth: 'I'm going to be there when he decides' (C1 §6): no source in Ch1-18." Do not let the Ch14 pass close 14.5 on "no payoff is broken".
- **(c) Decide Q79 by test, not by argument.** Under R36 the reviser takes a lean. Mine: try the minimum (one Shade line, marked as prediction, no method, no metaphysics, placed at or just before Ch13:444 and paid for by cutting from the drags the cold reader named) and run the fresh check on Ch13 and Ch14 together. A prediction and a statement of refusal are character-defining dialogue and philosophical statement, the categories the reviser is cautious with (Craft.md:192-193): the line goes in plain, is flagged, and is listed for the author with an alternative or two. If the reveal reads as pre-spent, cut it and log the cut. Keep it either way as an item for him. A lean to keep the chapter as it is is also acceptable, if it is logged under (a).
- **(d) The record carries the reversal price.** If the author wants the full talk: it lives in Ch13 or at the end of Ch12 (C24:31 fixes only that the donation comes first; both slots follow it), about 12-20 lines, and Ch14:257, :485, :513 and :595-635 get rechecked so that "What happens to me?" does not repeat what Shade has already said. A minimum of one marked prediction costs two of those lines (:257, :513) at most.

### What only the author can settle (13.1)

1. Did he want Shade to say, before the fire and as a prediction, that Pathwell will try to put him back, and why that is not an acceptable outcome? Or does the first hearing at the fire serve? The book is currently the rejected option D of Q79. The cost is surprise at Ch14:485 against dread built beforehand.
2. Does he want Shade's "holding onto" reading of Pathwell and Elizabeth said at all (Ch11 now plants the evidence), and where? He chose to keep it over cutting it (Q82).
3. Does he want Elizabeth to say, before the fire, "I'm not going to tell him what to do. But I'm going to be there when he decides"? Or do her actions at Ch14:645-653 carry it?
4. Is "I want to stay here" enough for him as the implicit refusal the contract asks for, or does the refusal need to be named before Ch14?

---

## Item 13.2: the child is a boy, Milo, against "girl"

### Claim

The Camp child may be Milo, a boy, in every chapter, against C2 §4's "the girl" and the author's JUN 16 "keep it the existing girl" (triage.md:185: "The 'girl' belonged to a discarded draft").

### Assumptions

1. The lock's content is the identity of the child (runner, archive, climax), not a word. 2. Nothing the author wrote requires a girl. 3. The author has been asked. 4. A swap costs paid-off beats.

**Weakest: 4**, and in the opposite direction from the usual. The record overstates the cost. A close second is 2.

### Strongest alternative

The author wrote the child as a girl twice, in his own words (JUN 16) and in the lock (C2:40-42, "The girl sent to fetch the healing record ... [is] the same understated Camp child"), and "idk" (R32) is an abstention, not a ruling. A reviser who reads an abstention as consent has used R23 to override an explicit author choice. The 08-28 rewrite introduced both the boy and the name "Milo" (no Interview file contains the word "Milo": grep), so the gender in the book is the AI's, not the author's, and the triage's own reason for dismissing the girl ("a discarded draft") is wrong: she is the girl from his own Chapter 4 draft who leads Elizabeth in (Decisions.md:159 Q-M; Tenth-Seat/2026-10-03_Ch4-cuts.md:28-31).

### Evidence for the alternative

- JUN 16 (Timeline:50; Story_logic_test.md:2242): "yeah that works, keep it the existing girl." The approved idea there is a bookend: the child who leads her in is the child she runs to.
- C2 §4 (C2:40-42): "The girl".
- Triage.md:185 gives a factually wrong reason.

### Evidence against

- **The author has been asked.** R32 (Decisions.md:56): "idk". "Milo stays (R23: keep what works for what we have), and the question stays open in case the author decides." Q-M (Decisions.md:159) is still listed as open, default Milo. W8's duty ("put to him, not assumed") was met, after the triage, through the Ch4 seat.
- **The lock's identity requirement is met.** Same child, runner, archive, climax: Ch4:69 (turnips, sock), :377-406 (carries the cookbook, brings Elizabeth to the archive), Ch12:13 and :234 (bucket, sock) and :425 (the folded note, archive doorway), Ch13:78-228 (named, Hearts), Ch14:497-507 (sent to the archive, sock falling), Ch15 (rescued). C2:40-42's "no special bond, destiny, or supporting-character arc is required" is not violated: it says not required, not forbidden.
- **The approved bookend survives with a boy.** In Ch4 the boy leads her to the archive (Ch4:377-406); in Ch15 she runs in for him. That is JUN 16's "same inversion structure" (Story_logic_test.md:2243-2250), whatever the pronoun.
- **A is not contradicted by the text anywhere.** Ch13 never says "boy" against a "girl" lock in a way that would be a defect; the gender word is uniform (grep: "girl" in Ch4, 12-17 gives no child).
- **Cost of a swap is low, not high.** The record says "Swapping to a girl rewrites paid beats" (Ch4 seat, :37, :44), and that is not so. What is paid is the sock, the name's first use, the card game and "You still owe me a hand". None depends on gender. A swap is a rename and pronouns: "Milo" 110 times in Ch13-17 (22, 15, 26, 30, 17), "boy" 18 in Ch4, 4 in Ch12 and 10 in Ch13, "turnip boy" in Ch12. The name "Milo" is unlocked, so the author would also choose a name. It is mechanical, and the checker finds every one.

### Cost if wrong

If the author wanted the girl: a mechanical swap, about 180 spots, one pass, no re-staging. If the record keeps the wrong reason: a later reader of the triage thinks the girl was a mistake of the old draft, and Q-M slips out of the report to the author. That second one is the real risk.

### Verdict: GREEN, with two conditions

- **(a) Replace the reason.** triage.md:185 and :221 say the girl "belonged to a discarded draft". Point to R32 and Q-M instead.
- **(b) Keep Q-M open, and do not call it settled.** R32 is "idk". Keep it in the author's list, with the swap cost stated as above ("mechanical rename and pronouns, about 180 spots, no payoff depends on the gender").

One more observation, not a condition. C2 §4 also asks for an "understated" child. Ch13 gives Milo more weight than any other Camp character (22 "Milo" and 10 "boy", against 11 for Mama Baga and 12 for the archivist; a rival, a running payoff), and the blind reader braced because of it ("a named child at a card table right before a threshold opens is a classic setup", Cold-Read:511). The author's JUN 16 "A" wants the child with Elizabeth at Pathwell's arrival, so the presence is his; the telegraphing is a craft cost and not a lock breach. It could go in the author list as a taste note.

---

## Item 3: what else Ch13 owes for "Shade alive at Camp" (W14 and the locks)

| Requirement | Source | Ch13 | |
| --- | --- | --- | --- |
| Shade has a want unrelated to explaining himself or preparing to die | matrix:581, :599-601 | Coffee, Hearts, the jacket, "Pockets", "I don't know yet" (Ch13:119-185, 247-311, 351-379) | met |
| Value turn: from "Pathwell's consequence" to a person with preferences, habits, humor | matrix:589 | Same. Hearts shift at :278-280 | met |
| Creation-time fragments only; no ongoing memory | matrix:593; C22:15 | "Then I don't remember it" (:169); "I know the rules" / "I don't remember playing" (:210, :234-240) | met |
| Draw: directional compulsion with visible resistance, harder as Pathwell nears; no radar, no ETA | C1:45-56; C15:20-24; Q131/Q149 | Right hand at :27, :288-309, :416-440, :507-521; "Probably." (:438) as inference | met |
| Shade has no healing or treatment role | Q119 | none | met |
| Mama Baga sees him before her "Stop"; Camp neither trusts nor condemns him; she asks and does not decide | matrix:597; Q126; LOG_08 | :3-53, :442-462 ("I didn't ask what would help.") | met |
| Child/runner appears naturally; named through ordinary Camp life | matrix:597; C2:31-48 | :78-104, :188-228, :386-414 | met |
| Elizabeth observes without becoming his ally; shoulder limits persist | matrix:581; Q119 | :216, :327, :422, :485 | met |
| Archive, cookbook, diary stay background | matrix:595 | not shown at all (the archivist at the card table only) | met |
| No Shade-as-healer, no full metaphysics, no "he existed only to die", no sentimental redemption | matrix:603 | none present | met |
| Pleasure and tone: dry humor, not a funeral rehearsal | matrix:599-601 | yes (the cold reader's gripped list, Cold-Read:498-505) | met |
| Loss-memory: the reader remembers him alive | matrix:601 | Ch15:1114-1122; Ch16:546-554, :1116-1128 depend on it | met, strongly |
| **Exit state: "explicitly or implicitly clarified he does not consent to reintegration"; the reader "knows what could be erased"** | matrix:591 | Ch13 never mentions reintegration. "I want to stay here" (:458) is a choice to stay at Camp, not a refusal of absorption. The reader learns what could be erased (a person) but not what is coming | **loose; the "implicitly" carries all of it** |
| Shade says Pathwell is coming (optional) | C15:24 | Not said. Elizabeth's "Closer?" and his "Probably." do it by inference | optional |

I found no contradiction with the end of Ch12 or the start of Ch14. Checked: Ch12:440 to Ch13:3 (still by the fire; "Pathwell still wasn't there"); Ch13:210-244 to Ch14:3-19 (the unfinished Hearts hand, cards at his boots); Ch13:25-67 to Ch14:41-49 (coat, "Too many pockets." / "I changed my mind about those."); Ch13:288-309, :434-438 to Ch14:351-359 ("Stronger."); Ch13:412-414, :527-529 to Ch14:75-79 (the queen of spades, "Evidence is inconclusive."). Today's line pass cut glosses and merged short paragraphs (Chapter_13_before.txt against the working tree). It cut nothing a lock names. It did cut "That made him smile, and it wasn't Pathwell's smile." and "he didn't fill the silence" (the fourth and fifth statements of the Pathwell/Shade contrast: Cold-Read:516, Assessment:135), so W14's value turn leans on "You look like Pathwell. / But you don't talk as much." (:98-102) and the coat (:3-35).

Small, not a lock: Shade's palm was cut and bandaged at Camp (Ch11:429, Ch12:185-197, :256); in Ch13, a chapter about his hands, the bandage is never mentioned, and which hand holds the cards is unstated. (The Ch12 reader asked the same, Reader-Reports/2026-10-05_Ch12_reader.md, neutral question 4.)

**Verdict: YELLOW.** Everything but the exit-state clause is met, and met well. The clause is the same fact as 13.1c: nothing in Ch13 touches reintegration. If the author keeps the chapter silent, the contract's wording should say "implicitly: by choosing to stay" so a later pass does not read the clause as met by something that is not on the page.

---

## Overall verdict and where it leaves the record

**ORANGE** for "Chapter 13 needs nothing". The chapter may well be right, and the case for keeping its structure is better than the triage made. The record cannot say "needs nothing", because (1) the test it used cannot find what is owed, (2) two locked items the author chose to keep over cutting have no home in the book, (3) one line he asked to preserve is in no chapter, (4) nothing went to the author, and (5) an earlier version of the same verdict on Chapter 11 turned out to have dropped locked lines.

Verdicts by item:
- 13.1: ORANGE (13.1a, no advance scene: YELLOW; Q82 judgment and the witness line: ORANGE, and RED as to the record if the author confirms he still wants them).
- 13.2: GREEN, with a replaced reason and Q-M kept open.
- W14 duties: YELLOW (exit-state clause loose).

## Reopening indicators

- The author answers any of 1-4 above with "I wanted that".
- Someone writes Shade's or Elizabeth's pre-fire lines and finds Ch14:485 reads as pre-spent.
- A reader of the revised Ch13 and Ch14 asks where Shade got "I know the shape" and why nobody in Camp has said what Pathwell is coming to do.
- The Ch14 pass closes row 14.5 on the triage's reasoning, without the witness line having a home.
- The author picks the girl.

## What I could not do

I had no author access and ran no cold read of Ch13 and Ch14 with candidate lines. I did not draft prose. The evidence I weight least is the blind read (Cold-Read-2026-09-29), which was of the 08-28 text with five more lines in it than today's; it is the only blind read of the pair.

## Appendix: the old scene's content, for the record

(765b69b:Story/Chapters/Chapter_12.txt, lines 46-102, removed by 4a1d69c.) Shade at the tree line: "He did not seem haunted so much as accompanied." (:46); "He'll be here by morning." (:48); "He's going to try to cut me loose. ... He thinks that solves the problem." (:54); "It kills me. ... What's left of me, anyway." (:58); "From him deciding I wasn't going to happen. ... Decides ahead of time, so he doesn't have to watch it happen the slow way." (:62); "I'm not telling you to stop him. I'm telling you because he won't tell you." (:64) / "That's not the same thing as warning me." (:66); Elizabeth: "I'm not going to tell him what to do. But I'm going to be there when he decides." (:82); "Then I'll stand there until he has to notice." (:90); Shade: "You're not what he described." / "Something he was holding onto. You're not that." (:94-98). Locks overwrote "cut me loose" (Q79), "It kills me" (C2 §11), "he won't tell you" (Q86), "described" (Q82), and preserved the witness line and the "holding onto" idea (C1 §6, Q82).

## Note on the earlier seat's report (same day)

A first tenth seat ran at 10:19 on the Chapter 13 *decisions* (K1-K5, before drafting). Its report is preserved unchanged at scratchpad/ch13/tenth_seat_decisions_K1-K5_1019.md; this file replaced the name `tenth_seat.md`, and nothing was lost. I read it only after I had written the findings above, so the agreement is independent. It reached the same place on the facts: the triage's reason tests the wrong object; the locks home the content in the tree-line scene (Q79, Q82, Q86, C1 §6, C2 §11, Q119c); Q82's evidence was just planted in Ch11; the witness line is in no chapter; the structure holds; and the record must be logged as W19 and put to the author. Differences, so a reader can weigh them. (1) It says the home is the end of Ch12, because C24 puts the donation before Elizabeth "seeks Shade out"; I read C24 as fixing order only, so Ch13 is as good a slot as the end of Ch12, and I leave placement open. (2) It treats Ch14:257 and :513 as the price of one marked prediction; I agree and added them to the cost. (3) It also tests the line-pass decisions K2-K5 (Hearts, B7, the opening); I did not, except to read the diff for lock damage (none). (4) It does not treat 13.2 or the W14 duties; Items 13.2 and 3 above are new. (5) Its verdicts, YELLOW for the lean and ORANGE for the triage's row as recorded, match mine for 13.1.

---

## Appendix: the decisions as written


Repo: /home/claude/pathwell. Chapter: Story/Chapters/Chapter_13.txt (2,520 words; the August text, not the author's; his working draft stops at the museum). Records: Plan row 13 ("tighten the middle vignettes; keep the Hearts shift" / "a varied opening" / "Shade's procedural jokes (B7)"); Assessment-2026-09-29 C ("The point lands with the green jacket; the coffee, three Hearts sections and the onions then make it again. The only pulse is the hand. Tighten the middle vignettes so each one changes something"); triage rows 13.1–13.2 and "Chapter 13. It needs nothing."

## K1. No tree-line conversation (the triage's KEEP 13.1)

The locks keep a "tree-line conversation" in this stretch (Q79, Continued 20 and 21, LOCKED C+A HYBRID; C15 LOCKED B; also C2 §11). Shade, at the edge of Camp, predicts from the draw's pressure and his own knowledge of Pathwell that Pathwell is coming and will try to reintegrate him ("I think", "he'll probably"). He explains why losing an independent self is existentially unacceptable, even though no one knows what it would mechanically leave. The 08-28 text dropped it. The triage kept it out: Ch13 shows a self worth keeping, and Ch14's "You are going to use the existing connection as the return line…" / "What happens to me?" / "Do I remain myself?" / "Can." / "Not will." / "Then no." gives the prediction and the reason when they matter. Restoring it would pre-spend Ch14.

Lean: keep the triage (no tree-line talk) and log it as a W-row put to the author under W8, as W16 and W18 were. This is the tenth seat's trigger 2 (a lock-level KEEP sent nothing to the author).

## K2. Tighten the middle so each vignette changes something

Keep each vignette, but cut its repetition:

- **The jacket.** The point lands here. Line pass only.
- **The coffee.** It changes something: Shade learns the Space Between memory isn't his ("Then I don't remember it."). Keep it; trim the commentary.
- **Hearts 1.** It changes something: Milo's name, and "I know the rules." / "I don't remember playing." / "Then today you play." Cut the second queen-of-spades trap (the same joke twice) and keep one.
- **Hearts 2.** The Hearts shift (Plan: keep): he stops playing from remembered rules and plays the people. The draw opens his hand in front of Milo ("Does that hurt?" / "Something is pulling."). Keep it; trim the list.
- **The queen and "Pockets".** He names what he likes. Keep it; cut the procedural-joke run around it.
- **The onions.** The draw gets stronger, and Mama Baga asks "You want to leave?" / "I want to stay here." / "Then stay." / "People keep doing that." / "Asking." This is the chapter's choice. Keep it. Cut the potato set-up's "They bounce." / "Good system." and the purple-foot joke. Cut the "chain of custody" queen return, or make it plain.
- **The last hand.** The threshold opens. Keep it.

## K3. A varied opening

Ch12 opens on a personified Camp, and so does Ch13 ("By full morning, Camp Cunnan had decided Shade was neither an emergency nor an explanation."). Ch13 instead opens on the people: Elizabeth by the fire, and Mama Baga pinching Shade's sleeve.

## K4. B7, the shared deadpan

Shade's procedural jokes are cut down, and what's left is his:

- Cut: "Laughing seems medically irresponsible.", "This camp communicates like a hostage situation.", "That seems deliberately dangerous.", "Chain of custody has already been compromised.", "That is inconvenient.", "Good system.".
- Kept: "Evidence." / "Corruption.", "I can choose badly.", "Pockets.", "This child is cheating." / "He's just better than you.", "This place is hostile." / "You're still here.".

Milo, the archivist and the older woman keep their own registers: Milo blunt, the archivist dry about records, the woman silent. These are listed for the author.

## K5. Line pass

Narrator commentary cut:
- "Elizabeth was getting better at that distinction."
- "That, apparently, settled it."
- "No philosophy followed."
- "This seemed to make him happier than winning might have."
- "No hesitation."
- "No follow-up inspection. / No suggestion that his judgment outranked hers."
- "That was becoming one of the easiest ways to tell them apart."
- "Not certainty. / Not distance. / An inference from pressure."
- "He was losing the fight with the draw by inches. / He was winning the hand."

Fragments merged. Kept, because Ch14 opens on them: the last hand, the queen face-up beside an onion, "That hand was promising.", and "Then the threshold opened."
