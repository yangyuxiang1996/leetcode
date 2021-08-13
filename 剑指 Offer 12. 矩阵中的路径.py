#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-12 08:14:58
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-12 10:47:48
FilePath: /leetcode/剑指 Offer 12. 矩阵中的路径.py
Description: 
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。
'''
class Solution(object):
    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position    
    def dfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
        # check whether can find "word" along one direction
        res = self.dfs(board, i+1, j, word[1:]) or \
              self.dfs(board, i-1, j, word[1:]) or \
              self.dfs(board, i, j+1, word[1:]) or \
              self.dfs(board, i, j-1, word[1:])
        
        board[i][j] = tmp
        return res


if __name__ == '__main__':
    board = [["C","A","A"],["A","A","A"],["B","C","D"]]
    word = "AAB"
    print(Solution().exist(board, word))
