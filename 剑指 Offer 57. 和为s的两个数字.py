#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-19 00:01:32
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-19 00:10:14
FilePath: /leetcode/剑指 Offer 57. 和为s的两个数字.py
Description: 
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。
输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]
'''
class Solution(object):
    def twoSum0(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # hashmap
        m = {}
        for i in range(len(nums)):
            if nums[i] not in m:
                m[target - nums[i]] = i
            else:
                return [target - nums[i], nums[i]]
        return []
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 注意到是递增，因此可以用双指针
        if len(nums) < 2:
            return []
        
        left, right = 0, len(nums)-1
        while left <= right:
            if nums[left] + nums[right] == target:
                return [nums[left], nums[right]]
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        return []

