#!/usr/bin/env python3
"""Check and build the Pathwell Harada chart.

The chart's source is pathwell-harada.json in this folder. This script:

  1. checks it: every manuscript quote must appear in the chapter it names,
     no box may have more than eight boxes inside it, ids must be unique,
     and statuses must be one of the four the chart uses;
  2. warns about wording problems the method page asks us to avoid
     (see Chart-Method.md, "Rules for the boxes");
  3. builds pathwell-harada.html, the page that is published as the chart.

If the author edits the chart on the published page, save that page's HTML
and pull the edits back into the JSON first:

  python3 Story/Revision/Harada/build_chart.py --from-page saved-page.html

Usage, from the repository root:

  python3 Story/Revision/Harada/build_chart.py            # check, then build
  python3 Story/Revision/Harada/build_chart.py --check    # check only
  python3 Story/Revision/Harada/build_chart.py --from-page FILE   # sync, check, build

Exit status is 1 if the check finds errors (warnings don't fail it).
"""
import argparse
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CHAPTERS = ROOT / "Story" / "Chapters"
SOURCE = HERE / "pathwell-harada.json"
TEMPLATE = HERE / "chart-template.html"
OUTPUT = HERE / "pathwell-harada.html"

STATUSES = {"paid", "thin", "open", "author"}
MAX_KIDS = 8
LONG_TITLE = 70

# The same document head the published page writes when it saves itself,
# so a page built here and a page saved from the browser are identical.
HEAD = ('<!doctype html><html><head><meta charset=utf8><meta name=viewport '
        'content="width=device-width,initial-scale=1,viewport-fit=cover"><style>'
        ':root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);'
        'padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;'
        'font:14px system-ui,-apple-system,"Segoe UI",sans-serif}'
        'img{max-width:100%}[hidden]{display:none!important}</style></head><body>')
TAIL = "</body></html>"

# Box titles that are only a label, not a statement. Each was a real box in an
# earlier version; Chart-Method.md explains why they were replaced.
LABEL_TITLES = {"the pile", "help!", "recalculates", "the line", "the cost",
                "the claim", "the question", "his answer", "no answer"}


def chapters():
    return {i: re.sub(r"\s+", " ", (CHAPTERS / f"Chapter_{i:02d}.txt").read_text())
            for i in range(1, 19)}


def walk(node, depth=0, parent=None):
    yield node, depth, parent
    for kid in node.get("kids", []):
        yield from walk(kid, depth + 1, node)


def check(data):
    text = chapters()
    errors, warnings = [], []
    seen = set()
    counts = {s: 0 for s in STATUSES}
    boxes = deepest = 0
    for n, depth, parent in walk(data["root"]):
        boxes += 1
        deepest = max(deepest, depth)
        where = f'{n.get("id", "?")} “{n.get("title", "")}”'
        if not n.get("title", "").strip():
            errors.append(f"{where}: box has no title")
        if n.get("id") in seen:
            errors.append(f"{where}: duplicate id")
        seen.add(n.get("id"))
        if len(n.get("kids", [])) > MAX_KIDS:
            errors.append(f"{where}: {len(n['kids'])} boxes inside; the sheet holds {MAX_KIDS}")
        s = n.get("status")
        if s and s not in STATUSES:
            errors.append(f"{where}: unknown status {s!r}")
        elif s:
            counts[s] += 1
        q = n.get("quote")
        if q:
            ch = n.get("ch")
            if not isinstance(ch, int) or not 1 <= ch <= 18:
                errors.append(f"{where}: has a quote but no chapter")
            elif re.sub(r"\s+", " ", q) not in text[ch]:
                errors.append(f"{where}: quote not found in Chapter {ch}: {q[:80]}")
        # wording warnings (Chart-Method.md, rules 3-6)
        title = n.get("title", "")
        if len(title) > LONG_TITLE:
            warnings.append(f"{where}: title is {len(title)} characters; aim for under {LONG_TITLE}")
        if title.strip().lower() in LABEL_TITLES:
            warnings.append(f"{where}: title is a label, not a statement of what the box does")
        if n.get("kids") and not n.get("note"):
            warnings.append(f"{where}: has boxes inside but no note saying how it gets to the box above")
        if n.get("proposed") and n.get("status") != "author":
            warnings.append(f"{where}: proposed wording should be marked as needing the author")
    return errors, warnings, {"boxes": boxes, "levels": deepest, **counts}


def safe_json(obj):
    s = json.dumps(obj, ensure_ascii=False, separators=(",", ":"))
    return s.replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")


def build(data):
    template = TEMPLATE.read_text()
    if len(re.findall(r"__(DATA|TEMPLATE)__", template)) != 2:
        sys.exit("chart-template.html must contain __DATA__ and __TEMPLATE__ exactly once each")
    content = re.sub(r"__(DATA|TEMPLATE)__",
                     lambda m: safe_json(data) if m.group(1) == "DATA" else safe_json(template),
                     template)
    OUTPUT.write_text(HEAD + content + TAIL)


def from_page(path):
    html = pathlib.Path(path).read_text()
    m = re.search(r"^const DATA = (.*);$", html, re.M)
    if not m:
        sys.exit(f"{path}: no chart data found (expected a line starting 'const DATA = ')")
    data = json.loads(m.group(1))
    SOURCE.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n")
    print(f"Pulled the chart from {path} into {SOURCE.name}")
    return data


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="check only; don't build the page")
    ap.add_argument("--from-page", metavar="FILE", help="pull edits from a saved copy of the published page first")
    args = ap.parse_args()

    data = from_page(args.from_page) if args.from_page else json.loads(SOURCE.read_text())
    errors, warnings, stats = check(data)
    print(f"{stats['boxes']} boxes, {stats['levels']} levels deep · "
          f"on the page {stats['paid']}, thin {stats['thin']}, open {stats['open']}, needs the author {stats['author']}")
    for w in warnings:
        print("warning:", w)
    for e in errors:
        print("ERROR:", e)
    if errors:
        print(f"{len(errors)} error(s); page not built.")
        return 1
    if not args.check:
        build(data)
        print(f"Built {OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
