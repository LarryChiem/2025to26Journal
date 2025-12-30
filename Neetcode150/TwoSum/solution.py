from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for i, val in enumerate(nums):
            complement = target - val
            if complement in index_map:
                return [index_map[complement], i]
            index_map[val] = i
