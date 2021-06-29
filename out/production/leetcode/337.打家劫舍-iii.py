#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-04 12:08:01
LastEditors: yangyuxiang
LastEditTime: 2021-05-04 12:19:06
FilePath: /leetcode/337.打家劫舍-iii.py
'''
#
# @lc app=leetcode.cn id=337 lang=python
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        memo = {}
        def helper(root):
            if not root:
                return 0
            if root in memo:
                return memo[root]
            
            do = root.val
            if root.left is not None:
                do = do + helper(root.left.left) + helper(root.left.right)
            
            if root.right is not None:
                do = do + helper(root.right.left) + helper(root.right.right)
            
            not_do = helper(root.left) + helper(root.right)
            res = max(do, not_do)
            memo[root] = res

            return res

        res = helper(root)
        
        return res
            

# @lc code=end

