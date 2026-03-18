def main_func(font_sizes):
    if len(font_sizes) == 0:
        return None
    sorted_list = sorted(font_sizes)
    median_index = (len(sorted_list) - 1) // 2
    return sorted_list[median_index]

run_cases = [
    ([4, 3, 2, 1, 5], 3),
    ([20, 14, 16], 16),
    ([9, 11, 16, 20], 11),
    ([], None),
]

submit_cases = run_cases + [
    ([8, 8, 8], 8),
    ([30, 18, 14, 22], 18),
    ([6, 24, 6, 6, 24, 24, 2, 1, 3], 6),
]