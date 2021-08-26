#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-25 07:58:35
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-25 08:00:55
FilePath: /leetcode/剑指 Offer II 006. 排序数组中两个数字之和.py
Description: 
'''
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 双指针
        res = []
        left, right = 0, len(numbers)-1
        while left < right:
            if numbers[left] + numbers[right] == target:
                res = [left, right]
                break
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        return res
