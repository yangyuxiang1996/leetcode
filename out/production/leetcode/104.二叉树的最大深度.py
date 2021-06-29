#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-17 18:29:00
LastEditors: yangyuxiang
LastEditTime: 2021-05-17 18:32:35
FilePath: /leetcode/104.二叉树的最大深度.py
'''
#
# @lc app=leetcode.cn id=104 lang=python
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        层次遍历
        """
        if not root:
            return 0
        
        q = [root]
        max_depth = 0
        while q:
            max_depth += 1
            sz = len(q)
            for i in range(sz):
                cur = q.pop(0)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return max_depth


    def maxDepth1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        递归
        """
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1
        
# @lc code=end

