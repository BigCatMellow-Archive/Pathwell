# Writing against sameness

## Status

**Procedure, active. Created 2026-09-30 in [pass P5](Pass-Log.md#p5-2026-09-30-craft-adjustments-and-ai-tells).** This page owns how the revision writes and checks for *sameness*: the same few polished moves, used successfully and evenly everywhere. That's what the [AI-detection read](AI-Detection-Notes-2026-09-30.md) of Chapter 12 showed, and it's what makes prose read as generated. The fix isn't to hide anything. It's to write the book the voice sources already describe ([R18](Decisions.md#the-authors-rulings-for-this-revision)). For Pathwell only, for now.

Almost nothing here is new. The [voice guide](../Sunday-Morning/Sources/Voice-Guide.md) already says "everyone sharing the same sense of humor", "constant quipping" and "self-consciously clever narration" are to be avoided. The [narrator register guide](../Story_Files/pathwell_narrator_register.md) says when the narrator speaks and when it steps aside. [pathwell_prose_voice.md](../Story_Files/pathwell_prose_voice.md) says "the wrong detail is the character". This page turns those into steps a pass can follow and a check can test. The list of common AI tells to be aware of is in [AI-Tells](AI-Tells.md).

These are guides for judgment, not rules to satisfy. Any of them can be broken on purpose. What they catch is a move made by habit.

## Before writing a scene

1. **Map the register.** Mark each stretch of the scene with the [narrator register guide](../Story_Files/pathwell_narrator_register.md):
   - **Narrator quiet:** action, sensation and magic, any stretch with Shade in frame, and the line after a punchline.
   - **Narrator present:** arrivals, transitions, aftermath, character observations (one line when someone does something characteristically themselves), and what Elizabeth hasn't named yet.

   The narrator's attitude goes only where the map puts it, and even there it's usually small: "anyway", "probably", "which turned out to be", the wrong detail noticed, an absence noted. As a rough suggestion (not the guide's wording), once per stretch, not in every paragraph; the guide says to use it "sparingly".
2. **Know whose joke it is.** Each character's humour has its own source ([character bible, voice](../Story_Files/character_bible.md#voice-all-characters)). Before a joke goes in, ask whether someone else in the scene could have said it. If they could, it probably isn't that character's joke yet; consider changing, moving or cutting it.
3. **Let the situation be funny first** (voice guide). If a scene is funny, the characters are usually sincere in it. If only the phrasing is funny, the scene is being decorated.

## While writing

- **Elizabeth thinks like a person.** Her interior runs body-first ([prose voice 1](../Story_Files/pathwell_prose_voice.md#1-body-first-interiority)), in worries and lists, with wrong guesses and half-finished thoughts. The benchmark is the Chapter 2 run of worries: the landlord, the door, the dry cleaning, the meeting. A line in which she names her own psychology neatly ("she could tell herself she'd only moved the checking somewhere safer") is emotional material. Flag it for the author; don't polish it.
- **Usually no more than one polished closing line per scene.** A closing line here means an aphorism, a neat reversal, a two-part antithesis ("The diary belonged to Camp now. The life in its pages was still hers."), or a "for the first time" turn. A suggestion from the research rather than the guides: most paragraphs can end on an action, a line of dialogue or a plain fact. When a scene has two closing lines, keep the one that's earned.
- **Some texture is just texture.** Not every object in a room has to be a callback, a symbol or a setup. A wagon can have a thing in it because wagons have things in them.
- **Vary the move, not the words.** Swapping synonyms doesn't help. If the same construction ("nodded as though X were a Y") has been used nearby, the next beat needs a different kind of move: an action, a line of dialogue, or silence.
- **New emotional lines and new jokes are the author's.** When a fix needs new text in those categories, put in the plainest version that does the job and list it for the author with an alternative or two. Keep it plain and flag it. P4's own new lines were among those the detector flagged hardest ([notes, point 4](AI-Detection-Notes-2026-09-30.md#what-it-teaches-this-revision)).
- **Don't make it worse on purpose.** Avoid typos, filler, random fragments and deliberate clumsiness. The aim is the book the guides describe, not prose that fools a detector.

## After writing

These run inside [after every pass](README.md#after-every-pass).

- **Two benchmarks, not one number.** Compare interiority, the senses and how distinct the voices are with the author's own [Chapters 1–2](Voice-Benchmark/README.md). Compare the narrator's presence with the register guide's calibration lines. The checker's counts (contractions, "Not…" fragments, commentary paragraphs) are a floor, not the test.
- **The Registry tracks joke shapes**, as it tracks names and openings: [joke shapes already used](Registry.md#joke-shapes-already-used). The checker's watch patterns count the ones a pattern can catch ("as if / as though X were…"). A count is a pointer for reading.
- **The fresh check reads for sameness.** Beyond drift, lost setups and continuity, the independent reader answers these:
  1. Is any joke construction, closing line or gesture repeated within the chapter, or from the chapter before or after?
  2. Does each joke belong to the character who says it? Could any line move to another character without changing?
  3. Is the narrator speaking where its register says to step aside (action, sensation, Shade, after a punchline)? Is it quiet where it should be present?
  4. Does Elizabeth's thinking read like a person thinking, or like an explanation of her?
  5. How many polished closing lines does each scene have?
  6. Does anything on the [AI-Tells](AI-Tells.md) list cluster here?
- **Leave the detector out.** A detector score isn't a check here ([R17](Decisions.md#the-authors-rulings-for-this-revision)).
