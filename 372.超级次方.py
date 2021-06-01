#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-19 10:31:50
LastEditors: yangyuxiang
LastEditTime: 2021-05-19 11:01:38
FilePath: /leetcode/372.超级次方.py
'''
#
# @lc app=leetcode.cn id=372 lang=python
#
# [372] 超级次方
#

# @lc code=start
base = 1337
class Solution(object):
    def myPow(self, a, k):
        a %= base
        res = 1
        for i in range(k):
            res *= a
            # res %= base

        return res % base

    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        if not b:
            return 1
        
        last = b.pop()
        num1 = self.myPow(a, last)
        num2 = self.myPow(self.superPow(a, b), 10)
        return (num1 * num2) % base
        
# @lc code=end

