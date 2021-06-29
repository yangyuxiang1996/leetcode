#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-20 14:24:18
LastEditors: yangyuxiang
LastEditTime: 2021-04-20 16:12:39
FilePath: /leetcode/322.零钱兑换.py
'''
#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
class Solution:
    def coinChange(self, coins, amount):
        memo = {}
        def helper(amount):
            if amount in memo:
                return memo[amount]
            if amount < 0:
                return -1
            if amount == 0:
                return 0

            cnt = float("inf")
            for coin in coins:
                sub = helper(amount-coin)
                if sub == -1:
                    continue
                cnt = min(cnt, sub + 1)

            memo[amount] = cnt if cnt != float("inf") else -1
            return memo[amount]
        
        return helper(amount)

    def coinChange1(self, coins, amount):
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 


if __name__ == "__main__":
    coins = [1,2,5]
    amount = 11
    print(Solution().coinChange(coins, amount))
# @lc code=end

