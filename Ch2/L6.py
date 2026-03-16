def main_func(document: str) -> str:
    # split_lines = document.split("\n")
    filter_lambda = lambda str: not str[0] == "-" if len(str) > 0 else True
    # filtered_lines = list(filter(filter_lambda, split_lines))
    # return "\n".join(filtered_lines)
    return "\n".join(list(filter(filter_lambda, document.split("\n"))))

run_cases = [
    (
        "\n* We are the music makers\n- And we are the dreamers of dreams\n* Come with me and you'll be\n",
        "\n* We are the music makers\n* Come with me and you'll be\n",
    ),
    (
        "\n* In a world of pure imagination\n- There is no life I know\n* Living there - you'll be free\n",
        "\n* In a world of pure imagination\n* Living there - you'll be free\n",
    ),
]

submit_cases = run_cases + [
    (
        "\n* If you want to view paradise\n- Simply look around and view it\n* Anything you want to, do it\n* There is no life I know\n- To compare with pure imagination\n* Living there, you'll be free\n",
        "\n* If you want to view paradise\n* Anything you want to, do it\n* There is no life I know\n* Living there, you'll be free\n",
    ),
]