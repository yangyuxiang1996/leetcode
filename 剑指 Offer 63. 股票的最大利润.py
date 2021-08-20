#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-20 23:54:31
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-21 00:22:04
FilePath: /leetcode/剑指 Offer 63. 股票的最大利润.py
Description: 
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
'''
class Solution(object):
    def maxProfit0(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        max_profit, min_price = float("-inf"), prices[0]
        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, prices[i]- min_price)
        return max_profit
    
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        dp = [-prices[0], 0]
        for i in range(1, len(prices)):
            dp[0], dp[1] = max(dp[0], -prices[i]), max(dp[1], dp[0]+prices[i])
        return dp[1]
    