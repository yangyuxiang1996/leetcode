#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-13 22:22:47
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-13 23:04:02
FilePath: /leetcode/剑指 Offer 29. 顺时针打印矩阵.py
Description: 
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
'''
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        res = []
        left, right = 0, len(matrix[0])-1
        up, down = 0, len(matrix)-1
        while len(res) < len(matrix) * len(matrix[0]):
            # 向右
            for i in range(left, right+1):
                res.append(matrix[up][i])
            up += 1
            if len(res) == len(matrix) * len(matrix[0]):
                break
            # 向下
            for i in range(up, down+1):
                res.append(matrix[i][right])
            right -= 1
            if len(res) == len(matrix) * len(matrix[0]):
                break
            # 向左
            for i in range(right, left-1, -1):
                res.append(matrix[down][i])
            down -= 1
            if len(res) == len(matrix) * len(matrix[0]):
                break
            # 向上
            for i in range(down, up-1, -1):
                res.append(matrix[i][left])
            left += 1
            if len(res) == len(matrix) * len(matrix[0]):
                break
        return res


if __name__ == '__main__':
    matrix = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
    print(Solution().spiralOrder(matrix))