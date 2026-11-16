# Experiment tools

## Status

**Active.** Added 2026-11-16 ([P119](../../Pass-Log.md#p119-2026-11-16-a-brief-for-a-high-effort-session)). These are the session-scratch scripts from the Garden and Wild work, moved here so a fresh session doesn't have to rebuild them.

## The tools

| Tool | What it does |
| --- | --- |
| `build_book.py --src DIR --subtitle "…" --out PATH [--docx] [--epub]` | Builds a reading copy from any folder of `Chapter_NN.txt` files: a docx from `docx-template.docx` (the 10.23 reading-copy look), an epub through pandoc, or both. It applies smart quotes (with the em-dash quote bug fixed), turns 3+ newlines into scene breaks, and keeps line breaks inside documents (recipes, cards, lists). |
| `overlap.py --draft DIR --against DIR [--against DIR …] [--show N]` | Counts the six-word phrases a draft shares with source folders, per chapter and in total, and lists draft paragraphs with at least N shared phrases. It prints draft-side text only, so you can check for transplanting without reading the source. |
| `docx-template.docx` | The template `build_book.py` uses. It includes the fonts. |

The other checks already live in the repo:

- Freshness: `python3 Story/Sunday-Morning/tools/sunday_morning_check.py --registry Story/Sunday-Morning/Registry.md --drafts DIR --pattern "Chapter_*.txt"`
- Manuscript rebuild: `python3 Story/assemble_manuscript.py`
- Harada: `python3 Story/Revision/Harada/build_chart.py --check`. Compare against the error count recorded in the latest pass log entry; 22 were pre-existing at P104.
