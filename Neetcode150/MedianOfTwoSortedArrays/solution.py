from typing import Optional, List
# 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
# Example 1:
#
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) ->float:
        total = len(nums1) + len(nums2)
        half = total // 2

        # Swap A and B if B is longer than A so that we can start binary search on the smaller array
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        # Initialize l, r pointers for binary search on A
        l, r = 0, len(A) - 1

        while True:
            # Get the mid-point of A (i) and mid-point of B (j)
            i = (l + r) // 2
            j = (half - i - 2)

            INF = 10**18
            # Get both 'mid' points of A and B and checking boundary
            Aleft = A[i] if i >= 0 else -INF
            Aright = A[i + 1] if i + 1 < len(A) else INF
            Bleft = B[j] if j >= 0 else -INF
            Bright = B[j + 1] if j + 1 < len(B) else INF

            # Partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2: # If odd length, return the min of the two right-side partitions
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # Aright partition is too large, check left partition of A
            elif Aright > Bleft:
                r = i - 1

            # Aright partition is too small, check right partition of A
            else:
                l = i + 1