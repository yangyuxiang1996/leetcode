#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-22 07:56:50
LastEditors: yangyuxiang
LastEditTime: 2021-06-23 08:09:02
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
        m = {}
        for i in range(len(nums)):
            # if nums[i] in m:
            #     return [m[nums[i]], i]
            # else:
            #     m[target-nums[i]] = i
            
            if target-nums[i] in m:
                return [m[target-nums[i]], i]
            else:
                m[nums[i]] = i
                

# @lc code=end

