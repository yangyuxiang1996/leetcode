/*
 * @lc app=leetcode.cn id=279 lang=java
 *
 * [279] 完全平方数
 */

// @lc code=start
class Solution {
    public int numSquares(int n) {
        // 完全背包问题
        if (n == 1) {
            return 1;
        }
        int max = Integer.MAX_VALUE;
        int[] dp = new int[n+1];
        for (int i = 0; i < n+1; i++) {
            dp[i] = max;
        }
        dp[0] = 0;

        for (int i = 1; i * i <= n; i++) {
            for (int j = i * i; j < n+1; j++) {
                if (dp[j - i * i] != max){
                    dp[j] = Math.min(dp[j], dp[j-i*i]+1);
                }
            }
        }

        return dp[n];

    }
}
// @lc code=end

