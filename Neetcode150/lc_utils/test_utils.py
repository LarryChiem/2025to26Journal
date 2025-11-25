def run_tests(test_cases):
    """
    test_cases: list of (callable, description)
    Each callable should raise AssertionError on failure or return None on success.
    """
    total = len(test_cases)
    for idx, (test_func, desc) in enumerate(test_cases, start=1):
        try:
            test_func()
            print(f"✅ Test {idx}/{total}: {desc}")
        except AssertionError as e:
            print(f"❌ Test {idx}/{total}: {desc}")
            print("   ", e)
            return

    print(f"\n🎉 All {total} tests passed!")
