from solution import Solution

def run_tests():
    obj = Solution()

    test_num = 1
    nums1 = [1, 3]
    nums2 = [2]
    expected = 2.0000
    actual = obj.findMedianSortedArrays(nums1, nums2)

    assert actual == expected, (
        f"Test {test_num} failed, findMedianSortedArrays({nums1}, {nums2}) expected {expected} but returned {actual}."
    )

    test_num = 2
    nums1 = [1, 2]
    nums2 = [3, 4]
    expected = 2.5000
    actual = obj.findMedianSortedArrays(nums1, nums2)

    assert actual == expected, (
        f"Test {test_num} failed, findMedianSortedArrays({nums1}, {nums2}) expected {expected} but returned {actual}."
    )

    print(f"All {test_num} tests passed successfully!")

run_tests()