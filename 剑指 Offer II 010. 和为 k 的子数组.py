#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-26 08:23:53
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-26 08:45:36
FilePath: /leetcode/剑指 Offer II 010. 和为 k 的子数组.py
Description: 
给定一个整数数组和一个整数 k ，请找到该数组中和为 k 的连续子数组的个数。
'''
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums) == 1:
            if nums[0] == k:
                return 1
            else:
                return 0
        import collections
        m = collections.defaultdict(int)
        m[0] = 1
        sum_i, sum_j, count = 0, 0, 0
        for j in range(len(nums)):
            sum_j += nums[j]
            m[sum_j] += 1
            sum_i = sum_j - k
            if sum_i in m:
                count += m[sum_i]
            
        return count


if __name__ == '__main__':
    nums = [1,2,3]
    k=3
    print(Solution().subarraySum(nums, k))