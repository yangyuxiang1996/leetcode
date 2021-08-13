#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-13 14:05:10
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-13 14:19:30
FilePath: /leetcode/剑指 Offer 27. 二叉树的镜像.py
Description: 
请完成一个函数，输入一个二叉树，该函数输出它的镜像。
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mirrorTree0(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root
    
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        deque = []
        cur = root
        deque.append(root)
        while deque:
            n = len(deque)
            for i in range(n):
                cur = deque.pop(0)
                if cur.left:
                    deque.append(cur.left)
                if cur.right:
                    deque.append(cur.right)
                cur.left, cur.right = cur.right, cur.left
        return root
