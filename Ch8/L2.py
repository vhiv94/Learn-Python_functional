def args_logger (*args, **kwargs):
    for i in range(len(args)):
        print(f"{i}. {args[i]}")
    for arg in kwargs:
        print(f"* {arg}: {kwargs[arg]}")


def test(*args, **kwargs):
    args_logger(*args, **kwargs)
    print("========================================")


def main():
    print("--- Test 1: Mix of args & kwargs -------")
    test("Good", "riddance", date_str="01/01/2023")

    print("--- Test 2: Only kwargs ----------------")
    test(message="Hello World", to_delete="l")

    print("--- Test 3: Only args ------------------")
    test("two", "star-crossed", "lovers")

    print("--- Test 4: Mix of args & kwargs -------")
    test("hi", True, f_name="Lane", l_name="Wagner", age=28)


main()
