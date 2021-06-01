#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-12 10:08:49
LastEditors: yangyuxiang
LastEditTime: 2021-05-12 10:28:03
FilePath: /leetcode/78.子集.py
'''
#
# @lc app=leetcode.cn id=78 lang=python
#
# [78] 子集
#

# @lc code=start
class Solution(object):
    def __init__(self):
        self.res = []

    def backtrace(self, nums, start, trace):
        
        self.res.append(trace[:]) # 将当前叶子节点加入result
        
        for i in range(start, len(nums)): # 选择
            trace.append(nums[i]) # 添加选择
            self.backtrace(nums, i+1, trace) # 回溯
            trace.pop() # 移除当前选择

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        回溯法，使用start指针避免重复子集
        """
        if not nums:
            return [[]]

        trace = []
        self.backtrace(nums, 0, trace)
        return self.res


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().subsets(nums))

        

        
# @lc code=end

