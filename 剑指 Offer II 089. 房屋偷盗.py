#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-26 07:38:38
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-26 08:18:15
FilePath: /leetcode/剑指 Offer II 089. 房屋偷盗.py
Description: 
一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响小偷偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，
如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。
输入：nums = [1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划
        n = len(nums)
        if n < 2:
            return max(nums)
        
        dp = [nums[0], 0]
        for i in range(1, len(nums)):
            dp[0], dp[1] = dp[1] + nums[i], max(dp[0], dp[1])

        return max(dp)
        


