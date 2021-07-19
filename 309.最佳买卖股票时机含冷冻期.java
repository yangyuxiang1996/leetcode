/*
 * @lc app=leetcode.cn id=309 lang=java
 *
 * [309] 最佳买卖股票时机含冷冻期
 */

// @lc code=start
class Solution {

    // public static void main(String[] args) {
    //     int[] prices = {1,2,3,0,2};
    //     System.out.println(new MaxProfit().maxProfit(prices));
    // }

    public int maxProfit(int[] prices) {
        // 动态规划
        if (prices.length == 0) {
            return 0;
        }
        int[][] profits = new int[prices.length][3];
        profits[0][0] = -prices[0];
        profits[0][1] = 0;
        profits[0][2] = 0;

        for (int i = 1; i < prices.length; i++) {
            profits[i][0] = Math.max(profits[i-1][0], profits[i-1][2]-prices[i]);
            profits[i][1] = Math.max(profits[i-1][1], profits[i-1][0]+prices[i]);
            profits[i][2] = Math.max(profits[i-1][2], profits[i-1][1]);
        }
        return profits[prices.length-1][1];


    }
}
// @lc code=end

