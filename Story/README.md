# Pathwell

## Canonical manuscript

The current manuscript source of truth is the numbered chapter sequence:

```text
Chapters/Chapter_01.txt
...
Chapters/Chapter_18.txt
```

Read those files in numeric order. Do not treat older working snapshots or planning files as manuscript canon.

`Chapter_12b.txt` was a superseded climax draft and has been removed from the live chapter directory; it remains available through Git history.

`Pathwell Working.docx` is a legacy working snapshot. It is retained for historical/reference purposes and is **not** the canonical manuscript.

The old hand-maintained `Pathwell.txt` was also removed because it contained the pre-reconciliation manuscript. To generate a fresh assembled plain-text manuscript from the canonical chapters, run:

```bash
python3 Story/assemble_manuscript.py
```

That writes `Story/Pathwell.txt` from Chapters 1–18. The chapter files remain authoritative if the generated file ever differs.

## Revision

The current revision of the manuscript, using the Sunday Morning method (not its tone), is recorded in:

```text
Revision/
```

Start at `Revision/README.md`: its order of authority, the plan, the open questions for James, the promise ledger and the pass log.

## Story support material

Planning, canon, audit, reconciliation, and execution-support documents live in:

```text
Story_Files/
```

These files explain the manuscript but are not themselves chapters.

## Sunday Morning notes

A general guideline for writing Sunday Morning stories (low-pressure, character-forward stories) in any setting: the framework, James's voice guide, rules, craft, a step-by-step pipeline, collection templates and a freshness checker. It isn't part of the Pathwell manuscript.

```text
Sunday-Morning/
```

Start at `Sunday-Morning/README.md`.

## MAP coordination system

The project-local MAP coordination system lives in:

```text
MAP_System/
```

Start here:

- `MAP_System/AGENTS.md` - shared Codex/Claude rules
- `MAP_System/CLAUDE.md` - Claude Code instructions
- `MAP_System/tasks/TASK-001.json` - first ready task
- `MAP_System/shared/project_brief.md` - project objective
- `MAP_System/archive/root-map-pathwell-run-2026-06-27/` - archived Pathwell task run separated from the reusable root MAP engine

Validate the Pathwell task graph:

```bash
python3 MAP_System/scripts/validate_task_graph.py
```
