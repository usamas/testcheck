#!/usr/bin/env python3
"""Master builder: regenerate the populated Document 5B from the source template.

Idempotent - always starts from the copied template and writes the final answers.
Run:  ../../../.venv/bin/python build_5b.py
"""
import os
import shutil
from docx import Document
import lib_5b

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", "..", ".."))
TEMPLATE = os.path.join(
    ROOT, "Sudbury surgery",
    "Document 5 B - Quality and Technical Questions - Lot 4 Sudbury Surgery v2.docx")
TRD = os.path.normpath(os.path.join(HERE, "..", "..", "01 - Tender Response Documents"))
SRC = os.path.join(TRD, "Document 5B - Quality and Technical Questions v2.docx")


def load_module(name):
    try:
        return __import__(name)
    except Exception as e:  # pragma: no cover
        print(f"  [skip] {name}: {e}")
        return None


def main():
    shutil.copyfile(TEMPLATE, SRC)  # always start from pristine template
    doc = Document(SRC)
    total = 0

    P = load_module("content_prereq")
    if P:
        print("Prerequisites:")
        lib_5b.mark_yes_no_after(doc, "FP1.1")
        lib_5b.mark_yes_no_after(doc, "FP1.2")
        lib_5b.populate_answer(doc, "FP1.3", P.FP1_3, attachments=["TUPE Mobilisation Plan"])
        lib_5b.mark_yes_no_after(doc, "Q1.1")
        lib_5b.mark_yes_no_after(doc, "Q1.2")

    for modname, label in [
        ("content_c2", "Criterion 2 - Quality"),
        ("content_c3", "Criterion 3 - Integration"),
        ("content_c4", "Criterion 4 - Access & PHM"),
        ("content_c5", "Criterion 5 - Social Value"),
    ]:
        M = load_module(modname)
        if not M:
            continue
        print(f"{label}:")
        for ref, blocks, attachments in M.ANSWERS:
            total += lib_5b.populate_answer(doc, ref, blocks, attachments=attachments)

    if P:
        total += lib_5b._count_words(P.FP1_3)

    doc.save(SRC)
    print(f"\nSaved: {SRC}")
    print(f"Total weighted+FP narrative words: {total}")


if __name__ == "__main__":
    main()
