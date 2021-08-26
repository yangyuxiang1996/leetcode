#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-25 08:10:40
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-25 09:05:16
FilePath: /leetcode/剑指 Offer II 007. 数组中和为 0 的三个数.py
Description: 
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a ，b ，c ，
使得 a + b + c = 0 ？请找出所有和为 0 且 不重复 的三元组。
'''
class Solution(object):
    def twoSum(self, nums, target):
        # 有序
        res = []
        left, right = 0, len(nums)-1
        while left < right:
            lo, hi = nums[left], nums[right]
            if nums[left] + nums[right] == target:
                res.append([nums[left], nums[right]])
                while left < right and nums[left] == lo:
                    left += 1
                while left < right and nums[right] == hi:
                    right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                right -= 1
        return res
        
        
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 回溯，超时
        n = len(nums)
        if n < 3:
            return []
        nums = sorted(nums)
        res = []
        demo = []
        for i in range(n):
            if nums[i] in demo:
                continue
            if nums[i] > 0:
                break
            demo.append(nums[i])
            tmps = self.twoSum(nums[i+1:], -nums[i])
            if tmps != []:
                for tmp in tmps: 
                    tmp.append(nums[i])
                    res.append(tmp)
        return res


    def threeSum0(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 回溯，超时
        n = len(nums)
        if n < 3:
            return []
        nums = sorted(nums)
        res = []

        def helper(nums, start, path):
            demo = []
            if len(path) == 3:
                if sum(path) == 0:
                    res.append(path[:])
                return
            for i in range(start, len(nums)):
                if nums[i] in demo:
                    continue
                demo.append(nums[i])
                path.append(nums[i])
                helper(nums, i+1, path)
                path.pop()
        
        helper(nums, 0, [])
        return res


if __name__ == '__main__':
    nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
    print(Solution().threeSum(nums))