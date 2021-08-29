#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-27 11:10:18
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-27 11:20:30
FilePath: /leetcode/剑指 Offer II 016. 不含重复字符的最长子字符串.py
Description: 
给定一个字符串 s ，请你找出其中不含有重复字符的 最长连续子字符串 的长度。
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子字符串是 "abc"，所以其长度为 3。
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        window = collections.defaultdict(int)
        left, right, max_len = 0, 0, 0
        while right < len(s):
            c = s[right]
            right += 1
            window[c] += 1
            while window[c] > 1:
                window[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left)

        return max_len


if __name__ == '__main__':
    s = ""
    print(Solution().lengthOfLongestSubstring(s))


