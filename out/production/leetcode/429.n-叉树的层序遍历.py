#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-29 23:28:31
LastEditors: yangyuxiang
LastEditTime: 2021-05-29 23:33:54
FilePath: /leetcode/429.n-叉树的层序遍历.py
'''
#
# @lc app=leetcode.cn id=429 lang=python
#
# [429] N 叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []

        from collections import deque
        stack = deque()
        stack.append(root)
        res = []
        while stack:
            n = len(stack)
            tmp = []
            for i in range(n):
                cur = stack.popleft()
                tmp.append(cur.val)
                if cur.children:
                    for child in cur.children:
                        stack.append(child)
            res.append(tmp)
        return res


# @lc code=end
