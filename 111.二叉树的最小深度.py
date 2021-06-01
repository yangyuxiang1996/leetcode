#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-04-21 08:58:18
LastEditors: yangyuxiang
LastEditTime: 2021-05-31 08:48:27
FilePath: /leetcode/111.二叉树的最小深度.py
'''
#
# @lc app=leetcode.cn id=111 lang=python
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def minDepth1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        :迭代
        """

        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        q = [root]
        step = 1
        while q:
            s = len(q)
            for i in range(s):
                cur = q.pop(0) 
                if not cur.left and not cur.right:
                    return step
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

            step += 1

        return step
    
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        :递归
        """
        if not root:
            return 0
        left_min = self.minDepth(root.left)
        right_min = self.minDepth(root.right)
        if not root.left and root.right:
            return right_min+1
        if root.left and not root.right:
            return left_min+1
        return 1 + min(left_min, right_min)
            
    

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print(Solution().minDepth(root))

    
            
# @lc code=end

