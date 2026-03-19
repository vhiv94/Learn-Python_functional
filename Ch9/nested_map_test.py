data =  [
            ["Customer ID", "Billed", "Paid"],
            [1, 100, 100],
            [2, 400, 99],
            [3, 50, 25],
        ]

str_list: list[list[str]] = list(map(lambda in_list: list(map(lambda val: str(val), in_list)), data))
csv_str = "\n".join(list(map(", ".join, str_list)))
print("\n".join(map(lambda in_list: ",".join(map(lambda val: str(val), in_list)), data)))