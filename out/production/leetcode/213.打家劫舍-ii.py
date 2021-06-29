#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-04 12:00:29
LastEditors: yangyuxiang
LastEditTime: 2021-05-04 12:05:50
FilePath: /leetcode/213.打家劫舍-ii.py
'''
#
# @lc app=leetcode.cn id=213 lang=python
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]

        def helper(nums, start, end):
            n = len(nums)
            
            d_i_1 = d_i_2 = 0 
            d_i = 0

            for i in range(start, end+1):
                d_i = max(d_i_1, nums[i] + d_i_2)
                d_i_2 = d_i_1
                d_i_1 = d_i

            return d_i
        
        res = max(helper(nums, 0, n-2), \
            helper(nums, 1, n-1)
            )

        return res

        
# @lc code=end

