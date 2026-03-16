valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

def main_func(doc_names, doc_formats):
    zipped = list(zip(doc_names, doc_formats))
    is_valid_ext = lambda ext: ext[1] in valid_formats
    return list(filter(is_valid_ext, zipped))

run_cases = [
    (
        ["Proposal", "Invoice", "Contract"], ["docx", "pdoof", "txt"],
        [("Proposal", "docx"), ("Contract", "txt")],
    ),
    (
        ["Presentation", "Summary"], ["pptx", "docx"],
        [("Presentation", "pptx"), ("Summary", "docx")],
    ),
]

submit_cases = run_cases + [
    ([], [], []),
    (["Test", "Example"], ["ppt", "docx"], [("Test", "ppt"), ("Example", "docx")]),
    (
        
        ["Python Cheatsheet", "Java Cheatsheet", "Malware", "Golang Cheatsheet"],
        ["pdf", "docx", "trash", "docx"],
        
        [
            ("Python Cheatsheet", "pdf"),
            ("Java Cheatsheet", "docx"),
            ("Golang Cheatsheet", "docx"),
        ],
    ),
]