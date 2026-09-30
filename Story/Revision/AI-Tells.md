# AI tells: what to be aware of

## Status

**Reference, active. Created 2026-09-30 in [pass P5](Pass-Log.md#p5-2026-09-30-craft-adjustments-and-ai-tells).** This page collects what research, editors and readers report as common features of AI-generated fiction. Each is set against what this book's own guides say. It follows the author's ruling ([R18](Decisions.md#the-authors-rulings-for-this-revision)): *"obviously we dont need to adheare to every. single. rule. but it does help to be aware of what is maybe a common occurrence or staples of AI writing… The goal isnt to deceive but just provide the best product we can that matches the guide and stlye we have in place now."*

So this is awareness, not a rulebook:

- **The book's guides decide.** Where a tell overlaps something the author does on purpose (body-first interiority, smell, fragments for percussion, "mostly"), his [voice guide](../Sunday-Morning/Sources/Voice-Guide.md), [prose voice](../Story_Files/pathwell_prose_voice.md) and [narrator register](../Story_Files/pathwell_narrator_register.md) win.
- **Look for density, not presence.** Every item below is a legitimate technique that human writers use. The sources agree that what gives AI away is using them reflexively, at every opportunity, and in clusters: "the signal lies not in any one tell but in the clustering of them" ([Vollmer](#sources)); in models, "what should be a rhetorical 'special effect' ends up being used so frequently that it loses its special character and becomes monotonous" ([Gorrie](#sources)).
- **Never make the prose worse to avoid a tell.** No typos, filler, synonym swapping or random fragments.
- **A detector score is not a target** ([R17](Decisions.md#the-authors-rulings-for-this-revision)).

How a pass uses this page: [Writing against sameness](Writing-Against-Sameness.md). The ones a pattern can count are in the Registry's [watch patterns](Registry.md#watch-patterns).

## What the manuscript shows

The Chapter 12 detector read, the cold read and a count across the eighteen chapters (about 48,000 words) point the same way. **The vocabulary tells are almost absent. The structural ones are everywhere.**

- **Almost absent:** "delve", "tapestry", "testament", "a mix of", "something shifted", silence that "settled" or "stretched", "eyes widened", "barely above a whisper". Em dashes are few (about one per 1,000 words).
- **Present at a low level:** stock gestures ("swallowed" 11 times, "jaw tightened/set" 8 times, about half of them in Chapters 7–9). "The corner of the mouth moved" appears 8 times, but that may be a family tell ([ledger R17](Promise-Ledger.md#relationships-and-running-elements)).
- **Everywhere:** the rewrite's habits are the structural and story-level items below. Explanation after showing, "Not X. / Y." antithesis, polished closing lines, one shared deadpan, narrator conceits, and self-diagnosing interiority. This is what the [checker](README.md#after-every-pass) and the [fresh check](Writing-Against-Sameness.md#after-writing) should watch.

## Story level

StoryScope compared 10,272 published human stories (from Books3) with stories written from the same premises by five models, including Claude. It found the differences run deeper than style: narrative choices alone separated human from AI stories with a 93% macro-F1 ([Russell et al., 2026](#sources)). Of the five, Claude's "narrative voice is the most uniform".

| Tell | What the research found | In Pathwell |
| --- | --- | --- |
| **The narrator explains the theme** | "Narrators explicitly explain the story's theme 77% of the time, versus 52% for humans"; AI stories are "more explicit and moralizing" | Already a fault here: the Thesis page's test ("If a character says the theme out loud, it's failed"), [prose voice](../Story_Files/pathwell_prose_voice.md#sentence-level-faults) "Thesis statement as prose fault". The commentary-paragraph count is its measure |
| **Resolution by understanding** | "AI resolutions favor internal understanding or acceptance (47% vs. 27%), whereas humans are more comfortable with ambiguous endings" | The locks keep real ambiguity: the prune's content stays open, "It was my fault" stands unexplained, and Pathwell chooses not to find out whether he can still prune. Protect those. Watch for scene endings that resolve into a realization ("She knew it better now.") |
| **The protagonist resolves it** | "more protagonist-driven resolutions (69% vs. 46%)" | The interview locked Elizabeth as witness in the confrontation, and the climax is still open ([Q-E](Decisions.md#open-for-the-author)). Worth knowing when the options are weighed: a choice that neatly resolves everything is also a default |
| **Few subplots, tight causal chains** | "far fewer subplots (79% 'no subplots' vs. 57%)"; tighter causal chains | Camp's ordinary life, Stansbury, the meeting and Milo are the book's texture. Don't trim them away as "not causal" |
| **Flat escalation, quiet endings, epilogues** | for Claude, "event intensity escalates less than in any other source"; it "favor[s] quiet endings" and epilogues | A known risk for the back third (the cold read found it slowing). Chapter 18 is the author's ending, so this is not a reason to change it |
| **Conventions honoured, not subverted** | Claude honours conventions in 62% of stories (39–56% for the other sources) | The book's wrong-detail responses and irreverence are its subversions. Keep them the characters' own |
| **Emotion through the body; smell** | AI "conveys emotion through physical sensations and bodily metaphors (81% vs. 38% human)" and uses "more smell-based imagery (82% vs. 57%)"; "Humans use explicit emotion labels 29% of the time versus just 8% for AI" | **The one real tension.** Body-first interiority and smell are the author's own signature, in his benchmark Chapters 1–2 (the sugar-cookie scene, "a stench of low tide"). Keep them; the guides also rule out naming feelings outright ("She felt sad." Cut: narrator register). What's worth watching is only that the body doesn't become the one vehicle for every feeling. Vary it: an object carrying grief (the voice guide), a wrong-detail response, or one narrator line for what Elizabeth hasn't named yet (narrator register) |

## Scene and paragraph level

| Tell | What it looks like | Where it's named | In Pathwell |
| --- | --- | --- | --- |
| **Aphoristic closure** | a paragraph or scene ending on a pull-quote: "the sentence has the *shape* of wisdom without its friction" | Vollmer; Wikipedia ("compulsive summaries") | [Usually one polished closing line per scene](Writing-Against-Sameness.md#while-writing), the one that's earned |
| **Negated contrast, "It's not X, it's Y"** | "The pull from the deep was no current. It was a summons." | Wikipedia; Gorrie; Antislop (up to 6.3× the human rate in some models); Slop Score weights it at 25% | Counted: "Not…/No…" paragraphs; P4 took Chapter 12 from 11 to 0 |
| **Rule of three** | three parallel items of equal weight, again and again | Wikipedia; Gorrie; Record Crash | Watch by reading: list-of-three descriptions, triple fragments ("Fast. Simple. Effective.") |
| **Explaining what was shown** | "Unnecessary/redundant exposition" was 18% of professional writers' edits to AI fiction | Chakrabarty et al. (LAMP) | The scene diagnostic's question 4; the commentary count |
| **Uniform rhythm** | a metronomic sentence length; or in fiction, the "short, short, polished capstone" pattern | Vollmer ("low burstiness"); the handoff | Vary on purpose: long uneven sentences, paragraphs with no punchline |
| **Pacing flatness** | every beat at the same speed; no summary, no elision | Vollmer | Let small things go by in a line ("They ate."); spend space where it matters |
| **Flattened dialogue** | "characters sound alike; no distinct idiolect. No one has verbal tics, dialect, or pattern of evasion" | Vollmer; voice guide ("everyone sharing the same sense of humor") | [Whose joke is it](../Story_Files/character_bible.md#where-each-characters-humour-comes-from) |
| **As-you-know-Bob exposition** | characters explaining the world to each other | Vollmer; voice guide | Mostly gone (cold read); the Ask in Chapter 10 repeats its facts |
| **Setting that mirrors feeling** | "rain pattered softly against the window, mirroring her unspoken grief" | Vollmer | [Prose voice 7](../Story_Files/pathwell_prose_voice.md#7-ambient-atmosphere-without-commentary): "Cut the 'a reminder.' The image is the reminder." |
| **Missing concrete particular** | no specific Tuesday, laundromat or grandmother | Vollmer; LAMP ("lack of specificity") | The author's strength ("It's Thursday."; the dry cleaning; the spoon). Keep particulars particular |
| **Every detail optimized** | every object is a symbol, a callback or a setup | the handoff | [Some texture is just texture](Writing-Against-Sameness.md#while-writing) |
| **Personification as literary shortcut** | objects and abstractions doing human things: "silence settled", a sock "surrendered" | the handoff; Symban | Some of it is the narrator's sanctioned attitude: the [register guide](../Story_Files/pathwell_narrator_register.md#the-grammar-of-narrator-attitude) lists "as if it had personally disappointed him". Only density is the concern. Counted in part (body parts "deciding"); the rest are in [joke shapes](Registry.md#joke-shapes-already-used) |

## Sentence and word level

| Tell | Examples | Where it's named | In Pathwell |
| --- | --- | --- | --- |
| **Stock gestures** | a shiver down the spine, heart hammered, jaw tightened, swallowed hard, eyes widened, a smile played on her lips, the breath she didn't know she was holding | Symban; Antislop (in one model's output: "heart hammered ribs" 1,192×; also "took deep breath", "smile playing lips") | "Swallowed" 11, "jaw tightened/set" 8: counted as a [watch pattern](Registry.md#watch-patterns) |
| **Over-used words** | shimmered, flickered, gaze, unsettlingly, stammered, muttered; delve, tapestry, testament, pivotal, intricate | Antislop (in one model's output: "shimmered" 2,882×, "unsettlingly" 3,833×); Wikipedia; Vollmer | Nearly absent (4 of shimmered/flickered/gaze); keep it that way |
| **Stock constructions** | "the weight of [adjective] [noun]"; "a mix of [noun] and [noun]" | Chakrabarty et al. (LAMP) | One "the weight of" (Ch1, and literal) |
| **Participial tail** | a trailing "-ing" phrase that restates the clause: "…, underscoring its importance" | Vollmer; Wikipedia | Watch by reading |
| **Incoherent or abstract metaphor** | "smiled like sunrise over a sink"; "collect your griefs like stones in your pockets" (Nostalgebraist, quoted in The Argument): images that "sound vaguely pleasing but are logically incoherent" | The Argument; Record Crash ("eyeball kicks") | Metaphor is a cautious category (voice guide). A suggestion, not a guide rule: a figure that comes from the character's world tends to hold up; one that doesn't is worth questioning |
| **Em-dash overuse** | dashes used for every added clause | Wikipedia; Vollmer; StoryScope's press coverage | About 1 per 1,000 words here; fine |
| **Too clean** | no contractions, perfect grammar, no informal slips | Vollmer | [Write how people talk](../Sunday-Morning/Craft.md#write-how-people-talk). Contractions in narration; "polish should improve communication, not sterilize personality" (voice guide) |
| **Stock names** | "Elara" appears 85,513× more often than in human text (in one model's output) | Antislop | Not an issue: the names are the author's |

## Sources

- Wikipedia, [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WikiProject AI Cleanup), read through the summary at [Beutler Ink](https://www.beutlerink.com/blog/how-to-spot-ai-writing). Negative parallelisms, rule of three, em dashes, "cursed vocabulary", false ranges, compulsive summaries. It notes that humans use some of these too.
- Chakrabarty, T. et al., [Can AI writing be salvaged? Mitigating idiosyncrasies and improving human-AI alignment in the writing process through edits](https://arxiv.org/abs/2409.14509) (CHI 2025). Eighteen MFA-trained writers edited 1,057 AI paragraphs, making 8,035 edits (the LAMP corpus). Edit categories: awkward word choice 28%, poor sentence structure 20%, unnecessary exposition 18%, cliché 17%, plus purple prose, lack of specificity and tense inconsistency. The same patterns showed up across GPT-4o, Claude 3.5 Sonnet and Llama 3.1.
- Paech, S. et al., [Antislop: a comprehensive framework for identifying and eliminating repetitive patterns in language models](https://arxiv.org/pdf/2510.15061) (2025). Word and n-gram over-representation against human text (the largest ratios are from single models); "It's not X, it's Y" up to 6.3× in some models. See also the [Slop Score](https://eqbench.com/slop-score.html) (slop words, not-X-but-Y, trigrams).
- Russell, Rajendhran, Pham, Iyyer and Wieting, [StoryScope](https://arxiv.org/html/2604.03136) (University of Maryland and Google DeepMind, 2026). Narrative-level differences between human and AI fiction; the percentages above are quoted from it. Press summary: [IBM Think](https://www.ibm.com/think/news/ai-fiction-stories-share-common-quirks-study-says).
- Gorrie, C., [Why ChatGPT writes like that](https://www.deadlanguagesociety.com/p/rhetorical-analysis-ai). Parallelism, antithesis and tricolon as legitimate devices overused without taste.
- Vollmer, M., [I asked the machine to tell on itself: a field guide to AI tells](https://matthewvollmer.substack.com/p/i-asked-the-machine-to-tell-on-itself). Lexical, syntactic, rhetorical, tonal and fiction-specific tells; clustering over single signs.
- Makin, [How to identify AI-written web fiction](https://recordcrash.substack.com/p/how-to-identify-ai-written-web-fiction) (Record Crash). Repeated sentence shapes, "Not X; Y", lists of three, stagnant vocabulary, "eyeball kicks".
- Symban, [Why AI novels often sound the same, and how to avoid it](https://symban.de/en/blog/ai-novels-sound-same-how-to-avoid). Stock gestures, atmosphere, dialogue habits.
- [The literary world is sleepwalking into an AI disaster](https://www.theargumentmag.com/p/the-literary-world-is-sleepwalking) (The Argument). Incoherent and abstract-to-concrete metaphors, including lines it quotes from Nostalgebraist.
- NousResearch, [autonovel ANTI-SLOP.md](https://github.com/NousResearch/autonovel/blob/master/ANTI-SLOP.md). A general (not fiction-specific) banned-word and structure list.
- The author's GPTZero handoff, in [AI detection notes](AI-Detection-Notes-2026-09-30.md#the-handoff-as-the-author-gave-it).
