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
  5. uncontracted forms in narration (Craft, 'Write how people talk'), per 1,000 words.

Everything collection-specific lives in the Registry, between marker comments:
  registry:names    the Names table (Story | Name | Role | Kind)
  registry:stock    stock phrases to avoid, one "- phrase" per line
  registry:allow    deliberate exceptions (Story file | Phrase | Reason)
  registry:linked   phrases shared across stories on purpose, one "- phrase" per line

It reports; it never edits. Canon names are shown but never flagged as must-fix.
Drafts are the .md files in the drafts folder (README.md is skipped). Everything
before the first line that is exactly "---" is treated as the draft's status block
and skipped, so don't use a bare "---" as a scene break above the prose you want read.

Run from the repository root, for example:
  python3 Story/Sunday-Morning/tools/sunday_morning_check.py \\
      --registry Story/My-Collection/Registry.md --drafts Story/My-Collection/Drafts
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
    return rows, stock, allow, linked


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


def draft_texts(folder):
    texts = {}
    for f in sorted(glob.glob(os.path.join(folder, "*.md"))):
        if os.path.basename(f) == "README.md":
            continue
        t = open(f, encoding="utf-8").read()
        t = re.split(r"\n---\n", t, maxsplit=1)[-1]  # prose only, after any status block
        texts[os.path.basename(f)[:-3]] = t
    return texts


def check_phrases(texts, linked, n=5):
    where = collections.defaultdict(set)
    for story, t in texts.items():
        words = re.findall(r"[a-z']+", t.lower())
        for i in range(len(words) - n + 1):
            g = tuple(words[i:i + n])
            if sum(w not in STOP for w in g) >= 2:
                where[g].add(story)
    shared = [(" ".join(g), sorted(s)) for g, s in where.items()
              if len(s) >= 2 and not any(k in " ".join(g) for k in linked)]
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


FILTERS = r"\b(?:he|she|they)\s+(?:saw|felt|heard|noticed|watched)\b"
SPOKEN = (r"\b(?:did|was|were|could|would|had|has|have|is|are|does|do|should) not\b"
          r"|\bcannot\b|\b(?:did not|could not) manage\b")


def narration_only(t):
    return re.sub(r"[\"\u201c][^\"\u201d]*[\"\u201d]", " ", t)  # ignore dialogue


def rate(texts, pattern, narration_words):
    out = []
    for story, t in texts.items():
        narration = narration_only(t)
        words = len(re.findall(r"\w+", narration if narration_words else t))
        hits = re.findall(pattern, narration, re.I)
        out.append((story, len(hits), round(1000 * len(hits) / max(words, 1), 1)))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--registry", required=True, help="the collection's copy of Registry.md")
    ap.add_argument("--drafts", required=True, help="the collection's drafts folder")
    a = ap.parse_args()
    rows, stock, allow, linked = load_registry(a.registry)
    texts = draft_texts(a.drafts)
    print(f"Registry: {len(rows)} names, {len(stock)} stock phrases. Drafts: {len(texts)} stories.\n")
    print("== Names ==")
    res = check_names(rows)
    for level in ("MUST-FIX", "CHECK", "WATCH"):
        for lv, msg in res:
            if lv == level:
                print(f"[{lv}] {msg}")
    if not res:
        print("no clashes")
    print("\n== Five-word phrases shared across stories ==")
    shared = check_phrases(texts, linked)
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
    print("   Pathwell forbidden pattern #3. Not all are wrong; review any story above ~2 per 1,000 words.")
    for story, n, r in sorted(rate(texts, FILTERS, False), key=lambda x: -x[2]):
        print(f"  {story}: {n} ({r} per 1,000 words)")
    print("\n== Uncontracted forms in narration (did not / was not / cannot) ==")
    print("   Craft, 'Write how people talk'. Fine for emphasis; review any story above ~1 per 1,000 words.")
    for story, n, r in sorted(rate(texts, SPOKEN, True), key=lambda x: -x[2]):
        print(f"  {story}: {n} ({r} per 1,000 words)")
    must = sum(1 for lv, _ in res if lv == "MUST-FIX")
    return 1 if must else 0


if __name__ == "__main__":
    sys.exit(main())
