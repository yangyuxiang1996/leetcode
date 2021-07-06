#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-13 07:51:40
LastEditors: yangyuxiang
LastEditTime: 2021-07-05 07:44:38
FilePath: /leetcode/37.解数独.py
'''
#
# @lc app=leetcode.cn id=37 lang=python
#
# [37] 解数独
#

# @lc code=start
class Solution(object):
    def backtrace(self, m, n, board):
        # m, n 分别为行列
        if m == 9:
            return True
        if n == 9:
            return self.backtrace(m+1, 0, board)
        if board[m][n] != '.':
            return self.backtrace(m, n+1, board)
    
        for i in range(1, 10):        
            if self.isValid(m, n, board, i):
                board[m][n] = str(i)
                if self.backtrace(m, n+1, board):
                    return True
                board[m][n] = '.'
            

        
    def isValid(self, r, c, board, n):
        for i in range(9):
            # 同行是否重复
            if board[r][i] == str(n):
                return False
            # 同列是否重复
            if board[i][c] == str(n):
                return False
            # 9宫格是否重复
            row, col = (r//3)*3 + i//3, (c//3)*3 + i%3
            if board[row][col] == str(n):
                return False

        return True
        

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.backtrace(0, 0, board)        
        return 

        
# @lc code=end

