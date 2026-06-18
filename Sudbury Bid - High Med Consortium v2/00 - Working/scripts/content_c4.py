# -*- coding: utf-8 -*-
"""Criterion 4 - Improving Access, Reducing Health Inequalities and Facilitating Choice.

Q4.1 Equity of Access (4%, <= 800 words)
Q4.2 Patient Engagement / PPG - Improving Outcomes (4%, <= 1000 words)
Q4.3 Lessons Learnt (4%, <= 800 words)
Q4.4 Population Health Management (9%, <= 1500 words, PHM Proposal attachment)

Case studies (Q4.1a) and the PHM illustrative example (Q4.4a) are 2-page
attachments held in content_attach.py.

v2 closes the Isleworth gaps on equity methodology, co-production framework,
carer identification, before/after lessons learnt, PHM dataset access route,
workflow and capacity modelling, and cohort-specific time-bound KPIs.
"""

# ---------------------------------------------------------------------------
# Q4.1 - Patient Journey: Equity of Access (4%, <= 800 words)
# ---------------------------------------------------------------------------
Q4_1 = [
    ("p", "Sudbury Surgery serves a Wembley population in Brent - the 4th most deprived London "
          "borough - where around 64% of residents are from BAME communities and roughly one in "
          "three do not use English as a main language. Our approach to equitable access is "
          "designed, delivered, monitored and improved by named leads (Dr Muhammad Adem for data; "
          "Ms Manjot Kaur for operations) and is built to reduce, not reproduce, inequality."),

    ("h", "Understanding population need"),
    ("p", "We use publicly available data to target action: the Brent Joint Strategic Needs "
          "Assessment, the Index of Multiple Deprivation, OHID/Fingertips local health profiles "
          "and our own dashboard stratified by ethnicity, age and deprivation. These confirm "
          "priority groups and conditions - high diabetes prevalence (8.58% vs 7.26% England), "
          "CVD, severe mental illness (1.15% vs London 0.95%), and access barriers for "
          "non-English-speaking, digitally excluded and disabled patients - which we map to "
          "specific access measures."),

    ("h", "Patient and community engagement"),
    ("p", "We engage patients, carers and seldom-heard groups through the PPG, multilingual "
          "feedback, and partnership with Brent Health Matters (around 35 community events a "
          "month) and local faith and community organisations, so service design is informed by "
          "lived experience rather than assumption."),

    ("h", "Operational delivery model"),
    ("p", "Practical, owned measures improve access:"),
    ("b", [
        "Interpretation and translation: professional telephone and face-to-face interpreters, "
        "translated materials, and recorded language preference under the Accessible Information "
        "Standard.",
        "Digital inclusion: a weekly reception-supported NHS App clinic, assisted online "
        "consultation, and a protected non-digital route (phone, walk-in) so no patient is excluded.",
        "Outreach and targeted engagement: proactive recall and community clinics for underserved "
        "groups, including housebound and care-home patients.",
        "Reasonable adjustments: longer appointments, accessible formats, step-free access and "
        "carer involvement, recorded and honoured.",
    ]),

    ("h", "Monitoring, evaluation and continuous improvement"),
    ("p", "We monitor equity of access through metrics stratified by protected characteristic and "
          "deprivation - appointment access, DNA rates, screening, immunisation and review uptake "
          "and patient experience - reviewed monthly with a named action for each gap and reported "
          "to the PPG. Insights drive continuous improvement across the contract."),

    ("h", "How the methodology works in practice"),
    ("p", "Our equity methodology is a continuous, owned cycle rather than a one-off exercise. Step "
          "one, Dr Adem builds and maintains a needs profile combining the JSNA, IMD and Fingertips "
          "with the practice's own coded data, identifying where access and outcome gaps fall by "
          "ward, ethnicity, age, disability and language. Step two, Ms Kaur translates each "
          "identified gap into a specific operational change with an owner and timescale. Step "
          "three, we engage the affected group directly - through the PPG, community partners and "
          "translated outreach - to co-design the change so it fits lived experience. Step four, we "
          "measure the effect on the stratified metrics and iterate. This explicit, "
          "data-to-action-to-evaluation methodology directly answers the debrief learning that "
          "equity approaches must be practical and measurable, not aspirational."),
    ("h", "Translating measures into projected Sudbury improvement"),
    ("p", "Each measure is tied to an intended local outcome. For example, professional "
          "interpretation and translated recall are expected to raise screening and review uptake "
          "among non-English-speaking patients; the assisted-digital clinic is expected to raise "
          "NHS App registration and online access in older and digitally excluded patients while "
          "protecting the phone route; and outreach with Brent Health Matters is expected to lift "
          "immunisation and case-finding in the most deprived wards. We track each link from "
          "intervention to outcome on the dashboard, so prior experience is translated into "
          "projected, monitored Sudbury improvement rather than presented as a generic claim."),
    ("h", "Equity of access KPI trajectory"),
    ("t", [
        ["Measure", "Baseline (Day-1 audit)", "6 months", "12 months", "18 months"],
        ["Access gap (most vs least deprived)", "Establish", "Narrowing", "Narrowed", "Minimised"],
        ["Interpreter use vs identified need", "Establish", ">=90%", ">=95%", ">=95%"],
        ["Digitally assisted patients supported", "n/a", "Live", "Growing", "Sustained"],
        ["Reasonable adjustments recorded/honoured", "Establish", ">=95%", "100%", "100%"],
    ]),

    ("h", "Added value"),
    ("p", "Beyond specification we will publish an annual equity-of-access report to the PPG and "
          "ICB, evidencing measurable reductions in access inequality for Sudbury's priority "
          "groups."),
]

