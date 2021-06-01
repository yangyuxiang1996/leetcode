#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-14 08:21:46
LastEditors: yangyuxiang
LastEditTime: 2021-05-14 08:25:30
FilePath: /leetcode/167.两数之和-ii-输入有序数组.py
'''
#
# @lc app=leetcode.cn id=167 lang=python
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers)-1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left+1, right+1]
            elif s > target:
                right -= 1
            else:
                left += 1

        return [-1, -1]


        
# @lc code=end

