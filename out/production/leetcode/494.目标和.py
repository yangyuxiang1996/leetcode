#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-04 21:15:55
LastEditors: yangyuxiang
LastEditTime: 2021-05-04 22:13:10
FilePath: /leetcode/494.目标和.py
'''
#
# @lc app=leetcode.cn id=494 lang=python
#
# [494] 目标和
#

# @lc code=start
class Solution(object):
    def __init__(self):
        self.res = 0
    def backtrack(self, nums, i, tmp, target):
            if i == len(nums):
                if tmp == target:
                    self.res += 1
                return

            for op in [1, -1]:
                tmp += op * nums[i]
                self.backtrack(nums, i+1, tmp, target)
                tmp -= op * nums[i]
    
    def findTargetSumWays1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        self.backtrack(nums, 0, 0, target)

        return self.res

    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        s = sum(nums)
        if s < target or (target + s) % 2 == 1:
            return 0
        
        def subset(nums, sum):
            n = len(nums)
            dp = [[0] * (sum + 1) for _ in range(n+1)]
            for i in range(n + 1):
                dp[i][0] = 1
            
            for i in range(1, n + 1):
                for j in range(0, sum+1):
                    if j - nums[i-1] >= 0:
                        dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
                    else:
                        dp[i][j] = dp[i-1][j]
            return dp[n][sum]
                    

        return subset(nums, (target + s) // 2)

        



if __name__ == '__main__':
    nums = [7,46,36,49,5,34,25,39,41,38,49,47,17,11,1,41,7,16,23,13]
    target = 3
    print(Solution().findTargetSumWays(nums, target))
        
# @lc code=end

