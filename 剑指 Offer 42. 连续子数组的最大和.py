#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-17 10:03:18
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-17 10:13:51
FilePath: /leetcode/剑指 Offer 42. 连续子数组的最大和.py
Description: 
输入一个整型数组，数组中的一个或连续多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)。
'''
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0] * (n+1)
        res = float("-inf")
        for i in range(1, n+1):
            dp[i] = max(nums[i-1], dp[i-1]+nums[i-1])
            res = max(res, dp[i])
        return res
            

