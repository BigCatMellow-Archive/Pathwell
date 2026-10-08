#!/usr/bin/env python3
"""Counts for a reader panel (Reader-Panel.md, steps 7-8 and the checks on the panel).

Mechanical only: it applies the protocol's rules to the extracted records and the
two merges. Every judgement (which subjects match, which + and - findings form a
split, whether a finding is real) stays with the merge and synthesis agents.

Usage:
  panel_counts.py --records all_records.csv --merge A=merge_A.csv --merge B=merge_B.csv --out DIR

Writes to DIR:
  clusters_<M>.csv      one row per cluster of merge M, with readers, families,
                        severity and the mechanical sort category
  merge_compare.md      pair agreement between the merges, and every multi-record
                        cluster whose records the other merge groups differently
  sort_compare.csv      for every cluster in either merge, its category under both
  checks.md             the noise check, the diversity check (overlap, unique
                        contribution, coverage) and the counts behind the sort
"""
import argparse
import collections
import csv
import itertools
import os

# The roster (Reader-Panel.md, "The roster"). Lens -> (family, built to find).
ROSTER = {
    "target": ("experience", {"tone", "strength", "pacing"}),
    "reluctant": ("experience", {"confusion", "rule", "pacing"}),
    "skimmer": ("experience", {"pacing", "confusion", "structure"}),
    "bookclub": ("experience", {"strength", "motivation", "tone"}),
    "auditor": ("audit", {"continuity", "confusion"}),
    "rules": ("audit", {"rule", "promise"}),
    "character": ("craft", {"motivation", "voice/repetition", "promise"}),
    "editor": ("craft", {"structure", "pacing", "promise"}),
    "prose": ("craft", {"voice/repetition", "tone"}),
    "rereader": ("craft", {"promise", "structure"}),
    "middle": ("craft", {"structure", "promise", "confusion"}),
    "hostile": ("adversarial", set()),
    "goals": ("goals", set()),
}
SEV = {"stopper": 3, "snag": 2, "quibble": 1, "strong": 2, "mild": 1}
SEV_NAME = {
    "-": {3: "stopper", 2: "snag", 1: "quibble"},
    "+": {2: "strong", 1: "mild"},
}
# Repeated lenses: lens -> the runs of it.
CATEGORIES = ["convergent", "short of convergent", "lens-specific", "minority", "noise suspect"]


def reader(r):
    return f"{r['lens']}-{r['run']}"


def family(lens):
    return ROSTER.get(lens, ("unknown", set()))[0]


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def build_clusters(records, merge):
    by_id = {r["id"]: r for r in records}
    clusters = collections.OrderedDict()
    titles = {}
    for row in merge:
        clusters.setdefault(row["cluster"], []).append(by_id[row["id"]])
        titles[row["cluster"]] = row["cluster_title"]
    return clusters, titles


def describe(cid, recs, title, runs_per_lens):
    unp = [r for r in recs if r["prompted"] == "unprompted"]
    readers_all = sorted({reader(r) for r in recs})
    readers_unp = sorted({reader(r) for r in unp})
    lenses_unp = sorted({r["lens"] for r in unp})
    fams_unp = sorted({family(r["lens"]) for r in unp if family(r["lens"]) != "goals"})
    # The goals lens never counts toward convergence.
    readers_conv = [x for x in readers_unp if not x.startswith("goals-")]
    pol = recs[0]["polarity"]
    typ = recs[0]["type"]
    sev = max(SEV.get(r["severity"], 0) for r in recs)
    lenses_all = sorted({r["lens"] for r in recs})
    if len(fams_unp) >= 2 and len(readers_conv) >= 3:
        cat = "convergent"
    elif len(lenses_all) == 1:
        lens = lenses_all[0]
        repeated = runs_per_lens.get(lens, 1) > 1
        if repeated and len(readers_all) == 1:
            cat = "noise suspect"
        elif typ in ROSTER.get(lens, ("", set()))[1]:
            cat = "lens-specific"
        else:
            cat = "minority"
    else:
        # Two or more lenses, short of the bar (or only prompted). Not named in
        # the protocol's four lists; kept as its own list so nothing is dropped.
        cat = "short of convergent"
    return {
        "cluster": cid,
        "title": title,
        "type": typ,
        "polarity": pol,
        "severity": SEV_NAME[pol].get(sev, str(sev)),
        "sev_rank": sev,
        "records": len(recs),
        "readers": ";".join(readers_all),
        "readers_unprompted": ";".join(readers_unp),
        "n_readers_unprompted": len(readers_conv),
        "families_unprompted": ";".join(fams_unp),
        "n_families_unprompted": len(fams_unp),
        "chapters": ";".join(sorted({c for r in recs for c in r["chapters"].split(";") if c},
                                     key=lambda c: int("".join(ch for ch in c if ch.isdigit()) or 0))),
        "top_ten_by": ";".join(sorted({reader(r) for r in recs if r["rank"]})),
        "category": cat,
        "ids": ";".join(r["id"] for r in recs),
        "quotes": " | ".join(sorted({r["quote"] for r in recs if r["quote"]})[:3]),
    }


