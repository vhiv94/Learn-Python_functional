'''
#Asignment#
Fix the converted_font_size function. We are using a 3rd party code library that 
expects our function to be a curried series of functions that each take a single argument.

- converted_font_size should just take a single argument, font_size and return a new function.
- The returned function should take a single argument, doc_type, and return font_size 
multiplied by the appropriate value for the given doc_type.
'''

def main_func(font_size):
    def inner(doc_type):
        match doc_type:
            case "txt":
                return font_size
            case "md":
                return font_size * 2
            case "docx":
                return font_size * 3
            case _:
                raise ValueError("invalid doc type")
    return inner

run_cases = [
    (12, "txt", 12),
    (16, "md", 32),
]

submit_cases = run_cases + [
    (14, "html", "invalid doc type"),
    (0, "txt", 0),
    (50, "md", 100),
]