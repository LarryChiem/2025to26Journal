from solution import Solution

def run_tests():
    obj = Solution()

    test_num = 1
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    expected = 20
    actual = obj.minCostConnectPoints(points)

    assert actual == expected, (
        f"Test {test_num} failed, minCostConnectPoints({points}) expected {expected} but returned {actual}."
    )

    test_num += 1
    points = [[3, 12], [-2, 5], [-4, 1]]
    expected = 18
    actual = obj.minCostConnectPoints(points)

    assert actual == expected, (
        f"Test {test_num} failed, minCostConnectPoints({points}) expected {expected} but returned {actual}."
    )

    print(f"All {test_num} tests passed successfully!")

run_tests()