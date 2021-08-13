#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-13 10:16:29
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-13 10:52:42
FilePath: /leetcode/剑指 Offer 26. 树的子结构.py
Description: 
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构， 即 A中有出现和B相同的结构和节点值。
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasSameStruct(self, rootA, rootB):
        if not rootB: 
            return True
        if not rootA or rootA.val != rootB.val: 
            return False
        
        return self.hasSameStruct(rootA.left, rootB.left) \
                and self.hasSameStruct(rootA.right, rootB.right)

    def isSubStructure(self, rootA, rootB):
        """
        :type rootA: TreeNode
        :type rootB: TreeNode
        :rtype: bool
        """
        if not rootA or not rootB:
            return False
        
        
        if rootA.val == rootB.val and self.hasSameStruct(rootA, rootB):
            return True
        
        return self.isSubStructure(rootA.left, rootB) or \
            self.isSubStructure(rootA.right, rootB)
        
        

        
            
        
        
