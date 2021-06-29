#!/usr/bin/env python
# coding=utf-8
'''
Description:  
Author: yangyuxiang
Date: 2021-05-29 23:41:49
LastEditors: yangyuxiang
LastEditTime: 2021-05-30 10:51:16
FilePath: /leetcode/116.填充每个节点的下一个右侧节点指针.py
'''
#
# @lc app=leetcode.cn id=116 lang=python
#
# [116] 填充每个节点的下一个右侧节点指针
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


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        递归法
        此题规定了二叉树是完美二叉树，所以一个节点要么是叶子节点，要么包含左右两个节点
        """
        if not root:
            return root
        if root.left:  # 说明有左右子树
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            else:
                root.right.next = None
            self.connect(root.left)
            self.connect(root.right)
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
