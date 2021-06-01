#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-22 23:07:22
LastEditors: yangyuxiang
LastEditTime: 2021-04-22 23:35:52
FilePath: /leetcode/76.最小覆盖子串.py
'''
#
# @lc app=leetcode.cn id=76 lang=python
#
# [76] 最小覆盖子串
#

# @lc code=start
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left = right = valid = 0
        need = {}
        window = {}
        for c in t:
            if c not in need:
                need[c] = 1
            else:
                need[c] += 1
        start = 0
        length = float("inf")
        while right < len(s):
            c = s[right]
            if c in need:
                if c not in window:
                    window[c] = 1
                else:
                    window[c] += 1
                if window[c] == need[c]:
                    valid += 1
            right += 1 
            
            while valid == len(need):
                if right - left < length:
                    start = left
                    length = right - left

                c = s[left]
                left += 1
                if c in window:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1

        return s[start:start + length] if length != float("inf") else ''


if __name__ == "__main__":
    s = 'ADOBECODEBANC'
    t = 'ABC'
    print(Solution().minWindow(s, t))


        

# @lc code=end

