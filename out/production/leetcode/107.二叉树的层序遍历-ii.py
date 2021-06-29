#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-28 08:22:53
LastEditors: yangyuxiang
LastEditTime: 2021-05-28 08:47:44
FilePath: /leetcode/107.二叉树的层序遍历-ii.py
'''

#
# @lc app=leetcode.cn id=107 lang=python
#
# [107] 二叉树的层序遍历 II
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        stack = []
        res = []
        stack.append(root)
        while stack:
            n = len(stack)
            tmp = []
            for i in range(n):
                cur = stack.pop(0)
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
                tmp.append(cur.val)
            res.append(tmp)

        left, right = 0, len(res) - 1
        while left <= right:
            res[left], res[right] = res[right], res[left]
            left+=1
            right-=1
        return res


# @lc code=end
