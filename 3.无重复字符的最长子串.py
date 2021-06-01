#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-25 10:28:11
LastEditors: yangyuxiang
LastEditTime: 2021-05-23 08:22:24
FilePath: /leetcode/3.无重复字符的最长子串.py
'''
#
# @lc app=leetcode.cn id=3 lang=python
#
# [3] 无重复字符的最长子串
#


# @lc code=start
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = right = 0
        window = {}
        max_length = 0

        while right < len(s):
            c = s[right]
            if c not in window:
                window[c] = 1
            else:
                window[c] += 1
            right += 1

            while window[c] > 1:
                d = s[left]
                left += 1
                window[d] = window[d] - 1
            max_length = max(max_length, right-left)

        return max_length

    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = right = 0
        max_length = 0
        while right < len(s):
            c = s[right]
            if c not in s[left:right]:
                right += 1
                max_length = max(max_length, right - left)
            else:
                left = s[left:right].index(c) + left + 1

        return max_length


a = "abcabcbb"
print(Solution().lengthOfLongestSubstring(a))
# @lc code=end
