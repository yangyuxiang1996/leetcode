import java.util.Stack;

/*
 * @lc app=leetcode.cn id=123 lang=java
 *
 * [123] 买卖股票的最佳时机 III
 */

// @lc code=start
class Solution {
    // public static void main(String[] args) {
    //     int[] prices = {1,2,4,2,5,7,2,4,9,0};
    //     System.out.println(new MaxProfit().maxProfit(prices));
    // }
    public int maxProfit(int[] prices) {
        int[] profits = new int[prices.length]; // 保存到第i天的最大利润
        int cur_min = prices[0];
        int max_profit = Integer.MIN_VALUE;
        for (int i = 1; i < prices.length; i++) {
            cur_min = Math.min(cur_min, prices[i]);
            max_profit = Math.max(max_profit, prices[i]-cur_min);
            profits[i] = max_profit;
        }

        int total_max = 0;
        max_profit = 0;
        int cur_max = prices[prices.length-1];
        for (int i = prices.length - 1; i >= 0; i--) {
            cur_max = Math.max(cur_max, prices[i]);
            max_profit = Math.max(max_profit, cur_max - prices[i]);
            total_max = Math.max(total_max, profits[i] + max_profit);
        }

        return total_max;
    }
}
// @lc code=end

