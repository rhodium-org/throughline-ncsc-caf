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

## Principle A1 Governance

<!-- tl:item UR-0001 -->
**UR-0001 — A1 — Governance** — `user_requirement`, status `approved`

> Governance

*Rationale:* The organisation has appropriate management policies, processes and procedures in place to govern its approach to the security of network and information systems.

*Derives from:* INT-0001

**source_ref**: A1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('A1.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0001 | system_requirement | approved | CAF A1.a — Board Direction |
| SR-0002 | system_requirement | approved | CAF A1.b — Roles and Responsibilities |
| SR-0003 | system_requirement | approved | CAF A1.c — Decision-making |
<!-- tl:end -->

## Principle A2 Risk Management

<!-- tl:item UR-0002 -->
**UR-0002 — A2 — Risk Management** — `user_requirement`, status `approved`

> Risk Management

*Rationale:* The organisation takes appropriate steps to identify, assess and understand security risks to network and information systems supporting the operation of essential functions. This includes an overall organisational approach to risk management.

*Derives from:* INT-0001

**source_ref**: A2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('A2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0004 | system_requirement | approved | CAF A2.a — Risk Management Process |
| SR-0005 | system_requirement | approved | CAF A2.b — Understanding Threat |
| SR-0006 | system_requirement | approved | CAF A2.c — Assurance |
<!-- tl:end -->

## Principle A3 Asset Management

<!-- tl:item UR-0003 -->
**UR-0003 — A3 — Asset Management** — `user_requirement`, status `approved`

> Asset Management

*Rationale:* Everything required to deliver, maintain or support network and information systems necessary for the operation of essential functions is determined and understood. This includes data, people and systems, as well as any supporting infrastructure (such as power or cooling).

*Derives from:* INT-0001

**source_ref**: A3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('A3.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0007 | system_requirement | approved | CAF A3.a — Asset Management |
<!-- tl:end -->

## Principle A4 Supply Chain

<!-- tl:item UR-0004 -->
**UR-0004 — A4 — Supply Chain** — `user_requirement`, status `approved`

> Supply Chain

*Rationale:* The organisation understands and manages security risks to network and information systems supporting the operation of essential functions that arise as a result of dependencies on suppliers. This includes ensuring that appropriate measures are employed where third party services are used.

*Derives from:* INT-0001

**source_ref**: A4
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('A4.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0008 | system_requirement | approved | CAF A4.a — Supply Chain |
| SR-0009 | system_requirement | approved | CAF A4.b — Secure Software Development and Support |
<!-- tl:end -->

# Objective B — Protecting against cyber attack

<!-- tl:item INT-0002 -->
**INT-0002 — Objective B — Protecting against cyber attack** — `intent`, status `approved`

> Proportionate security measures are in place to protect network and information systems supporting essential functions from cyber attack.

**source_ref**: B
<!-- tl:end -->

## Principle B1 Service Protection Policies, Processes and Procedures

<!-- tl:item UR-0005 -->
**UR-0005 — B1 — Service Protection Policies, Processes and Procedures** — `user_requirement`, status `approved`

> Service Protection Policies, Processes and Procedures

*Rationale:* The organisation defines, implements, communicates and enforces appropriate policies, processes and procedures that direct its overall approach to securing systems and data that support operation of essential functions.

*Derives from:* INT-0002

**source_ref**: B1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('B1.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0010 | system_requirement | approved | CAF B1.a — Policy, Process and Procedure Development |
| SR-0011 | system_requirement | approved | CAF B1.b — Policy, Process and Procedure Implementation |
<!-- tl:end -->

## Principle B2 Identity and Access Control

<!-- tl:item UR-0006 -->
**UR-0006 — B2 — Identity and Access Control** — `user_requirement`, status `approved`

> Identity and Access Control

*Rationale:* The organisation understands, documents and manages access to network and information systems supporting the operation of essential functions. Users (or automated functions) that can access data or systems are appropriately verified, authenticated and authorised.

*Derives from:* INT-0002

**source_ref**: B2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('B2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0012 | system_requirement | approved | CAF B2.a — Identity Verification, Authentication and Authorisation |
| SR-0013 | system_requirement | approved | CAF B2.b — Device Management |
| SR-0014 | system_requirement | approved | CAF B2.c — Privileged User Management |
| SR-0015 | system_requirement | approved | CAF B2.d — Identity and Access Management (IdAM) |
<!-- tl:end -->

## Principle B3 Data Security

<!-- tl:item UR-0007 -->
**UR-0007 — B3 — Data Security** — `user_requirement`, status `approved`

> Data Security

*Rationale:* Data stored or transmitted electronically is protected from actions such as unauthorised access, modification, or deletion that may cause an adverse impact on essential functions. Such protection extends to the means by which authorised users, devices and systems access critical data necessary for the operation of essential functions. It also covers information that would assist a threat actor, such as design details of network and information systems.

*Derives from:* INT-0002

**source_ref**: B3
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('B3.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0016 | system_requirement | approved | CAF B3.a — Understanding Data |
| SR-0017 | system_requirement | approved | CAF B3.b — Data in Transit |
| SR-0018 | system_requirement | approved | CAF B3.c — Stored Data |
| SR-0019 | system_requirement | approved | CAF B3.d — Mobile Data |
| SR-0020 | system_requirement | approved | CAF B3.e — Media / Equipment Sanitisation |
<!-- tl:end -->

## Principle B4 System Security

<!-- tl:item UR-0008 -->
**UR-0008 — B4 — System Security** — `user_requirement`, status `approved`

> System Security

*Rationale:* Network and information systems and technology critical for the operation of essential functions are protected from cyber attack. An organisational understanding of risk to essential functions informs the use of robust and reliable protective security measures to effectively limit opportunities for threat actors to compromise networks and systems.

*Derives from:* INT-0002

**source_ref**: B4
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('B4.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0021 | system_requirement | approved | CAF B4.a — Secure by Design |
| SR-0022 | system_requirement | approved | CAF B4.b — Secure Configuration |
| SR-0023 | system_requirement | approved | CAF B4.c — Secure Management |
| SR-0024 | system_requirement | approved | CAF B4.d — Vulnerability Management |
<!-- tl:end -->

## Principle B5 Resilient Networks and Systems

<!-- tl:item UR-0009 -->
**UR-0009 — B5 — Resilient Networks and Systems** — `user_requirement`, status `approved`

> Resilient Networks and Systems

*Rationale:* The organisation builds resilience against cyber attack and system failure into the design, implementation, operation and management of systems that support the operation of your essential function(s).

*Derives from:* INT-0002

**source_ref**: B5
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('B5.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0025 | system_requirement | approved | CAF B5.a — Resilience Preparation |
| SR-0026 | system_requirement | approved | CAF B5.b — Design for Resilience |
| SR-0027 | system_requirement | approved | CAF B5.c — Backups |
<!-- tl:end -->

## Principle B6 Staff Awareness and Training

<!-- tl:item UR-0010 -->
**UR-0010 — B6 — Staff Awareness and Training** — `user_requirement`, status `approved`

> Staff Awareness and Training

*Rationale:* Staff have appropriate awareness, knowledge and skills to carry out their organisational roles effectively in relation to the security of network and information systems supporting the operation of your essential function(s).

*Derives from:* INT-0002

**source_ref**: B6
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('B6.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0028 | system_requirement | approved | CAF B6.a — Cyber Security Culture |
| SR-0029 | system_requirement | approved | CAF B6.b — Cyber Security Training |
<!-- tl:end -->

# Objective C — Detecting cyber security events

<!-- tl:item INT-0003 -->
**INT-0003 — Objective C — Detecting cyber security events** — `intent`, status `approved`

> Capabilities exist to ensure security defences remain effective and to detect cyber security events and incidents adversely affecting, or with the potential to adversely affect, essential function(s).

**source_ref**: C
<!-- tl:end -->

## Principle C1 Security Monitoring

<!-- tl:item UR-0011 -->
**UR-0011 — C1 — Security Monitoring** — `user_requirement`, status `approved`

> Security Monitoring

*Rationale:* The organisation monitors the security status of network and information systems supporting the operation of essential function(s) in order to detect security events indicative of a security incident.

*Derives from:* INT-0003

**source_ref**: C1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('C1.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0030 | system_requirement | approved | CAF C1.a — Sources and Tools for Logging and Monitoring |
| SR-0031 | system_requirement | approved | CAF C1.b — Securing Logs |
| SR-0032 | system_requirement | approved | CAF C1.c — Generating Alerts |
| SR-0033 | system_requirement | approved | CAF C1.d — Triage of Security Alerts |
| SR-0034 | system_requirement | approved | CAF C1.e — Personnel Skills for Monitoring and Detection |
| SR-0035 | system_requirement | approved | CAF C1.f — Understanding User's and System's Behaviour, and Threat Intelligence |
<!-- tl:end -->

## Principle C2 Threat Hunting

<!-- tl:item UR-0012 -->
**UR-0012 — C2 — Threat Hunting** — `user_requirement`, status `approved`

> Threat Hunting

*Rationale:* The organisation proactively seeks to detect, within networks and information systems, adverse activity affecting, or with the potential to affect, the operation of essential functions even when the activity evades standard security prevent / detect solutions (or when standard solutions are not deployable).

*Derives from:* INT-0003

**source_ref**: C2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('C2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0036 | system_requirement | approved | CAF C2.a — Threat Hunting |
<!-- tl:end -->

# Objective D — Minimising the impact of cyber security incidents

<!-- tl:item INT-0004 -->
**INT-0004 — Objective D — Minimising the impact of cyber security incidents** — `intent`, status `approved`

> Capabilities exist to minimise the adverse impact of a cyber security incident on the operation of essential functions, including the restoration of those function(s) where necessary.

**source_ref**: D
<!-- tl:end -->

## Principle D1 Response and Recovery Planning

<!-- tl:item UR-0013 -->
**UR-0013 — D1 — Response and Recovery Planning** — `user_requirement`, status `approved`

> Response and Recovery Planning

*Rationale:* There are well-defined and tested incident management processes in place, that aim to ensure continuity of essential function(s) in the event of system or service failure. Mitigation activities designed to contain or limit the impact of compromise are also in place.

*Derives from:* INT-0004

**source_ref**: D1
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('D1.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0037 | system_requirement | approved | CAF D1.a — Response Plan |
| SR-0038 | system_requirement | approved | CAF D1.b — Response and Recovery Capability |
| SR-0039 | system_requirement | approved | CAF D1.c — Testing and Exercising |
<!-- tl:end -->

## Principle D2 Lessons Learned

<!-- tl:item UR-0014 -->
**UR-0014 — D2 — Lessons Learned** — `user_requirement`, status `approved`

> Lessons Learned

*Rationale:* When an incident occurs, steps are taken to understand its causes and to ensure remediating action is taken to protect against future incidents.

*Derives from:* INT-0004

**source_ref**: D2
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('source_ref').startswith('D2.') -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0040 | system_requirement | approved | CAF D2.a — Post Incident Analysis |
| SR-0041 | system_requirement | approved | CAF D2.b — Using Incidents to Drive Improvements |
<!-- tl:end -->

