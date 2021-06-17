#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-22 23:07:22
LastEditors: yangyuxiang
LastEditTime: 2021-06-17 23:07:28
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
        from collections import Counter
        need = Counter(t)  # 记录字符串t中的字符出现次数
        n = len(s)
        left = right = 0  # 滑动窗口边界
        window = {}  # 记录滑动窗口中的字符频次
        valid = 0  # 记录window中满足要求的字符个数
        start = 0
        min_length = n + 1

        while right < n:
            c = s[right]
            right += 1
            if c in window:
                window[c] += 1
            else:
                window[c] = 1
            if c in need:
                if window[c] == need[c]:
                    valid += 1
            
            while valid == len(need):  # 需要缩小滑动窗口
                if right - left < min_length:
                    min_length = right - left
                    start = left

                c = s[left]
                left += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                window[c] -= 1

        return s[start: start+min_length] if min_length <= n else ""




if __name__ == "__main__":
    s = 'ADOBECODEBANC'
    t = 'ABC'
    print(Solution().minWindow(s, t))


        

# @lc code=end

