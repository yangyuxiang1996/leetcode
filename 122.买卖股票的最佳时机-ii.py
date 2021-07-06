#
# @lc app=leetcode.cn id=122 lang=python
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        利润可以拆解为每一天的利润之和
        """
        profits = [0] * len(prices)

        for i in range(1, len(prices)):
            profits[i] = max(prices[i] - prices[i-1], profits[i])

        return sum(profits)

        

# @lc code=end

