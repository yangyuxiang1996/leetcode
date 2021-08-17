#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-08-16 07:19:43
LastEditors: Yuxiang Yang
LastEditTime: 2021-08-16 07:26:34
FilePath: /leetcode/剑指 Offer 24. 反转链表.py
Description: 
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last


    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        
        dummy = None
        while head:
            cur = head
            head = head.next
            cur.next = dummy
            dummy = cur
        return dummy
