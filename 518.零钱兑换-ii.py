#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-30 10:40:31
LastEditors: yangyuxiang
LastEditTime: 2021-04-30 17:54:51
FilePath: /leetcode/518.零钱兑换-ii.py
'''
#
# @lc app=leetcode.cn id=518 lang=python
#
# [518] 零钱兑换 II
#

# @lc code=start
class Solution(object):
    def change1(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        dp = [[0] * (amount+1) for _ in range(len(coins)+1)]
        for i in range(len(dp)):
            dp[i][0] = 1  # amount为0时，无为而治

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                w1 = dp[i-1][j]
                if j - coins[i-1] < 0:
                    dp[i][j] = w1
                else:
                    w2 = dp[i][j-coins[i-1]]
                    dp[i][j] = w1 + w2
        
        return dp[len(coins)][amount] 


    def change(self, amount, coins):
        if amount == 0:
            return 1
        if not coins:
            return 0

        dp = [0] * (amount + 1)
        dp[0] = 1

        for i in range(len(coins)):
            for j in range(1, len(dp)):
                w1 = dp[j]
                if j - coins[i] < 0:
                    continue
                else:
                    w2 = dp[j-coins[i]]
                    dp[j] = w1 + w2
        return dp[amount]



if __name__ == '__main__':
    print(Solution().change(500, [1,2,5]))


        
# @lc code=end

