
def test(func, test_case):
    input = test_case[:-1]
    expected_output = test_case[-1]
    print("---------------------------------")
    print(f"Inputs: {input}")
    print(f"Expected: {expected_output}")
    actual_output = func(input)
    print(f"Actual: {actual_output}")
    if actual_output == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False


def run_tests(func, test_cases, submit_cases, _submit_):
    if _submit_:
        test_cases = submit_cases
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
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
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")