def pairs(clusters):
    out = set()
    for recs in clusters.values():
        ids = sorted(r["id"] for r in recs)
        out.update(itertools.combinations(ids, 2))
    return out


def dice(a, b):
    return (2 * len(a & b) / (len(a) + len(b))) if (a or b) else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--records", required=True)
    ap.add_argument("--merge", action="append", required=True, help="NAME=path")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)

    records = load(args.records)
    ids = [r["id"] for r in records]
    runs_per_lens = collections.Counter()
    for lens, run in {(r["lens"], r["run"]) for r in records}:
        runs_per_lens[lens] += 1

    merges = {}
    report = []
    for spec in args.merge:
        name, path = spec.split("=", 1)
        rows = load(path)
        out_ids = [r["id"] for r in rows]
        missing = set(ids) - set(out_ids)
        extra = set(out_ids) - set(ids)
        dup = [k for k, v in collections.Counter(out_ids).items() if v > 1]
        clusters, titles = build_clusters(records, rows)
        mixed = [c for c, recs in clusters.items()
                 if len({(r["type"], r["polarity"]) for r in recs}) > 1]
        report.append(f"- Merge {name}: {len(rows)} rows for {len(ids)} records; missing {len(missing)}, "
                      f"unknown {len(extra)}, duplicated {len(dup)}; {len(clusters)} clusters; "
                      f"clusters mixing type or polarity: {len(mixed)}"
                      + (f" ({', '.join(mixed[:10])})" if mixed else ""))
        desc = [describe(c, recs, titles[c], runs_per_lens) for c, recs in clusters.items()]
        merges[name] = {"clusters": clusters, "titles": titles, "desc": {d["cluster"]: d for d in desc}}
        of = os.path.join(args.out, f"clusters_{name}.csv")
        with open(of, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(desc[0].keys()), quoting=csv.QUOTE_ALL)
            w.writeheader()
            for d in sorted(desc, key=lambda d: (CATEGORIES.index(d["category"]), d["polarity"] != "-",
                                                 -d["sev_rank"], -d["n_families_unprompted"],
                                                 -d["n_readers_unprompted"], d["cluster"])):
                w.writerow(d)

    names = list(merges)
    rec_cluster = {n: {r["id"]: c for c, recs in merges[n]["clusters"].items() for r in recs} for n in names}

    # ---- merge comparison
    cmp_lines = ["# Merge comparison", "", "Completeness:", ""] + report + [""]
    if len(names) == 2:
        a, b = names
        pa, pb = pairs(merges[a]["clusters"]), pairs(merges[b]["clusters"])
        both = pa & pb
        cmp_lines += [
            f"Record pairs grouped together: {a} {len(pa)}, {b} {len(pb)}, both {len(both)} "
            f"(agreement on grouped pairs, Dice {dice(pa, pb):.2f}).",
            "",
            f"Records that are singletons in both merges: "
            f"{sum(1 for i in ids if len(merges[a]['clusters'][rec_cluster[a][i]]) == 1 and len(merges[b]['clusters'][rec_cluster[b][i]]) == 1)} of {len(ids)}.",
            "",
        ]
        for x, y in ((a, b), (b, a)):
            cmp_lines += [f"## {x} clusters (two or more records) that {y} groups differently", ""]
            n = 0
            for c, recs in merges[x]["clusters"].items():
                if len(recs) < 2:
                    continue
                ys = collections.defaultdict(list)
                for r in recs:
                    ys[rec_cluster[y][r["id"]]].append(r["id"])
                same = len(ys) == 1 and len(merges[y]["clusters"][next(iter(ys))]) == len(recs)
                if same:
                    continue
                n += 1
                cmp_lines.append(f"- **{x} {c}** ({len(recs)}; {merges[x]['desc'][c]['category']}): {merges[x]['titles'][c]}")
                for yc, members in ys.items():
                    extra = len(merges[y]["clusters"][yc]) - len(members)
                    cmp_lines.append(f"  - {y} {yc} ({merges[y]['desc'][yc]['category']}): "
                                     f"{merges[y]['titles'][yc]} — holds {', '.join(members)}"
                                     + (f" and {extra} more" if extra else ""))
            cmp_lines += ["", f"{n} {x} clusters differ.", ""]
    with open(os.path.join(args.out, "merge_compare.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(cmp_lines) + "\n")

    # ---- sort compared across merges: one row per (cluster in either), its category in both
    if len(names) == 2:
        a, b = names
        rows = []
        seen = set()
        for c, recs in merges[a]["clusters"].items():
            bcs = sorted({rec_cluster[b][r["id"]] for r in recs})
            cats_b = sorted({merges[b]["desc"][x]["category"] for x in bcs})
            d = merges[a]["desc"][c]
            rows.append({"merge": a, "cluster": c, "title": d["title"], "type": d["type"], "polarity": d["polarity"],
                         "severity": d["severity"], "category_here": d["category"],
                         "other_clusters": ";".join(bcs), "category_other": ";".join(cats_b),
                         "agree": "yes" if cats_b == [d["category"]] else "no"})
        for c, recs in merges[b]["clusters"].items():
            acs = sorted({rec_cluster[a][r["id"]] for r in recs})
            cats_a = sorted({merges[a]["desc"][x]["category"] for x in acs})
            d = merges[b]["desc"][c]
            rows.append({"merge": b, "cluster": c, "title": d["title"], "type": d["type"], "polarity": d["polarity"],
                         "severity": d["severity"], "category_here": d["category"],
                         "other_clusters": ";".join(acs), "category_other": ";".join(cats_a),
                         "agree": "yes" if cats_a == [d["category"]] else "no"})
        with open(os.path.join(args.out, "sort_compare.csv"), "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), quoting=csv.QUOTE_ALL)
            w.writeheader()
            w.writerows(rows)

    # ---- checks
    lines = ["# Counts for the sort and the checks on the panel", ""]
    lines += ["Severity floor for the checks: snag or above, and strong strengths (quibbles and mild strengths are left out).", ""]
    for n in names:
        desc = merges[n]["desc"].values()
        lines += [f"## Merge {n}", "", "### Sort, mechanical first cut", "",
                  "| Category | All clusters | At the floor | Stoppers |", "| --- | --- | --- | --- |"]
        for cat in CATEGORIES:
            ds = [d for d in desc if d["category"] == cat]
            lines.append(f"| {cat} | {len(ds)} | {sum(1 for d in ds if d['sev_rank'] >= 2)} | "
                         f"{sum(1 for d in ds if d['sev_rank'] >= 3 and d['polarity'] == '-')} |")
        lines.append("")

        # noise check per repeated lens
        lines += ["### Noise check (repeated lenses)", ""]
        for lens, k in runs_per_lens.items():
            if k < 2:
                continue
            runs = sorted({reader(r) for r in records if r["lens"] == lens})
            sets = {}
            for rn in runs:
                sets[rn] = {c for c, recs in merges[n]["clusters"].items()
                            if any(reader(r) == rn and SEV.get(r["severity"], 0) >= 2 for r in recs)}
            for x, y in itertools.combinations(runs, 2):
                either = sets[x] | sets[y]
                bothc = {c for c in either
                         if {reader(r) for r in merges[n]["clusters"][c]} >= {x, y}}
                pct = 100 * len(bothc) / len(either) if either else 0
                lines.append(f"- {x} raised {len(sets[x])} findings at the floor, {y} raised {len(sets[y])}; "
                             f"either {len(either)}, both {len(bothc)}: overlap {pct:.0f}%.")
                # top-ten overlap between the runs, for the diversity comparison
        lines.append("")

        # diversity: top-ten overlap
        top = collections.defaultdict(set)
        for c, recs in merges[n]["clusters"].items():
            for r in recs:
                if r["rank"]:
                    top[reader(r)].add(c)
        rd = sorted(top)
        lines += ["### Diversity: top-ten overlap (Dice, on clusters holding a ranked record)", "",
                  "| | " + " | ".join(rd) + " |", "| --- " * (len(rd) + 1) + "|"]
        for x in rd:
            lines.append(f"| {x} | " + " | ".join("—" if x == y else f"{dice(top[x], top[y]):.2f}" for y in rd) + " |")
        repeat_pairs = [(x, y) for x, y in itertools.combinations(rd, 2) if x.split("-")[0] == y.split("-")[0]]
        other = [dice(top[x], top[y]) for x, y in itertools.combinations(rd, 2) if (x, y) not in repeat_pairs]
        lines.append("")
        for x, y in repeat_pairs:
            lines.append(f"- Repeat pair {x} / {y}: {dice(top[x], top[y]):.2f}.")
        if other:
            lines.append(f"- Lens-to-lens pairs: mean {sum(other)/len(other):.2f}, max {max(other):.2f}.")
            hi = sorted(((dice(top[x], top[y]), x, y) for x, y in itertools.combinations(rd, 2)
                         if (x, y) not in repeat_pairs), reverse=True)[:5]
            lines.append("- Highest lens-to-lens pairs: " + "; ".join(f"{x}/{y} {v:.2f}" for v, x, y in hi) + ".")
        lines.append("")

        # unique contribution
        lines += ["### Diversity: unique contribution (clusters at the floor found by one reader or one family only)", "",
                  "| Reader | Findings at the floor | Only this reader | Only this reader, in its own types |",
                  "| --- | --- | --- | --- |"]
        for rn in sorted({reader(r) for r in records}):
            lens = rn.rsplit("-", 1)[0]
            own = ROSTER.get(lens, ("", set()))[1]
            mine = [c for c, recs in merges[n]["clusters"].items()
                    if any(reader(r) == rn for r in recs) and max(SEV.get(r["severity"], 0) for r in recs) >= 2]
            only = [c for c in mine if {reader(r) for r in merges[n]["clusters"][c]} == {rn}]
            only_own = [c for c in only if merges[n]["clusters"][c][0]["type"] in own]
            lines.append(f"| {rn} | {len(mine)} | {len(only)} | {len(only_own)} |")
        lines += ["", "| Family | Findings at the floor | Only this family |", "| --- | --- | --- |"]
        for fam in sorted({family(r["lens"]) for r in records}):
            mine = [c for c, recs in merges[n]["clusters"].items()
                    if any(family(r["lens"]) == fam for r in recs) and max(SEV.get(r["severity"], 0) for r in recs) >= 2]
            only = [c for c in mine if {family(r["lens"]) for r in merges[n]["clusters"][c]} == {fam}]
            lines.append(f"| {fam} | {len(mine)} | {len(only)} |")
        lines.append("")

    # coverage (records, merge-independent)
    lines += ["## Coverage: records by type and family (merge-independent)", ""]
    fams = sorted({family(r["lens"]) for r in records})
    types = sorted({r["type"] for r in records})
    lines += ["| Type | " + " | ".join(fams) + " | All | of which + |", "| --- " * (len(fams) + 3) + "|"]
    for t in types:
        row = [sum(1 for r in records if r["type"] == t and family(r["lens"]) == fm) for fm in fams]
        allt = sum(row)
        plus = sum(1 for r in records if r["type"] == t and r["polarity"] == "+")
        lines.append(f"| {t} | " + " | ".join(map(str, row)) + f" | {allt} | {plus} |")
    lines.append("")
    lines += ["## Records by reader", "", "| Reader | Model | Records | Unprompted | Prompted | Ranked |", "| --- | --- | --- | --- | --- | --- |"]
    for rn in sorted({reader(r) for r in records}):
        rs = [r for r in records if reader(r) == rn]
        lines.append(f"| {rn} | {rs[0]['model']} | {len(rs)} | {sum(r['prompted']=='unprompted' for r in rs)} | "
                     f"{sum(r['prompted']=='prompted' for r in rs)} | {sum(1 for r in rs if r['rank'])} |")
    with open(os.path.join(args.out, "checks.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(report))
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
