#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-21 10:04:45
LastEditors: yangyuxiang
LastEditTime: 2021-04-21 12:24:19
FilePath: /leetcode/51.n-皇后.py
'''
#
# @lc app=leetcode.cn id=51 lang=python
#
# [51] N 皇后
#

# @lc code=start
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        results = []
        board = [['.'] * n for i in range(n)]

        def backtrack(board, row):
            # 满足结束条件
            if row == len(board):
                results.append(["".join(line) for line in board])
            
            for col in range(len(board)):
                # 判断当前位置是否合法
                if not isValid(board, row, col):
                    continue
                # 做选择
                board[row][col] = 'Q'
                # 回溯
                backtrack(board, row+1)
                board[row][col] = '.'

                
            
        def isValid(board, row, col): 
            # 同一列
            for i in range(row):
                if board[i][col] == "Q":
                    return False
            
            # 右上
            j = col
            for i in range(row-1, -1, -1):
                j += 1
                if j >= len(board):
                    continue
                if board[i][j] == "Q":
                    return False
            
            # 左上
            z = col
            for i in range(row-1, -1, -1):
                z -= 1
                if z < 0:
                    continue
                if board[i][z] == "Q":
                    return False

            return True

        backtrack(board, row=0)
        return results
                

if __name__ == '__main__':
    input = 4
    print(Solution().solveNQueens(4))           
        
# @lc code=end

