# Merge instructions

Input: all_records.csv (one row per finding from nine reader reports; columns id, lens, run, model, chapters, subject, type, polarity, quote, severity, prompted, rank, source). Rows are sorted by type, polarity, then first chapter.

Your job: group records that are THE SAME FINDING into clusters, by this rule only:
- Two records match when they have the same type, the same polarity, the same subject (the same character, object, event or line, judged by you), and chapter spans that overlap or touch (within one chapter).
- Never put records of different types or different polarities in one cluster.
- Don't lump: two different complaints about the same chapter are two clusters. A cluster is one finding that several readers made.
- A record that matches nothing is a cluster of one.

Write a CSV (all fields double-quoted, header first) with exactly one row per input record:
id,cluster,cluster_title
- cluster: an id you make up, like "C001", shared by all records in that cluster.
- cluster_title: a one-line statement of the finding (same text on every row of the cluster), e.g. "Why Pathwell was in Elizabeth's flat is never explained (Ch1-3)".

Every input id must appear exactly once. At the end of your reply give: number of input rows, number of output rows, number of clusters, and a short list of any judgement calls you were unsure about (subject matches you weren't sure of). Don't read any other file. Don't judge whether findings are right.
