"""
1. Two Sum
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.
"""  # run once 'pip install pytest'
# To run this test, run 'pytest -q'
import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_two_sum(nums, target, expected):
    """Test two sum."""
    obj = Solution()
    actual = obj.two_sum(nums, target)

    # If your method might return indices in either order, compare as sets:
    assert sorted(actual) == sorted(expected)
