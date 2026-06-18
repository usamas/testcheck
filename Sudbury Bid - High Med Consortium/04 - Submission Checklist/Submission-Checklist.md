# Submission Checklist — Lot 4 Sudbury Surgery (Atamis C444743)

**Bidder:** High Med Ltd (Lead) + Dr Singh Hammond Road (key party)
**Deadline:** 29 June 2026, 12:00 | **Service start:** 1 November 2026
**Status of this pack:** Full first draft generated and red-team verified (see notes).

---

## Documents to upload (01 - Tender Response Documents/)

- [x] Document 5A — Selection Questionnaire — High Med Ltd (Lead)
- [x] Document 5A — Selection Questionnaire — Dr Singh Hammond Road
- [x] Document 5B — Quality and Technical Questions v2 (all FP + 20 weighted answers)
- [x] Document 5C — Financial Ratio Template (FRT) — structure + bidder names
- [x] Document 5D — Commercial Schedule — workforce roster + activity + CQ notes
- [x] Document 5F — Form of Offer and Declarations — signature block + interests

## Attachments (02 - Attachments/) — all ≤ 2 pages A4

- [x] FP1.3 — TUPE Mobilisation Plan
- [x] Q2.1 — Implementation Plan; Organisational Structure; Clinical and Operational Workflows; Workforce Plan
- [x] Q2.4 — Safeguarding Adults Policy; Safeguarding Children Policy
- [x] Q2.7 — Mobilisation Gantt; Mobilisation Risk Assessment
- [x] Q2.8 — Premises Mobilisation Plan; Premises Risk Register
- [x] Q3.2 — Workforce Structure; Retention Policy
- [x] Q4.1a — Case Study 1; Case Study 2
- [x] Q4.4 — PHM Proposal
- [x] Q4.4a — PHM Illustrative Example

## Supporting evidence (03 - Supporting Evidence/)

- [x] Safeguarding policy (Appendix 1), Retention policy (Appendix 2)
- [x] ICO certificate, CQC certificates (Dr Singh), audited accounts

---

## Red-team verification (run: 00 - Working/scripts/red_team.py)

- [x] Every weighted question and FP1.3 has a populated answer
- [x] All responses within their 5B v2 word limits (headroom remains on every question)
- [x] No question left blank (no score-0 elimination risk on completeness)
- [x] FP1.3 holds TUPE/PID/GDPR/DPA2018/BCP/pensions; Q2.7 is access/choice only
- [x] Q5.3 framed as break down barriers to opportunity (inclusive recruitment), not wellbeing
- [x] Q2.8 = Premises; Q2.9 = Patients 75+ (12 bullets covered)
- [x] All 17 TUPE positions named (Q3.2 + Workforce Structure); 3 vacancies have locum contingency
- [x] No cross-references between questions; evidence duplicated inline
- [x] No Hounslow / Isleworth / Ivybridge / other-lot references in 5B
- [x] All attachments ≤ 2 pages A4

---

## Outstanding items before final submission (owner action)

These are deliberately NOT fabricated and must be confirmed:

- [ ] **Deepen narratives toward word limits** — every response is complete and covers all
      mandatory bullets, but sits well under the limit; expand local evidence and detail to
      maximise the Excellent (10) score on high-weight questions (Q2.1, Q4.4, Q3.2 first).
- [ ] **Commercial (5D/5C)** — enter confirmed cost figures and audited-accounts financials.
      Pending clarifications: global sum/affordability (CQ5/CQ22), LES/DES (CQ52), locum
      (CQ53), estates/NIA (CQ9/CQ21/CQ44/CQ48), ARRS WTE (CQ50), QOF (CQ51), weighted list (CQ47).
- [ ] **5A identity fields** — replace "[To confirm: …]" placeholders (email, FTS ID for High Med;
      Dr Singh Hammond Road registration/address/PSC).
- [ ] **Clinical system** — confirm EMIS vs SystmOne with NHSolutions; update FP1.3/Q2.1/Q2.5.
- [ ] **Named roles** — confirm TUPE PM/DPM names, frailty home-visit clinician model.
- [ ] **Signatures and dates** — sign 5F; convert final docs to required upload format.
- [ ] **Convert attachments** — review reportlab PDFs; brand/format as preferred before upload.
- [ ] **Word-count cells** — figures auto-filled in 5B; re-check after any narrative expansion.

---

## How to regenerate the pack

From `00 - Working/scripts/` using the project venv:

```bash
/Users/usama/Desktop/Bid\ for\ surgerys/.venv/bin/python build_5b.py
/Users/usama/Desktop/Bid\ for\ surgerys/.venv/bin/python build_attachments.py
/Users/usama/Desktop/Bid\ for\ surgerys/.venv/bin/python build_commercial.py
/Users/usama/Desktop/Bid\ for\ surgerys/.venv/bin/python build_5a.py
/Users/usama/Desktop/Bid\ for\ surgerys/.venv/bin/python build_5f.py
/Users/usama/Desktop/Bid\ for\ surgerys/.venv/bin/python red_team.py
```

Answer content lives in `content_prereq.py`, `content_c2.py`, `content_c3.py`,
`content_c4.py`, `content_c5.py` (5B narratives) and `content_attach.py` (attachments).
Edit those and re-run `build_5b.py` / `build_attachments.py` to update the pack.
