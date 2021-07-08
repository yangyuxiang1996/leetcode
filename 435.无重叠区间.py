#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-24 07:59:37
LastEditors: yangyuxiang
LastEditTime: 2021-07-08 08:04:21
FilePath: /leetcode/435.无重叠区间.py
'''

#
# @lc app=leetcode.cn id=435 lang=python
#
# [435] 无重叠区间
#


# @lc code=start
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) <= 1:
            return 0
        intervals = sorted(intervals, key=lambda x: x[1])
        stack = []
        stack.append(intervals[0])
        end = intervals[0][1]
        count = 0
        for i in range(1, len(intervals)):
            if end <= intervals[i][0]:  # 无重叠，指向下一个
                stack.append(intervals[i])
                end = intervals[i][1]
            else:  # 有重叠
                count += 1

        return count


# @lc code=end
