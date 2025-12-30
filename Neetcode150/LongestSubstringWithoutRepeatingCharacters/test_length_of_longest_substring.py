# run once 'pip install pytest'
# To run this test, run 'pytest -q'

# Given a string s, find the length of the longest substring without duplicate characters.
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
    obj = Solution()
    actual = obj.length_of_longest_substring(s)

    assert expected == actual