# ---------------------------------------------------------------------------
# Q4.2 - Patient Engagement: Improving Outcomes / PPG (4%, <= 1000 words)
# ---------------------------------------------------------------------------
Q4_2 = [
    ("p", "We will establish, support and actively engage a representative Patient Participation "
          "Group (PPG) so patient views genuinely shape service delivery and continuous "
          "improvement at Sudbury Surgery. Ms Manjot Kaur is the named PPG lead, with clinical "
          "input from Dr Gursharan Singh. Reflecting debrief learning, our model embeds patients "
          "in redesign - co-production - rather than simply collecting and analysing feedback."),

    ("h", "Establishing and engaging a PPG"),
    ("p", "Where a PPG is in place we will strengthen it; where not, we will establish one within "
          "the first three months, with a published terms of reference, quarterly meetings (in "
          "person and virtual), and a linked virtual PPG for those who cannot attend. Meetings have "
          "a standing agenda, patient-set items, and feedback on actions, so members influence "
          "decisions rather than receive updates."),

    ("h", "Gathering and using patient feedback"),
    ("p", "We collect feedback through PPG meetings, the Friends and Family Test, the GP Patient "
          "Survey, real-time and translated surveys, complaints and compliments, and digital "
          "tools. Feedback is collated monthly, analysed for theme and prioritised against clinical "
          "risk and reach by Ms Kaur, then tabled at the Delivery Board where decisions on changes "
          "are made and owned."),

    ("h", "Communication and feedback loops"),
    ("p", "We close the loop visibly through a 'You Said, We Did' board (physical and online), "
          "newsletters, the website and SMS, in plain English and community languages, so patients "
          "see that their views led to specific changes. Illustrative example (proposed model): if "
          "patients report difficulty getting through by phone in the morning, we adjust "
          "appointment release and promote online and call-back options, then report the improved "
          "wait times back to patients."),

    ("h", "Driving service improvement"),
    ("p", "Insights are translated into tangible change through clear governance: the Delivery "
          "Board agrees the change, assigns an owner and timescale, implements via a PDSA cycle, "
          "and reviews impact. Examples of change types include clinic timing, recall wording, "
          "accessible communications, and environment improvements from PPG walk-rounds."),

    ("h", "Inclusivity and representation"),
    ("p", "We will actively build a PPG representative of Sudbury's population - by ethnicity, age, "
          "disability, language and carer status - through targeted recruitment via community and "
          "faith partners and Brent Health Matters, translated invitations, and flexible "
          "participation. Carers are systematically identified, added to the carers register and "
          "engaged as a distinct voice, addressing the prior gap on carer identification."),

    ("h", "Monitoring and continuous improvement"),
    ("p", "We evaluate engagement effectiveness through PPG diversity against practice demographics, "
          "number and impact of changes made, FFT and survey trends, and an annual review of the "
          "engagement approach, using learning to improve reach and influence over time."),

    ("h", "Co-production in practice - embedding patients in redesign"),
    ("p", "Addressing the specific learning that patient voice must move from being heard to "
          "shaping change, we operate a co-production framework with defined touchpoints: patients "
          "sit on the practice improvement forum alongside clinicians and managers; service changes "
          "above a defined threshold require PPG input at design stage, not just consultation after "
          "the fact; and PPG members participate in walk-rounds, communication reviews and recall "
          "redesign. We use accessible methods - facilitated workshops, translated materials, "
          "telephone input for those who cannot attend - so co-production is genuinely inclusive. "
          "This ensures patients influence what changes and how, which is what distinguishes an "
          "excellent engagement model from a compliant one."),
    ("h", "Engaging carers and seldom-heard groups"),
    ("p", "Carers are identified at registration, at every relevant contact and through proactive "
          "case-finding, added to the carers register, offered health checks and vaccination, and "
          "engaged as a distinct voice in the PPG. Seldom-heard groups - non-English-speaking "
          "residents, people with serious mental illness, those experiencing homelessness or "
          "domestic abuse, and disabled patients - are reached through trusted community and faith "
          "partners and Brent Health Matters, so the PPG and feedback reflect the whole population. "
          "Local baselines for engagement (PPG diversity, carer numbers, survey reach) are "
          "established at the Day-1 audit so improvement is measured from evidence."),
    ("h", "Governance for decision-making and implementation"),
    ("p", "Decisions on service change follow clear governance: the PPG and improvement forum "
          "propose and shape changes; the Delivery Board agrees, resources and assigns them; and "
          "implementation runs through a PDSA cycle with impact reviewed and reported back. This "
          "gives patients confidence that engagement leads to action, and gives the Relevant "
          "Authority assurance that feedback is converted into governed, accountable improvement "
          "rather than goodwill."),
    ("h", "Patient engagement KPI trajectory"),
    ("t", [
        ["Measure", "Baseline", "6 months", "12 months", "18 months"],
        ["PPG established and meeting quarterly", "Confirm/establish", "Live", "Embedded", "Mature"],
        ["PPG representativeness vs demographics", "Establish", "Improving", "Representative", "Sustained"],
        ["'You Said, We Did' changes delivered", "n/a", ">=3", ">=6", "Ongoing"],
        ["Carers identified and on register", "Establish", "+ on baseline", "Growing", "Sustained"],
        ["FFT positive experience", "Establish", "+ on baseline", "Above median", "Sustained"],
    ]),

    ("h", "Added value"),
    ("p", "Beyond specification we will recruit two PPG patient representatives from seldom-heard "
          "groups onto our practice improvement forum, giving patients a direct, ongoing role in "
          "co-producing service change."),
]

