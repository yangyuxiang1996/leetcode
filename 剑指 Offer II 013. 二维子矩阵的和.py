#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-27 08:02:42
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-27 08:34:34
FilePath: /leetcode/剑指 Offer II 013. 二维子矩阵的和.py
Description: 

'''
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.m, self.n = len(matrix), len(matrix[0])
        self.right = [[0]*self.n for i in range(self.m)]
        for i in range(self.n-1, -1, -1):
            for j in range(self.m):
                if i == self.n-1:
                    self.right[j][i] = self.matrix[j][i]
                else:
                    self.right[j][i] = self.right[j][i+1] + self.matrix[j][i]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        for i in range(row1, row2+1):
            if col2 == self.n-1:
                res += self.right[i][col1]
            else:
                res += self.right[i][col1] - self.right[i][col2+1]
        return res



if __name__ == '__main__':
    matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
    row1, col1, row2, col2 = 2, 1, 4, 3
    obj = NumMatrix(matrix)
    print(obj.sumRegion(row1, col1, row2, col2))
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)