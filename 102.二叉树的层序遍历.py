#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-28 07:55:52
LastEditors: yangyuxiang
LastEditTime: 2021-05-28 08:22:15
FilePath: /leetcode/102.二叉树的层序遍历.py
'''

#
# @lc app=leetcode.cn id=102 lang=python
#
# [102] 二叉树的层序遍历
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        BFS，宽度优先
        """
        if not root:
            return []

        stack = []
        res = []
        stack.append(root)
        while stack:
            n = len(stack)
            tmp = []
            for i in range(n):
                cur = stack.pop(0)
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
                tmp.append(cur.val)
            res.append(tmp)
        return res


# @lc code=end
