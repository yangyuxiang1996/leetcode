import java.util.Arrays;

/*
 * @lc app=leetcode.cn id=53 lang=java
 *
 * [53] 最大子序和
 */

// @lc code=start
class Solution {
    public int maxSubArray0(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }

        int maxSum = Integer.MIN_VALUE;
        int tmp = 0;
        for (int i = 0; i < nums.length; i++) {
            
            tmp = Math.max(nums[i], tmp+nums[i]);
            maxSum = Math.max(maxSum, tmp);
            
        }

        return maxSum;
    }

    public int maxSubArray(int[] nums) {
        // dp
        if (nums.length == 0) {
            return 0;
        }
        if (nums.length == 1) {
            return nums[0];
        }

        int[] dp = new int[nums.length];
        dp[0] = nums[0];
        int max = nums[0];
        for (int i = 1; i < dp.length; i++) {
            dp[i] = Math.max(nums[i], dp[i-1] + nums[i]);
            max = Math.max(max, dp[i]);
        }
        return max;
    }
}
// @lc code=end

