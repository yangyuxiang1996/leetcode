#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-09-04 11:07:15
LastEditors: Yuxiang Yang
LastEditTime: 2021-09-04 11:29:25
FilePath: /leetcode/剑指 Offer II 039. 直方图最大矩形面积.py
Description: 
给定非负整数数组 heights ，数组中的数字用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
求在该柱状图中，能够勾勒出来的矩形的最大面积。
输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
'''
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # 对于i，往左往右找第一个比它小的，以i为基准的矩形面积为heights[i] * (right-left-1)
        # 从前往后
        n = len(heights)
        left, right = [-1] * n, [n] * n

        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                index = stack.pop()
                right[index] = i
            stack.append(i)
        
        stack = []
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] > heights[i]:
                index = stack.pop()
                left[index] = i
            stack.append(i)
        
        print(left)
        print(right)

        max_areas = float("-inf")
        for i in range(n):
            max_areas = max(max_areas, heights[i] * (right[i] - left[i] - 1))
        
        return max_areas

if __name__ == "__main__":
    heights = [2,1,5,6,2,3]
    heights = [2,4]
    print(Solution().largestRectangleArea(heights))


