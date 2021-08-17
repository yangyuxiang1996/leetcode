#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-18 00:32:14
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-18 00:34:51
FilePath: /leetcode/剑指 Offer 32 - II. 从上到下打印二叉树 II.py
Description: 
从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
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
                if cur:
                    tmp.append(cur.val)
                    stack.append(cur.left)
                    stack.append(cur.right)
            if tmp:
                res.append(tmp)

        return res

        
