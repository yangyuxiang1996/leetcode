#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-09-04 11:37:46
LastEditors: Yuxiang Yang
LastEditTime: 2021-09-04 15:11:09
FilePath: /leetcode/剑指 Offer II 040. 矩阵中最大的矩形.py
Description: 

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
        
        # print(left)
        # print(right)

        max_areas = float("-inf")
        for i in range(n):
            max_areas = max(max_areas, heights[i] * (right[i] - left[i] - 1))
        
        return max_areas

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[str]
        :rtype: int
        """
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        ans = float('-inf')
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0
            ans = max(ans, self.largestRectangleArea(heights))

        return ans


if __name__ == '__main__':
    matrix = ["10100","10111","11111","10010"]
    print(Solution().maximalRectangle(matrix))
                


