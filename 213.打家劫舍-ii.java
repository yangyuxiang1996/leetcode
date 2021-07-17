/*
 * @lc app=leetcode.cn id=213 lang=java
 *
 * [213] 打家劫舍 II
 */

// @lc code=start
class Solution {
    public int rob(int[] nums) {
        // 分两种情况，要不要先偷第一家，最后看两种方式哪种更大
        if (nums.length == 1) {
            return nums[0];
        }
        if (nums.length == 2) {
            return Math.max(nums[0], nums[1]);
        }
        return Math.max(rob(nums, 0, nums.length-1), rob(nums, 1, nums.length));

    }

    public int rob(int[] nums, int start, int end) {
        int[] dp = new int[end];
        dp[start] = nums[start];
        dp[start+1] = Math.max(nums[start], nums[start+1]);
        for (int i = start+2; i < end; i++) {
            dp[i] = Math.max(dp[i-2]+nums[i], dp[i-1]);
        }
        return dp[end-1];
    }
}
// @lc code=end

