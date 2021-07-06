#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-20 22:48:13
LastEditors: yangyuxiang
LastEditTime: 2021-07-03 23:18:35
FilePath: /leetcode/46.全排列.py
'''
#
# @lc app=leetcode.cn id=46 lang=python
#
# [46] 全排列
#

# @lc code=start
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        paths = []
        visited = [False] * len(nums)

        def backtrace(path):
            if len(path) == len(nums):
                paths.append(path[:])
            for i in range(len(nums)):
                if visited[i] == False:
                    path.append(nums[i])
                    visited[i] = True
                    backtrace(path)
                    path.pop()
                    visited[i] = False
        backtrace([])
        return paths

if __name__ == '__main__':
    nums = [1,2,3]
    print(Solution().permute(nums))

        
# @lc code=end

