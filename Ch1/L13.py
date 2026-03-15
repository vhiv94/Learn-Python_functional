def main_func(file_extension):
    return "markdown" if file_extension.lower() in ("markdown", "md") else "plaintext"

run_cases: list[tuple[str, str]] = [
    ("md", "markdown"),
    ("txt", "plaintext"),
]

submit_cases: list[tuple[str, str]] = run_cases + [
    ("markdown", "markdown"),
    ("MD", "markdown"),
    ("docx", "plaintext"),
]