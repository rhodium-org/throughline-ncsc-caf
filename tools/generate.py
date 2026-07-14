#!/usr/bin/env python3
"""Generate the NCSC CAF 4.0 throughline source from the hand-transcribed data.

The CAF is published as HTML/PDF, not a clean data export, so the content is transcribed
into ``tools/caf_data.py`` (from the vendored ``tools/caf-4.0/`` PDF, © Crown copyright,
OGL v3.0). This script turns those records into throughline items, mirroring the AISVS /
GOV.UK generators' discipline:

* **UIDs are permanent.** The mapping from an Objective / Principle / Contributing Outcome
  handle to a throughline UID is derived from the items already on disk, keyed by
  ``attrs.source_ref`` (the CAF handle: ``"A"``, ``"A2"``, ``"A2.a"``). Anything without an
  item yet gets a freshly allocated UID in document order; a UID, once allocated, never
  moves. Bodies regenerate from ``caf_data.py`` each run.

**The "why" spine is genuinely multi-root.** The CAF's four Objectives (A managing risk /
B protecting / C detecting / D minimising impact) are four distinct reasons an organisation
must act, so there are **four co-equal root intents** (INT-0001..INT-0004 = A..D), never a
single umbrella. Each Principle is a ``user_requirement`` that ``derives_from`` its own
Objective and carries the principle's published statement as its ``rationale``; each
Contributing Outcome is a ``system_requirement`` that ``implements`` its principle, with the
CAF handle in ``attrs.source_ref`` and its Indicators of Good Practice in ``attrs.igp_*``.

**The CAF is outcome-based, not graded** — there are no assurance levels, so a system
requirement carries no ``attrs.level`` (unlike ASVS / AISVS). Editions (4.0, and future
revisions) are git tags of this one repo.

Usage:  python tools/generate.py
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "tools"))

import caf_data  # noqa: E402

INTENTS_DIR = REPO / "intents"        # intent (Objective roots), prefix INT
PRINCIPLES_DIR = REPO / "principles"  # user_requirement (Principles), prefix UR
OUTCOMES_DIR = REPO / "outcomes"      # system_requirement (Contributing Outcomes), prefix SR
SPEC = REPO / "docs" / "spec.md"


def _dump(path: Path, item: dict) -> None:
    path.write_text(
        yaml.safe_dump(item, sort_keys=False, allow_unicode=True, width=90),
        encoding="utf-8",
    )


def _scan(dir_: Path) -> dict[str, str]:
    ref2uid: dict[str, str] = {}
    for f in dir_.glob("*.yml"):
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
        ref = (data.get("attrs") or {}).get("source_ref")
        if ref:
            ref2uid[ref] = data["uid"]
    return ref2uid


def _max(ref2uid: dict[str, str], prefix: str) -> int:
    return max((int(u.split("-")[1]) for u in ref2uid.values()
               if u.startswith(prefix + "-")), default=0)


def generate() -> dict[str, int]:
    int_ref = _scan(INTENTS_DIR)
    ur_ref = _scan(PRINCIPLES_DIR)
    sr_ref = _scan(OUTCOMES_DIR)
    n_int = _max(int_ref, "INT") + 1
    n_ur = _max(ur_ref, "UR") + 1
    n_sr = _max(sr_ref, "SR") + 1
    counts = {"int": 0, "ur": 0, "sr": 0}

    for obj in caf_data.OBJECTIVES:
        oref = obj["id"]
        int_uid = int_ref.get(oref)
        if int_uid is None:
            int_uid = f"INT-{n_int:04d}"; n_int += 1; int_ref[oref] = int_uid
            counts["int"] += 1
        _dump(INTENTS_DIR / f"{int_uid}.yml", {
            "uid": int_uid,
            "type": "intent",
            "status": "approved",
            "title": f"Objective {oref} — {obj['title']}",
            "text": obj["text"],
            "normative": False,
            "attrs": {"source_ref": oref},
        })

    for pr in caf_data.PRINCIPLES:
        pref = pr["id"]
        int_uid = int_ref[pr["objective"]]
        ur_uid = ur_ref.get(pref)
        if ur_uid is None:
            ur_uid = f"UR-{n_ur:04d}"; n_ur += 1; ur_ref[pref] = ur_uid
            counts["ur"] += 1
        _dump(PRINCIPLES_DIR / f"{ur_uid}.yml", {
            "uid": ur_uid,
            "type": "user_requirement",
            "status": "approved",
            "title": f"{pref} — {pr['title']}",
            "text": pr["title"],
            "rationale": pr["statement"],
            "links": [{"target": int_uid, "type": "derives_from"}],
            "attrs": {"source_ref": pref},
        })

    for oc in caf_data.OUTCOMES:
        cref = oc["id"]
        ur_uid = ur_ref[oc["principle"]]
        sr_uid = sr_ref.get(cref)
        if sr_uid is None:
            sr_uid = f"SR-{n_sr:04d}"; n_sr += 1; sr_ref[cref] = sr_uid
            counts["sr"] += 1
        attrs = {"source_ref": cref}
        if oc.get("not_achieved"):
            attrs["igp_not_achieved"] = oc["not_achieved"]
        if oc.get("partially_achieved"):
            attrs["igp_partially_achieved"] = oc["partially_achieved"]
        if oc.get("achieved"):
            attrs["igp_achieved"] = oc["achieved"]
        _dump(OUTCOMES_DIR / f"{sr_uid}.yml", {
            "uid": sr_uid,
            "type": "system_requirement",
            "status": "approved",
            "title": f"CAF {cref} — {oc['title']}",
            "text": oc["statement"] or oc["title"],
            "links": [{"target": ur_uid, "type": "implements"}],
            "attrs": attrs,
        })

    return counts


SPEC_HEADER = """\
# NCSC Cyber Assessment Framework 4.0 — throughline source

