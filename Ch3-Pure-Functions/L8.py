def main_func(text, target_format):
    if not text or not target_format:
        raise ValueError(f"no text or target format provided")

    if target_format == "uppercase":
        return text.upper()
    if target_format == "lowercase":
        return text.lower()
    if target_format == "titlecase":
        return text.title()
    raise ValueError(f"unsupported format: {target_format}")

run_cases = [
    (
        "Through the darkness of future past",
        "uppercase",
        "THROUGH THE DARKNESS OF FUTURE PAST",
    ),
    ("The magician longs to see", "lowercase", "the magician longs to see"),
]

submit_cases = run_cases + [
    (
        "One chants out between two worlds",
        "titlecase",
        "One Chants Out Between Two Worlds",
    ),
    ("Fire walk with me", "garbagecase", "unsupported format: garbagecase"),
]