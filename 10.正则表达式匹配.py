#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-27 22:30:18
LastEditors: yangyuxiang
LastEditTime: 2021-04-27 22:48:57
FilePath: /leetcode/10.正则表达式匹配.py
'''
#
# @lc app=leetcode.cn id=10 lang=python
#
# [10] 正则表达式匹配
#

# @lc code=start
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def helper(s, p, i, j):
            if j == len(p):
                return i == len(s)
            if i == len(s):
                if (len(p) - j) % 2 == 1:
                    return False
                while j+1 < len(p):
                    if p[j+1] != '*':
                        return False
                    j += 2
                return True 
            
            if s[i] == p[j] or p[j] == '.': 
                if j+1 < len(p) and p[j+1] == '*':
                    return helper(s, p, i, j+2) or helper(s, p, i+1, j)
                else:
                    return helper(s, p, i+1, j+1)
            else:
                if j+1 < len(p) and p[j+1] == '*':
                    return helper(s, p, i, j+2)
                else:
                    return False
            

        return helper(s, p, 0, 0)

# @lc code=end

