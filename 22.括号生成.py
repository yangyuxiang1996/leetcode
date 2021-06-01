#!/usr/bin/env python
# coding=utf-8
'''
Description:  leetcode
Author: yangyuxiang
Date: 2021-05-13 10:23:48
LastEditors: yangyuxiang
LastEditTime: 2021-05-24 07:37:29
FilePath: /leetcode/22.括号生成.py
'''

#
# @lc app=leetcode.cn id=22 lang=python
#
# [22] 括号生成
#


# @lc code=start
class Solution(object):
    def __init__(self):
        self.res = []

    def backtrace(self, left, right, trace):
        if left == 0 and right == 0:
            self.res.append("".join(trace))
            return

        if left > right:  # '(' 剩得比 ')' 多
            return

        if left > 0:
            trace.append("(")
            self.backtrace(left - 1, right, trace)
            trace.pop()

        if right > 0:
            trace.append(")")
            self.backtrace(left, right - 1, trace)
            trace.pop()

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        if n == 1:
            return ['()']

        trace = []
        self.backtrace(n, n, trace)
        return self.res


# @lc code=end
