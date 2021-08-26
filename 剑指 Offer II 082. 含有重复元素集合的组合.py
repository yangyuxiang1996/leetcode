#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-24 10:18:32
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-24 10:30:03
FilePath: /leetcode/剑指 Offer II 082. 含有重复元素集合的组合.py
Description: 
给定一个可能有重复数字的整数数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。
candidates 中的每个数字在每个组合中只能使用一次，解集不能包含重复的组合。 
输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
'''
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 每一层，不能用重复的数字
        import copy
        def helper(candidates, target, path, tmp, start):
            demo = []
            if tmp == target:
                res.append(copy.deepcopy(path))
                return
            if tmp > target:
                return

            for i in range(start, len(candidates)):
                if candidates[i] in demo:
                    continue
                demo.append(candidates[i])
                path.append(candidates[i])
                tmp += candidates[i]
                helper(candidates, target, path, tmp, i+1)
                tmp -= candidates[i]
                path.pop()

        res = []
        candidates = sorted(candidates) # 需要先排序
        helper(candidates, target, [], 0, 0)
        return res
