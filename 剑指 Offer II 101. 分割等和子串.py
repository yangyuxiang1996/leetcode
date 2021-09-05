#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-09-04 21:54:45
LastEditors: Yuxiang Yang
LastEditTime: 2021-09-04 23:24:41
FilePath: /leetcode/剑指 Offer II 101. 分割等和子串.py
Description: 
给定一个非空的正整数数组 nums ，请判断能否将这些数字分成元素和相等的两部分。
输入：nums = [1,5,11,5]
输出：true
解释：nums 可以分割成 [1, 5, 5] 和 [11] 。
'''
class Solution(object):
    def canPartition0(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 背包问题
        if len(nums) == 1:
            return False
        
        sum_ = sum(nums)
        if sum_ % 2 == 1:
            return False
        
        target = sum_ // 2

        dp = [[False] * (target + 1) for _ in range(len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][0] = True
        
        for i in range(1, len(nums)+1):
            for j in range(1, target+1):
                if j - nums[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]

        return dp[-1][-1]


    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 背包问题, 状态压缩
        if len(nums) == 1:
            return False
        
        sum_ = sum(nums)
        if sum_ % 2 == 1:
            return False
        
        target = sum_ // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for i in range(len(nums)):
            for j in range(target, -1, -1):
                if j - nums[i] >= 0:
                    dp[j] = dp[j] or dp[j-nums[i]]
        
        return dp[-1]



    





if __name__ == '__main__':
    nums = [1,2,3,6,4]
    print(Solution().canPartition(nums))




