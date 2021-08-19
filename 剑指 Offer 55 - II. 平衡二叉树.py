#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-20 00:06:39
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-20 00:13:20
FilePath: /leetcode/剑指 Offer 55 - II. 平衡二叉树.py
Description: 
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。
如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def depth(self, root):
        if not root:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1 
        
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        left = self.depth(root.left)
        right = self.depth(root.right)
        
        return abs(left-right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

