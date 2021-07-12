#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        min_price = prices[0]
        profit = 0
        for i in range(1, n):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] >= min_price and prices[i] <= min_price+fee:
                continue
            if prices[i] > min_price+fee:
                profit += prices[i] - min_price - fee
                min_price = prices[i] - fee  # 继续持有，相当于反向加上每一天的手续费
        return profit


if __name__ == '__main__':
    prices = [1,3,2,8,4,9]
    fee = 2
    print(Solution().maxProfit(prices, fee))
# @lc code=end

