# Reader panel

## Status

**Procedure, active (D25).** This page owns how to put several AI readers on a book at once so that they read it *differently*: how each reader is built, how they're kept blind and independent, how real findings are told apart from run-to-run noise, how the reports are combined without smoothing them into one voice, and how to check that the panel didn't collapse into one reader. The [reader protocol](Reader-Protocol.md) owns how one reader reads. This page owns the panel, and it holds a starting roster of twelve readers (the lens cards) that a book copies into its own folder and adapts.

**Why it exists.** After the first whole-book read with a goals questionnaire, the author asked for "a way to have protocols for any number of readers look at the story and give us its opinions", with two worries:

> "having just 1 run of a reader, and secondly having the agents all look for the same things so we would never find anything beyond what that one personality would be looking for… if I tell you to have a dozen agents read it, I worry its going to be the same agent a dozen times"

The research below backs both worries. A single reading is one sample from a noisy process. Twelve readers built from one model, one prompt and a different job title are close to twelve copies of one reader. The panel is built against both, and it measures itself against both every time it runs (the [noise check](#the-noise-check) and the [diversity check](#the-diversity-check)).

---

## What the research says

**What the evidence doesn't cover.** None of the studies below tests an AI reading and critiquing a finished book. They cover idea generation, accuracy on questions with checkable answers, judging answers, and simulating survey respondents. They point the same way, and the panel follows them, but the panel is a design to be tested by its own checks, not a proven method.

### One run is one sample

- **The same model, given the same prompt, varies a lot from run to run.** Across 12 models and 12,000 samples, sampling alone accounted for roughly 10–34% of the variation in creative output, and the authors warn that "single-sample evaluations risk conflating sampling noise with genuine prompt or model effects" (Haase et al., 2026). An earlier study found "the same LLM, given the same prompt, can produce outputs ranging from below-average to original" (Haase, Hanel and Pokutta, 2025).
- **So a finding from one reader could be the book or the dice.** The only way to tell is to run the same reader again and see what survives.

### Many readers from one model converge

- **One model gives different people similar outputs.** In a study of creative ideation, each person's own ideas stayed as varied with ChatGPT as with a deck of prompt cards (Oblique Strategies), but across people the ChatGPT ideas were less semantically distinct (a modest effect); the authors explain that "an LLM will tend to produce similar outputs in response to similar inputs, even when those inputs come from different users" (Anderson, Shah and Kreminski, 2024). A panel of readers with near-identical briefs is that situation.
- **A role label is not a dependable way to change what a model does.** On questions with checkable answers, adding a persona to the system prompt didn't improve accuracy, and "the effect of each persona can be largely random" (Zheng et al., 2024). That study measured accuracy, not critique, but it's a warning against building a panel out of job titles.
- **Models flatten the groups they're asked to play.** Asked to answer as members of a demographic group, models misportrayed the group and gave answers less varied than real members did (Wang, Morgenstern and Dickerson, 2025). In simulated populations, demographic labels alone did worst; a moderate set of theory-driven traits did better, and adding many more gave no further gain and in some respects did worse (Qin, Li and Cheng, 2026). Agents built from two-hour interviews about a real person predicted that person's survey answers better than agents built from demographics (Park et al., 2024). On how much backstory helps, the evidence is mixed.
- **Variety can be designed in.** Ten deliberately different AI personas gave writers story plots that preserved the diversity of a human-only baseline; the authors conclude that the loss of diversity comes from deploying AI uniformly, not from an inherent limit of the technology (Wan and Kalman, 2025).
- **The task and the model both matter, about equally.** For the originality of creative output, the choice of model explained about 41% of the variation and the prompt (which there meant a different creative task) about 36% (Haase et al., 2026). The panel uses both levers: each reader gets a different job, and the models rotate.
- **Several model families beat one big judge.** A panel of three smaller models from three different families agreed with human judgments better than one large model, with less bias toward any one model's own outputs (Verga et al., 2024). That study used different families; three sizes of one family, which is what this harness has, is weaker.

### The readers' own biases

- **Models favour their own writing.** LLM evaluators rated their own outputs above others', and the bias rose with their ability to recognise their own text (Panickssery, Bowman and Feng, 2024). A book revised with Claude and read by Claude will, by inference, get kinder readers than strangers would be.
- **Models tell people what they want to hear.** Assistants gave more positive feedback on a passage when the user said they liked or wrote it, and more negative when they said they didn't (Sharma et al., 2023). A reader told the author's goals will tend to find them, and a reader whose sketch describes the book's own tone will tend to like it.

### Independence

- **Crowds are wise only when their members are independent.** When people could see each other's estimates, the range of answers narrowed without the crowd getting more accurate, and people grew more confident (Lorenz et al., 2011). Readers who can see each other's reports, or a shared summary, stop being separate readers.

### Human practice

- **Novelists use a few readers of different kinds.** Writers surveyed (92, from writers' groups) used "between two and twelve" beta readers, mixing target-audience readers, other writers and specialists; a weakness named by several readers, "especially if they included both writers and non-writers", is the one to take seriously (Probst, for Jane Friedman, 2019, updated 2025). Questions focus the feedback; without them you get "vague praise or people thinking they're line editors."
- **Small panels find most of what one kind of reader will find; distinct groups each need their own.** Five users find about 85% of a design's usability problems, and the curve flattens after that; with several distinct user groups, test three or four from each; and run several small rounds rather than one big one (Nielsen, 2000).
- **Opinions come last, and questions shouldn't carry them.** Liz Lerman's Critical Response Process separates what struck the responder, the maker's own questions, "questions without an opinion embedded in them", and opinions offered only when asked for.

### What this means for the panel

1. Run more than one reader, and run at least one of them twice on the same model, so noise can be seen.
2. Make readers differ in their **job**, their **reading condition** and their **model**, not only in who they're told they are.
3. Give each reader a short, specific life as a reader, built from reading history, not from demographics and not from the book's own design.
4. Make blindness as close to physical as the harness allows: each reader gets its own copy of exactly the text it should read, and nothing else.
5. Don't show any reader the questions every reader shares until its own job is done.
6. Count a finding as strong when readers from *different families* found it on their own.
7. Assume the panel is kinder and more alike than real readers, and confirm its big findings with a person when possible.

---

## The panel

### The levers

Each reader differs from every other on at least three of these. The [lever matrix](#step-2-pick-the-lenses-and-check-the-lever-matrix) checks it before a panel runs.

1. **The job.** What the reader produces: a quit point, a continuity table, a one-star review, discussion questions, one character's arc, an editorial letter. Each lens has its own questions.
2. **The model.** Rotate Haiku, Sonnet and Opus. A non-Claude model or a human reader, where one can be had, is the only way to get a reader outside the family; treat one as worth more than another Claude reader (a working assumption, not a measured one).
3. **The reading condition.** Cold and whole; chapter by chapter; in short sittings with forgetting in between; twice through; starting in the middle; one character's scenes only. Conditions that depend on forgetting are run with chained agents ([below](#lenses-that-need-more-than-one-agent)), because one agent can't forget what it has read.
4. **The reader's life.** Five to eight lines of reading history (named kinds of books they love and are tired of, what burned them, why they picked this one up, how they read). Written from reading history only. This length is a working choice.
5. **The stance.** Some lenses read for what works, some for what's wrong, some for both.

### Families

Lenses fall into four families. Agreement *within* a family is one kind of reader agreeing with itself; agreement *across* families is the strong signal.

- **Experience:** reads as a reader, for how it felt (target, reluctant, skimmer, book-club host).
- **Audit:** reads to check something specific (continuity auditor, rules reader).
- **Craft:** reads as a maker (developmental editor, prose reader, rereader, middle-starter, character reader).
- **Adversarial:** reads for the case against (hostile reviewer).

### What counts as a finding

Every report is turned into finding records before anything is compared. One record per finding:

| Field | Values |
| --- | --- |
| reader | lens, run number, model |
| chapters | a chapter or a span ("Ch5–7") |
| subject | the character, object, event or line the finding is about, in a few words |
| type | one of: confusion, continuity, knowledge (who knows what, and how), logic, rule, motivation, voice/repetition, pacing, tone, promise (setup or payoff), structure, strength |
| polarity | + (works) or − (doesn't) |
| quote | a verbatim line from the book, 25 words or fewer |
| severity | the reader protocol's words: stopper, snag or quibble (strengths: strong or mild) |
| prompted | **unprompted** if it came from the reader's running log, or from an answer to a question that didn't name the topic; **prompted** if the question pointed at it |
| rank | its place in that reader's top ten, if it's there |

**Two records match** when they have the same type, the same polarity, the same subject, and chapter spans that overlap or touch (within one chapter). Whether two subjects are the same is decided by the merge agents ([step 7](#step-7-merge-twice)), and their disagreements are listed. Lumping three different complaints into one record isn't allowed; a record that needs two types is two records.

**Each lens's top ten** is its own ranked list of "ten things I'd tell the author", written last, after the shared core. The checks count findings at snag or above (and strong strengths), so quibbles don't swamp them.

### The shared core

Six open questions, identical for everyone, so readers can be compared:

1. What is this book about, in three or four sentences, without listing the plot?
2. The moment that worked best for you, and why.
3. The moment that worked least, and why.
4. Where did you get confused or stop believing it?
5. What did you want from the book that you didn't get?
6. One thing you'd tell the author.

**The core arrives second.** The reader is given only its lens brief and reads the book. When its lens output and running log are written, the session sends the core questions as a second message to the same agent (SendMessage). Then it asks for the ranked top ten. No reader reads the book with the shared questions in mind. For a chained lens, the last agent in the chain gets the chain's logs and answers the core and the top ten.

### The roster

Twelve lenses to start from. A book copies the roster into its own folder; the reader lives are drafted fresh for each panel ([who writes the briefs](#writing-a-readers-brief)). The stance and "built to find" columns are what the synthesis uses.

| # | Lens | Family | Stance | Built to find | Reading condition | Default model | Produces |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | **The target reader** | experience | works | tone, strength, pacing | cold, whole book, at leisure | Sonnet | where they leaned in, laughed, braced, skimmed; what they'd cut before what they'd praise; which two comparable books they'd rank it between, and why |
| 2 | **The reluctant reader** | experience | both | confusion, rule, pacing | cold, whole book | Haiku | every place they needed something explained; the line where they'd have quit if a friend hadn't insisted; what hooked them, if anything |
| 3 | **The skimmer** | experience | wrong | pacing, confusion, structure | short sittings with forgetting ([chained](#lenses-that-need-more-than-one-agent)) | Haiku | an attention map: at each sitting, what they remember, what they've lost, whether they'd pick it up again; the exact line they'd stop for good |
| 4 | **The continuity auditor** | audit | wrong | continuity, confusion | chapter by chapter, keeping a table | Sonnet | where every person and object is at each scene change; injuries, time and light; every fact that changes; every line where the speaker is unclear |
| 5 | **The rules reader** | audit | wrong | rule, promise | whole book, keeping a rules sheet | Opus | the world's rules as stated and as used; every rule broken, bent or never explained; the move a clever character would have made |
| 6 | **The character reader** | craft | both | motivation, voice/repetition, promise | one character's scenes only (rotate between characters across panels) | Sonnet | that character's wants, changes, voice, best and worst moments; where they act out of character; whether their ending follows from what they did |
| 7 | **The developmental editor** | craft | both | structure, pacing, promise | whole book, then a second skim of their own notes | Opus | an editorial letter: what the book is, what it does best, the three biggest structural problems, pacing by act, setups and payoffs, what to cut |
| 8 | **The prose reader** | craft | wrong | voice/repetition, tone | the first, middle and last chapters in full, then three more chosen in the brief (fixed, so a repeat reads the same text) | Opus | repeated sentence shapes, jokes, gestures and scene endings; where characters sound alike; the best and worst paragraphs |
| 9 | **The rereader** | craft | both | promise, structure | twice through, as two agents ([chained](#lenses-that-need-more-than-one-agent)) | Opus | what the second reading changed: setups visible only in hindsight, lines that got better or worse, what the first reading predicted wrongly |
| 10 | **The middle-starter** | craft | both | structure, promise, confusion | the second half, then written predictions about the first half, then the first half | Sonnet | what the second half carries on its own; which predictions were wrong; what the first half added when read last |
| 11 | **The hostile reviewer** | adversarial | wrong | none (its findings count toward convergence, but alone they are minority reports) | cold, whole book | Opus | the strongest honest one-star review, quoted; the single change that would have won them over |
| 12 | **The book-club host** | experience | both | strength, motivation, tone | cold, whole book | Haiku | eight discussion questions, phrased neutrally; what members would disagree about, and where the book gives each side something to stand on |

**Specialist slots**, added when a book needs them: an authenticity reader for an experience the book depicts; a reader in the age group of a crossover audience; a reader who knows a real place or craft the book uses.

**A goals questionnaire, if the book has one,** is a thirteenth lens (family: goals; stance: both; built to find: the beats its questions name), the most goal-directed, and never the only one. Its questions name specific late beats, which primes the reader (the first one said so), so it never counts toward convergence on those beats.

### Lenses that need more than one agent

One agent holds everything it has read and has no clock. Lenses that depend on forgetting or on a second look are run as chains:

- **The skimmer:** one agent per sitting of about 2,500 words. Each gets only its sitting's text and the previous agent's written recap (never the earlier text), writes what it remembers, what it has lost, and whether it would keep going, then hands its recap on. The chain runs to the end of the book either way; each agent also says whether it would still be reading, so the quit point is recorded without losing the later sittings.
- **The rereader:** the first agent reads the whole book and writes a prediction and expectation log as it goes. The second, fresh agent gets the book and that log, reads it as a second reading, and marks what the log got wrong, what it never saw coming, and what now reads differently.
- **The middle-starter:** one agent reads the second half and writes its predictions about the first half to a file before it's given the first half.
- **The character reader** needs a list of the chapters and scenes where its character appears. A separate agent makes that list from the chapter files alone (no records) before the reader starts.

### Writing a reader's brief

Each brief has four parts, in this order:

1. **The ground rules**, the same for every reader: read only the files in your folder, and say if you opened anything else; write only to your own output folder; write your log as you read, and don't revise it afterwards; quote and give chapter numbers; "I don't know" and "I didn't care" are answers; don't guess what the author wanted; name what you'd cut before what you'd praise.
2. **Who you are as a reader**: the lens's five to eight lines, in the second person.
3. **How you read**: the reading condition, step by step, with where to write the running log.
4. **What you produce**: the lens's own output, in its own format.

Don't name the lens ("you are the skeptic"), don't mention other readers, and don't describe the book's goals, tone or genre beyond what its cover would say. The shared core and the top ten come later, by message.

**Who writes the briefs.** Not the session that revised the book. First, one agent reads only the first chapter and writes a two-sentence cover line (the shelf it would sit on and the premise, as a back cover would put it). Then each brief is drafted by its own agent from its lens card and that cover line, with no other access to the book, the records or the goals. Then one reviewer agent reads all the briefs together and checks two things: that no brief leaks the book's goals or tone beyond the cover line, and that every pair of reader lives differs on at least three of reading history, patience, what they're carrying, and what they distrust. A brief the reviewer rejects goes to a fresh drafting agent with the reviewer's note.

**An example reader's life** (the reluctant reader; adapt, don't copy):

> You read mostly literary fiction and memoir: quiet books about families, work, places. The last fantasy novel you finished was in school, and you remember the maps and the invented words more than the story. You're tired of books that explain themselves, and you put down anything that opens with a glossary. A friend you trust pushed this one on you and said, "Just give it fifty pages." You read in the evening, a chapter or two at a time, and you'll say so when you're lost.

---

## Running a panel

### Sizes

| Size | Readers | Reads | When |
| --- | --- | --- | --- |
| **Quick** | 4: the target reader, the reluctant reader, the continuity auditor, the hostile reviewer; one run each | the changed chapters, starting one chapter before them | after a large revision of several chapters |
| **Standard** | 8: the target reader (run twice, same model), the reluctant reader, the skimmer, the continuity auditor, the rules reader, the character reader, the prose reader, the hostile reviewer. With the default models that is 4 Sonnet, 3 Opus and 2 Haiku runs | the whole book (the prose reader and character reader read less) | after a full pass on the book; at L4 |
| **Full** | all 12, plus specialists and the goals lens; the target reader and the continuity auditor each run twice on the same model; two lenses also run on a second model | the whole book | before the book goes to human readers |

**Cost.** The one whole-book reader so far used about 233,000 tokens (the first Pathwell questionnaire reader, recorded in that book's pass log, Q1). A standard panel is roughly nine whole-book reads, plus about one more for extraction and merging and one for the informed pass; the rereader costs two reads, the skimmer's chain about one. Calibration is a second panel of its own. Opus costs several times what Haiku does, so the model mix decides the price more than the reader count.

### Step 1: freeze and sandbox the text

Record the commit. Build one folder per reader (and per stage of a chained lens) in a scratch area outside the repository, containing exactly the text that reader should see: the whole book, the second half only, one sitting, one character's chapters, or the changed chapters with the one before. No history, notes or reports go in. Each reader gets its folder, its brief and its own output folder, and nothing else. A subagent could still look elsewhere, so the ground rules ask it to say if it did; the sandbox removes the easy paths, it doesn't make looking impossible.

### Step 2: pick the lenses and check the lever matrix

List the panel's readers with their job, model, reading condition, family and stance. Job and reader's life differ for every pair by design, so they don't count. For every pair except a repeat pair, count how many of model, reading condition, family and stance differ. Any pair that differs on fewer than two is changed (a different model or condition) before the panel runs. Models are assigned so no model reads more than half the panel. In a full panel, run at least two lenses on two models each, so differences between lenses can be told apart from differences between models; check Haiku reports for lens adherence first (step 5), since a small model on a long book is the likeliest to drift into a generic report.

### Step 3: write and check the briefs

[As above](#writing-a-readers-brief): one agent per brief, then one reviewer for leakage and contrast.

### Step 4: run the readers, in parallel and blind

Each reader writes its running log as it reads and its lens output at the end, to its own file. Then it gets the shared core by message, then the request for its top ten. Repeats are separate fresh agents with the identical brief and the identical text.

### Step 5: check each reader did its job

Before reading any findings: did the skimmer give an attention map, did the auditor keep its table, did the reluctant reader say where it would have quit? A report that reads like a generic book report has failed its lens. Its findings count as one generic reader's, not as that lens's, and the lens is rerun with a sharper brief if it matters.

### Step 6: extract

One agent per report turns that report into finding records ([schema](#what-counts-as-a-finding)). No extraction agent sees two reports. Each record keeps a pointer to the report and line it came from.

### Step 7: merge, twice

Two agents on different models merge all the records into one table by the [matching rule](#what-counts-as-a-finding), independently. Where their tables disagree, both versions are listed, not resolved. Then:

- **Completeness:** every extracted record appears in exactly one row. The counts must match.
- **Splits** are computed from polarity: a row with both + and − records is a split, and it stays a split. The target reader loving what the reluctant reader skipped is information about audience, not a draw.
- **Types:** where the two merge agents tagged the same record with different types, both tags are listed.
- **Quotes:** the synthesis agent checks ten quotes, chosen at random, against the chapters.

### Step 8: sort

A fresh synthesis agent (not the revising session, and not a merge agent) runs this step and the checks below from the merged table. Counts are done by a short script where possible.

1. **Convergent:** found unprompted by lenses from **two or more families**, and in a standard or full panel by at least three readers. Treat as real.
2. **Lens-specific:** found by the lens whose "built to find" column covers its type (only the auditor will catch a cup that changes hands). Treat as real if it's quoted and specific.
3. **Minority report:** found by one reader outside its "built to find" types, or by one reader against the rest. Listed verbatim, never dropped.
4. **Noise suspect:** found in one of a repeated lens's two runs and by no other lens. Listed, marked low confidence, never deleted.

Within each list, order by severity (stoppers first), then by how many families found it.

### Step 9: the informed pass

The panel is blind to the records, so it can't run the checks that need them. After the sort, one informed reader follows the [reader protocol's](Reader-Protocol.md) second and third passes over the sorted findings: it labels each with the protocol's labels (hole, late, gap, lock, rule, taste), checks them against the locks and the ledger, and runs the [tone and rules check](Reader-Protocol.md#the-tone-and-rules-check) (D24). At L4, the panel plus this pass replaces the single whole-book reader; neither replaces it alone.

### Step 10: compare with the goals, if there are any

Only now does anyone open the book's goals key. The comparison goes lens by lens and family by family, and the goals lens is reported separately from the blind ones.

### Step 11: report and file

To the author: the convergent findings, the splits, the lens-specific findings, the minority reports, the noise check, the diversity check, and what the informed pass and the goals comparison added. Then file everything ([records](#records)).

### Afterwards: small rounds

After fixes, don't rerun the whole panel. Rerun the lens that found each stopper, on the changed chapters, to see whether the fix worked (Nielsen's several small rounds).

---

## The checks on the panel itself

These answer the author's two worries every time a panel runs.

### The noise check

*One run is one sample.* For each repeated lens (same brief, same text, same model), count the findings at snag or above that either run raised, and how many both raised. Report that overlap.

- It's a rough flag, not a measurement: two runs of one lens give one number.
- **Working band, untested:** under about 40% means single runs of that lens can't be trusted alone, and the next panel should repeat it more. Revise the band once a few panels have run.
- Repeat a general lens (the target reader) as well as a structured one (the auditor). A structured lens looks more reliable than an open one because its format constrains it.

### The diversity check

*A dozen copies of one reader.* Computed on the lens output only, not the shared core (the core is where agreement is expected).

- **Pairwise overlap:** for each pair of lenses, the share of their top-ten findings that match. The test is relative: lens-to-lens overlap should be well below the repeat-run overlap of a single lens. If two different lenses agree as much as one lens agrees with itself, they're one reader.
- **Unique contribution:** for each reader, how many findings (snag or above) only that reader found; for each family, how many only that family found. A reader or family that contributes nothing unique added cost, not a reader. This is order-free, unlike counting "new per reader" in reading order.
- **Coverage:** which finding types the panel produced at all. Low overlap is easy to get by giving lenses different formats; it doesn't show the panel looked widely. A panel with nothing in some type (no motivation findings, say) didn't look there.
- **Lens adherence:** step 5.
- **Shared phrasing:** strip quoted book text, the core questions and the schema headings from the reports, and run the repository's checker for five-word phrases shared across files (`tools/sunday_morning_check.py --registry <the book's Registry> --drafts <reports folder> --pattern "*.md" --status-block off --min-files 3`). The same unusual phrase in several reports ("the narrator tells me what to think") is a sign of one voice.

When the check fails, change the levers before adding readers: sharper and more different jobs, a different reading condition, a different model, and best of all a human reader.

### Calibration

When a panel is new, or its briefs change, run a calibration panel on a separate copy of the text with one planted defect per type the lenses claim: an object that changes hands with no one handing it over (continuity), a world rule broken once (rule), a character acting against an established want (motivation), a phrase repeated in five chapters (voice/repetition), and a promise set up and dropped (promise). Each lens reads only the copy; the real panel reads the real text. Record which lenses caught which plants. A lens that misses the plant it's built to find needs a sharper brief. The planted copy never reaches the author and never enters the book's folder.

### When to add readers

A family has added all it will when its last two readers contributed no unique findings in their own types. Don't add another of that family; add a different family, a different model, or a person. (This is this page's own heuristic, drawn from Nielsen's diminishing returns, not a rule from the source.)

### Limits

- **Every reader here is the same family of model.** Different sizes help; they don't make strangers. Simulated readers are flatter than real ones, and no prompt fully fixes it.
- **They'll be kind.** Weight criticism above praise when the two are close.
- **They aren't the audience.** A panel can find where readers stop, what confuses, and what the book makes people argue about. Whether readers in the target audience love it is a question for real readers. Treat panel findings as strong hypotheses, and confirm the big ones with a person when possible.

---

## Records

A panel's files go in the book's reader-reports folder, in one dated subfolder (`Reader-Reports/Panel-<date>/`):

- `briefs/`: every brief as sent, and the lever matrix.
- one report per reader, named by lens and run (`target-1.md`, `target-2.md`, `skimmer-chain.md`);
- `findings.csv`: the extracted records;
- `synthesis.md`: the merged table (with both merges' disagreements), the four sorted lists, the noise check, the diversity check, the calibration results if any, and the commit the panel read;
- `informed-pass.md`; and `alignment.md` if the book has a goals key.

The book's pass log gets one entry per panel, with links.

## When to run it

- **After a full pass on a book:** a standard panel.
- **At L4** ([Pipeline, Stage 4](Pipeline.md#stage-4--judge-review-independently)): a standard or full panel, then the informed pass.
- **Not after every chapter pass.** The single [reader protocol](Reader-Protocol.md) does that job; a panel there costs too much for what a chapter can show. A quick panel is for a large revision of several chapters.

---

## Sources

- **Run-to-run variance:** Haase, Gonnermann-Müller, Hanel, Leins, Kosch, Mendling and Pokutta, ["Within-Model vs Between-Prompt Variability in Large Language Models for Creative Tasks"](https://arxiv.org/abs/2601.21339) (2026); Haase, Hanel and Pokutta, ["Has the Creativity of Large-Language Models peaked? An analysis of inter- and intra-LLM variability"](https://arxiv.org/abs/2504.12320) (2025).
- **Homogenization across users:** Anderson, Shah and Kreminski, ["Homogenization Effects of Large Language Models on Human Creative Ideation"](https://arxiv.org/abs/2402.01536) (Creativity & Cognition, 2024).
- **Personas in prompts:** Zheng et al., ["When 'A Helpful Assistant' Is Not Really Helpful: Personas in System Prompts Do Not Improve Performances of Large Language Models"](https://aclanthology.org/2024.findings-emnlp.888/) (Findings of EMNLP, 2024).
- **Flattening and grounding:** Wang, Morgenstern and Dickerson, ["Large language models that replace human participants can harmfully misportray and flatten identity groups"](https://www.nature.com/articles/s42256-025-00986-z) (Nature Machine Intelligence, 2025); Qin, Li and Cheng, ["Restoring Heterogeneity in LLM-based Social Simulation: An Audience Segmentation Approach"](https://arxiv.org/html/2604.06663v1) (2026); Park et al., ["Generative Agent Simulations of 1,000 People"](https://arxiv.org/abs/2411.10109) (2024; the arXiv version is now titled "LLM Agents Grounded in Self-Reports Enable General-Purpose Simulation of Individuals").
- **Designed diversity:** Wan and Kalman, ["Diverse AI Personas Can Mitigate the Homogenization Effect in Human-AI Collaborative Ideation"](https://arxiv.org/abs/2504.13868) (2025).
- **Panels of models:** Verga et al., ["Replacing Judges with Juries: Evaluating LLM Generations with a Panel of Diverse Models"](https://arxiv.org/abs/2404.18796) (2024).
- **Self-preference:** Panickssery, Bowman and Feng, ["LLM Evaluators Recognize and Favor Their Own Generations"](https://proceedings.neurips.cc/paper_files/paper/2024/file/7f1f0218e45f5414c79c0679633e47bc-Paper-Conference.pdf) (NeurIPS, 2024).
- **Sycophancy:** Sharma et al., ["Towards Understanding Sycophancy in Language Models"](https://arxiv.org/abs/2310.13548) (2023).
- **Independence:** Lorenz, Rauhut, Schweitzer and Helbing, ["How social influence can undermine the wisdom of crowd effect"](https://www.pnas.org/doi/10.1073/pnas.1008636108) (PNAS, 2011).
- **Beta readers:** Barbara Linn Probst, ["Beta Readers: Who, When, Why, and So What?"](https://janefriedman.com/beta-readers/) (Jane Friedman, 2019, updated 2025).
- **Sample sizes:** Jakob Nielsen, ["Why You Only Need to Test with 5 Users"](https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/) (Nielsen Norman Group, 2000).
- **Neutral questions:** [Liz Lerman's Critical Response Process](https://notes.artsmanaged.org/p/neutral-questions-and-welcomed-opinions); the [original handout](https://bussigel.com/communityart/wp-content/uploads/2016/08/critical_response.pdf).
