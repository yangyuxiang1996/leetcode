#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-30 11:14:39
LastEditors: yangyuxiang
LastEditTime: 2021-05-30 11:23:43
FilePath: /leetcode/226.翻转二叉树.py
'''

#
# @lc app=leetcode.cn id=226 lang=python
#
# [226] 翻转二叉树
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree1(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        解法：递归
        """
        if not root:
            return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(
            root.left)
        return root

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        解法：迭代
        """
        if not root:
            return root
        import collections
        st = collections.deque()
        st.append(root)
        while st:
            n = len(st)
            for _ in range(n):
                node = st.popleft()
                if node:
                    node.left, node.right = node.right, node.left
                    st.append(node.left)
                    st.append(node.right)
        return root


# @lc code=end
