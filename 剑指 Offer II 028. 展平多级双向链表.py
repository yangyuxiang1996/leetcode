#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-30 21:13:23
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-30 21:41:21
FilePath: /leetcode/剑指 Offer II 028. 展平多级双向链表.py
Description: 
多级双向链表中，除了指向下一个节点和前一个节点指针之外，它还有一个子链表指针，可能指向单独的双向链表。这些子列表也可能会有一个或多个自己的子项，依此类推，生成多级数据结构，如下面的示例所示。
给定位于列表第一级的头节点，请扁平化列表，即将这样的多级双向链表展平成普通的双向链表，使所有结点出现在单级双链表中。
'''
"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        dummy = Node(0, None, head, None)
        pre = dummy
        cur = head
        stack = [cur]
        while stack:
            cur = stack.pop()
            pre.next = cur
            cur.prev = pre

            if cur.next:
                stack.append(cur.next)
            
            if cur.child:
                stack.append(cur.child)
                cur.child = None
            
            pre = cur
        
        dummy.next.prev = None
        return dummy.next





        



