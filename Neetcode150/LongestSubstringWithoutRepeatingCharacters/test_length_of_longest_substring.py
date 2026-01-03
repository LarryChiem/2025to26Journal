""" 3. Longest Substring Without Repeating Characters
Medium
Given a string s, find the length of the longest substring without duplicate characters.
"""
# run once 'pip install pytest'
# To run this test, run 'pytest -q'

# Description
# The input will be a list of integers, each separated by a newline character.
# The first line of the input will be an integer N (1 <= N <= 100), indicating the number of test cases to follow.
# Each of the test cases will consist of a line with an integer X (0 < X <= 100), followed by another line consisting of X number of space-separated integers Yn (-100 <= Yn <= 100).
# For each test case, calculate the power of four of Yn, excluding when Yn is positive, and print the calculated sum in the output.
# Notes
# There should be no output until all the input has been received.
# Do not put blank lines between test cases solutions.
# Take input from standard input, and output to standard output.
# There will be no EOF.
# The final output is guaranteed to be within the int32 range.
# It is possible that X and the number of integers Yn may not be equal. If that is the case, print -1 as the output.

# Sample Input
# 2 # The first line of the input will be an integer N (1 <= N <= 100), indicating the number of test cases to follow.
# 4 # Each of the test cases will consist of a line with an integer X (0 < X <= 100), followed by another line consisting of X number of space-separated integers Yn (-100 <= Yn <= 100).
# 3 -1 1 10
# 5
# 9 -5 -5 -10 10
# Sample Output
# 1
# 11250
import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "s,expected",
    [
        ("abcabcbb", 3),
        ("bbbb", 1),
        ("pwwke", 3),
    ],
)
def test_length_of_longest_substring(s: str, expected: int) -> None:
    """Test longest substring without repeating characters."""
    obj = Solution()
    actual = obj.length_of_longest_substring(s)

    assert expected == actual
