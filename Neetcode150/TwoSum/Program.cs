/*
   LeetCode 1 — Two Sum

   Given an array of integers nums and an integer target,
   return indices of the two numbers such that they add up to target.

Assumptions:
- Exactly one solution exists
- Cannot use the same element twice

Example:
nums = [2,7,11,15], target = 9
=> [0,1]

Pattern: Hash Map
Time: O(n)
Space: O(n)
*/
using System;

class Program
{
    static void Main()
    {
        RunTest(new[] { 2, 7, 11, 15 }, 9);
        RunTest(new[] { 3, 2, 4 }, 6);
        RunTest(new[] { 3, 3 }, 6);

        Console.WriteLine("All tests passed.");
    }

    static void RunTest(int[] nums, int target)
    {
        var result = Solution.TwoSum(nums, target);

        if (nums[result[0]] + nums[result[1]] != target)
            throw new Exception("Test failed");
    }
}
