#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-19 23:46:34
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-20 00:00:45
FilePath: /leetcode/剑指 Offer 54. 二叉搜索树的第k大节点.py
Description: 
给定一棵二叉搜索树，请找出其中第k大的节点。
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthLargest0(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # 中序遍历
        res = []
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur:
                res.append(cur.val)
                cur = cur.right
        return res[len(res)-k]

    def kthLargest1(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # 中序遍历
        res = []
        stack = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res[len(res)-k]

    def kthLargest1(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # 中序遍历反过来，即左中右 -> 右中左
        stack = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.right
            else:
                cur = stack.pop()
                k -= 1
                if k == 0:
                    return cur.val
                cur = cur.left
        return -1
                
