def add_prefix(document, documents: tuple):
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    documents += (new_doc,)
    return documents

def main_func(input):
    try:
        documents = ()
        for doc in input:
            documents = add_prefix(doc, documents)
    except Exception as e:
        documents = f"Error: {e}"
    return documents

run_cases = [
    (
        ("hello there", "sonny", "how ya doing"),
        ("0. hello there", "1. sonny", "2. how ya doing"),
    )
]

submit_cases = run_cases + [
    (
        ("go", "python", "java", "javascript"),
        ("0. go", "1. python", "2. java", "3. javascript"),
    ),
    (
        ("boots", "everyone else"),
        ("0. boots", "1. everyone else"),
    ),
]