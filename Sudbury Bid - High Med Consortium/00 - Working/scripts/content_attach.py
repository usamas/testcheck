# -*- coding: utf-8 -*-
"""Attachment content (<= 2 pages A4 each) for Lot 4 Sudbury Surgery.

Each entry: (output_filename, blocks). Built by build_attachments.py.
FP1.3 attachment lives in content_prereq.FP1_3_ATTACH.
"""

# ----------------------------- Q2.1 (4 attachments) -----------------------------
Q2_1_IMPL = [
    ("title", "Q2.1 Service Model - Implementation Plan"),
    ("p", "Mobilisation Lead Dr Usama Safeer; Clinical Director Dr Shumaila Mahmood. "
          "Service commencement 1 November 2026; 18-month improvement trajectory."),
    ("h", "Phased implementation"),
    ("t", [
        ["Phase", "Timeframe", "Objectives", "Owner"],
        ["Phase 1 - Stabilise", "Mob (Aug-Oct 2026) + months 0-3",
         "TUPE transfer; system/data continuity; Day-1 audit; confirm QOF/screening/immunisation registers; access standards met",
         "Dr Safeer / Ms Kaur"],
        ["Phase 2 - Embed", "Months 4-12",
         "Risk stratification; structured LTC reviews; access redesign; PHM programmes; recall optimisation",
         "Dr Singh / Dr Adem"],
        ["Phase 3 - Optimise", "Months 13-18",
         "Close inequality gaps; upper-quartile QOF; demonstrate measurable outcomes",
         "Dr Mahmood"],
    ]),
    ("h", "Key milestones"),
    ("b", [
        "Month 0: go-live with hypercare; baseline report to ICB within 30 days.",
        "Month 3: access standards evidenced; registers validated.",
        "Month 6: PHM programmes live; first improvement review with PPG/PCN.",
        "Month 12: inequality and QOF trajectory review.",
        "Month 18: outcomes report; sustained performance.",
    ]),
    ("h", "Governance of delivery"),
    ("p", "Monthly delivery board chaired by the Clinical Director; RAG milestone tracker; "
          "exception reporting to the ICB; risk register maintained throughout."),
]

Q2_1_ORG = [
    ("title", "Q2.1 Service Model - Organisational Structure"),
    ("p", "Named leadership for the High Med Ltd + Dr Singh Hammond Road consortium delivering "
          "Sudbury Surgery (E84685)."),
    ("h", "Leadership and accountability"),
    ("t", [
        ["Role", "Named lead", "Responsibility"],
        ["Clinical Director / accountable officer", "Dr Shumaila Mahmood", "Governance, board assurance, CQC interface"],
        ["Local clinical lead (LTC, frailty, prescribing, safeguarding)", "Dr Gursharan Singh", "Clinical delivery and governance"],
        ["Mobilisation lead", "Dr Usama Safeer", "Transition, access mobilisation"],
        ["Practice Manager", "Ms Manjot Kaur", "Operations, workforce, engagement"],
        ["Deputy Practice Manager", "Transferring DPM", "Day-to-day operations; interim PM governance"],
        ["Caldicott / IG / PHM dashboard", "Dr Muhammad Adem", "DSPT, data migration, population health"],
        ["Public health / immunisation", "Dr Saira Safeer", "Vaccination programmes"],
        ["Infection prevention & control", "Ms Gladys Amaf", "IPC, premises safety"],
    ]),
    ("h", "Reporting lines"),
    ("b", [
        "Clinical team and ARRS report to the local clinical lead; clinical lead reports to the Clinical Director.",
        "Operational and reception/admin teams report to the Practice Manager via the Deputy PM.",
        "IG, safeguarding and IPC leads provide assurance to the Clinical Director and board.",
        "Deputising arrangements defined for every leadership role.",
    ]),
    ("h", "Workforce in scope"),
    ("p", "17 positions: 14 transferring (Lead GP, HCA, 2 phlebotomists, PM, DPM, 7 reception/"
          "admin) plus 3 vacancies (2 GP, 1 Practice Nurse), supplemented by PCN ARRS roles."),
]

