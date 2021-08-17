#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-17 10:15:00
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-17 11:13:43
FilePath: /leetcode/剑指 Offer 36. 二叉搜索树与双向链表.py
Description: 
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。
'''
"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.inorder_list = []
    
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.inorder_list.append(root)
        self.inorder(root.right)
    
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # 递归
        def helper(root):
            if not root:
                return
            helper(root.left)
            if inorder_list:
                inorder_list[-1].right = root
                root.left = inorder_list[-1]
            inorder_list.append(root)
            helper(root.right)
        
        inorder_list = []
        helper(root)
        inorder_list[0].left, inorder_list[-1].right = inorder_list[-1], inorder_list[0]
        return inorder_list[0]
        
    def treeToDoublyList0(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # 递归中序遍历，将节点保存在list中，遍历list修改节点指针
        if not root:
            return None
        
        self.inorder(root)
        n = len(self.inorder_list)
        self.inorder_list[0].left = self.inorder_list[-1]
        self.inorder_list[-1].right = self.inorder_list[0]
        for i in range(n-1):
            self.inorder_list[i].right = self.inorder_list[i+1]
            self.inorder_list[i+1].left = self.inorder_list[i]
        return self.inorder_list[0]

    def treeToDoublyList1(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # 迭代中序遍历，将节点保存在list中，遍历list修改节点指针
        if not root:
            return None
        
        stack = []
        inorder_list = []
        cur = root
        while cur is not None or stack != []:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            inorder_list.append(cur)
            cur = cur.right        
            
        n = len(inorder_list)
        inorder_list[0].left = inorder_list[-1]
        inorder_list[-1].right = inorder_list[0]
        for i in range(n-1):
            inorder_list[i].right = inorder_list[i+1]
            inorder_list[i+1].left = inorder_list[i]
        return inorder_list[0]

    def treeToDoublyList2(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # 迭代中序遍历，将节点保存在list中，一边迭代一边修改指针
        if not root:
            return None
        
        stack = []
        inorder_list = []
        tmp = root
        
        while tmp is not None or stack != []:
            while tmp:
                stack.append(tmp)
                tmp = tmp.left
            tmp = stack.pop()
            if inorder_list:
                inorder_list[-1].right = tmp
                tmp.left = inorder_list[-1]
            inorder_list.append(tmp)
        inorder_list[0].left, inorder_list[-1].right = inorder_list[-1], inorder_list[0]
        return inorder_list[0]


    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # 迭代中序遍历，双指针，原地修改节点指向
        if not root:
            return None
        
        stack = []
        tmp = root
        pre = head = None
        
        while tmp is not None or stack != []:
            while tmp:
                stack.append(tmp)
                tmp = tmp.left
            tmp = stack.pop()
            if pre:
                pre.right = tmp
                tmp.left = pre
            else:
                head = tmp
            pre = tmp
            tmp = tmp.right   
        
        head.left = pre
        pre.right = head
        return head
        
        
                    

