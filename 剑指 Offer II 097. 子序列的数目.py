#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-09-04 00:17:14
LastEditors: Yuxiang Yang
LastEditTime: 2021-09-04 01:06:17
FilePath: /leetcode/剑指 Offer II 097. 子序列的数目.py
Description: 
给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。
字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。
（例如，"ACE" 是 "ABCDE" 的一个子序列，而 "AEC" 不是）
题目数据保证答案符合 32 位带符号整数范围。
输入：s = "rabbbit", t = "rabbit"
输出：3
解释：
如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
rabbbit
rabbbit
rabbbit
'''
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(m+1):
                dp[0][i] = 1

        for i in range(1, n+1):
            for j in range(1, m+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]

        return dp[-1][-1]


if __name__ == '__main__':
    s = "rabbbit"
    t = "rabbit"
    print(Solution().numDistinct(s, t))


