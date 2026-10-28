# Council round 1 · 26-ai-prose-detector

**Provenance:** council round 1, 2026-10-28. Blind brief from `Council/members/26-ai-prose-detector.md`, plus the round's "best version" section. Text: frozen `Story/Pathwell.txt` at commit 90bf73c. Model: sonnet. Retried on sonnet after an opus API safety false positive. The reader's report file write was blocked, so its hand-back text was saved by the coordinating session. Unedited.

REPORT PATH: I could not write /tmp/claude-0/-home-claude/2ba250fe-1d7c-5648-ad70-74e72ec9c33c/scratchpad/council1/26-ai-prose-detector/report.md. The Write tool refused ("Subagents should return findings as text, not write report files"), and my standing instructions say the same, so I did not work around it. The complete report is below. Save it to that path if you need the file.

THREE-LINE SUMMARY
1. Ch1-5 read human (rough, "!?" tags, adverbs, clichés). From Ch6 on the prose is controlled and homogenised: 264 "X looked at Y" beats (about one per 175 words), call-and-response "I know."/"No."/"That's not the question", 38 of 79 scenes ending on a short aphorism, and every Camp character speaking in the same dry register.
2. The late chapters' specifics (found documents, Hess, Milo's sock, SAM HOME TODAY, the Merritt cookbook, the geese) are unmistakably a person's and are the best thing in the book. The smoothing is in the connective tissue, the theme-announcing lines and the abstract emotional scenes (Ch6 mirror, Ch10 van confession, Ch14 climax, Ch16 apology/tribunal).
3. Fix: differentiate the voices, cut about half the gaze beats and scene-closing morals, make the emotional scenes concrete, compress repeated beats (the diary donation repeats the cookbook donation, and the lists are re-quoted), and leave Ch1-5 rough.

---

# Cold read, whole book: machine-smoothing report

Reader condition: cold, whole book, in order, about 400 lines at a time. The manuscript is about 45,800 words in 18 chapters. I opened only the brief and the manuscript. After the read was finished I ran counts on the manuscript text so the numbers below are real. The running log is at the end (Appendix A), written as I went and not revised.

## Verdict first

I can't prove machine involvement and I won't pretend to. What I can say: this is two books in one voice, and only one of them worries me.

- **Chapters 1-5** read like a person, a slightly rough and enthusiastic one. They have exclamatory dialogue ("Where is here!?"), adverbs on tags ("Pathwell said cheerfully", "said dismissively"), stock phrases ("The taste of dirt kissed her lips", "as all storms do, this one passed too") and awkward sentences nobody sanded. Those are the opposite of machine-smooth. All 8 "!?" in the book fall in Chapters 1-7. After that the book stops having them.
- **Chapters 6-18** are more controlled and funnier on the line level, and they are also where the signature of smoothing arrives: one prose rhythm, one dialogue shape, one emotional temperature, every character speaking in the same deadpan. Gaze beats climb from about 2-5 per thousand words in Chapters 2-5 to 10-17 per thousand from Chapter 6 on. Across the book there are 264 named-subject look constructions (Elizabeth/Pathwell/Shade/Stansbury/Mama Baga/Milo/archivist/healer looked at/toward/back/from/down/up), about once every 175 words. The bare phrase "looked at" appears 237 times.

