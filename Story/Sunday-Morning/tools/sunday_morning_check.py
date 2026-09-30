#!/usr/bin/env python3
"""Freshness checker for a Sunday Morning story collection.

Reads a collection's Registry (a copy of Story/Sunday-Morning/Registry.md)
and its prose drafts, then reports:

  1. name clashes: protagonists sharing initials; names in different stories
     sharing their first three letters; repeated surname endings; crowded
     first letters;
  2. repeated phrases: five-word phrases that appear in two or more stories;
  3. the Registry's stock phrases that still appear in the drafts;
  4. filter verbs (Pathwell forbidden pattern #3), per 1,000 words;
  5. uncontracted forms in narration (Craft, 'Write how people talk'), per 1,000 words;
  6. the Registry's own watch patterns (optional), per 1,000 words;
  7. very short paragraphs (four words or fewer) as a share of all paragraphs.

Everything collection-specific lives in the Registry, between marker comments:
  registry:names    the Names table (Story | Name | Role | Kind)
  registry:stock    stock phrases to avoid, one "- phrase" per line
  registry:allow    deliberate exceptions (Story file | Phrase | Reason)
  registry:linked   phrases shared across stories on purpose, one "- phrase" per line
  registry:watch    optional: "- label :: regex" or "- label :: regex :: all", one per
                    line. Counted in narration only, unless the line ends ":: all".

It reports; it never edits. Canon names are shown but never flagged as must-fix.
Filter verbs are counted after he/she/they and after the first names of every
protagonist and cast member in the Names table.

By default the drafts are the .md files in the drafts folder (README.md is skipped),
and everything before the first line that is exactly "---" is treated as the
draft's status block and skipped, so don't use a bare "---" as a scene break
above the prose you want read. For a novel or any other set of plain files, pass
--pattern (for example "Chapter_*.txt"); files that aren't .md have no status block
unless --status-block on is given. In a single long work, five-word phrases shared
by two chapters are often deliberate callbacks, so --min-files raises the bar.

Run from the repository root, for example:
  python3 Story/Sunday-Morning/tools/sunday_morning_check.py \\
      --registry Story/My-Collection/Registry.md --drafts Story/My-Collection/Drafts
  python3 Story/Sunday-Morning/tools/sunday_morning_check.py \\
      --registry Story/Revision/Registry.md --drafts Story/Chapters \\
      --pattern "Chapter_*.txt" --min-files 3
"""
import argparse, collections, glob, os, re, sys

STOP = set("""a an the and or but of to in on at by for with from as is was were be been
it its he she they them his her their i you we me my our your this that there then
had have has not no so if into out up down over all what who which when while would
could should did do does said says""".split())


def block(text, name):
    m = re.search(rf"<!-- registry:{name}:start -->(.*?)<!-- registry:{name}:end -->", text, re.S)
    return m.group(1) if m else None


def table_rows(chunk, width):
    rows = []
    for line in (chunk or "").splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != width or set(cells[0]) <= set("-: "):
            continue
        rows.append(cells)
    return rows[1:] if rows else rows  # drop the header row


def bullets(chunk):
    out = []
    for line in (chunk or "").splitlines():
        m = re.match(r"\s*[-*]\s+(.*\S)", line)
        if m:
            out.append(m.group(1).strip().strip('"“”').strip())
    return out


def load_registry(path):
    text = open(path, encoding="utf-8").read()
    names = block(text, "names")
    if names is None:
        sys.exit(f"Names table markers (registry:names) not found in {path}")
    rows = [dict(story=c[0], name=c[1], role=c[2], kind=c[3]) for c in table_rows(names, 4) if c[1]]
    stock = [re.escape(p).replace(r"\ ", r"\s+") for p in bullets(block(text, "stock"))]
    allow = {(c[0], c[1].lower()) for c in table_rows(block(text, "allow"), 3) if c[0] and c[1]}
    linked = [p.lower() for p in bullets(block(text, "linked"))]
    watch = []
    for line in (block(text, "watch") or "").splitlines():
        m = re.match(r"\s*[-*]\s+(.+?)\s*::\s*(.+?)(?:\s*::\s*(all|narration))?\s*$", line)
        if m:
            try:
                watch.append((m.group(1).strip("` "), re.compile(m.group(2).strip("` "), re.M), m.group(3) == "all"))
            except re.error as e:
                sys.exit(f"Bad watch pattern '{m.group(1)}' in {path}: {e}")
    return rows, stock, allow, linked, watch


def parts(name):
    return [p for p in re.findall(r"[A-Z][a-z]+", name) if p not in ("Mrs", "Mother", "Old")]


