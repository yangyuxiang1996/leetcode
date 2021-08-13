#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-11 10:15:36
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-11 10:28:24
FilePath: /leetcode/剑指 Offer 04. 二维数组中的查找.py
Description:
在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
class Solution(object):
    def binarySearch(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
    
    def findNumberIn2DArray0(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 时间复杂度:O(mlogn)
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][n-1]:
                if self.binarySearch(matrix[i], target):
                    return True
        return False

    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 从右上角出发，碰到大于target的列减一，碰到小于target的行加一
        # 时间复杂度:O(m+n)
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n-1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
                



if __name__ == '__main__':
    nums = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    print(Solution().findNumberIn2DArray(nums, target))
