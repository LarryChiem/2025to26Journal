from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # space complexity is O(n)
        res = []
        # Check for empty intervals
        if not intervals:
            return res

        # First, sort the intervals by x: x[0].
        # Time complexity is O(nlogn) where n is the number of intervals
        intervals.sort(key=lambda x: x[0])

        prev_start, prev_end = intervals[0]

        # Time complexity O(n)
        for cur_start, cur_end in intervals[1:]:
            # merge
            if cur_start <= prev_end:
                prev_end = max(prev_end, cur_end)
            # don't merge
            else:
                res.append([prev_start, prev_end])
                prev_start, prev_end = cur_start, cur_end

        # now, we are left with the last [prev_start, prev_end]
        res.append([prev_start, prev_end])
        return res
