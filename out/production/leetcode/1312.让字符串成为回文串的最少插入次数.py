#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-27 21:53:18
LastEditors: yangyuxiang
LastEditTime: 2021-04-27 22:04:16
FilePath: /leetcode/1312.让字符串成为回文串的最少插入次数.py
'''
#
# @lc app=leetcode.cn id=1312 lang=python
#
# [1312] 让字符串成为回文串的最少插入次数
#

# @lc code=start
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n < 2:
            return 0
        
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1

        return dp[0][n-1]


if __name__ == "__main__":
    s = 'zzazz'
    print(Solution().minInsertions(s))
                
        
# @lc code=end