def check_names(rows):
    out = []
    prot = [r for r in rows if r["kind"] == "protagonist"]
    inits = collections.defaultdict(list)
    for r in prot:
        ps = parts(r["name"])
        if len(ps) >= 2:
            inits[ps[0][0] + ps[-1][0]].append(r)
    for k, rs in inits.items():
        if len(rs) > 1:
            out.append(("MUST-FIX", f"protagonists share initials {k}: " + ", ".join(f"{r['name']} ({r['story']})" for r in rs)))
    # shared 3-letter prefixes across different stories (ignoring same-surname families)
    seen = collections.defaultdict(list)
    for r in rows:
        for p in parts(r["name"]):
            if len(p) >= 3:
                seen[p[:3].lower()].append((p, r))
    for pre, items in sorted(seen.items()):
        words = {p for p, _ in items}
        stories = {r["story"] for _, r in items}
        if len(words) < 2 and len(stories) < 2:
            continue
        if len(words) == 1:  # the same name reused (a cross-story character or a family surname)
            if len(stories) > 1 and not any(r["kind"] == "canon" for _, r in items):
                who = sorted({f"{r['name']} ({r['story']})" for _, r in items})
                out.append(("CHECK", f"same name part '{items[0][0]}' in several stories: " + ", ".join(who)))
            continue
        canon = any(r["kind"] == "canon" for _, r in items)
        level = "WATCH" if canon else ("MUST-FIX" if any(r["kind"] == "protagonist" for _, r in items) else "CHECK")
        who = sorted({f"{p} ({r['story']})" for p, r in items})
        out.append((level, f"shared prefix '{pre}': " + ", ".join(who)))
    # surname endings
    ends = collections.defaultdict(list)
    for r in rows:
        ps = parts(r["name"])
        if len(ps) >= 2:
            for suf in ("water", "wright", "brook", "mere", "hollow", "field", "well", "wick", "more"):
                if ps[-1].lower().endswith(suf):
                    ends[suf].append(r)
    for suf, rs in ends.items():
        fams = {parts(r["name"])[-1] for r in rs}
        if len(fams) > 1:
            out.append(("CHECK", f"repeated surname ending '-{suf}': " + ", ".join(sorted(fams))))
    # crowded letters (first names only, non-canon)
    first = collections.Counter(parts(r["name"])[0][0] for r in rows if r["kind"] != "canon" and parts(r["name"]))
    crowded = [f"{k}×{v}" for k, v in first.most_common() if v >= 5]
    if crowded:
        out.append(("WATCH", "crowded first letters (pick new names elsewhere): " + ", ".join(crowded)))
    return out


def draft_texts(folder, pattern="*.md", status_block="auto"):
    texts = {}
    for f in sorted(glob.glob(os.path.join(folder, pattern))):
        if os.path.basename(f) == "README.md" or not os.path.isfile(f):
            continue
        t = open(f, encoding="utf-8").read().lstrip("﻿")
        if status_block == "on" or (status_block == "auto" and f.endswith(".md")):
            t = re.split(r"\n---\n", t, maxsplit=1)[-1]  # prose only, after any status block
        texts[os.path.splitext(os.path.basename(f))[0]] = t
    return texts


def check_phrases(texts, linked, n=5, min_files=2):
    where = collections.defaultdict(set)
    for story, t in texts.items():
        words = re.findall(r"[a-z']+", t.lower())
        for i in range(len(words) - n + 1):
            g = tuple(words[i:i + n])
            if sum(w not in STOP for w in g) >= 2:
                where[g].add(story)
    shared = [(" ".join(g), sorted(s)) for g, s in where.items()
              if len(s) >= min_files and not any(k in " ".join(g) for k in linked)]
    shared.sort(key=lambda x: (-len(x[1]), x[0]))
    return shared


def check_stock(texts, stock, allow):
    hits = []
    for story, t in texts.items():
        for pat in stock:
            plain = re.sub(r"\\s\+", " ", pat).replace("\\", "")
            if (story, plain.lower()) in allow:
                continue
            c = len(re.findall(r"\b" + pat + r"\b", t, re.I))
            if c > (1 if "way you might" in plain else 0):
                hits.append((story, plain, c))
    return hits


FILTER_VERBS = r"\s+(?:saw|felt|heard|noticed|watched)\b"
SPOKEN = (r"\b(?:did|was|were|could|would|had|has|have|is|are|does|do|should) not\b"
          r"|\bcannot\b|\b(?:did not|could not) manage\b")


def filter_pattern(rows):
    """he/she/they plus the first names of the registry's protagonists and cast."""
    names = sorted({parts(r["name"])[0] for r in rows
                    if r["kind"] in ("protagonist", "cast") and parts(r["name"])})
    subjects = ["he", "she", "they"] + [re.escape(n) for n in names]
    return r"\b(?:" + "|".join(subjects) + ")" + FILTER_VERBS


