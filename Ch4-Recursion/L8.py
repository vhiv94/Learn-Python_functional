def main_func(lst: list) -> int:
    result: int = 0
    for item in lst:
        if type(item) == int: 
            result += item
        else:
            result += main_func(item)
    return result

run_cases = [
    ([1, 2, [3, 4]], 10),
    ([5, [6, 7], [[8, 9], 10]], 45),
]

submit_cases = run_cases + [
    ([], 0),
    ([1, [2], [3, [4, [5, [6, [7, [8, [9, [10]]]]]]]]], 55),
]