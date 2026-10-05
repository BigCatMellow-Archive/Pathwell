# Tenth seat: the Chapter 11 decisions, 2026-10-05

**Evidence, closed; preserved whatever the verdict (Sunday D21).** These decisions were written before drafting ([appendix](#appendix-the-decisions-as-written)). Verdict: **ORANGE** (H1 as written). How it was answered is in [pass P36](../Pass-Log.md#p36-2026-10-05-chapter-11-the-museum).

---

# Tenth seat: the Chapter 11 decisions, 2026-10-05

tenth_seat: fresh agent (not the reviser)
against: ch11_decisions.md (H1-H6, written before drafting)
head_sha: d685e44 (P35, /home/claude/pathwell; evidence read from the working tree and, where stated, from git history)
independent: true
verdict: ORANGE overall (H1 as written). H1 ORANGE, with 11.5 RED; H2 YELLOW, with the cannon chain and "I hate you both" ORANGE as written; H3 GREEN; H4 YELLOW; H5 GREEN; H6 GREEN with an extended keep list.
summary: The structure of Chapter 11 may well stand, but "Chapter 11 needs nothing" cannot be recorded as settled. Five deviations from the interview locks were kept by a triage that sent nothing to the author (87 KEEP, 0 AUTHOR across 114 findings), against W8. Two of them are not equal. 11.5 (the road-accusation lines) is the weak one: the lines are existing text that the 08-28 rewrite dropped, three later locks name Chapter 11 as their evidence, and the triage's only reason ("no later chapter uses them") tested the wrong object. 11.1 is a lock the author wrote himself (LOCKED USER REFINEMENT). 11.2 and 11.3 hold better than the audit thought, because Ch17:358-366 and Ch14:1097 depend on the kept staging. H4's clock gives Shade hours of waiting that the page ("Drive-too-long tired") and two locks contradict. H2's reassignment of the graffiti speech to Pathwell is defensible and fits a slot already in the chapter, but the cannon, "I hate you both" and the poem each need a condition.

Paths are under /home/claude/pathwell/Story unless given in full. Ch = Chapters/Chapter_NN.txt as it is today. "draft" = the author's working draft, scratchpad/working.txt (cited by line there). Interview files are cited by short name: R0 = MANUSCRIPT_RECONCILIATION_AUDIT_REFINEMENTS_2026-08-23.md; C2, C3, C10, C11, C12, C13, C21, C22, C41, C66 = the CONTINUED_N files. I did not edit any repo file, and I did not draft prose (Pipeline, "tenth seat": it never drafts prose); where a fix needs a line, I say what the line must do.

On the trigger. The 2026-10-01 audit did articulate the case against Chapter 11 (audit_ch10-12.md:30-38; it named 11.1, 11.2 and 11.5 as "highest-value items for the author" at :66). What had no one arguing for the audit's side was the triage's verdict: Ch11 got 0 FIX and 0 AUTHOR, and the paragraph at Currency-Audit-2026-10-01/triage.md:168 says "Needs nothing." That is Pipeline D21 trigger 2 ("nothing to fix" in a triage), not the strict "no findings" reading of the MAPS playbook. There is also a base rate. Three earlier triage KEEPs over locks, each later put to the author after a tenth seat: Ch4 (Q-M, Decisions.md:158), Ch6 (W15, Q-L) and Ch8 (W16).

---

# Minority report: Chapter 11 decisions

## H1. The structure stays ("Chapter 11 needs nothing")

**Claim, stated so it can be proven wrong.** Chapter 11 may stand as written on five points where it differs from the interview: Shade waits outside by his car and walks in with the group (11.1), the trigger is a draw-stumble and a grab (11.2), "I don't need to be rescued" follows an argument (11.3), there are no road-accusation lines (11.5), and the dagger is not mentioned (11.8, which H1 changes to one line). Each can stand because the text works, nothing later depends on the locked alternatives, and none of it needs logging or a question to the author (triage.md:168; the lean in ch11_decisions.md H1).

**Assumptions.**
1. R23 covers all five. R23 is the author's own words about "the audit's staging findings": "most of this was done by the AI ... evaluate what works for the story overall" (Decisions.md:47).
2. "Nothing later in the book depends on the locked alternatives" (triage.md:168) was tested correctly. The row for 11.5 tested it by grepping Chapters 12-18 for the lines (triage.md:149).
3. The kept staging works for readers.
4. The reasons given in each row are enough. For 11.1 the reason is that Shade hiding inside "would need a way past the locked side door (Pathwell's key)" (triage.md:145).
5. W8 allows the reviser to keep a staging that differs from a lock without asking: "a later record that differs from one is put to him, not assumed" (Decisions.md:138).
6. Keeping five deviations in one chapter does not add up to a different chapter from the one the author locked.

**Weakest: 2, with 5 behind it.**

On 2: the triage tested the wrong object. The dependents of the three lines are not chapters; they are locks. C2 §12 says: "Chapter 11 already supplies the key evidence: Pathwell says `you took her from me`, and Shade answers `She wasn't yours to take from.`" (C2:143-148). C21 repeats it (C21:67). C22 locks it: Shade's "holding onto" judgment comes from "Pathwell's museum control reflex and possessive slip toward `you took her from me`" (C22:9-14). So the grep result ("none in Ch12-18") does not show that nothing depends on the lines. It shows that the dependent beat was lost in the same rewrite. I confirmed that: no chapter contains "hold onto" or "holding onto" (grep, Chapters/), the tree-line exchange C2/C22 describe is not in the current Ch12 or Ch13, and no Revision record says it was dropped. The lock chain is broken at both ends and the triage read the break as proof of independence.

On 5: W8 is not optional, and the triage's own categories had no route for it. KEEP means "differs only from an interview staging or line lock, and the text works"; AUTHOR means "a taste call" (triage.md:7-9). A lock deviation that the reviser wants to keep is neither, so "0 AUTHOR" across 114 findings (triage.md:11) is a result of the definition, not evidence that nothing needed the author.

**Strongest alternative.** Not "rebuild Chapter 11 to the locks". A capable person would defend this: Chapter 11 keeps its structure as a *logged working decision* in the W16 shape, not as "needs nothing". The lock rows stay standing until the author answers. 11.1, 11.2 and 11.3 are put to him with the real reasons for keeping them. 11.5 is restored, because R23's own rule ("existing text and existing canon are preferred over new material", Decisions.md:47) points at it: the lines are existing text.

**Evidence that should exist if the alternative is true, and whether it does.**
- The three lines were in the manuscript before the 08-28 rewrite and were dropped without a record. They were. `git show 765b69b:Story/Chapters/Chapter_11.txt` lines 78-88 have "You're the one who took her from the road." / "Also you took her from me." / "She wasn't yours to take from." (765b69b is 2026-08-26; the rewrite is 7b0136d, 2026-08-28). Audit 11.5 says the W12 log does not record dropping them (audit_ch10-12.md:34).
- Later locks cite Chapter 11 as their evidence. They do (C2:146, C21:67, C22:13).
- The author's own words are involved in the staging, not only the AI's. For 11.1: C10:32-44 is marked "LOCKED USER REFINEMENT". It supersedes an earlier AI framing: Shade "wanders through the dark museum simply to kill time" and "can already be settled somewhere in the shadows rather than standing conspicuously at the threshold" (C10:36-38). C11:35-44 locks the car as warning only ("They know Shade is probably somewhere inside, but they do not know exactly where", C11:41), and C12:9-14 has Shade "appear from the museum shadows". R23 says "most of this was done by the AI". It does not say all, and a USER REFINEMENT is the part that was not.
- A lock's stated *purpose* is not met. Q69 (C13:9-20) exists "to keep Pathwell's museum failure rooted in his control reflex rather than in a reasonable response to an ambiguous attack" (C13:16). Ch11:640 stages the grab as "simple and ugly from Pathwell's side of the room", and Ch11:706 gives him "He grabbed you." The audit notes the 08-28 log chose this on purpose ("a plausible but incorrect protective read", audit_ch10-12.md:31). That is the thing Q69 was written to avoid.
- Internal redundancy from the displaced scene. The lot scene already has Elizabeth tell Shade "So am I" about Camp (Ch11:135-155), then the gallery has Shade ask "You chose Camp?" / "Camp." / "Not him?" (Ch11:500-506). The second exchange partly repeats the first, which is what you would expect if a confrontation the locks put in one place was split across two.

**Evidence against the alternative (what holds the kept structure up).**
- R23 itself, and its use: Decisions.md:47.
- The cold reader: "the best-constructed chapter so far" (Cold-Read-2026-09-29.md:413), and the first "Gripped" item is the sock memory shared "from opposite sides of the glass" (:417). That beat runs with Shade walking the tour with the group (Ch11:308-360), which depends on the lot scene. Restoring Q64r/Q68 literally would move or lose it. (One rescue: Shade is waiting at the Vale case, since he has wandered the building and remembers the socks. That is a re-stage, not a cut.) Assessment-2026-09-29.md:123: "line work only, and protect the destruction sequence entire."
- 11.2 has later dependents. Ch17:358-366 is Elizabeth's witness statement: "She wrote that Shade slipped. She wrote that she told Pathwell she was fine. She wrote that she told him not to use the letter. She wrote that he used it anyway." That rests on Ch11:646-654 ("I'm fine", "He slipped", "No") and the "Put it away" at :682. Ch14:1097 ("That's what you said at the museum.", answering Pathwell's "I can hold it.") rests on "I can contain this." at Ch11:718. The triage said nothing later depends on the *locked alternatives*. True, but the kept staging has dependents, which is the better reason to keep 11.2 and which the triage did not give.
- Elizabeth's "He slipped" (Ch11:650) and her "No" (:654) come before Pathwell acts, so inside the scene his overreach is still plainly his. The lock's purpose is partly met.
- 11.3: Pathwell does move first (Ch11:514-516), and she corrects him ("Stop.", :518). The line comes after "Elizabeth--" (:568) and she is the one stepping between (:560). It is the lock's spirit through a different gesture.
- Restoring 11.5 adds dialogue to a chapter that is already dense, and it needs a place. (Candidates exist: the lot, or the grab at Ch11:640-706. Pathwell saw Elizabeth leave with Shade, because W16 keeps the roadside reveal in front of both brothers, so "left the crash with her" is something he literally saw.)

**What the audit and the triage each got right and wrong, by row.**

| Row | Triage reason | What the evidence says | Item verdict |
| --- | --- | --- | --- |
| 11.1 Shade outside | "would need a way past the locked side door" | Weak. Shade is a practitioner who has had time in the building; nothing says how he got in, and C11:42 only says he "arrived first, wandered to kill time". The real reasons to keep it are the sock beat and R23. Also, the lot gives Shade a stated aim ("Yes. Camp.", Ch11:151) that no lock gives him. C10:44 gives his reason for staying as "his unresolved confrontation with Pathwell plus the draw". It is a motive in a place the locks assign to no one. | ORANGE: put to the author. A real keep, but on different grounds. |
| 11.2 stumble and grab | "keeps Pathwell's overreach his fault" | Partly right (Ch11:650, :654). The lock's own purpose (C13:16) is only partly met, and Ch17:362 now depends on "Shade slipped". | YELLOW: keep, log it, put it to the author, list the dependents. |
| 11.3 argument, not body-block | "staging is incidental" | Fine. Pathwell's movement is on the page and Elizabeth corrects it. | GREEN: keep. |
| 11.5 no accusation lines | "No later chapter uses them" | Wrong test. Existing text, LOCKED B, and three downstream locks. C3 §2 (C3:22-33) is a constraint on where it goes, not a reason to skip it. | RED: restore. |
| 11.8 dagger | deferred to R13/R15 | See below. | YELLOW: neutral line only. |
| 11.4 (not asked) | she permits it | Q69 says she *asks* Shade (C13:12); in the text Shade volunteers ("I need the wall", Ch11:542) and she tells Pathwell "let him open it" (:566). Low. | GREEN, note only. |
| 11.6 (not asked) | the hedge fits a man guided by a pull | C10:20-30 (LOCKED C) says he infers and drives directly. The page has a guess (Ch11:101-111). H4 builds on this. | See H4. |

**The dagger line (11.8).** H1 says "one line" and does not say which. The triage's own example was "she gives it back to Stansbury" (triage.md:152), which would settle the dagger's fate against R15 ("the dagger joins the climax exploration", Decisions.md:39) and against Plan option 3 ("she cuts the draw", Plan.md:80) before the author picks. Plan.md:135 says the dagger's fate "goes with the climax option (3 or 3b); otherwise it's lost on the page at the museum". The only line that costs nothing either way keeps it with her (a physical presence beat, such as when she hits the floor; the shoulder and the case give the natural moment). It must not have her reach for it, because the museum working is a separating working and a reach would read as a miss. The cold reader lost it exactly here (Cold-Read:468).

**Cost if wrong.**
- If "needs nothing" is recorded and 11.5 is wrong: the Q82 beat (Shade's "holding onto" inference, a locked item with no home in Ch12-14 today) has no evidence on the page. Whoever restores it later finds no slip to point at and must reopen Chapter 11 after Ch12-14 have been revised around it. The record also tells later sessions the locks were followed, which is false for five of them (no "kept over" flag for Q64r, C11, Q68, Q69 or C3 §3 exists in Decisions.md, Plan.md or the Pass-Log).
- If 11.1-11.3 are put to the author and he says "keep": a W-row and a note. Nothing else.
- If 11.5 is restored and he disagrees: about six lines, and the old text is in git.
- If 11.1 or 11.2 is reversed later: Ch11 lines 33-185 and 618-730, plus Ch17:362 and the sock beat.

**Verdict: ORANGE as written.** The evidence does not let the claim "needs nothing" be recorded as settled. Narrow it. Move to YELLOW when these hold:
- (a) **Log it.** A working-decision row (W18, same shape as W16): "Chapter 11 keeps the lot scene (11.1), the stumble-and-grab (11.2) and the argument (11.3) over C10 Q64r, C11, C12 Q68 and C13 Q69; put to the author under W8; the lock rows stand." Reword triage.md:168 from "needs nothing". It is not a rebuild order.
- (b) **Restore 11.5 from existing text** unless the author says otherwise: Pathwell's literal accusation of what he saw (Shade left the crash with her), his possessive slip, and Shade's reply (C3:37-42). Constraints: Shade must say nothing right after "I don't need to be rescued" (C3:22-33; Q68 in C12:14-16), so the exchange sits before the wall argument or at the grab and never beside Ch11:570. Shade's reply corrects Pathwell's framing; the narrator does not (Craft.md:176, lesson 7: "An accusation is the speaker's reading of events; let the other character's reply correct it"). Add a Promise-Ledger row: "Shade's 'holding onto' inference (C2 §12, Q82): planted in Ch11 slip; payoff absent from Ch12-14".
- (c) **Dagger: one neutral line**, keeping it with her, no reach, no hand-back.
- (d) **Ledger the dependents** of the kept staging: Ch17:358-366 and Ch14:1097 against Ch11:646-654, :682 and :718, so a later reversal has a known price.
- (e) **If the author keeps the lot scene, keep it on its merits** (the sock beat; Cold-Read:413, :417), not on the side-door reason. If he wants the locks, Shade waiting at the Vale case is the cheapest re-stage I can see, and the lot shrinks to the car and Elizabeth's recognition (C11:35-44).

**Reopening indicators.** The author says he wanted Shade inside, or the body-block; someone writes Shade's "holding onto" beat and finds nothing to cite; a reader asks why Shade stands there with a calm talk before a fight; Ch17:362 is revised and "slipped" no longer matches.

---

## H2. The author's lines brought in (W14)

**Claim.** W14 supports bringing five of his passages into Chapter 11 with the adaptations H2 lists, without touching a lock: (1) the blue-spot parking exchange for the precision-parking joke; (2) his lobby paragraph, which also "settles" Shade's front-door/gift-shop contradiction; (3) his graffiti-house speech, given to Pathwell; (4) "For the record, I hate you both." for "No one commented. / For a while."; (5) his poem beat, inverted: Stansbury looks at the framed poem and goes for the first-aid box.

**Assumptions.**
1. W14 lets whole passages change speaker and scene, not only voice and small lines. W14: "adapted as little as the lock needs, and the change is listed for him" (Decisions.md:134).
2. His passages transplant. They were written for a kidnapping, a lock-picked door, a jump scare and a fight (ch11_decisions.md, top).
3. Each adaptation is the smallest one the new story needs, and each is listed for him.
4. No lock is touched: Q104/Q139 for the poem, R0 §22 for the speech, R0 §23 for the blame in "both".
5. The lines being replaced are the reviser's and nothing leans on them.
6. Each new beat in a cautious category (jokes, character-defining dialogue, narrator commentary) stays plain and flagged (Craft.md:192-193).

**Weakest: 5 for the cannon (it is a five-beat chain and H2 changes one link), and 4 for "both".** For the speech, the weakest assumption is the unstated one that Pathwell can say Shade's want in front of Shade.

**Strongest alternative.** Bring in his *images and rhythm*, not whole passages. Keep the parking exchange as he wrote it, including its last line. Take the lobby paragraph but decide the cannon once, and fix every line that points at it. Fold the speech's content into the wall description and a short Pathwell/Elizabeth exchange, so it is said once. Keep "I hate you both" only if it cannot read as blame on Shade for the injury. Plant the poem earlier or leave it out.

### H2.1 Parking (YELLOW)

For: it is his, and it replaces the joke the fresh check flagged. The "standards" thread survives without it: Ch10:265 ("I am developing standards"), Ch11:25-31 and Ch12:265 ("Stansbury has infected you" calls back to Ch10:265, not to Ch11). A blue-spot scruple is a different kind of Stansbury joke from precision parking. The lot is empty (Ch11:7), so the gag is pure scruple.

Against: H2 does not use his last line. Draft:2072 is "just because we are trying to find a bad guy, doesnt mean we need to be one." H2 has "just because we're in a hurry doesn't mean we need to be jerks." His line is a small piece of dramatic irony for the chapter (the brothers' side is about to be the one that wrecks the building), and it is the chapter's flaw said lightly by the decent brother. The paraphrase loses that. No lock forbids "bad guy"; if the reason is that Shade should not be called one, say so and list the change. Also: the cold reader called the re-parking bit "fun" and flagged the "Pathwell states, Stansbury corrects a number" formula ("Nine.", "Three times.", Cold-Read:414). H2 swaps the part readers liked and leaves the part they called formula. (Minor, unverified: H2 says the fresh check found the car-loss joke four times across Ch8, Ch10 and Ch11. I find it at Ch10:105 and Ch11:25-31 only.)

Conditions: keep his closing line as written unless a lock needs the change; list any change for him.

### H2.2 Lobby and cannon (ORANGE as written)

For: it is his description and it is better than "exactly where Shade remembered it" (Ch11:248-250). "Two brothers split by land and ideology" is a mirror of the book's own brothers, in Elizabeth's noticing.

Against: it changes one link in a chain. The cannon is in Ch11 at:
- :101 (Shade's memory: "pointed at the front door");
- :115-121 (Stansbury: "historically appropriate"; Shade: "It is aimed at the gift shop."; "History has casualties.");
- :248-250 and :252-258 ("I see his point." / "Thank you," / "Traitor");
- :864 (the cannon rolls six inches);
- :974 ("another inch of its journey toward the gift shop");
- :1126 ("The cannon still aimed badly").

If the lobby paragraph says front door and nothing else changes, :101 and :248 now agree, but :119, :252-258 and :974 point at the gift shop and the contradiction has only moved. If the cannon points at the door, the "I see his point" exchange has lost its referent. H2 and H6 list none of these lines. Smaller points: his "sparse glow of sprinkled lights" (draft:2053) has to sit with Ch11:246 ("The lobby lights were off ... a weak gray"); case lights would do it. His lobby was at night and this one is dawn. His "cursed tales of longing, dashing the hope of ever seeing homes night sky again" is not in H2's quoted portion; keep it out, because Ch11:776-784 already says it.

Condition: decide the direction once (front door: his; gift shop: the AI chain). List every line that changes, by number. If his direction wins, the :252-258 exchange is rewritten from "front door", not deleted; the cold reader liked the cannon bit.

### H2.3 The graffiti speech, given to Pathwell (YELLOW)

What the draft does: Shade, not Pathwell, says it, to a kidnapped Elizabeth, while Pathwell hides behind a display and hears "himself" (draft:2074-2078). H2 moves it to Pathwell and rewrites her line.

For the reassignment:
- R0 §22 (R0:278-287) forbids Shade turning Elizabeth into "a witness, proof, or pressure mechanism". A Shade docent speech to her at the wall would be that. R0 §20 (:262) says the wall's meaning is "especially resonant for Elizabeth and Shade", as "payoff, not the logistical excuse".
- The slot is already in the text: "Elizabeth felt it before Pathwell said anything." (Ch11:468), and then he says nothing. Pathwell is already the chapter's docent: "Museums are arguments conducted very slowly." (:290), the key, the donor, Margaret Bell. He is the right mouth for the museum.
- The irony is useful: the man who voices the wall's care is about to destroy three records. Q142 wants the museum shown as human history first (C66:57-68; Cold-Read:413, "the tour was a setup").
- His own notes ask for more graffiti-house description (draft:2077 and :2095).
- Shade's "Not the people. The route." (Ch11:494) becomes an answer to it.
- The content is the lock's theme (R0:262) and the tether for the diary (Ch12:372-376).

Against, and these are the conditions:
1. It says what the narration says. Ch11:474-478: "Hundreds of people insisting, in one form or another, that they had been there." Two tellings of one sad idea (Rules.md "one sad moment, said once"; Craft.md:210, "telling what the scene just showed"; the docent entry, Craft.md:205). One of them goes. H6's cut of "calling the ocean damp" (:452) is a good swap partner: his "Not just a wall" does that job. The narrator lines at :474-478 should be trimmed, not added to.
2. "A wall?" is a knowledge slip. Elizabeth was told "the graffiti wall" (Ch10:586) and says "I came here to go to Camp" (Ch11:562). In the draft she had been taken and did not know. The line has to be about what the wall is, not whether it is one (Craft.md:171, lesson 2).
3. "Without his hearing it" is not true of the staging. Shade walks in with them and is at the gallery entrance (Ch11:240-244, :480-484). If he hears Pathwell voice a want for being remembered, that is new. No lock gives Pathwell that knowledge, and Shade's want on the page is "For him to stop deciding what I am before I get to" (Ch9:312, Ch10:538), which is not the same want. Pathwell learning what Shade wants is Ch14's work ("I heard him." / "That's not the same as listening.", Ch10:542-544). Either Shade is not in earshot, or the page must not show Pathwell understanding him.
4. Naming. "Graffiti house" is in no chapter; the book says "wall" (Ch10:586; Ch11 five times). His "house" was a building, a "hut" (draft:2074). One name (Craft.md:172, lesson 3).
5. A change of speaker is a story change under W14, so it is listed for him as such.

### H2.4 "For the record, I hate you both." (ORANGE as written)

For: it is his line, in his Stansbury's voice, a pressure valve; Sunday Morning asks for somewhere soft to land after a sad moment (Rules.md).

Against:
- "Both" puts fault on Shade. R0 §23 (R0:289-301): the injury is "not random combat collateral and not caused by Shade attacking her". The lock's irony is that the blame is Pathwell's alone. Shade is bleeding from the palm and was thrown into the barrier (Ch11:744, :934-936). In his draft "both" meant two fighters; here it does not.
- "First upright" is stale. Stansbury is already up and has handled Elizabeth (Ch11:886-932). Q139 puts it in order: "still goes to Elizabeth first and then returns to Pathwell" (C66:11).
- Placement. The beat it replaces ("No one commented. / For a while.", :976-978) is the pause before the chapter's moral beat: "You said all right." / "Do you?" (:988-996). A joke aimed at all three men first spends it. Elizabeth is in "pain so bright the room lost its edges" (:896).

Conditions: the line must not read as blame on Shade for the injury, or he approves it as Stansbury's anger at the feud; place it after Shade's "Do you?" so the accusation lands first, or leave the pause; the author decides.

### H2.5 The inverted poem (YELLOW)

What the locks require: Q104 and Q139 remove the healing (C41:45-54; C66:9-21). Stansbury uses "ordinary practical aid", and "the museum poem/history remains intact". They do not require the poem on the page. The ordinary aid is already in the chapter (Ch11:1163-1197). So by W14's own measure ("as little as the lock needs") the minimum is to delete the healing and add nothing.

For: it keeps his lilac image and meets the lock he made himself. Stansbury is the moral anchor of the aftermath ("That is not the same as fixing it.", :1199), and a refusal beside a record he could spend contrasts with Pathwell, who has just spent a letter. H2's own reasoning, with ledger R9: a fourth record spent by Stansbury would undercut the chapter's turn.

Against:
- The restraint is already said, in dialogue: "before you offer your future, your coat, your expertise, or a charmingly illegal replacement scheme: no." (Ch11:1205). A silent look repeats it.
- It only reads if the poem was planted. A reader with no draft sees a man glance at a framed poem. Craft.md:172 (lesson 3): plant it, make it matter before it is lost. H2 does not plant it.
- Q104's own reason: it "avoids repeating the 'other people's records are available if the need is important enough' ethic immediately after Pathwell's failure" (C41:52). A glance dramatizes the temptation of that ethic, even though it refuses. The lock chose absence.
- A fifth soldier-and-home record after buttons, socks, Sam's eggs and soap. Q142 says "a few specific visible losses can establish scale while avoiding catalog prose" (C66:65).
- Survival needs staging. Q144 says the destruction is physical (C66:88-95), so a framed poem hung on a wall far from the toppled cases can survive. But "every loose object in the gallery lurched toward the doorway" (Ch11:816) and the poem is a charged record of the kind the working catches. It must be plainly wall-hung and away from the blast.
- New text in a cautious category. His "perfumed embrace of his wife" (draft:2153) becomes "smell his wife's lilacs" in H2: an adaptation, to be listed with his wording alongside.

Conditions: plant it earlier, wall-hung, away from the cases; one glance, no interior (Q140 gives Stansbury no POV); listed as new text, plain, with his wording beside it. If it cannot be planted without adding a catalog beat, leave it out; the lock does not need it.

**Cost if wrong (H2 as a whole).** Parking and speech: a few lines each, reversible. The cannon: six places in Ch11. "Both": one line, but if it reads as blame on Shade it works against a LOCKED A item (R0 §23) and against Shade's later standing with Stansbury at Camp. The poem: one beat. Nothing in Ch12-18 depends on the cannon, parking, lilacs or the speech (grep: no "cannon" or "lilac" in Ch12-18; "dagger" is not in Ch12-18 either).

**Verdict: YELLOW overall; H2.2 and H2.4 ORANGE as written.** Proceed with the conditions: each adaptation listed for him (R36); the speech said once, in one name, with Shade's hearing settled; the cannon decided and every line listed; "both" fixed or moved; the poem planted or left out.

**Reopening indicators.** The author says the speech was Shade's; the author wants his parking line as written; a reader asks why Stansbury looks at a poem; a reader reads "both" as blame on Shade.

---

## H3. Plan row 11's cuts (brief; GREEN)

**Claim.** The four cuts are safe: "good hand" (a causality slip), "Three adults," / "Do not make me decide which one of you I meant." (Pathwell denying Shade is a person, as a joke), the narrator's "because she had chosen Camp and the route belonged to that choice" with the other "I chose Camp" repeats, and "The sentence changed the room. / Not magically. / More effectively."

**Evidence for.** These are Plan.md's own row 11 (Plan.md:126: "good hand"; "Three adults"; the repeated "I chose Camp"; "The sentence changed the room."). The Assessment (Assessment-2026-09-29.md:123) and the cold reader (Cold-Read:406, :409) both flagged them. Kept after the cuts: Shade's "You chose Camp?" / "Camp." (Ch11:500-506), her speech (:582) and the last pair (:1132-1138), which are the lines the locks and Ch17 lean on.

**Notes, none a blocker.**
- The "causality error" reason is not quite right. She does have a sore shoulder from the seatbelt (Ch8:315; Ch10:9), as the Assessment says ("defensible, ... but it reads as a slip"). The cut is still right; the reason is that "good" suggests a hurt hand. Do not touch Ch13:178, where "good hand" is correct after the injury. Keep the sides consistent: the museum injury is the left shoulder (Ch11:891; Ch12:5, :88); the seatbelt side is never stated.
- "Three adults" is a free plant for Pathwell deciding what Shade is (Ch9:312), but nobody reacts to it on the page, and the cold reader read it as "slightly murky" (Cold-Read:409). Cut it. If H1's 11.5 lines are restored, the possessive slip is carried there and nothing is stranded.
- The Assessment named two more narrator verdicts that H3 and H6 do not list: "He looked at the room as though seeing the difference between a plan and its consequences for the first time in real time." (Ch11:872) and "Pathwell sitting among the consequences of protecting her after she told him not to." (:1128). Add both to the cut list, and cut without replacing (Craft.md:173, lesson 4).

**Verdict: GREEN.** Conditions: add :872 and :1128 to the cuts; leave Ch13:178 alone.

---

## H4. The clock (YELLOW)

**Claim.** Ch10 ends around one in the morning (the catch at the diner, found on the road an hour or so later; W17). Ch11 opens in gray dawn. One clause carries the gap: "The drive took most of what was left of the night." Shade, who drove straight there from the diner, has been waiting hours, which fits "drive-too-long tired" and "More driving. Worse coffee."

**Assumptions.**
1. Ch10 ends about one in the morning. (No text gives a clock time. Sunset is at the bar, Ch6:278-282; the diner is "less than an hour" after the crash, Ch9:196; "still full night" when she leaves, Ch9:366; she has "been walking for a little over an hour" when Ch10 opens, Ch10:3. One o'clock is an inference.)
2. Dawn needs a drive of four or five hours, and the museum is that far.
3. One clause is enough, and does not raise more questions than it answers.
4. Shade can be at the museum hours ahead of the group.
5. "Drive-too-long tired" fits hours of waiting.

**Weakest: 4, and 5 is the same fault.**

Shade's own lines in Ch11 say the opposite. "Drive-too-long tired" (Ch11:47) means a long drive, not a long wait; a man who went straight there and waited hours would be waiting-too-long tired. "The pull brought me this direction. Then I recognized the building." (:97) means he followed the draw and recognized the place on the way. C10 (LOCKED C, C10:20-30) says he follows the draw's rough pull, infers the destination as Pathwell's moving bearing aligns with a route he knows, and "drives directly" to arrive first. The draw "does not provide ... Pathwell's plans" (C10:23). While Pathwell is working at Stansbury's house (Ch10:93-301), the bearing is not moving toward anything. Shade cannot know the museum is the destination until the van moves. Q64r gives him "several minutes" to wander (C10:37). R0 §21 does say he "can therefore reach the museum first and wait" (R0:273), so waiting is locked; hours of it are not.

**Strongest alternative.** State the group's side of the gap only, or state no number. Let Shade's lead be small, as the locks have it, and let "drive-too-long" mean what it says.

**Evidence for H4.**
- Ch10 ends in the dark ("The dark waited outside the windows", Ch10:420) and Ch11 reaches gray without any marker (Ch11:179 "before the sun comes up"; :246; :421; :1247). A gap marker is not wrong.
- Dawn is his own: "Its almost dawn" at the museum (draft:2048).
- The draft's Shade drove the long way round (draft:1999), so a long night is his shape too.

**Evidence against.**
- Ch10:586: "The nearest one I know is at the museum." A threshold four or five hours off is a strange "nearest". (Cold-Read:367 finds the geography consistent: museum east, as the van turns east at Ch10:606. No distance is given anywhere.)
- The cold reader says of the clock: "By now I've mostly stopped trying to track it" (Cold-Read:450). The complaint was Camp being dark when the museum is light (11.9). A clause that says "most of what was left of the night" asks the reader to track it, and sets up Ch12:7 ("here it was still dark") as a second discrepancy.
- Five hours of van with Elizabeth, straight after the Ask (Ch10:560-564) and her "Camp." (:572), is a lot of unseen time. A reader may ask what they said.

**Cost if wrong.** One clause and one sentence in the pass log. But the clause fixes two facts (the museum's distance, Shade's wait) that the book would then have to honor and that two locks contradict.

**Verdict: YELLOW.** Proceed if:
- (a) The clause is about the group's travel only, and nothing in the chapter or the log says Shade waited hours. His lead stays small.
- (b) It does not contradict "nearest" (Ch10:586): either number-free or worded so the long road is a surprise.
- (c) Ch12:7 and Ch11:1247 are checked together (11.9) and the time-of-day gap is left as a deliberate difference, as the triage has it.
- (d) The assumed clock (Ch10 about one a.m.; museum at first light) goes in the Pass-Log marked unconfirmed, and the distance goes on the author's list (Q9 below).

**Reopening indicators.** A reader asks why nobody spoke for five hours; the author says the museum is near; 11.1 is reversed and Shade is inside for the whole night.

---

## H5. Ch10's duplicate museum joke (brief; GREEN)

**Claim.** Cut Ch10:596-600 back to "You know the place?" / "Unfortunately.", because Ch11's "I support the arts." exchange has the same shape and is the better one.

**Evidence for.**
- Ch11's exchange does a second job. "He donated the climate-control system ... eleven years" (:206) is paid in Ch17:252 ("Climate-control inspection because your discharge knocked two sensors out of calibration."), and the donor card in Ch12 (L9, Promise-Ledger; Ch12:529) is its echo. Ch10's does no work like that. No later chapter quotes "Museums like me." (grep).
- With Ch10 shortened, "Pathwell had a key." (Ch11:188) lands as a reveal instead of confirming "Pathwell likes museums".
- Ch10 still ends on a quiet character beat: "Stansbury turned east. Pathwell didn't correct the route." (Ch10:606).

**Against.** Ch10:596-600 is the chapter's one soft landing after the Ask (Rules.md: "somewhere soft to land"). Taking it out thins it. P35 found every chapter already has its soft landing, and "Unfortunately." plus the closing gesture do the work.

**Notes.** It reopens a chapter closed in P33/P34, so it needs a line in the pass log. The cold reader's complaint was the "Nine." correction formula (Cold-Read:414), not the duplicated joke; H5 does not touch that.

**Verdict: GREEN.** Condition: cut the "Why unfortunately?" line along with it, so nothing dangles.

---

## H6. Line pass (brief; GREEN with an extended keep list)

**Claim.** The examples are narrator flourishes and glosses, and the keep list holds everything the locks and later chapters rely on.

**Evidence for.** Each example is in the 08-28 narration, not in his lines: Ch11:3, :5, :386, :452, :454, :950, :1147, :1243-1245, and the blast runs. They are the tics the Cold-Read listed (Cold-Read:441).

**Against.** The keep list has gaps. Things later chapters rely on that it does not name:
- **The horse.** H6 cuts "one carefully drawn horse with the proportions of an unsuccessful dog" (Ch11:454), but the horse is a landmark. It marks the route ("a badly proportioned horse", :1050) and Ch12:11 calls back to it ("The badly drawn horse disappeared with it."). Cut the simile and keep the horse, or the callback has no plant (Craft.md:172, lesson 3).
- **Ch17's witness statement** (Ch17:358-366) rests on Ch11:646-654 ("I'm fine", "He slipped", "No") and :682 ("Put it away.").
- **"I can contain this."** (:718), which Ch14:1097 answers ("That's what you said at the museum.").
- **The museum records as Ch17 lists them** (Ch17:262-292, :342, :393): "narrow socks" (Ch11:340), the exact SAM HOME TODAY string (:405), the medical ledger, Margaret Bell's cards, Henry Vale on the buttons card (:282; Ch17:276-290 "Same family line"), the photograph.
- **Margaret Bell's bans** (Ch11:296-306; L5; Ch14:387), though one of the three number-corrections the cold reader called a formula can go (Cold-Read:413-414).
- **Shade's right hand,** a locked device (Q131/Q149, Decisions.md:100). "Restraint notes and gestures are trimmed" must not take the hand from the places that set up the snap at :620: :35-39, :482-484, :618-624, :938-940.
- **The destruction sequence.** The Assessment says to protect it "entire" (Assessment:123). Merging fragment runs is fine; the beats are not to go: the porch and the sister and socks (:776-784), "Someone needed eggs" (:810), the bandages-and-soap panic (:844-856), the cannon rolling (:864).
- **The climate-control and donor line** (:206) from H5.
- **His own imported lines.** Do not run the line pass on them (Craft.md:192-196; the same condition as the Chapter 10 report, G6).
- **Narrator verdicts** at :872 and :1128 (see H3) belong on the cut list.

**Verdict: GREEN.** Conditions: extend the keep list as above; run the pass after H1-H5 are settled, since H1(b) and H2 add lines the pass should not flatten.

---

# Overall verdict: ORANGE (H1 as written)

Per decision: H1 ORANGE (11.5 RED; 11.1 ORANGE; 11.2 YELLOW; 11.3 GREEN; 11.8 YELLOW), H2 YELLOW (H2.2 cannon and H2.4 "both" ORANGE as written), H3 GREEN, H4 YELLOW, H5 GREEN, H6 GREEN.

Draft H2-H6 with the conditions above. Do not record "Chapter 11 needs nothing". Either log H1 as a working decision put to the author (W16's shape) and restore 11.5, or keep the claim and say why W8 does not apply. If the claim must stay as written, my vote is RED on 11.5 and ORANGE on the rest of H1.

**What this report did not find.** No contradiction between H2-H6 and R23, R36 or W14 as such. No chapter after Ch11 depends on the parking exchange, the cannon, the lilacs, the speech or "I hate you both". No second lock that the poem inversion breaks: Q104 and Q139 ask for absence of the healing, not absence of the poem. No text that says Shade waited hours.

**What I could not verify.**
- Whether R23 was meant to reach a LOCKED USER REFINEMENT (Q64r) or a line lock (C3 §3). Its words are about "the audit's staging findings" and "most of this was done by the AI".
- The clock. No chapter states a time, so the one-o'clock and four-to-five-hour figures are inferences.
- Whether the 08-26 text of Chapter 11 (git 765b69b), which holds the three accusation lines, was written by the author or by the AI before the reconciliation. The lines are not in his working draft (grep of working.txt: no "took her", "yours"), so the lock may be preserving an AI line he approved. The locks are still his.
- Whether the fresh check's "four times" for the car-loss joke includes Ch8.

**Questions only the author can settle, in the order they are likely to change the chapter.**
1. **Q1. Shade's place and the trigger (11.1, 11.2, 11.3).** Do you want Shade inside, appearing from the shadows, Pathwell's body-block, and Shade's small open-handed step (the locks), or the lot scene, the argument and the stumble-and-grab (the manuscript)? Default: keep the manuscript, because of the sock beat and Ch17:362.
2. **Q2. The three accusation lines (C3 §3).** "You left the crash with her" / "you took her from me" / "She wasn't yours to take from." Restored? Default: restore.
3. **Q3. The graffiti speech.** Yours was Shade's. Is it Pathwell's now, and may Pathwell show he understands what Shade wants before Ch14?
4. **Q4. "For the record, I hate you both."** Does "both" include Shade, given the injury is Pathwell's alone?
5. **Q5. The poem.** Your Stansbury heals Pathwell with it; the locks you made say he does not. Is a silent look at it a beat you want, or should the poem stay out?
6. **Q6. The parking line.** Keep "just because we are trying to find a bad guy, doesnt mean we need to be one" as written?
7. **Q7. The cannon.** Points at the front door (yours) or the gift shop (the manuscript's running gag, five places)?
8. **Q8. The dagger.** A neutral line that keeps it with her now, or leave it until you choose the climax (R13, R15)?
9. **Q9. The clock.** How far is the museum, and how long does Shade wait?

**Reopening indicators (all).** The author wants Shade inside or the three lines back; someone writes Shade's "holding onto" inference and finds no slip to cite; Ch17:362 or Ch14:1097 is revised; a reader asks what the brothers and Elizabeth said for five hours; the cannon's lines disagree after the lobby swap; the speech reads twice; "both" reads as blame on Shade.

---

## Appendix: the decisions as written


Repo: /home/claude/pathwell. Chapter: Story/Chapters/Chapter_11.txt (3,831 words; the 2026-08-28 rewrite, not the author's text). The author's own museum draft: /tmp/claude-0/-home-claude/c14102f3-1f35-5356-85de-0367ac67de1f/scratchpad/working.txt lines 2030–2167, written for the older story (Shade kidnapping her and hearing "the narrator", a lock-picking entrance, a jump scare, Pathwell "killing himself before", a fight with exploding sheets, Stansbury healing Pathwell with a soldier's poem).

Authority: R1–R36 and W1–W17 in Story/Revision/Decisions.md (newest wins); then the Bible interview; then canon. W14 (his draft sets the voice, the newest locks set the story). R23 (interview staging is guidance; prefer existing text). R36 (leans applied and listed). The Chapter 11 locks are listed in Story/Revision/Decision-Timeline.md (grep "Ch 11" / "Ch11"): R0 §21, §23, §24; C2 §13; C3 §1–§3; Continued 10 (Q64 revised, C10 D), Continued 11, Continued 12 (Q68).

## H1. The structure stays (the triage's "Chapter 11 needs nothing")

The 2026-10-01 triage ([triage](../../../../../home/claude/pathwell/Story/Revision/Currency-Audit-2026-10-01/triage.md) rows 11.1–11.9) kept Ch11's staging against several locks:

- 11.1: Shade waits outside by his car, not inside wandering the dark museum (Q64 revised says he wanders inside and is settled in the shadows).
- 11.2: the trigger is a draw-stumble and a grab, not the lock's "small, open-handed, nonthreatening movement" (R0 §23).
- 11.3: "I don't need to be rescued" follows an argument, not Pathwell's body-block (Q68).
- 11.5: no road-accusation lines. C3 §3 (LOCKED B) wants Pathwell to accuse Shade of the literal event first ("You left the crash with her."), then reveal the possessive reading ("you took her from me"), and Shade's answer "She wasn't yours to take from."
- 11.8: the foam dagger is never mentioned after Ch10.

Lean: keep the triage, except that the dagger gets one line (it was last seen in her waistband in Ch10). That triage verdict was accepted with no findings, which is the tenth seat's trigger 2. **This is the decision most worth testing, especially 11.5 and 11.2.**

## H2. The author's lines brought in (W14)

- **Parking.** His Stansbury drives past the empty disabled spaces by the door: "Well, I don't want to get towed for parking in a blue spot. What if someone comes along and needs it?" / "Are you serious?" / "Look, just because we're in a hurry doesn't mean we need to be jerks." This replaces the current precision-parking and "I have suffered one vehicular loss tonight. I am restoring standards." (The fresh check found the car-loss joke four times across Ch8, Ch10 and Ch11.)
- **The lobby, his description.** "The museum was dim, the sparse glow of sprinkled lights cutting corners off the shadows… Front and center sat a cannon, pointed at the front door, flanked by two soldiers, one in dark blue, the other gray. Two brothers split by land and ideology… Photographs of still-framed ghosts, letters home." This replaces "The cannon was exactly where Shade remembered it. Pointed toward the gift shop." It also settles a contradiction: Shade's memory says the cannon points at the front door, but then he says it's aimed at the gift shop.
- **The graffiti house, his speech, given to Pathwell** (the museum's donor, with a key). Elizabeth: "This is what we came all the way out here for? A wall?" / "Not just a wall. The graffiti house." / "Civil War soldiers would come and leave graffiti… They were messages home, or attempts to be remembered as something beyond literal cannon fodder. These were men and boys looking for a chance to not be lost to time." That's Shade's own want, said by Pathwell without his hearing it.
- **After the blast:** Stansbury, first upright: "For the record, I hate you both." This replaces "No one commented. / For a while."
- **The aftermath, his image inverted.** In his draft Stansbury heals Pathwell by spending a soldier's poem (the lilacs, the "perfumed embrace of his wife"). After Pathwell has just destroyed three records, Stansbury spending a fourth would undercut the chapter's turn ("That is not the same as fixing it."; ledger R9). So Stansbury looks at the framed poem, the soldier wondering if he'll ever smell his wife's lilacs again, and goes to the office for the first-aid box instead. It's a new character beat in a cautious category, so it's plain and flagged.
- Not used: the narrator and the voice, the lock-picking, the jump scare, "killed himself before", the exploding sheets, Shade's ribs kicked, Elizabeth thrown through a display.

## H3. Plan row 11's cuts

- "She put out her good hand on instinct.": a causality error. She isn't hurt yet; the case hits her shoulder later. It becomes "her hand".
- "Three adults," / "Do not make me decide which one of you I meant.": Pathwell denying Shade is a person, as a joke.
- The repeated "I chose Camp". The narrator's "because she had chosen Camp and the route belonged to that choice" is cut. Kept: Shade's "You chose Camp?" / "Camp.", her speech's "I chose Camp.", and her last "I chose Camp." / "I'm still choosing it."
- "The sentence changed the room. / Not magically. / More effectively."

## H4. The clock

Ch10 now ends around one in the morning (P33/P34: the catch at the diner, found on the road an hour or so later). Ch11 opens in a gray dawn. One clause carries the gap: "The drive took most of what was left of the night." Shade, who drove straight there from the diner, has been waiting hours, which fits his "drive-too-long tired" and "More driving. Worse coffee."

## H5. Ch10's duplicate museum joke

Ch10 ends with "Pathwell likes museums." / "Museums like me." / "They do not.", the same shape as Ch11's "I support the arts." / the climate-control system / "Nine." The fresh check called Ch11's the better one. Ch10's exchange is cut back to "You know the place?" / "Unfortunately."

## H6. Line pass, with the tone and rules check in mind

Merge the fragment runs and cut narrator flourishes and glosses. Examples:

- "left it behind with excellent signage"
- "three fonts"
- "calling the ocean damp"
- "the proportions of an unsuccessful dog" (Ch4's horse was just cut for the same joke)
- "That was irritatingly good."
- "Possibly because Stansbury's tone had finally discovered a frequency…"
- "Which was worse."
- "No softening. / No correction."
- the "Not X. / Y." runs in the blast

Restraint notes and gestures are trimmed. Kept: everything the locks and later chapters rely on:

- "I don't need to be rescued."
- Shade's silence after it (C3 §2)
- "All right." / "You said all right." / "Do you?"
- the quarantine letter
- "Quickest. / Cleanest. / I can handle it." (Ch10's echo)
- "Third board from the left. Low."
- "I chose Camp." / "I'm still choosing it."
- "That is not the same as fixing it."
- "The information can be copied from the museum scans." / "The information." (ledger R9)
- "I did that." / "Yes."
