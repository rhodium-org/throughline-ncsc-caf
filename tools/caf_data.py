"""Hand-transcribed CAF v4.0 content for the throughline source.

Source of truth: ``tools/caf-4.0/NCSC-Cyber-Assessment-Framework-4.0.pdf`` (© Crown
copyright, Open Government Licence v3.0). ``tools/generate.py`` turns these records into
throughline items with permanent UIDs.

**This file currently holds the VERTICAL SLICE only** — the four Objective roots plus one
representative Principle per Objective (A3, B6, C2, D2) and their six Contributing
Outcomes, each with its full Indicators of Good Practice (IGP) table. It is the shape the
operator reviews before the full 14-principle / 41-outcome catalogue is transcribed.

Modelling notes surfaced by the slice:
  * Some Contributing Outcomes publish an italicised outcome *statement* under the handle
    (B6.a, B6.b, D2.a, D2.b); others jump straight to the IGP table with no statement of
    their own (A3.a, C2.a) — for those, ``statement`` is None and the generator falls back
    to the outcome title for the item ``text``.
  * IGP columns vary: some outcomes are two-column (Not Achieved / Achieved), others carry
    a middle Partially Achieved column. ``partially_achieved`` is [] when absent.
"""

# Four Objectives -> four root intents. `text` is the Objective's own description.
OBJECTIVES = [
    {
        "id": "A",
        "title": "Managing security risk",
        "text": (
            "Appropriate organisational structures, policies, processes and procedures in "
            "place to understand, assess and systematically manage security risks to "
            "network and information systems supporting essential functions."
        ),
    },
    {
        "id": "B",
        "title": "Protecting against cyber attack",
        "text": (
            "Proportionate security measures are in place to protect network and "
            "information systems supporting essential functions from cyber attack."
        ),
    },
    {
        "id": "C",
        "title": "Detecting cyber security events",
        "text": (
            "Capabilities exist to ensure security defences remain effective and to detect "
            "cyber security events and incidents adversely affecting, or with the potential "
            "to adversely affect, essential function(s)."
        ),
    },
    {
        "id": "D",
        "title": "Minimising the impact of cyber security incidents",
        "text": (
            "Capabilities exist to minimise the adverse impact of a cyber security incident "
            "on the operation of essential functions, including the restoration of those "
            "function(s) where necessary."
        ),
    },
]

# Principles -> user_requirements. `statement` is the principle's published narrative,
# carried as the UR `rationale`.
PRINCIPLES = [
    {
        "id": "A3",
        "objective": "A",
        "title": "Asset Management",
        "statement": (
            "Everything required to deliver, maintain or support network and information "
            "systems necessary for the operation of essential functions is determined and "
            "understood. This includes data, people and systems, as well as any supporting "
            "infrastructure (such as power or cooling)."
        ),
    },
    {
        "id": "B6",
        "objective": "B",
        "title": "Staff Awareness and Training",
        "statement": (
            "Staff have appropriate awareness, knowledge and skills to carry out their "
            "organisational roles effectively in relation to the security of network and "
            "information systems supporting the operation of your essential function(s)."
        ),
    },
    {
        "id": "C2",
        "objective": "C",
        "title": "Threat Hunting",
        "statement": (
            "The organisation proactively seeks to detect, within networks and information "
            "systems, adverse activity affecting, or with the potential to affect, the "
            "operation of essential functions even when the activity evades standard "
            "security prevent / detect solutions (or when standard solutions are not "
            "deployable)."
        ),
    },
    {
        "id": "D2",
        "objective": "D",
        "title": "Lessons Learned",
        "statement": (
            "When an incident occurs, steps are taken to understand its causes and to "
            "ensure remediating action is taken to protect against future incidents."
        ),
    },
]

