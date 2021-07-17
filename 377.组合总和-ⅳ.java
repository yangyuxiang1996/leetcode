/*
 * @lc app=leetcode.cn id=377 lang=java
 *
 * [377] 组合总和 Ⅳ
 * 完全背包问题
 */

// @lc code=start
class Solution {
    public int combinationSum4(int[] nums, int target) {
        if (target == 0) {
            return 1;
        }
        if (nums.length == 0) {
            return 0;
        }

        int[] dp = new int[target+1];
        dp[0] = 1;
        for (int j = 1; j < target+1; j++) { // 注意这里的遍历顺序，因为是排列，所以先遍历容量，再遍历物品
            for (int i = 0; i < nums.length; i++) {
                if (j - nums[i] >= 0) {
                    dp[j] += dp[j-nums[i]];
                } else {
                    dp[j] = dp[j];
                }
            }
        }
        return dp[target];

    }
}
// @lc code=end

