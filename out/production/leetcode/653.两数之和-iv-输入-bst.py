#!/usr/bin/env python
# coding=utf-8
'''
Description: 
Author: yangyuxiang
Date: 2021-05-15 08:50:35
LastEditors: yangyuxiang
LastEditTime: 2021-05-15 09:30:15
FilePath: /leetcode/653.两数之和-iv-输入-bst.py
'''
#
# @lc app=leetcode.cn id=653 lang=python
#
# [653] 两数之和 IV - 输入 BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        BFS+HashSet
        """
        hs = set()
        q = []
        q.append(root)
        # hs.add(root.val)

        while q:
            sz = len(q)
            for i in range(sz):
                cur = q.pop(0)
                if k - cur.val in hs:
                    return True
                hs.add(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        return False
                
    def findTarget1(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        先中序遍历，再双指针
        """
        res = []
        def help(root):
            if not root:
                return
            help(root.left)
            res.append(root.val)
            help(root.right)

        help(root)
        # print(res)

        left, right = 0, len(res)-1
        while left < right:
            
            if res[left] + res[right] == k:
                return True  

            elif res[left] + res[right] < k:
                left = left + 1

            else:
                right = right - 1

        return False     
        
# @lc code=end

