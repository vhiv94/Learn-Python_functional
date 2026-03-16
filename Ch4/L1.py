def main_func(x):
    if x <= 0:
        return 1
    return x * main_func(x - 1)

run_cases = [
    (3, 6),
    (5, 120),
    (0, 1),
]

submit_cases = run_cases + [
    (1, 1),
    (2, 2),
    (10, 3628800),
]