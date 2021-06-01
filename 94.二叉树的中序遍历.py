#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-27 07:52:19
LastEditors: yangyuxiang
LastEditTime: 2021-05-28 07:53:49
FilePath: /leetcode/94.二叉树的中序遍历.py
'''

#
# @lc app=leetcode.cn id=94 lang=python
#
# [94] 二叉树的中序遍历
#


# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal2(self, root):
        if not root:
            return []
        stack = []
        res = []
        stack.append(root)
        while stack:
            cur = stack[-1]
            if cur:
                stack.pop()
                if cur.right:
                    stack.append(cur.right)
                stack.append(cur)
                stack.append(None)
                if cur.left:
                    stack.append(cur.left)
            else:
                stack.pop()  # 碰到None，pop掉取下一个元素
                node = stack.pop()
                res.append(node.val)
        return res

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        算法：栈+迭代
        基本思路：
        明确中序遍历的顺序：左中右，
        所以首先要先遍历到最左边的节点，并不断将节点放入栈中；
        到达最左边之后，开始从栈中弹出元素，并保存在数组中；
        每弹出一个元素，都要判断其有没有左子树，然后重复上述过程
        """
        if not root:
            return []

        stack = []  # 栈用于访问二叉树
        res = []  # 结果数组
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if cur is not None:
                    res.append(cur.val)
                    cur = cur.right

        return res

    def inorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        算法：递归
        """
        if not root:
            return []

        res = []

        def traversal(root, res):
            if not root:
                return
            traversal(root.left, res)
            res.append(root.val)
            traversal(root.right, res)

        traversal(root, res)
        return res


# @lc code=end