Q2_1_WORKFLOWS = [
    ("title", "Q2.1 Service Model - Clinical and Operational Workflows"),
    ("h", "Access and care navigation"),
    ("p", "Single point of contact with care navigation and same-day clinical assessment; duty "
          "GP/NP for urgent need and home visits throughout core hours; choice of consultation "
          "mode and named clinician for continuity."),
    ("h", "Proactive care and recall (rolling 12-month cycle)"),
    ("t", [
        ["Workflow", "Method", "Owner"],
        ["QOF and LTC annual reviews", "Register search, structured recall, birthday-month model", "Dr Singh"],
        ["National screening (cervical, bowel, breast, AAA, DES)", "Call/recall, DNA follow-up", "Nursing team"],
        ["Childhood & seasonal immunisations", "Call/recall, opportunistic, outreach", "Dr Saira Safeer"],
        ["Medication reviews / SMRs", "Risk-prioritised, pharmacist-led", "Dr Singh / PCN pharmacist"],
    ]),
    ("h", "Safe operational workflows"),
    ("b", [
        "Repeat prescribing SOP with re-authorisation and synchronised quantities.",
        "Results, documents and tasks with safety-netting and failsafe tracking.",
        "Referrals via e-RS with two-week-wait tracking.",
        "Care navigation protocols and scripts for reception staff.",
    ]),
    ("h", "Monitoring"),
    ("p", "All workflows monitored via the clinical system and population-health dashboard with "
          "monthly KPI review and exception reporting."),
]

Q2_1_WORKFORCE = [
    ("title", "Q2.1 Service Model - Workforce Plan"),
    ("p", "Staffing sized to the contractual access standards for a 7,788 list (recalibrated to "
          "the Carr-Hill weighted list at award)."),
    ("h", "Establishment"),
    ("t", [
        ["Group", "Posts", "Notes"],
        ["GPs", "Lead GP (transferring) + 2 vacancies (37.5 & 20 hrs)", "Locum cover until recruited"],
        ["Nursing", "1 Practice Nurse vacancy (37.5 hrs)", "Recruitment + locum"],
        ["HCA / phlebotomy", "1 HCA + 2 phlebotomists (transferring)", "Continuity of bloods/pathology"],
        ["Management", "Practice Manager + Deputy PM", "Interim governance for PM post"],
        ["Reception / admin", "7 transferring staff", "Care navigation trained"],
        ["PCN ARRS", "Pharmacist, FCP, social prescriber, H&W coach", "Network-allocated; supervised"],
    ]),
    ("h", "Capacity vs contractual standards"),
    ("b", [
        "Target >=561 GP/NP and >=195 nurse/HCA consultations per week (>=100/1,000 total).",
        ">=3 NHS 111 bookable slots per week.",
        "Duty clinician throughout core hours for urgent care and home visits.",
    ]),
    ("h", "Recruitment, retention and contingency"),
    ("b", [
        "Active recruitment for 3 vacancies; pre-agreed locum and PCN mutual aid.",
        "Retention: NHS Pension continuity, induction, supervision, CPD, London Living Wage.",
        "Contingency for sickness, leave and surge via bank/locum pool and cross-cover.",
    ]),
]

# ----------------------------- Q2.4 (2 policy attachments) -----------------------------
Q2_4_ADULTS = [
    ("title", "Q2.4 Safeguarding Adults Policy (Summary) - Sudbury Surgery"),
    ("p", "Safeguarding lead GP: Dr Gursharan Singh. Board assurance: Dr Shumaila Mahmood. "
          "Aligned to the Care Act 2014, Mental Capacity Act 2005 and Brent multi-agency "
          "safeguarding arrangements. Full policy held in the practice policy suite."),
    ("h", "Purpose and scope"),
    ("p", "Protects adults at risk of abuse or neglect, setting out recognition, response, "
          "referral and recording for all staff including locums."),
    ("h", "Key provisions"),
    ("b", [
        "Types and indicators of abuse and neglect; making safeguarding personal.",
        "Mental Capacity Act 2005, best-interest decisions and Liberty Protection Safeguards.",
        "Consent and information-sharing under the correct legal basis (UK GDPR / DPA 2018).",
        "Referral pathway to Brent adult social care / MASH and named ICB designated professionals.",
        "Domestic abuse, modern slavery, Prevent, self-neglect and carer support.",
    ]),
    ("h", "Governance and training"),
    ("b", [
        "Clinicians trained to Level 3; all staff to role-appropriate level; tracked on matrix.",
        "Vulnerable-adult register and alerts; regular safeguarding meeting and case review.",
        "Annual audit; significant event analysis; policy review cycle.",
    ]),
]

