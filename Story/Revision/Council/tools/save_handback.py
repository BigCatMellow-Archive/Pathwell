#!/usr/bin/env python3
"""Save a reader's report from its agent transcript.

Background reader agents are often blocked from writing their own report file
("Subagents should return findings as text"), so the report arrives only as the
agent's final hand-back. This pulls the longest assistant text (or hand-back tool
input) out of the agent's JSONL transcript and writes it to a file, without the
coordinating session having to retype it.

    python3 Story/Revision/Council/tools/save_handback.py <agent transcript .output> <report.md>
"""
import json, sys
src, out = sys.argv[1], sys.argv[2]
best = ""
for line in open(src):
    try: o = json.loads(line)
    except Exception: continue
    msg = o.get("message") or {}
    if msg.get("role") != "assistant": continue
    for c in msg.get("content") or []:
        if not isinstance(c, dict): continue
        t = ""
        if c.get("type") == "text": t = c.get("text", "")
        elif c.get("type") == "tool_use":
            inp = c.get("input") or {}
            t = max((v for v in inp.values() if isinstance(v, str)), key=len, default="")
        if len(t) > len(best): best = t
open(out, "w").write(best)
print(len(best), best[:120].replace("\n", " | "))
