#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-26 08:02:36
LastEditors: yangyuxiang
LastEditTime: 2021-07-05 23:17:38
FilePath: /leetcode/53.最大子序和.py
'''
#
# @lc app=leetcode.cn id=53 lang=python
#
# [53] 最大子序和
#

# @lc code=start
class Solution(object):
    def maxSubArray0(self, nums):
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

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        解法：动态规划
        """
        dp = [0] * len(nums)
        dp[0] = nums[0]
        maxSum = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            if dp[i] > maxSum:
                maxSum = dp[i]

        return maxSum
# @lc code=end