Q2_4_CHILDREN = [
    ("title", "Q2.4 Safeguarding Children Policy (Summary) - Sudbury Surgery"),
    ("p", "Safeguarding lead GP: Dr Gursharan Singh. Board assurance: Dr Shumaila Mahmood. "
          "Aligned to Working Together to Safeguard Children and Brent safeguarding "
          "partnership arrangements. Full policy held in the practice policy suite."),
    ("h", "Purpose and scope"),
    ("p", "Protects children and young people, including the specific position for 16-17 year-"
          "olds, the unborn, and children in vulnerable circumstances."),
    ("h", "Key provisions"),
    ("b", [
        "Recognising abuse and neglect; thresholds and early help.",
        "Mental Capacity Act considerations for 16-17 year-olds; Gillick competence and consent.",
        "Referral to Brent children's social care / MASH; named and designated professionals.",
        "Children with a child protection plan and looked-after children registers and alerts.",
        "FGM, CSE/CCE, domestic abuse, and was-not-brought (rather than DNA) follow-up.",
    ]),
    ("h", "Governance and training"),
    ("b", [
        "Clinicians trained to Level 3; all staff to role-appropriate level; tracked on matrix.",
        "Information-sharing with health visiting, schools and social care under correct basis.",
        "Annual audit; significant event analysis; multi-agency participation; review cycle.",
    ]),
]

# ----------------------------- Q2.7 (2 attachments) -----------------------------
Q2_7_GANTT = [
    ("title", "Q2.7 Mobilisation - Access & Choice Timeline"),
    ("p", "Access mobilisation led by Dr Usama Safeer with Ms Manjot Kaur. Focus: appointment "
          "system, patient choice and Enhanced Access (TUPE/PID/BCP are in FP1.3)."),
    ("t", [
        ["Period", "Access mobilisation activity", "Owner"],
        ["Aug 2026", "Day-1 audit commissioned with NHSolutions; appointment policy drafted", "Dr Safeer"],
        ["Sep 2026", "Telephony & online consultation configured; care-navigation training", "Ms Kaur"],
        ["Sep-Oct", "NHS 111 slots (>=3/week) set up; Enhanced Access MOU with PCN", "Dr Safeer"],
        ["Oct 2026", "Rota and capacity modelling; access KPIs and dashboards tested", "Ms Kaur"],
        ["1 Nov 2026", "Go-live; same-day assessment and choice live; hypercare", "Dr Safeer"],
        ["By day 30", "Baseline access report to ICB; improvement plan published", "Dr Mahmood"],
    ]),
    ("h", "Access standards from go-live"),
    ("b", [
        "Single point of contact; same-day clinical assessment; duty clinician in core hours.",
        "Choice of clinician and consultation mode; continuity for LTCs.",
        ">=3 NHS 111 bookable slots/week; Enhanced Access via Brent Central K&W PCN.",
    ]),
]

Q2_7_RISK = [
    ("title", "Q2.7 Mobilisation - Access Risk Assessment"),
    ("t", [
        ["Risk", "RAG", "Mitigation", "Owner"],
        ["No incumbent wait-time baseline at go-live", "Amber",
         "Day-1 joint audit; interim contractual targets; 30-day baseline report", "Dr Safeer"],
        ["Telephony demand exceeds capacity", "Amber",
         "Cloud telephony with call-back; care navigation; rota flex", "Ms Kaur"],
        ["Enhanced Access arrangement delayed", "Green",
         "Early PCN MOU; network Access Hub", "Dr Safeer"],
        ["Digital exclusion limits access", "Amber",
         "Preserved phone/walk-in routes; assisted digital; translations", "Ms Kaur"],
        ["DNA rates reduce effective capacity", "Amber",
         "Reminders, partial booking, easy cancellation; monitor by cohort", "Dr Adem"],
    ]),
    ("h", "Monitoring"),
    ("p", "Monthly access huddle; telephony analytics (speed-to-answer, abandonment); FFT and "
          "GPPS; quarterly PPG review with 'You Said, We Did'."),
]

