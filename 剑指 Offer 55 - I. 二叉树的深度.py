#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-18 23:06:36
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-18 23:16:00
FilePath: /leetcode/剑指 Offer 55 - I. 二叉树的深度.py
Description: 
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 递归
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 层次遍历
        if not root:
            return 0
        
        stack = [root]
        cur = root
        res = 0
        while stack:
            n = len(stack)
            for i in range(n):
                cur = stack.pop(0)
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
            res += 1
        return res