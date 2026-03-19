from enum import Enum

class Doctype(Enum):
    PDF = 1
    TXT = 2
    DOCX = 3
    MD = 4
    HTML = 5


run_cases = [
    (lambda: Doctype.PDF, "Doctype.PDF", False),
    (lambda: Doctype.TXT, "Doctype.TXT", False),
    (lambda: Doctype.DOCX, "Doctype.DOCX", False),
    (lambda: Doctype.MD, "Doctype.MD", False),
]

submit_cases = run_cases + [
    (lambda: Doctype.HTML, "Doctype.HTML", False),
    (lambda: Doctype.Invalid, "Doctype.Invalid", True),
]


def test(func, name, is_err):
    print("---------------------------------")
    print(f"Checking value: {name}")
    try:
        func()
        print("...Valid enum value!")
        return not is_err
    except Exception:
        print("...Invalid enum value!")
        return is_err