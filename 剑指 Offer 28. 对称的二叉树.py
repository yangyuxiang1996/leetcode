#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-13 14:21:21
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-13 15:16:57
FilePath: /leetcode/剑指 Offer 28. 对称的二叉树.py
Description: 
请实现一个函数，用来判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric0(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        
        deque = []
        cur = root
        deque.append(cur)
        while deque:
            n = len(deque)
            stack = []
            for i in range(n):
                cur = deque.pop(0)
                if cur:
                    stack.append(str(cur.val))
                else:
                    stack.append("null")
                deque.append(cur.left)
                deque.append(cur.right)
            l ,r = 0, len(stack)-1
            while l <= r:
                if stack[l] != stack[r]:
                    return False
                l += 1
                r -= 1
        return True

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(left, right):
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            
            return helper(left.left, right.right) and helper(left.right, right.left)
        
        if not root:
            return True
        
        return helper(root.left, root.right)
                    
        
