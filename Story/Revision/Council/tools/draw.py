#!/usr/bin/env python3
"""Draw council members for a read, and optionally write their filled-in briefs.

Run from the repository root. Examples:

    # 5 random members, spread across families, skipping anyone used in the last 2 runs
    python3 Story/Revision/Council/tools/draw.py --n 5 --avoid-recent 2

    # pick by hand, plus 2 random wildcards from other families
    python3 Story/Revision/Council/tools/draw.py --include 17 --include comedy-writer --n 4

    # only market and adversarial seats, reproducible
    python3 Story/Revision/Council/tools/draw.py --family market --family adversarial --n 3 --seed 7

    # write ready-to-send briefs for the draw, pointing at a frozen copy of the text
    python3 Story/Revision/Council/tools/draw.py --n 5 --text /path/to/frozen/Pathwell.txt --briefs /path/to/briefs

Chained members (they need several agents) are left out of random draws unless --allow-chained.
"""
import argparse, json, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
COUNCIL = os.path.dirname(HERE)
ROSTER = json.load(open(os.path.join(COUNCIL, "roster.json")))
LEDGER = os.path.join(COUNCIL, "LEDGER.md")


def find(key):
    for m in ROSTER:
        if key in (m["id"], m["slug"], m["id"].lstrip("0")):
            return m
    sys.exit(f"No council member '{key}'. See ROSTER.md.")


def recent_slugs(k):
    """Members used in the last k ledger rows (rows are newest last)."""
    if k <= 0 or not os.path.exists(LEDGER):
        return set()
    rows = [l for l in open(LEDGER) if l.startswith("| 20")]
    used = set()
    for row in rows[-k:]:
        used.update(re.findall(r"\b([a-z]+(?:-[a-z]+)+)\b", row))
    return used & {m["slug"] for m in ROSTER}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--n", type=int, default=5, help="total members to seat (default 5)")
    ap.add_argument("--include", action="append", default=[], help="seat this member (id or slug); repeatable")
    ap.add_argument("--exclude", action="append", default=[], help="never seat this member; repeatable")
    ap.add_argument("--family", action="append", default=[], help="draw only from these families; repeatable")
    ap.add_argument("--avoid-recent", type=int, default=0, help="skip members used in the last K ledger runs")
    ap.add_argument("--allow-chained", action="store_true", help="allow chained (multi-agent) members in random draws")
    ap.add_argument("--seed", type=int, help="random seed, for a reproducible draw")
    ap.add_argument("--text", help="path to the frozen manuscript copy (fills {TEXT} in the briefs)")
    ap.add_argument("--briefs", help="folder to write filled briefs into (one file per member)")
    a = ap.parse_args()

    rng = random.Random(a.seed)
    seated = [find(k) for k in a.include]
    excluded = {find(k)["slug"] for k in a.exclude} | recent_slugs(a.avoid_recent)
    pool = [m for m in ROSTER
            if m["slug"] not in excluded and m not in seated
            and (not a.family or m["family"] in a.family)
            and (a.allow_chained or not m["chained"])]

    # Spread across families first: one per family not yet seated, in random order, then fill.
    fams = sorted({m["family"] for m in pool})
    rng.shuffle(fams)
    for f in fams:
        if len(seated) >= a.n:
            break
        if any(s["family"] == f for s in seated):
            continue
        choices = [m for m in pool if m["family"] == f]
        pick = rng.choice(choices)
        seated.append(pick); pool.remove(pick)
    while len(seated) < a.n and pool:
        pick = rng.choice(pool)
        seated.append(pick); pool.remove(pick)

    print(f"{'ID':<4}{'Member':<38}{'Family':<12}{'Model':<8}Card")
    for m in seated:
        print(f"{m['id']:<4}{m['name']:<38}{m['family']:<12}{m['model']:<8}{m['file']}")
    fams_seated = {m["family"] for m in seated}
    print(f"\n{len(seated)} seated across {len(fams_seated)} families: {', '.join(sorted(fams_seated))}")

    if a.briefs:
        if not a.text:
            sys.exit("--briefs needs --text (the frozen manuscript path).")
        os.makedirs(a.briefs, exist_ok=True)
        for m in seated:
            card = open(os.path.join(COUNCIL, m["file"])).read()
            brief = card.split("````text\n", 1)[1].rsplit("````", 1)[0]
            out = os.path.join(a.briefs, f"{m['slug']}_report.md")
            brief = brief.replace("{TEXT}", a.text).replace("{OUT}", out)
            path = os.path.join(a.briefs, f"{m['id']}-{m['slug']}_brief.md")
            open(path, "w").write(brief)
            print("brief:", path)


if __name__ == "__main__":
    main()
