# Review of Story/Sunday-Morning/Reader-Panel.md

Reviewer: independent, read-only. Read: Reader-Panel, README, Reader-Protocol, Pipeline (Stage 4, after-every-pass), Decisions D20-D25, Reader-Questionnaire (+ the first whole-book run's files in Story/Revision/Reader-Reports). Sources fetched: Haase 2026, Haase 2025, Anderson 2024 (abstract + HTML), Zheng 2024, Verga 2024 (abstract + HTML), Panickssery 2024, Nielsen 2000, Probst 2019/2025, Wan & Kalman, Qin et al., Wang et al., Park et al., Sharma (abstract only), Lerman handout. Lorenz 2011 (PNAS, PubMed) returned 403/429 and was not checked.

## Verdict

The page is well organised and honest in its Limits section, and it fits the house style. The panel design (jobs over hats, repeat run, blind readers, a synthesis that keeps splits) is the right shape. But as written it does not yet protect against the author's second worry in this harness, and another session could not run it from the page alone. Three gaps matter most:

- "Finding" is never defined, so every check (noise, overlap, new-per-reader, convergence) is uncomputable.
- Blindness is only an instruction, and some lenses (skimmer, rereader, middle-starter) cannot happen inside one agent's context.
- One synthesiser, one brief-writer and one shared core quietly put a single voice back into the middle and the two ends of the pipeline.

Several quoted phrases in the research section are not in the sources.

---

## MUST-FIX

### M1. "Finding" has no definition, so the checks can't be computed
Passages: Synthesis ("The synthesiser reads every report and builds one table of findings"); diversity check ("Compare the lenses' top ten findings... the share of top findings they have in common"); noise check ("Of the findings either run raised, how many did both raise?").

Problems:
- No unit: is "the middle drags" in Ch5-9 one finding or five?
- No matching rule: when are two reports' findings "the same"?
- "Top ten" is undefined: whose ranking?
- "Unprompted/prompted" is ambiguous, because every brief contains the lens questions and the six core questions, so almost any finding can be called prompted. Conversely, the auditor's table is prompted by its job, so by the page's rule it can never be convergent.
- Lumping inflates convergence: merging three different complaints into one row makes three lenses "converge".

Fix: add a "What counts as a finding" section. Suggested schema, one record per finding:
- reader/lens/run
- chapter span
- type, from a closed list (confusion, continuity, rule, motivation, voice/repetition, pacing, tone, promise, structure, strength)
- polarity (+/-)
- a verbatim quote of 25 words or fewer
- severity, using the existing words stopper/snag/quibble
- prompted/unprompted

Matching rule: same type, same polarity and overlapping chapter span (plus or minus one chapter). Ties go to a second agent.

"Unprompted" = raised in the running log, or in an answer to a question that doesn't name the topic. A reader's own ranked "ten things I'd tell the author", written last, defines each lens's top ten. Compute noise overlap and the diversity checks on findings at snag or above, so quibbles don't inflate the union.

### M2. The synthesiser is a single bottleneck and can smooth the splits
Passages: Procedure step 6 ("Synthesise, with a fresh agent that read none of the book's records"); Synthesis ("A split is kept as a split, never averaged").

Problems:
- One agent, one personality, reads everything. Instructing it not to average isn't a mechanism.
- Volume: the first Pathwell run produced about 12,000 words (log 6,384 + answers 5,725), roughly 16k tokens. A standard panel (9 runs) is about 110k words. A full panel (15 runs) is about 180k words, about 240k tokens, which won't fit one synthesiser's context with room to work.
- It doesn't say whether the synthesiser reads the chapters. Without them it can't check quotes; with them it isn't "fresh" in the sense the page wants.
- The sort puts "Convergent" first, so lumping is rewarded.

Fix, as a two-stage synthesis:
1. One extraction agent per report, in parallel, each turning one report into M1-schema records. No agent sees two reports.
2. Merge by the mechanical rule in M1. Run the merge twice with two independent agents (e.g., Opus and Sonnet) and list the disagreements instead of resolving them silently.
3. Completeness check: the count of extracted records must equal the count of source rows in the merged table (each record in exactly one row).
4. Every row keeps reader file and line pointers. Splits are computed from the polarity field, not judged.
5. Minority reports and noise suspects are appended verbatim, not paraphrased.
6. Spot-check ten quotes against the chapters.

### M3. Blindness and independence are only instructions; the briefs reintroduce one voice
Passages: Procedure step 4 ("Run the readers in parallel, blind... to its own file. Nobody sees anyone else's"); ground rules ("don't open notes, records, other readers' reports or any key"); Writing a brief ("Don't tell readers there are other readers").

Problems:
- Readers are fresh subagents in a repository that contains the goals key, the pass log and 30+ earlier reader reports. Blindness depends on self-report. The first run's own record says "it opened nothing but" the questionnaire and chapters, with no audit trail.
- Readers writing to files in the same tree can list each other's output.
- A reader that can run `git log` sees the commit message ("Reader questionnaire and a whole-book read against the goals").
- Ground rule 1 tells every reader "other readers' reports" exist, which contradicts "Don't tell readers there are other readers".
- The brief contains the lens questions and all six core questions up front. "Each reader answers its own lens questions first, then the core. Answering the core first would pull every reader toward the same reading" is moot when every reader has read the core questions before reading chapter 1. Every reader reads with the same six questions in mind. This is the shared-core pull the author worried about.
- "Write each reader's brief" doesn't say who. If the session that revised the book writes all twelve briefs, one writer's voice and knowledge of the goals goes into every life sketch.

Fix:
- Sandbox: copy the frozen chapters into a scratch directory outside the repo with no git history. The reader gets only that path, the brief and its own output path. Say this in step 1.
- Reword ground rule 1 to "read only the files you are given" with no mention of other readers.
- Stage the brief: give the lens task and the log format first, and reveal the shared core only after the lens output is written (second turn to the same agent, or a second agent handed the written log). Otherwise say plainly that the core is not blind and drop the "answered last" justification.
- Briefs: each drafted by a separate agent from only its lens card (no goals, no records), then one reviewer agent checks goal leakage and contrast between sketches. Ship one fully written exemplar brief in the page.

### M4. Lenses that depend on forgetting or on a clock cannot be performed in one context
Passages: roster rows 3, 9, 10 and parts of 2.
- 3, skimmer: "breaks every ~10 minutes of reading and says what they remember".
- 9, rereader: "The whole book twice... what changed on the second reading".
- 10, middle-starter: "reads the beginning last... what they'd guessed wrong".

A single agent has the whole text verbatim in context. It has no clock, it cannot forget, and a second read in the same context is not a second read. Run as written, these will produce an ordinary whole-book report under different headings. This is a concrete way the dozen collapses.

Fix: specify real mechanisms.
- Skimmer: chained agents, one per roughly 2,500 words (about ten minutes at 250 wpm), each handed only the previous agent's written recap (not the text), then asked what it remembers and where it would stop.
- Rereader: pass 1 writes a prediction/expectation log; pass 2 is a separate agent given the text plus that log and told to mark what the log got wrong or never saw coming.
- Middle-starter: commit predictions about the missing first half in writing before it is read (the page implies this but doesn't require it).

Also note that the character reader needs a scene list per character from somewhere, which is a record the reader is supposed to be blind to. Say who supplies it.

### M5. The convergence rule can't be applied: lens families, stances and "built for" are not stated
Passages: Synthesis sort 1 ("found unprompted by three or more different lenses, or by both a 'for what works' lens and a 'for what's wrong' lens"); sort 2 ("the one built to find it"); lever 5 ("the stance").

Problems:
- The roster has no stance column, so branch 2 of the convergent rule is not computable.
- "Built to find it" is defined only for specialist lenses (auditor). For generalists (1, 2, 11, 12, 7) every finding is "built for".
- Lenses 1, 2, 11 and 12 (and 7 in part) all read "cold, whole book" and produce general impressions (bored, confused, would recommend). Three of them agreeing is one family agreeing three times, which is the "same agent a dozen times" in miniature. In the Quick panel, three of four lenses are in this family.
- "Convergent" in branch 2 reads as "found by", while Split is defined by polarity; it should say "the same problem".

Fix: add three columns to the roster: family (experience / audit / craft / adversarial), stance (works / wrong / both) and "built to find" (a closed list of finding types, M1). Require convergence across at least two families. State that the "built to find" tag is what makes a finding lens-specific.

### M6. The panel has no home for the L4 record checks or the D24 tone-and-rules check
Passages: Pipeline Stage 4 ("a standard panel... in place of a single whole-book reader"); Reader-Protocol "When to run it" ("by a reader panel of readers who read differently, not one reader (D25)"); panel step 5-7, ground rule ("don't open notes, records").

The Reader-Protocol's passes 2 and 3 (sort against rules and records; the item-by-item tone-and-rules check, D24) need the records. Stage 4's checks (must-establish items, ledger promises, Framework checklist, canon) also need them. The panel readers are blind to all records and the synthesiser reads none. Replacing the single reader with a blind panel silently drops D24 at L4, and nothing in the page says so.

Fix: add a short step after synthesis, "Informed pass": one reader following Reader-Protocol passes 2-3 sorts the synthesised findings with the existing labels (hole / late / gap / lock / rule / taste; stopper / snag / quibble) and runs the D24 check. Then edit Pipeline Stage 4 and Reader-Protocol line 127 to say "panel, then informed pass". Alternatively state in the page that L4's record checks stay with the existing reviewer and the panel only supplies the cold-read evidence.

### M7. Quoted phrases that are not in the sources
- Line 25 (Zheng): the page quotes small effects that "might largely be random". The abstract says "the effect of each persona can be largely random". Fix the quote. The finding is also narrower than the page implies: personas gave no improvement in accuracy on questions with checkable answers. It is not evidence that "A reader told 'you are a skeptical reader' is mostly the same reader". Reword to "a role label is not a dependable way to change what the model does on tasks with checkable answers; none of these studies tests an AI critiquing a book."
- Line 24 (Anderson): the page quotes ChatGPT ideas as "significantly less semantically diverse at the group level". Neither the abstract (which says "less semantically distinct") nor the results text (which says "more homogenized") contains that phrase. The second quote, about similar outputs for similar inputs from different users, is in the paper. The comparison condition was the Oblique Strategies card deck, not unaided people, and the effect is modest (M = .24 vs .28, d = .47, p = .038). Quote the real sentence and name the comparator.
- Line 39 (Probst): the page quotes "especially both writers and non-writers". The source reads "especially if they included both writers and non-writers". Fix the quotation. The survey was 92 writers recruited from five Facebook groups for writers, not "writers and editors"; line 39's "Writers and editors say the same" should be "writers".

---

## SHOULD-FIX

### S1. Sizes, scope and cost are underspecified
- "Standard: 8 lenses, one of them run twice" and "Pipeline: a standard panel: eight readers" never name the 8. Name them or give the selection rule. Suggested: target, reluctant, skimmer, auditor, rules, character (rotate), prose, hostile, with the target reader repeated. That covers all four families.
- Quick is "after a large revision of a few chapters", but the target reader, reluctant reader and hostile reviewer are listed as "Cold, whole book". Four whole-book reads is about 0.9M tokens for a few changed chapters, which contradicts "Not after every chapter pass... costs too much". Say what each size reads: whole book, or changed chapters with the preceding chapters.
- Line 126: "about 230,000 tokens for one reader in the first Pathwell run" has no source. I found no token figure in the Reader-Reports or the Pass-Log. The book is about 45,700 words (about 60-65k tokens), so the figure is plausible but should cite where it came from.
- "Roughly nine times" ignores that the rereader costs about two reads, and that tokens are not cost: Haiku, Sonnet and Opus price very differently. Add a rough cost per lens and the synthesis cost (M2).

### S2. The diversity check measures overlap, not coverage, and some measures are order-dependent
Passage: "The checks on the panel itself".
- Low overlap is easy to get by giving lenses different output formats (the auditor's cups against the prose reader's sentence shapes). A panel can pass with zero overlap and still be twelve readers looking at a narrow slice. The author's worry is "never find anything beyond what that one personality would be looking for", which is a coverage question.
- "New per reader... in the order the reports are read" depends on the order. Use leave-one-out: for each reader, how many findings (at snag or above) were found only by that reader or only by that reader's family.
- The shared core is identical for all twelve. Compute overlap on lens-specific output only, and read the core separately as the convergence evidence. Otherwise core answers dominate the "top ten".
- "Shared phrasing" is not mechanical. The repo's own checker (`tools/sunday_morning_check.py`, five-word phrases shared across files, `--min-files`) can be pointed at the report files after quoted book text is stripped. Mention it.
- "Each reader differs from the others on at least three of these [levers]" is asserted, not checked. Pairs 4 and 5 (auditor and rules reader: same model, both "whole book keeping a sheet", both find-faults) differ mainly on job. Pair 1 and 11 (same model, same condition) differ on job and stance only. Add a lever matrix in the procedure and a rule to reject pairs below three differing levers.
- ">about half" average pair overlap is arbitrary. Say so, or tie it to the noise check: lens-to-lens overlap should be well below the repeat-run overlap of the same lens.

### S3. The noise check needs a threshold, a pair design and seeds
- No guidance on what overlap is "low". With one repeated lens (Standard), the estimate is a single number from two runs. State that it is a rough flag only. Give a working band (e.g., under about 40% means treat single runs of that lens as unreliable) and mark it as untested.
- The prose reader reads "any three at random" and the character reader "rotates", so a repeat pair can read different text. Seed or assign the sample in the brief so the repeat differs only by sampling.
- "In a full panel, two lenses, on different models" confounds noise with model difference. Separate the two: repeat on the same model for noise; compare models as a different check.
- Choose the repeated lens deliberately: a general lens (target reader) shows open-ended noise; a structured lens (auditor) will look more reliable than it is.
- Noise suspects: say what happens to them (listed, marked low confidence, not deleted), as for minority reports.

### S4. The reader-life sketches are the weakest part of the design
- Line 62: "five to eight lines" is demanded, but the roster sketches are one clause each, and rows 4, 5, 7, 8, 9 restate the job ("A detail person who notices when a cup moves hands"). That is the job title the page says doesn't work. Only rows 1, 2, 3, 10 have anything life-like.
- Line 62: "longer backstories made simulated people worse, not better" is not what Qin et al. found. They varied the number of survey identifiers (15 versus 59) in a US climate-opinion simulation using two open-weight models, not backstory length. Park et al. points the other way (two-hour interviews beat demographics, 83-86% versus 74% of test-retest consistency). The evidence on length is mixed; say so and call 5-8 lines a working choice.
- Fix: include one fully written exemplar sketch (named titles read, what burned them, why they picked the book up, how they read) and a contrast rule: each pair of sketches must differ on at least three named axes (reading history, patience, what they're carrying, what they distrust).

### S5. Calibration is too thin to calibrate anything
Passage: Calibration ("plant one known problem... Note which lenses caught it").
- One continuity plant tests the auditor and little else. "A panel where only the auditor catches a planted continuity slip is working as designed" is the only case the page evaluates.
- It doesn't say whether the planted copy is the one the real panel reads. If it is, the plant contaminates findings and the middle-starter and character lenses may never see it.
- Fix: plant one defect per class the lenses claim (continuity, a world-rule break, a character break, a repeated tic, a structural gap) in a separate copy, read by the relevant lenses only. Record the plants, and require the planted copy never reach the author.

### S6. Saturation rule is invented and mostly not applicable
Passage: "Saturation. Following Nielsen, a lens group is saturated when its last two readers added nothing new in their own job."
- Nielsen's article gives the 85% figure, the "several small rounds" advice and 3-4 users per distinct group (three for three or more groups). It gives no stopping rule like this one.
- With one run per lens, there are no "last two readers" in a lens group except the repeat, so the rule duplicates the noise check.
- Fix: delete it, or define "lens group" as a family (M5) and make it a rule for adding more readers in a later round. Say it is the page's own heuristic.

### S7. Reuse the existing vocabulary
- "Severity: would a reader stop, stumble, or just notice?" duplicates Reader-Protocol's stopper / snag / quibble. One concept, one owner: use those words.
- The post-synthesis labels (hole / late / gap / lock / rule / taste) belong to the informed pass (M6).

### S8. Research claims that over-reach
- Line 11: "Both worries are right, and the research below says why." None of the cited studies tests an AI reading and critiquing a fixed text; they cover idea generation, accuracy on questions, judging QA correctness, simulating survey respondents. Add one sentence ("what this evidence doesn't cover") and treat the panel as a design to be tested by its own checks.
- Line 28 ("The strongest lever this panel has is giving each reader a different job"): in Haase 2026 the model explained more of the originality variance (40.94%) than the prompt (36.43%), and the lever list ranks the model fourth. Either re-rank or drop "strongest". The paper's "prompt" means different creative tasks, so "job" is an extrapolation.
- Line 29 and lever 4: Verga's PoLL used three different families (Command R, Haiku, GPT-3.5) judging QA correctness and Chatbot Arena pairs; its gain comes from aggregating votes toward one verdict. Rotating Haiku, Sonnet and Opus is one family at three sizes, not the tested condition. The claims "Different sizes notice different things" and "one of either is worth several more Claude readers" (line 63) have no source. Mark them as working assumptions.
- Line 26: Wang et al.'s abstract says LLMs "misportray and flatten"; "more stereotyped" is not in the abstract. Qin et al.: "did not provide additional gains and in some respects worsened" becomes "made it worse again". Park: 83-86% versus 74% is better, not "far better".
- Line 27 (Wan & Kalman): "preserved the diversity of story plots that a uniform setup lost". The study compared diverse AI inputs with a human-only baseline; a uniform-persona condition was not tested. The personas generated plots for human writers, not reviews.
- Line 33: Panickssery's link between recognition and self-preference is supported (linear correlation, controlled fine-tuning). The study measured evaluators scoring summaries; the leap to "kinder to a book Claude revised" is reasonable but is inference.
- Lerman, line 41: the heading "Neutral questions get honest answers" is not claimed by the handout, which says neutral questions help responders recognise their own values and let artists think afresh. Nothing in the panel procedure uses it.

### S9. Model and lens are confounded
Default models are matched to difficulty (Opus for editor, prose, rereader; Haiku for reluctant, skimmer). Line 63 says "rotate across the models", but the table doesn't rotate. A difference between lenses can't be separated from a difference between models, and Haiku on a 60k-token whole-book read is the likeliest source of generic reports. Say that the Full panel runs at least two lenses on two models to separate them, and that Haiku reports get the step-5 adherence check first.

### S10. Goal leakage, priming and sycophancy in the roster itself
- Lens 1's sketch ("loves found family, small stakes, magic that feels homely... drops books that turn grim without warning") restates the Sunday Morning promise and Pathwell's tone, while the brief rules say "don't describe the book's goals". Combined with Sharma et al. (feedback tilts toward what the user says they like), this reader will find the book fits. Write that sketch from reading history, not from the book's design.
- The questionnaire reader is told specific late beats in its questions (the cookbook in the shop, "It was my fault", the last exchange). The first run's alignment page records that it "knew a few late beats existed" and may have been primed. The page counts it "the most goal-directed lens" but says nothing about this lesson.
- Add a praise-inflation guard to the ground rules: for example, ask lens 1 and 12 to name what they'd cut before what they'd praise, or ask for a ranking against two named comparison books.

---

## NICE-TO-HAVE

- README rule 1 says a new page gets a row in the Notes table and in "Find it fast". The Notes row exists; "Find it fast" has no row for the panel (or the reader protocol). Add: "How do I run several readers on a book?" -> Reader panel.
- Records: the page puts panels in `Story/Revision/Reader-Panels/<date>/`, while existing reports live in `Story/Revision/Reader-Reports/`. Either use the existing folder with a `Panel-<date>/` subfolder or add a line to the Revision README saying why there are two.
- History.md has no entry for the D25 lesson (the first whole-book reader was primed by reading the questionnaire first). Per README's "Lessons become method" and "History records what happened", add one line.
- Nielsen's advice to run several small rounds isn't in the procedure. Add "after fixes, rerun the lens that found each stopper rather than the whole panel".
- The page names Pathwell in lines 100, 126 and 184. The notes folder is meant to be setting-free (README, second rule 6); Reader-Protocol and Pipeline already name it, so this is only a consistency nudge.
- Link hygiene: Haase 2026 is linked via awesomepapers.io; use https://arxiv.org/abs/2601.21339. Park is linked via ResearchGate; use https://arxiv.org/abs/2411.10109 (the arXiv title is "LLM Agents Grounded in Self-Reports Enable General-Purpose Simulation of Individuals", the ResearchGate copy carries the earlier title).
- Lens 12's output ("which side of each argument the book seems to take") and lens 1's "whether they'd recommend it" are opinion-laden; given the page cites Lerman, phrase lens questions neutrally.

---

## Source spot-check

| Claim (line) | Verdict |
| --- | --- |
| Haase 2026: 12 models, 12,000 samples, 10-34% within-model, quote on single-sample evaluations | Supported (arXiv 2601.21339; 100 samples per model). Prompt 36.43% / model 40.94% for originality is right but contradicts "strongest lever" (S8) |
| Haase, Hanel, Pokutta 2025 quote | Supported (arXiv preprint) |
| Anderson, Shah, Kreminski 2024 | Venue and year right. Quote 1 not found; quote 2 supported; comparator is Oblique Strategies; "each person's own ideas stayed varied" supported (M7) |
| Zheng et al. 2024 | Authors/venue/year right. Quote altered; finding is about accuracy (M7) |
| Wang et al. 2025 | Flattening supported; "more stereotyped" not in the abstract; "reduce but do not remove" matches the page's "no prompt fully fixes it" |
| Qin, Li, Cheng 2026 | Demographics-only worst: supported. "Worse again": overstated. Domain: US climate opinions (S4) |
| Park et al. 2024 | Direction supported; "far better" overstated; use the arXiv link |
| Wan & Kalman 2025/2026 | Quote supported. The "uniform setup lost" comparison is not in the study (S8) |
| Verga et al. 2024 | Right authors/year. Three families supported (Command R, Haiku, GPT-3.5). Does not test same-family sizes (S8) |
| Panickssery, Bowman, Feng, NeurIPS 2024 | Supported, including the correlation between recognition and self-preference |
| Sharma et al. 2023 | Abstract supports sycophancy in feedback; specific like/wrote conditions not verified from the abstract alone |
| Lorenz et al. 2011 | Not checked (403/429) |
| Nielsen 2000 | 85% with 5 users, 3-4 per group for two groups (3 for three or more), several small rounds: all supported. The saturation rule is not Nielsen's (S6) |
| Probst for Jane Friedman 2019/2025 | Dates right (published 2019-03-20, updated 2025-02-18). "Between two and twelve" supported. Quote altered; 92 writers; not editors (M7) |
| Lerman / CRP | Four steps as described. "Neutral questions get honest answers" not claimed (S8) |

---

# Re-review of the rewritten Reader-Panel.md (307 lines)

Status per item: F = fixed, P = partly, N = not fixed. Anchors from Pipeline, Reader-Protocol, README and History all resolve.

| Item | Status | Note |
| --- | --- | --- |
| M1 finding defined | P | Schema, matching rule, unprompted rule, top-ten all added. Gaps: no rank field, matching ignores subject, types omit knowledge/logic |
| M2 synthesiser | P | Extract per report, double merge, completeness, polarity splits all added. Gaps: extraction taggers unchecked; steps 8, noise and diversity have no named executor; "ten quotes chosen at random" by whom |
| M3 blindness / core / briefs | P | Core-second via SendMessage, sandbox, brief-writing agents, "other readers" wording all fixed. Gaps below |
| M4 chained lenses | P | Designed. Gaps: partial-text folders, core for chains, skimmer "rest is read" unclear |
| M5 families / stance / built-to-find | P | Columns added. Hostile "any" swallows everything into lens-specific; convergence now only 2 families |
| M6 informed pass | F | Step 9 plus Pipeline and Reader-Protocol edits. Cost not in the cost line |
| M7 misquotes | F (one check) | Zheng, Anderson, Probst fixed. Wan & Kalman quote reads "rather than from"; the fetched source text reads "rather from an inherent limitation of GenAI" (check) |
| S1 sizes/cost | P | Standard named, Quick scoped, 233k now cited to "harness usage report" (not in the repo records). Informed pass and calibration cost omitted |
| S2 diversity | P | Leave-one-out, core excluded, coverage, relative overlap, checker command (flags valid). Lever matrix is nominal (below) |
| S3 noise | F | Band marked untested, fixed samples, same-model repeats, suspects kept. Overlap is only as meaningful as the matching rule |
| S4 sketches | P | Roster sketches removed; exemplar added; mixed-evidence stated. Exemplar leaks tone ("distrust anything described as cozy") |
| S5 calibration | P | Per-type plants, separate copy. A second full panel per calibration, cost unstated |
| S6 saturation | F | Relabelled as the page's own heuristic |
| S7 vocabulary | F | stopper/snag/quibble and hole/late/gap/lock/rule/taste reused |
| S8 research | F | Evidence-gap paragraph, model 41% vs prompt 36%, Verga caveat, Wan & Kalman comparator, Lerman heading all fixed |
| S9 model/lens | P | Full panel runs two lenses on two models; Standard defaults still capability-matched |
| S10 leakage/sycophancy | P | Cut-before-praise rule, comparison-book ranking, questionnaire primed note. Questionnaire lens has no family/stance/built-to-find |

## New problems introduced by the rewrite

Must-fix:
1. Step 1 gives each reader the whole chapter folder, but the middle-starter ("before it's given the first half"), the skimmer chain ("only its sitting's text"), the character reader and Quick ("starting one chapter before") each need to be shown only part of the text. Say the orchestrator builds one folder per lens or per stage.
2. "This is what makes 'blind' true rather than promised" (Step 1) and "make blindness physical" (line 53; History: "physically blind") overclaim. A subagent can still read the repo and the other readers' output files. The ground rule "say what you opened by mistake" was dropped, so a peek can't be detected. Restore it, give each reader its own output folder, and soften the claim.
3. Who writes each reader's life is contradictory: line 114 says the book "writes each reader's life to fit"; line 155 says not the revising session; the drafting agent gets "the lens card alone", but the roster no longer holds any life or genre. The target reader's life needs the book's cover-level genre. Say who supplies it, and what happens when the reviewer rejects a brief.
4. Matching rule is too coarse: same type + polarity + span means any two "confusion" records in one chapter match, which inflates noise overlap, convergence and pairwise overlap, and conflicts with "Lumping isn't allowed". Add a same-subject condition (same character, object or event) decided by the merge agents.
5. The core and top ten for chained lenses (skimmer, rereader) have no recipient. Say the final agent in the chain gets them, with its own written log, or that the lens skips them.

Should-fix:
6. Lever matrix is nominal: "job" and "life" differ for every pair of distinct readers by construction, so the check only needs one more difference. Count only model, condition and stance, or require three beyond job and life. Repeat pairs must be exempt. The default Standard panel puts 5 of 9 runs on Sonnet, which breaks "no model reads more than half".
7. Top-ten ranking is used by the pairwise overlap but not in the record schema; add a rank field. Name who computes steps 5, 8 and the two checks (a script where possible; "chosen at random" should be a script).
8. Convergence now needs only two families, so in a Quick panel almost any two cross-family agreements qualify; and the hostile reviewer's "any" built-to-find makes all its findings lens-specific, never minority. Require at least two families and at least three readers in Standard and Full, and give the hostile reviewer no built-to-find tag (or treat its findings as minority unless confirmed).
9. Extraction agents tag types independently; add a small check (two agents tag a sample of records and compare). Type list lacks knowledge/logic from the reader protocol's plot-hole kinds.
10. Shared-phrasing check: the reports repeat the core questions and the schema headings in every file, so the checker will flag them; say to strip those and the quoted book text (script).
11. Exemplar reader life says "you distrust anything described as 'cozy'", which hints at the book's tone and will be copied. Reword it from reading history.
12. Cost line omits the informed pass (a reader doing the tone and rules check needs the text again, about one read) and the calibration panel (a second panel).
13. Questionnaire lens (line 133) has no family, stance or built-to-find, so Step 8 can't sort its findings.

Nice-to-have: Park link text still uses the older title with the arXiv URL; README row for the panel doesn't mention extraction or the informed pass; Quick says "a few chapters" in one place and "several" in another; skimmer chain "the rest is read only to note where it would have quit" doesn't say who reads it.
