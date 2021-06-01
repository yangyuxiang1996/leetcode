#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-27 07:59:46
LastEditors: yangyuxiang
LastEditTime: 2021-05-23 10:19:44
FilePath: /leetcode/5.最长回文子串.py
'''

#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#


# @lc code=start
class Solution(object):
    def palindrome(self, s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1:j], j-i-1

    def longestPalindrome1(self, s):
        """
        双指针，从中间向两边展开
        """
        n = len(s)
        if n < 2:
            return s

        res = ""
        max_len = 0
        for i in range(n):
            substr, l = self.palindrome(s, i, i)
            if l > max_len:
                res = substr
                max_len = l
            substr, l = self.palindrome(s, i, i + 1)
            if l > max_len:
                res = substr
                max_len = l

        return res

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        dp数组：储存s[i:j]是否为回文串
        动态规划：dp[i][j] = dp[i+1][j-1] & s[i] == s[j]
        判断边界条件，j-i<3 ? s[i] == s[j] -> True
        """

        n = len(s)
        if n < 2:
            return s

        dp = [[False] * n for _ in range(n)]
        max_len = 1
        begin = 0
        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i

        return s[begin:begin + max_len]


if __name__ == "__main__":
    s = "aacabdkacaa"
    print(Solution().longestPalindrome(s))

# @lc code=end
