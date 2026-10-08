# Reader panel 2026-10-08: synthesis

**Text read:** Chapters 1–18 at commit 281524a, unchanged at HEAD.
**Panel:** nine runs by eight lenses in four families: experience (target ×2, reluctant, skimmer), audit (continuity auditor, rules reader), craft (character reader on Shade, prose reader), adversarial (hostile reviewer).

**Lean finish (the author's choice, 2026-10-08).** To save cost, the orchestrating session did the sort, the informed check and the goals comparison itself, from the script's counts. The protocol asks for a fresh synthesis agent and a separate informed-pass agent. So this file combines the protocol's `synthesis.md`, `informed-pass.md` and `alignment.md`. The full D24 tone and rules check was not run on the findings.

**Counts:** [counts/](counts/), made by [panel_counts.py](../../../Sunday-Morning/tools/panel_counts.py). Every cluster in either merge is in `clusters_A.csv` and `clusters_B.csv`, with its readers, families, severity and category. The lists below show only findings at snag or above (and strong strengths). Quibbles stay in the CSVs and are not dropped.

## 1. The two merges

| | Merge A (Sonnet) | Merge B (Haiku) |
| --- | --- | --- |
| Records in, rows out | 883 / 883 | 883 / 883 |
| Clusters | 649 | 632 |
| Clusters mixing type or polarity | 0 | 0 |
| Convergent clusters (any severity) | 43 | 43 |

- **Agreement.** They agree on 77% of the record pairs either one grouped (Dice 0.77). 452 records are singletons in both.
- **Disagreements.** 102 multi-record clusters in A are grouped differently in B; they are listed in [merge_compare.md](counts/merge_compare.md). Most are one record more or less.
- **B lumped more.** B itself named C136 (one dry register), C141 (narrator explains), C097 (the accession cards) and C044 (Hearts) as its likeliest over-lumps.

**Quotes.** Ten records were drawn at random (seed 20261008) and checked against the chapters: 10/10 are in the text. One of them spans a paragraph break (Ch5:208–210). Across the whole set, 704 of the 749 quotes match verbatim after normalising punctuation; the remainder are mostly quotes with ellipses or quotes spanning a line break.

## 2. Convergent (two or more families, three or more readers, unprompted)

"Both" means both merges sort it as convergent; "A only" and "B only" are listed, not resolved.

### Problems

| # | Finding | Ch | Sev | Readers | Families | Merges |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Rai Stones, Lydian coins and the bill's currency are never explained | 3 | **stopper** | reluctant, skimmer, hostile | 2 | both |
| 2 | Restitution scenes list their items and repeat the point | 16–17 | **stopper** | auditor, skimmer (+target-2 in B) | 2 | B only (A: short of convergent) |
| 3 | The Hearts game runs long and drains the threat | 13 | snag | 5 | 3 | both |
| 4 | The diary donation (Ch12) repeats the cookbook donation (Ch4) | 4, 12 | snag | 4 | 3 | both |
| 5 | "That was the choice." repeated | 4, 15 | snag | 4 | 3 | both |
| 6 | "He still has it." — who and what is unclear | 2 | snag | 3 | 3 | both |
| 7 | Elizabeth's own want is thin or unclear | whole book | snag | 3 | 3 | both |
| 8 | Ch8 reopens with Ch1's first line | 1, 8 | snag | 3 | 3 | both |
| 9 | Milo's sock gag repeats | 4–15 | snag | 4 | 3 | both |
| 10 | Stansbury's "Leo" / "big cat" is never explained | 10 | snag | 5 | 2 | both |
| 11 | Who asked Pathwell for the prune, and what the problem was, is never said | 5–18 | snag | 4 | 2 | both |
| 12 | Day-of-week slips (Thursday/Saturday/Friday) go unacknowledged | 2–5 | snag | 3 | 2 | both |
| 13 | Why the blob was already at her door before the cookbook was used | 1–15 | snag | 3 | 2 | both |
| 14 | Why Pathwell was in her flat, and whose door it was, is never answered | 1–17 | snag | 3 | 2 | both |
| 15 | Pathwell repeats "I can contain this" and the same mistake | 10–14 | snag | 3 | 2 | both |
| 16 | Every character speaks in the same dry register | 4–18 | snag | 4 | 3 | B only (A splits it: C134, C135, C137, each 2 readers) |
| 17 | The narrator explains what the scene already showed | 4–18 | snag | 4 | 3 | B only |
| 18 | The magic has no plain rules to judge choices by | 1–18 | snag | 3 | 2 | B only (A: C035, 2 readers) |
| 19 | Ch17's aftermath and recap passages run long; summary paragraphs restate the arc | 17 | snag | 3–4 | 2 | B only (two clusters) |

Convergent quibbles (both merges): the Camp roll call drags (Ch4); Bakhtak is never explained (Ch5); "how much machine she was responsible for" (Ch7); "Lizzy" comes before she gives the name (Ch2–3); the second-person town aside (Ch5); Milo in the burning archive is stock peril (Ch14).

### Strengths (both merges unless marked)

- **The Ch4 cookbook give** — the whole book for one page. 4–5 readers.
- **The Merritt marginalia**, "RUTH LIED ABOUT THE LARD" (Ch4, Ch18). 5–6 readers, 3 families.
- **The bookshop:** "Not books — lives", and Pathwell paying in potential (Ch3). 4–5 readers.
- **Elizabeth's car speech** (Ch7) and **the deliberate crash** (Ch8). 5 readers each.
- **The museum accession cards** and Sam's eggs (Ch11). 5 readers.
- **The fire takes the diary and cookbook** — "No spell. No sacrifice." (Ch15). 4–5 readers.
- **"You were never the point"** (Ch9).
- **The van:** the confession, the unsent letter, the grocery lists (Ch10).
- **The archive burning** (Ch14).
- **Stansbury's responsibility speech** (Ch14).
- **The opening image** of the diary read like a magazine (Ch1); A only.
- **The changed street** (Ch2).
- **"Wet. Heavy."** (Ch6).
- **"Same ingredients. Different recipe."** (Ch8); A only.
- **The healer asks permission** (Ch12); A only.
- **"PATHWELL IS NOT DONOR"** (Ch12).
- **Shade's ledger entry** (Ch16).
- **Elizabeth refusing to make his guilt useful** (Ch16).
- **Mama Baga's restitution refuses the grand gesture** (Ch16); A only.

## 3. Short of convergent (two lenses or more, below the bar)

The protocol's four lists have no place for these, so they have a list of their own; a protocol fix is noted in §9. All are at snag or above.

**Stoppers:**
- **Shade's death feels convenient or unneeded** (Ch15). Character reader and target-2.
- **Olan and Hess are named with no context** (Ch4, Ch17). Reluctant reader and skimmer.

**Problems at snag:**
- **Shade's reason for volunteering isn't stated** (Ch15). Character reader and target-1.
- **The waste-creature rule ("unpleasant rather than murderous") is dropped** when Shade dies (Ch5, Ch15). Hostile reviewer and rules reader.
- **The cookbook page count:** two pages were used, and the card says one (Ch1–12). Auditor and rules reader.
- **The wrecked Cadillac and fence** are never resolved (Ch8–11). Auditor and rules reader.
- **The Ch11 museum blast:** readers lost track of who was where, and it reads as spectacle. Rules reader, skimmer and target-2.
- **The five-routes exchange runs long** (Ch18). Three experience readers.
- **"Perfect." is repeated at both bookends** (Ch1, Ch18). Hostile reviewer and prose reader.
- **Phrases shared across characters:** the "important distinction" catchphrase, and "Not X. Y." pairs (Ch4–18). Prose reader and target-1.
- **Things never explained:**
  - "marked" (Ch1);
  - the blob (Ch1);
  - the pull (Ch6);
  - what Shade is (Ch8);
  - the mirror (Ch6–8);
  - Thumper (Ch12);
  - the unnamed archivist and older woman (Ch13);
  - Pathwell's promise to answer all her questions (Ch3).

  Mostly the reluctant reader and the skimmer, with the rules reader.

**Strengths:**
- Shade refuses to be the anchor (Ch14). Four readers.
- Shade walks into the blob: "You still owe me a hand." (Ch15). Three readers.
- Pathwell offers Henry Vale's letters, then takes the offer back (Ch17). Three readers.
- Camp keeps asking Shade what he wants, and the coffee exchange (Ch13). Three readers.
- The queen of spades, laid early and paid late (Ch13–17).
- "Will you stay?" / "No." (Ch15).
- **The Ch18 cookbook put-back** with no speech. Hostile reviewer and target-2.
- "Do you want to come?" hands the choice back (Ch18).
- Costs are real and carried through: the shoulder, the scar, Shade.

## 4. Lens-specific stoppers and snags (found only by the lens built to find them)

All four pacing stoppers come from the **skimmer**, at the points where it would have stopped reading:
- the "Which prune?" loop (Ch7–8);
- the narrator's crossroads-town paragraph (Ch5);
- the soldier's poem in the museum (Ch11);
- Mama Baga's "Stop" section (Ch14, about lines 379–463).

The auditor's continuity snags, the rules reader's rule snags and the character reader's Shade findings are in `clusters_A.csv` (category "lens-specific", 53 at the floor in each merge).

## 5. Minority reports (one reader, outside its own types), stoppers

- **Prose reader:** Elizabeth complies and leaves too fast; it stopped believing at "Do you have shoes?" (Ch1).
- **Auditor:** Elizabeth drives off the road on purpose and the others shrug it off (Ch8). This one is a split: five readers call the crash a strength.

The hostile reviewer's 15 unique findings at the floor are all minority by rule. The full list is in the CSVs.

## 6. Splits (the same subject praised and faulted)

- **The Hearts game (Ch13).** Five readers say it runs long. Two say it's where Shade becomes a person, and three praise the Camp asking Shade what he wants. *Trim it; don't cut it.*
- **The Ch8 crash.** Five readers call it a strength; the auditor (stopper) says the others shrug it off.
- **The Ch11 museum.** The accession cards are convergent praise. The blast and the soldier's poem are faulted.
- **Restitution (Ch16–17).** Mama Baga's refusal of the grand gesture and Shade's ledger entry are praised. The lists and repeated scenes are faulted (a stopper in B).
- **"Perfect." / "Ready?" "No." "Perfect."** The skimmer likes the bookend; the hostile reviewer and the prose reader call it a repeated button.
- **Fragments.** The prose reader praises the "Not X. Y." runs that earn their place in Ch4 and Ch15, and faults their overuse in Ch4–13.
- **Shade's death (Ch15).** The exit lines and "Shade closed it himself" are praised. Two readers call the death convenient, and two say his reason isn't stated.

## 7. Checks on the panel

**Noise check.** The two target runs overlap 36% (A) or 31% (B) on findings at snag or above. That is under the 40% working band, so a single run of the target reader can't be trusted alone; repeat it again next time. As the protocol says, it's one number from two runs.

**Diversity check** (top-ten overlap, Dice):
- **The repeat pair:** target-1 / target-2 score 0.22.
- **Different lenses:** a mean of 0.03 (A) and 0.04 (B). The panel is not one reader nine times.
- **The one flag:** prose / target-1 scores 0.20–0.21, as close as the repeat pair. They share four top-ten items:
  - "important distinction";
  - "Not X. Y.";
  - "That was the choice.";
  - the repeated donation. Both readers are Sonnet; the prose reader was meant to be Opus.

**Unique contribution** (findings at the floor that only this reader or family found):
- Every reader added some: from 10 (target-2) to 35 (the skimmer).
- By family: experience 105–109, craft 38–40, audit 30–34, adversarial 15.
- The hostile reviewer's unique findings are all outside its "built to find" types, by design.

**Coverage.** Every type has records.
- Thin: rule (18 records), knowledge (22), motivation (24). Motivation came mostly from craft and experience.
- **No reader read for motivation as its main job.** The book-club host and the developmental editor were not in this panel.

**Lens adherence** (step 5): every lens produced its own format.
- The skimmer gave an attention map with a stop line.
- The auditor kept its table.
- The reluctant reader named its quit point.

**Prompted.** The character reader's brief named Shade, so 45 of its 54 records are marked prompted (per the extraction rule) and don't count toward convergence. Several Shade findings sit just under the bar because of that.

**Shared phrasing.** One five-word phrase appears in three reports: "in order of how much" (prose, target-1, target-2). It traces to the shared ground rule "name what you'd cut before what you'd praise". This is not a sign of one voice.

## 8. Informed check: the findings against the records (lean)

Labels are the reader protocol's.

| Finding | Label | Note |
| --- | --- | --- |
| Opening premise: why he was in her flat, whose door it was, the blob already there, "He still has it", "Lizzy", the page count (#6, #13, #14, short list) | **gap** | The 10-06 whole-book reader's top finding, now confirmed by three families independently. The canon has the answer (he followed charged material); the page doesn't give it. The page count is accurate (the Ch12 card counts only Camp's use), but without the cookie page's fate it reads as a contradiction. **The biggest finding of the panel.** |
| Who asked for the prune (#11) | **gap** / author's call | Withheld on purpose? No lock found that says so. Four readers want it. |
| The currency in Ch3 (#1) | **gap** | A stopper for three readers, two of them built to find confusion. One line of gloss in Pathwell's voice would carry it. |
| Elizabeth's own want (#7) | **gap** | Matches the climax-rule finding (09-18 §3, put to the author in P40) and the 10-06 reader's wish for "one moment in which Elizabeth says what she wants". |
| Narrator explains; "That was the choice." (#5, #17) | **taste** (leans in question) | The 10-06 reader named the same lines. The leans kept in P38–P43 have now been faulted by four or more readers in three families. Recommend cutting them. |
| One dry register; shared catchphrases (#16, short list) | **taste** | Matches the 10-06 reader's sameness note. The prose / target-1 overlap means it is partly one model's taste, but it's convergent in B. |
| The diary donation repeats the cookbook (#4) | **gap** | Matches the 10-06 reader ("set up to burn"). The fix is a stronger want of hers at the give, not a cut. |
| Ch8 reopens with Ch1's line (#8) | **lock** (R11) | The author asked for the echo, bare. Three families noticed it and read it as repetition. Push back (R26): the echo registers but doesn't land as a choice. Worth a word with the author; leave it unless he changes it. |
| Milo's sock (#9) | **lock** (R32, Promise-Ledger R11) | A running gag with a payoff in Ch15. Four readers find it repeats. Lean: keep the gag and drop one middle use. |
| "Leo" / "big cat" (#10) | **late** (Promise-Ledger L15, open) | The ledger already suggests one later use. Five readers confirm it. |
| Day-of-week slips (#12) | **taste** | Pathwell's patter in Ch2 and Ch5; readers took it for errors. One acknowledgement from Elizabeth would fix it. |
| "I can contain this" (#15) | **lock** (P39) | Planted on purpose as his flaw repeating. Readers caught the repetition, which is the point. No change. |
| Restitution lists (#2), Ch17 recap (#19), the Ch16 hearing | **taste** | Matches the 10-06 reader's weakest chapter. Trim the lists; keep Mama Baga's refusal and the ledger entry. |
| The Hearts game (#3) | **taste**, split | Trim within the scene; protect "I want to stay here." / "Then stay." and the coffee. |
| Shade's death convenient; his reason not stated (short list) | **gap** | P40 added his reason line; it still isn't landing for 2–4 readers, as with the 10-06 reader. |
| The skimmer's stop points (Ch5 town, "Which prune?", the poem, the "Stop" section) | **taste** | The Ch5 cut matches the 10-06 reader's wish to cut Ch5 down. |

## 9. Against the goals (the goals key, opened last)

What the blind panel found, goal by goal:

- **Elizabeth's rungs: partly.**
  - The panel praises her choices in Ch4 (the cookbook), Ch7 (the car speech), Ch8 (the crash) and Ch16 (refusing his guilt), all unprompted and across families.
  - Rungs 1–2 (Ch3, Ch4's forest) don't appear.
  - Her own want is a convergent problem.
- **Earned beats: mostly yes.** The protected beats are almost all on the convergent strengths list: the cookbook give, the marginalia, the fire with no payoff, the ledger entry, "You were never the point". The Ch13 coffee and Shade beats are just under the bar.
- **The climax rule: not met, as recorded.**
  - No reader names Elizabeth's rescue as a turning point.
  - Milo's peril is a convergent quibble ("stock").
  - Shade's death is a stopper for two readers.
- **Pathwell's change: aligned.** The van confession is convergent. The Henry Vale retraction and the Ch18 put-back are praised. No reader reads the put-back as replacing Nana's book; that is consistent with the 10-06 reader, and the motive still doesn't come through.
- **Losses stay lost: aligned.** The fire, the shoulder, the scar and Shade's death are named as real costs.
- **Tone, and no narrator grading: partly.** The narrator-explains finding is convergent (B), and so is the dry register.
- **The opening premise.** Not a goal on the key, but it's the book's first question, and the panel confirms it is the top gap.

## 10. Protocol notes for next time

- Add **"short of convergent"** to step 8: two or more lenses, below the bar.
- Repeat the target reader three times, since it is under the noise band.
- Get Opus for the prose and rules readers.
- Add a motivation lens (the book-club host or the developmental editor).
- For a character lens, decide in advance whether its findings about the named character count toward convergence. This run said no.
