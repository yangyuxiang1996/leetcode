/*
 * @lc app=leetcode.cn id=122 lang=java
 *
 * [122] 买卖股票的最佳时机 II
 */

// @lc code=start
class Solution {
    public int maxProfit0(int[] prices) {
        // 贪心
        int max_profit = 0;
        for (int i = 1; i < prices.length; i++) {
            max_profit += Math.max(prices[i]-prices[i-1], 0);
        }
        return max_profit;
    }

    public int maxProfit1(int[] prices) {
        // 动态规划
        int[] dp = new int[prices.length];
        dp[0] = 0;
        for (int i = 1; i < prices.length; i++) {
            dp[i] = Math.max(dp[i-1], dp[i-1]+prices[i]-prices[i-1]);
        }
        return dp[prices.length-1];
    }

    public int maxProfit(int[] prices) {
        // 动态规划
        int[][] dp = new int[prices.length][2];
        dp[0][0] = -prices[0];
        dp[0][1] = 0;

        for (int i = 1; i < prices.length; i++) {
            dp[i][0] = Math.max(dp[i-1][0], dp[i-1][1]-prices[i]);  // 注意这里与上一题的区别，买入股票之前必须从上一天未持有股票的时候开始
            dp[i][1] = Math.max(dp[i-1][1], dp[i-1][0]+prices[i]);
        }
        return dp[prices.length-1][1];
    }

}
// @lc code=end

