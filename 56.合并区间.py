#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-24 08:33:13
LastEditors: yangyuxiang
LastEditTime: 2021-07-08 23:32:57
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
        
        # 按照左边界从小到大排序, 每次需要判断是否重叠，如果重叠则要选择较大的右边界
        intervals = sorted(intervals, key=lambda x: x[0])
        stack = []
        for i in range(0, len(intervals)):
            start = intervals[i][0]
            if stack and stack[-1][1] >= start:
                stack[-1][1] = max(stack[-1][1], intervals[i][1])
            else:
                stack.append([start, intervals[i][1]])

        return stack

        
    def merge0(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(intervals)
        if n <= 1:
            return intervals

        # 按照右边界从小到大排序, 每次需要判断是否重叠，如果重叠则要选择较小的左边界
        intervals = sorted(intervals, key=lambda x: x[1])
        stack = []
        for i in range(0, len(intervals)):
            start = intervals[i][0]
            while stack and stack[-1][1] >= intervals[i][0]:
                start = min(stack[-1][0], intervals[i][0])
                stack.pop()
            stack.append([start, intervals[i][1]])
        return stack


if __name__ == '__main__':
    intervals = [[1, 3], [2, 6], [4,5], [8, 10], [15, 18]]
    print(Solution().merge(intervals))

# @lc code=end
