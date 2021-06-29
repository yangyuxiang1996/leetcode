#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-13 22:22:41
LastEditors: yangyuxiang
LastEditTime: 2021-05-14 07:54:14
FilePath: /leetcode/773.滑动谜题.py
'''
#
# @lc app=leetcode.cn id=773 lang=python
#
# [773] 滑动谜题
#

# @lc code=start
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        visited = []
        start = board[0] + board[1]

        neighbor = {
            0:[1,3], 
            1:[0,2,4], 
            2:[1,5],
            3:[0,4],
            4:[1,3,5],
            5:[2,4]
            }

        q = []
        q.append(start)
        visited.append(start)

        step = 0
        while q:
            sz = len(q)
            for i in range(sz):
                cur = q.pop(0)
                if cur == [1,2,3,4,5,0]:
                    return step
                
                j = 0
                while cur[j] != 0:
                    j += 1

                for adj in neighbor[j]:
                    new_board = cur[:]
                    new_board[adj], new_board[j] = new_board[j], new_board[adj]
                    if new_board not in visited:
                        visited.append(new_board)
                        q.append(new_board)

            step += 1

        return -1


if __name__ == "__main__":
    nums = [[1,2,3],[4,0,5]]
    print(Solution().slidingPuzzle(nums))
                    
                

            

        

        
        
# @lc code=end

