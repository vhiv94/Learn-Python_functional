data =  [
            ["Customer ID", "Billed", "Paid"],
            [1, 100, 100],
            [2, 400, 99],
            [3, 50, 25],
        ]

print(list(map(lambda in_list: list(map(lambda val: str(val), in_list)), data)))