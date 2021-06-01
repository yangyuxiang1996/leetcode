#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-24 08:33:13
LastEditors: yangyuxiang
LastEditTime: 2021-05-24 08:58:11
FilePath: /leetcode/56.合并区间.py
'''

#
# @lc app=leetcode.cn id=56 lang=python
#
# [56] 合并区间
#


# @lc code=start
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        if n <= 1:
            return intervals

        intervals = sorted(intervals, key=lambda x: x[1])
        stack = []
        stack.append(intervals[0])
        for i in range(1, n):
            start = intervals[i][0]
            while stack and stack[-1][1] >= start:
                start = min(stack[-1][0], intervals[i][0])
                stack.pop()
            stack.append([start, intervals[i][1]])
            # stack.append(intervals[i])

        return stack


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [4,5], [8, 10], [15, 18]]
    print(Solution().merge(intervals))

# @lc code=end
