#!/usr/bin/env python3
"""Check and build a Harada chart (see ../SKILL.md).

A chart is one JSON file (format: ../reference/chart-schema.json). This script:

  1. checks it. Errors (the build stops): a quote that isn't in the source it
     names, a box with more than eight boxes inside, a duplicate or missing id,
     an unknown status, a box with no title.
     Warnings (fix or decide): titles that are labels or too long, boxes with
     boxes inside but no note, proposed wording not marked for the owner.
  2. builds the chart page: one self-contained HTML file that can be opened
     in a browser or published, and that can save edits to itself; and the
     agent edition: the same chart as a Markdown outline, for another agent
     (or a person) to read in order.
  3. optionally pulls edits back from a saved copy of the published page.

Sources are the text files quotes are checked against. Each file's key is the
first number in its name (Chapter_07.txt -> 7) or, if it has none, its name
without the extension (canon.txt -> "canon"). A box's "ch" names that key.

  python3 harada_chart.py CHART.json --sources "Story/Chapters/Chapter_*.txt"
  python3 harada_chart.py CHART.json --sources "docs/*.md" --check
  python3 harada_chart.py CHART.json --sources "..." --from-page saved.html
  python3 harada_chart.py CHART.json --sources "..." --out page.html

Exit status is 1 when there are errors. Standard library only.
"""
import argparse
import glob
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
DEFAULT_TEMPLATE = HERE.parent / "assets" / "chart-template.html"

STATUSES = {"paid", "thin", "open", "author"}
MAX_KIDS = 8
LONG_TITLE = 70

# The head the page itself writes when it saves, so a built page and a page
# saved from the browser are byte-identical.
HEAD = ('<!doctype html><html><head><meta charset=utf8><meta name=viewport '
        'content="width=device-width,initial-scale=1,viewport-fit=cover"><style>'
        ':root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);'
        'padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;'
        'font:14px system-ui,-apple-system,"Segoe UI",sans-serif}'
        'img{max-width:100%}[hidden]{display:none!important}</style></head><body>')
TAIL = "</body></html>"

# Titles that only label a box. Each was a real box in an early chart and was
# replaced; reference/wording.md shows what replaced it.
LABEL_TITLES = {"the pile", "help!", "recalculates", "the line", "the cost", "the claim",
                "the question", "his answer", "her answer", "no answer", "seen first"}


def norm(s):
    return re.sub(r"\s+", " ", s)


def load_sources(pattern):
    out = {}
    for f in sorted(glob.glob(pattern, recursive=True)):
        p = pathlib.Path(f)
        m = re.search(r"\d+", p.stem)
        key = int(m.group()) if m else p.stem
        if key in out:
            sys.exit(f"Two sources share the key {key!r}: {out[key][0]} and {f}")
        out[key] = (f, norm(p.read_text(encoding="utf-8")))
    if not out:
        sys.exit(f"No source files match {pattern!r}")
    return out


def walk(node, depth=0):
    yield node, depth
    for kid in node.get("kids", []):
        yield from walk(kid, depth + 1)


def check(chart, sources):
    errors, warnings = [], []
    seen = set()
    counts = {s: 0 for s in STATUSES}
    boxes = deepest = 0
    if "root" not in chart:
        return ["chart has no root box"], [], {}
    for n, depth in walk(chart["root"]):
        boxes += 1
        deepest = max(deepest, depth)
        nid = n.get("id")
        title = (n.get("title") or "").strip()
        where = f"{nid or '?'} “{title}”"
        if not title:
            errors.append(f"{where}: no title")
        if not nid:
            errors.append(f"{where}: no id")
        elif nid in seen:
            errors.append(f"{where}: duplicate id")
        seen.add(nid)
        if len(n.get("kids", [])) > MAX_KIDS:
            errors.append(f"{where}: {len(n['kids'])} boxes inside; a sheet holds {MAX_KIDS}")
        s = n.get("status")
        if s and s not in STATUSES:
            errors.append(f"{where}: unknown status {s!r} (use {', '.join(sorted(STATUSES))})")
        elif s:
            counts[s] += 1
        q = n.get("quote")
        if q:
            key = n.get("ch")
            if sources is None:
                pass
            elif key is None:
                errors.append(f"{where}: has a quote but no source (ch)")
            elif key not in sources:
                errors.append(f"{where}: source {key!r} not found among the source files")
            elif norm(q) not in sources[key][1]:
                errors.append(f"{where}: quote not found in {sources[key][0]}: {q[:80]}")
        if len(title) > LONG_TITLE:
            warnings.append(f"{where}: title is {len(title)} characters; aim for under {LONG_TITLE}")
        if title.lower() in LABEL_TITLES:
            warnings.append(f"{where}: title is a label; say what the box does for the box above")
        if n.get("kids") and not n.get("note"):
            warnings.append(f"{where}: has boxes inside but no note saying how it gets to the box above")
        if n.get("proposed") and s != "author":
            warnings.append(f"{where}: proposed wording should have status 'author'")
    if sources is None:
        warnings.append("no --sources given, so quotes were not checked")
    return errors, warnings, {"boxes": boxes, "levels": deepest, **counts}


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def safe_json(obj):
    s = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    return s.replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")


