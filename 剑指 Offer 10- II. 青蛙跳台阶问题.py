#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-11 10:40:07
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-11 10:42:31
FilePath: /leetcode/剑指 Offer 10- II. 青蛙跳台阶问题.py
Description: 
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
'''
class Solution(object):
    def numWays(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        dp = [1, 2]
        for i in range(3, n+1):
            tmp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = tmp
        return dp[1]
        