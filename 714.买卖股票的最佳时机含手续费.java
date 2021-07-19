/*
 * @lc app=leetcode.cn id=714 lang=java
 *
 * [714] 买卖股票的最佳时机含手续费
 */

// @lc code=start
class Solution {
    public int maxProfit(int[] prices, int fee) {
        // 动态规划
        if (prices.length == 0) {
            return 0;
        }

        int[][] profits = new int[prices.length][2];
        profits[0][0] = -prices[0]-fee;
        profits[0][1] = 0;

        for (int i = 1; i < prices.length; i++) {
            profits[i][0] = Math.max(profits[i-1][0], profits[i-1][1]-prices[i]-fee);
            profits[i][1] = Math.max(profits[i-1][1], profits[i-1][0]+prices[i]);
        }
        return profits[prices.length-1][1];

    }
}
// @lc code=end