# ---------------------------------------------------------------------------
# Q4.3 - Patient Journey: Lessons Learnt (4%, <= 800 words)
# ---------------------------------------------------------------------------
Q4_3 = [
    ("p", "We will embed a culture of continuous learning and improvement at Sudbury Surgery, "
          "systematically learning from patient feedback, complaints, safety incidents (including "
          "diagnostic errors) and stakeholder input to strengthen clinical governance, patient "
          "safety and communication. Dr Gursharan Singh leads clinical learning; Ms Manjot Kaur "
          "leads complaints and feedback."),

    ("h", "Gathering insights"),
    ("p", "We capture insight from the Friends and Family Test, surveys, complaints and "
          "compliments, PPG input, significant events, LFPSE reports and staff and stakeholder "
          "feedback, logged centrally so nothing is lost."),

    ("h", "Analysis and learning processes"),
    ("p", "Information is analysed through monthly thematic and trend review and, for incidents, "
          "structured root-cause/contributory-factor analysis. Themes are prioritised by risk and "
          "translated into specific, owned actions on the continuous-improvement log."),

    ("h", "Complaints and concerns management"),
    ("p", "Complaints are managed to NHS Complaint Regulations timescales: acknowledged within "
          "three working days, investigated proportionately, responded to with apology and "
          "explanation, and used for learning. Patients are told what changed as a result, and "
          "themes are reported to the PPG."),

    ("h", "Incident management and patient safety, including diagnostic error"),
    ("p", "Patient-safety incidents, including diagnostic errors and missed/delayed follow-up, are "
          "reported on LFPSE, investigated under a Patient Safety Incident Response Framework "
          "approach, and addressed with corrective and preventative actions (e.g. failsafe and "
          "safety-netting improvements). Duty of candour is applied."),

    ("h", "Embedding learning and a before/after example"),
    ("p", "Learning updates policies, SOPs, clinical pathways, templates and training. Before/after "
          "example (proposed model): a significant event of a delayed abnormal-result action leads "
          "to a redesigned results failsafe with named daily ownership and a four-hour escalation "
          "rule; re-audit then evidences improved timely action - demonstrating measurable, "
          "before-and-after improvement rather than activity alone."),

    ("h", "Stakeholder engagement"),
    ("p", "We engage patients, carers, staff and system partners (PCN, community services, "
          "secondary care) in identifying and acting on learning, with transparency through the "
          "PPG and team meetings."),

    ("h", "Monitoring and continuous improvement"),
    ("p", "We monitor whether changes worked through re-audit, trend tracking and governance "
          "oversight, running continuous PDSA cycles so improvement is sustained, not one-off."),

    ("h", "Systematic learning and sustained patient involvement"),
    ("p", "Our learning system is structured and owned. A monthly quality and learning meeting "
          "reviews complaints, FFT, significant events, LFPSE reports, audits and stakeholder "
          "feedback together, so trends across sources are seen, not missed. Each theme is "
          "prioritised by risk and reach, assigned to a named owner with a timescale, and tracked "
          "to completion with re-audit. Crucially - and addressing the debrief learning that "
          "patient involvement in redesign must be sustained - patients and the PPG are involved "
          "throughout: they help interpret feedback, co-design solutions, and review whether "
          "changes worked from a patient perspective. Seldom-heard groups are reached through "
          "translated channels and community partners so learning reflects the whole population."),
    ("h", "Strengthening governance, safety and communication"),
    ("p", "Learning feeds directly into clinical governance and patient safety: significant-event "
          "and diagnostic-error learning updates failsafe and safety-netting processes; complaints "
          "learning improves communication, access and the patient journey; and recurring themes "
          "trigger SOP, template and training changes. Communication is strengthened through "
          "accessible, multilingual 'You Said, We Did' feedback and duty-of-candour conversations "
          "that are honest and timely. This makes the learning culture visible to patients and "
          "staff and demonstrably linked to safer, better care."),
    ("h", "Embedding learning into policies, training and pathways"),
    ("p", "Learning is only valuable when it changes practice. Each agreed action is written back "
          "into the relevant policy, SOP, clinical-system template or training plan, with the "
          "change communicated at team meetings and induction so it sticks. We maintain a learning "
          "log that links every theme to the specific document or process changed and the staff "
          "group responsible, and we re-audit to confirm the change held. This closed loop - "
          "capture, analyse, act, embed, re-measure - is what turns isolated incidents and "
          "complaints into durable improvement in clinical governance, patient safety and "
          "communication."),
    ("h", "Lessons-learnt KPI trajectory"),
    ("t", [
        ["Measure", "Baseline", "6 months", "12 months", "18 months"],
        ["Complaints responded within timescale", "Establish", ">=95%", "100%", "100%"],
        ["Incidents with completed learning + re-audit", "Establish", "100%", "100%", "100%"],
        ["Changes evidenced by before/after data", "n/a", ">=2", ">=4", "Ongoing"],
    ]),

    ("h", "Added value"),
    ("p", "Beyond specification we will publish an annual 'learning and improvement' summary to "
          "patients and the PCN, evidencing measurable before-and-after outcomes from our learning "
          "culture."),
]

