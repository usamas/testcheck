#!/usr/bin/env python3
"""Generate all attachment PDFs (<= 2 pages A4 each) into 02 - Attachments/."""
import os
import re
import lib_pdf
import content_attach
import content_prereq

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, "..", "..", "02 - Attachments"))


def page_count(path):
    data = open(path, "rb").read()
    return len(re.findall(rb"/Type\s*/Page[^s]", data))


def main():
    os.makedirs(OUT, exist_ok=True)
    items = [("FP1.3 - TUPE Mobilisation Plan.pdf", content_prereq.FP1_3_ATTACH)]
    items += content_attach.ATTACHMENTS
    warn = []
    for fname, blocks in items:
        path = os.path.join(OUT, fname)
        lib_pdf.build_pdf(path, blocks)
        pc = page_count(path)
        flag = "  <-- OVER 2pp" if pc > 2 else ""
        if pc > 2:
            warn.append(fname)
        print(f"  {fname}: {pc} page(s){flag}")
    print(f"\n{len(items)} attachments built in: {OUT}")
    if warn:
        print("WARNING - over 2 pages:", warn)


if __name__ == "__main__":
    main()
