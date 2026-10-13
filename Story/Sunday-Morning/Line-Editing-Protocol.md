# Line-editing and revision verification protocol

**Status: active operational procedure, initial implementation 2026-10-13 (D26; trial needed).** This page owns **how to diagnose, change and verify prose from the individual word through the chapter**. It is a procedure for editors and independent reviewers, not a universal formula for creative choices. The author's voice and rulings still govern taste. [Craft](Craft.md) owns *what strong prose does*, [Pipeline](Pipeline.md) owns the project workflow, [Reader protocol](Reader-Protocol.md) owns blind reading/causality, and [Line notes](Line-Notes.md) owns worked evidence behind earlier rules. Do not replicate those owners here.

**Use for:** a requested word/line edit, an author's margin notes, a prose-polish pass, or inspecting a proposed diff. For a full chapter, run the levels in order. For a two-word change, use the compact path in §7. This is not a demand to rewrite everything or fill out a form for every comma.

## 1. Non-negotiable gates

1. **Read the actual passage and its neighbors first.** Read enough before/after to understand speaker, viewpoint, time, staging, information and current emotional beat. The story is evidence; a summary or Bible does not replace it.
2. **Find the highest-level defect first.** Book/scene cause, chronology, motive, and character knowledge outrank paragraph flow; paragraph flow outranks sentence rhythm; sentence meaning outranks single-word polish. Do not beautify a line in a scene whose causal premise may change.
3. **State a concrete diagnosis before a rewrite.** “Awkward,” “flat,” “more literary,” “needs depth,” “AI-ish,” or “sounds better” are not self-proving failures. Identify the phrase, the reader effect, and a reason grounded in the text or an author ruling. If it's taste, label it taste and leave room for KEEP.
4. **Use the smallest sufficient intervention:** KEEP → CUT → REPLACE A WORD / PHRASE → REPAIR A SENTENCE → MOVE A BEAT → REWORK A SCENE. A larger change requires evidence that the smaller one fails. Deletion can be the finished fix; don't compensate with an explanatory sentence.
5. **Preserve who knows, who chooses, and who speaks.** New wording cannot quietly grant knowledge, mind-reading, cause, moral authority, a different temperament, or an event that hasn't happened. An author-side thematic interpretation is not automatically a character's conscious thought.
6. **No rule-by-keyword editing.** “Was,” “felt,” “saw,” “very,” “that,” adverbs, passive voice, fragments, repeated words, and short sentences can all be correct. Automated counts are search flags, never a replacement instruction or an automatic failure.
7. **A rewrite must survive a regression check.** Compare original and revised passage; read aloud; check local neighbors, continuity, foreshadowing/payoffs, and whether the new wording creates another tic. Don't call a pass finished merely because the new sentence is grammatical or prettier.
8. **No self-approval of consequential work.** Follow [Pipeline's after-every-pass routine](Pipeline.md#after-every-pass), including its recorded skips, and [Reader protocol](Reader-Protocol.md) as applicable. A blind reader sees the text **before** editorial goals or a diff. Editor and reviewer are separate for substantive changes. Don't claim checks ran if they didn't.

**Result labels:** `KEEP` (working text), `CUT`, `REPLACE`, `MOVE`, `OPEN` (missing fact or author choice), `FLAG` (voice/taste or uncertain impact), `REVERT` (candidate worsened the text). Each applied change points to an identifiable problem; not every reviewed line receives a change.

## 2. Fixed order of an editing pass

| Pass | What to test | Leave this pass with | Do not do yet |
| --- | --- | --- | --- |
| **A. Story contract** | Existing author ruling; chapter purpose; viewpoint; what characters know; fixed world rules; promise ledger; what the scene must leave behind | a short list of constraints and actual unresolved questions | infer new canon from a tempting fix |
| **B. Causal read** | Staging, props, time, physical ability, knowledge transfers, motives, reaction → later decision, chapter seam | verified faults and open questions at their proper level | polish vocabulary to conceal causal holes |
| **C. Paragraph and dialogue read** | Beat order; focus; response to previous line; voice and speaking motive; what can be inferred without explanation | paragraphs and exchanges that carry the intended action | scatter new gestures or slogans |
| **D. Sentence and word read** | Referents, syntax, precise meaning, implications, diction, sound, rhythm, repetition, jargon, punctuation | the smallest candidate edits with before/after evidence | blanket-find/replace stylistic tokens |
| **E. Regression and review** | Old versus new; read aloud; story-state ledger; nearby lines and cross-chapter dependencies; repeated replacements; independent reader | `KEEP`/`CHANGE`/`REVERT` dispositions with check status | declare a chapter approved from an unverified diff |

**Routing:** A broken premise goes to THINK, a missing beat or wrong scene order to PLAN, a sentence-level repair to DO, a new canon/taste ruling to the author ([Pipeline Stage 3](Pipeline.md#stage-3--do-draft)). The protocol does not authorize an editor to choose open lore.

## 3. Exact tests by editing scale

### Word: meaning first, then music

Before replacing a word, answer:

- **Denotation:** Does it name the right object, action, quantity, tense or certainty? “Again,” “still,” “already,” “finally,” “only,” “back,” and “another” imply a prior state; verify one exists.
- **Connotation:** Does it smuggle in an unintended mood or fact? “Crisp” paper can imply newness; “snatched” implies more force than “took”; “allowed” implies power to grant permission.
- **Speaker/register:** Would *this* character or this viewpoint narrator choose it? Ordinary feeling is not automatically formal analysis. Keep names for tracked objects consistent unless a change is intentional.
- **Reference:** Can the reader identify the `it`, `she`, `that`, `there`, or `again` without rereading? Check especially after inserting a character action: the next pronoun may change owner.
- **Emphasis/sound:** Does replacing it actually improve clarity, rhythm, or voice without flattening a deliberate repetition? A poetic synonym is not intrinsically stronger.

**Disposition:** change one word only if a real distinction improves; then reread **the whole sentence and neighboring sentences**. Keep the original if the new word is merely fancier.

### Sentence: who does what, when, and why this phrasing?

- **Subject/agency:** The doer is intelligible; an object has not taken agency away from a person unless that is the intended image or mechanism.
- **Information order:** Prerequisites exist *before* the sentence relies on them. A poured drink may be raised; an unopened drink cannot be drunk; the viewpoint cannot identify an unknown person by name.
- **Grammar and referents:** No accidental tense jump, dangling modifier, ambiguous pronoun, or changed certainty (“could” versus “would”).
- **Inference:** Cut a sentence that tells readers the conclusion the previous action already let them reach, **unless** the narrator's interpretation adds a distinct perception.
- **Voice and breath:** Read it aloud. Natural speech can be fragmentary, repetitive, indirect or blunt. Fix tongue-twisting or generic cadence only when it obstructs the intended character or moment.
- **No meaning drift:** A rewrite does not turn a conditional possibility into a fact, an argument into a resolution, or a momentary emotion into a lifelong diagnosis.

### Dialogue exchange: it must be something these people would say *here*

- For each speaker, record mentally: **want / knows / believes / is avoiding / hears from the previous line**. The spoken line must be possible from that state.
- Each reply should respond to the other person (directly, by deflection, refusal, joke, change of subject, interruption, or deliberate silence) rather than alternate author speeches.
- If a character warns, persuades or manipulates, identify the **personal payoff**, the **basis for their claim**, and **how the words might change the listener's choice**. Truth can be used deceptively; that is a character act, not evidence that the narrator endorses the warning.
- Remove information both speakers already know unless there's a reason to repeat it (accusation, mockery, confirmation, ritual).
- Read the exchange with dialogue tags removed: can the reader still distinguish voices and track the speaker changes? If not, fix what genuinely confuses; do not impose catchphrases.

### Paragraph: one intentional beat, no duplicated work

- Identify the paragraph's main job: perception, action, reaction, decision, transition or deliberate pause. It may do several; it shouldn't mechanically repeat the previous paragraph's emotional conclusion.
- Check **sequence:** stimulus → a plausible reaction (which may be confused) → action after whatever time or information is needed. Do not jump straight from revelation to the location the outline requires.
- Break paragraphs for real changes in speaker, emphasis, action or attention; don't put every dramatic sentence alone, or add a quiet line solely to manufacture significance.
- **Cut test:** If removing a sentence changes no fact, emotion, rhythm, voice, pacing or setup, cut it and reread. If removal makes the beat abrupt or incomprehensible, restore or repair.

### Scene and chapter: verify the smaller edits did not change the story

- **Scene:** Who comes in wanting/avoiding what? What information, cost, relationship or practical situation changes? Does the final response grow from the scene instead of the next plot requirement? What is deliberately left uncertain?
- **Chapter:** Reconcile entrances/exits, times, distances, objects, injuries, knowledge, emotional timing, world-rule costs, promises, and the following chapter's starting state. Payoffs and planted details outrank elegant micro-edits.
- **Book:** When a line changes a claim, clue, recurring object, naming choice, or character motive, find its other appearances and reconcile them. Don't reopen the whole book for an adjective that has no wider dependency.

## 3A. Coverage rule for a complete line-edit review

**A full line-edit review covers the entire requested scope in reading order**, including lines the editor expects to keep. Don't inspect only suspicious phrases or cherry-pick elegant alternatives. For each paragraph, test its purpose and transitions; for each sentence, run the §3 sentence checks; at points where meaning, voice or clarity depends on a particular word, run the word test. **Do not manufacture a finding for every sentence.** Record the exact ranges actually read, all actionable exceptions, and representative passages deliberately kept. Then inspect proposed changes as a separate diff audit.

**A surgical request covers less:** the named words/lines, surrounding paragraph and any specifically affected dependencies. Report that limited scope truthfully rather than saying the chapter was reviewed.

## 4. Issue classification: what a reviewer can actually require

| Class | Evidence | Priority | Normal disposition |
| --- | --- | --- | --- |
| **FACT / CAUSE / POV / KNOWLEDGE / LOCK** | Specific passage contradicts a preceding event, a character's access to information, a rule, or a binding author decision | **blocker** if consequential | fix at correct level or flag authority conflict |
| **CLARITY / CONTINUITY** | Careful reader loses who acts, when, where, why, or what pronoun refers to | **stopper** or **snag** | smallest clarifying change; recheck neighbors |
| **VOICE / CADENCE / REDUNDANCY** | Concrete repeated construction, register mismatch, duplicated explanation, or unnatural response *in context* | **snag** or **taste** | candidate cut/rewrite; read aloud and compare |
| **STYLE / PREFERENCE** | Another valid phrasing sounds preferable to an editor but has no demonstrable loss | **taste** | KEEP by default, or offer as an option |
| **UNKNOWN** | Mechanism or motive is not established; available pages don't answer | **open** | preserve as unresolved; ask/plan rather than invent |

Use the existing reader labels `hole`, `late`, `gap`, `lock`, `rule`, `taste` and severity `stopper`/`snag`/`quibble` when writing an [independent reader report](Reader-Protocol.md#sorting-open-questions-pass-2). The table above is **editing priority**, not a replacement for reader findings.

## 5. Required edit trace (compact; for each material change, not each comma)

```text
Location: chapter/scene and exact quote (or line range)
Finding: observed failure and its evidence; class / severity
Intent: what the existing line must still accomplish
Disposition: KEEP | CUT | REPLACE | MOVE | OPEN | FLAG | REVERT
Before → After: exact text if changed
Ripple check: adjoining sentences; facts/objects; speaker knowledge; voice;
              setup/payoff; adjacent scene/chapter (as relevant)
Verification: read aloud / diff inspected / reader reviewed / not run (reason)
```

A batch of local word fixes can share one short trace when they have the same cause, but high-risk changes need their own evidence. Don't produce this entire template in the book itself. Record findings in the existing story development record or pass log; no extra spreadsheet, issue tracker or compulsory document.

**Review output rule:** Report **what was kept as well as what changed** when it matters. Reviewers are not paid by the number of edits. A clean paragraph can earn KEEP.

## 6. Worked calibration from an actual Pathwell passage

The Chapter 9 diner once had Shade answer Elizabeth's conditional question with “Then you were never the point” and add “Of whatever followed him. Don't make that sentence larger than it is.” The author challenged the second line. Test it:

- **Evidence:** Shade has no demonstrated access to the private significance Elizabeth attaches to the news. The qualifier editorializes the reader's inference instead of advancing Shade's agenda or answering a question.
- **Class:** voice/redundancy, with character-knowledge risk. **Fix:** CUT the explanatory aside, not replace it with another polished warning. **Preserve:** the *conditional* “Then” because Shade cannot know what brought the first creature.
- **Regression:** Elizabeth still hears the discovery; her follow-up question and Shade's limited knowledge still make sense. Cross-reference Pathwell [pass P45](../Revision/Pass-Log.md#p45-2026-10-12-chapter-9-diner--remove-shades-explanatory-aside).

**A distinct unresolved example:** In the same diner, Elizabeth presently says “I'm going back” and later starts walking toward Pathwell. The author's October 13 discussion suggests she may first be angry and confused. **This is not automatically a line-edit defect.** It is a possible emotional-transition issue at the *scene* level, to examine before changing her dialogue. See [the exploration record](../Revision/Chapter-09-Character-Dynamics-and-Camp-Access-2026-10-13.md#october-13-return-to-the-diner--emotion-before-destination-open-not-implemented).

## 7. Minimum path for a truly small edit

For a single word/line requested by the author, the editor needn't perform a fake full-book investigation. **Still do these five things**:

1. Locate the exact current text and read its paragraph plus enough before and after to hear the exchange; check an affected rule/lock if relevant.
2. State one sentence: what this change corrects, and whether it is fact/clarity/voice or author taste.
3. Make only the necessary change; explicitly preserve important phrasing and facts nearby.
4. Compare exact before/after; check new pronoun references, punctuation, rhythm aloud, and any obvious related callback.
5. Record the diff-derived result and which [Pipeline](Pipeline.md#after-every-pass) checks were done, skipped (why), or not applicable. If a change is consequential, use an independent cold reader; do not represent a local check as full L4 approval.

## 8. Stop and escalate

- **STOP / THINK:** The wording only appears wrong because the scene's motive or world mechanism doesn't work. Fix the plan, not the adjective.
- **STOP / AUTHOR:** Two binding rulings contradict each other, or a scene needs an unchosen world fact. Record both and ask rather than quietly select one.
- **KEEP:** A reader understands and the apparent imperfection is part of this person's voice, humor, or lived moment.
- **REVERT:** The revision introduces a new inconsistency, generic voice, a doubled explanation, a worse transition, or an unearned claim.
- **FLAG:** The best answer depends on the author's particular taste or a new defining emotional/philosophical line. Supply the plainest functional alternative, not an unsolicited grand statement.

The goal is **fewer justified changes and fewer unnoticed errors**, not a higher edit count or more sophisticated-looking prose.
