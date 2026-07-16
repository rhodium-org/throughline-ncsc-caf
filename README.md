# throughline-ncsc-caf

The **NCSC Cyber Assessment Framework (CAF) 4.0** expressed as a
[throughline](https://pypi.org/project/throughline/) **source** — a standalone, grounded
requirements graph that a consuming project composes with
[throughline-compose](https://github.com/timebacksolutions/throughline-compose).

This repository holds no application code. It is a directory of small YAML items with
permanent UIDs, validated by `tl check`. Consumers import it under a namespace and
reference its contributing outcomes as `caf:SR-0007`.

> **Status: full CAF 4.0 catalogue.** This holds the complete framework — all four
> Objectives, all fourteen Principles and all forty-one Contributing Outcomes, each with its
> published Indicators of Good Practice.

## Status

A grounded graph of
<!-- tl:count type == 'intent' -->
4
<!-- tl:end --> Objective intents,
<!-- tl:count type == 'user_requirement' -->
14
<!-- tl:end --> Principle requirements and
<!-- tl:count type == 'system_requirement' -->
41
<!-- tl:end --> contributing-outcome requirements, published to [`docs/spec.md`](docs/spec.md).
The counts are rendered from the live graph by `tl:count`, so they cannot drift.

## Why this source is multi-root

A throughline source gets **as many root intents as the standard has genuine "why"s** — a
single umbrella root would throw away the reason each clause exists, which is the whole
point of IDD. A single artificial `INT-0001` that every requirement ultimately hangs off is
the **anti-pattern**: it flattens four distinct security purposes into one bland "…exists".

The CAF is organised under **four top-level Objectives**, and those are four genuinely
different reasons an organisation must act — managing security risk is not the same "why" as
detecting events or recovering from an incident. So this graph has **four co-equal root
intents** (all `normative: false`), each carrying its Objective's own description as its
`text`:

| Root | Objective |
|---|---|
| `INT-0001` | **A** — Managing security risk |
| `INT-0002` | **B** — Protecting against cyber attack |
| `INT-0003` | **C** — Detecting cyber security events |
| `INT-0004` | **D** — Minimising the impact of cyber security incidents |

- Each of the CAF's **14 Principles** (e.g. `A2` Risk Management) is a `user_requirement`
  that `derives_from` **its own Objective** (not a catch-all), and carries the principle's
  published statement as its `rationale` — the mid-level *why* the CAF writes down.
- Each **Contributing Outcome** (`A2.a`) is a `system_requirement` that `implements` its
  principle. The CAF hierarchy is strict (one objective per principle), so an outcome
  grounds up to an Objective through `implements` → `derives_from` with no extra edge.

## Outcome-based, not graded — IGPs are attributes

Unlike ASVS or AISVS, the CAF is **outcome-based**: it describes *outcomes to achieve*, not
graded controls, so there are **no assurance levels**. What an assessor actually checks are
the **Indicators of Good Practice (IGPs)** — the statements that characterise an outcome
being *achieved*, *partially achieved* or *not achieved*. Those are preserved as structured
attributes on each contributing-outcome item:

- `attrs.source_ref` — the published CAF handle (`A2.a` for an outcome, `A2` for a
  principle, `A` for an objective), never the UID.
- `attrs.igp_not_achieved` / `attrs.igp_partially_achieved` / `attrs.igp_achieved` — the
  IGP statements for each assessment column (the middle column is present only where the CAF
  publishes a "partially achieved" state).

**Editions are git tags of this one repo.** `v4.0` tags the CAF 4.0 edition; a future CAF
revision would be a new tag on this same repo. A consumer pins `caf@v4.0`.

## Modelling conventions

- **throughline UIDs are this source's own** (`SR-0007`…), immutable and never the CAF
  handle. The CAF handle lives in `attrs.source_ref`.
- **An outcome's `text`** is its published outcome statement; where the CAF gives an outcome
  no separate statement (e.g. `A3.a`, `C2.a`), the item `text` falls back to the outcome
  title and the meaning is carried by its IGPs.
- The graph is generated from the hand-transcribed CAF content in `tools/caf_data.py` (from
  the vendored PDF under `tools/caf-4.0/`) by `tools/generate.py` (permanent-UID, additive).
  Editing the content means editing the data + generator, not the YAML by hand.

## Composing it

In a consuming project's `throughline.toml`:

```toml
[sources.caf]
url = "https://github.com/timebacksolutions/throughline-ncsc-caf"
ref = "v4.0"
```

Then reference a contributing outcome as `caf:SR-0007` from your own items.

## Licence

Repository structure, tooling and configuration: Apache-2.0 (see `LICENSE`). The CAF
Objective descriptions, Principle statements, Contributing Outcome statements and Indicators
of Good Practice are © Crown copyright, reproduced under the **Open Government Licence v3.0**
with attribution to the NCSC — see `NOTICE`. Authoritative source:
https://www.ncsc.gov.uk/collection/cyber-assessment-framework.
