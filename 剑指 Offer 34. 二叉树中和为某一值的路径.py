#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-18 22:44:27
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-18 23:06:04
FilePath: /leetcode/剑指 Offer 34. 二叉树中和为某一值的路径.py
Description: 
输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from copy import deepcopy
class Solution(object):
    def __init__(self):
        self.res = []
    
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.helper(root, target, [root.val])
        return self.res

    def helper(self, root, target, path):
        if not root.left and not root.right:
            if target == root.val:
                self.res.append(deepcopy(path))
            return
        
        if root.left:
            path.append(root.left.val)
            self.helper(root.left, target-root.val, path)
            path.pop()
        if root.right:
            path.append(root.right.val)
            self.helper(root.right, target-root.val, path)
            path.pop()

    def pathSum0(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[List[int]]
        """
        self.helper0(root, target, [])
        return self.res

    def helper0(self, root, target, path):
        if not root:
            return
        if not root.left and not root.right:
            if target == root.val:
                path.append(root.val)
                self.res.append(deepcopy(path))
                path.pop()
            return
        
        path.append(root.val)
        self.helper0(root.left, target-root.val, path)
        self.helper0(root.right, target-root.val, path)
        path.pop()
    


        
