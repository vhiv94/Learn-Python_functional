def main_func(document: str, memos: dict[str, int]) -> tuple[int, dict[str, int]]:
    if document in memos.keys():
        return memos[document], memos
    
    new_count = word_count(document)
    new_memos = memos.copy()
    new_memos[document] = new_count
    return new_count, new_memos

def word_count(document: str) -> int:
    count = len(document.split())
    return count

run_cases = [
    (
        "My hovercraft is full of eels",
        {
            "My hovercraft is full of eels": 6,
            "He's a lumberjack and he's okay. He sleeps all night and he works all day": 15,
        },
        (
            6,
            {
                "My hovercraft is full of eels": 6,
                "He's a lumberjack and he's okay. He sleeps all night and he works all day": 15,
            },
        ),
    ),
    (
        "Spam, spam, spam, spam, spam, spam, baked beans, spam, spam, and spam",
        {},
        (
            12,
            {
                "Spam, spam, spam, spam, spam, spam, baked beans, spam, spam, and spam": 12
            },
        ),
    ),
]

submit_cases = run_cases + [
    (
        "This is an ex-parrot",
        {"This parrot is no more": 5},
        (4, {"This parrot is no more": 5, "This is an ex-parrot": 4}),
    ),
    (
        "This doc should 'incorrectly' have 9999 words to test that the memoization is working",
        {
            "My hovercraft is full of eels": 6,
            "This doc should 'incorrectly' have 9999 words to test that the memoization is working": 9999,
        },
        (
            9999,
            {
                "My hovercraft is full of eels": 6,
                "This doc should 'incorrectly' have 9999 words to test that the memoization is working": 9999,
            },
        ),
    ),
]