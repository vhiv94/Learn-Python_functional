
def test(func, test_case):
    input = test_case[:-1]
    expected_output = test_case[-1]
    print("---------------------------------")
    print(f"Inputs: {input}")
    print(f"Expected: {expected_output}")
    try:
        actual_output = func(*input)
        print(f"Actual: {actual_output}")
        if actual_output == expected_output:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print(e)


def run_tests(func, test_cases):
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(func, test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")
