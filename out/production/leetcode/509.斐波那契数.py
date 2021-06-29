#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-20 16:24:47
LastEditors: yangyuxiang
LastEditTime: 2021-04-20 16:32:33
FilePath: /leetcode/509.斐波那契数.py
'''
#
# @lc app=leetcode.cn id=509 lang=python
#
# [509] 斐波那契数
#

# @lc code=start
class Solution(object):
    def __init__(self):
        self.memo = dict()
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in self.memo:
            return self.memo[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        self.memo[n] = self.fib(n-1) + self.fib(n-2)
        return self.memo[n]
# @lc code=end

