def main_func(hex_color):
    if not is_hexadecimal(hex_color) or not len(hex_color) == 6: 
        raise Exception("not a hex color string")

    r = int(hex_color[:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:], 16)
    return r, g, b

def is_hexadecimal(hex_string):
    try:
        int(hex_string, 16)
        return True
    except Exception:
        return False

run_cases = [
    (
        "00FFFF",
        (0, 255, 255),
    ),
    (
        "FFFF00",
        (255, 255, 0),
    ),
    (
        "Hello!",
        None,
    ),
    (
        "42",
        None,
    ),
    (
        1_000_000,
        None,
    ),
]

submit_cases = run_cases + [
    (
        "",
        None,
    ),
    (
        "FF00FF",
        (255, 0, 255),
    ),
    (
        "000000",
        (0, 0, 0),
    ),
    (
        "FFFFFF",
        (255, 255, 255),
    ),
]