# ----------------------------- Q2.8 (2 attachments) -----------------------------
Q2_8_MOB = [
    ("title", "Q2.8 Premises Mobilisation Plan - Vale Farm PCC"),
    ("p", "Premises: 3-storey purpose-built NHS property, Vale Farm Primary Care Centre, Watford "
          "Road, Wembley HA0 3HG. Landlord: Community Health Partnerships (CHP). Lease to "
          "5 November 2032. Lead: Ms Manjot Kaur."),
    ("t", [
        ["Activity", "Timeframe", "Owner"],
        ["Engage CHP; agree lease assignment / occupational terms", "Aug-Sep 2026", "Ms Kaur"],
        ["Statutory compliance checks (fire, H&S, IPC, accessibility)", "Sep 2026", "Ms Amaf"],
        ["Facilities/service contracts continuity; signage", "Sep-Oct 2026", "Ms Kaur"],
        ["Room readiness and minor works (if any)", "Oct 2026", "Ms Kaur"],
        ["Operational from premises at go-live", "1 Nov 2026", "Ms Kaur"],
    ]),
    ("h", "Cost basis (to confirm via due diligence)"),
    ("b", [
        "Reimbursable rent in the order of GBP 337,824/yr; rates around GBP 12,906.",
        "Service charges and net internal area to be confirmed (clarification).",
    ]),
]

Q2_8_RISK = [
    ("title", "Q2.8 Premises Risk Register - Vale Farm PCC"),
    ("t", [
        ["Risk", "RAG", "Mitigation", "Owner"],
        ["Lease assignment not completed before go-live", "Amber",
         "Early CHP engagement; legal support; lease secured to 2032", "Ms Kaur"],
        ["Building condition / backlog maintenance", "Green",
         "Modern PCC; condition survey; landlord responsibilities defined", "Ms Kaur"],
        ["Use restrictions / shared occupancy", "Green",
         "Confirm permitted use and shared areas with CHP", "Ms Kaur"],
        ["Statutory compliance gap (fire/H&S/IPC)", "Amber",
         "Pre-go-live verification; scheduled checks; IPC audit", "Ms Amaf"],
        ["Accessibility for disabled/older patients", "Green",
         "Step-free access; adjustments; accessibility audit", "Ms Amaf"],
    ]),
    ("h", "Assurance"),
    ("p", "Register reviewed at the delivery board through mobilisation and maintained in "
          "operation; long lease to 2032 secures tenure."),
]

# ----------------------------- Q3.2 (2 attachments) -----------------------------
Q3_2_STRUCT = [
    ("title", "Q3.2 Workforce Structure - Sudbury Surgery"),
    ("p", "All 17 positions in scope (Document 4, Lot 4): 14 transferring + 3 vacancies, plus "
          "PCN ARRS. Lead: Ms Manjot Kaur; clinical oversight: Dr Shumaila Mahmood."),
    ("t", [
        ["#", "Position", "Status"],
        ["1", "Lead GP", "Transferring"],
        ["2", "Healthcare Assistant", "Transferring"],
        ["3-4", "Phlebotomists (x2)", "Transferring"],
        ["5", "Practice Manager", "Transferring (interim DPM governance)"],
        ["6", "Deputy Practice Manager", "Transferring"],
        ["7-13", "Reception / administrative (x7)", "Transferring"],
        ["14", "Transferring staff member (per TUPE pack)", "Transferring"],
        ["15", "GP (37.5 hrs)", "Vacancy - recruit + locum"],
        ["16", "GP (20 hrs)", "Vacancy - recruit + locum"],
        ["17", "Practice Nurse (37.5 hrs)", "Vacancy - recruit + locum"],
        ["ARRS", "Clinical pharmacist, FCP, social prescriber, H&W coach", "PCN-allocated, supervised"],
    ]),
    ("h", "Capacity and contingency"),
    ("b", [
        "Sized to contractual access standards; recalibrated to Carr-Hill weighted list at award.",
        "Pre-agreed locum and PCN mutual-aid cover for the 3 vacancies.",
        "Bank/locum pool, flexible rotas and cross-cover for absence and surge.",
    ]),
]

