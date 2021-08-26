#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-24 22:04:39
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-24 22:09:44
FilePath: /leetcode/剑指 Offer II 003. 前 n 个数字二进制中 1 的个数.py
Description: 
给定一个非负整数 n ，请计算 0 到 n 之间的每个数字的二进制表示中 1 的个数，并输出一个数组。
'''
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # if n == 0:
        #     return [0]
        # if n == 1:
        #     return [0, 1]
        # dp = [0] * (n+1)
        # dp[0], dp[1], dp[2] = 0, 1, 1
        # for i in range(3, n+1):
        #     if i % 2 == 1:
        #         dp[i] = dp[i-1] + 1
        #     else:
        #         dp[i] = dp[i // 2]
        # return dp

        dp = [0] * (n + 1)
        for i in range(1, n+1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp