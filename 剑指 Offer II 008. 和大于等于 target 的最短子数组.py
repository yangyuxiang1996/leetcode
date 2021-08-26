#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-25 22:44:41
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-25 23:03:04
FilePath: /leetcode/剑指 Offer II 008. 和大于等于 target 的最短子数组.py
Description: 
给定一个含有 n 个正整数的数组和一个正整数 target 。
找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
'''
class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        # 双指针
        i, j = 0, 0
        res = len(nums)+1
        tmp = 0
        while i < len(nums) and j < len(nums):
            tmp += nums[j]
            while tmp >= target:
                res = min(res, j-i+1)
                tmp -= nums[i]
                i += 1
            j += 1
        
        return res if res != len(nums)+1 else 0


if __name__ == "__main__":
    target = 11
    nums = [1,1,1,1,1,1,1,1]
    print(Solution().minSubArrayLen(target, nums))



        

