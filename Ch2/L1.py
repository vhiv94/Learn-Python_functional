def main_func(file: dict, to_string):
    file_string = to_string(file)
    return f"```\n{file_string}\n```"


run_cases = [
    (
        {
            "filename": "essay.txt",
            "content": "Dear Mr. Vernon, we accept the fact that we had to sacrifice a whole Saturday in detention for whatever it was we did wrong...",
            "author_first_name": "Brian",
            "author_last_name": "Johnson",
        },
        "```\nFile: essay.txt\nAuthor: Brian Johnson\nContent: Dear Mr. Vernon, we accept the fact that we had to sacrifice a whole Saturday in detention for whatever it was we did wrong...\n```",
    ),
    (
        {
            "filename": "letter.txt",
            "content": "But we think you're crazy to make us write an essay telling you who we think we are.",
            "author_first_name": "Brian",
            "author_last_name": "Johnson",
        },
        "```\nFile: letter.txt\nAuthor: Brian Johnson\nContent: But we think you're crazy to make us write an essay telling you who we think we are.\n```",
    ),
]

submit_cases = run_cases + [
    (
        {
            "filename": "note.txt",
            "content": "Does Barry Manilow know that you raid his wardrobe?",
            "author_first_name": "John",
            "author_last_name": "Bender",
        },
        "```\nFile: note.txt\nAuthor: John Bender\nContent: Does Barry Manilow know that you raid his wardrobe?\n```",
    ),
]