#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-12 10:37:48
LastEditors: yangyuxiang
LastEditTime: 2021-05-12 11:00:22
FilePath: /leetcode/90.子集-ii.py
'''
#
# @lc app=leetcode.cn id=90 lang=python
#
# [90] 子集 II
#

# @lc code=start
class Solution(object):
    def __init__(self):
        self.res = []

    def backtrace(self, nums, start, trace):
        self.res.append(trace[:])

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i-1]:
                continue
            trace.append(nums[i])
            self.backtrace(nums, i+1, trace)
            trace.pop()
        
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [[]]

        trace = []
        nums = sorted(nums)  # 注意这里要先排序
        self.backtrace(nums, 0, trace)
        return self.res

if __name__ == "__main__":
    nums = [1,2,2,1]
    print(Solution().subsetsWithDup(nums))

        

# @lc code=end

