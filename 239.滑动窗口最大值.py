#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-11 08:17:35
LastEditors: yangyuxiang
LastEditTime: 2021-05-11 08:39:16
FilePath: /leetcode/239.滑动窗口最大值.py
'''
#
# @lc app=leetcode.cn id=239 lang=python
#
# [239] 滑动窗口最大值
#

# @lc code=start
import collections

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        queue = collections.deque()
        for i in range(k):
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)

        ans = [nums[queue[0]]]
        for i in range(k, len(nums)):
            if i - k >= queue[0]:
                queue.popleft()
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
            queue.append(i)

            ans.append(nums[queue[0]])

        return ans
            
             

            


        
# @lc code=end

