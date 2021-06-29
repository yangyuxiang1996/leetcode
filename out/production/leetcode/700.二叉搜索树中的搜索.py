#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-06 21:12:31
LastEditors: yangyuxiang
LastEditTime: 2021-05-06 21:18:11
FilePath: /leetcode/700.二叉搜索树中的搜索.py
'''
#
# @lc app=leetcode.cn id=700 lang=python
#
# [700] 二叉搜索树中的搜索
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        if root.val == val:
            return root
        
        if root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)

# @lc code=end