The good news is large. The specifics in the late chapters (Hess, the socks, SAM HOME TODAY, Milo's boot, the Merritt cookbook) are not things I associate with machine prose. They're the best thing in the book. The problem isn't the content. It's the connective tissue and the dialogue music around it, which is homogeneous enough that an editor who has been burned by machine submissions starts to flinch. Confidence: medium. My uncertainty is whether this is machine smoothing or one writer's tic hardening as the book went on. The fix is the same either way.

---

## 1. Patterns I'd flag (with counts and quotes)

### A. The gaze beat as universal connective tissue
"X looked at Y. Y looked at Z." is the book's default way of moving between lines of dialogue.
- 264 named-subject look constructions. 88 lines begin "Elizabeth looked".
- Density by chapter (per 1,000 words): Ch2 1.8, Ch3 3.1, Ch4 8.0, Ch5 5.0, Ch6 14.5, Ch7 10.2, Ch8 13.0, Ch13 17.1, Ch16 16.4, Ch18 12.8.
- The triangular version is the worst: "Pathwell looked at him. Stansbury looked back at Pathwell." (Ch7); "Pathwell looked at her. Shade looked at Pathwell. Stansbury looked at the road." (Ch8); "Stansbury looked at Pathwell. Pathwell looked away." (Ch7); "Pathwell looked toward Stansbury." (Ch8). I count at least six glance-triangles.

### B. One-line dialogue ping-pong, with withheld answers
Short Q/A where the answer is refused, redirected or corrected: "That's not an answer." / "That wasn't the question." / "That isn't the same thing."
- Bare "I know." as an entire line: 17. "I know" in any form: 55. Bare "No.": 36. Bare "Yes.": 49. "I don't know": 26. The "That wasn't/isn't the question/an answer/the same..." family: about 14.
- Ch14's climax is largely a chant: "No." / "I know." / "Stop." / "Don't." / "I know." The beat works once or twice. It's used so often that it feels like a rhythm setting, not a scene.
- Ch9's diner interrogation: "What do you know?" / "I don't know." / "What did he choose?" / "That's his answer." / "Convenient." / "Accurate."

### C. Scene-ending one-liners
79 sections by my split. 38 end on a line of 7 words or fewer. Some are excellent ("Elizabeth drank." Ch4; "Nobody asked when she was coming back." Ch17; "He could." Ch17). The run of them is the sheen:
- "Pathwell stayed by the wheel." (Ch4)
- "Elizabeth followed. Pathwell didn't." (Ch4)
- "Too late to call it an accident." (Ch8)
- "Outside the high windows, it was daylight." (Ch11)
- "Shade did not either." (Ch15)
- "Elizabeth smiled." (Ch17)
- "Behind her, Camp Cunnan kept being a place without asking permission." (Ch4)
The last is the tell in miniature: an abstract noun ("permission") given a trailing flourish to close the scene.

### D. Aphorism-as-scene-closer, the "That was the choice" family
- "That was the choice. / Everything afterward was consequence." (Ch4)
- "That was the choice. / Everything else burned afterward." (Ch15; a deliberate rhyme, but the same device)
- "Not everything. Something." (Ch15)
- "Loss didn't care much about paperwork." (Ch16)
- "That didn't make it nothing." (Ch12)
- "The choice was ridiculous. / It was still hers." (Ch17)
- "The information survived. The page didn't." (Ch17)
- "Museums are arguments conducted very slowly." (Ch11)
Each is fine alone. As a family they teach the reader to wait for the moral at the end of every beat.

### E. "Not X. Y." and other negated-fragment turns
- "Not burned. Spent." (Ch4)
- "Not hidden. Not displayed. Available." (Ch4)
- "Not cruel. Worse. Useful." (Ch7)
- "Not now. Not here. Not necessarily not her." (Ch6)
- "Not compulsion. Awareness." (Ch8)
- "Not who. Not where. Which way," (Ch8, dialogue)
- "Not later. Not at Camp. Now." (Ch10)
- "Not a direction he trusted. Barely a direction at all." (Ch6)
- "Something opened. Not flesh. A seam." (Ch7)
- "Not disastrously; worse than that, because..." (Ch13)
About ten, concentrated between Ch4 and Ch13.

### F. Triplets and anaphora in speeches
- Elizabeth: "I'm not asking you whether it's a good idea to tell me. I'm not asking what you think I can handle. I'm asking what you did." (Ch10)
- Elizabeth: "Important enough to get dragged out of my apartment. Important enough to follow your cart through the woods. Important enough to give up Nana's cookbook..." five times (Ch8).
- Elizabeth: "I am not going to tell you what lesson to learn so you can learn it at me. I am not going to make your guilt useful. I am not going to say losing Shade was worth something because maybe you change after it." (Ch16)
- Narration: "Elizabeth cried for Nana. / For Shade's green jacket and excessive pockets. / For a man whose history had only just begun..." (Ch16)
- "The diary was gone. / The cookbook was gone. / Shade was gone. / Milo was alive." (Ch16)
- Descriptive triples: "a distant siren, a taxi splashing through a puddle, a group talking and laughing as they passed" (Ch2); "Journals with cracked spines, letters bundled in ribbon, recipes on index cards spotted with oil" (Ch3); "Easy to dismiss as pruning damage, or exhaustion, or age" (Ch6).
Triplets in the late-chapter comedy mostly work (Consistency/Stagnation/Branding, Ch6). The emotional ones read as the machine default.

### G. Characters announce the theme
The book dramatizes its subject (use versus preservation, asking before taking, who decides), then has someone say it.
- "Familiar things are useful." (Ch3)
- Elizabeth, Ch5: "It doesn't really feel any different from what you did at the bookstore. Selling off potential nobody was going to use."
- "Museums are arguments conducted very slowly." and "History books make everyone sound like they spent all day becoming history. Mostly they were worrying about socks." (Ch11)
- Shade: "People keep doing that." / "Asking." / "Terrible habit." / "Disorienting." (Ch13). By then the asking-permission motif has already been shown several times (Stansbury Ch6, healer Ch12, archivist Ch12, Mama Baga Ch13).
- Mama Baga: "Person is the word I have for that." after "He chose to stay here. He played cards. He made bad coffee. He died." (Ch16). The list does the work; the last line explains it.
- "I need you not to make me responsible for whether you become a better person." (Ch16)
- "The person who broke the thing does not get to set the schedule because waiting makes him uncomfortable." (Ch16)

### H. Abstract nouns doing emotional work
Strongest where the book is least specific.
- "A life she'd packed into garbage bags and moved across the city because staying felt worse than leaving, but leaving didn't feel like anything at all." (Ch2)
- "Pathwell screamed in a million voices, voices lost to time, burning out to become memories never made. One by one they fell quiet, until all that was left was a harmony of extinguished cries." (Ch3)
- "His own face in the mirror suddenly felt less like evidence than like an accusation." (Ch6)
- "A woman's patience worn raw around one particular absence." (Ch10)
- "Someone writing a daughter's name three times because once had not felt sufficient." (Ch14)
- "pale branching light spreading from Pathwell's shadow, possibility given a shape only because the eye needed something to fail at understanding." (Ch14)
- "ordinary things had remained aggressively themselves." (Ch17)
- Pathwell's confession in the van (Ch10): "They had a problem. A real one." / "Because I thought I knew the cleanest way through it." / "My choice produced the failure he came from. That much is mine." / "At the time, I would have called that responsibility." The whole scene is made of abstractions and has no object in it. The Nana scenes are made of objects.

### I. The inanimate object has an attitude
A charming habit that turns into a monoculture.
- Fish: "watched the room... with the exhausted expression of something that had heard all of this before", later "The mounted fish went on withholding judgment." (Ch6)
- Mirror: "The mirror offered no opinion." (Ch6)
- Wall: "The wall had been arrogant all day." (Ch6)
- Bells: "a small, exhausted noise" (Ch9)
- Mailbox: "The mailbox declined responsibility." (Ch10)
- Shoulder: "like something offended to still be attached to her" (Ch15)
- Apartment: "The apartment didn't answer. It had gotten better about that." (Ch18)
- Bus: "A bus sighed at the curb." (Ch18)
- Also trees "spiteful", counter and shelves "complained", silence "practicing".
About 14 across the book. Each is a joke. Fourteen is a house style.

### J. Callbacks that are explained, and verbatim recycling
- "One sock had surrendered halfway down his calf." appears word for word in Ch4 and Ch12.
- "It was the crash that woke her." (Ch1) returns verbatim in the middle of the Cadillac crash (Ch8).
- "Wet. Heavy." (Ch1, end of Ch6).
- "It's the useful version." (Ch5, Ch6).
- "Elizabeth's hand was still halfway raised. She lowered it." (Ch4) and "Elizabeth's hand stayed suspended after the diary left it. Empty. She lowered it." (Ch12). The diary donation is the cookbook donation run again.
- The CALL ELECTRIC / BUY BOXES / CHANGE ADDRESS / FIND NANA'S SPOON list is quoted in full in Ch12 and again in Ch15. The cookbook card is requoted in Ch15. "MORE IF THEY'RE SICK" reappears in Ch18.
- Callbacks that point at themselves: "Elizabeth heard the work van inside the sentence. Quickest. Cleanest. I can handle it." (Ch11); "Elizabeth remembered the Space Between, and then the diner." (Ch13); "Pathwell said exactly that to me once. About terrible coffee." (Ch13); "Disorienting," she told the empty apartment. (Ch18).
Callbacks are lovely when they land silently (the geese; "'Worse,' Mama Baga said, and went to see about the goat."). They're weakest when the narration leans in and points.

### K. Same voice everywhere
Mama Baga, the archivist, the healer, the shopkeeper, the curator, Stansbury, Shade, Pathwell and eventually Elizabeth all speak in short, dry, formally built lines that end on a turn. These could be swapped between mouths:
- Archivist: "Specificity is expensive."
- Healer: "I ask because people point at the wrong thing surprisingly often."
- Shopkeeper: "A month is not a character trait."
- Curator: "Paid is not completed."
- Mama Baga: "That is not a posture."
- Stansbury: "It makes the cost mine to approve."
- Shade: "Observation. Not memory."
Each is excellent. In a row they sound like one thoughtful narrator in costume. Pathwell was the only grandiloquent one in Ch4 ("Dwelling of charmers..."). By Ch16 everyone has caught it. Only Milo, the bartender, Ken the security guard, the waitress and the old woman in the knitted cap sound like someone else.

### L. Everyone is considerate
Mama Baga waits; the healer asks permission; the archivist asks "Store?" "Loan?"; Stansbury doesn't give opinions Elizabeth hasn't asked for; the curator doesn't ask her to mediate; Shade waits; Pathwell finally asks "May I?" It's a stated value and a good one. But it means there is almost no friction among the Camp people, and the conflict becomes Pathwell against everyone else being reasonable. That is the machine's resting state: warm, procedural, nobody unreasonable (except the shopkeeper, who is great because he is).

### M. The usual vocabulary tells are not the problem
Em dashes 37 in 45,800 words (fine). "somehow" 7, "exactly" 23, "quietly" 8, "ordinary" 15, "aggressively" 2, "Of course" 10, semicolons 7. "terrible" 17 is the coffee motif and it's earned. The vocabulary isn't the issue. The rhythm is.

---

## 2. Chapters, most to least machine-smoothed

**Most smoothed** (the connective tissue, not the jokes)
1. **Ch16**: 49 one-line narration paragraphs, the highest in the book; "looked" 16.4 per 1,000 words. The apology, the tribunal ("Agreed." x5), the "person" speech. It also holds Milo's best lines. The smoothing is in the ethics, not the particulars.
2. **Ch14**: the climax is a chant of "No." / "I know." / "Stop." plus mechanism jargon ("rejoining frame", "Two anchors. One return.", "Your intent is split").
3. **Ch13**: 17.1 looks per 1,000 words, 30 one-line paragraphs. Pleasant, but four Hearts scenes make the same move four times.
4. **Ch10 second half** (the van confession) and **Ch9** (the diner interrogation). Abstract Q/A with almost no objects.
5. **Ch6 mirror interlude** (Pathwell alone): "A thread caught somewhere behind the ribs and drawn taut at odd intervals."
6. Ch12 middle (stew, wagon, archive).

**Least smoothed**
1. **Ch5** (school, Cadillac, town): rough, adverbial, fun, even clumsy. "The pint-sized siege of chaos raged around them, but as all storms do, this one passed too." That's a person.
2. **Ch1 and Ch2**: wobbly in places, specific everywhere ("a tray of cheese cubes going dry", the ticket skipping into the gutter, "ELIZ").
3. **Ch3 Nana flashback** and **Ch4 archive scene**: made of nouns and oddities.
4. **Ch11 museum**: accession cards, socks, cannon aimed at the gift shop, the Vale letters.
5. **Ch17**: a montage, yet specific and funny line by line (The Lemon; "spaewife"; "Label crooked.").
6. Ch18 Merritt cookbook and the geese.

---

## 3. Passages that are unmistakably a person (protect these)

- "reading her diary like a magazine in a waiting room" (Ch1)
- "half a sheet cake that now only read ELIZ, because her coworkers had started at the wrong end." and "The cake, somehow, was fine." (Ch1)
- The dry-cleaning panic monologue, and the ticket that "skipped off the edge, caught the gutter, and was gone." (Ch2)
- "It's not a dream. Just a really weird Tuesday for you." / "It's Thursday." / "Which makes it all the weirder." (Ch2)
- The Nana flashback in full (Ch3): "Nana's house had thirteen stairs, and by the end Elizabeth knew which ones complained." / "'We'll see' in the voice she used for weather and doctors." / "She learned to carry a plate up thirteen stairs without spilling it, and to carry it back down mostly full." / "The pepper was the best part, Lizzy." / "told her the dumplings were heavy." / "Then you made them wrong." / "She topped off her own glass while she was at it, because she was at it." / "There was no upstairs."
- "leaving behind a lingering feeling that reminded her of a boy she knew in middle school." (Ch3)
- "He's the full-time guardian and part-time blood god." / "We pay him in mice." / "It's alarmingly close." (Ch3)
- "as though posture had become the problem" (Ch3)
- "with the offended posture of a man who had only recently learned the handcart existed" (Ch4)
- The beetle: "It's practicing," ... "Being dead." (Ch4)
- "It was tea, or something tea had become after a long argument with bark." / "Sit before you fall over politely." / "That is not a posture." (Ch4)
- MORE IF THEY'RE SICK. THEY WON'T EAT ENOUGH. and "She believed soup was an argument you could win." (Ch4)
- "The expectation arrived automatically, the way you hold out your hand for change after paying." (Ch4)
- The archivist: "Everything is new when you are twelve." / "I'm eleven." / "That explains the filing." / "Hess has been dead twenty-two years." / "He'd still argue." / "That is generally the opposite of an archive." (Ch4)
- "Thumper's paw print was in there somewhere. He had been a very bad cat about ink." (Ch5)
- "You would be forgiven for not stopping in the town as you drove through, and even more forgiven if you didn't notice it while you did." and "whether the cars would just migrate from one to the other as the day went on." (Ch5)
- "The bartender opened a jar of pickled eggs, reconsidered the smell, and closed it again." / "I tip historically." / "The wall had been arrogant all day." (Ch6)
- "Stansbury had said that at the school as though there were ordinary situations in which such a sentence belonged." (Ch7)
- "Her knees felt weak. They weren't hurt, just late to the decision." / "He'd gotten her name right. It didn't improve the sentence." / "My axle is in a drainage culvert. I'm evaluating several positions." (Ch8)
- "Try some nouns." and Shade's list "A room in Prague I have never entered. A woman named Celia who hated pears..." (Ch9); "A gas station with one light still on. A church sign announcing last week's fish fry. A motel vacancy sign missing the V." (Ch9)
- "She sang them in her head until her humming gave her away." (Ch9)
- "Stansbury lived two miles from the ditch. This hadn't saved the Cadillac. It had only made the walk home shorter." / the grocery lists (MILK / ONIONS / ASPIRIN / STAMPS / SHOE POLISH) and "Nothing more romantic than errands." (Ch10)
- Ch11 almost whole: "Look, just because we're trying to find a bad guy doesn't mean we need to be one."; "He donated the climate-control system after arguing with the board for eleven years." / "Nine." / "The first two years still count if nobody invited you."; "one of them had a key and poor boundaries"; the corrected accession card (REGIMENT UNKNOWN. / Then UNKNOWN crossed out. / Then 19TH VIRGINIA?...); the socks; SAM HOME TODAY. THIN AS A FENCE RAIL. ATE THREE EGGS.; "Someone was home. Someone wasn't dead. Someone needed eggs."; "Her arm stopped belonging anywhere reasonable."
- The Ch12 healer scene: "Because it's your shoulder."; "Strong sales pitch."; "You people are committed to making trees unpleasant."
- "FIND NANA'S SPOON. The last item was checked twice." and DONOR PERMISSION REQUIRED. PATHWELL IS NOT DONOR. (Ch12)
- "dissolved a burnt fence post in hot water and then concentrated it for shipping"; "Pockets," he said.; the boy's "You look like Pathwell. But you don't talk as much." (Ch13)
- "His sock had finally stayed up. Elizabeth hated that detail immediately."; "This next part is stupid." / "Pathwell stupid?" / "Worse. Mine."; "like something offended to still be attached to her" (Ch15)
- "He still owes me a hand."; SHADE — DIED AT CAMP. ... LIKED POCKETS.; "Archive burned. Categories are temporarily flexible."; "like a tongue finding the place a tooth used to be"; "You inhaled like an advertisement."; "Elizabeth didn't laugh. She didn't mind that someone else had." (Ch16)
- Ch17: "restitution contained more rulers than magic"; "I have been placed under unreasonable government."; the third copy where "Pathwell had quietly fixed somebody's spelling of Susquehanna" and then "copied the page again, mistake included"; "with more spaewife in it"; "'Worse,' Mama Baga said, and went to see about the goat."; "Label crooked."
- Ch18: "emotional support dumpling"; "I could have called someone. I didn't."; RUTH LIED ABOUT THE LARD. / ALSO GOOD WHEN YOU HAVE BEEN FIRED. / NOT THAT GOOD.; "They have learned commerce." / "They steal buttons."; and the closing "Are you ready?" / "No." / "Perfect."

If I could keep only one thing, it would be the found documents (cookbook margins, accession cards, the loss sheet, the road notebook). That's where the book's voice is least reproducible.

---

## 4. What a human editor would roughen, vary or cut

**Cut or fold**
- The diary donation (Ch12) duplicates the cookbook donation (Ch4) beat for beat: offer, "Store?" "Loan?", hand out, hand left suspended, "She lowered it". Compress it to a paragraph or find a different action. It also puts the CALL ELECTRIC list on the page a second time.
- Re-quoted lists and cards in Ch15 (the diary list, the cookbook card). One glance, not the full text.
- Ch16 tribunal: five "Agreed." and a long recited obligations list. Keep Mama Baga's "What do you owe?" / "Wrong." and "When somebody tells you stop, develop a new hobby." Cut about half of the archivist's list.
- Elizabeth's Ch16 speech has one great phrase ("so you can learn it at me"). The other two anaphoric sentences are the machine default. Keep one.
- Ch13: four separate Hearts scenes. Keep the queen-of-spades humiliation, the onion sack with "Pockets", and the sock-circulation gag. Fold the rest.
- "People keep doing that." / "Asking." / "Terrible habit." / "Disorienting." (Ch13): cut. The reader got it.
- "Person is the word I have for that." (Ch16): cut the line, trust the list.
- Narrator's moral-gloss endings (Pattern D): cut at least half, especially "Behind her, Camp Cunnan kept being a place without asking permission." (Ch4), "Loss didn't care much about paperwork." (Ch16), "That didn't make it nothing." (Ch12), "Not everything. Something." (Ch15).
- Ch14's chant: trim the repeated "No." / "I know." / "Stop." runs by about a third and let a physical action break them.

**Roughen or vary**
- Gaze beats: replace roughly half with action, an object, a noise from outside, or nothing. Start with the glance-triangles in Ch7 and Ch8. Let some dialogue run unbroken.
- Dialogue length: give Mama Baga one long, rambling, uncomposed speech. Make the healer sharp in a different way (she's currently a calmer archivist). Make the archivist pettier. Make the curator tired or rude. At present every Camp character ends a sentence on a polished turn.
- Let someone at Camp be unreasonable. The shopkeeper and the museum curator are the only authority figures with an edge.
- Let Elizabeth say something stupid or unfair at least once after Ch8. She becomes the book's reasonable speaker, then its judge ("I need you not to make me responsible for whether you become a better person").
- Pathwell's confession (Ch10 van) needs an object and a name. Who asked for help? What was the problem? One concrete image would move the whole scene from abstract to felt. At present it is "A real one." and "the cleanest way through it".
- Ch6 mirror interlude: add one physical detail from Pathwell's life (a coat lining, a cup, a name he's forgotten). As written, "tension" appears five times in nine lines and abstract nouns carry the emotion.
- Magic vocabulary: "working," "prune," "draw," "threshold," "charged," "waste," "return line," "rejoining frame." They are introduced deadpan and fast. A cold reader never gets one plain sentence like "pruning means selling your own future." That is a style choice and also another abstraction layer.
- The Ch10 slaps ("the next time I call you an idiot, you smack me") and "Bank it.": I didn't understand them and didn't care. Make the joke legible or cut it.
- Sentence length: late chapters live in the 4-12 word band. Allow one long runaway sentence per chapter (the Ch4 boar-and-fiddle paragraph shows you can).
- Hide some callbacks. Let the reader catch "terrible" / "I know" without the narration saying so.

---

## 5. Ranked top ten: what I most want you to hear

1. **The book is better than its rhythm.** The invention is strong (the archive that asks "Store?" "Loan?"; found documents as magic; the Space Between's tribute). It is wrapped in a rhythm that sounds the same on every page after Ch6. Fix the rhythm, not the content.
2. **Everyone speaks like the narrator.** Mama Baga, the archivist, the healer, the curator, Stansbury and Shade can be swapped line for line. Differentiate by length, pettiness, error, tangent and vocabulary. Give at least three characters speech a reader could identify with the tags removed.
3. **Gaze-beat dependence.** 264 looks, 88 of them Elizabeth's. From Ch6 on it's the connective tissue of nearly every exchange. Cut half and replace with action, objects or nothing.
4. **Stop telling us the theme after we've felt it.** "People keep doing that. / Asking." (Ch13), "Person is the word I have for that." (Ch16), "That was the choice. Everything afterward was consequence." (Ch4), "Loss didn't care much about paperwork." (Ch16). Trust the scene.
5. **Scene endings.** 38 of 79 sections close on a short line. Keep the best (Elizabeth drank; He could; Nobody asked when she was coming back). End others mid-motion, on an object, or on dialogue that isn't a turn.
6. **The emotional spine goes abstract exactly where it should go specific.** Pathwell's confession (Ch10), the mirror (Ch6), the Ch14 mechanics, the Ch3 sacrifice ("a harmony of extinguished cries"). Give each a name, a place, a thing in a hand.
7. **Repeated and re-quoted material is padding.** The diary donation duplicates the cookbook donation; the CALL ELECTRIC list is printed in full twice; the sock sentence recurs verbatim; the "No." / "I know." chant. Trim 5-8% overall.
8. **Everyone at Camp is reasonable.** The "ask first" ethic is admirable and also soothing to the point of sameness. Let it cost something, or let someone get it wrong.
9. **The first five chapters and the last thirteen read as different hands.** The early ones are rougher and adverb-happy ("said cheerfully", "!?", "The taste of dirt kissed her lips"). The late ones are controlled and uniform. Do not smooth Ch1-5 to match. Let the late chapters recover some of the early looseness. Fix the clichés in Ch1-5 ("a beacon to all late night cravings"; "as all storms do, this one passed too") but keep the mess in the voice.
10. **Protect the objects.** The cookbook margins, the accession cards, the loss sheet, the road notebook, the Merritt book, Hess. When in doubt, add another one and take out a line of dialogue.

---

## 6. The best version

### 6.1 What to protect (quoted)

- The found documents: MORE IF THEY'RE SICK. THEY WON'T EAT ENOUGH.; the accession card that had to be corrected three times; SAM HOME TODAY. THIN AS A FENCE RAIL. ATE THREE EGGS.; DO NOT TRUST THE SOUTH BANK AFTER THREE DAYS OF RAIN, NO MATTER WHAT HESS SAYS. / HESS SAYS FOUR.; SHADE — DIED AT CAMP. / LIKED POCKETS.; RUTH LIED ABOUT THE LARD.; the diary to-do list with "The last item was checked twice."
- The Nana flashback (Ch3), whole. It is the book's prose standard.
- Milo and his sock ("His sock had finally stayed up. Elizabeth hated that detail immediately."), and "He still owes me a hand."
- The comic objects: the cannon aimed at the gift shop, the geese ("They have learned commerce."), the wall that was "arrogant all day", The Lemon, the Cadillac "sitting about six inches lower than the rest of it."
- The restraint when it shows up: Pathwell waiting while others are treated ("So he waited. Elizabeth noticed how strange that looked on him."), "I could have called someone. I didn't." (Ch18), and "Elizabeth didn't laugh. She didn't mind that someone else had."
- The structural bookend: Ch1 "Ready?" / "No." / "Perfect." and the last page.
- The premise at the heart of the archive: the cookbook given up whole, the diary given, and the choice to save Milo over both (Ch15). Keep that decision close to unadorned.

### 6.2 The changes, in order of impact

1. **Differentiate the voices. (Medium-large.)** Where: Ch4, Ch12, Ch13, Ch14, Ch16, Ch17. Pick distinct registers: the healer blunt, practical and technical, no wit; the archivist finicky and petty, easily offended by disorder; Mama Baga warm and long-winded with short barbs saved for a crisis; the curator tired and bureaucratic; Stansbury crankier and less composed than Pathwell; Shade even more sparing. Reader effect: you can tell who is speaking without tags, and the deadpan stops sounding like a house style. Size: a dialogue pass across about eight chapters.
2. **Cut the gaze beats and glance-triangles by half. (Medium.)** Where: Ch6-Ch18. Replace with an action, a prop, a noise, or a plain run of dialogue. Reader effect: pace quickens and the prose stops feeling like a loop. Size: line edit, mostly mechanical.
3. **Remove the moral glosses that follow scenes. (Small-medium.)** Where: Ch4 (scene ends), Ch12 ("That didn't make it nothing."), Ch13 ("People keep doing that."), Ch15 ("Not everything. Something."), Ch16 ("Loss didn't care much about paperwork.", "Person is the word I have for that."), Ch17 ("The information survived. The page didn't."). Reader effect: the reader does the arithmetic and the moments land harder.
4. **Make the emotional scenes concrete. (Medium.)** Where: Ch6 mirror, Ch10 van confession, Ch14 climax mechanics, Ch3 sacrifice, Ch16 apology. Add one specific, named, physical detail and cut one abstraction in each. Pathwell's old job especially needs a person and a problem the reader can picture. Reader effect: the central wound becomes visible and Shade, who is its result, becomes someone to mourn for more than his pockets.
5. **Compress the repeated beats. (Medium.)** Where: Ch12 diary donation, Ch13 Hearts, Ch15 quoted lists, Ch16 tribunal, Ch14 chant. Reader effect: about 3,000-4,000 words lighter, and the quiet middle stops reading as one engine run four times.
6. **Give the middle some friction. (Medium-large.)** Where: Ch12-13 and Ch16. A Camp resident who resents Elizabeth or Shade; Elizabeth being wrong about something and saying so; a disagreement among the Camp elders about Pathwell that doesn't resolve in two lines. Reader effect: the book's ethic (ask, wait, listen) costs something, so it counts.
7. **Light-touch the first five chapters. (Small.)** Fix the real flab and clichés: reduce the "!?" pattern (keep two); tighten the Ch5 portal paragraph, which repeats "spinning" and "gaining"; resolve the Ch1 contradiction ("The party was still out here... The guests had left hours ago."); remove the duplicated "laughed at her joke about the landlord, which was more than anyone from work had managed" (Ch1 and Ch3). Do not smooth these chapters to match the rest. They are the book's most human.
8. **A deliberate sentence-length and sound variation pass. (Small-medium.)** Allow one long wandering paragraph per chapter. Mix in a paragraph that ends mid-thought. Vary section endings. Reader effect: the page stops looking like a series of equally weighted lines.
9. **Make the magic vocabulary legible to a cold reader. (Small.)** One plain sentence defining "prune" and "working" in Ch5 or Ch6, in an off-hand voice, not a lecture. Fix or cut the "Bank it." slap gag in Ch10. Reader effect: fewer moments of "I don't know what this means and I don't care."
10. **Add more found documents. (Small.)** Wherever a character is about to deliver a thematic sentence, try handing the reader a card, a list or a margin note instead.

### 6.3 The shape of the best version

A reader opens it in a messy apartment with a funny, specific, slightly off-kilter voice. They stay with it through the dumpling stand, the Space Between and the cat, and then the quiet of the Nana chapter, where the prose goes to actual objects and stays there. At Camp the book gets populated. A cheerfully merciless eleven-year-old, a petty archivist and a healer who talks like a nurse and not a fortune cookie give the place a crowd. The brothers' bickering stays and the jokes still land, but the speech patterns separate, so that by the middle the reader can tell who is talking without a tag. Pathwell's old failure is no longer "a problem, a real one". It is a person with a name and something he was trying to save, so that Shade, the walking result of that failure, makes sense as someone to mourn.

The prose gets quieter in the middle. Fewer glances, more hands doing things: a coffee grinder, a hammer, a lantern, a pin in the dirt. The archive fire isn't a chant. It is one stretch of terrible, concrete action followed by Elizabeth's decision, which the narration leaves alone. The loss sheet and the Hess notebook do the grieving, so the speeches don't have to. Camp is warm but not frictionless. Someone is wrong, someone is unfair, someone holds a grudge, and the "ask first" ethic costs something real before it pays off.

The ending is the same ending. Ch18 stays, because the Merritt cookbook, the geese and "Then come with me." are the best proof the book has learned what it's about. The reader closes it knowing a handful of people by how they talk, remembering a sock, a card game and a cookbook that said RUTH LIED ABOUT THE LARD, and not remembering a rhythm.

---

## Appendix A. Running log (first reactions, written as I read; not revised)

*Lines 0-400, Ch1 to start of Ch3.* Ch1 is funny, specific, clumsy in a good way: "reading her diary like a magazine in a waiting room", "ELIZ", "The cake, somehow, was fine." Odd contradiction: "The party was still out here... The guests had left hours ago." "Stillness. There was only her racing heart and stillness. A stillness interrupted by a dull rumbling, rumbling that grew into shaking, a shaking that rocked the walls" is the first machine-looking move (anaphoric chain). Ch1 ends on "Perfect." Ch2 banter is good ("It's Thursday." "Which makes it all the weirder."). Panic monologue good. Ticket in the gutter great. Then: "A life she'd packed into garbage bags... leaving didn't feel like anything at all." Smooth. "The sounds of the night took over: a distant siren, a taxi... The city was in motion even now." Triplet plus stock. Ch3: "Not books—lives." "a silence that felt like it had been here practicing for years." Flagged as sheen.

*Lines 400-800, Ch3 end to Ch4 mid.* The Nana flashback is the best prose so far and the first thing I'd protect in the whole book. "'We'll see' in the voice she used for weather and doctors." The party paragraph repeats Ch1's landlord line almost verbatim. Pathwell's sacrifice ("a harmony of extinguished cries") reads like autopilot after the Nana scene. The shopkeeper and "Will that be paper or plastic?" are good. Ch4 starts well ("Camp Cunnan announced itself in woodsmoke before it showed up."). Sock, beetle, "Sit before you fall over politely." Cliché flags: "The taste of dirt kissed her lips." "She didn't ask about the apartment, or the missing front door, or what kind of person follows a man like Pathwell through a wall after midnight." (negative triplet).

*Lines 800-1200, Ch4 mid to end.* Healer scene: MORE IF THEY'RE SICK. is lovely. Then "That was the choice. Everything afterward was consequence." and "Not burned. Spent." I start to hear a rhythm. Clothes and gold chain: stock warm-old-woman scene. Archivist: terrific. "Specificity is expensive." Closing line "Behind her, Camp Cunnan kept being a place without asking permission." flagged. Everyone wry in the same way.

*Lines 1200-1600, Ch4 end, Ch5, start of Ch6.* Ch5 is a different texture: adverbs, "!?", the portal paragraph runs long and repeats "spinning". Reads like an older draft or a different mood. Funny details (Thumper). "pint-sized siege of chaos... as all storms do" is cliché. Stansbury's exposition is serviceable. Elizabeth explicitly says the theme ("Selling off potential nobody was going to use"). Ch6 bar: fish, pickled eggs, "I tip historically": great.

*Lines 1600-2000, Ch6, start of Ch7.* The Pathwell mirror interlude is the first stretch I'd call smooth: "A pull without a destination. A thread caught somewhere behind the ribs..." plus a triplet plus "damage was easier than mystery." "The mirror offered no opinion" echoes the fish. Ch7 fight is crisp with short sentences. "Do it quieter." "Criticism received." good.

*Lines 2000-2400, Ch7 end, start of Ch8.* Elizabeth chooses the ditch: good voice. "Her knees... just late to the decision." "It was the crash that woke her." dropped into the middle of the crash, odd but deliberate. Her five-times "Important enough" speech is a structured heroine speech. The stranger arrives.

*Lines 2400-2800, Ch8 end, start of Ch9.* Shade is distinct for a while ("Enough name." "Try some nouns."). Road details good. Diner coffee: "terrible" again, restating Ch3 ("Late nights spent studying"). Bells "exhausted".

*Lines 2800-3200, Ch9 end, start of Ch10.* Q/A ping-pong in the diner, a lot of "I don't know." The account of what Pathwell did is abstract. "I'm tired of carrying pieces of an answer that belong to a question I never asked." polished. Ch10 walk good. Slap gag confusing. Unsent letter passage: "A woman's patience worn raw around one particular absence." Abstract.

*Lines 3200-3600, Ch10 end, start of Ch11.* Grocery lists wonderful. The van confession is pure abstraction ("A real one."). Elizabeth's triple "I'm not asking..." I wasn't moved and didn't quite believe it. "Mama Baga didn't ask me anything I didn't want to tell her": earlier she did ask. "Because Mama Baga doesn't belong to either of you" is the best line in the scene.

*Lines 3600-4000, Ch11.* Museum: the best chapter so far. The accession card, socks, SAM HOME TODAY, "Someone needed eggs." Pathwell's graffiti lecture is stiff. "two brothers split by land and by ideology" is cliché; "photographs of still-framed ghosts" awkward. Mild boredom at the freeze/stop choreography of the Shade/Pathwell standoff.

*Lines 4000-4400, Ch11 end, Ch12.* "I am adjusting my brand." "a cold pack that took both hands and an insult to activate." Healer scene lovely. The sock sentence repeats verbatim from Ch4.

*Lines 4400-4800, Ch12 end, Ch13.* The diary donation is Ch4 again. "That didn't make it nothing." DONOR PERMISSION REQUIRED. PATHWELL IS NOT DONOR. Jacket and "I have inherited worse problems." Coffee. Interest dips with the second Hearts scene.

*Lines 4800-5200, Ch13 end, start of Ch14.* "Pockets." Onion sack. "People keep doing that. / Asking." (flagged: says the theme). Ch14 opens strongly: "The threshold opened onto the unfinished hand of Hearts."

*Lines 5200-5600, Ch14.* Banter good ("I'm standing beautifully." "You're listing."). The climax is mostly "No." "I know." "Stop." Jargon ("rejoining frame", "Two anchors. One return."). I started skimming for plot.

*Lines 5600-6000, Ch14 end, Ch15.* Fire sequence: the list of released impressions starts generic then lands ("Someone writing a daughter's name three times because once had not felt sufficient."). Ch15 rescue is the best action prose in the book. "His sock had finally stayed up." "Worse. Mine." "That was the choice. Everything else burned afterward." (echo of Ch4).

*Lines 6000-6400, Ch15 end, Ch16.* Stansbury's burn: good. "Loss didn't care much about paperwork." flagged. The "Alive." / "The diary was gone." run is a staccato quartet. The young woman returns with chicken ("They're not as good."): moved.

*Lines 6400-6800, Ch16.* Milo and "He still owes me a hand": moved. The loss sheet: moved. Then the apology and the tribunal: respectable but legalistic; "Agreed" x5; Elizabeth's "I am not going to..." triple is machine-clean. "You inhaled like an advertisement": human.

*Lines 6800-7200, Ch16 end, Ch17.* "Elizabeth cried for Nana. / For Shade's..." triple. Mama Baga's "Person is the word I have for that." Ch17 is delightful: rulers, lemon, Susquehanna. Montage structure with some summarizing.

*Lines 7200-end, Ch17 end, Ch18.* The welcome-speech payoff ("more spaewife in it") and the goat: best stretch of the second half. The door is paid off. The Merritt cookbook delighted me. "I could have called someone. I didn't." and "That's not what I did." are the right size. The geese are great. The ending echoes Ch1 and works.

## Appendix B. Method note

I read only the brief and the manuscript, in order, in chunks of 400 lines (7,757 lines in all). I did not open any other file, folder, note or site. After the full read I ran word and phrase counts on the manuscript text (grep and a short Python script) to size the patterns above. The counts are line- or phrase-level and approximate. The "sections" count splits the book on blank-line gaps (79 sections, including chapter ends). Chapter One was not captured by the per-chapter density table because my split started at "Chapter Two", so my comments on Ch1 come from the read, not the numbers.