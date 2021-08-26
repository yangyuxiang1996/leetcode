#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-24 10:35:31
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-24 10:38:53
FilePath: /leetcode/剑指 Offer II 083. 没有重复元素集合的全排列.py
Description: 
给定一个不含重复数字的整数数组 nums ，返回其 所有可能的全排列 。可以 按任意顺序 返回答案。
输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        visited = [False] * len(nums)
        def helper(nums, path):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i in range(len(nums)):
                if visited[i] == True:
                    continue
                visited[i] = True
                path.append(nums[i])
                helper(nums, path)
                path.pop()
                visited[i] = False
        helper(nums, 0, [])
        return res

