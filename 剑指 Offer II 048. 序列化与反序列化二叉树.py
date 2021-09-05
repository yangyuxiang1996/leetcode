#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-09-03 07:52:34
LastEditors: Yuxiang Yang
LastEditTime: 2021-09-03 08:24:17
FilePath: /leetcode/剑指 Offer II 048. 序列化与反序列化二叉树.py
Description: 
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
        nodes = []
        stack = [root]
        cur = root
        while cur or stack:
            cur = stack.pop()
            if cur:
                nodes.append(str(cur.val))
            else:
                nodes.append('null')
            
            if cur:
                stack.append(cur.right)
                stack.append(cur.left)
            
        return nodes


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(data):
            if not data:
                return None
            
            val = data.pop(0)
            if val == 'null':
                return None
            root = TreeNode(int(val))
            root.left = helper(data)
            root.right = helper(data)

            return root
        
        root = helper(data)
        print(self.serialize(root))
        return root


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    data = Codec().serialize(root)
    print(data) 
    print(Codec().deserialize(data))  

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
