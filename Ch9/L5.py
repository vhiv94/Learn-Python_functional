from enum import Enum


DocFormat = Enum("DocFormat", "PDF TXT MD HTML")

def convert_format(content: str, from_format: DocFormat, to_format: DocFormat) -> str:
    match (from_format, to_format):
        case (DocFormat.MD, DocFormat.HTML):
            return f"<h1>{content[2:]}</h1>"
        case (DocFormat.TXT, DocFormat.PDF):
            return f"[PDF] {content} [PDF]"
        case (DocFormat.HTML, DocFormat.MD):
            return f"# {content[4:-5]}"
        case _:
            raise Exception("invalid type")



run_cases = [
    ("# Hello, world!", DocFormat.MD, DocFormat.HTML, "<h1>Hello, world!</h1>"),
    (
        "This is plain text.",
        DocFormat.TXT,
        DocFormat.PDF,
        "[PDF] This is plain text. [PDF]",
    ),
]

submit_cases = run_cases + [
    ("<h1>Title</h1>", DocFormat.HTML, DocFormat.MD, "# Title"),
    ("Something wicked", DocFormat.TXT, None, "invalid type"),
]


def test(content, from_format, to_format, expected_output):
    print("---------------------------------")
    print(f"Converting from {from_format} to {to_format}...")
    print(f"Content: {content}")
    print(f"Expected: {expected_output}")
    try:
        result = convert_format(content, from_format, to_format)
    except Exception as e:
        result = str(e)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False