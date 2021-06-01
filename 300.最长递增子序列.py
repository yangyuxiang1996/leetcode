#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-25 15:04:38
LastEditors: yangyuxiang
LastEditTime: 2021-04-25 15:11:08
FilePath: /leetcode/300.最长递增子序列.py
'''
#
# @lc app=leetcode.cn id=300 lang=python
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)  # 状态转移方程

        result = dp[0]
        for i in range(len(dp)):
            if dp[i] > result:
                result = dp[i]

        return result

# @lc code=end

