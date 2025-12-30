using System;
using System.Collections.Generic;

public class Solution
{
    public static int[] TwoSum(int[] nums, int target)
    {
        Dictionary<int, int> map = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++)
        {
            int complement = target - nums[i];

            if (map.ContainsKey(complement))
            {
                return new int[] { map[complement], i };
            }

            // store value -> index
            map[nums[i]] = i;
        }

        return new int[0]; // or throw exception if guaranteed solution exists
    }
}
