def main_func(doc: str) -> str:
    lines = doc.split("\n")
    new_lines = map(remove_line_emphasis, lines)
    return "\n".join(new_lines)


# Don't touch below this line


def remove_line_emphasis(line: str) -> str:
    words = line.split()
    new_words = map(remove_word_emphasis, words)
    return " ".join(new_words)


def remove_word_emphasis(word: str) -> str:
    return word.strip("*")

TestCase = tuple[str, str]

run_cases: list[TestCase] = [
    ("*Don't* panic.\n", "Don't panic.\n"),
    (
        "The **answer to the ultimate question** of life, the universe and everything is *42*\n",
        "The answer to the ultimate question of life, the universe and everything is 42\n",
    ),
    (
        "For a moment, *nothing* happened.\nThen, after a second or so, nothing **continued** to happen.\n",
        "For a moment, nothing happened.\nThen, after a second or so, nothing continued to happen.\n",
    ),
]

submit_cases: list[TestCase] = run_cases + [
    ("", ""),
    (
        "The Hitchhiker's Guide is a d*mn **useful** book.\n",
        "The Hitchhiker's Guide is a d*mn useful book.\n",
    ),
    (
        "In the beginning the *universe* was created.\nThis has made a lot of people very *angry* and been widely regarded as a bad move.\n",
        "In the beginning the universe was created.\nThis has made a lot of people very angry and been widely regarded as a bad move.\n",
    ),
    (
        "Ford, you're turning into a *penguin*\n",
        "Ford, you're turning into a penguin\n",
    ),
    (
        "*Space* is big.\nYou just won't **believe** how vastly, hugely, mind-bogglingly big it is.\n",
        "Space is big.\nYou just won't believe how vastly, hugely, mind-bogglingly big it is.\n",
    ),
    (
        "***Life before death, journey before destination.***\n",
        "Life before death, journey before destination.\n",
    ),
]