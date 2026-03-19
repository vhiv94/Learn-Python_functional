from functools import lru_cache

@lru_cache
def is_palindrome(word: str) -> bool:
    if len(word) <= 1:
        return True
    if not word[0] == word[-1]:
        return False
    else:
        return is_palindrome(word[1:-1])

run_cases = [
    (
        "aibohphobia",
        True,
    ),
    (
        "eve",
        True,
    ),
    (
        "level",
        True,
    ),
    (
        "",
        True,
    ),
    (
        "tat",
        True,
    ),
    (
        "rotator",
        True,
    ),
    (
        "potato",
        False,
    ),
]


submit_cases = run_cases + [
    (
        "a",
        True,
    ),
    (
        "apple",
        False,
    ),
    (
        "redivider",
        True,
    ),
    (
        "divide",
        False,
    ),
    (
        "kayak",
        True,
    ),
    (
        "river",
        False,
    ),
]


def is_lru_cache_imported_from_functools():
    func_name = "lru_cache"
    module_name = "functools"
    return (
        func_name in globals()
        and callable(globals()[func_name])
        and globals()[func_name].__module__ == module_name
    ) or module_name in globals()


def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: '{input}'")
    print(f"Expected: {expected_output}")
    result = is_palindrome(input)
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False
