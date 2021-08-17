#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-18 00:26:39
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-18 00:31:28
FilePath: /leetcode/剑指 Offer 32 - I. 从上到下打印二叉树.py
Description: 
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。
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
        :rtype: List[int]
        """
        # 层序遍历
        res = []
        stack = []
        cur = root
        stack.append(cur)
        while stack:
            n = len(stack)
            for i in range(n):
                cur = stack.pop(0)
                if cur:
                    res.append(cur.val)
                    stack.append(cur.left)
                    stack.append(cur.right)

        return res

            
