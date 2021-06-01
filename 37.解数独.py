#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-13 07:51:40
LastEditors: yangyuxiang
LastEditTime: 2021-05-13 08:40:30
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

        if m == 9:
            return True
        if n == 9:
            return self.backtrace(m+1, 0, board)
        if board[m][n] != '.':
            return self.backtrace(m, n+1, board)
    
        for i in range(1, 10):        
            if not self.isValid(m, n, board, i):
                continue
            board[m][n] = str(i)
            if self.backtrace(m, n+1, board):
                return True
            board[m][n] = '.'
            

        
    def isValid(self, r, c, board, n):
        for i in range(9):
            if board[r][i] == str(n):
                return False
            if board[i][c] == str(n):
                return False
            if board[(r//3)*3 + i//3][(c//3)*3 + i%3] == str(n):
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

