# from test import test_nested, curry_test
from Ch8.L4 import submit_cases, test

def main():
    passed = 0
    failed = 0
    for test_case in submit_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")

# def transform(test_case):
#     passed = False
#     for test_case in submit_cases:
#         func1 = test_case[0]
#         func2 = test_case[1]
#         test_cases = test_case[2]
#         print("---------------------------------")
#         print(f"Input functions: {func1.__name__} and {func2.__name__}")
#         func = main_func(func1, func2)
#         passed = test_nested(func, test_cases)
#     return passed


if __name__ == "__main__":
    main()
