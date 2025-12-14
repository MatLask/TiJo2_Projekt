from tests.manual_test_cases import manual_test_cases

for i, case in enumerate(manual_test_cases, 1):
    print(f"{i}. Given: {case['Given']}, When: {case['When']}, Then: {case['Then']}")
