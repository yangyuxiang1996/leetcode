#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-21 23:44:30
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-22 00:12:05
FilePath: /leetcode/剑指 Offer 47. 礼物的最大价值.py
Description: 
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于 0）。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向右或者向下移动一格、直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物的价值，请计算你最多能拿到多少价值的礼物？
'''
class Solution(object):
    def __init__(self):
        self.ans = 0

    def maxValue0(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 回溯，超时
        def backtrace(grid, m, n, row, col, value):
            if row >= m or col >= n:
                return
            if row == m-1 and col == n-1:
                self.ans = max(self.ans, value+grid[row][col])
                return
            
            visited[row][col] = True
            # 向右
            value += grid[row][col]
            backtrace(grid, m, n, row, col+1, value)
            value -= grid[row][col]
            # 向下
            value += grid[row][col]
            backtrace(grid, m, n, row+1, col, value)
            value -= grid[row][col]

            visited[row][col] = False

        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        backtrace(grid, m, n, 0, 0, 0)

        return self.ans

    def maxValue1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 动态规划, 二维DP
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
        for j in range(1, m):
            dp[j][0] = dp[j-1][0] + grid[j][0]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[m-1][n-1]


    def maxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 动态规划, 一维DP
        m, n = len(grid), len(grid[0])
        dp = [0] * n
        for i in range(n):
            if i == 0:
                dp[i] = grid[0][0]    
            else:
                dp[i] = dp[i-1] + grid[0][i]
        for i in range(1, m):
            for j in range(n):
                if j == 0:
                    dp[0] = dp[0] + grid[i][0]
                else:
                    dp[j] = max(dp[j-1], dp[j]) + grid[i][j]
        return dp[-1]
            





if __name__ == '__main__':
    grid = [[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]
    print(Solution().maxValue(grid))
            
        

