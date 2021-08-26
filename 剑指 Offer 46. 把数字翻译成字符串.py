#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-23 22:58:40
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-23 23:22:04
FilePath: /leetcode/剑指 Offer 46. 把数字翻译成字符串.py
Description: 
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
'''
class Solution(object):
    def translateNum0(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        n = len(num)
        if n <= 1: 
            return n
        dp = [0] * n
        dp[0] = 1
        if int(num[:2]) > 25:
            dp[1] = 1
        else: 
            dp[1] = 2
        for i in range(2, n):
            if int(num[i-1:i+1]) <= 25 and int(num[i-1]) != 0:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[n-1]

    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        n = len(num)
        if n <= 1: 
            return n
        a, b = 1, 1
        if int(num[:2]) <= 25:
            b = 2
        for i in range(2, n):
            if int(num[i-1:i+1]) <= 25 and int(num[i-1]) != 0:
                a, b = b, a + b
            else:
                a, b = b, b
        return b


if __name__ == '__main__':
    num = 506
    print(Solution().translateNum(num))
    
