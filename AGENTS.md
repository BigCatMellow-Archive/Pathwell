# Instructions for agents working on Pathwell

Pathwell is the author's novel. Your job is to help him become more himself, not to supply a substitute voice. This repository runs on a written method, the **Sunday Morning notes**, and a record of the author's rulings. Follow both. A pass that skipped them once nearly undid a dozen of his rulings in one go.

## Read first, every session

1. **[Before you touch a chapter](Story/Revision/Before-You-Touch-A-Chapter.md).** One page: the rulings most likely to be undone, who writes what, and how a change gets in.
2. **[The Sunday Morning notes](Story/Sunday-Morning/README.md).** The method: how stories here are planned, drafted, revised and checked. Pathwell takes the method, and some of the tone ([R1](Story/Revision/Decisions.md#the-authors-rulings-for-this-revision), [R24](Story/Revision/Decisions.md#the-authors-rulings-for-this-revision)).
3. **[The revision README](Story/Revision/README.md).** Pathwell's own order of authority, chapter levels and routine, which adapt the notes to this book.

## Which part of the Sunday notes to open, and when

| When you're… | Open |
| --- | --- |
| drafting or revising prose | [Craft](Story/Sunday-Morning/Craft.md), then the [Voice Guide](Story/Sunday-Morning/Sources/Voice-Guide.md) and [Pathwell's prose voice](Story/Story_Files/pathwell_prose_voice.md) |
| writing a new joke, emotional line or character-defining line | [Craft: who writes what](Story/Sunday-Morning/Craft.md#ai-and-the-author-who-writes-what): keep it plain, flag it, offer an alternative |
| changing exact words, a sentence or a paragraph | [Line-editing protocol](Story/Sunday-Morning/Line-Editing-Protocol.md) (§7 for small edits) |
| finishing any pass | [Pipeline: after every pass](Story/Sunday-Morning/Pipeline.md#after-every-pass), reported step by step (D23) |
| getting an independent read | [Reader protocol](Story/Sunday-Morning/Reader-Protocol.md); for several readers, the [reader panel](Story/Sunday-Morning/Reader-Panel.md) |
| wondering whether the author already decided something | [Revision Decisions](Story/Revision/Decisions.md), then the method's [Decisions](Story/Sunday-Morning/Decisions.md) |
| checking a draft for sameness or AI tells | [Craft: writing against sameness](Story/Sunday-Morning/Craft.md#writing-against-sameness); [AI tells](Story/Sunday-Morning/Sources/AI-Tells.md) (awareness, not rules) |

## Working rules

- **The canon is `Story/Chapters/Chapter_01–18.txt`** ([R3](Story/Revision/Decisions.md#the-authors-rulings-for-this-revision)). Exports and assembled copies aren't.
- **Anything the author hasn't picked is a candidate,** not an edit: an `EXP-NNNN` page with one patch per candidate in `Story/Revision/Emergence/experiments/`.
- **Push back** when a request or note has a cost, with the reason and an alternative ([R26](Story/Revision/Decisions.md#the-authors-rulings-for-this-revision)). On your own questions, go with your lean and list it for him to overrule ([R36](Story/Revision/Decisions.md#the-authors-rulings-for-this-revision)).
- **Every pass** gets a [Pass Log](Story/Revision/Pass-Log.md) entry and an update to [Revision Status](Revision-Status.md). Record a new ruling as an R-row, in his words.
- **Run the checker** after prose changes, from the repository root:

  ```text
  python3 Story/Sunday-Morning/tools/sunday_morning_check.py --registry Story/Revision/Registry.md --drafts Story/Chapters --pattern "Chapter_*.txt" --min-files 3
  ```

- **Refer to him as "the author"** in files, filenames and commit messages. Never by name.
- **Commit after each step** ([R8](Story/Revision/Decisions.md#the-authors-rulings-for-this-revision)).
