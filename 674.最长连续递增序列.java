/*
 * @lc app=leetcode.cn id=674 lang=java
 *
 * [674] 最长连续递增序列
 */

// @lc code=start
class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int res = 1;
        int tmp = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] > nums[i-1]) {
                tmp += 1;
            } else {
                tmp = 1;
            }
            res = Math.max(res, tmp);
        }

        return res;
        

    }
}
// @lc code=end

