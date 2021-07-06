#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-23 21:54:43
LastEditors: yangyuxiang
LastEditTime: 2021-07-06 08:23:57
FilePath: /leetcode/55.跳跃游戏.py
'''

#
# @lc app=leetcode.cn id=55 lang=python
#
# [55] 跳跃游戏
#


# @lc code=start
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # n = len(nums)
        # max_step = 0
        # for i in range(n-1):
        #     max_step = max(max_step, nums[i]+i)
        #     if max_step <= i:
        #         return False
        # return True

        n = len(nums)
        if n == 1:
            return True
        cover = 0
        i = 0
        while i <= cover:
            cover = max(cover, nums[i]+i)
            if cover >= len(nums)-1:
                return True
            i += 1
        return False



# @lc code=end
