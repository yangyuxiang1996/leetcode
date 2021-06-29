#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-12 10:28:49
LastEditors: yangyuxiang
LastEditTime: 2021-05-12 10:36:07
FilePath: /leetcode/77.组合.py
'''
#
# @lc app=leetcode.cn id=77 lang=python
#
# [77] 组合
#

# @lc code=start
class Solution(object):
    def __init__(self):
        self.res = []

    def backtrace(self, n, k, start, trace):
        if len(trace) == k:
            self.res.append(trace[:])
            return
        
        for i in range(start, n+1):
            trace.append(i)
            self.backtrace(n, k, i+1, trace)
            trace.pop()


    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n <= 0 and k <= 0:
            return []
        
        trace = []
        start = 1
        self.backtrace(n, k, start, trace)

        return self.res        
        
# @lc code=end

