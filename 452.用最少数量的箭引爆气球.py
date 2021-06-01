#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-24 08:19:06
LastEditors: yangyuxiang
LastEditTime: 2021-05-24 08:22:37
FilePath: /leetcode/452.用最少数量的箭引爆气球.py
'''

#
# @lc app=leetcode.cn id=452 lang=python
#
# [452] 用最少数量的箭引爆气球
#


# @lc code=start
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n < 2:
            return n
        points = sorted(points, key=lambda x: x[1])
        count = 1
        end = points[0][1]
        for i in range(1, n):
            if end < points[i][0]:
                count += 1
                end = points[i][1]

        return count
            

# @lc code=end
