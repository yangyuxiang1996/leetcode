#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-13 21:52:38
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-13 22:01:32
FilePath: /leetcode/剑指 Offer 21. 调整数组顺序使奇数位于偶数前面.py
Description: 
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
'''
class Solution(object):
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] % 2 == 1:
                left += 1
            while left <= right and nums[right] % 2 == 0:
                right -= 1
            if left > right:
                break
            nums[left], nums[right] = nums[right], nums[left]
        return nums

if __name__ == '__main__':
    nums = [1,3,5]
    Solution().exchange(nums)
    print(nums)