def build(chart, template_path, out_path):
    template = pathlib.Path(template_path).read_text(encoding="utf-8")
    for token in ("__DATA__", "__TEMPLATE__", "__TITLE__"):
        if template.count(token) != 1:
            sys.exit(f"{template_path} must contain {token} exactly once")
    title = chart.get("title") or "Harada chart"
    content = re.sub(r"__(DATA|TEMPLATE|TITLE)__",
                     lambda m: {"DATA": safe_json(chart), "TEMPLATE": safe_json(template),
                                "TITLE": esc(title)}[m.group(1)],
                     template)
    pathlib.Path(out_path).write_text(HEAD + content + TAIL, encoding="utf-8")


STATUS_NAMES = {"paid": "on the page", "thin": "thin", "open": "open on purpose", "author": "needs the author"}


def to_markdown(chart, chart_name):
    """The chart as a Markdown outline: the version to hand another agent."""
    labels = {"center": "The goal", "sourceName": "Chapter", **chart.get("labels", {})}
    src = labels["sourceName"]
    names = {**STATUS_NAMES, **chart.get("statuses", {})}
    root = chart["root"]
    out = []
    w = out.append

    def meta(n):
        bits = []
        if n.get("kind") == "character":
            bits.append("CHARACTER")
        if n.get("ch") is not None:
            bits.append(f"{src} {n['ch']}")
        if n.get("status"):
            bits.append(n["status"])
        return (" · " + " · ".join(bits)) if bits else ""

    def details(n, pad):
        if n.get("note"):
            w(f"{pad}How: {n['note']}")
        if n.get("quote"):
            w(f"{pad}Quote ({src} {n.get('ch')}): “{n['quote']}”")
        if n.get("proposed"):
            w(f"{pad}Proposed (not in the source yet): “{n['proposed']}”")

    def path_of(target):
        def find(n, trail):
            if n is target:
                return trail
            for k in n.get("kids", []):
                r = find(k, trail + [n])
                if r is not None:
                    return r
            return None
        return find(root, []) or []

    allboxes = [n for n, _ in walk(root)]
    title = chart.get("title") or "Harada chart"
    w(f"# {title}: agent edition")
    w("")
    w(f"Generated from `{chart_name}` by the Harada method's `harada_chart.py`. Don't edit this file: "
      "edit the JSON (or the published page, then sync) and rebuild. Same content as the chart page, "
      "written to be read in order.")
    w("")
    w("## How to read this")
    w("")
    w(f"- The chart is a tree. The center is {labels['center'].lower()}. **Every box's children are how it gets to that box.**")
    w(f"- Each box is `[id] Title`, then where it comes from ({src} N) and its status, if any.")
    w("  - **How:** how the box gets to the box above it.")
    w(f"  - **Quote:** exact words from the {src.lower()} named; every one is checked against the source when the chart is built.")
    w("  - **Proposed:** candidate wording that is *not* in the source. It's waiting on the author. Never treat it as canon.")
    w("- Ids give the position: `p3-6-2` is the 3rd box around the center, its 6th box, and that box's 2nd box.")
    w("- Statuses: " + "; ".join(f"`{k}` = {v}" for k, v in names.items()) + ". A box with no status is structure.")
    w("- `CHARACTER` marks an actor. Its children are facets: Start, Wants, Needs, Stands for, In the way (or Flaw, Blind spot), Arc, Voice, End.")
    st = {k: sum(1 for n in allboxes if n.get("status") == k) for k in names}
    depth = max(d for _, d in walk(root))
    w(f"- Size: {len(allboxes)} boxes, {depth} levels below the center. " + ", ".join(f"{v} {names[k]}" for k, v in st.items()) + ".")
    w("")
    w("## At a glance")
    w("")
    w(f"**{labels['center']}: {root['title']}**")
    w("")
    for i, k in enumerate(root.get("kids", []), 1):
        w(f"{i}. **[{k['id']}] {k['title']}**{meta(k)}")
        for f in k.get("kids", []):
            w(f"   - [{f['id']}] {f['title']}")
    w("")
    parent = {}
    for n, _ in walk(root):
        for k in n.get("kids", []):
            parent[id(k)] = n
    for key in ("author", "thin", "open"):
        # One entry per decision: a box with this status whose parent doesn't
        # share it. Its children with the same status are listed as its options.
        items = [n for n in allboxes if n.get("status") == key
                 and parent.get(id(n), {}).get("status") != key]
        if not items:
            continue
        heading = names[key][0].upper() + names[key][1:]
        w(f"## {heading}: {len(items)} item{'s' if len(items) != 1 else ''}")
        w("")
        for n in items:
            trail = " › ".join(p["title"] for p in path_of(n)[1:])
            w(f"- **[{n['id']}] {n['title']}**{meta(n)}" + (f" — under {trail}" if trail else ""))
            if n.get("note"):
                w(f"  {n['note']}")
            label = "Option" if key == "author" else "Includes"
            for o in [k for k in n.get("kids", []) if k.get("status") == key]:
                w(f"  - {label} [{o['id']}] {o['title']}" + (f": {o['note']}" if o.get("note") else ""))
                for oo in [k for k in o.get("kids", []) if k.get("status") == key]:
                    w(f"    - {label} [{oo['id']}] {oo['title']}" + (f": {oo['note']}" if oo.get("note") else ""))
        w("")
    if chart.get("loose"):
        w("## Not on the chart yet")
        w("")
        for l in chart["loose"]:
            w(f"- **{l['id']}**: {l['text']}" + (f" · {l['status']}" if l.get("status") else ""))
        w("")
    w("## The chart")
    w("")
    w(f"### {labels['center']} [{root['id']}]: {root['title']}{meta(root)}")
    w("")
    details(root, "")
    w("")

    def box(n, depth):
        if depth == 1:
            w(f"## [{n['id']}] {n['title']}{meta(n)}")
            w("")
            details(n, "")
            w("")
        elif depth == 2:
            w(f"### [{n['id']}] {n['title']}{meta(n)}")
            w("")
            details(n, "")
            w("")
        else:
            pad = "  " * (depth - 3)
            w(f"{pad}- **[{n['id']}] {n['title']}**{meta(n)}")
            details(n, pad + "  ")
        for k in n.get("kids", []):
            box(k, depth + 1)
        if depth == 2 and n.get("kids"):
            w("")

    for k in root.get("kids", []):
        box(k, 1)
    return "\n".join(out).rstrip() + "\n"


