/*
 * @lc app=leetcode.cn id=70 lang=java
 *
 * [70] 爬楼梯
 */

// @lc code=start
class Solution {
    public int climbStairs0(int n) {
        // f[n] = f[n-2] + 2
        if (n == 1) {
            return 1;
        }
        int[] dp = new int[n + 1];
        dp[1] = 1;
        dp[2] = 2;
        for (int i=3; i < n+1; i++) {
            dp[i] = dp[i-2] + dp[i-1];
        }
        return dp[n];

    }

    public int climbStairs(int n) {
        // 当成完全背包来做

        int[] dp = new int[n+1];
        dp[0] = 1;

        for (int j=1; j < n+1; j++) {
            for (int i=1; i <= 2; i++) {
                if (j - i >= 0){
                    dp[j] += dp[j-i];
                }
            }
        }
        return dp[n];
    }
}
// @lc code=end

