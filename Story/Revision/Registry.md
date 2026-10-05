# Registry: Pathwell

## Status

**Active. Book record, copied from the [Registry template](../Sunday-Morning/Registry.md) and adapted for one novel.** This page owns what the manuscript has already used: names, chapter shapes, devices, stock phrases and the watch patterns the checker counts. It keeps a revision pass from quietly repeating itself or introducing a clash. Created 2026-09-29 in [pass P1](Pass-Log.md).

For a novel, the template's "story" is a chapter, and a phrase shared by two chapters is often a deliberate callback rather than a tic. So the checker is run with a higher bar for shared phrases (`--min-files 3`), the deliberate callbacks are listed under [linked phrases](#checker-exceptions), and the book's own habits are counted as [watch patterns](#watch-patterns) rather than listed as stock phrases to remove.

Run it from the repository root. It reads the chapter files directly and never edits them:

```text
python3 Story/Sunday-Morning/tools/sunday_morning_check.py --registry Story/Revision/Registry.md --drafts Story/Chapters --pattern "Chapter_*.txt" --min-files 3
```

`Coda.txt` was retired to the [archive](../Archive/README.md) on 2026-09-30; its row below is kept as history.

**Update this page whenever a pass adds or renames a character, or changes a chapter's opening, engine, resolution or final line.** Keep the `<!-- registry:… -->` marker comments; the checker reads between them.

## Names

Every named person in the manuscript. The Story column is the chapter where the name first appears; the checker compares names across it, which for one book means "anywhere in the novel". Unnamed roles (the healer, the archivist, the shopkeeper, the curator, the bartender, the waitress, the woman in the knitted cap) are left out on purpose; see [devices](#devices-already-used).

<!-- registry:names:start -->
| Story | Name | Role | Kind |
| --- | --- | --- | --- |
| Ch01 | Elizabeth | viewpoint character; family name given in Ch4 but never printed | protagonist |
| Ch01 | Nana Jones | Elizabeth's grandmother, dead before Ch1; her first name is spoken in Ch4 but never printed | cast |
| Ch02 | Pathwell | practitioner; one name only ("Don't need one. Saves everybody time.") | cast |
| Ch04 | Mama Baga | head of Camp Cunnan; Pathwell's adoptive mother (not stated on the page) | cast |
| Ch04 | Olan | Camp; disputes the creek crossing (offstage) | minor |
| Ch04 | Hess | Camp; dead 22 years, still quoted in the road book | minor |
| Ch04 | Stansbury | Pathwell's older brother; imbues foam weapons | cast |
| Ch08 | Shade | made from Pathwell's failed prune | cast |
| Ch09 | Celia | in Shade's inherited memories ("hated pears") | minor |
| Ch10 | Ellison | estate whose unsent letters Stansbury keeps | minor |
| Ch10 | Leo | Stansbury's first name; only Pathwell uses it (the author's, P33) | cast |
| Ch11 | Margaret Bell | the museum's first curator | minor |
| Ch11 | Daniel Vale | Civil War letter writer, museum collection | minor |
| Ch11 | Henry Vale | Daniel's family; attic coat (Ch11), letter packet (Ch17) | minor |
| Ch11 | Sam | household notebook ("SAM HOME TODAY") | minor |
| Ch11 | Elsie | addressee of the quarantine letter | minor |
| Ch13 | Milo | Camp child ("the turnip boy", "the one-sock boy") until named | cast |
| Ch18 | Ruth Merritt | first name in the Merritt family cookbook | minor |
| Ch18 | Joanne Merritt Pike | Merritt cookbook | minor |
| Ch18 | Ellen Pike | Merritt cookbook | minor |
| Ch18 | Mara Pike Solis | Merritt cookbook | minor |
<!-- registry:names:end -->

### Name rules

The template's [name rules](../Sunday-Morning/Registry.md#name-rules) apply. For this book:

- **Crowded letters:** E (Elizabeth, Elsie, Ellen, Ellison), M (Mama Baga, Milo, Margaret, Mara, Merritt), S (Stansbury, Shade, Sam). Pick any new name from open letters: A, B, F, G, I, K, Q, T, U, V (Vale is taken), W, X, Y, Z.
- **Place names in use:** Camp Cunnan, the Space Between, the museum (unnamed town), Prague (in Pathwell's past). New places stay unnamed unless a scene needs the name.
- *Rename log:* none yet.
- *Expected checker notes:* the Vale family (Daniel, Henry) and the Merritt/Pike family share surnames on purpose. `Ell-` (Ellen, Ellison) and `Mar-` (Margaret, Mara) are minor names in different chapters; leave them unless a pass puts them on the same page.

## Chapter shapes

The book's variety lives here. Filled in from the manuscript as it stood at pass P1 (2026-09-29); update it whenever a pass changes an opening, engine, resolution or ending. POV is Elizabeth's unless noted. The [shape check in the assessment](Assessment-2026-09-29.md#chapter-shape-check) reads this table.

| Ch | Engine | Resolved by | Register | Opening | Final line |
| --- | --- | --- | --- | --- | --- |
| 1 | the guest who stayed, casually reading her diary after her welcome party, until the blob at the door makes him think it's there for her (P7, P7b) | an act (Elizabeth grabs the book) and flight | comic panic | "It was the crash that woke her." | "Ready?" / "No." / "Perfect." |
| 2 | Pathwell walks off with her books without noticing (Q118) | her realization: "He still has it." (R12; the author's July ending) | numb grief, comic, warm | dialogue ("Will you slow down!?") | "He still has it." |
| 3 | get the books back; the Space Between | a transaction (future paid through the tome, R29) | wonder, cost | Pathwell at a streetlight, the books under his arms (the author's opening, P16) | "Don't make anything of that." (her laugh; the choice to go on is told at the top of Ch4, R31) |
| 4 | arrival at Camp; the dying woman | a gift (the whole cookbook) | tender | "She had assumed…the word camp would mean something she could leave." | "Camp Cunnan kept being a place without asking permission." (she follows) |
| 5 | the portal to the school; meet Stansbury; the order of events | a question ("Was it?") | brisk comic | a field at dawn; the portal (the author's, P25) | "Elizabeth followed him inside." |
| 6 | the bar; the mirror (Pathwell POV section) | a realization ("Mine.") | warm, then uneasy | "The bar wasn't nearly as dingy as she'd imagined." (the author's, P28) | "Then, from the far side of the Cadillac, a thud. / Wet. Heavy." (cliffhanger; echoes Ch1's first thud) |
| 7 | blob takes Pathwell | an act (Elizabeth cuts him out); then being shut out | action, anger | "The smell reached Elizabeth before the shape did." | "For the first time since the apartment, nobody was telling Elizabeth where to go." |
| 8 | the withheld prune | an act (the deliberate crash); Shade arrives | defiance | "Elizabeth chose the ditch." | "Too late to call it an accident." |
| 9 | the diner | a conversation (Shade: "You were never the point") | quiet, sharp | "The radio glowed blue through the dark." | she walks back ("She had a question now, and this time she intended to make him answer it.") |
| 10 | the walk home and the tracking working (brothers' POV, the author's, P33); the Ask | a confession ("But you still chose it." / "Yes.") | brothers' banter, procedural, then bare | "She'd been walking for a little over an hour." | "Pathwell didn't correct the route." |
| 11 | the museum; the quarantine letter | a disaster (Pathwell acts against her no) | wonder, then catastrophe | "The drive took most of what was left of the night." | "Outside the high windows, it was daylight." |
| 12 | shoulder set; diary given | a gift (the diary) | recovery | "Camp Cunnan was awake enough to notice trouble and asleep enough to resent it." | she watches Camp wake, under Mama Baga's blanket (P37) |
| 13 | Shade becomes a person at Camp | a choice ("I want to stay here.") | warm, funny | "By full morning, Elizabeth was still by the central fire when Mama Baga stopped beside Shade…" (P38) | "Then the threshold opened." (cliffhanger) |
| 14 | the rejoining frame; her stance and the dagger left where it is (P39) | a forced act (Pathwell releases payment, against every no) | dread | "The threshold opened onto the unfinished hand of Hearts." | "And inside it, Milo shouted again." (cliffhanger) |
| 15 | the fire; Shade walks away | acts (Elizabeth saves Milo; Shade separates the signals) | grief | "Elizabeth reached the archive before the bucket line existed." | "Shade did not either." |
| 16 | aftermath; restitution terms | people (a hearing, a boundary: "Let it be.") | grief, dry | "The archive roof came down and Camp Cunnan kept moving." | "…for once Pathwell would not be the person deciding what those things were." |
| 17 | three weeks of restitution | behaviour over time (corrections accepted) | dry comic | "By the third morning, Pathwell had learned that restitution contained more rulers than magic." | "Not because she knew where she wanted to go yet. / Because she wanted to go." |
| 18 | a visit asked for; the Merritt cookbook | a refusal (he lifts his hand) and her invitation | light, wry | "Three weeks and four days after the archive burned, Elizabeth called Pathwell…" | "Are you ready?" / "No." / "Perfect." |
| Coda | Pathwell alone at the counter; a failed prune | an errand card | wry | "The Space Between smelled the same as it always had…" | "Are you ready?" she said. / "No," he said. / "Perfect." |

**Resolutions already used:** a transaction or a refused transaction on the ledger (3, 18); a gift of a record (4, 12); an act by Elizabeth (1, 7, 8, 15); a conversation or confession (9, 10); a disaster from Pathwell overriding a no (11, 14).

## Devices already used

Reuse one only on purpose, and never in the next chapter. Counts are from pass P1; see the [assessment](Assessment-2026-09-29.md) for where each sits.

| Device | Where |
| --- | --- |
| Elizabeth follows Pathwell as the chapter's last beat | 1, 2, 3, 4, 5; paid off deliberately in 8 ("following another man who sounded certain") and inverted in 18 |
| Motive-list close: "Not because X. Not because Y. Because Z." | 2, 4, 9, 17 (Chapter 12's removed in P4) |
| "For the first time since…" / "For once…" as a closing turn | 4, 7, 16, 17 |
| The world goes on "without asking permission" | 4, 16, 18 |
| Opening on a personified place or group | 6, 12 (and a similar witty verdict in 17; 11 and 13 changed in P36/P38) |
| A drink that "was terrible" | 3, 4, 9, 13, 18 |
| Milo's falling sock | 4, 12, 13, 14, 15, 16 |
| "Lizzy—" / "Elizabeth." correction | he hears it in Nana's echo in 1 (R21; the banner reads WELCOME ELIZABETH); first said in 2; corrected in 3, 7, 8, 10, 14; inverted in 16 ("He did not say Lizzy.") |
| The Space Between coffee memory recited ("late nights spent studying") | 3, 9, 10, 13, 18 |
| Pathwell goes still as a tell | 1, 4, 5, 6, 7, 8, 10, 11 and later |
| A found document read aloud as a small payoff (accession card, road book, Merritt margins) | 4, 11, 17, 18 |
| Unnamed functional roles (healer, archivist, shopkeeper, curator) | throughout; deliberate, but see [Open for the author](Decisions.md#open-for-the-author) on the healer |
| Rhymed choices: "It was an absurdly small decision. / It was still hers." → "The choice was ridiculous. / It was still hers." | 2 → 17 |
| Rhymed choices: "That was the choice. / Everything afterward was consequence." → "…Everything else burned afterward." | 4 → 15 |
| The ledger payment and its mirror | 3 → 18 (and Coda) |

## Joke shapes already used

A joke's *construction* repeats even when its words don't. The words can differ while the reader still sees the mold. Added in [pass P5](Pass-Log.md#p5-2026-09-30-craft-adjustments-and-ai-tells) ([Writing against sameness](Writing-Against-Sameness.md)). Try not to repeat a shape within a chapter unless it's deliberate. The counts are from the chapters as of P5.

| Shape | Where |
| --- | --- |
| Narrator's "as if / as though X were…" conceit ("breathed as though breathing were the only task she had agreed to perform") | 2, 4 (×2), 6, 7, 9, 12 (×2); the checker's count also catches plainer uses (1, 2, 3) |
| "…nodded as though X were Y" (a reaction read as a category or verdict) | 6 ("as though this were enough information"), 12 (×2, "a medically useful category", "a recognized injury category") |
| "X is a category" (injuries, museums, Pathwell) | 12 (×2, since P37) |
| Objects and places given human verbs in narration (a sock "surrendered", a fiddle "rejected" notes, a realization "arrived", body parts "deciding"). Some of this is the narrator's sanctioned attitude ("as if it had personally disappointed him", [register guide](../Story_Files/pathwell_narrator_register.md#the-grammar-of-narrator-attitude)); density is the concern | throughout; body parts are counted as a [watch pattern](#watch-patterns), the rest by reading. "One sock had surrendered halfway down his calf" is word for word in both 4 and 12 |
| Formal phrasing used as a punchline in dialogue ("Efficient system." "Diversifying." "Strong sales pitch." "Important distinction.") | throughout, across most of the cast; see the [character bible's humour sources](../Story_Files/character_bible.md#where-each-characters-humour-comes-from) |
| Two-part antithesis as a scene's last word ("The diary belonged to Camp now. The life in its pages was still hers.") | throughout; count by reading; usually no more than one per scene |

## Stock phrases to avoid

The template's list, which the checker reports if any appear. The book's own habits are counted separately as [watch patterns](#watch-patterns), because most of them are right some of the time and the question is density, not presence.

<!-- registry:stock:start -->
- wrote it down
- nobody said so
- delighted to be asked
- for thirty years
- for the first time in his life
- for the first time in her life
- the way you might
<!-- registry:stock:end -->

## Watch patterns

Counted per 1,000 words of narration (dialogue removed) unless the line ends `:: all`. They measure the watch-list items in [Craft](../Sunday-Morning/Craft.md#the-authors-watch-list) and the habits the [cold read](Cold-Read-2026-09-29.md#repeated-habits-across-chapters) found. A count is a pointer for reading, not a verdict.

<!-- registry:watch:start -->
- paragraphs opening "Not…" or "No…" (fragment rhythm) :: ^(?:Not|No)\b[^\n]{0,80}$
- evaluative follow-up ("That mattered." "That helped.") :: \bThat (?:mattered|helped|was (?:also )?(?:new|useful|information|enough|pleasant|important))\b
- reversal beat ("That made it worse.") :: \bThat (?:made (?:it|her|him|the choice) \w+|was almost the worst part|should have (?:helped|been satisfying))|\bWhich was worse\b
- "for the first time" / "for once" :: (?i)\bfor (?:the first time|once)\b
- body parts deciding :: (?i)\b(?:knees?|legs?|body|stomach|shoulder|feet|hands?)\b[^.\n]{0,40}\b(?:decided|decision|decisions|objected|participating|consulting|punished)\b
- "without asking permission" :: (?i)without (?:asking (?:permission|whether)|anyone's permission)
- narrator's "apparently" :: (?i)\bapparently\b
- narrator's "as if / as though X were…" :: (?i)\bas (?:if|though)\b[^.\n]{0,60}\b(?:were|was)\b
- "category" joke :: (?i)\bcategor(?:y|ies)\b :: all
- stock gestures common in AI fiction (see AI-Tells) :: (?i)\bswallowed\b|\bjaw (?:tightened|clenched|set)\b|\beyes widened\b|\bheart (?:hammered|pounded|raced)\b|\b(?:let out|released) a breath\b|\bshiver\w* (?:ran )?down\b|\bsmile play\w*|\bghost of a smile\b|\bdidn't quite smile\b
- going still :: (?i)\b(?:went|gone|go|goes|going|became|become|stood|remained)\s+(?:very |completely |abruptly )?still\b
- choice words (theme density) :: (?i)\b(?:choice|choices|chose|choose|chosen|choosing)\b
- "it was terrible" (drink gag) :: (?i)\bIt was terrible\b|\bThat(?:'s| is) terrible\b :: all
- "Fair." as a reply :: "Fair[.?!]" :: all
- "difficult night / morning" :: (?i)difficult (?:night|morning|evening) :: all
- "Lizzy" :: Lizzy :: all
- bureaucratic imagery :: (?i)\badministrative\b|\bpaperwork\b|\bbureaucra
- "noticed that too" / "saw that too" :: (?i)\b(?:noticed|saw)(?: that| it)? too\b
- "mouth moved at one corner" (stock gesture, or a family tell shared by Mama Baga, Shade and Pathwell? for the author, P4) :: (?i)mouth (?:moved|twitched) at one corner|mouth moved\b :: all
- commentary paragraph (a short line that evaluates the beat just shown) :: ^(?:That|This|It was|Which|For once|Neither|There it was|Good\.|Elizabeth (?:appreciated|liked|noticed|understood|believed|approved|found|realized|knew|felt)|She (?:believed|appreciated|understood|resented|hated|knew)|The (?:answer|sentence|word|question|correction|distinction))\b[^\n]{0,90}$
<!-- registry:watch:end -->

Also watch for, by reading (the checker can't catch them):

- explanation after showing: a short narration paragraph after a beat that names what the beat meant;
- the narrator grading a line of dialogue ("The sentence changed the room." "That saved it.");
- one shared deadpan: lines that could be swapped between Pathwell, Stansbury, Shade, the archivist and the shopkeeper;
- a chapter ending on the same kind of beat as the one before it (see [shapes](#chapter-shapes)).
- the same joke shape twice in one chapter (see [joke shapes](#joke-shapes-already-used));
- a line of wit given to a minor character or to Shade that belongs to the narrator's or the shared deadpan;
- several polished closing lines in one scene ([Writing against sameness](Writing-Against-Sameness.md#while-writing));
- anything that clusters from the [AI-Tells](AI-Tells.md) list.

## Checker exceptions

**Allowed stock phrases:** none.

<!-- registry:allow:start -->
| Story file | Phrase | Reason |
| --- | --- | --- |
| Chapter_04 | wrote it down | the archivist literally records the donation |
| Chapter_04 | for thirty years | literal ("may not touch it for thirty years"; the sage "spending thirty years inside a wagon") |
| Chapter_09 | wrote it down | the waitress takes the order |
<!-- registry:allow:end -->

**Linked phrases:** deliberate callbacks and recurring documents. The checker ignores five-word phrases that contain any of these.

<!-- registry:linked:start -->
- low tide
- wet rot
- ready
- perfect
- that hand was promising
- that was the choice
- it was still hers
- more if they're sick
- sam home today
- call electric
- buy boxes
- find nana's spoon
- south bank after three days
- hess says
- ruth lied about the lard
- queen of spades
- late nights spent studying
- it's the useful version
- wouldn't dream of it
- one sock had surrendered
- the whole book
- the space between
- camp cunnan
<!-- registry:linked:end -->
