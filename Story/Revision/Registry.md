# Registry: Pathwell

## Status

**Active. Book record, copied from the [Registry template](../Sunday-Morning/Registry.md) and adapted for one novel.** This page owns what the manuscript has already used: names, chapter shapes, devices, stock phrases and the watch patterns the checker counts. It keeps a revision pass from quietly repeating itself or introducing a clash. Created 2026-09-29 in [pass P1](Pass-Log.md).

For a novel, the template's "story" is a chapter, and a phrase shared by two chapters is often a deliberate callback rather than a tic. So the checker is run with a higher bar for shared phrases (`--min-files 3`), the deliberate callbacks are listed under [linked phrases](#checker-exceptions), and the book's own habits are counted as [watch patterns](#watch-patterns) rather than listed as stock phrases to remove.

Run it from the repository root. It reads the chapter files directly and never edits them:

```text
python3 Story/Sunday-Morning/tools/sunday_morning_check.py --registry Story/Revision/Registry.md --drafts Story/Chapters --pattern "Chapter_*.txt" --min-files 3
```

Add `Coda.txt` to a run with `--pattern "*.txt"` while [its status](Decisions.md#open-for-james) is undecided.

**Update this page whenever a pass adds or renames a character, or changes a chapter's opening, engine, resolution or final line.** Keep the `<!-- registry:… -->` marker comments; the checker reads between them.

## Names

Every named person in the manuscript. The Story column is the chapter where the name first appears; the checker compares names across it, which for one book means "anywhere in the novel". Unnamed roles (the healer, the archivist, the shopkeeper, the curator, the bartender, the waitress, the woman in the knitted cap) are left out on purpose; see [devices](#devices-already-used).

<!-- registry:names:start -->
| Story | Name | Role | Kind |
| --- | --- | --- | --- |
| Ch01 | Elizabeth | viewpoint character; family name given in Ch4 but never printed | protagonist |
| Ch01 | Nana Jones | Elizabeth's grandmother, dead before Ch1; her first name is spoken in Ch4 but never printed | cast |
| Ch02 | Pathwell | practitioner; "also Pathwell, if the situation becomes formal" | cast |
| Ch04 | Mama Baga | head of Camp Cunnan; Pathwell's adoptive mother (not stated on the page) | cast |
| Ch04 | Olan | Camp; disputes the creek crossing (offstage) | minor |
| Ch04 | Hess | Camp; dead 22 years, still quoted in the road book | minor |
| Ch04 | Stansbury | Pathwell's older brother; imbues foam weapons | cast |
| Ch08 | Shade | made from Pathwell's failed prune | cast |
| Ch09 | Celia | in Shade's inherited memories ("hated pears") | minor |
| Ch10 | Ellison | estate whose unsent letters Stansbury keeps | minor |
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
| 1 | intrusion; the blob at the door | an act (Elizabeth grabs the book) and flight | comic panic | "It was the crash that woke her." | "Ready?" / "No." / "Perfect." |
| 2 | Pathwell walks off with her books | her choice to follow | numb grief, comic | dialogue ("Will you slow down?") | follows him (motive list: "Not because… Because…") |
| 3 | get the books back; the Space Between | a transaction (future paid on the ledger) | wonder, cost | Pathwell at a streetlight, "Again." | "The shopkeeper closed the door behind them." (she goes with him) |
| 4 | arrival at Camp; the dying woman | a gift (the whole cookbook) | tender | "She had assumed…the word camp would mean something she could leave." | "Camp Cunnan kept being a place without asking permission." (she follows) |
| 5 | meet Stansbury; the order of events | a question ("Was it?") | brisk comic | Pathwell on a Cadillac hood | "Elizabeth followed the brothers inside." |
| 6 | the bar; the mirror (Pathwell POV section) | a realization ("Mine.") | warm, then uneasy | "The bar was neater than it had any right to be." | "Low tide. / Wet rot." (cliffhanger) |
| 7 | blob takes Pathwell | an act (Elizabeth cuts him out); then being shut out | action, anger | "The smell reached Elizabeth before the shape did." | "For the first time since the apartment, nobody was telling Elizabeth where to go." |
| 8 | the withheld prune | an act (the deliberate crash); Shade arrives | defiance | "Elizabeth chose the ditch." | "Too late to call it an accident." |
| 9 | the diner | a conversation (Shade: "You were never the point") | quiet, sharp | "The radio glowed blue through the dark." | she walks back ("Not because… Because she had a question now.") |
| 10 | the tracking working; the Ask (brothers' POV section) | a confession ("But you still chose it." / "Yes.") | procedural, then bare | "The road had the quality of roads in early morning…" | "Pathwell did not correct the route." |
| 11 | the museum; the quarantine letter | a disaster (Pathwell acts against her no) | wonder, then catastrophe | "The museum was a Civil War building on the edge of a town…" | "Outside the high windows, morning finally committed to daylight." |
| 12 | shoulder set; diary given | a gift (the diary) | recovery | "Camp Cunnan was awake enough to notice trouble and asleep enough to resent it." | "For the first time since the museum…" then she watches Camp wake |
| 13 | Shade becomes a person at Camp | a choice ("I want to stay here.") | warm, funny | "By full morning, Camp Cunnan had decided Shade was neither an emergency nor an explanation." | "Then the threshold opened." (cliffhanger) |
| 14 | the rejoining frame | a forced act (Pathwell releases payment) | dread | "The threshold opened onto the unfinished hand of Hearts." | "And inside it, Milo shouted again." (cliffhanger) |
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
| Motive-list close: "Not because X. Not because Y. Because Z." | 2, 4, 9, 17 (and near the end of 12) |
| "For the first time since…" / "For once…" as a closing turn | 4, 7, 12, 16, 17 |
| The world goes on "without asking permission" | 2, 4, 16, 18 |
| Opening on a personified place or group | 6, 11, 12, 13 (and a similar witty verdict in 17) |
| A drink that "was terrible" | 3, 4, 9, 12, 13, 18 |
| Milo's falling sock | 4, 12, 13, 14, 15, 16 |
| "Lizzy—" / "Elizabeth." correction | 3, 7, 8, 10, 14; inverted in 16 ("He did not say Lizzy.") |
| The Space Between coffee memory recited ("two in the morning", "highlighters") | 3, 9, 10, 13, 18 |
| Pathwell goes still as a tell | 1, 4, 5, 6, 7, 8, 10, 11 and later |
| A found document read aloud as a small payoff (accession card, road book, Merritt margins) | 4, 11, 17, 18 |
| Unnamed functional roles (healer, archivist, shopkeeper, curator) | throughout; deliberate, but see [Open for James](Decisions.md#open-for-james) on the healer |
| Rhymed choices: "It was an absurdly small decision. / It was still hers." → "The choice was ridiculous. / It was still hers." | 2 → 17 |
| Rhymed choices: "That was the choice. / Everything afterward was consequence." → "…Everything else burned afterward." | 4 → 15 |
| The ledger payment and its mirror | 3 → 18 (and Coda) |

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

Counted per 1,000 words of narration (dialogue removed) unless the line ends `:: all`. They measure the watch-list items in [Craft](../Sunday-Morning/Craft.md#jamess-watch-list) and the habits the [cold read](Cold-Read-2026-09-29.md#repeated-habits-across-chapters) found. A count is a pointer for reading, not a verdict.

<!-- registry:watch:start -->
- paragraphs opening "Not…" or "No…" (fragment rhythm) :: ^(?:Not|No)\b[^\n]{0,80}$
- evaluative follow-up ("That mattered." "That helped.") :: \bThat (?:mattered|helped|was (?:also )?(?:new|useful|information|enough|pleasant|important))\b
- reversal beat ("That made it worse.") :: \bThat (?:made (?:it|her|him|the choice) \w+|was almost the worst part|should have (?:helped|been satisfying))|\bWhich was worse\b
- "for the first time" / "for once" :: (?i)\bfor (?:the first time|once)\b
- body parts deciding :: (?i)\b(?:knees?|legs?|body|stomach|shoulder|feet|hands?)\b[^.\n]{0,40}\b(?:decided|decision|decisions|objected|participating|consulting|punished)\b
- "without asking permission" :: (?i)without (?:asking (?:permission|whether)|anyone's permission)
- narrator's "apparently" :: (?i)\bapparently\b
- going still :: (?i)\b(?:went|gone|go|goes|going|became|become|stood|remained)\s+(?:very |completely |abruptly )?still\b
- choice words (theme density) :: (?i)\b(?:choice|choices|chose|choose|chosen|choosing)\b
- "it was terrible" (drink gag) :: (?i)\bIt was terrible\b|\bThat(?:'s| is) terrible\b :: all
- "Fair." as a reply :: "Fair[.?!]" :: all
- "difficult night / morning" :: (?i)difficult (?:night|morning|evening) :: all
- "Lizzy" :: Lizzy :: all
- bureaucratic imagery :: (?i)\badministrative\b|\bpaperwork\b|\bbureaucra
- "noticed that too" / "saw that too" :: (?i)\b(?:noticed|saw)(?: that| it)? too\b
- "mouth moved at one corner" (stock gesture) :: (?i)mouth (?:moved|twitched) at one corner|mouth moved\b :: all
- commentary paragraph (a short line that evaluates the beat just shown) :: ^(?:That|This|It was|Which|For once|Neither|There it was|Good\.|Elizabeth (?:appreciated|liked|noticed|understood|believed|approved|found|realized|knew|felt)|She (?:believed|appreciated|understood|resented|hated|knew)|The (?:answer|sentence|word|question|correction|distinction))\b[^\n]{0,90}$
<!-- registry:watch:end -->

Also watch for, by reading (the checker can't catch them):

- explanation after showing: a short narration paragraph after a beat that names what the beat meant;
- the narrator grading a line of dialogue ("The sentence changed the room." "That saved it.");
- one shared deadpan: lines that could be swapped between Pathwell, Stansbury, Shade, the archivist and the shopkeeper;
- a chapter ending on the same kind of beat as the one before it (see [shapes](#chapter-shapes)).

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
- two in the morning
- highlighters
- it's the useful version
- wouldn't dream of it
- one sock had surrendered
- the whole book
- the space between
- camp cunnan
<!-- registry:linked:end -->
