#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File:       剑指 Offer II 024. 反转链表.py
@Time:       2021/08/30 08:39:06
@Author:     Yuxiang Yang
@Version:    1.0
@Describe:   
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList0(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last