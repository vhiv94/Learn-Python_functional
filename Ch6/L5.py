from copy import deepcopy
from typing import Callable

'''
#Assignment#
Complete the css_styles function. 
It accepts:
- initial_styles: a nested dictionary

It returns:
- add_style: a function

The css_styles function should:
1. Copy initial_styles to avoid modifying the original dictionary.

    ## Because we're dealing with nested dictionaries here, the .copy() method 
    # will produce a shallow copy: the outer dict is a new object, but mutating 
    # inner dicts will still affect the original one. So, you should import copy 
    # and use copy.deepcopy() instead.

2. Return an add_style function that:
    1. Takes three string arguments: selector, property, and value. selector is a key in 
       the initial_styles dictionary and its value should be a dictionary.
    2. Checks if the selector exists in the dictionary. If not, creates a new dictionary 
       for the selector value.
    3. Then adds or updates the property with the given value for the selector dictionary.
    4. Returns the updated dictionary.
'''
def css_styles(initial_styles: dict) -> Callable[[str, str, str], dict]:
    styles: dict = deepcopy(initial_styles)
    def add_style(selector: str, property: str, value: str) -> dict:
        nonlocal styles
        if selector not in styles:
            styles[selector] = {}
        styles[selector][property] = value
        return styles
    return add_style

run_cases = [
    (
        {
            "h1": {
                "color": "yellow",
            },
            "body": {
                "background-color": "black",
                "color": "white",
            },
        },
        [
            ("h1", "color", "#CC00FF"),
            ("body", "background-color", "#696969"),
        ],
        {
            "h1": {
                "color": "#CC00FF",
            },
            "body": {
                "background-color": "#696969",
                "color": "white",
            },
        },
    ),
]


submit_cases = run_cases + [
    (
        {},
        [
            ("p", "font-size", "16px"),
        ],
        {
            "p": {
                "font-size": "16px",
            },
        },
    ),
    (
        {
            ".container": {
                "max-width": "1200px",
                "margin": "0 auto",
                "padding": "0 20px",
            },
        },
        [
            (".container", "max-width", "1450px"),
            (".container", "color", "#660099"),
        ],
        {
            ".container": {
                "max-width": "1450px",
                "margin": "0 auto",
                "padding": "0 20px",
                "color": "#660099",
            },
        },
    ),
]


def test(initial_styles, styles_to_add, expected_output):
    print("---------------------------------")
    print(f"Initial styles: {initial_styles}")
    initial_styles_copy = deepcopy(initial_styles)
    add_style = css_styles(initial_styles)
    result = initial_styles.copy()
    for style in styles_to_add:
        print(f"Style to add: {style}")
        result = add_style(*style)
    print(f"Expected: {expected_output}")
    print(f"Actual:   {result}")
    if initial_styles_copy != initial_styles:
        print("Fail: You should not modify the initial styles")
        return False
    if result != expected_output:
        print("Fail: Unexpected result")
        return False
    print("Pass")
    return True


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
