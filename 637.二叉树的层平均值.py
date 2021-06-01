#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-29 23:19:49
LastEditors: yangyuxiang
LastEditTime: 2021-05-29 23:24:48
FilePath: /leetcode/637.二叉树的层平均值.py
'''

#
# @lc app=leetcode.cn id=637 lang=python
#
# [637] 二叉树的层平均值
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        stack = deque()
        stack.append(root)
        res = []
        while stack:
            n = len(stack)
            tmp = 0.
            for _ in range(n):
                cur = stack.popleft()
                tmp += cur.val
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
            res.append(tmp / n)
        return res


# @lc code=end
