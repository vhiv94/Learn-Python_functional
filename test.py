
def test(func, test_case):
    failed = False
    input = test_case[:-1]
    expected_output = test_case[-1]
    print("---------------------------------")
    print(f"Inputs: {str(input)}")
    try:
        result = func(*input)
    except Exception as e:
        result = str(e)
    print(f"Expected: {expected_output}")
    print(f"Actual: {result}")
    if result != expected_output:
        failed = True
        print("Fail")
    else:
        print("Pass")
    passed = not failed
    return passed
    
def test_nested(func, test_cases):
    failed = False
    for case in test_cases:
        input = case[0]
        expected_output = case[-1]
        print("---------------------------------")
        print(f"Inputs: {str(input)}")
        try:
            result = func(*input)
        except Exception as e:
            result = str(e)
        print(f"Expected: {expected_output}")
        print(f"Actual:   {result}")
        if result != expected_output:
            failed = True
            print("Fail")
        else:
            print("Pass")
    passed = not failed
    return passed

def test_list(func, test_case):
    failed = False
    input = test_case[0]
    expected_output = test_case[-1]
    print("---------------------------------")
    print(f"Inputs: {str(input)}")
    try:
        result = func(*input)
    except Exception as e:
        result = str(e)
    print(f"Expected: {expected_output}")
    print(f"Actual: {result}")
    if result != expected_output:
        failed = True
        print("Fail")
    else:
        print("Pass")
    passed = not failed
    return passed

def curry_test(func, test_case):
    failed = False
    input = test_case[:-1]
    expected_output = test_case[-1]
    print("---------------------------------")
    print(f"Inputs: {str(input)}")
    try:
        result = func(input[0])(input[1])
    except Exception as e:
        result = str(e)
    print(f"Expected: {expected_output}")
    print(f"Actual: {result}")
    if result != expected_output:
        failed = True
        print("Fail")
    else:
        print("Pass")
    passed = not failed
    return passed