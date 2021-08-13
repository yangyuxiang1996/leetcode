#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-11 08:33:12
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-11 08:33:25
FilePath: /leetcode/剑指 Offer 10- I. 斐波那契数列.py
Description: 
'''
class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        
        f = [0,1]
        for i in range(2,n+1):
            tmp = f[0] + f[1]
            f[0] = f[1]
            f[1] = tmp

        return f[1] % (1000000007)
