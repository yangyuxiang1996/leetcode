#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-20 22:48:13
LastEditors: yangyuxiang
LastEditTime: 2021-04-20 23:11:00
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

        def backtrack(nums, path):
            if len(path) == len(nums):
                paths.append(path[:])
                return
            for num in nums:
                if num in path:
                    continue
                path.append(num)
                backtrack(nums, path)
                path.remove(num)

        backtrack(nums, [])
        return paths

if __name__ == '__main__':
    nums = [1,2,3]
    print(Solution().permute(nums))

        
# @lc code=end

