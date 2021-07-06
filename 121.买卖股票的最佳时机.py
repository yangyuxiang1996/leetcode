#
# @lc app=leetcode.cn id=121 lang=python
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # res = 0
        # right = [0] * len(prices)
        # right[-1] = prices[-1]

        # for i in range(len(prices)-2, -1, -1):
        #     right[i] = max(prices[i], right[i+1])
        
        # for i in range(len(prices)):
        #     res = max(res, max(right[i]-prices[i], 0))

        # return res

        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)

        return max_profit


if __name__ == '__main__':
    prices = [1,2,3,4,5]
    print(Solution().maxProfit(prices))
# @lc code=end

