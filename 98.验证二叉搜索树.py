#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-06 18:14:40
LastEditors: yangyuxiang
LastEditTime: 2021-05-06 18:49:21
FilePath: /leetcode/98.验证二叉搜索树.py
'''
#
# @lc app=leetcode.cn id=98 lang=python
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.min_val = float("-inf")
        
    def isValidBST(self, root):
        if root is None:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val <= self.min_val:
            return False
        self.min_val = root.val
        if not self.isValidBST(root.right):
            return False
        
        return True
        
        
    def isValidBST1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if not root.left and not root.right:
            return True
        if not root.left and root.val >= root.right.val:
            return False
        if not root.right and root.val <= root.left.val:
             return False

        output = self.inOrder(root, [])
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False
        return True
            

    def inOrder(self, root, output):
        if not root:
            return
        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)
        return output
        

        
# @lc code=end

