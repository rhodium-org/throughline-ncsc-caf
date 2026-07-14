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

# Objective A — Managing security risk

<!-- tl:item INT-0001 -->
**INT-0001 — Objective A — Managing security risk** — `intent`, status `approved`

> Appropriate organisational structures, policies, processes and procedures in place to understand, assess and systematically manage security risks to network and information systems supporting essential functions.

**source_ref**: A
<!-- tl:end -->

## Principle A3 Asset Management

<!-- tl:item UR-0001 -->
**UR-0001 — A3 — Asset Management** — `user_requirement`, status `approved`

> Asset Management

*Rationale:* Everything required to deliver, maintain or support network and information systems necessary for the operation of essential functions is determined and understood. This includes data, people and systems, as well as any supporting infrastructure (such as power or cooling).

**source_ref**: A3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('A3.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0001 | system_requirement | approved | CAF A3.a — Asset Management |
<!-- tl:end -->

# Objective B — Protecting against cyber attack

<!-- tl:item INT-0002 -->
**INT-0002 — Objective B — Protecting against cyber attack** — `intent`, status `approved`

> Proportionate security measures are in place to protect network and information systems supporting essential functions from cyber attack.

**source_ref**: B
<!-- tl:end -->

## Principle B6 Staff Awareness and Training

<!-- tl:item UR-0002 -->
**UR-0002 — B6 — Staff Awareness and Training** — `user_requirement`, status `approved`

> Staff Awareness and Training

*Rationale:* Staff have appropriate awareness, knowledge and skills to carry out their organisational roles effectively in relation to the security of network and information systems supporting the operation of your essential function(s).

**source_ref**: B6
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('B6.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0002 | system_requirement | approved | CAF B6.a — Cyber Security Culture |
| SR-0003 | system_requirement | approved | CAF B6.b — Cyber Security Training |
<!-- tl:end -->

# Objective C — Detecting cyber security events

<!-- tl:item INT-0003 -->
**INT-0003 — Objective C — Detecting cyber security events** — `intent`, status `approved`

> Capabilities exist to ensure security defences remain effective and to detect cyber security events and incidents adversely affecting, or with the potential to adversely affect, essential function(s).

**source_ref**: C
<!-- tl:end -->

## Principle C2 Threat Hunting

<!-- tl:item UR-0003 -->
**UR-0003 — C2 — Threat Hunting** — `user_requirement`, status `approved`

> Threat Hunting

*Rationale:* The organisation proactively seeks to detect, within networks and information systems, adverse activity affecting, or with the potential to affect, the operation of essential functions even when the activity evades standard security prevent / detect solutions (or when standard solutions are not deployable).

**source_ref**: C2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('C2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0004 | system_requirement | approved | CAF C2.a — Threat Hunting |
<!-- tl:end -->

# Objective D — Minimising the impact of cyber security incidents

<!-- tl:item INT-0004 -->
**INT-0004 — Objective D — Minimising the impact of cyber security incidents** — `intent`, status `approved`

> Capabilities exist to minimise the adverse impact of a cyber security incident on the operation of essential functions, including the restoration of those function(s) where necessary.

**source_ref**: D
<!-- tl:end -->

## Principle D2 Lessons Learned

<!-- tl:item UR-0004 -->
**UR-0004 — D2 — Lessons Learned** — `user_requirement`, status `approved`

> Lessons Learned

*Rationale:* When an incident occurs, steps are taken to understand its causes and to ensure remediating action is taken to protect against future incidents.

**source_ref**: D2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('D2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0005 | system_requirement | approved | CAF D2.a — Post Incident Analysis |
| SR-0006 | system_requirement | approved | CAF D2.b — Using Incidents to Drive Improvements |
<!-- tl:end -->

