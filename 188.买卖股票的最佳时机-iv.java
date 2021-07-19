/*
 * @lc app=leetcode.cn id=188 lang=java
 *
 * [188] 买卖股票的最佳时机 IV
 */

// @lc code=start
class Solution {
    public int maxProfit(int k, int[] prices) {
        // 动态规划，定义二维数组dp[i][j]，j:0,1,2,3,4,2*k，1，2，3，4分别表示第1次买入，第一次卖出，第二次买入，第二次卖出，后续类推
        // 二维数组的值表示当前情况下的最大现金
        if (prices.length == 0) {
            return 0;
        }
        int[][] profits = new int[prices.length][2*k+1];
        profits[0][0] = 0;
        for (int i = 1; i < 2*k; i+=2) {
            profits[0][i] = -prices[0];
        }

        for (int i = 1; i < prices.length; i++) {
            for (int j = 0; j < 2*k-1; j+=2) {
                profits[i][j+1] = Math.max(profits[i-1][j+1], profits[i-1][j]-prices[i]);
                profits[i][j+2] = Math.max(profits[i-1][j+2], profits[i-1][j+1]+prices[i]);
            }
        }
        return profits[prices.length-1][2*k];
    }
}
// @lc code=end

