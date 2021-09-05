#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-09-02 08:46:56
LastEditors: Yuxiang Yang
LastEditTime: 2021-09-02 08:54:50
FilePath: /leetcode/剑指 Offer II 095. 最长公共子序列.py
Description: 
给定两个字符串 text1 和 text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。
'''
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # dp[i][j]表示text1[:i]和text[:j]的最长公共子序列的长度
        # dp[i][j] = dp[i-1][j-1] + 1 if text1[i] == text[j] else max(dp[i][j-1], dp[i-1][j])

        m, n = len(text1), len(text2)
        if m == 0 or n == 0:
            return 0
        
        dp = [[0] * (n + 1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