# ---------------------------------------------------------------------------
# Q4.4 - Population Health Management (9%, <= 1500 words, PHM Proposal attachment)
# ---------------------------------------------------------------------------
Q4_4 = [
    ("p", "Our population health management (PHM) approach identifies high-risk cohorts, targets "
          "interventions and improves outcomes for Sudbury's high-need population, using data, "
          "intelligence and partnership working to deliver proactive care, reduce inequality and "
          "address unwarranted variation. Dr Muhammad Adem owns the PHM dashboard; Dr Gursharan "
          "Singh leads clinical delivery. A two-page PHM Proposal is attached."),

    ("h", "Identification of population need and risk stratification - data and access route"),
    ("p", "We will use a defined, named data stack: the practice clinical system (EMIS/SystmOne) "
          "for clinical and demographic data; the North West London Whole Systems Integrated Care "
          "(WSIC) dashboards and the Discover/linked datasets accessed via our ICB and PCN "
          "data-sharing agreements; the Brent JSNA and OHID Fingertips for population context; and "
          "deprivation (IMD) and ethnicity coding. Risk stratification combines validated tools - "
          "the electronic Frailty Index, QRISK, QDiabetes and segmentation models - to identify "
          "high-risk and rising-risk cohorts. The access route to linked data is explicit: WSIC "
          "via ICB information-governance approval, with Dr Adem as the accountable data lead, "
          "addressing the prior gap on how data is actually obtained."),

    ("h", "Workflow - from data to intervention"),
    ("p", "The PHM workflow runs monthly and is owned end to end: (1) Dr Adem refreshes "
          "stratification and inequality views; (2) cohorts are prioritised (e.g. uncontrolled "
          "diabetes, undiagnosed hypertension, SMI without physical-health checks); (3) the MDT "
          "agrees interventions and capacity; (4) named clinicians deliver targeted recall, "
          "reviews, SMRs and outreach; (5) outcomes and uptake are measured and fed back. Workflow "
          "diagrams are in the attached PHM Proposal."),

    ("h", "Understanding drivers of inequality"),
    ("p", "We interpret the social, economic, cultural and environmental drivers of poor outcomes "
          "in Sudbury: deprivation, overcrowding, language and digital exclusion, low health "
          "literacy, and the higher diabetes and CVD risk in South Asian and Black communities. "
          "This shapes who we target and how we engage them."),

    ("h", "Culturally informed and inclusive approaches"),
    ("p", "Interventions are culturally sensitive and co-designed: language-matched communication, "
          "trusted community and faith messengers, Brent Health Matters outreach, and "
          "culturally-tailored education (e.g. diet and Ramadan-aware diabetes management). "
          "Inclusion is built into engagement and intervention design, not added afterwards."),

    ("h", "Capacity and workforce modelling"),
    ("p", "We model the clinician time and capacity each PHM programme requires - estimating the "
          "number of patients in a cohort, the review/SMR time per patient, and the GP, nurse, HCA "
          "and ARRS-pharmacist sessions needed - and schedule it into clinics and Enhanced Access "
          "so PHM is resourced rather than aspirational. This capacity modelling addresses the "
          "prior gap on workforce/time feasibility."),

    ("h", "Outcomes, metrics and evaluation - Core20PLUS5 cohort KPIs"),
    ("p", "We define cohort-specific, time-bound outcome measures aligned to Core20PLUS5 and report "
          "them on the dashboard, stratified by ethnicity and deprivation, with named actions for "
          "variation."),
    ("t", [
        ["Cohort / Core20PLUS5 area", "Baseline", "6 months", "12 months", "18 months"],
        ["Diabetes: 8 care processes + HbA1c control", "Establish", "Improving", "At/above Brent median", "Sustained gain"],
        ["Hypertension/CVD: BP to target (incl. case-finding)", "Establish", "+ on baseline", "At target", "Sustained"],
        ["SMI: annual physical health checks", "Establish", ">=75%", ">=90%", ">=90%"],
        ["Cancer: screening uptake + early diagnosis", "Establish", "+5 pts", "+8 pts", "At/above median"],
        ["Respiratory: structured reviews + low-carbon inhalers", "Establish", "Improving", "At target", "Sustained"],
        ["Inequality gap (most vs least deprived)", "Establish", "Narrowing", "Narrowed", "Minimised"],
    ]),

    ("h", "Designing and implementing targeted interventions"),
    ("p", "For each prioritised cohort we design a specific, resourced intervention and implement it "
          "through named clinicians on a defined schedule. For uncontrolled diabetes: dashboard-led "
          "recall, structured reviews completing the eight care processes, pharmacist-led titration "
          "and SMRs, and language-matched group education. For undiagnosed hypertension and CVD "
          "risk: opportunistic and targeted BP case-finding, home BP monitoring, and lipid "
          "optimisation. For SMI: proactive physical-health-check recall co-ordinated with the "
          "mental-health team. For respiratory disease: structured reviews, inhaler technique and "
          "low-carbon switches. Each intervention has an owner, a capacity allocation and a "
          "measurable target, so PHM is delivered as concrete operational activity, not strategy."),
    ("h", "From partnership to measurable impact"),
    ("p", "We make the link from partnership to outcome explicit. Working with Brent Health Matters "
          "and community partners on diabetes and CVD outreach is expected to raise case-finding "
          "and review uptake in the most deprived and South Asian populations; PCN pharmacist "
          "capacity is expected to increase SMR completion and improve medicines safety; and "
          "social-prescribing partnerships are expected to improve self-management and reduce "
          "avoidable contacts. Each partnership carries a measurable indicator on the dashboard, so "
          "we can evidence the impact of collaboration rather than asserting it - directly closing "
          "the debrief gap on partnership-to-outcome evidence."),
    ("h", "Reducing unwarranted variation"),
    ("p", "We monitor variation in access, quality and outcomes across population groups using the "
          "dashboard, and respond with targeted recall, outreach and pathway changes, reviewing "
          "impact monthly so variation is actively reduced rather than just described."),

    ("h", "Partnership working and system integration"),
    ("p", "PHM is delivered with the Brent Central K&W PCN (shared dashboards, SMR and DES "
          "delivery), the ICB, community and mental-health services, the local authority and the "
          "voluntary sector, linking clinical intervention to action on wider determinants - and "
          "we evidence the link from partnership to measurable outcome, not just activity."),

    ("h", "Evaluation, scaling and sustainability"),
    ("p", "Each PHM programme is evaluated against its baseline and cohort target at six, twelve and "
          "eighteen months, with success criteria agreed in advance. Where an intervention works, "
          "we scale it and share the model with the PCN; where it underperforms, we use PDSA "
          "iteration to adjust the approach, the target group or the channel. Sustainability is "
          "built in by embedding successful PHM activity into routine recall and clinic templates "
          "rather than running it as a time-limited project, and by resourcing it through the "
          "workforce capacity model above. This ensures improvements in outcomes and reductions in "
          "inequality are sustained across the contract term and beyond."),
    ("h", "Proactive, anticipatory care delivery"),
    ("p", "PHM shifts care from reactive to anticipatory. Rising-risk patients - those approaching "
          "a threshold or recently destabilised (for example a new abnormal HbA1c or BP, a recent "
          "admission or A&E attendance) - are surfaced by the dashboard for early, proactive "
          "contact before they deteriorate. Personalised care and support plans are created for "
          "the highest-risk cohort and shared via the London Care Record, and continuity is "
          "prioritised so these patients see a consistent clinician. This anticipatory model is "
          "designed to reduce avoidable admissions and unplanned care, particularly for the frail, "
          "multimorbid and SMI cohorts that drive unplanned demand in Brent."),
    ("h", "Data quality, intelligence and information governance"),
    ("p", "Reliable PHM depends on reliable data. We maintain coding standards and run regular "
          "data-quality validation searches so registers, risk scores and inequality views are "
          "accurate, with a named data lead (Dr Adem) accountable. All linked-data access operates "
          "under the relevant data-sharing agreements, the Data Security and Protection Toolkit, "
          "UK GDPR and the Data Protection Act 2018, with Caldicott oversight, so intelligence is "
          "used lawfully and proportionately. The dashboard is the single source of truth for "
          "stratification, recall and reporting, ensuring the whole team acts on the same "
          "intelligence."),
    ("h", "Governance and oversight"),
    ("p", "A monthly PHM review, reporting to the Delivery Board and aligned to the ICS population-"
          "health strategy and Brent's Core20PLUS5 plan, provides continuous oversight, with "
          "data-quality assurance, information-governance compliance and clear accountability "
          "through Dr Adem and Dr Singh."),

    ("h", "Added value"),
    ("p", "Beyond specification we commit to a flagship diabetes-equity programme for Sudbury's "
          "South Asian population - proactive case-finding, language-matched group education and "
          "intensive review of the poorest-controlled cohort - with outcomes published quarterly, "
          "directly targeting the borough's standout inequality."),
]

ANSWERS = [
    ("Q4.1", Q4_1, None),
    ("Q4.2", Q4_2, None),
    ("Q4.3", Q4_3, None),
    ("Q4.4", Q4_4, ["Population Health Management Proposal"]),
]
