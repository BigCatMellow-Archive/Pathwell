# Collection Registry (template)

## Status

**Writing reference: a general guideline for Sunday Morning stories in any setting.** This page is a **template**. Copy it into each collection's folder (for example `Story/My-Collection/Registry.md`) and fill it in there. The copy owns what that collection has already used (names, story shapes, devices and stock phrases) so new stories and new passes stay fresh instead of quietly repeating the last ones.

The idea came from the first collection, after James noticed two protagonists with the same initials ([D8](Decisions.md#standing-rulings): keep every story unique and fresh). The lessons behind each rule below are in [History](History.md#what-went-wrong-and-where-the-lesson-lives-now).

The checker reads this page's marked sections and the collection's drafts, and reports clashes, repeated phrases, stock phrases, filter verbs and uncontracted narration. Run it from the repository root:

```text
python3 Story/Sunday-Morning/tools/sunday_morning_check.py --registry <Collection>/Registry.md --drafts <Collection>/Drafts
```

**Update the collection's copy whenever a story adds or renames a character, or changes its shape.** The script only knows what is written there. When to run it is part of the [Pipeline](Pipeline.md#after-every-pass). Keep the `<!-- registry:… -->` marker comments: they tell the checker where each list starts and ends. The checker skips everything in a draft above its first line that is exactly `---` (the draft's status block), so don't use a bare `---` as a scene break.

## Names

Every named character in the drafts, registered at L0, before drafting ([Pipeline: Stage 0](Pipeline.md#stage-0--add-a-story)). Kinds are `protagonist`, `cast`, `minor` and `canon`. Mark the setting's own established figures `canon`: the script reports them but never asks for them to change. Leave unnamed roles (the tea seller, the land agent, the market master) out on purpose. Leaving a role unnamed is itself a device, so track it under [Devices](#devices-already-used) if it recurs.

<!-- registry:names:start -->
| Story | Name | Role | Kind |
| --- | --- | --- | --- |
| *Story title* | *First Last* | *what they do* | protagonist |
<!-- registry:names:end -->

Delete the example row when you add the first real one.

### Name rules

- **No two protagonists share initials,** or a first name's first three letters.
- **No two names anywhere in the collection share a first name's or surname's first three letters,** unless one is canon or the characters are family in the same story.
- **Don't repeat surname endings** such as -water, -wright or -brook.
- **Watch crowded letters.** List them here as they fill up, and pick new names from open letters. In the first collection, T, H and A filled up fast; U, X, Y, Z, K, Q and V stayed open. *Crowded here:* (fill in)
- **Name new places with the setting's own naming logic** and mark them provisional ([Rules: canon discipline](Rules.md#canon-discipline)).
- **Keep a rename log.** Record each rename and why, so a later pass doesn't reintroduce a clash. In the first collection, seven renames were needed: shared initials, too-close first names, a third "-water" surname, a cluster of four names starting with the same letters, three "Hol-" names across three stories (the checker caught this on its first run, after the manual audit missed it), and a farm name that falsely echoed a character who took an outsider's money two stories later. One fix introduced a fresh clash; the checker caught that too.
  - *Rename log:* (fill in: old name → new name, reason)
- **Expected checker notes.** List clashes that are deliberate (a character who appears in two stories on purpose; a canon name that shares a prefix), so nobody "fixes" them.
  - *Expected:* (fill in)

## Story shapes

The collection's variety lives here. A new story should differ from its neighbors in reading order on at least three of these columns. Fill it in at L2 and update it whenever a pass changes an opening, engine, resolution or ending ([Pipeline: collection shape check](Pipeline.md#collection-shape-check-for-a-set-of-stories)).

| # | Story | Protagonist type | Engine | Resolved by | Register | Opening | Final line |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | | | | | | | |

**Resolution types to spread across the collection:** a document read closely, an object, a witnessed act, people (a message carried, a walk somewhere together), memory. In the first collection, six of seven plans resolved by reading a document closely, because the running element (a language habit) pulled every story toward textual precision and nobody compared shapes. It took a drafting pass to undo. Avoid "an old document" unless the story does something new with it.

**Resolutions already used:** (fill in, with story numbers)

## Devices already used

Reuse one of these only on purpose, and never in the next story in reading order.

| Device | Where |
| --- | --- |
| | |

Devices that repeated in the first collection, as a starting list to watch for:

- the same kind of running element in every story (for example, a language habit each time);
- an old record or archive discovery;
- a clerk or records person as protagonist;
- a child who sees what adults won't;
- an elder who answers sideways;
- food as the soft landing;
- someone asks the hero for the next small job (two stories ended this way until an independent reader recognized one ending as the other's);
- a bookend of the opening line;
- a public reading or telling to a crowd;
- two names or two words kept side by side;
- an unnamed polite antagonist;
- a stamp or mark as the payoff.

## Stock phrases to avoid

These became tics during AI drafting of the first collection, and they're a good starting list for any collection. Add the collection's own as they appear. The checker reports any listed phrase still in the drafts, and any five-word phrase that appears in two or more stories.

<!-- registry:stock:start -->
- wrote it down
- nobody said so
- delighted to be asked
- for thirty years
- for the first time in his life
- for the first time in her life
- the way you might
<!-- registry:stock:end -->

Also watch for, by reading (the checker can't catch them reliably):

- "didn't say anything" / "without a word" as a scene ending;
- "wrote it down" or a silence as the default scene ending (after one tic is removed, check that another hasn't taken its place);
- "the way you might…" similes, more than one per story (the checker allows one).

## Checker exceptions

Deliberate exceptions. Keep them short, and give each a reason.

**Allowed stock phrases:** a listed phrase that is right in one story (a character's trait, approved text, a deliberate callback). The Story column is the draft's file name without `.md`; the Phrase column matches a line in the stock list above.

<!-- registry:allow:start -->
| Story file | Phrase | Reason |
| --- | --- | --- |
<!-- registry:allow:end -->

**Linked phrases:** words shared across stories on purpose, such as the details of a [cross-story promise](Collection.md#cross-story-promise-ledger) or one character described in two stories. The checker ignores five-word phrases that contain any of these.

<!-- registry:linked:start -->
<!-- registry:linked:end -->
