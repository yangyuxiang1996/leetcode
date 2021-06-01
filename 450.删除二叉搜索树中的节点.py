#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-06 22:29:48
LastEditors: yangyuxiang
LastEditTime: 2021-05-06 23:04:12
FilePath: /leetcode/450.删除二叉搜索树中的节点.py
'''
#
# @lc app=leetcode.cn id=450 lang=python
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def deleteNode(self, root, key):
        if not root:
            return None
        if root.val == key:
            if root.right:
                now = root.right
                while now.left:
                    now = now.left
                now.left = root.left
                return root.right
            else:
                return root.left


        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        else:
            root.left = self.deleteNode(root.left, key)
        
        return root
            

    def deleteNode1(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        out = []
        def inOrder(root):
            if root:
                inOrder(root.left)
                out.append(root.val)
                inOrder(root.right)
        inOrder(root)

        if key not in out:
            return root

        out.remove(key)
        
        def listToBST(nums):
            if not nums:
                return None

            left = 0
            right = len(nums)
            mid = (left + right) // 2

            root = TreeNode(nums[mid])
            root.left = listToBST(nums[:mid])
            root.right = listToBST(nums[mid+1:])

            return root

        return listToBST(out)
        
# @lc code=end

