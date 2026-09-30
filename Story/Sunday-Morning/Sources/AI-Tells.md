# AI tells: what to be aware of

## Status

**Writing reference: a general guideline for Sunday Morning stories in any setting. Researched 2026-09-30 during the Pathwell revision ([D18](../Decisions.md#standing-rulings)).** This page collects what research, editors and readers report as common features of AI-generated fiction. Each one is set against what the author's [voice guide](Voice-Guide.md) and [Craft](../Craft.md) already say. The author's words: *"obviously we dont need to adheare to every. single. rule. but it does help to be aware of what is maybe a common occurrence or staples of AI writing that we can avoid or at least be aware of. The goal isnt to deceive but just provide the best product we can that matches the guide and stlye we have in place now."*

So this is awareness, not a rulebook:

- **The guides decide.** Where a tell overlaps something the author does on purpose (the body knowing before the mind, smell, fragments for danger and comic timing), the [voice guide](Voice-Guide.md) and the setting's own voice notes win.
- **Look for density, not presence.** Every item below is a legitimate technique that human writers use. The sources agree that what gives AI away is using them reflexively and in clusters. "The signal lies not in any one tell but in the clustering of them" ([Vollmer](#sources)). In models, "what should be a rhetorical 'special effect' ends up being used so frequently that it loses its special character and becomes monotonous" ([Gorrie](#sources)).
- **Never make the prose worse to avoid a tell.** No typos, filler, synonym swapping or random fragments. The voice guide's "Imperfection" section is about humanity, not about errors.
- **A detector score is not a target** ([D17](../Decisions.md#standing-rulings)).

How a pass uses this page: [Craft: writing against sameness](../Craft.md#writing-against-sameness). Tells a pattern can count go into a collection's Registry as [watch patterns](../Registry.md#watch-patterns-optional). How one book applied it, with counts: [AI tells in Pathwell](../../Revision/AI-Tells.md).

**The finding that matters most.** In the Pathwell revision, the vocabulary tells were almost absent. The structural ones were everywhere: explanation after showing, "Not X. / Y." antithesis, polished closing lines, one shared deadpan, narrator conceits in every paragraph, and interior thought that diagnoses itself. A pass that only checks word lists will miss what actually gives AI prose away.

## Story level

StoryScope compared 10,272 published human stories (from Books3) with stories written from the same premises by five models, including Claude. It found the differences run deeper than style: narrative choices alone separated human from AI stories with a 93% macro-F1 ([Russell et al., 2026](#sources)). Of the five, Claude's "narrative voice is the most uniform".

| Tell | What the research found | What the guides already say |
| --- | --- | --- |
| **The narrator explains the theme** | "Narrators explicitly explain the story's theme 77% of the time, versus 52% for humans"; AI stories are "more explicit and moralizing" | "question → character choice → consequence" over "question → speech explaining the theme" (voice guide); [Craft 13](../Craft.md#13-theme-through-action-not-speeches-carries-over) |
| **Resolution by understanding** | "AI resolutions favor internal understanding or acceptance (47% vs. 27%), whereas humans are more comfortable with ambiguous endings" | Leave deliberate ambiguity alone ([Pipeline](../Pipeline.md#after-every-pass)); [Craft 9](../Craft.md#9-incomplete-answers-need-a-human-reason-carries-over) |
| **The protagonist resolves it** | "more protagonist-driven resolutions (69% vs. 46%)" | Worth knowing when a climax is chosen: a choice that neatly resolves everything is also a default |
| **Few subplots, tight causal chains** | "far fewer subplots (79% 'no subplots' vs. 57%)"; tighter causal chains | "Quiet scenes are not filler" (voice guide); [Craft 3](../Craft.md#3-every-scene-changes-something-or-makes-a-later-change-matter-adapted): enjoying the characters is a job a scene can do |
| **Flat escalation, quiet endings, epilogues** | For Claude, "event intensity escalates less than in any other source"; it "favor[s] quiet endings" and epilogues | "movement → interruption → reaction → breathing room → … → renewed movement" (voice guide). Check that the movement actually renews |
| **Conventions honoured, not subverted** | Claude honours conventions in 62% of stories (39–56% for the other sources) | Irreverence that "should target pretension more often than sincerity" (voice guide) |
| **Emotion through the body; smell** | AI "conveys emotion through physical sensations and bodily metaphors (81% vs. 38% human)" and uses "more smell-based imagery (82% vs. 57%)"; "Humans use explicit emotion labels 29% of the time versus just 8% for AI" | **A real tension.** The body knowing first and smell are the author's own signature (the voice guide; [Craft 5](../Craft.md#5-the-body-may-know-before-the-mind-adapted)). Craft already says it's "one route into feeling, not a compulsory beat". Vary the vehicle: an object that contains the feeling ("a stained recipe card", "an old spoon"), habit or expertise, a wrong-detail response. Don't swap it for stated feelings: the guides still say emotion "should often arrive indirectly" |

## Scene and paragraph level

| Tell | What it looks like | Where it's named | What the guides already say |
| --- | --- | --- | --- |
| **Aphoristic closure** | a paragraph or scene ending on a pull-quote: "the sentence has the *shape* of wisdom without its friction" | Vollmer; Wikipedia ("compulsive summaries") | "Not every line should be quotable"; avoid "writing designed primarily to produce quotable lines" and "forced profundity" (voice guide) |
| **Negated contrast, "It's not X, it's Y"** | "The pull from the deep was no current. It was a summons." | Wikipedia; Gorrie; Antislop (up to 6.3× the human rate in some models); Slop Score weights it at 25% | A good watch pattern: paragraphs opening "Not…" or "No…" |
| **Rule of three** | three parallel items of equal weight, again and again | Wikipedia; Gorrie; Record Crash | Watch by reading: list-of-three descriptions, triple fragments ("Fast. Simple. Effective.") |
| **Explaining what was shown** | "Unnecessary/redundant exposition" was 18% of professional writers' edits to AI fiction | Chakrabarty et al. (LAMP) | [Scene diagnostic](../Craft.md#sunday-morning-scene-diagnostic) question 4; the watch-list's "Telling what the scene just showed" |
| **Uniform rhythm** | a metronomic sentence length; or in fiction, "short, short, polished capstone" | Vollmer ("low burstiness"); the Pathwell handoff | The voice guide's "Sentence Rhythm"; "Do not make every sentence compete for attention" |
| **Pacing flatness** | every beat at the same speed; no summary, no elision | Vollmer | "Do not sprint through the entire story" (voice guide). Let small things go by in a line |
| **Flattened dialogue, one shared deadpan** | "characters sound alike; no distinct idiolect. No one has verbal tics, dialect, or pattern of evasion" | Vollmer | Avoid "everyone sharing the same sense of humor"; dialogue "character-specific… imperfect… often indirect" (voice guide) |
| **As-you-know-Bob exposition** | characters explaining the world to each other | Vollmer | "Avoid dialogue whose only function is explaining the world to the reader" (voice guide); the watch-list's docent |
| **Setting that mirrors feeling** | "rain pattered softly against the window, mirroring her unspoken grief" | Vollmer | "Do not force every event to symbolize something" (voice guide) |
| **Missing concrete particular** | no specific Tuesday, laundromat or grandmother | Vollmer; LAMP ("lack of specificity") | "Sensory details should be specific enough to trigger association" (voice guide); [Craft 10](../Craft.md#10-place-is-functionally-specific-carries-over) |
| **Every detail optimized** | every object is a symbol, a callback or a setup | the Pathwell handoff | "Do not force every event to symbolize something. But allow ordinary events to accumulate meaning." (voice guide) |
| **Consistently clever narration** | every mundane event turned into a polished observation; objects and abstractions doing human things ("silence settled", a sock "surrendered") | the Pathwell handoff; Symban | "Do not turn every observation into a clever observation"; avoid "self-consciously clever narration" (voice guide). Narration may still have attitude ([Craft: voice](../Craft.md#voice)). Density is the concern |

## Sentence and word level

| Tell | Examples | Where it's named | What the guides already say |
| --- | --- | --- | --- |
| **Stock gestures** | a shiver down the spine, heart hammered, jaw tightened, swallowed hard, eyes widened, a smile played on her lips, the breath she didn't know she was holding | Symban; Antislop (in one model's output: "heart hammered ribs" 1,192×; also "took deep breath", "smile playing lips") | The watch-list's body-part cataloging; the setting's cliché list |
| **Over-used words** | shimmered, flickered, gaze, unsettlingly, stammered, muttered; delve, tapestry, testament, pivotal, intricate | Antislop (in one model's output: "shimmered" 2,882×, "unsettlingly" 3,833×); Wikipedia; Vollmer | [Write how people talk](../Craft.md#write-how-people-talk): say it the everyday way |
| **Stock constructions** | "the weight of [adjective] [noun]"; "a mix of [noun] and [noun]" | Chakrabarty et al. (LAMP) | — |
| **Participial tail** | a trailing "-ing" phrase that restates the clause: "…, underscoring its importance" | Vollmer; Wikipedia | — |
| **Incoherent or abstract metaphor** | "smiled like sunrise over a sink"; "collect your griefs like stones in your pockets" (Nostalgebraist, quoted in The Argument): images that "sound vaguely pleasing but are logically incoherent" | The Argument; Record Crash ("eyeball kicks") | Metaphor is a cautious category; avoid "endless metaphors" (voice guide); [Craft 8](../Craft.md#8-dont-explain-the-metaphor-before-performing-it-carries-over). A suggestion, not a guide rule: a figure that comes from the character's world tends to hold up |
| **Em-dash overuse** | dashes used for every added clause | Wikipedia; Vollmer; StoryScope's press coverage | — |
| **Too clean** | no contractions, perfect grammar, no informal slips | Vollmer | "Polish should improve communication, not sterilize personality"; "Do not polish the humanity out of the prose" (voice guide); contractions by default ([Craft](../Craft.md#write-how-people-talk)) |
| **Stock names** | "Elara" appears 85,513× more often than in human text (in one model's output) | Antislop | Register names ([Registry](../Registry.md#names)) |

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
- The author's GPTZero read of a Pathwell chapter, kept in the Pathwell revision's [AI detection notes](../../Revision/AI-Detection-Notes-2026-09-30.md#the-handoff-as-the-author-gave-it).
