#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-18 10:35:07
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-18 10:46:30
FilePath: /leetcode/剑指 Offer 32 - III. 从上到下打印二叉树 III.py
Description: 
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        res = []
        cur = root
        stack = [cur]
        l = 0
        while stack:
            tmp = []
            n = len(stack)
            for i in range(n):
                cur = stack.pop(0)
                if cur:
                    tmp.append(cur.val)
                    stack.append(cur.left)
                    stack.append(cur.right)
            if tmp:
                if l % 2 == 0:
                    res.append(tmp)
                else:
                    res.append(tmp[::-1])
            l += 1
        return res
                        
                        

                
                


