#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-20 08:25:59
LastEditors: yangyuxiang
LastEditTime: 2021-04-20 10:10:16
FilePath: /leetcode/124.二叉树中的最大路径和.py
'''
#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.maxSum =  -float('inf')
        
    def helper(self, root):
        if root == None:
            return 0
            
        left = max(0, self.helper(root.left))
        right = max(0, self.helper(root.right))

        self.maxSum = max(self.maxSum, left + right + root.val)

        return max(left, right) + root.val

    def maxPathSum(self, root):
        self.helper(root)
        return self.maxSum

if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    
    print(Solution().maxPathSum(root))
        
# @lc code=end