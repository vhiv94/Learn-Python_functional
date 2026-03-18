def file_type_getter(file_extension_tuples: list[tuple]):
    tuple_dict = {}
    for tup in file_extension_tuples:
        for ext in tup[1]:
            tuple_dict[ext] = tup[0]

    return lambda val: tuple_dict.get(val, "Unknown")

def main_func(tup_list: list[tuple], value):
    getter_function = file_type_getter(tup_list)
    return getter_function(value)

run_cases = [
    (
        [("document", [".doc", ".docx"]), ("image", [".jpg", ".png"])],
        ".doc",
        "document",
    ),
    (
        [("document", [".doc", ".docx"]), ("image", [".jpg", ".png"])],
        ".png",
        "image",
    ),
]

submit_cases = run_cases + [
    (
        [("document", [".doc", ".docx"]), ("image", [".jpg", ".png"])],
        ".txt",
        "Unknown",
    ),
    (
        [("code", [".py", ".js"]), ("markup", [".html", ".xml"])],
        ".js",
        "code",
    ),
]