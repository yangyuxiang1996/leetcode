#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-12 21:40:45
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-12 22:14:24
FilePath: /leetcode/剑指 Offer 13. 机器人的运动范围.py
Description: 
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。
请问该机器人能够到达多少个格子？
'''
class Solution(object):
    def __init__(self):
        self.count = 0
    
    def sums(self, num):
        res = 0
        while num != 0:
            res += num % 10
            num //= 10
        return res
    
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        # directions = [[0,1], [0,-1], [1,0], [-1,0]]
        directions = [[0,1], [1,0]]
        visited = [[False] * n for _ in range(m)]

        def dfs(m, n, i, j, k, visited):
            if i < 0 or j < 0 or i >= m or j >= n:
                return
            if self.sums(i) + self.sums(j) > k:
                return
            if visited[i][j] == True:
                return

            visited[i][j] = True
            self.count += 1
            for direction in directions:
                new_i, new_j = i+direction[0], j+direction[1]
                dfs(m, n, new_i, new_j, k, visited)
        
        
        dfs(m, n, 0, 0, k ,visited)
        return self.count
                
                
            
            


