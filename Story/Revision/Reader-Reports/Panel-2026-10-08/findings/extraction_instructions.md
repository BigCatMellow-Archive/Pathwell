# Extraction instructions (one agent per reader report)

You turn ONE reader's report into finding records. Read only the files named in your prompt (that reader's brief and its out folder). Do not open the book, other readers' files, or anything else. Do not judge whether findings are right; record what the reader said.

Write a CSV (comma-separated, double-quote every field, header row first) to the output path in your prompt, with these columns:

reader,run,model,chapters,subject,type,polarity,quote,severity,prompted,rank,source

- reader: the lens name given in your prompt; run: given; model: given.
- chapters: the chapter or span the finding is about, e.g. "Ch5" or "Ch5-7" or "Ch1;Ch18".
- subject: the character, object, event or line the finding is about, in a few words (e.g. "Pathwell's reason for being in her flat", "the cookbook page count", "Ch16 hearing", "Shade's death").
- type: exactly one of: confusion, continuity, knowledge, logic, rule, motivation, voice/repetition, pacing, tone, promise, structure, strength.
  (knowledge = who knows what and how; logic = cause and effect; promise = a setup or payoff; strength = something that works.)
- polarity: + (works) or - (doesn't work).
- quote: a verbatim line FROM THE BOOK as the reader quoted it, 25 words or fewer; empty if the reader quoted none.
- severity: for problems, stopper (the reader stopped or quit or stopped believing), snag (a real problem that cost them), quibble (minor); for strengths, strong or mild.
- prompted: "unprompted" if the finding appears in the reader's running log, or answers a question that did not name its specific subject; "prompted" only if a question in the brief or the later questions named that specific subject (e.g. a brief that names a character prompts findings about that character).
- rank: the finding's position in the reader's top-ten list (topten.md) if it is there, else empty.
- source: file name and a short locator (section or line), e.g. "lens_output.md (b)3" or "log.md Ch7".

Rules:
- One record per distinct finding. Do not lump different complaints into one record; a record that would need two types is two records.
- The same finding repeated in the log, the report, the core answers and the top ten is ONE record (cite the earliest source; fill rank if it's in the top ten).
- Include strengths as well as problems.
- Record findings at all severities.
- At the end of your reply, give the number of records you wrote. Reply briefly.