Q3_2_RETENTION = [
    ("title", "Q3.2 Staff Retention Policy (Summary) - Sudbury Surgery"),
    ("p", "Supports retention and wellbeing of transferring and new staff. Lead: Ms Manjot Kaur. "
          "Full policy held in the practice policy suite (based on consortium retention policy)."),
    ("h", "Retention measures"),
    ("b", [
        "TUPE protection of terms; continuity of NHS Pension membership.",
        "Structured 12-week induction and buddying; clinical and managerial supervision.",
        "Funded CPD, appraisal and revalidation; protected learning time.",
        "Flexible and family-friendly working; wellbeing and Employee Assistance Programme.",
        "Freedom to Speak Up access; fair and supportive performance management.",
        "Payment of at least the London Living Wage.",
    ]),
    ("h", "Targets and monitoring"),
    ("t", [
        ["Measure", "Target"],
        ["Transferring staff retained at 6 months", ">=90%"],
        ["Appraisal completion (12 months)", "100%"],
        ["Mandatory training compliance", ">=98%"],
        ["Staff engagement/wellbeing review", "Annual + pulse checks"],
    ]),
]

# ----------------------------- Q4.1a (2 case studies) -----------------------------
CASE_STUDY_1 = [
    ("title", "Q4.1a Case Study 1 - Improving Diabetes Care for an Asian-Heritage Cohort"),
    ("h", "Why this group is a priority (local need)"),
    ("p", "Over half of Sudbury's registered patients are of Asian heritage and Brent diabetes "
          "prevalence (8.58%) exceeds England (7.26%), with earlier onset and higher "
          "complication risk in South Asian communities. Closing this gap is a Core20PLUS5 "
          "priority."),
    ("h", "Potential barriers to access"),
    ("b", [
        "Language and health-literacy barriers (around one in three not using English as a main language).",
        "Cultural factors in diet, fasting and self-management.",
        "Lower uptake of structured reviews and retinal/foot screening in some groups.",
    ]),
    ("h", "Specific measures to address barriers"),
    ("b", [
        "Bilingual recall and education materials; interpreter-supported reviews.",
        "Culturally tailored self-management and dietary advice (including Ramadan guidance) with community partners.",
        "Pharmacist-led structured medication reviews; proactive recall for the 3 treatment targets and screening.",
        "Brent Health Matters outreach and community-venue clinics.",
    ]),
    ("h", "How effectiveness would be evaluated"),
    ("t", [
        ["Measure", "Baseline", "Target (12-18 months)"],
        ["3 diabetes treatment targets achieved", "Establish", "At/above benchmark"],
        ["Retinal and foot screening uptake", "Establish", "Improving"],
        ["Equity gap vs least-deprived cohort", "Measure", "Narrowing"],
    ]),
    ("p", "No patient-identifiable information is used; this is an illustrative model."),
]

CASE_STUDY_2 = [
    ("title", "Q4.1a Case Study 2 - Supporting Digitally Excluded Older Patients"),
    ("h", "Why this group is a priority (local need)"),
    ("p", "Brent's 75+ population is projected to grow 71% by 2041. Many older patients face "
          "digital exclusion, risking poorer access as services digitise."),
    ("h", "Potential barriers to access"),
    ("b", [
        "Limited digital skills, devices or connectivity.",
        "Sensory, cognitive or mobility impairments.",
        "Social isolation and low confidence navigating services.",
    ]),
    ("h", "Specific measures to address barriers"),
    ("b", [
        "Preserved telephone and walk-in routes alongside digital channels.",
        "Assisted digital support and carer involvement; accessible information.",
        "Proactive telephone recall and home visits for housebound patients.",
        "Social prescribing to tackle isolation; partnership with Age UK and voluntary sector.",
    ]),
    ("h", "How effectiveness would be evaluated"),
    ("t", [
        ["Measure", "Baseline", "Target (12-18 months)"],
        ["Non-digital access maintained when needed", "100%", "100%"],
        ["75+ care plans and reviews completed", "Establish", ">=90%"],
        ["Older-patient experience (FFT/survey)", "Establish", "Improving"],
    ]),
    ("p", "No patient-identifiable information is used; this is an illustrative model."),
]

