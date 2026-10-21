#!/usr/bin/env python3
"""Check and build the Pathwell Harada chart.

A thin wrapper: the checker, the builder and the viewer belong to the Harada
method in Story/Harada-Method/ (its SKILL.md says how to use them). This file
only supplies Pathwell's paths, so the commands stay short:

  python3 Story/Revision/Harada/build_chart.py                 # check, then build
  python3 Story/Revision/Harada/build_chart.py --check         # check only
  python3 Story/Revision/Harada/build_chart.py --from-page F   # pull page edits, check, build
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "Story" / "Harada-Method" / "scripts"))
import harada_chart  # noqa: E402

if __name__ == "__main__":
    sys.exit(harada_chart.main([
        str(HERE / "pathwell-harada.json"),
        "--sources", str(ROOT / "Story" / "Chapters" / "Chapter_*.txt"),
        "--out", str(HERE / "pathwell-harada.html"),
        *sys.argv[1:],
    ]))
