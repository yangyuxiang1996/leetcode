#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-12 22:42:48
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-12 22:56:22
FilePath: /leetcode/剑指 Offer 07. 重建二叉树.py
Description: 
输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None
        val = preorder.pop(0)
        root = TreeNode(val)
        root_index = inorder.index(val)
        left_inorder, right_inorder = inorder[:root_index], \
            inorder[root_index + 1:]
        left_preorder, right_preorder = preorder[:len(left_inorder)], \
            preorder[len(left_inorder):]
        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)
        return root

