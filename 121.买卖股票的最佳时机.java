/*
 * @lc app=leetcode.cn id=121 lang=java
 *
 * [121] 买卖股票的最佳时机
 */

// @lc code=start
class Solution {
    public int maxProfit0(int[] prices) {
        // 贪心
        int max_profit = 0;
        int min_price = Integer.MAX_VALUE;
        for (int i = 0; i < prices.length; i++) {
            min_price = Math.min(min_price, prices[i]);
            max_profit = Math.max(max_profit, prices[i]-min_price);
        }

        return max_profit;

    }
    public int maxProfit(int[] prices) {
        // 动态规划
        // dp[i][0]表示第i天持有股票所得最多现金；dp[i][1]表示第i天不持有股票所得最多现金
        int[][] dp = new int[prices.length][2];
        dp[0][0] = -prices[0];
        dp[0][1] = 0;

        for (int i = 1; i < prices.length; i++) {
            dp[i][0] = Math.max(dp[i-1][0], -prices[i]);
            dp[i][1] = Math.max(dp[i-1][1], dp[i-1][0]+prices[i]);
        }

        return dp[prices.length - 1][1];



    }
}
// @lc code=end