# ----------------------------- Q4.4 / Q4.4a -----------------------------
Q4_4_PROPOSAL = [
    ("title", "Q4.4 Population Health Management Proposal - Sudbury Surgery"),
    ("p", "Owner: Dr Muhammad Adem. Framework: Core20PLUS5. Tools: clinical system, eFI, "
          "WSIC / NWL primary care dashboards. Delivered with Brent Central K&W PCN and "
          "system partners."),
    ("h", "Method: segment, stratify, intervene, evaluate"),
    ("t", [
        ["Step", "Action"],
        ["Segment", "Identify Core20 (most deprived 20%), PLUS inclusion-health groups, and the 5 clinical priorities"],
        ["Stratify", "Risk-stratify with eFI and dashboards; validate registers"],
        ["Intervene", "Targeted, culturally tailored interventions with named owners"],
        ["Evaluate", "Baseline -> KPI trajectory; equity-gap monitoring; governance review"],
    ]),
    ("h", "Priority programmes (dataset -> intervention -> owner -> target)"),
    ("t", [
        ["Priority", "Intervention", "Owner", "Target"],
        ["Diabetes (prev. 8.58%)", "SMRs, bilingual education, screening recall", "Dr Singh / pharmacist", "3 targets at/above benchmark"],
        ["Hypertension/CVD", "Case-finding, BP@home, optimisation", "Dr Singh", "BP controlled improving"],
        ["SMI", "Annual physical health checks", "Nursing team", ">=90%"],
        ["Cancer", "Screening uptake in underserved groups", "Dr Adem", "At/above benchmark"],
        ["Respiratory/maternity", "Greener inhalers; maternity continuity links", "Dr Singh", "Improving"],
    ]),
    ("h", "Governance and equity"),
    ("p", "Quarterly PHM review with data-quality assurance and equity monitoring; annual "
          "Sudbury inequalities outcomes report to PPG and ICB."),
]

Q4_4A_EXAMPLE = [
    ("title", "Q4.4a Illustrative Example - Wembley Diabetes Prevention & Control Programme"),
    ("h", "Proposed model"),
    ("p", "A flagship programme for Sudbury's highest-risk communities, applying the PHM method "
          "to Brent's elevated diabetes burden. Illustrative only; no patient-identifiable data."),
    ("h", "How the approach is applied"),
    ("b", [
        "Identify: dashboard finds patients with diabetes and those at high risk (NDH/pre-diabetes), prioritising the most deprived and South Asian cohorts.",
        "Engage: bilingual outreach with Brent Health Matters, faith and community venues; referral to the NHS Diabetes Prevention Programme.",
        "Intervene: structured reviews, pharmacist-led SMRs, culturally tailored lifestyle and dietary support, retinal/foot screening recall.",
        "Coordinate: PCN clinical pharmacist, community dietetics and social prescribing.",
    ]),
    ("h", "Outcomes and evaluation"),
    ("t", [
        ["Measure", "Baseline", "12 months", "18 months"],
        ["NDH patients referred to NDPP", "Establish", "Increasing", "Sustained"],
        ["Diabetes 3 treatment targets", "Establish", "Improving", "At/above benchmark"],
        ["Screening uptake (retinal/foot)", "Establish", "Improving", "At/above benchmark"],
        ["Equity gap (most vs least deprived)", "Measure", "Narrowing", "Reduced"],
    ]),
    ("h", "System fit"),
    ("p", "Aligns with Core20PLUS5, the ICS population-health strategy and Brent neighbourhood "
          "priorities; governed through the practice PHM review and PCN."),
]

ATTACHMENTS = [
    ("Q2.1 - Implementation Plan.pdf", Q2_1_IMPL),
    ("Q2.1 - Organisational Structure.pdf", Q2_1_ORG),
    ("Q2.1 - Clinical and Operational Workflows.pdf", Q2_1_WORKFLOWS),
    ("Q2.1 - Workforce Plan.pdf", Q2_1_WORKFORCE),
    ("Q2.4 - Safeguarding Adults Policy.pdf", Q2_4_ADULTS),
    ("Q2.4 - Safeguarding Children Policy.pdf", Q2_4_CHILDREN),
    ("Q2.7 - Mobilisation Gantt.pdf", Q2_7_GANTT),
    ("Q2.7 - Mobilisation Risk Assessment.pdf", Q2_7_RISK),
    ("Q2.8 - Premises Mobilisation Plan.pdf", Q2_8_MOB),
    ("Q2.8 - Premises Risk Register.pdf", Q2_8_RISK),
    ("Q3.2 - Workforce Structure.pdf", Q3_2_STRUCT),
    ("Q3.2 - Retention Policy.pdf", Q3_2_RETENTION),
    ("Q4.1a - Case Study 1.pdf", CASE_STUDY_1),
    ("Q4.1a - Case Study 2.pdf", CASE_STUDY_2),
    ("Q4.4 - PHM Proposal.pdf", Q4_4_PROPOSAL),
    ("Q4.4a - PHM Illustrative Example.pdf", Q4_4A_EXAMPLE),
]
