import functools

def main_func(sentences, n):
    cat = lambda doc_so_far, sentence: f"{doc_so_far} {sentence}."
    return functools.reduce(cat, sentences[:n], "").strip()

run_cases = [
    (
        ["I don't feel safe", "Are you cussing with me"],
        2,
        "I don't feel safe. Are you cussing with me.",
    ),
    (
        ["You're fantastic", "He's just another rat", "Where'd the food come from"],
        2,
        "You're fantastic. He's just another rat.",
    ),
]

submit_cases = run_cases + [
    (["I'm not different"], 0, ""),
    (
        [
            "You wrote a bad song",
            "This is a good idea",
            "Just buy the tree",
            "It's going to flood",
            "Tell us what to do",
            "Here comes the train",
            "Are you cussing with me?",
            "This is just cider",
            "Get me a bandit hat",
        ],
        3,
        "You wrote a bad song. This is a good idea. Just buy the tree.",
    ),
]