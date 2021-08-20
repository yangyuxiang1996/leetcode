#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-20 08:30:51
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-20 08:49:04
FilePath: /leetcode/剑指 Offer 65. 不用加减乘除做加法.py
Description: 
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。
'''
class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        """
        考虑进位，
        1. 没有进位，例如a=0001，b=0010，那么a+b的结果就是a^b：0011
        2. 有进位，例如a=0010，b=0010，那么a+b的结果就是a&b << 1：0100
        3. 同时存在，就是两种情况的和，直至没有进位
        """
        x = 0xffffffff
        a, b = a&x, b&x
        while b != 0:
            a, b = (a ^ b), (a & b) << 1 & x
        return a if a <= 0x7fffffff else ~(a ^ x)


if __name__ == '__main__':
    print(Solution().add(3,2))