# Contributing Outcomes -> system_requirements. `statement` -> item `text` (falls back to
# `title` when None). IGP lists -> attrs.igp_not_achieved / igp_partially_achieved /
# igp_achieved.
OUTCOMES = [
    {
        "id": "A3.a",
        "principle": "A3",
        "title": "Asset Management",
        "statement": None,
        "not_achieved": [
            "Inventories of assets relevant to network and information systems supporting "
            "your essential function(s) are incomplete, non-existent or inadequately "
            "detailed.",
            "Only certain domains or types of asset are documented and understood. "
            "Dependencies between assets are not understood (such as the dependencies "
            "between IT and OT).",
            "Information assets, which could include personally identifiable information "
            "and / or important / critical data, are stored for long periods of time with "
            "no clear business need or retention policy.",
            "Knowledge critical to the management, operation, or recovery of network and "
            "information systems supporting your essential function(s) is held by one or "
            "two key individuals with no succession plan.",
            "Asset inventories are neglected and out of date.",
        ],
        "partially_achieved": [],
        "achieved": [
            "All assets relevant to the secure operation of network and information systems "
            "supporting your essential function(s) are identified and inventoried (at a "
            "suitable level of detail). The inventory is kept up-to-date.",
            "Dependencies on supporting infrastructure (e.g. power, cooling etc) are "
            "recognised and recorded.",
            "You have prioritised your assets according to their importance to the "
            "operation of network and information systems supporting your essential "
            "function(s).",
            "You have assigned responsibility for managing all assets, including physical "
            "assets, relevant to the operation of network and information systems "
            "supporting your essential function(s).",
            "Assets relevant to network and information systems supporting your essential "
            "function(s) are managed with cyber security in mind throughout their "
            "lifecycle, from creation through to eventual decommissioning or disposal.",
        ],
    },
    {
        "id": "B6.a",
        "principle": "B6",
        "title": "Cyber Security Culture",
        "statement": (
            "You develop and maintain a positive cyber security culture and a shared sense "
            "of responsibility."
        ),
        "not_achieved": [
            "People in your organisation do not understand what they contribute to the "
            "cyber security of network and information systems supporting your essential "
            "function(s).",
            "People in your organisation do not know how to raise a concern about cyber "
            "security.",
            "People believe that reporting issues may get them into trouble.",
            "Your organisation's approach to cyber security is perceived by staff as "
            "hindering the business of the organisation and may encourage poor security "
            "behaviours.",
            "Formal or informal incentives and rewards conflict with the promotion of "
            "positive security outcomes.",
        ],
        "partially_achieved": [
            "Your executive management understand and widely communicate the importance of "
            "a positive cyber security culture. Positive attitudes, behaviours and "
            "expectations are described for your organisation.",
            "All people in your organisation understand the contribution they make to the "
            "cyber security of network and information systems supporting your essential "
            "functions(s).",
            "All individuals in your organisation know who to contact and where to access "
            "more information about cyber security. They know how to raise a cyber security "
            "issue.",
            "You identify and address issues that inhibit people from behaving in a manner "
            "that supports your intended cyber security outcomes.",
        ],
        "achieved": [
            "Your executive management clearly and effectively communicates the "
            "organisation's cyber security priorities and objectives to all staff. Your "
            "organisation displays positive cyber security attitudes, behaviours, "
            "expectations.",
            "People in your organisation raising potential cyber security incidents and "
            "issues are treated positively.",
            "Individuals at all levels in your organisation routinely report concerns or "
            "issues about cyber security and are recognised for their contribution to "
            "keeping the organisation secure.",
            "Your management is seen to be committed to and actively involved in cyber "
            "security.",
            "Your organisation communicates openly about cyber security, with any concern "
            "being taken seriously.",
            "People across your organisation collaborate in cyber security activities and "
            "improvements, building joint ownership and bringing knowledge of their area of "
            "expertise.",
        ],
    },
    {
        "id": "B6.b",
        "principle": "B6",
        "title": "Cyber Security Training",
        "statement": (
            "The people who support the operation of network and information systems "
            "supporting your essential function(s) are appropriately trained in cyber "
            "security."
        ),
        "not_achieved": [
            "There are teams who operate and support your essential function(s) that lack "
            "any cyber security training.",
            "Cyber security training is restricted to specific roles in your organisation.",
            "Cyber security training records for your organisation are lacking or "
            "incomplete.",
            "Training is used as a \"silver bullet\" for all user security behaviours.",
            "The success of training is only measured by the number of people reached, "
            "rather than assessing whether it has a positive impact on security "
            "behaviours.",
            "Training materials contain out of date or contradictory information, or "
            "information that conflicts with other policies, processes or procedures.",
        ],
        "partially_achieved": [
            "You have defined appropriate cyber security training and awareness activities "
            "for all roles in your organisation, from executives to the most junior roles.",
            "You use a range of teaching and communication techniques for cyber security "
            "training and awareness to reach the widest audience effectively.",
            "Cyber security information is easily available.",
        ],
        "achieved": [
            "All people in your organisation, from the most senior to the most junior, "
            "follow appropriate cyber security training paths.",
            "Each individuals cyber security training is tracked and refreshed at suitable "
            "intervals.",
            "You routinely evaluate your cyber security training and awareness activities "
            "to ensure they reach the widest audience and are effective.",
            "You make cyber security information and good practice guidance easily "
            "accessible, widely available and you know it is referenced and used within "
            "your organisation.",
        ],
    },
    {
        "id": "C2.a",
        "principle": "C2",
        "title": "Threat Hunting",
        "statement": None,
        "not_achieved": [
            "You do not know the resources required for threat hunting.",
            "You do not have access to an effective threat hunting capability.",
            "Your threat hunts do not follow any structure and few if any records are "
            "created.",
        ],
        "partially_achieved": [
            "You have identified the resources required to perform threat hunting and are "
            "able to deploy these, in a timely manner, on an occasional basis.",
            "You deploy an effective threat hunting capability but not frequent enough to "
            "match the risks posed to network and information systems supporting your "
            "essential function(s) (e.g. you perform threat hunts in response to a tip off "
            "from a reputable source).",
            "Your threat hunts follow pre-determined and documented methods (e.g. "
            "hypothesis driven, data driven, entity driven) designed to identify adverse "
            "activity not detected by automated detections.",
            "You document details of threat hunts and post hunt analysis.",
        ],
        "achieved": [
            "You understand the resources required to perform threat hunting and these are "
            "deployed as part of business as usual.",
            "You deploy threat hunting resources at a frequency that matches the risks "
            "posed to network and information systems supporting your essential "
            "function(s).",
            "Your threat hunts follow pre-determined and documented methods (e.g. "
            "hypothesis driven, data driven, entity driven) designed to identify adverse "
            "activity not detected by automated detections.",
            "You turn threat hunts into automated detections and alerting where "
            "appropriate.",
            "You routinely record details of previous threat hunts and post hunt "
            "activities. You use these to drive improvements in your threat hunting and "
            "security posture.",
            "You have justified confidence in the effectiveness of your threat hunts and "
            "the threat hunting process is reviewed and updated to match the risks posed to "
            "network and information systems supporting your essential function(s).",
            "You leverage automation to improve threat hunts where appropriate (e.g. some "
            "stages of the threat hunting process are automated).",
            "Your threat hunts focus on the tactics, techniques and procedures (TTPs) of "
            "threats over atomic IoCs (e.g. hashes, IP addresses, domain names etc).",
        ],
    },
    {
        "id": "D2.a",
        "principle": "D2",
        "title": "Post Incident Analysis",
        "statement": (
            "When an incident occurs, your organisation takes steps to understand its "
            "causes, informing appropriate remediating action."
        ),
        "not_achieved": [
            "You are not usually able to resolve incidents to a root cause or identify the "
            "contributing factors within a broader systems context.",
            "You do not have a formal process for investigating causes.",
            "Investigators form theories early in the process and only seek evidence that "
            "affirms their belief.",
            "Investigations are solely focused on identifying the person(s) who can be held "
            "responsible for the incident.",
        ],
        "partially_achieved": [],
        "achieved": [
            "Post incident analysis is conducted routinely as a key part of your lessons "
            "learned activities following an incident.",
            "Your post incident analysis is comprehensive, considering organisational "
            "factors (e.g. policies, processes and procedures), technical factors (e.g. "
            "system design, vulnerabilities), human factors (e.g. training, security "
            "culture) and any changes to threat.",
            "All relevant incident data is made available to the analysis team to perform "
            "post incident analysis.",
            "Your analysis considers what could have happened under plausible, alternative "
            "circumstances (e.g. 'what if' / 'if only' scenarios).",
        ],
    },
    {
        "id": "D2.b",
        "principle": "D2",
        "title": "Using Incidents to Drive Improvements",
        "statement": (
            "Your organisation uses lessons learned from incidents to improve your security "
            "measures."
        ),
        "not_achieved": [
            "Following incidents, lessons learned are not captured or are limited in "
            "scope.",
            "Improvements arising from lessons learned following an incident are not "
            "implemented or not given sufficient organisational priority.",
            "Changes are made as a 'knee jerk' reaction to an incident without proper "
            "analysis and testing to ensure the change is appropriate.",
            "You wait until a severe or high-profile incident has occurred before you take "
            "steps to improve.",
        ],
        "partially_achieved": [],
        "achieved": [
            "You have a documented incident review process / policy which ensures that "
            "lessons learned from each incident, including near misses, are identified, "
            "captured, and acted upon.",
            "Lessons learned cover issues with reporting, roles, governance, skills and "
            "organisational policies, processes and procedures as well as technical aspects "
            "of network and information systems.",
            "You use lessons learned to improve security measures, including updating and "
            "retesting response plans when necessary.",
            "Security improvements identified as a result of lessons learned are "
            "prioritised, with the highest priority improvements completed promptly.",
            "Analysis is fed to senior management and incorporated into risk management and "
            "continuous improvement.",
            "Your organisation maximises the lessons learned by using the analysis into "
            "'what if' / 'if only' scenarios.",
            "Your organisation learns from reported incidents in your sector and the wider "
            "national infrastructure.",
        ],
    },
]
