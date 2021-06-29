#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-23 10:20:35
LastEditors: yangyuxiang
LastEditTime: 2021-05-23 11:38:49
FilePath: /leetcode/26.删除排序数组中的重复项.py
'''

#
# @lc app=leetcode.cn id=26 lang=python
#
# [26] 删除排序数组中的重复项
#


# @lc code=start
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        双指针
        """
        # slow, fast = 0, 1
        # while fast < len(nums):
        #     if nums[fast] == nums[slow]:
        #         fast += 1
        #     else:
        #         slow += 1
        #         nums[slow] = nums[fast]

        # return slow + 1
        slow = fast = 1
        while fast < len(nums):
            if nums[fast] != nums[slow-1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow


# @lc code=end
