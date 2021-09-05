#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-31 08:05:46
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-31 08:25:07
FilePath: /leetcode/剑指 Offer II 090. 环形房屋偷盗.py
Description: 
一个专业的小偷，计划偷窃一个环形街道上沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
给定一个代表每个房屋存放金额的非负整数数组 nums ，请计算 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        # 分两种情况：偷第一家，不偷第一家
        def helper(nums, start, end):
            a = [nums[start], 0]
            for i in range(start+1, end+1):
                tmp = a[1]
                a[1] = max(a[0], a[1])
                a[0] = max(a[0], tmp+nums[i])

            return max(a)

        first = helper(nums, 0, len(nums)-2)
        second = helper(nums, 1, len(nums)-1)
        return max(first, second)

            