def from_page(page_path, chart_path):
    html = pathlib.Path(page_path).read_text(encoding="utf-8")
    m = re.search(r"^const DATA = (.*);$", html, re.M)
    if not m:
        sys.exit(f"{page_path}: no chart data found (expected a line starting 'const DATA = ')")
    chart = json.loads(m.group(1))
    pathlib.Path(chart_path).write_text(json.dumps(chart, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"Pulled the chart from {page_path} into {chart_path}")
    return chart


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("chart", help="the chart JSON file")
    ap.add_argument("--sources", help="glob of the source text files quotes are checked against")
    ap.add_argument("--check", action="store_true", help="check only; don't build")
    ap.add_argument("--out", help="page to build (default: the chart's name with .html)")
    ap.add_argument("--md", help="agent edition to write (default: the chart's name with .md)")
    ap.add_argument("--template", default=str(DEFAULT_TEMPLATE), help="viewer template")
    ap.add_argument("--from-page", metavar="FILE", help="pull edits from a saved copy of the published page first")
    args = ap.parse_args(argv)

    chart_path = pathlib.Path(args.chart)
    chart = from_page(args.from_page, chart_path) if args.from_page else json.loads(chart_path.read_text(encoding="utf-8"))
    sources = load_sources(args.sources) if args.sources else None
    errors, warnings, st = check(chart, sources)
    if st:
        print(f"{st['boxes']} boxes, {st['levels']} levels deep · on the page {st['paid']}, thin {st['thin']}, "
              f"open {st['open']}, needs the owner {st['author']}")
    for w in warnings:
        print("warning:", w)
    for e in errors:
        print("ERROR:", e)
    if errors:
        print(f"{len(errors)} error(s); page not built.")
        return 1
    if not args.check:
        out = args.out or chart_path.with_suffix(".html")
        build(chart, args.template, out)
        md = args.md or chart_path.with_suffix(".md")
        pathlib.Path(md).write_text(to_markdown(chart, chart_path.name), encoding="utf-8")
        print(f"Built {out} and {md}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
