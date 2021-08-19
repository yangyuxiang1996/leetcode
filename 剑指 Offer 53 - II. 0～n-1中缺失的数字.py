#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-19 23:38:13
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-19 23:45:20
FilePath: /leetcode/剑指 Offer 53 - II. 0～n-1中缺失的数字.PY
Description: 
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
输入: [0,1,3]
输出: 2
'''
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for i in range(len(nums)):
        #     if nums[i] != i:
        #         return i
        # return i + 1

        # 有序，二分
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1
        return left
    


