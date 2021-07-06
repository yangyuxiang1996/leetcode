/*
 * @lc app=leetcode.cn id=53 lang=java
 *
 * [53] 最大子序和
 */

// @lc code=start
class Solution {
    public int maxSubArray(int[] nums) {
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
}
// @lc code=end

