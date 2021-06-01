#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-22 07:56:50
LastEditors: yangyuxiang
LastEditTime: 2021-05-14 08:20:23
FilePath: /leetcode/1.两数之和.py
'''
#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp = {}
        for i, num in enumerate(nums):
            if num not in tmp:
                tmp[target-num] = i
            else:
                return [tmp[num], i]
        # tmp = {}
        # for i in range(len(nums)):
        #     tmp[nums[i]] = i

        # for i in range(len(nums)):
        #     other = target - nums[i]
        #     if other in tmp and tmp[other] != i:
        #         return [i, tmp[other]]

        # return [-1, -1]                

# @lc code=end

