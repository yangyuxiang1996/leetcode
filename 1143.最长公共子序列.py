#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-26 11:13:44
LastEditors: yangyuxiang
LastEditTime: 2021-05-30 22:43:08
FilePath: /leetcode/1143.最长公共子序列.py
'''
#
# @lc app=leetcode.cn id=1143 lang=python
#
# [1143] 最长公共子序列
#


# @lc code=start
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if not text1 or not text2:
            return 0
        
        len1 = len(text1)
        len2 = len(text2)

        dp = [[0] * (len2+1)] * (len1+1)
        for i in range(1, len1+1):
            for j in range(1, len2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[len1][len2]
        


# @lc code=end
