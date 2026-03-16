def add_format(default_formats, new_format):
    result = dict(default_formats)
    result[new_format] = True
    return result


def remove_format(default_formats, old_format):
    result = dict(default_formats)
    result[old_format] = False
    return result

run_cases = [
    (
        {"docx": True, "pdf": True},
        add_format,
        "txt",
        {"docx": True, "pdf": True, "txt": True},
    ),
    (
        {"md": True, "txt": False},
        add_format,
        "ppt",
        {"md": True, "txt": False, "ppt": True},
    ),
    ({"md": True, "txt": False}, remove_format, "md", {"md": False, "txt": False}),
]

submit_cases = run_cases + [
    ({}, add_format, "docx", {"docx": True}),
    (
        {"docx": True, "pdf": True, "txt": False},
        remove_format,
        "pdf",
        {"docx": True, "pdf": False, "txt": False},
    ),
    (
        {"docx": True, "pdf": True, "txt": False},
        add_format,
        "jpg",
        {"docx": True, "pdf": True, "txt": False, "jpg": True},
    ),
    (
        {"docx": False, "pdf": True, "txt": True},
        add_format,
        "docx",
        {"docx": True, "pdf": True, "txt": True},
    ),
]