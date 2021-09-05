#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-09-04 15:19:20
LastEditors: Yuxiang Yang
LastEditTime: 2021-09-04 16:27:41
FilePath: /leetcode/剑指 Offer II 100. 三角形中最小路径之和.py
Description: 
给定一个三角形 triangle ，找出自顶向下的最小路径和。
每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
'''
class Solution(object):
    def minimumTotal0(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # 暴力解法
        if not triangle:
            return 0
        
        tmp = [triangle[0][0]]
        for i in range(len(triangle)-1):
            next_tmp = [float('inf')] * len(triangle[i+1])
            for j in range(len(tmp)):
                next_tmp[j] = min(next_tmp[j], triangle[i+1][j]+tmp[j])
                next_tmp[j+1] = min(next_tmp[j+1], triangle[i+1][j+1]+tmp[j])
            tmp = next_tmp
        
        return min(tmp)

    def minimumTotal1(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # 自底向上的动态规划, 二维DP数组
        if not triangle:
            return 0
        
        n = len(triangle)
        dp = [[0] * (n+1) for _ in range(n+1)]
        for i in range(n-1, -1, -1):
            for j in range(i+1):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]

        return dp[0][0]


    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # 自底向上的动态规划， 压缩成一维DP数组
        if not triangle:
            return 0
        
        n = len(triangle)
        dp = [0] * (n+1)
        for i in range(n-1, -1, -1):
            for j in range(i+1):
                dp[j] = min(dp[j], dp[j+1]) + triangle[i][j]

        return dp[0]
        



if __name__ == '__main__':
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    print(Solution().minimumTotal(triangle))
