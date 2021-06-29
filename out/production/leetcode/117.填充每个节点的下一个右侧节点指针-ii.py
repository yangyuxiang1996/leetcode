#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-30 10:05:20
LastEditors: yangyuxiang
LastEditTime: 2021-05-30 11:05:29
FilePath: /leetcode/117.填充每个节点的下一个右侧节点指针-ii.py
'''
#
# @lc app=leetcode.cn id=117 lang=python
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def find_next(self, root):
        if not root:
            return root
        if root.left:
            return root.left
        if root.right:
            return root.right
        return self.find_next(root.next)

    def connect2(self, root):
        """
        :type root: Node
        :rtype: Node
        递归
        """
        if not root:
            return root
        if root.left:
            root.left.next = root.right if root.right else self.find_next(
                root.next)
        if root.right:
            root.right.next = self.find_next(root.next)
        self.connect(root.right)
        self.connect(root.left)
        return root

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        迭代：哑节点指代每一层的头节点，利用next指针遍历
        """
        if not root:
            return root
        cur = root
        while cur:
            dummy = pre = Node(0)
            while cur:
                if cur.left:
                    pre.next = cur.left
                    pre = pre.next
                if cur.right:
                    pre.next = cur.right
                    pre = pre.next
                cur = cur.next
            cur = dummy.next
        return root

    def connect1(self, root):
        """
        :type root: Node
        :rtype: Node
        迭代法
        """
        if not root:
            return root
        stack = []
        stack.append(root)
        while stack:
            n = len(stack)
            pre = None
            cur = None
            for i in range(n):
                if i == 0:
                    pre = stack.pop(0)
                    cur = pre
                else:
                    cur = stack.pop(0)
                    pre.next = cur
                    pre = pre.next
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
            pre.next = None

        return root


# @lc code=end
