from typing import Callable


type Replacer = Callable[[str], str]
type Wrapper = Callable[[str], Replacer]
type Replacer_Factory = Callable[[Replacer], Wrapper]

def replacer(old: str, new: str) -> Replacer_Factory:
    def replace(decorated_func: Replacer) -> Wrapper:
        def wrapper(text: str) -> Replacer:
            return decorated_func(text.replace(old, new))

        return wrapper
        
    return replace


@replacer("&", "&amp;")
@replacer("<", "&lt;")
@replacer(">", "&gt;")
@replacer('"', "&quot;")
@replacer("'", "&#x27;")
def tag_pre(text: str) -> str:
    return f"<pre>{text}</pre>"

run_cases = [
    (
        replacer("faith", "salmon")(lambda x: x),
        'replacer("faith", "salmon")(lambda x: x)',
        "I find your lack of faith disturbing, young Skywalker.",
        "I find your lack of salmon disturbing, young Skywalker.",
    ),
    (
        replacer("paragraph", "span")(replacer("p>", "span>")(lambda x: x)),
        'replacer("paragraph", "span")(replacer("p>", "span>")(lambda x: x))',
        "<p>Here is a paragraph</p>",
        "<span>Here is a span</span>",
    ),
    (
        tag_pre,
        "tag_pre",
        '<a href="https://www.boot.dev/blog/wiki/troubleshoot-code-editor-issues/">link</a>',
        "<pre>&lt;a href=&quot;https://www.boot.dev/blog/wiki/troubleshoot-code-editor-issues/&quot;&gt;link&lt;/a&gt;</pre>",
    ),
]

submit_cases = run_cases + [
    (
        tag_pre,
        "tag_pre",
        '<img src="https://imgur.com/a/VlMAK0B" alt="mystery">',
        "<pre>&lt;img src=&quot;https://imgur.com/a/VlMAK0B&quot; alt=&quot;mystery&quot;&gt;</pre>",
    ),
    (
        tag_pre,
        "tag_pre",
        "<p>This paragraph has <em>italic text</em></p>",
        "<pre>&lt;p&gt;This paragraph has &lt;em&gt;italic text&lt;/em&gt;&lt;/p&gt;</pre>",
    ),
]


def test(func, func_name, input, expected_output):
    print("---------------------------------")
    print(f"Function: {func_name}")
    print(f"    Input: {input}")
    print(f"Expected: {expected_output}")
    result = func(input)
    print(f"Actual:   {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False