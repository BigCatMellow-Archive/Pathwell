# Blind A/B read: the diner and Shade's death (2026-10-23)

**What it tested:** whether [EXP-0024](../../Emergence/experiments/EXP-0024-Diner-and-Shades-Death-Candidates-2026-10-23.md)'s six candidates (D1, D2, S1–S4) make the diner and Shade's death land harder for a reader who knows nothing about the goals. Reconciled in EXP-0024 ("Test: two blind readers, A/B") and [P88](../../Pass-Log.md#p88-2026-10-23-the-diner-and-shades-death-exp-0024-with-a-blind-ab-read). It also overturned most of [EXP-0023](../../Emergence/experiments/EXP-0023-Whole-Book-Resource-Review-Candidates-2026-10-23.md)'s cuts ([INS-0002](../../../insights/INS-0002-check-blind-reader-logs-before-cutting-a-line.md)).

**Status:** evidence, not authority. One reader per arm.

| File | Reader | Text read |
| --- | --- | --- |
| [READER-A-CONTROL.md](READER-A-CONTROL.md) | fresh agent, blind | `Story/Chapters/` at `5817524` (P86): the control |
| [READER-B-CANDIDATES.md](READER-B-CANDIDATES.md) | fresh agent, blind | the same, with the six `EXP-0024-*.patch` files applied |

Each file is the reader's own log, unedited: an entry per chapter and per reaction, a closing paragraph, then the **Follow-up** answers. To rebuild either text: check out `5817524`, copy `Story/Chapters/`, and for B run `git apply Story/Revision/Emergence/experiments/EXP-0024-*.patch`.

## How it was run

Each reader was a separate agent, given a folder containing only the 18 chapter files and told not to open anything else. Neither saw the other, the records, or the goals. The questions were sent only after each had finished the book and written its closing paragraph.

**Stage 1, the brief (verbatim, the same for both but for the folder path):**

> You're a reader, not an editor. A friend has handed you a novel manuscript and asked what it was like to read. Read only the files in [the book folder] (Chapter_01.txt to Chapter_18.txt), in order, start to finish. Don't open any other file or folder on this machine, and don't search the web.
>
> As you read, keep a running reading log in [log.md]. Write an entry at the end of every chapter, and also any time something makes you feel something (laugh, worry, get bored, get confused, get attached, get annoyed, get moved). Each entry: chapter and roughly where (quote a few words), what you felt, and why. Be honest; "nothing much here" is a valid entry. Don't summarise the plot; record your reactions as a reader. Don't skim: read every chapter fully.
>
> When you've finished the book, write a short paragraph at the end of the log: your overall reaction, and which moments stayed with you. Then stop and return the final paragraph as your message. You may be asked a few follow-up questions afterwards.

**Stage 2, the follow-up (verbatim, the same for both):**

> Thanks. A few follow-up questions about your experience as a reader. Answer from memory of how it felt while reading; you may reread your own log, but don't reread the chapters before answering. Be honest, short answers are fine, "I didn't feel much" is a valid answer. Append your answers to the end of [log.md] under a heading "Follow-up", and return them as your message.
>
> 1. Which three characters did you like most, ranked, and why?
> 2. Did you come to care about Shade? If so, when did it start? Name the moment.
> 3. When Shade was taken, what did you feel, in the moment? Did it feel unfair? Did it feel like something was lost beyond the person, and if so, what?
> 4. Did the book give his loss enough room, or move on too quickly? Where?
> 5. Before he was gone, was there anything you wanted from Shade, or for him, that you didn't get?
> 6. At the diner, when Shade says "Then you were never the point", what did that mean for Elizabeth, and what did you feel she lost, if anything?
> 7. In your own words, why did Elizabeth leave the diner and go back toward Pathwell? Did it make sense to you?
> 8. On a scale of 1–10, how much did Shade's death hurt? And the diner, how much did it land?

## Results at a glance

| | Reader A (control) | Reader B (candidates) |
| --- | --- | --- |
| Favourite character | Shade | Shade |
| Shade's death | 8/10 | 8/10 |
| The diner | 7/10 | 7/10 |
| Most moving moment | "LIKED POCKETS" ("the line I'll remember longest") | "LET OUT SLEEVES… REPAIR REQUESTED." ("the most moving moment in the book for me") |
| Wanted and didn't get | "some sign he'd keep living at Camp"; "one more word" | "To get his sleeves let out"; "A goodbye of any kind" |
| Too quick | the Ch18 confession | the death in Ch15; the Ch18 confession |
