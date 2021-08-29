#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-29 00:02:49
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-29 00:16:39
FilePath: /leetcode/剑指 Offer II 020. 回文子字符串的个数.py
Description: 
给定一个字符串 s ，请计算这个字符串中有多少个回文子字符串。
具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。
'''
class Solution(object):
    def countSubstrings0(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 动态规划
        # dp[i][j]表示s[i:j+1]是否为回文子串
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        res = 0
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i < 3 or dp[i+1][j-1] == 1:
                        dp[i][j] = 1
                        res += 1
        return res
    
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 中心扩散
        def helper(s, left, right):
            res = 0
            while  left>=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                res += 1

            return res

        n = len(s)
        res = 0
        for i in range(n):
            res += helper(s, i, i)
            res += helper(s, i, i+1)

        return res







