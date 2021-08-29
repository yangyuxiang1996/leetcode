#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-27 11:23:01
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-27 11:30:37
FilePath: /leetcode/剑指 Offer II 017. 含有所有字符的最短字符串.py
Description: 
给定两个字符串 s 和 t 。返回 s 中包含 t 的所有字符的最短子字符串。如果 s 中不存在符合条件的子字符串，则返回空字符串 "" 。
如果 s 中存在多个符合条件的子字符串，返回任意一个。
输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC" 
解释：最短子字符串 "BANC" 包含了字符串 t 的所有字符 'A'、'B'、'C'
'''
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(s) < len(t):
            return ""

        import collections
        need = collections.defaultdict(int)
        window = collections.defaultdict(int)
        for c in t:
            need[c] += 1
        
        left, right, min_len = 0, 0, len(s)+1
        valid, res = 0, ""
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] += 1
                if need[c] == window[c]:
                    valid += 1
            while valid == len(need):
                if right - left < min_len:
                    start = left
                    min_len = right - left
                    res = s[start:start + min_len]
                c = s[left]
                left += 1
                if c in window:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
        return res


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))


