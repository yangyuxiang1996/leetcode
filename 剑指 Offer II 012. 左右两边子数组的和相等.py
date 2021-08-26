#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-26 11:18:54
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-26 11:22:13
FilePath: /leetcode/剑指 Offer II 012. 左右两边子数组的和相等.py
Description: 
给你一个整数数组 nums ，请计算数组的 中心下标 。
数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。
如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。
如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1 。
输入：nums = [1,7,3,6,5,6]
输出：3
解释：
中心下标是 3 。
左侧数之和 sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11 ，
右侧数之和 sum = nums[4] + nums[5] = 5 + 6 = 11 ，二者相等。
'''
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left, right = [0] * n, [0] * n
        for i in range(1, n):
            left[i] = left[i-1] + nums[i-1]
        for j in range(n-2, -1, -1):
            right[j] = right[j+1] + nums[j+1]
        for i in range(n):
            if left[i] == right[i]:
                return i
        return -1


if __name__ == '__main__':
    nums = [1,7,3,6,5,6]
    print(Solution().pivotIndex(nums))



