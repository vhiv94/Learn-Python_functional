def create_markdown_image(alt_text: str):
    alt_text = f"![{alt_text}]"
    def with_alt_text(url: str):
        link = f"{alt_text}({url.replace("(", "%28").replace(")", "%29")})"
        def with_title(title: str | None = None):
            if title:
                return f'{link.strip(")")} "{title}")'
            else:
                return link
        return with_title
    return with_alt_text

run_cases = [
    (
        "seal",
        "https://imgur.com/oglPAXK",
        "this is a seal",
        '![seal](https://imgur.com/oglPAXK "this is a seal")',
    ),
    (
        "cinnamon roll",
        "https://imgur.com/a/0MyOP",
        "this is a cinnamon roll",
        '![cinnamon roll](https://imgur.com/a/0MyOP "this is a cinnamon roll")',
    ),
]

submit_cases = run_cases + [
    (
        "banana",
        "https://imgur.com/nlArAKx",
        None,
        "![banana](https://imgur.com/nlArAKx)",
    ),
    (
        "not an image",
        "https://en.wikipedia.org/wiki/Variable_(computer_science)",
        "showing escape characters",
        '![not an image](https://en.wikipedia.org/wiki/Variable_%28computer_science%29 "showing escape characters")',
    ),
]


def test(alt_text, url, title, expected_output):
    print("---------------------------------")
    print("Inputs:")
    print(f"* Alt Text: {alt_text}")
    print(f"* URL: {url}")
    print(f"* Title: {title}")
    print(f"Expected: {expected_output}")
    result = create_markdown_image(alt_text)(url)()
    if title:
        result = create_markdown_image(alt_text)(url)(title)
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False