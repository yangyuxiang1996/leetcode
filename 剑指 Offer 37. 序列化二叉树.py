#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-17 22:58:51
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-17 23:30:16
FilePath: /leetcode/剑指 Offer 37. 序列化二叉树.py
Description: 
请实现两个函数，分别用来序列化和反序列化二叉树。
你需要设计一个算法来实现二叉树的序列化与反序列化。
这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # 前序遍历
        stack = []
        preorder = ""
        cur = root
        stack.append(root)
        while cur or stack:
            cur = stack.pop()
            if cur:
                preorder += str(cur.val) + ","
            else:
                preorder += "null" + ","
            if cur:
                stack.append(cur.right)
                stack.append(cur.left)
        return preorder
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        preorder_list = data.split(',')
        def decode(data):
            if not data:
                return None
            val = data.pop(0)
            if val == "null":
                root = None
            else:
                root = TreeNode(int(val))
                root.left = decode(data)
                root.right = decode(data)
            return root
        
        root = decode(preorder_list)
        return root

        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
