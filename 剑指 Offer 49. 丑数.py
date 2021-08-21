#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-21 17:32:52
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-21 23:06:34
FilePath: /leetcode/剑指 Offer 49. 丑数.py
Description: 
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
输入: n = 10
输出: 12
解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数
题解：https://leetcode-cn.com/problems/chou-shu-lcof/solution/mian-shi-ti-49-chou-shu-dong-tai-gui-hua-qing-xi-t/
'''

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1] * n
        a, b, c = 0, 0, 0
        for i in range(1, n):
            n_a, n_b, n_c = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n_a, n_b, n_c)
            if n_a == dp[i]:
                a += 1
            if n_b == dp[i]:
                b += 1
            if n_c == dp[i]:
                c += 1
        return dp[-1]
        

        