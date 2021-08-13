#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-12 22:57:06
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-13 08:42:47
FilePath: /leetcode/剑指 Offer 14- I. 剪绳子.py
Description: 
给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），
每段绳子的长度记为 k[0],k[1]...k[m-1] 。请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？
例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
'''
class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 动态规划
        if n <= 3:
            return n - 1
        dp = [0] * (n + 1)
        dp[1] = 0
        dp[2] = 1
        dp[3] = 2
        for i in range(4, n+1):
            for j in range(1, i//2 + 1):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        return dp[n]

    def cuttingRope(self, n):
        # 贪心
        if n < 4:
            return n - 1
        
        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res * n

    def cuttingRope(self, n):
        # 贪心
        if n < 4:
            return n - 1

        if n % 3 == 1:
            return 3**(n//3-1) * 4
        elif n % 3 == 2:
            return 3**(n//3) * 2
        else:
            return 3**(n//3)
        
            
        
        

