#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-19 22:31:32
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-19 23:36:18
FilePath: /leetcode/剑指 Offer 53 - I. 在排序数组中查找数字 I.py
Description: 
统计一个数字在排序数组中出现的次数。
输入: nums = [5,7,7,8,8,10], target = 8
输出: 2
'''
class Solution(object):
    def searchLeftBound(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        if left == len(nums) or nums[left] != target:
            return -1
        else:
            return left

    def searchRightBound(self, nums, target):
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if nums[right] != target or right == -1:
            return -1
        else:
            return left - 1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0

        left = self.searchLeftBound(nums, target)
        right = self.searchRightBound(nums, target)
        return right - left + 1 if left != -1 and right != -1 else 0

    def search0(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                res = 1
                i = mid + 1
                while i <= right and nums[i] == target:
                    res += 1
                    i += 1
                i = mid - 1
                while i >= left and nums[i] == target:
                    res += 1
                    i -= 1
                return res
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return 0


if __name__ == '__main__':
    nums = [1]
    target = 1
    print(Solution().searchLeftBound(nums, target))
    print(Solution().searchRightBound(nums, target))

