#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-24 10:05:21
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-24 10:17:37
FilePath: /leetcode/剑指 Offer II 081. 允许重复选择元素的组合.py
Description: 
给定一个无重复元素的正整数数组 candidates 和一个正整数 target ，找出 candidates 中所有可以使数字和为目标数 target 的唯一组合。

candidates 中的数字可以无限制重复被选取。如果至少一个所选数字数量不同，则两种组合是唯一的。 

对于给定的输入，保证和为 target 的唯一组合数少于 150 个。
'''
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        from copy import deepcopy
        def helper(candidates, start, target, path, tmp):
            if tmp == target:
                res.append(deepcopy(path))
                return
            if tmp > target:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                tmp += candidates[i]
                helper(candidates, i, target, path, tmp) # 注意这里从i作为下一次的起点
                tmp -= candidates[i]
                path.pop()

        res = []
        helper(candidates, 0, target, [], 0)
        return res

