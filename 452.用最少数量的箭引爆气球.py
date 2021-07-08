#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-24 08:19:06
LastEditors: yangyuxiang
LastEditTime: 2021-07-08 22:56:29
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
        # points = sorted(points, key=lambda x: x[0])
        # count = 1
        # for i in range(1, n):
        #     if points[i-1][1] < points[i][0]:
        #         count += 1
        #     else:
        #         points[i][1] = min(points[i - 1][1], points[i][1])  # 更新当前的最小右边界

        points = sorted(points, key=lambda x: x[1])
        count = 1
        end = points[0][1]  # 这里一开始就是最小的右边界
        for i in range(1, n):
            if end < points[i][0]:
                count += 1
                end = points[i][1]
                
        
        return count


if __name__ == '__main__':
    points = [[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]
    print(Solution().findMinArrowShots(points))
            

# @lc code=end
