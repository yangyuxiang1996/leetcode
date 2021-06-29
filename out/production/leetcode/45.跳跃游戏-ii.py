#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-23 22:11:07
LastEditors: yangyuxiang
LastEditTime: 2021-05-23 23:11:51
FilePath: /leetcode/45.跳跃游戏-ii.py
'''

#
# @lc app=leetcode.cn id=45 lang=python
#
# [45] 跳跃游戏 II
#


# @lc code=start
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        解法:贪心
        """
        n = len(nums)
        if n <= 1:
            return 0

        farthest = end = nums[0]
        jump = 1

        for i in range(1, n - 1):
            farthest = max(farthest, nums[i] + i)
            if end == i:
                end = farthest
                jump += 1
        return jump

    def jump1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        解法:动态规划
        """
        n = len(nums)
        memo = [n for _ in range(n)]

        def dp(nums, p):
            if p >= len(nums) - 1:
                return 0
            if memo[p] < n:
                return memo[p]
            steps = nums[p]
            for i in range(1, steps + 1):
                sub = dp(nums, p + i)
                memo[p] = min(memo[p], sub + 1)

            return memo[p]

        return dp(nums, 0)


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    print(Solution().jump(nums))
# @lc code=end
