/*
 * @lc app=leetcode.cn id=518 lang=java
 *
 * [518] 零钱兑换 II
 */

// @lc code=start
class Solution {
    public int change(int amount, int[] coins) {
        // 完全背包问题
        if (amount == 0) {
            return 1;
        }
        if (coins.length == 0) {
            return 0;
        }

        int[] dp = new int[amount+1];
        dp[0] = 1;
        for (int i = 0; i < coins.length; i++) {
            for (int j = coins[i]; j < amount+1; j++) {
                dp[j] += dp[j-coins[i]];
            }
        }
        return dp[amount];

    }
}
// @lc code=end

