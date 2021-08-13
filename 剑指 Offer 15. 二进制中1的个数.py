#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-13 22:02:23
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-13 22:19:58
FilePath: /leetcode/剑指 Offer 15. 二进制中1的个数.py
Description: 
编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为 汉明重量).）。
'''
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(32):
            if n & (1 << i) != 0:
                res += 1
        return res
            

    def hammingWeight0(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n != 0:
            n &= n-1
            res += 1
        return res
