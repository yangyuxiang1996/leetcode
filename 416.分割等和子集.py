#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-30 16:02:25
LastEditors: yangyuxiang
LastEditTime: 2021-04-30 17:59:17
FilePath: /leetcode/416.分割等和子集.py
'''
#
# @lc app=leetcode.cn id=416 lang=python
#
# [416] 分割等和子集
#

# @lc code=start
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n <= 1:
            return False
        
        s = sum(nums)
        if s % 2 == 1: # 奇数肯定不可分割成和相等的两部分
            return False

        s = s // 2
        # dp = [[False] * (s+1) for _ in range(n+1)]
        # for i in range(len(dp)):
        #     dp[i][0] = True
        
        # for i in range(1, n+1):
        #     for j in range(1, s+1):
        #         if j - nums[i-1] < 0:
        #             dp[i][j] = dp[i-1][j]
        #         else:
        #             dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]

        dp = [False] * (s+1)
        dp[0] = True

        for i in range(0, n):
            for j in range(s, -1, -1):
                if j - nums[i] >= 0:
                    dp[j] = dp[j] or dp[j-nums[i]]


        return dp[s]

        
        
        
        
        
# @lc code=end

