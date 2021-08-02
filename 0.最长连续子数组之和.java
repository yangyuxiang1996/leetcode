/*
 * @lc app=leetcode.cn id=152 lang=java
 *
 * [152] 乘积最大子数组
 */

// @lc code=start
class Solution {
    public int maxSum(int[] nums) {
        if (nums.length == 1) {
            return nums[0];
        }
        int res = Integer.MIN_VALUE;
        int cur = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] < 0) {
                cur = 0;
            } else {
                cur += nums[i];
            }
            res = Math.max(res, cur);
        }
        return res;

    }
}
// @lc code=end

