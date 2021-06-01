#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-29 23:34:53
LastEditors: yangyuxiang
LastEditTime: 2021-05-29 23:39:09
FilePath: /leetcode/515.在每个树行中找最大值.py
'''

#
# @lc app=leetcode.cn id=515 lang=python
#
# [515] 在每个树行中找最大值
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        import collections
        stack = collections.deque()
        stack.append(root)
        res = []

        while stack:
            n = len(stack)
            max_v = float('-inf')
            for _ in range(n):
                cur = stack.popleft()
                max_v = max(max_v, cur.val)
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
            res.append(max_v)
        return res


# @lc code=end
