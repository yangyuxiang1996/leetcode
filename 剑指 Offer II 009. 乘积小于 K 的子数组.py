#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-25 23:26:12
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-25 23:55:32
FilePath: /leetcode/剑指 Offer II 009. 乘积小于 K 的子数组.py
Description: 
给定一个正整数数组 nums和整数 k ，请找出该数组内乘积小于 k 的连续的子数组的个数。
输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8 个乘积小于 100 的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
'''
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 双指针
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans


    def numSubarrayProductLessThanK0(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 暴力解法，超时
        count = 0
        last = 0
        for i in range(len(nums)):
            if nums[i] >= k:
                last = i
                continue
            tmp = 1
            for j in range(i, last-1, -1):
                tmp *= nums[j]
                if tmp < k:
                    count += 1
                else:
                    break
        return count





if __name__ == "__main__":
    nums = [10,5,2,6]
    k = 100
    print(Solution().numSubarrayProductLessThanK(nums, k))
                


