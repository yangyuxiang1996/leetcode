#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-11 08:34:20
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-11 08:53:36
FilePath: /leetcode/剑指 Offer 03. 数组中重复的数字.py
Description: 
'''
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections
        m = collections.defaultdict(int)
        for num in nums:
            m[num] += 1
            if m[num] > 1:
                return num
        return -1

    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 原地置换
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[nums[i]] == nums[i]:
                return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1


