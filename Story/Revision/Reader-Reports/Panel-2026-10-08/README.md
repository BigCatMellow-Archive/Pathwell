# Reader panel, 2026-10-08

**Status: complete (lean finish). Start with the [Findings Report](Findings-Report.md); the method view is in [synthesis.md](synthesis.md).** The first standard [reader panel](../../../Sunday-Morning/Reader-Panel.md) on the whole book. The text read is the chapters at commit 281524a (unchanged since 568dd16).

## Done

- **Setup.**
  - A cover line, written by an agent that read only Chapter 1 ([cover_line.md](cover_line.md)).
  - Shade's chapter list, for the character reader ([shade_chapters.md](shade_chapters.md)).
  - Eight briefs, each drafted by its own agent. A reviewer rejected six for shared reading histories and reasons; fresh agents redrafted them ([briefs/](briefs/); the rejected drafts are in [briefs/rejected-v1/](briefs/rejected-v1/)).
  - The [lever matrix](lever_matrix.md).
- **Readers: all nine runs finished** ([readers/](readers/)). Each has its running log, its lens output, its answers to the six shared questions (sent after the reading), and its ranked top ten.
  - The target reader, run twice (Sonnet).
  - The reluctant reader (Haiku).
  - The skimmer: a chain of 18 Haiku agents, one per chapter, each remembering the book only through a 150-word recap ([chain_log.md](readers/skimmer/chain_log.md)).
  - The continuity auditor (Sonnet).
  - The rules reader (Haiku).
  - The character reader: Shade's chapters only (Sonnet).
  - The prose reader: Chapters 1, 4, 9, 12, 15 and 18 (Sonnet).
  - The hostile reviewer (Haiku).
- **Extraction.** One agent per report turned each into finding records: 883 in all ([findings/](findings/), one CSV per reader, combined in [all_records.csv](findings/all_records.csv)).
- **Merge A.** One merge agent grouped the records into 649 clusters ([merge_A.csv](findings/merge_A.csv)).

- **Merge B.** A second, independent merge on a different model (Haiku): 632 clusters ([merge_B.csv](findings/merge_B.csv)). Both merges are complete, and neither mixes types or polarities. They agree on 77% of grouped record pairs (Dice).
- **Counts.** Made by [panel_counts.py](../../../Sunday-Morning/tools/panel_counts.py) and filed in [counts/](counts/):
  - the first-cut sort for each merge;
  - the merge comparison;
  - the noise check: the two target runs overlap 36% (A) or 31% (B), under the 40% working band;
  - the diversity check: top-ten overlap between different lenses averages 0.03–0.04, against 0.22 for the repeat pair, but prose/target-1 reaches 0.20–0.21;
  - coverage by type and family;
  - shared phrasing: one five-word phrase in three reports, traced to the briefs' shared ground rule.

- **Sort, informed check and goals comparison**, all in [synthesis.md](synthesis.md).
  - The author chose a lean finish to save cost, so the orchestrating session did these steps itself, without a fresh synthesis agent or an informed-pass agent.
  - The full D24 check was not run on the findings.

## Deviations from the protocol, recorded

- **Models.** Opus was unavailable (weekly limit until 2026-10-11), so only Sonnet and Haiku were used. Sonnet has 5 of the 9 runs, one more than the protocol's "no more than half". Merge A was Sonnet, and Merge B will be too, not a different model.
- **Retries.**
  - Several runs stopped on rate limits and were retried. See [run_notes.md](run_notes.md) for which out-folders held partial logs from failed attempts and how each was handled.
  - The target-2 retry appended below its earlier partial log and didn't read it.
  - The auditor retry read its own earlier rows for Chapters 1–9 and appended to them.
- **Report files.**
  - Some readers' harnesses refused to save files named as reports. Their reports were saved under `lens_output.md` instead.
  - For the rules reader, the orchestrator saved the report from the reader's reply: [lens_output.md](readers/rules/lens_output.md) and [core_and_topten.md](readers/rules/core_and_topten.md).
- **Brief edits.** After the redraft, the orchestrator swapped two titles that were still shared (auditor: the Dresden Files became Glen Cook's Garrett books; hostile: A Wizard of Earthsea became Tigana).