def narration_only(t):
    """Drop dialogue. Works paragraph by paragraph, so a speech that runs past the
    end of a paragraph without a closing quote doesn't swallow the narration after it."""
    out = []
    for para in t.split("\n"):
        para = re.sub(r"[\"\u201c][^\"\u201d\n]*[\"\u201d]", " ", para)
        para = re.sub(r"[\"\u201c][^\"\u201d\n]*$", " ", para)  # an unclosed opening quote
        out.append(para)
    return "\n".join(out)


def rate(texts, pattern, narration_words, narration_hits=True, flags=re.I):
    out = []
    for story, t in texts.items():
        narration = narration_only(t)
        words = len(re.findall(r"\w+", narration if narration_words else t))
        hits = re.findall(pattern, narration if narration_hits else t, flags)
        out.append((story, len(hits), round(1000 * len(hits) / max(words, 1), 1)))
    return out


def short_paragraphs(texts, limit=4):
    out = []
    for story, t in texts.items():
        paras = [p for p in re.split(r"\n\s*\n", t) if p.strip()]
        short = sum(1 for p in paras if len(re.findall(r"[\w']+", p)) <= limit)
        out.append((story, short, len(paras), round(100 * short / max(len(paras), 1))))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--registry", required=True, help="the collection's copy of Registry.md")
    ap.add_argument("--drafts", required=True, help="the collection's drafts folder")
    ap.add_argument("--pattern", default="*.md",
                    help='which files in the drafts folder to read (default "*.md"; e.g. "Chapter_*.txt")')
    ap.add_argument("--status-block", choices=("auto", "on", "off"), default="auto",
                    help="skip everything above the first bare '---' line: auto = only in .md files")
    ap.add_argument("--min-files", type=int, default=2,
                    help="report a five-word phrase only when it appears in at least this many files (default 2)")
    a = ap.parse_args()
    rows, stock, allow, linked, watch = load_registry(a.registry)
    texts = draft_texts(a.drafts, a.pattern, a.status_block)
    if not texts:
        sys.exit(f"No drafts matched {a.pattern!r} in {a.drafts}")
    print(f"Registry: {len(rows)} names, {len(stock)} stock phrases, {len(watch)} watch patterns. "
          f"Drafts: {len(texts)} files matching {a.pattern!r}.\n")
    print("== Names ==")
    res = check_names(rows)
    for level in ("MUST-FIX", "CHECK", "WATCH"):
        for lv, msg in res:
            if lv == level:
                print(f"[{lv}] {msg}")
    if not res:
        print("no clashes")
    print(f"\n== Five-word phrases shared across {a.min_files} or more files ==")
    shared = check_phrases(texts, linked, min_files=a.min_files)
    for phrase, stories in shared[:60]:
        print(f"  \"{phrase}\" — {', '.join(stories)}")
    if not shared:
        print("none")
    print("\n== Registered stock phrases still present ==")
    hits = check_stock(texts, stock, allow)
    for story, pat, c in hits:
        print(f"  {story}: {pat} ×{c}")
    if not hits:
        print("none")
    print("\n== Filter verbs in narration (he saw / she felt / they heard / noticed / watched) ==")
    print("   Pathwell forbidden pattern #3; subjects are he/she/they and the Registry's protagonists and cast.")
    print("   Not all are wrong; review any file above ~2 per 1,000 words.")
    for story, n, r in sorted(rate(texts, filter_pattern(rows), False), key=lambda x: -x[2]):
        print(f"  {story}: {n} ({r} per 1,000 words)")
    print("\n== Uncontracted forms in narration (did not / was not / cannot) ==")
    print("   Craft, 'Write how people talk'. Fine for emphasis; review any file above ~1 per 1,000 words.")
    for story, n, r in sorted(rate(texts, SPOKEN, True), key=lambda x: -x[2]):
        print(f"  {story}: {n} ({r} per 1,000 words)")
    for label, pat, everywhere in watch:
        print(f"\n== Watch: {label} ({'narration and dialogue' if everywhere else 'narration only'}) ==")
        results = rate(texts, pat, not everywhere, narration_hits=not everywhere, flags=0)
        total = sum(n for _, n, _ in results)
        print(f"   {total} in all files")
        for story, n, r in sorted(results, key=lambda x: -x[2]):
            if n:
                print(f"  {story}: {n} ({r} per 1,000 words)")
    print("\n== Very short paragraphs (four words or fewer) ==")
    print("   Voice guide: fragments are for danger and comic timing, not the default rhythm.")
    for story, short, total, pct in sorted(short_paragraphs(texts), key=lambda x: -x[3]):
        print(f"  {story}: {short} of {total} paragraphs ({pct}%)")
    must = sum(1 for lv, _ in res if lv == "MUST-FIX")
    return 1 if must else 0


if __name__ == "__main__":
    sys.exit(main())
