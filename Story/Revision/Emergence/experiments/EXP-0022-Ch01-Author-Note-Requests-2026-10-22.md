# EXP-0022: Chapter 1, the author's note requests that need writing

**Date:** 2026-10-22  
**Status:** **CANDIDATES. Nothing applied.** The rest of his 2026-10-08 Ch1 notes were applied as he wrote them ([R61](../../Decisions.md#the-authors-rulings-for-this-revision), [P86](../../Pass-Log.md#p86-2026-10-22-the-authors-own-ch1-line-notes)). These six ask for something new to be written. Each one is sensory, emotional or blocking, so it's his to pick, rewrite or refuse ([who writes what](../../../Sunday-Morning/Craft.md#ai-and-the-author-who-writes-what)).  
**Source:** [his notes, verbatim](../../Author-Notes/2026-10-08_Chapter-01_line-notes.md); the [R38 disposition](../CHAPTER-01-R38-CURRENT-DISPOSITION-2026-10-16.md).  
**Aim:** his [voice guide](../../../Sunday-Morning/Sources/Voice-Guide.md): "Objects and habits should carry emotional history"; "A magical experience should sometimes be understood through the body before it is understood intellectually"; sensory detail "specific enough to trigger association".  
**Control (A):** Chapter 1 after P86.

| # | His note | Candidate | Lean | Patch |
| --- | --- | --- | --- | --- |
| C1a | ¶65: "describe the low tide better since it's the second time we have used it" | `Ooze searched through the gaps. The low tide was in the room now, close enough to taste, and it turned her stomach.` The first mention is "faint… a long way from any sea"; the second escalates by distance, then by taste | take | [C1a](EXP-0022-C1a-Ch01-Low-Tide-Taste.patch) |
| C1b | (same) | `…and the low tide came with it, stronger now: weed left to rot in a bucket in the sun. It turned her stomach.` A specific image, but a new one | | [C1b](EXP-0022-C1b-Ch01-Low-Tide-Bucket.patch) |
| C2 | ¶69: "Need to convey her panic and confusion better, she is seeing two things here, magic, and something happen to her grandmother's cookbook" | a new paragraph before the grab: `Under it, Nana's handwriting was going pale.` She sees the cost in the object before she understands the magic, so the grab is a reaction to *that*. It's the book's own rule (the ink fades as it's used, Ch10), seen first here | take | [C2](EXP-0022-C2-Ch01-Handwriting-Fading.patch) |
| C3 | ¶73: "we can be a little more poetic here" | `Her grandmother smiled, flour on her glasses, and Elizabeth felt…` One real thing from that kitchen, per the 10-08 review, rather than adjectives | take, plain; the line he's most likely to want to write himself | [C3](EXP-0022-C3-Ch01-Flour-On-Her-Glasses.patch) |
| C4 | ¶125: "Maybe some light blocking here?" | `"Huh." He stepped over the ooze and stopped short of the bathroom door.` | keep the current text: her opening the bathroom door on the next line already moves the scene | [C4](EXP-0022-C4-Ch01-Huh-Blocking.patch) |
| C5 | ¶167: "How did she go from leaving the bathroom to her attention shifting down the hall?" | `The man looked down the hall. "Shoes. Now. I did say please."` "His attention" follows her paragraph, so it reads as hers; this is the 10-08 review's fix | take: action clarity, no new content | [C5](EXP-0022-C5-Ch01-His-Attention.patch) |
| C6 | ¶39: "Might need more details here." | `Another thud, harder. The chain jumped in its track.` One physical detail; the chain is set up when she opens the door against it | take | [C6](EXP-0022-C6-Ch01-Another-Thud.patch) |

*(C5 and C6 were added after the fresh check found these two notes untracked.)*

Every patch passes `git apply --check` alone, and C1a + C2 + C3 + C5 + C6 apply together.
