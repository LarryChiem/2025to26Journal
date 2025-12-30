using System;

class Program
{
    static void Main()
    {
        int[] nums = { 2, 7, 11, 15 };
        int target = 9;

        int[] result = Solution.TwoSum(nums, target);

        if (nums[result[0]] + nums[result[1]] != target)
            throw new Exception("Test failed");

        Console.WriteLine("Test passed!");
    }
}
