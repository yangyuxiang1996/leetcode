#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-26 08:02:36
LastEditors: yangyuxiang
LastEditTime: 2021-04-26 08:19:43
FilePath: /leetcode/53.最大子序和.py
'''
#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子序和
#

# @lc code=start
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        
        maxsum = -float('inf')
        sum = 0
        for i in range(len(nums)):
            sum = max(sum+nums[i], nums[i])
            maxsum = max(maxsum, sum)

        return maxsum
# @lc code=end

