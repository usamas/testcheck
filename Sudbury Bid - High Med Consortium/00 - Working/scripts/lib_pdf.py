"""Helper to render attachment PDFs (<= 2 pages A4) from a block list.

Block format mirrors lib_5b:
  ("title", "Document title")  -> document title (once, top)
  ("h", "Heading")
  ("p", "paragraph")
  ("b", ["item", ...])
  ("t", [[header...],[row...]])
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, ListFlowable, ListItem,
)
from reportlab.lib.enums import TA_LEFT


def _styles():
    ss = getSampleStyleSheet()
    base = ss["Normal"]
    base.fontName = "Helvetica"
    base.fontSize = 8.5
    base.leading = 11
    title = ParagraphStyle("DocTitle", parent=base, fontName="Helvetica-Bold",
                           fontSize=13, leading=15, spaceAfter=6)
    sub = ParagraphStyle("Sub", parent=base, fontSize=7.5, textColor=colors.HexColor("#444444"),
                         spaceAfter=8)
    head = ParagraphStyle("Head", parent=base, fontName="Helvetica-Bold",
                          fontSize=9.5, leading=12, spaceBefore=6, spaceAfter=3)
    body = ParagraphStyle("Body", parent=base, alignment=TA_LEFT, spaceAfter=4)
    bullet = ParagraphStyle("Bullet", parent=body, leftIndent=10, spaceAfter=2)
    cell = ParagraphStyle("Cell", parent=base, fontSize=7.8, leading=9.5)
    cellh = ParagraphStyle("CellH", parent=cell, fontName="Helvetica-Bold",
                           textColor=colors.white)
    return dict(title=title, sub=sub, head=head, body=body, bullet=bullet,
                cell=cell, cellh=cellh)


SUBHEADER = ("High Med Ltd + Dr Singh Hammond Road consortium  |  "
             "Lot 4 Sudbury Surgery (E84685)  |  Atamis C444743")


def build_pdf(path, blocks):
    S = _styles()
    doc = SimpleDocTemplate(path, pagesize=A4,
                            leftMargin=14 * mm, rightMargin=14 * mm,
                            topMargin=12 * mm, bottomMargin=12 * mm)
    flow = []
    for kind, payload in blocks:
        if kind == "title":
            flow.append(Paragraph(payload, S["title"]))
            flow.append(Paragraph(SUBHEADER, S["sub"]))
        elif kind == "h":
            flow.append(Paragraph(payload, S["head"]))
        elif kind == "p":
            flow.append(Paragraph(payload, S["body"]))
        elif kind == "b":
            items = [ListItem(Paragraph(it, S["bullet"]), leftIndent=10) for it in payload]
            flow.append(ListFlowable(items, bulletType="bullet", start="\u2022",
                                     leftIndent=10))
        elif kind == "t":
            rows = payload
            ncols = max(len(r) for r in rows)
            data = []
            for ri, row in enumerate(rows):
                rendered = []
                for ci in range(ncols):
                    val = str(row[ci]) if ci < len(row) else ""
                    rendered.append(Paragraph(val, S["cellh"] if ri == 0 else S["cell"]))
                data.append(rendered)
            t = Table(data, repeatRows=1)
            t.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1f4e79")),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#888888")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1),
                 [colors.white, colors.HexColor("#eef3f8")]),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
                ("LEFTPADDING", (0, 0), (-1, -1), 3),
                ("RIGHTPADDING", (0, 0), (-1, -1), 3),
            ]))
            flow.append(t)
            flow.append(Spacer(1, 4))
    doc.build(flow)
    return path