Generated from the graph. Prose between `tl:item` / `tl:table` markers is injected by
`tl docs` — edit the YAML items (or `tools/caf_data.py` + `tools/generate.py`), not the
injected regions.

The "why" spine is **multi-root by design**: the CAF's four Objectives (A managing security
risk, B protecting against cyber attack, C detecting cyber security events, D minimising the
impact of cyber security incidents) are four distinct reasons an organisation must act —
four root `intent`s, not one umbrella. Each Principle is a `user_requirement` that
`derives_from` its Objective and carries the principle's published statement as its
`rationale`; each Contributing Outcome is a `system_requirement` that `implements` its
principle. The CAF handle lives in `attrs.source_ref` (`"A2.a"`) and the Indicators of Good
Practice in `attrs.igp_*`. The CAF is outcome-based, so there are no assurance levels.
"""


def generate_spec() -> None:
    int_ref = _scan(INTENTS_DIR)
    ur_ref = _scan(PRINCIPLES_DIR)
    parts = [SPEC_HEADER]
    for obj in caf_data.OBJECTIVES:
        oref = obj["id"]
        int_uid = int_ref[oref]
        parts.append(f"# Objective {oref} — {obj['title']}\n")
        parts.append(f"<!-- tl:item {int_uid} -->\n<!-- tl:end -->\n")
        for pr in caf_data.PRINCIPLES:
            if pr["objective"] != oref:
                continue
            ur_uid = ur_ref[pr["id"]]
            parts.append(f"## Principle {pr['id']} {pr['title']}\n")
            parts.append(f"<!-- tl:item {ur_uid} -->\n<!-- tl:end -->\n")
            flt = ("type == 'system_requirement' and "
                   f"attrs.get('source_ref').startswith('{pr['id']}.')")
            parts.append(f"<!-- tl:table {flt} -->\n<!-- tl:end -->\n")
    SPEC.parent.mkdir(parents=True, exist_ok=True)
    SPEC.write_text("\n".join(parts) + "\n", encoding="utf-8")


def main() -> int:
    c = generate()
    generate_spec()
    print(f"intents:  {c['int']} new (Objectives)")
    print(f"principles: {c['ur']} new (user_requirements)")
    print(f"outcomes: {c['sr']} new (system_requirements)")
    print(f"totals: {len(list(INTENTS_DIR.glob('INT-*.yml')))} INT, "
          f"{len(list(PRINCIPLES_DIR.glob('UR-*.yml')))} UR, "
          f"{len(list(OUTCOMES_DIR.glob('SR-*.yml')))} SR")
    print("next: run `tl docs` to inject content, then `tl check --strict`")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
