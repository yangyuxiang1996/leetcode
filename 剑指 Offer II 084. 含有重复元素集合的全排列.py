#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-24 10:41:34
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-24 10:50:17
FilePath: /leetcode/剑指 Offer II 084. 含有重复元素集合的全排列.py
Description: 
给定一个可包含重复数字的整数集合 nums ，按任意顺序 返回它所有不重复的全排列。
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
'''
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 同一层要剪枝, 子节点要剪枝
        # 数组先排序
        nums = sorted(nums)
        res = []
        visited = [False] * len(nums)
        def helper(nums, path):
            demo = []
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in demo:
                    continue
                if visited[i] == False:
                    demo.append(nums[i])
                    visited[i] = True
                    path.append(nums[i])
                    helper(nums, path)
                    path.pop()
                    visited[i] = False
        helper(nums, [])
        return res
