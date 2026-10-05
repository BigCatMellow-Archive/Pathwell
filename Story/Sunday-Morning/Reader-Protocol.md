# Reader protocol

## Status

**Procedure, active (D20).** This page owns how an independent reader reads a story or chapter as a reader, what questions it asks, and how it reports them. It runs after every pass, in the [after-every-pass routine](Pipeline.md#after-every-pass), and at L4.

**Why it exists.** In the Pathwell revision the author read the rebuilt Chapter 4 and asked: "How did Elizabeth lose track of Pathwell so easily?" The pass had been through a fresh check, the locks, the checker and the line-note rules. None of them caught it, because none of them read the chapter the way a person does: picturing it, and stopping when the picture doesn't hold. The author asked for "an independent reader asking questions as they read", backed by research on how to analyze a story and by the rules built so far.

The checks already in place are audits: they compare a text against a list. This protocol is a reading. The two work together: the reading finds where a reader stops, and the rules then help explain why.

## What the research says a reader does

- **Readers keep a running model of the situation and update it at every break.** Comprehension research (the event-indexing model of Zwaan and colleagues) finds that readers track at least five things as they go:
  - **time**
  - **space**
  - **cause**
  - **characters' goals**
  - **who is present**

  A break in any of these (a time jump, a new place, an effect without a cause) costs the reader effort, because the model has to be updated. If the page gives the reason, the update is smooth. If it doesn't, the reader is left with a question. Most of this protocol's questions are those five, asked on purpose.
- **Some gaps are the reader's job, and some are holes.** Wolfgang Iser's reader-response theory calls the places a text leaves open "blanks". Readers fill them from what the page has given, and that work is part of the pleasure. The reader's job here is to tell the two apart. A gap can be filled from the page or is clearly meant to stay open. A hole can't be filled, because the page is missing something.
- **Plot holes come in a few kinds:**
  - continuity (a fact changes);
  - logic (the world's own rules are broken);
  - motivation (a character does something their psychology doesn't support);
  - worldbuilding (the setting bends for convenience);
  - knowledge (someone knows something they had no way to learn).

  Editors find these by asking scene-by-scene questions and by tracking what each character knows.
- **Convenience breaks belief.** An "idiot plot" (Damon Knight's term, after James Blish) only works because someone fails to do or say the obvious thing; Roger Ebert's version is a problem that "could be cleared up at any moment by one line of sensible dialogue". Pixar's story rule 19: coincidences that get characters into trouble are fine; coincidences that get them out are cheating. Editor Beth Hill's view is that coincidence "so quickly and thoroughly reminds readers that they are reading fiction".
- **Reactions are part of belief.** Readers stop believing when a character's reaction doesn't fit them, or when nobody reacts to something large.
- **Capture questions as they come.** A think-aloud protocol has a reader say what they notice, wonder and feel while reading, not afterward. Questions written down at the point they arise are more complete and more honest, because the reader hasn't yet explained them away with what comes later.
- **Lead with meaning, then questions, then opinions.** Liz Lerman's Critical Response Process puts what worked first, then the artist's own questions, then the responders' neutral questions, and only then opinions, given with permission. It keeps feedback useful to the person who owns the work, and it records what to keep, not only what to fix.

## Who reads, and how

- **A reader who didn't write or revise the text.** It gets no account of the pass and no list of intended fixes before the cold read.
- **It reads in order from the start.** For a chapter of a novel, that means the earlier chapters first, the way a reader comes to it. A reader who hasn't seen Chapter 3 can't notice what Chapter 4 forgets.
- **Pass 1, cold (think-aloud).** It reads the new text section by section and writes each question down where it arises, with the line number and what set it off. It writes down what it expects to happen next. It notes where it skimmed, where it was pulled out of the story, where it laughed and where it cared. It doesn't look anything up and doesn't go back to fix its questions. When a later line answers a question, it marks the question answered and says where.
- **Pass 2, informed.** Only then does it read the rules and the records: the [line-note lessons](Craft.md#lessons-from-the-authors-line-notes), [writing against sameness](Craft.md#writing-against-sameness), the [tone guardrails](Rules.md#tone-guardrails), [AI tells](Sources/AI-Tells.md), the setting's narrator register, and the story's own locks, decisions and promise ledger. It then sorts every question it left open.

## The questions

These are prompts for noticing, not a form to fill in. Ask whichever ones the page raises.

1. **Space and staging.** Where is everyone, and how far apart are they? What is each person holding? Could she see or hear that from where she is? How did that thing get there, or get lost? Is anything used before it arrives (a drink sipped before it's poured, a tool swung before it's picked up)? Does the physical cause work at that distance and speed?
2. **Time and light.** What time is it, and how much time has passed? Is it still the same night? Do the light, the weather and the season fit? Could she see that colour in the dark?
3. **Cause.** Why did this happen now? Would it physically work? Is a coincidence getting someone out of trouble?
4. **Goals.** What does each character want in this scene? Why doesn't she just do the obvious thing? (the idiot-plot test) Would this person really do or say this?
5. **Knowledge.** How does he know that? Who told whom, and when? Does the narration know something the viewpoint character doesn't? Is anyone named before the viewpoint character learns the name?
6. **Who.** Who is this? Have we met them? Is it the same person as before?
7. **World rules.** Does the magic, cost or rule work the way it did last time? If not, does the page show why?
8. **Reaction.** Did anyone react to the big thing? Is the reaction the right size for this person?
9. **Promise.** What do I expect next? Was something set up and then dropped? Was something paid off that was never set up?
10. **Engagement.** Where did I skim? Where was I pulled out of the story? Where did I laugh? Where did I care? Which line would I quote?

## Sorting open questions (pass 2)

Each question still open at the end of the chapter gets one label:

| Label | Means | What happens |
| --- | --- | --- |
| **hole** | The page can't answer it, and a reader would notice | fix it (smallest change that answers it) |
| **late** | Answered, but after the reader had already stopped | move the answer earlier, or plant it |
| **gap** | Deliberately open, or answered later in the book (check the promise ledger) | leave it; confirm that the ledger tracks it |
| **lock** | The page contradicts a locked decision | fix it, or take it to the author |
| **rule** | The page breaks one of the craft rules or tone guardrails | fix it, or flag it if it's taste |
| **taste** | Not a fault; a choice the author should hear about | ask it as a neutral question |

**Severity:** *stopper* means a reader would stop and reread or lose belief. *Snag* means a reader would notice it and go on. *Quibble* means only an editor would notice.

## The report

1. **What worked.** Three to six lines with quotes: what the author should keep.
2. **Question log.** A table with the line, the question, what set it off, whether it was answered (and where), the label and the severity.
3. **Stoppers.** Every place the reader was pulled out, with a line each.
4. **Neutral questions for the author.** Taste matters, asked as questions, not verdicts ("What's the cart doing when she falls behind?" rather than "the cart is wrong").
5. **Opinions, last, and marked as opinions.**

The reader suggests only the smallest fix for a hole. It doesn't rewrite the prose. Drafting stays with the reviser, and taste stays with the author.

## When to run it

- **After every pass, before the author sees it** (after-every-pass step 6). The fix list and the report to the author say what the reader asked and what was done about it.
- **At L4**, the whole book read in order (Pipeline [Stage 4](Pipeline.md#stage-4--judge-review-independently)).
- **Calibrate when it's new.** The first run includes a known miss, to check that the reader catches it. If it doesn't, find out what in the protocol let it through.

## Sources

- **Readers' situation models:** Zwaan, Radvansky, Hilliard and Curiel, ["Constructing Multidimensional Situation Models During Reading"](https://www.tandfonline.com/doi/abs/10.1207/s1532799xssr0203_2) (Scientific Studies of Reading, 1998), with the [ResearchGate copy](https://www.researchgate.net/publication/248943192_Constructing_Multidimensional_Situation_Models_During_Reading); [Frontiers in Psychology on situation models](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2016.00116/full).
- **Iser:** [Yanling Shi, "Review of Wolfgang Iser and His Reception Theory"](https://www.academypublication.com/issues/past/tpls/vol03/06/17.pdf).
- **Think-aloud:** [Think aloud protocol (Wikipedia)](https://en.wikipedia.org/wiki/Think_aloud_protocol); [Reading Rockets on think-alouds](https://www.readingrockets.org/classroom/classroom-strategies/think-alouds).
- **Plot holes and beta-reader questions:** [InkShift, "Plot Holes in Fiction"](https://inkshift.io/resources/plot-holes-fix); [Stoney deGeyter, "51 Questions to Ask Beta Readers"](https://stoneydegeyter.com/blog/51-questions-to-ask-beta-readers/) ("Could you visualize actions clearly, or did you lose track?").
- **Convenience:** [Idiot plot (Wikipedia)](https://en.wikipedia.org/wiki/Idiot_plot); [Pixar's 22 rules of storytelling](https://www.articulatemarketing.com/blog/rules-of-storytelling-from-pixar) (rule 19); [Beth Hill, "Coincidence Destroys the Suspension of Disbelief"](https://theeditorsblog.net/2012/01/20/coincidence-destroys-the-suspension-of-disbelief/).
- **Belief and reaction:** [K.M. Weiland, "5 Ways You're Blocking Readers From Suspension of Disbelief"](https://www.helpingwritersbecomeauthors.com/5-ways-youre-preventing-readers-from/).
- **Order of feedback:** [Liz Lerman's Critical Response Process](https://bussigel.com/communityart/wp-content/uploads/2016/08/critical_response.pdf).
