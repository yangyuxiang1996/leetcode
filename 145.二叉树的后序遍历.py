#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-27 08:44:15
LastEditors: Yuxiang Yang
LastEditTime: 2021-07-30 11:26:17
FilePath: /leetcode/145.二叉树的后序遍历.py
'''

#
# @lc app=leetcode.cn id=145 lang=python
#
# [145] 二叉树的后序遍历
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverse(self, nums):
        left = 0
        right = len(nums) - 1
        while left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return nums

    def postorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        算法：迭代
        后序遍历顺序：左右中
        先中右左，再反转数组
        """
        if not root:
            return []
        stack = []
        res = []
        cur = root
        stack.append(cur)
        while stack:
            cur = stack.pop()
            res.append(cur.val)

            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)

        # 反转数组
        res = self.reverse(res)
        return res

    def postorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        算法：递归
        """
        if not root:
            return []
        res = []

        def traverse(root, res):
            if not root:
                return
            traverse(root.left, res)
            traverse(root.right, res)
            res.append(root.val)

        traverse(root, res)
        return res

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        算法：迭代
        后序遍历顺序：左右中
        """
        if not root:
            return []
        
        stack = []
        cur = root
        res = []

        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            cur = cur.left
        res = self.reverse(res)
        
        return res


# @lc code=end
