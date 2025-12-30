from solution import Solution


def run_tests():
    obj = Solution()

    test_num = 1
    s = "babad"
    expected = "bab"

    actual = obj.longestPalindrome(s)

    assert (
        actual == expected
    ), f"Test {test_num} failed, longestPalindrome({s}) expected {expected} but returned {actual}."

    test_num += 1
    s = "cbbd"
    expected = "bb"

    actual = obj.longestPalindrome(s)

    assert (
        actual == expected
    ), f"Test {test_num} failed, longestPalindrome({s}) expected {expected} but returned {actual}."

    print(f"All {test_num} tests passed successfully!")


run_tests()
