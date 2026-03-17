def main_func(filter_one, filter_two):
    def filter_cmd(content: str, option: str = "--one"):
        match option:
            case "--one":
                return filter_one(content)
            case "--two":
                return filter_two(content)
            case "--three":
                return filter_two(filter_one(content))
            case _:
                raise Exception("invalid option")
    return filter_cmd


# don't touch below this line


def replace_bad(text):
    return text.replace("bad", "good")


def replace_ellipsis(text):
    return text.replace("..", "...")


def fix_ellipsis(text):
    return text.replace("....", "...")


run_cases = [
    (
        replace_bad,
        replace_ellipsis,
        [
            (
                (
                    "I'm bad, and that's good. I will never be good, and that's not bad..",
                ),
                "I'm good, and that's good. I will never be good, and that's not good..",
            ),
            (
                (
                    "I'm bad, and that's good. I will never be good, and that's not bad..",
                    "--one",
                ),
                "I'm good, and that's good. I will never be good, and that's not good..",
            ),
            (
                (
                    "I'm bad, and that's good. I will never be good, and that's not bad..",
                    "--two",
                ),
                "I'm bad, and that's good. I will never be good, and that's not bad...",
            ),
            (
                (
                    "I'm bad, and that's good. I will never be good, and that's not bad..",
                    "--three",
                ),
                "I'm good, and that's good. I will never be good, and that's not good...",
            ),
        ],
    ),
]

submit_cases = run_cases + [
    (
        replace_ellipsis,
        fix_ellipsis,
        [
            (
                (
                    "There's no place like home.. but sometimes, it's nice to get away... and explore....",
                ),
                "There's no place like home... but sometimes, it's nice to get away.... and explore......",
            ),
            (
                (
                    "There's no place like home.. but sometimes, it's nice to get away... and explore....",
                    "--one",
                ),
                "There's no place like home... but sometimes, it's nice to get away.... and explore......",
            ),
            (
                (
                    "There's no place like home.. but sometimes, it's nice to get away... and explore....",
                    "--two",
                ),
                "There's no place like home.. but sometimes, it's nice to get away... and explore...",
            ),
            (
                (
                    "There's no place like home.. but sometimes, it's nice to get away... and explore....",
                    "--three",
                ),
                "There's no place like home... but sometimes, it's nice to get away... and explore.....",
            ),
            (
                (
                    "There's no place like home.. but sometimes, it's nice to get away... and explore....",
                    "",
                ),
                "invalid option",
            ),
        ],
    ),
]

'''
Assignment
Complete the get_filter_cmd function. It takes two functions as input, 
filter_one and filter_two, and returns a function, filter_cmd.

filter_cmd should take as input two strings: content and option.

1. Set the default value of the option argument to "--one".
2. Complete filter_cmd so that it filters and returns the content according to the input option.
    1. If "--one", use filter_one
    2. If "--two", use filter_two
    3. If "--three", use filter_one first, then use filter_two
    4. If another option is passed, raise an exception, "invalid option"
'''