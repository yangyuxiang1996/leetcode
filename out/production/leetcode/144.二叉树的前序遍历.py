#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-27 08:26:45
LastEditors: yangyuxiang
LastEditTime: 2021-05-27 08:42:40
FilePath: /leetcode/144.二叉树的前序遍历.py
'''

#
# @lc app=leetcode.cn id=144 lang=python
#
# [144] 二叉树的前序遍历
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        算法：迭代
        基本思想：
        前序遍历顺序：中左右
        所以先将root节点入栈，然后出栈并保存，
        再将其右节点入栈，左节点入栈，然后依次pop并保存
        """
        if not root:
            return []
        stack = []
        res = []
        cur = root
        stack.append(cur)
        while stack:
            cur = stack.pop()
            res.append(cur.val)

            if cur.right:
                stack.append(cur.right)

            if cur.left:
                stack.append(cur.left)

        return res

    def preorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        算法：递归
        """
        if root is None:
            return []
        res = []

        def traversal(root, res):
            if not root:
                return
            res.append(root.val)
            traversal(root.left, res)
            traversal(root.right, res)

        traversal(root, res)
        return res


# @lc code=end
