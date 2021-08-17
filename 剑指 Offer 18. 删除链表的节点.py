#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-16 07:27:34
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-16 07:44:09
FilePath: /leetcode/剑指 Offer 18. 删除链表的节点.py
Description: 
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。
返回删除后的链表的头节点。
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        if head.val == val:
            return head.next
        
        head.next = self.deleteNode(head.next, val)
        return head
        
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        
        dummy = ListNode(0)
        dummy.next = head
        pre, cur = dummy, head
        while cur and cur.val != val:
            pre = pre.next
            cur = cur.next
        
        pre.next = pre.next.next
        return dummy.next

    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return None
        if head.val == val:
            return head.next

        fast, slow = head.next, head
        while fast and fast.val != val:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head


