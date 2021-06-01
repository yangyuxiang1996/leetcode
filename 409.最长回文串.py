#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-27 11:16:16
LastEditors: yangyuxiang
LastEditTime: 2021-04-27 12:39:57
FilePath: /leetcode/409.最长回文串.py
'''
#
# @lc app=leetcode.cn id=409 lang=python
#
# [409] 最长回文串
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        res = 0
        flag = False
        for k, v in d.items():
            if v % 2 == 0:
                res += v
            else:
                flag = True
                res += v-1
        return res+1 if flag else res

                
        
# @lc code=end

